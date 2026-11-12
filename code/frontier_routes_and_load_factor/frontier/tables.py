"""Write the small processed tables behind the Frontier overview and Theses 1-2. Run from frontier/code."""
import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd
P = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'out') + '/'; _os.makedirs(P, exist_ok=True)
_PROC = _os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier/processed') + '/'
f = pd.read_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier/raw/frontier_quarterly_ops_2019Q1_2026Q3.csv')).set_index('quarter')

# Thesis 1 inputs from reported actuals
g = lambda a, b, c='rpm_m': round((f.loc[a, c] / f.loc[b, c] - 1) * 100, 2)
pd.DataFrame([
    ('Q2 2026 traffic (RPM) growth YoY, %', g('2026Q2', '2025Q2'), 'Frontier Q2 2026 10-Q: RPM 8,915M vs 8,182M'),
    ('Prior-year load factor Q4 2025, %', f.loc['2025Q4', 'load_factor_pct'], 'Frontier Q4 2025 release'),
    ('Prior-year load factor Q1 2026, %', f.loc['2026Q1', 'load_factor_pct'], 'Frontier Q1 2026 10-Q'),
    ('Q3 2026 system ASMs, M', f.loc['2026Q3', 'asm_m'], 'Frontier Q3 2026 10-Q (denominator for +1.2% added capacity)'),
], columns=['item', 'value', 'source']).to_csv(P + 'thesis1_inputs_reported.csv', index=False)

# Load factor build (deck slide 21 / appendix C2); fare and seat inputs as in e2_build.py
rows = []
for q, lf, fare, seats in [('Q4 2026E', 78.9, 2.2, 5.4), ('Q1 2027E', 78.4, 2.9, 6.1)]:
    up = lf * 0.110; drag = (lf + up) * 0.16 * fare / 100; full = lf + up - drag
    cap = full - full / (1 + seats / 100)
    rows.append((q, lf, 11.0, round(up, 1), fare, 0.16, round(drag, 1), seats, round(cap, 1), round(full - cap, 1)))
pd.DataFrame(rows, columns=['quarter', 'prior_year_lf_pct', 'traffic_growth_pct', 'traffic_pts', 'fare_rise_pct',
                            'elasticity', 'fare_drag_pts', 'seat_growth_pct', 'added_capacity_pts', 'our_lf_pct']
             ).to_csv(P + 'thesis1_load_factor_build.csv', index=False)

# Results table (deck slide 20). Consensus LF column is Bloomberg consensus -> not redistributed.
VAR = 0.12   # variable cost on thesis revenue (model assumption) -> EBIT = 88% of revenue
res = pd.DataFrame([('Q4 2026E', 82.8, 3.3, 380000, 52), ('Q1 2027E', 81.6, 2.6, 290000, 41)],
                   columns=['quarter', 'our_lf_pct', 'extra_pts_vs_consensus', 'extra_pax', 'extra_revenue_usd_m'])
res['extra_ebit_usd_m'] = (res.extra_revenue_usd_m * (1 - VAR)).round(2)
res.loc[len(res)] = ['Total', None, None, res.extra_pax.sum(), res.extra_revenue_usd_m.sum(), round(res.extra_ebit_usd_m.sum(), 2)]
res.to_csv(P + 'thesis1_results.csv', index=False)

# Fare vs traffic scatter (deck slide 21 / appendix C1) = lcc_quarters rounded to 0.1
lcc = pd.read_csv(_PROC + 'lcc_quarters.csv')
lcc.assign(fare=lcc.fare.round(1), traffic=lcc.traffic.round(1))[['airline', 'quarter', 'fare', 'traffic']] \
   .rename(columns={'fare': 'fare_per_mile_yoy_pct', 'traffic': 'traffic_yoy_pct'}).to_csv(P + 'fare_vs_traffic_scatter.csv', index=False)

# Top booking factor survey (pie, slide 21)
pd.DataFrame([('Price', 57), ('Airline', 14), ('Number of stops', 9), ('Other', 20)],
             columns=['factor', 'share_pct']).to_csv(P + 'booking_factor_survey.csv', index=False)

# Six new routes (slides 5, 22-23; appendix D1-D2)
routes = [('Las Vegas–Oakland', 'LAS-OAK', '2026-08-20', 11, 407), ('Las Vegas–Boise', 'LAS-BOI', '2026-09-10', 4, 520),
          ('Nashville–Tampa', 'BNA-TPA', '2026-10-09', 2, 612), ('Denver–Fort Lauderdale', 'DEN-FLL', '2026-11-20', 7, 1703),
          ('Ontario–Oakland', 'ONT-OAK', '2026-11-21', 4, 361), ('Orlando–Cartagena', 'MCO-CTG', '2026-12-19', 1, 1340)]
r = pd.DataFrame(routes, columns=['route', 'code', 'launch_date', 'weekly_flights_each_way', 'miles'])
r['seats_per_flight'] = 230
r['weekly_seats'] = r.weekly_flights_each_way * 2 * 230
r['seat_miles_per_full_quarter_m'] = (r.weekly_seats * 30.4 / 7 * 3 * r.miles / 1e6).round(2)
r.to_csv(P + 'thesis2_new_routes.csv', index=False)
pd.DataFrame([(0, '0-2', 0.85), (3, '3-5', 1.05), (6, '6-8', 1.15), (9, '9+', 1.20)],
             columns=['months_since_launch_from', 'months', 'rasm_vs_system']).to_csv(P + 'thesis2_ramp_assumption.csv', index=False)
pd.DataFrame([('System RASM Q3 2026, cents', 11.87, 'Frontier Q3 2026 10-Q (total revenue / ASM)'),
              ('Q3 2027 route effect, $K', 3009, 'code/f2_ramp_k.py'),
              ('Run-rate, $M/yr (Q3 2027 x 4)', 12.04, 'code/f2_ramp_k.py; = model FY2028 Thesis 2 revenue'),
              ('Net effect Q4 2026-Q3 2027, $K', 4469, 'code/f2_ramp_k.py (deck rounds to $4.5M)'),
              ('Added capacity, % of Q3 2026 ASM', 1.2, 'code/f1_asm.py (134.76M / 11,419M)')],
             columns=['item', 'value', 'source']).to_csv(P + 'thesis2_summary.csv', index=False)

# Fleet mix and FY2025 revenue mix (Company Overview, slide 5)
pd.DataFrame({'as_of': ["Dec '23", "Dec '24", "Dec '25", "Sep '26"], 'A320ceo': [8, 8, 6, 6], 'A321ceo': [21, 21, 21, 21],
              'A320neo': [82, 82, 89, 68], 'A321neo': [25, 48, 60, 69]}).assign(
    total=lambda d: d[['A320ceo', 'A321ceo', 'A320neo', 'A321neo']].sum(axis=1)).to_csv(P + 'fleet_mix.csv', index=False)
pd.DataFrame([('A320ceo', 186), ('A321ceo', 230), ('A320neo', 186), ('A321neo', 240)],
             columns=['type', 'seats']).to_csv(P + 'fleet_seats.csv', index=False)
pd.DataFrame([('Fare', 1481), ('Non-fare passenger', 2117), ('Other', 126)],
             columns=['line', 'fy2025_usd_m']).to_csv(P + 'fy2025_revenue_mix.csv', index=False)
print(res.to_string(index=False))
