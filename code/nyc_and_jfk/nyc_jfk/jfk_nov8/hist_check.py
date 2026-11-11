"""Calc E: 2021-22 United JFK entry (JFK-LAX, JFK-SFO) vs JetBlue share and fares.
Inputs: src/t100_panel_jfk_transcon_hub_routes_2019_2026m7.csv (T-100, class F, both directions)
        src/dot_car_table1a_jfk_ewr_2019_2026q1.csv (DOT Consumer Airfare Report Table 1a)
        src/t100_ua_jfk_monthly_by_aircraft_2021_2022.csv
Periods (rules fixed before looking at results):
  PRE  = 2019 Q1-Q4 (2020 excluded, COVID)
  UA   = 2021Q3-2022Q3 (first and last full quarters of UA's ~2 daily round trips per route;
         UA began late Mar 2021 and its last flights were Oct 2022 per T-100 monthly data)
  POST = 2023Q1-2024Q4
Treated: JFK-LAX, JFK-SFO. Controls: JFK-SEA, LAS, SAN, PHX, SLC (JetBlue transcons/west routes UA did not fly).
DiD on JetBlue passenger share (pp) and on fares (log points), same-quarter matched to PRE (seasonality).
"""
import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../..')  # repo root
import pandas as pd, numpy as np, json
P = pd.read_csv(_os.path.join(_R, 'data/nyc_and_jfk/raw/jfk/t100_panel_jfk_transcon_hub_routes_2019_2026m7.csv'))
F = pd.read_csv(_os.path.join(_R, 'data/nyc_and_jfk/raw/jfk/dot_car_table1a_jfk_ewr_2019_2026q1.csv'))
U = pd.read_csv(_os.path.join(_R, 'data/nyc_and_jfk/raw/jfk/t100_ua_jfk_monthly_by_aircraft_2021_2022.csv'))
TREAT = ['LAX', 'SFO']; CTRL = ['SEA', 'LAS', 'SAN', 'PHX', 'SLC']
J = P[P.hub == 'JFK'].copy()
J['yq'] = J.year * 10 + J.quarter
tot = J.groupby(['x', 'yq']).agg(tot_pax=('pax', 'sum'), tot_seats=('seats', 'sum')).reset_index()
def car(c):
    d = J[J.carrier == c].groupby(['x', 'yq'])[['pax', 'seats', 'deps']].sum().add_prefix(c + '_').reset_index()
    return d
R = tot
for c in ['B6', 'UA', 'DL', 'AA', 'AS']:
    R = R.merge(car(c), on=['x', 'yq'], how='left')
R = R.fillna(0)
R['B6_share'] = R.B6_pax / R.tot_pax * 100
R['UA_share'] = R.UA_pax / R.tot_pax * 100
R['B6_seat_share'] = R.B6_seats / R.tot_seats * 100
R['B6_LF'] = np.where(R.B6_seats > 0, R.B6_pax / R.B6_seats * 100, np.nan)
R['year'] = R.yq // 10; R['quarter'] = R.yq % 10

def period(yq):
    if 20191 <= yq <= 20194: return 'PRE'
    if 20213 <= yq <= 20223: return 'UA'
    if 20231 <= yq <= 20244: return 'POST'
    return None
R['period'] = R.yq.apply(period)

# fares: Table 1a, JFK pairs
F['x'] = np.where(F.airport_1 == 'JFK', F.airport_2, np.where(F.airport_2 == 'JFK', F.airport_1, None))
F['yq'] = F.year * 10 + F.quarter
FJ = F[F.x.notna() & F.x.isin(TREAT + CTRL)].copy()
FJ['b6_fare'] = np.where(FJ.carrier_lg == 'B6', FJ.fare_lg, np.where(FJ.carrier_low == 'B6', FJ.fare_low, np.nan))
R = R.merge(FJ[['x', 'yq', 'fare', 'b6_fare', 'passengers_per_day', 'carrier_lg', 'carrier_low']], on=['x', 'yq'], how='left')
R['group'] = np.where(R.x.isin(TREAT), 'treated', np.where(R.x.isin(CTRL), 'control', 'other'))
R = R[R.group != 'other']
R.sort_values(['x', 'yq']).to_csv(_os.path.join(_R, 'data/air_traffic_dot_bts/processed/hist_route_quarter_panel.csv'), index=False)

# --- DiD on JetBlue share (quarter-matched to 2019) ---
pre = R[R.period == 'PRE'].set_index(['x', 'quarter'])
def did(var, per, log=False):
    d = R[R.period == per].copy()
    base = pre[var]
    d['base'] = [base.get((x, q), np.nan) for x, q in zip(d.x, d.quarter)]
    if log: d['chg'] = np.log(d[var]) - np.log(d['base'])
    else: d['chg'] = d[var] - d['base']
    g = d.groupby('group').chg.mean()
    byroute = d.groupby('x').chg.mean()
    return g.get('treated', np.nan) - g.get('control', np.nan), g.to_dict(), byroute.to_dict()

out = {}
for v, lg in [('B6_share', False), ('B6_seat_share', False), ('B6_LF', False), ('fare', True)]:
    for per in ['UA', 'POST']:
        out[f'{v}_{per}'] = did(v, per, lg)
# B6 fare only shown in some quarters: LAX vs controls where shown
out['b6_fare_UA'] = did('b6_fare', 'UA', True); out['b6_fare_POST'] = did('b6_fare', 'POST', True)

# market growth: total route pax change vs 2019 same quarter (log), treated vs control
out['tot_pax_UA'] = did('tot_pax', 'UA', True); out['tot_pax_POST'] = did('tot_pax', 'POST', True)

# UA operating stats 2021-22
U['yq'] = U.year * 10 + (U.month + 2) // 3
ua = U.groupby('x')[['pax', 'seats', 'deps']].sum()
ua['seats_per_dep'] = ua.seats / ua.deps; ua['LF'] = ua.pax / ua.seats * 100
ua_full = U[(U.year * 100 + U.month >= 202107) & (U.year * 100 + U.month <= 202209)]
uaf = ua_full.groupby('x')[['pax', 'seats', 'deps']].sum()
uaf['LF'] = uaf.pax / uaf.seats * 100; uaf['seats_per_dep'] = uaf.seats / uaf.deps
uaf['daily_rt'] = uaf.deps / 2 / 456   # Jul 1 2021 - Sep 30 2022 = 457 days
out['ua_ops_all'] = ua.round(2).to_dict('index'); out['ua_ops_jul21_sep22'] = uaf.round(3).to_dict('index')
ac = U.groupby(['actype'])[['deps']].sum().to_dict()['deps']; out['ua_aircraft_deps'] = ac

# headline period averages
summ = R[R.period.notna()].groupby(['x', 'period'])[['B6_share', 'UA_share', 'B6_seat_share', 'B6_LF', 'fare', 'b6_fare', 'tot_pax', 'B6_pax']].mean()
summ.round(2).to_csv(_os.path.join(_R, 'data/air_traffic_dot_bts/processed/hist_period_means.csv'))
_od = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'out'); _os.makedirs(_od, exist_ok=True)  # archive/jfk_nov8/ no longer in repo
json.dump(out, open(_os.path.join(_od, 'hist_check.json'), 'w'), indent=1, default=float)

# chart-ready CSV: by quarter, treated routes + control average
rows = []
for yq, d in R.groupby('yq'):
    t = d[d.group == 'treated']; c = d[d.group == 'control']
    row = dict(year=yq // 10, quarter=yq % 10, period=period(yq) or ('COVID/transition'))
    for x in TREAT:
        s = d[d.x == x]
        if len(s):
            s = s.iloc[0]
            row.update({f'{x}_UA_pax': s.UA_pax, f'{x}_UA_share_pct': round(s.UA_share, 2), f'{x}_B6_pax': s.B6_pax,
                        f'{x}_B6_share_pct': round(s.B6_share, 2), f'{x}_route_pax': s.tot_pax,
                        f'{x}_avg_fare_t1a': s.fare, f'{x}_B6_fare_t1a_if_shown': s.b6_fare})
    row['control_avg_B6_share_pct'] = round(c.B6_share.mean(), 2)
    row['control_avg_fare_t1a'] = round(c.fare.mean(), 2) if c.fare.notna().any() else np.nan
    rows.append(row)
H = pd.DataFrame(rows)
H = H[(H.year != 2020)]
H.to_csv(_os.path.join(_R, 'data/air_traffic_dot_bts/processed/csv3_2021_22_united_jfk_entry_vs_jetblue.csv'), index=False)
print(summ.round(2).to_string())
for k, v in out.items(): print(k, v)
