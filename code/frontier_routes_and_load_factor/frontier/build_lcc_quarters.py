"""Rebuild processed/lcc_quarters.csv (32 low-cost-airline quarters) from reported quarterly operating stats.
fare    = YoY % change in yield (passenger revenue / RPM, i.e. fare per passenger mile)
traffic = YoY % change in RPMs
seats   = YoY % change in ASMs (Sun Country: ASM = RPM / load factor, scheduled service)
Sample: drop quarters whose own or prior-year quarter falls in COVID (2020Q1-2022Q1) and quarters from
2025Q4 on (Spirit shrink/shutdown, Allegiant-Sun Country merger). Run from repo folder frontier/code."""
import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd
RAW = _os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier/raw') + '/'
_OUT = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'out'); _os.makedirs(_OUT, exist_ok=True)
f = pd.read_csv(RAW + 'frontier_quarterly_ops_2019Q1_2026Q3.csv')
a = pd.read_csv(RAW + 'allegiant_quarterly_ops_2018Q3_2026Q3.csv')
s = pd.read_csv(RAW + 'suncountry_quarterly_ops_2022Q2_2026Q1.csv')
s['asm_m'] = s.rpm_m / (s.load_factor_pct / 100)
rows = []
for name, df in [('Allegiant', a), ('Sun Country', s), ('Frontier', f)]:
    df = df.set_index('quarter')
    for q in df.index:
        base = f'{int(q[:4]) - 1}{q[4:]}'
        if base not in df.index: continue
        covid = lambda x: '2020Q1' <= x <= '2022Q1'
        if covid(q) or covid(base) or q >= '2025Q4': continue
        y = lambda r: r.passenger_revenue_usd_m / r.rpm_m
        g = lambda now, old: round((now / old - 1) * 100, 2)
        rows.append((name, q, g(y(df.loc[q]), y(df.loc[base])), g(df.loc[q, 'rpm_m'], df.loc[base, 'rpm_m']),
                     g(df.loc[q, 'asm_m'], df.loc[base, 'asm_m'])))
out = pd.DataFrame(rows, columns=['airline', 'quarter', 'fare', 'traffic', 'seats'])
out.to_csv(_os.path.join(_OUT, 'lcc_quarters_rebuilt.csv'), index=False)
ref = pd.read_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier/processed/lcc_quarters.csv'))
m = ref.merge(out, on=['airline', 'quarter'], suffixes=('', '_new'))
print(len(out), 'quarters rebuilt;', len(m), 'match keys; max abs diff',
      max((m[c] - m[c + '_new']).abs().max() for c in ['fare', 'traffic', 'seats']))
