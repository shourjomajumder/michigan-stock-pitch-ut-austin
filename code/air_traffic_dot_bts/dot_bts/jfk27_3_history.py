"""Agent 3: refined historical test of United at JFK (2021-22 entry/exit, 2015 exit).
Reuses inputs of hist_check.py (read-only):
  ../raw/t100/t100_panel_jfk_transcon_hub_routes_2019_2026m7.csv  (BTS T-100 segment, class F, both directions, quarterly)
  ../raw/dot_car_table1a/dot_car_table1a_jfk_ewr_2019_2026q1.csv             (DOT Consumer Airfare Report Table 1a)
  ../raw/t100/t100_ua_jfk_monthly_by_aircraft_2021_2022.csv
  ../raw/t100/t100_bos_jfk_ewr_transcon_monthly_2019_2026.csv  (BTS T-100 monthly, JFK/EWR/BOS - LAX/SFO, 2019-01..2024-04)
  vx_table6_values.py  (DOT Table 6 city-market values 2015Q1-2020Q4, typed from data.transportation.gov yj5y-b2ir)
Writes only ../processed/jfk27_3_*.csv
Design choices fixed before results (same as hist_check.py where it overlaps):
  treated JFK-LAX, JFK-SFO; controls JFK-SEA, LAS, SAN, PHX, SLC (alt: + DEN, ORD, IAH, which UA never flew from JFK)
  sample quarters 2019Q1-2019Q4, 2021Q1-2026Q2 (2020 COVID dropped; 2026Q3 = July only, dropped)
  dose = United seat share of route seats (pp). FE = route x quarter-of-year (seasonality) + calendar quarter.
"""
import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd, numpy as np, itertools, re, ast
rng = np.random.default_rng(20261111)
SRC = _os.path.join(_R, 'data/air_traffic_dot_bts/raw/')
OUT = _os.path.join(_R, 'data/air_traffic_dot_bts/processed/jfk27_3_')
TREAT = ['LAX', 'SFO']; CTRL = ['SEA', 'LAS', 'SAN', 'PHX', 'SLC']; CTRL_ALT = CTRL + ['DEN', 'ORD', 'IAH']
CARS = ['B6', 'UA', 'DL', 'AA', 'AS', 'OT']

# ---------------- quarterly panel ----------------
P = pd.read_csv(_os.path.join(_R, 'data/air_traffic_dot_bts/raw/t100/') + 't100_panel_jfk_transcon_hub_routes_2019_2026m7.csv')
J = P[P.hub == 'JFK'].copy()
J['yq'] = J.year * 10 + J.quarter
w = J.pivot_table(index=['x', 'year', 'quarter', 'yq'], columns='carrier', values=['pax', 'seats', 'deps'], aggfunc='sum').fillna(0)
w.columns = [f'{c}_{m}' for m, c in w.columns]
R = w.reset_index()
for c in CARS:
    for m in ['pax', 'seats', 'deps']:
        if f'{c}_{m}' not in R: R[f'{c}_{m}'] = 0.0
R['tot_pax'] = R[[f'{c}_pax' for c in CARS]].sum(1); R['tot_seats'] = R[[f'{c}_seats' for c in CARS]].sum(1)
for c in CARS:
    R[f'{c}_share'] = R[f'{c}_pax'] / R.tot_pax * 100
    R[f'{c}_seat_share'] = R[f'{c}_seats'] / R.tot_seats * 100
R['B6_LF'] = np.where(R.B6_seats > 0, R.B6_pax / R.B6_seats * 100, np.nan)
R['route_LF'] = R.tot_pax / R.tot_seats * 100
R['B6AA_share'] = R.B6_share + R.AA_share   # NEA partners Jul 2021 - Jul 2023
F = pd.read_csv(_os.path.join(_R, 'data/air_traffic_dot_bts/raw/dot_car_table1a/dot_car_table1a_jfk_ewr_2019_2026q1.csv'))
F = F[(F.airport_1 == 'JFK') | (F.airport_2 == 'JFK')].copy()
F['x'] = np.where(F.airport_1 == 'JFK', F.airport_2, F.airport_1)
F['b6_fare'] = np.where(F.carrier_lg == 'B6', F.fare_lg, np.where(F.carrier_low == 'B6', F.fare_low, np.nan))
F['dl_fare'] = np.where(F.carrier_lg == 'DL', F.fare_lg, np.where(F.carrier_low == 'DL', F.fare_low, np.nan))
R = R.merge(F[['x', 'year', 'quarter', 'fare', 'b6_fare', 'dl_fare', 'carrier_lg', 'large_ms', 'carrier_low', 'lf_ms']],
            on=['x', 'year', 'quarter'], how='left')
R['group'] = np.select([R.x.isin(TREAT), R.x.isin(CTRL)], ['treated', 'control'], 'control_alt')
R = R.sort_values(['x', 'yq'])
def per(yq):
    if 20191 <= yq <= 20194: return 'PRE_2019'
    if 20211 <= yq <= 20212: return 'RAMP_2021H1'
    if 20213 <= yq <= 20223: return 'UA_2021Q3_2022Q3'
    if yq == 20224: return 'EXIT_2022Q4'
    if 20231 <= yq <= 20244: return 'POST_2023_24'
    if 20251 <= yq <= 20262: return 'LATE_2025_26H1'
    return 'partial_2026Q3'
R['period'] = R.yq.apply(per)
keep = ['x', 'group', 'year', 'quarter', 'period', 'tot_pax', 'tot_seats', 'route_LF'] + \
       [f'{c}_{m}' for c in ['B6', 'UA', 'DL', 'AA', 'AS'] for m in ['pax', 'seats', 'deps', 'share', 'seat_share']] + \
       ['B6_LF', 'B6AA_share', 'fare', 'b6_fare', 'dl_fare', 'carrier_lg', 'large_ms', 'carrier_low', 'lf_ms']
R[keep].round(3).to_csv(OUT + 'quarterly_panel_2019_2026.csv', index=False)

# treated vs control average, by quarter (chart-ready)
qrows = []
for yq, d in R[R.period != 'partial_2026Q3'].groupby('yq'):
    row = dict(year=yq // 10, quarter=yq % 10, period=per(yq))
    for x in TREAT:
        s = d[d.x == x].iloc[0]
        for v in ['UA_seat_share', 'UA_share', 'B6_share', 'B6_seat_share', 'B6_LF', 'DL_share', 'AA_share', 'AS_share', 'fare', 'B6_pax', 'UA_seats', 'tot_pax']:
            row[f'{x}_{v}'] = s[v]
    c = d[d.group == 'control']
    for v in ['B6_share', 'B6_seat_share', 'B6_LF', 'DL_share', 'AA_share', 'fare']:
        row[f'CTRL5_avg_{v}'] = c[v].mean()
    qrows.append(row)
pd.DataFrame(qrows).round(2).to_csv(OUT + 'quarterly_treated_vs_control.csv', index=False)

# ---------------- monthly (treated routes + BOS/EWR comparison), 2019-01..2024-04 ----------------
T = pd.read_csv(_os.path.join(_R, 'data/air_traffic_dot_bts/raw/t100/t100_bos_jfk_ewr_transcon_monthly_2019_2026.csv'))
T['pax'] = pd.to_numeric(T.pax, errors='coerce'); T['deps'] = pd.to_numeric(T.deps, errors='coerce')
T = T.dropna(subset=['pax'])
T['c'] = np.where(T.carrier.isin(['B6', 'UA', 'DL', 'AA', 'AS']), T.carrier, 'OT')
M = T.pivot_table(index=['route', 'year', 'month'], columns='c', values=['pax', 'seats'], aggfunc='sum').fillna(0)
M.columns = [f'{c}_{m}' for m, c in M.columns]; M = M.reset_index()
M['tot_pax'] = M.filter(like='_pax').sum(1); M['tot_seats'] = M.filter(like='_seats').sum(1)
for c in ['B6', 'UA', 'DL', 'AA', 'AS']:
    M[f'{c}_share'] = M[f'{c}_pax'] / M.tot_pax * 100; M[f'{c}_seat_share'] = M[f'{c}_seats'] / M.tot_seats * 100
M['B6_LF'] = M.B6_pax / M.B6_seats * 100
M = M[~((M.year == 2024) & (M.month == 4) & (M.tot_pax < 0.5 * M.groupby('route').tot_pax.transform('median')))]  # drop truncated row if any
M.round(3).to_csv(OUT + 'monthly_lax_sfo_2019_2024m4.csv', index=False)

# ---------------- estimation helpers ----------------
S = R[(R.period != 'partial_2026Q3')].copy()
def twfe(d, y, x, routes):
    d = d[d.x.isin(routes)].dropna(subset=[y, x]).copy()
    d['rq'] = d.x + '_' + d.quarter.astype(str)
    X = pd.get_dummies(d[['rq']].astype(str), drop_first=False).astype(float)
    X = pd.concat([X, pd.get_dummies(d.yq.astype(str), prefix='t', drop_first=True).astype(float)], axis=1)
    X.insert(0, 'dose', d[x].values)
    A = X.values; b = d[y].values
    coef, *_ = np.linalg.lstsq(A, b, rcond=None)
    resid = b - A @ coef
    return coef[0], d, A, b, resid, coef

def wild_cluster(d, A, b, coef, reps=4999):
    """Webb 6-point wild cluster bootstrap by route (unrestricted). Few treated clusters -> treat as indicative only."""
    fit = A @ coef; res = b - fit; cl = d.x.values; ucl = np.unique(cl)
    webb = np.array([-np.sqrt(1.5), -1, -np.sqrt(.5), np.sqrt(.5), 1, np.sqrt(1.5)])
    pinv = np.linalg.pinv(A)[0]
    out = np.empty(reps)
    for r in range(reps):
        wv = dict(zip(ucl, rng.choice(webb, len(ucl))))
        out[r] = pinv @ (fit + res * np.array([wv[c] for c in cl]))
    return np.percentile(out, [2.5, 97.5])

def dose_path(d, x):
    return {r: g.set_index('yq')[x] for r, g in d.groupby('x')}

def placebo_routes(dfull, y, x, routes, beta_hat):
    """Randomization inference: move the LAX and SFO United dose paths onto every ordered pair of routes."""
    base = dfull[dfull.x.isin(routes)].copy()
    paths = {t: base[base.x == t].set_index('yq')[x] for t in TREAT}
    ests = []
    for a, bb in itertools.permutations(routes, 2):
        d = base.copy(); d['pdose'] = 0.0
        for tgt, src in [(a, 'LAX'), (bb, 'SFO')]:
            m = d.x == tgt
            d.loc[m, 'pdose'] = d.loc[m, 'yq'].map(paths[src]).fillna(0).values
        # actual treated routes keep their true dose only if they are assigned; otherwise dose removed -> partial out real dose as control
        d['real'] = np.where(d.x.isin(TREAT), d[x], 0.0)
        if set([a, bb]) == set(TREAT):
            e = twfe(d.assign(pd_=d.pdose), y, 'pd_', routes)[0]
        else:
            # include real dose as a covariate so the true effect does not contaminate the placebo
            dd = d.dropna(subset=[y]).copy(); dd['rq'] = dd.x + '_' + dd.quarter.astype(str)
            X = pd.get_dummies(dd[['rq']].astype(str)).astype(float)
            X = pd.concat([X, pd.get_dummies(dd.yq.astype(str), prefix='t', drop_first=True).astype(float)], axis=1)
            X.insert(0, 'real', dd.real.values); X.insert(0, 'pd', dd.pdose.values)
            e = np.linalg.lstsq(X.values, dd[y].values, rcond=None)[0][0]
        ests.append(((a, bb), e))
    vals = np.array([e for k, e in ests if set(k) != set(TREAT)])
    p = (np.sum(np.abs(vals) >= abs(beta_hat)) + 1) / (len(vals) + 1)
    return vals, p

def placebo_time(dfull, y, x, routes):
    """In-time placebo: put the real 2021Q1-2022Q4 dose profile on LAX/SFO in windows with no United (2023Q1 onward)."""
    qs = sorted(dfull.yq.unique()); real_q = [q for q in qs if 20211 <= q <= 20224]
    post = [q for q in qs if q >= 20231]
    ests = []
    for s in range(0, len(post) - len(real_q) + 1):
        win = post[s:s + len(real_q)]
        d = dfull[dfull.x.isin(routes) & ((dfull.yq < 20211) | (dfull.yq >= 20231))].copy()  # drop real UA era
        d['pd'] = 0.0
        for t in TREAT:
            prof = dfull[(dfull.x == t)].set_index('yq')[x].reindex(real_q).values
            for q, v in zip(win, prof):
                d.loc[(d.x == t) & (d.yq == q), 'pd'] = v
        ests.append(twfe(d, y, 'pd', routes)[0])
    return np.array(ests)

def ri_ci(dfull, y, x, routes, grid):
    """Confidence set by inverting the route-placebo test (Fisher-style, additive constant effect)."""
    acc = []
    for b0 in grid:
        d = dfull.copy(); d['y0'] = d[y] - b0 * np.where(d.x.isin(TREAT), d[x], 0)
        e0 = twfe(d, 'y0', x, routes)[0]
        vals, p = placebo_routes(d, 'y0', x, routes, e0)
        if p > 0.05: acc.append(b0)
    return (min(acc), max(acc)) if acc else (np.nan, np.nan)

# scaled outcomes for capacity effect: pax per 2019 same-quarter route total
base19 = S[S.year == 2019].set_index(['x', 'quarter']).tot_pax
S['scale'] = [base19.get((a, q), np.nan) for a, q in zip(S.x, S.quarter)]
for c in ['B6', 'DL', 'AA', 'AS', 'UA']:
    S[f'{c}_pax_s'] = S[f'{c}_pax'] / S.scale
S['tot_pax_s'] = S.tot_pax / S.scale; S['UA_seats_s'] = S.UA_seats / S.scale
S['ln_fare'] = np.log(S.fare) * 100; S['ln_b6_fare'] = np.log(S.b6_fare) * 100

results = []
def run(label, y, x, routes, scale=1.0, unit='', ci_inv=False, grid=None):
    bh, d, A, b, res, coef = twfe(S, y, x, routes)
    wcb = wild_cluster(d, A, b, coef)
    pv, p = placebo_routes(S, y, x, routes, bh)
    tv = placebo_time(S, y, x, routes)
    row = dict(estimate=label, y=y, dose=x, controls='5 (SEA,LAS,SAN,PHX,SLC)' if routes == TREAT + CTRL else '8 (+DEN,ORD,IAH)',
               beta=bh, scale=scale, effect=bh * scale, unit=unit, n_obs=len(d),
               wcb_lo=wcb[0] * scale, wcb_hi=wcb[1] * scale,
               route_placebo_p=p, route_placebo_sd=np.std(pv) * scale, route_placebo_n=len(pv),
               time_placebo_sd=np.std(tv) * scale, time_placebo_mean=np.mean(tv) * scale, time_placebo_n=len(tv),
               time_placebo_min=np.min(tv) * scale, time_placebo_max=np.max(tv) * scale)
    # combined placebo SE (route and time noise) -> normal 90/95% bands
    se = np.sqrt(np.var(pv) + np.var(tv)) / np.sqrt(2) * scale
    row['placebo_se'] = se; row['ci95_lo'] = row['effect'] - 1.96 * se; row['ci95_hi'] = row['effect'] + 1.96 * se
    if ci_inv:
        lo, hi = ri_ci(S, y, x, routes, grid); row['ri_ci95_lo'] = lo * scale; row['ri_ci95_hi'] = hi * scale
    results.append(row); return row

R5 = TREAT + CTRL; R8 = TREAT + CTRL_ALT
grid = np.arange(-1.5, 1.51, 0.02)
# share effects, per 10 pp of United seat share
for c in ['B6', 'DL', 'AA', 'AS', 'B6AA']:
    for rs in [R5, R8]:
        run(f'{c} pax share pp per +10pp UA seat share', f'{c}_share', 'UA_seat_share', rs, 10, 'share pp',
            ci_inv=(c == 'B6' and rs == R5), grid=grid)
run('B6 seat share pp per +10pp UA seat share', 'B6_seat_share', 'UA_seat_share', R5, 10, 'share pp')
run('B6 load factor pts per +10pp UA seat share', 'B6_LF', 'UA_seat_share', R5, 10, 'LF pts')
run('Route LF pts per +10pp UA seat share', 'route_LF', 'UA_seat_share', R5, 10, 'LF pts')
# capacity effect: passengers per United seat
for c in ['B6', 'DL', 'AA', 'AS', 'tot']:
    for rs in [R5, R8]:
        run(f'{c} pax change per United seat', f'{c}_pax_s', 'UA_seats_s', rs, 1, 'pax per UA seat')
run('UA pax per UA seat (check = UA LF)', 'UA_pax_s', 'UA_seats_s', R5, 1, 'pax per UA seat')
# price effect (log points per +10pp UA seat share); Table 1a fares exist only for the 5 controls before 2025Q2
run('Route avg fare log pts per +10pp UA seat share', 'ln_fare', 'UA_seat_share', R5, 10, 'log pts (~%)')
Res = pd.DataFrame(results)
Res.round(4).to_csv(OUT + 'did_dose_results.csv', index=False)

# ---------------- classic period DiD (vs 2019 same quarter), with placebo over route pairs ----------------
def period_did(var, period, routes=R5, log=False):
    pre = S[S.year == 2019].set_index(['x', 'quarter'])[var]
    d = S[(S.period == period) & S.x.isin(routes)].copy()
    d['b'] = [pre.get((a, q), np.nan) for a, q in zip(d.x, d.quarter)]
    d['chg'] = (np.log(d[var]) - np.log(d.b)) * 100 if log else d[var] - d.b
    byr = d.groupby('x').chg.mean()
    est = byr[TREAT].mean() - byr[[r for r in routes if r not in TREAT]].mean()
    pl = [byr[list(p)].mean() - byr[[r for r in routes if r not in p]].mean() for p in itertools.combinations(routes, 2) if set(p) != set(TREAT)]
    p = (np.sum(np.abs(pl) >= abs(est)) + 1) / (len(pl) + 1)
    # bootstrap: resample control routes and quarters within period
    bs = []
    ctrl = [r for r in routes if r not in TREAT]; qs = d.yq.unique()
    for _ in range(4999):
        qq = rng.choice(qs, len(qs)); cc = rng.choice(ctrl, len(ctrl)); tt = rng.choice(TREAT, 2)
        dd = pd.concat([d[d.yq == q] for q in qq]); g = dd.groupby('x').chg.mean()
        bs.append(g.reindex(tt).mean() - g.reindex(cc).mean())
    lo, hi = np.nanpercentile(bs, [2.5, 97.5])
    return dict(var=var, period=period, did=est, LAX=byr.get('LAX'), SFO=byr.get('SFO'), ctrl_mean=byr[ctrl].mean(),
                ctrl_min=byr[ctrl].min(), ctrl_max=byr[ctrl].max(), placebo_p=p, placebo_sd=np.std(pl), n_placebo=len(pl),
                boot_lo=lo, boot_hi=hi)
pd_rows = []
for v, lg in [('B6_share', 0), ('B6_seat_share', 0), ('B6_LF', 0), ('DL_share', 0), ('AA_share', 0), ('AS_share', 0), ('B6AA_share', 0),
              ('UA_seat_share', 0), ('fare', 1), ('tot_pax', 1), ('B6_pax', 1)]:
    for perd in ['RAMP_2021H1', 'UA_2021Q3_2022Q3', 'EXIT_2022Q4', 'POST_2023_24', 'LATE_2025_26H1']:
        pd_rows.append(period_did(v, perd, log=bool(lg)))
PD = pd.DataFrame(pd_rows); PD.round(3).to_csv(OUT + 'did_period_vs2019.csv', index=False)

# ---------------- exit test: 2022Q3 (UA in) -> 2023Q1-Q2/2023 (UA out), first difference vs controls ----------------
def exit_did(var):
    a = S[S.yq.isin([20223, 20221, 20222])].set_index(['x', 'quarter'])[var]
    b = S[S.yq.isin([20233, 20231, 20232])].set_index(['x', 'quarter'])[var]
    ch = (b - a).groupby('x').mean()
    est = ch[TREAT].mean() - ch[CTRL].mean()
    pl = [ch[list(p)].mean() - ch[[r for r in R5 if r not in p]].mean() for p in itertools.combinations(R5, 2) if set(p) != set(TREAT)]
    return dict(var=var, window='2022Q1-Q3 (UA in) -> 2023Q1-Q3 (UA out)', did=est, LAX=ch['LAX'], SFO=ch['SFO'],
                ctrl_mean=ch[CTRL].mean(), placebo_sd=np.std(pl), placebo_p=(np.sum(np.abs(pl) >= abs(est)) + 1) / (len(pl) + 1))
EX = pd.DataFrame([exit_did(v) for v in ['UA_seat_share', 'B6_share', 'DL_share', 'AA_share', 'AS_share', 'B6_seat_share', 'B6_LF', 'fare']])
EX.round(3).to_csv(OUT + 'did_exit_2022_23.csv', index=False)

# ---------------- monthly event study: JFK-LAX/SFO vs BOS-LAX/SFO (BOS had United throughout) ----------------
Mm = M[M.route.isin(['JFK-LAX', 'JFK-SFO', 'BOS-LAX', 'BOS-SFO'])].copy()
b19 = Mm[Mm.year == 2019].set_index(['route', 'month']).B6_share
Mm['chg'] = Mm.B6_share - [b19.get((r, m)) for r, m in zip(Mm.route, Mm.month)]
Mm['ym'] = Mm.year * 100 + Mm.month
ev = Mm.pivot_table(index='ym', columns='route', values='chg')
ev['JFK_minus_BOS_B6_share_chg_vs2019'] = ev[['JFK-LAX', 'JFK-SFO']].mean(1) - ev[['BOS-LAX', 'BOS-SFO']].mean(1)
uas = M[M.route.isin(['JFK-LAX', 'JFK-SFO'])].pivot_table(index=['year', 'month'], columns='route', values='UA_seat_share')
uas.index = [y * 100 + m for y, m in uas.index]
ev = ev.join(uas.add_suffix('_UA_seat_share'))
ev.round(2).to_csv(OUT + 'monthly_event_jfk_vs_bos.csv')
mon = {}
for lab, lo, hi in [('UA_full_202107_202209', 202107, 202209), ('post_202301_202404', 202301, 202404)]:
    mon[lab] = ev.loc[(ev.index >= lo) & (ev.index <= hi), 'JFK_minus_BOS_B6_share_chg_vs2019'].mean()

# ---------------- 2015 exit: DOT Table 6 city markets (only largest & lowest-fare carrier shown) ----------------
src = open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'vx_table6_values.py')).read()
blk = src[src.index('S={'):src.index('city={')]
nan = np.nan
Sdict = eval(blk[2:].strip().rstrip(','), {'nan': np.nan})
Q = [f"{y}Q{q}" for y in range(2015, 2021) for q in range(1, 5)]
rows = []
for (route, car, meas), v in Sdict.items():
    if route in ('NYC-SFO', 'LAX-NYC', 'BOS-SFO', 'BOS-LAX'):
        for q, val in zip(Q[:12], v[:12]):
            rows.append(dict(city_market=route, carrier=car, measure=meas, quarter=q, share_pct=None if np.isnan(val) else round(val * 100, 2)))
E15 = pd.DataFrame(rows)
E15['source'] = 'DOT Consumer Airfare Report Table 6 (data.transportation.gov/resource/yj5y-b2ir), values from vx_table6_values.py'
_od = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'out'); _os.makedirs(_od, exist_ok=True)  # source label differs from data/ copy -> write here
E15.to_csv(_os.path.join(_od, 'jfk27_3_exit_2015_table6_city_markets.csv'), index=False)

# ---------------- print ----------------
pd.set_option('display.width', 250)
print(Res[['estimate', 'controls', 'effect', 'unit', 'wcb_lo', 'wcb_hi', 'route_placebo_p', 'route_placebo_sd', 'time_placebo_sd', 'placebo_se', 'ci95_lo', 'ci95_hi', 'ri_ci95_lo', 'ri_ci95_hi']].round(3).to_string())
print(PD[PD.period.isin(['UA_2021Q3_2022Q3', 'POST_2023_24', 'LATE_2025_26H1'])].round(2).to_string())
print(EX.round(2).to_string()); print('monthly JFK-BOS', mon)
print(E15.pivot_table(index=['city_market', 'carrier'], columns='quarter', values='share_pct').to_string())
