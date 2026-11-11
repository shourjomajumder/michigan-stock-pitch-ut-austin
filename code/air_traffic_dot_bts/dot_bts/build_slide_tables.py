"""Rebuild every DOT/BTS/FAA-sourced slide number from the files in ../raw.

Run from this folder:  python build_slide_tables.py
Writes ../processed/slide_*.csv and asserts each number against the deck.

Slides covered
  Industry Overview (main deck slide 3): US domestic market share pie, US domestic load factor 2025
  JetBlue Thesis 1 (main deck slide 27) + appendix E1: on-time and cancellation rates, 2025
  Appendix E2 / E5 (and main deck slide 28 base): 2.316M switching passenger base
"""
import csv, collections
import pandas as pd

RAW = '../raw/'
OUT = '../processed/'

# ---------------------------------------------------------------- market share pie
ms = pd.read_csv(RAW + 'bts_market_share/bts_airline_domestic_market_share_aug2025_jul2026.csv')
named = ['Delta', 'American', 'United', 'Southwest', 'Alaska', 'JetBlue', 'Frontier']
pie = ms[ms.carrier.isin(named)][['carrier', 'share_pct']].copy()
other = round(ms[~ms.carrier.isin(named)].share_pct.sum(), 1)      # SkyWest + Spirit + Envoy + Other
pie = pd.concat([pie, pd.DataFrame([{'carrier': 'Other', 'share_pct': other}])], ignore_index=True)
pie['slide_value'] = (pie.share_pct / 100).round(3)
pie.to_csv(OUT + 'slide03_us_domestic_market_share_pie.csv', index=False)
assert list(pie.share_pct) == [17.9, 17.7, 17.2, 17.1, 7.1, 4.6, 3.9, 14.5], list(pie.share_pct)
assert round(pie.share_pct.sum(), 1) == 100.0
big4 = round(pie.share_pct[:4].sum(), 1)
assert big4 == 69.9   # note: old deck notes say "big four = 71.3%" - that was an earlier vintage

# ---------------------------------------------------------------- US domestic load factor 2025
lf = pd.read_csv(RAW + 'fred/LOADFACTORDD11_2025_2026.csv', parse_dates=['date'])
lf25 = lf[lf.date.dt.year == 2025].load_factor_pct_sa
lf_avg = round(lf25.mean(), 1)
assert len(lf25) == 12 and lf_avg == 81.7, lf_avg
pd.DataFrame([{'metric': 'US domestic scheduled load factor, 2025 (mean of 12 monthly SA values)',
               'value_pct': lf_avg, 'source': 'FRED LOADFACTORDD11 (BTS)'}]).to_csv(OUT + 'slide03_us_domestic_load_factor_2025.csv', index=False)

# ---------------------------------------------------------------- reliability 2025 (ATCR Feb 2026)
ot = pd.read_csv(RAW + 'atcr/c1_ontime.csv'); cx = pd.read_csv(RAW + 'atcr/c4_cancel.csv')
g = lambda d, c, m: float(d[(d.carrier == c) & (d.year == 2025) & (d.metric == m)].value.iloc[0])
rel = pd.DataFrame([
    dict(metric='On-time arrivals', carrier='United', raw=g(ot, 'UA', 'ontime_pct'), basis='mainline (ATCR Table 1D)', slide='77.6%'),
    dict(metric='On-time arrivals', carrier='JetBlue', raw=g(ot, 'B6', 'ontime_pct'), basis='single brand', slide='72.3%'),
    dict(metric='Cancelled flights', carrier='United', raw=g(cx, 'UA', 'cancel_pct_network'), basis='network incl. United Express (ATCR Table 6C)', slide='1.36%'),
    dict(metric='Cancelled flights', carrier='JetBlue', raw=g(cx, 'B6', 'cancel_pct'), basis='single brand', slide='1.65%'),
])
rel['memo_UA_mainline_cancel_pct'] = [None, None, g(cx, 'UA', 'cancel_pct'), None]
rel['p_at_least_one_cancel_in_20'] = [None, None, 1 - (1 - 0.0136) ** 20, 1 - (1 - 0.0165) ** 20]
rel.to_csv(OUT + 'slide27_E1_reliability_2025.csv', index=False)
assert (rel.raw.tolist() == [77.65, 72.34, 1.36, 1.65])
assert round(rel.p_at_least_one_cancel_in_20[2] * 100) == 24 and round(rel.p_at_least_one_cancel_in_20[3] * 100) == 28

# ---------------------------------------------------------------- 2.316M switching passenger base
# (a) NYC domestic 18 routes and international 5 routes from the L4Q (Q3'25-Q2'26) T-100 pull
ov = pd.read_csv(OUT + 'bluesky_nyc_overlap.csv')
DOM = ['FLL', 'LAX', 'PBI', 'SFO', 'BOS', 'TPA', 'ATL', 'RDU', 'JAX', 'SAN', 'BQN', 'PHX', 'CHS', 'DEN', 'SLC', 'MSY', 'IAH', 'CLE']
d = ov[(ov.scope == 'dom') & ov.nyc_airport.isin(['JFK', 'LGA']) & ov.dest.isin(DOM)]
dom = d.groupby('dest').b6_pax_L4Q.sum().sort_values(ascending=False)
pd.DataFrame({'route': ['NYC-' + k for k in dom.index], 'airports': 'JFK, LGA', 'b6_pax': dom.values,
              'b6_pax_M': (dom.values / 1e6).round(3)}).to_csv(OUT + 'slideE5_nyc_domestic_18_routes.csv', index=False)
assert len(dom) == 18 and round(dom.sum() / 1e6, 3) == 5.533

# (b) same-airport routes and JFK international, Aug 2025-Jul 2026 T-100 pulls
sa = pd.read_csv(RAW + 't100/t100_same_airport_pairs_B6_UA_aug2025_jul2026.csv').set_index('pair')
ip = pd.read_csv(RAW + 't100/t100_intl_pairs_B6_UA_aug2025_jul2026.csv').set_index('pair')
SAME = [('BOS-LAX', sa.loc['BOS-LAX', 'b6_pax'], 'same_airport_pairs Aug25-Jul26'),
        ('BOS-SFO', sa.loc['BOS-SFO', 'b6_pax'], 'same_airport_pairs Aug25-Jul26'),
        ('FLL-SFO', sa.loc['FLL-SFO', 'b6_pax'], 'same_airport_pairs Aug25-Jul26'),
        ('FLL-IAH', sa.loc['FLL-IAH', 'b6_pax'], 'same_airport_pairs Aug25-Jul26'),
        ('EWR-FLL', sa.loc['FLL-EWR', 'b6_pax'], 'same_airport_pairs Aug25-Jul26'),
        # the slide uses the Q3'25-Q2'26 value for EWR-PBI (188,843); the Aug25-Jul26 pull has 189,149
        ('EWR-PBI', int(ov[ov.route == 'EWR-PBI'].b6_pax_L4Q.iloc[0]), 'nyc overlap L4Q Q3 25-Q2 26')]
INTL = ['JFK-SDQ', 'JFK-PUJ', 'JFK-MBJ', 'JFK-LHR', 'JFK-NAS']
same = pd.DataFrame(SAME, columns=['route', 'b6_pax', 'period_source'])
same['ua_pax'] = [sa.loc[r if r != 'EWR-FLL' else 'FLL-EWR', 'ua_pax'] for r in same.route]
same.to_csv(OUT + 'slideE2_E5_same_airport_6_routes.csv', index=False)
intl = pd.DataFrame({'route': INTL, 'b6_pax': [ip.loc[r, 'b6_pax'] for r in INTL]})
intl.to_csv(OUT + 'slideE5_nyc_international_5_routes.csv', index=False)
assert same.b6_pax.tolist() == [462535, 464206, 208271, 15220, 276921, 188843]
assert intl.b6_pax.tolist() == [555989, 386552, 223368, 164861, 143297]

s_same, s_dom, s_intl = same.b6_pax.sum() / 1e6, dom.sum() / 1e6, intl.b6_pax.sum() / 1e6
base = round(s_same, 3) + round(0.10 * s_dom, 3) + round(0.10 * s_intl, 3)
rows = [dict(component='Same-airport routes (6)', passengers_M=round(s_same, 3), counted=1.0, in_base_M=round(s_same, 3)),
        dict(component='New York domestic (18 routes)', passengers_M=round(s_dom, 3), counted=0.10, in_base_M=round(0.10 * s_dom, 3)),
        dict(component='New York international (5 routes)', passengers_M=round(s_intl, 3), counted=0.10, in_base_M=round(0.10 * s_intl, 3)),
        dict(component='Total switching base', passengers_M=None, counted=None, in_base_M=round(base, 3))]
pd.DataFrame(rows).to_csv(OUT + 'slideE5_switching_passenger_base_2316k.csv', index=False)
assert (round(s_same, 3), round(s_dom, 3), round(s_intl, 3), round(base, 3)) == (1.616, 5.533, 1.474, 2.316)
assert abs(0.40 * 0.24 - 0.096) < 1e-12   # 40% live in Manhattan x 24% shown to use Newark -> counted at 10%

print('market share', pie.share_pct.tolist(), '| big four', big4, '| LF 2025', lf_avg)
print('reliability', rel.raw.tolist())
print(f'base: {s_same:.3f} + 10% x {s_dom:.3f} + 10% x {s_intl:.3f} = {base:.3f}M')
