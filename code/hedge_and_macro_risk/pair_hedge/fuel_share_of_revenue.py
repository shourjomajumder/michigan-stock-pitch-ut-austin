"""Fuel as % of revenue, Q1-Q3 2026 (Hedge Overview bar chart; '31.4% / 30.9% in Q3 2026').

    python code/fuel_share_of_revenue.py        (run from pair_hedge/)

Input: raw/filings/fuel_and_revenue_2026_quarters.csv, transcribed from the companies' SEC filings / earnings
releases (URLs in the file). Q1 = H1 minus Q2; Q2 and Q3 are reported three-month figures.
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
f = pd.read_csv(ROOT / 'raw/filings/fuel_and_revenue_2026_quarters.csv')
rows = []
for co, g in f.groupby('company', sort=False):
    g = g.set_index(g.period.str.split(' ').str[0])
    q = {'Q1 2026': g.loc['H1'][['total_operating_revenues_musd', 'aircraft_fuel_musd']]
                    - g.loc['Q2'][['total_operating_revenues_musd', 'aircraft_fuel_musd']],
         'Q2 2026': g.loc['Q2'][['total_operating_revenues_musd', 'aircraft_fuel_musd']],
         'Q3 2026': g.loc['Q3'][['total_operating_revenues_musd', 'aircraft_fuel_musd']]}
    assert (g.loc['H1'].iloc[2:4].astype(float) + g.loc['Q3'].iloc[2:4].astype(float)
            == g.loc['9M'].iloc[2:4].astype(float)).all()          # H1 + Q3 = 9M check
    for k, v in q.items():
        rows.append(dict(company=co, quarter=k, revenue_musd=int(v.iloc[0]), fuel_musd=int(v.iloc[1]),
                         fuel_pct_revenue=round(100 * v.iloc[1] / v.iloc[0], 1)))
out = pd.DataFrame(rows)
out.to_csv(ROOT / 'processed/fuel_share_of_revenue_2026.csv', index=False)
print(out.to_string(index=False))
