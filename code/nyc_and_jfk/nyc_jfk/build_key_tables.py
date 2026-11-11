"""Rebuild the headline New York / JFK tables used on the deck and appendix (E5, E2, E7, valuation stack).

Run from data_repo/nyc_jfk:  python3 code/build_key_tables.py
Inputs (all in this folder):
  raw/t100_aug2025_jul2026/*.csv           BTS T-100 Aug'25-Jul'26 pulls (same-airport and international pairs)
  processed/nyc/4_full_overlap.csv          JetBlue NYC routes with a United NYC nonstop, BTS T-100 L4Q (Q3'25-Q2'26)
  processed/jfk27/8_scenarios.csv           United JFK return scenario model (agent 8), quarterly
  processed/jfk27/scenario_outputs/thesis_dcf_inputs.csv  own-model DCF inputs (WACC, ke, tax, shares)
Outputs:
  processed/nyc_passenger_base.csv          2.316M = 1.616M + 10% x 5.533M + 10% x 1.474M
  processed/nyc_domestic_18_routes.csv      the 18 New York domestic routes (sum 5.533M)
  processed/jfk_switching_revenue_by_fy.csv JFK return, switching only: $0.5/4.4/8.1/8.4M and x60%
  processed/t2_per_share.csv                Thesis 2 DCF of the 60%-weighted revenue: -$0.06/share
"""
import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import json, pandas as pd

ov = pd.read_csv(_os.path.join(_R, 'data/nyc_and_jfk/processed/nyc/4_full_overlap.csv'))

# --- New York passenger base (slide E5 / main-deck slide 40) ---
DOM = ['FLL', 'LAX', 'PBI', 'SFO', 'BOS', 'TPA', 'ATL', 'RDU', 'JAX', 'SAN', 'BQN', 'PHX', 'CHS', 'DEN', 'SLC', 'MSY', 'IAH', 'CLE']
d = ov[(ov.scope == 'dom') & ov.nyc_airport.isin(['JFK', 'LGA']) & ov.dest.isin(DOM)]
dom = d.groupby('dest').b6_pax_L4Q.sum().sort_values(ascending=False)
dom.rename('b6_pax_L4Q').to_frame().assign(route=lambda x: 'NYC-' + x.index).to_csv(_os.path.join(_R, 'data/nyc_and_jfk/processed/nyc_domestic_18_routes.csv'))
# Same-airport routes: BTS T-100 Aug 2025-Jul 2026 pull (raw/t100_aug2025_jul2026/same_airport_pairs.csv),
# except EWR-PBI, which the deck took from the Q3'25-Q2'26 T-100 window (processed/nyc/4_full_overlap.csv: 188,843;
# the Aug-Jul pull has 189,149). Kept as on the slide; the difference is 306 passengers.
sap = pd.read_csv(_os.path.join(_R, 'data/nyc_and_jfk/raw/t100_aug2025_jul2026/same_airport_pairs.csv')).set_index('pair').b6_pax
ewr_pbi = int(ov[(ov.nyc_airport == 'EWR') & (ov.dest == 'PBI')].b6_pax_L4Q.iloc[0])
SAME = [('BOS-LAX', sap['BOS-LAX']), ('BOS-SFO', sap['BOS-SFO']), ('FLL-SFO', sap['FLL-SFO']), ('FLL-IAH', sap['FLL-IAH']),
        ('EWR-FLL', sap['FLL-EWR']), ('EWR-PBI', ewr_pbi)]
ip = pd.read_csv(_os.path.join(_R, 'data/nyc_and_jfk/raw/t100_aug2025_jul2026/intl_pairs.csv')).set_index('pair').b6_pax
INTL = [(r, ip[r]) for r in ('JFK-SDQ', 'JFK-PUJ', 'JFK-MBJ', 'JFK-LHR', 'JFK-NAS')]
assert [v for _, v in SAME] == [462535, 464206, 208271, 15220, 276921, 188843]
assert [v for _, v in INTL] == [555989, 386552, 223368, 164861, 143297]
same = sum(v for _, v in SAME) / 1e6
intl = sum(v for _, v in INTL) / 1e6
W = 0.10
rows = [(r, v / 1e6, 1.0, v / 1e6, 'same airport') for r, v in SAME]
rows += [('New York domestic, 18 routes (JFK+LGA vs United EWR)', dom.sum() / 1e6, W, W * dom.sum() / 1e6, 'NYC domestic')]
rows += [('New York international, 5 routes', intl, W, W * intl, 'NYC international')]
base = pd.DataFrame(rows, columns=['piece', 'pax_M', 'weight', 'in_base_M', 'group'])
total = round(same, 3) + round(W * dom.sum() / 1e6, 3) + round(W * intl / 1, 3)  # model input is the sum of the 3-dp pieces (unrounded sum = 2.3167M)
base.loc[len(base)] = ['Total switching base (sum of 3-dp pieces; model input)', float('nan'), float('nan'), total, 'total']
base.round(6).to_csv(_os.path.join(_R, 'data/nyc_and_jfk/processed/nyc_passenger_base.csv'), index=False)
assert len(dom) == 18 and round(dom.sum() / 1e6, 3) == 5.533 and round(W * dom.sum() / 1e6, 3) == 0.553
assert round(intl, 3) == 1.474 and round(W * intl, 3) == 0.147 and round(same, 3) == 1.616
assert round(total, 3) == 2.316

# --- United JFK return, switching revenue by FY (slide E7) ---
sc = pd.read_csv(_os.path.join(_R, 'data/nyc_and_jfk/processed/jfk27/8_scenarios.csv'))
sc = sc[sc.scenario == 'L27Q3_base'].copy()
sc['fy'] = sc.quarter.str[:4].astype(int)
ann = sc.groupby('fy')[['lost_pax_switching', 'lost_rev_switching_M', 'lost_rev_sw60_M']].sum()
ann.round(4).to_csv(_os.path.join(_R, 'data/nyc_and_jfk/processed/jfk_switching_revenue_by_fy.csv'))
assert [round(ann.loc[y, 'lost_rev_switching_M'], 1) for y in (2027, 2028, 2029, 2030)] == [0.5, 4.4, 8.1, 8.4]
assert [round(ann.loc[y, 'lost_rev_sw60_M'], 1) for y in (2027, 2028, 2029, 2030)] == [0.3, 2.6, 4.8, 5.1]

# --- Thesis 2 per share: same DCF mechanics as the JetBlue model's thesis block ---
_I = pd.read_csv(_os.path.join(_R, 'data/nyc_and_jfk/processed/jfk27/scenario_outputs/thesis_dcf_inputs.csv')).set_index('input').value
P = {k: (float(v) if k != 'source' else v) for k, v in _I.items()}
wacc, g, tax, ke, sh, stub, vc = P['wacc_implied'], P['g'], P['tax'], P['ke'], P['shares'], P['stub_years'], P['var_cost']
ebit = {y: -ann.loc[y, 'lost_rev_sw60_M'] * (1 - vc) for y in (2027, 2028, 2029, 2030)}
nopat = {y: e * (1 - tax) for y, e in ebit.items()}          # thesis EBIT is negative, taxed at the long-run rate
pv = {y: nopat[y] / (1 + wacc) ** (i + 0.5) for i, y in enumerate(nopat)}   # mid-year discounting
tv = nopat[2030] * (1 + g) * (1 - g / wacc) / (wacc - g)       # value-driver TV, RONIC = WACC
ev = sum(pv.values()) + tv / (1 + wacc) ** 4
eq_today = ev / (1 + ke) ** stub
ps = eq_today / sh
out = pd.DataFrame({'fy': list(ebit), 'rev_lost_x60_M': [ann.loc[y, 'lost_rev_sw60_M'] for y in ebit],
                    'thesis2_ebit_M': list(ebit.values()), 'after_tax_M': list(nopat.values()), 'pv_M': list(pv.values())})
out.loc[len(out)] = ['TV / EV / equity / per share', tv, ev, eq_today, ps]
out.round(6).to_csv(_os.path.join(_R, 'data/nyc_and_jfk/processed/t2_per_share.csv'), index=False)
print(f'base {total:.3f}M; JFK rev {[round(ann.loc[y,"lost_rev_switching_M"],1) for y in ebit]}; T2 {ps:.4f}/sh (model {P["t2_ps_model"]:.4f})')
assert round(ps, 2) == -0.06 and abs(ps - P['t2_ps_model']) < 0.002
