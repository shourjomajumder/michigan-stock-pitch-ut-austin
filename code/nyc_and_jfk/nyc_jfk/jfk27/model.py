"""Agent 8: JetBlue lost passengers and revenue on JFK-LAX / JFK-SFO from United's JFK return.
Quarterly 2026Q4 - 2030Q4; launch {2027Q2, 2027Q3, 2028Q1} x United capacity {low, base, high} = 9 scenarios.

(a) Same-airport switching: Blue Sky rate 3.1%/yr of JetBlue route pax, linear from United's launch quarter, cap 6%.
    From launch the route counts at 100% x fare-parity weight. The thesis already counts W_NY (10%) of these passengers
    (New York weight, building from Q4'26); that slice stays in the thesis and is not re-counted:
        incremental switching pax = pax x max(parity_w - W_NY, 0) x s(quarters since launch)
(b) Capacity effect: United pax x draw factor x JetBlue pre-entry route share (agent 4; = (1 - leakage), prior A5).
    Alternative (sensitivity): agent 3 per-seat estimate, JetBlue pax lost per United seat added.
    The prior run's A6 Delta-Alaska preference effect is NOT added: same loyalty mechanism as (a).
(c) Revenue = lost pax x JetBlue lowest economy fare (agent 5).  (d) JetBlue route pax: agent 2 / agent 7.
(a)+(b) are added (switchers are a preference shift on top of proportional draw, as in the prior run) and capped at
MAX_LOSS of JetBlue route pax; an overlap-adjusted variant max(a, b) is reported as a floor.
All inputs and sources: model_inputs.json.
"""
import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../..')  # repo root
import pandas as pd, json, os, copy
OUT = 'processed/jfk27'  # run from data_repo/nyc_jfk
P0 = json.load(open(os.path.join(OUT, _os.path.join(_R, 'data/nyc_and_jfk/processed/jfk27/model_inputs.json'))))
QTRS = [(2026, 4)] + [(y, q) for y in range(2027, 2031) for q in (1, 2, 3, 4)]
DAYS = {1: 90, 2: 91, 3: 92, 4: 92}
ROUTES = ('LAX', 'SFO')
def qi(yq): return yq[0] * 4 + yq[1] - 1
def qlab(yq): return f'{yq[0]}Q{yq[1]}'
def v(P, k): return P[k]['value']


def run(P, launch, cap, draw=None, per_seat=None):
    B6Q = {r: {int(q): x for q, x in d.items()} for r, d in v(P, 'b6_pax_by_qtr').items()}
    TOT = v(P, 'route_total_pax_L4Q')
    SH = {r: sum(B6Q[r].values()) / TOT[r] for r in ROUTES}
    rate, capsw, wny = v(P, 'switch_rate_per_yr'), v(P, 'switch_cap'), v(P, 'ny_weight')
    par, fare, g = v(P, 'fare_parity_weight'), v(P, 'fare'), v(P, 'b6_pax_growth_per_yr')
    chg, f1, mx = v(P, 'b6_capacity_change'), v(P, 'first_quarter_capacity_factor'), v(P, 'max_loss_share')
    C = v(P, 'capacity_scenarios')[cap]
    draw = v(P, 'draw_factor') if draw is None else draw
    start = tuple(v(P, 'thesis_build_start')); L = tuple(v(P, 'launch_scenarios')[launch])
    s = lambda k: 0.0 if k < 1 else min(rate * (k - 0.5) / 4, capsw)     # mid-quarter cumulative switched share
    rows = []
    for yq in QTRS:
        k, kt = qi(yq) - qi(L) + 1, qi(yq) - qi(start) + 1
        capf = 0.0 if k < 1 else (f1 if k == 1 else 1.0)
        for r in ROUTES:
            pax = B6Q[r][yq[1]] * (1 + g[r]) ** ((qi(yq) - qi((2026, 1))) / 4)   # L4Q midpoint ~2026Q1
            if r in chg and qi(yq) >= qi(tuple(chg[r]['from'])):
                pax *= chg[r]['factor']
            sw = pax * max(par[r] - wny, 0) * s(k)
            ua_seats = C['pairs'][r] * 2 * DAYS[yq[1]] * C['seats'] * capf
            ua_pax = ua_seats * C['lf']
            capl = ua_seats * per_seat if per_seat is not None else ua_pax * draw * SH[r]
            lost = min(sw + capl, mx * pax); sw_c = min(sw, lost); cap_c = lost - sw_c
            rows.append(dict(launch=launch, capacity=cap, quarter=qlab(yq), route='JFK-' + r, qtrs_since_launch=max(k, 0),
                             ua_capacity_factor=capf, switch_share=s(k), b6_pax=pax, ua_seats=ua_seats, ua_pax=ua_pax,
                             lost_pax_switching=sw_c, lost_pax_capacity=cap_c, lost_pax_total=lost,
                             lost_pax_overlap_floor=max(sw_c, cap_c), fare=fare[r],
                             lost_rev_switching_M=sw_c * fare[r] / 1e6, lost_rev_capacity_M=cap_c * fare[r] / 1e6,
                             lost_rev_M=lost * fare[r] / 1e6, lost_rev_overlap_floor_M=max(sw_c, cap_c) * fare[r] / 1e6,
                             lost_rev_at_t1a_avg_fare_M=lost * v(P, 'fare_t1a_all_cabin')[r] / 1e6,
                             memo_thesis_ny10_switch_pax=pax * wny * s(kt),
                             memo_A6_pref_pax_not_added=(0 if k < 1 else v(P, 'a6_pref_pts_crosscheck') / 100 * TOT[r] / 4 * min(k, 6) / 6)))
    return pd.DataFrame(rows)


NUM = ['b6_pax', 'ua_seats', 'ua_pax', 'lost_pax_switching', 'lost_pax_capacity', 'lost_pax_total', 'lost_pax_overlap_floor',
       'lost_rev_switching_M', 'lost_rev_capacity_M', 'lost_rev_M', 'lost_rev_overlap_floor_M', 'lost_rev_at_t1a_avg_fare_M',
       'memo_thesis_ny10_switch_pax', 'memo_A6_pref_pax_not_added']
def agg(R):
    Q = R.groupby(['launch', 'capacity', 'quarter'], sort=False)[NUM].sum().reset_index()
    Q.insert(0, 'scenario', Q.launch + '_' + Q.capacity)
    Q['cum_lost_rev_M'] = Q.groupby('scenario').lost_rev_M.cumsum()
    return Q


if __name__ == '__main__':
    P = P0
    R = pd.concat([run(P, l, c) for l in v(P, 'launch_scenarios') for c in v(P, 'capacity_scenarios')])
    R.round(4).to_csv(os.path.join(OUT, _os.path.join(_R, 'data/nyc_and_jfk/processed/jfk27/8_scenarios_by_route.csv')), index=False)
    Q = agg(R)
    out = Q.copy()
    for c in NUM + ['cum_lost_rev_M']:
        out[c] = out[c].round(0 if c.endswith('pax') or c in ('ua_seats',) else 3)
    out['lost_rev_sw60_M'] = 0.6 * out['lost_rev_switching_M']  # Thesis 2 probability weight P=0.60 (review agent 10); appended after the agent-8 run
    out.to_csv(os.path.join(OUT, _os.path.join(_R, 'data/nyc_and_jfk/processed/jfk27/8_scenarios.csv')), index=False)
    Q['year'] = Q.quarter.str[:4].astype(int)
    A = Q.groupby(['scenario', 'year'], sort=False)[['lost_pax_switching', 'lost_pax_capacity', 'lost_pax_total', 'lost_rev_M',
                                                     'lost_rev_switching_M', 'lost_rev_capacity_M', 'lost_rev_overlap_floor_M',
                                                     'lost_rev_at_t1a_avg_fare_M']].sum().reset_index()
    A.round(3).to_csv(os.path.join(OUT, _os.path.join(_R, 'data/nyc_and_jfk/processed/jfk27/8_annual.csv')), index=False)

    # sensitivities on L27Q3_base (one change at a time)
    sens = []
    def add(lbl, src, R_):
        q = agg(R_); y = q.quarter.str[:4].astype(int)
        sens.append(dict(case=lbl, source=src, rev_2027_M=q[y == 2027].lost_rev_M.sum(), rev_2028_M=q[y == 2028].lost_rev_M.sum(),
                         rev_2030_M=q[y == 2030].lost_rev_M.sum(), pax_2030=q[y == 2030].lost_pax_total.sum(),
                         cum_rev_M=q.lost_rev_M.sum()))
    add('Central: L27Q3, base capacity', _os.path.join(_R, 'data/nyc_and_jfk/processed/jfk27/model_inputs.json'), run(P, 'L27Q3', 'base'))
    add('Draw factor 0.5', 'agent 4 low bound', run(P, 'L27Q3', 'base', draw=0.5))
    add('Draw factor 1.0', 'agent 4 high bound', run(P, 'L27Q3', 'base', draw=1.0))
    add('Capacity per seat -0.47 (agent 3 TWFE)', _os.path.join(_R, 'data/nyc_and_jfk/processed/jfk27/3_did_dose_results.csv'), run(P, 'L27Q3', 'base', per_seat=0.4714))
    add('No capacity effect (switching only)', 'history-null reading (agent 3/10, LAX 2021-22)', run(P, 'L27Q3', 'base', draw=0.0))
    for lbl, key, val, src in [
        ('LAX fare-parity weight 1.0', 'fare_parity_weight', {'LAX': 1.0, 'SFO': 1.0}, 'treat LAX as full match'),
        ('NY weight 30% (less incremental)', 'ny_weight', 0.30, 'nyc/SYNTHESIS.md'),
        ('Fares $180 (task fallback)', 'fare', {'LAX': 180, 'SFO': 180}, 'task spec'),
        ('Fares = Table 1a JetBlue all-cabin avg', 'fare', None, 'prior run csv1'),
        ('Switch rate 6%/yr cap 6% (instant-ish)', 'switch_rate_per_yr', 0.06, 'stress'),
        ('JetBlue route pax +3%/yr', 'b6_pax_growth_per_yr', {'LAX': 0.03, 'SFO': 0.03}, 'agent 7: 2027 guide low-mid single digits (system)')]:
        Pp = copy.deepcopy(P); Pp[key]['value'] = val if val is not None else P['fare_t1a_all_cabin']['value']
        add(lbl, src, run(Pp, 'L27Q3', 'base'))
    Rb = run(P, 'L27Q3', 'base')
    sens.append(dict(case='Overlap floor max(a,b) instead of a+b', source='model', rev_2027_M=Rb[Rb.quarter.str[:4] == '2027'].lost_rev_overlap_floor_M.sum(),
                     rev_2028_M=Rb[Rb.quarter.str[:4] == '2028'].lost_rev_overlap_floor_M.sum(),
                     rev_2030_M=Rb[Rb.quarter.str[:4] == '2030'].lost_rev_overlap_floor_M.sum(),
                     pax_2030=Rb[Rb.quarter.str[:4] == '2030'].lost_pax_overlap_floor.sum(), cum_rev_M=Rb.lost_rev_overlap_floor_M.sum()))
    S = pd.DataFrame(sens); S.round(2).to_csv(os.path.join(OUT, _os.path.join(_R, 'data/nyc_and_jfk/processed/jfk27/8_sensitivity.csv')), index=False)

    piv = A.pivot(index='scenario', columns='year', values='lost_rev_M').round(1)
    piv['cum'] = Q.groupby('scenario').lost_rev_M.sum().round(1)
    print(piv.to_string()); print(A[A.year == 2030][['scenario', 'lost_pax_switching', 'lost_pax_capacity', 'lost_pax_total']].round(0).to_string())
    print(S.round(1).to_string())
    json.dump(dict(annual=A.round(3).to_dict('records'), sensitivity=S.round(3).to_dict('records')),
              open(os.path.join(OUT, _os.path.join(_R, 'data/nyc_and_jfk/processed/jfk27/8_results.json')), 'w'), indent=1)
