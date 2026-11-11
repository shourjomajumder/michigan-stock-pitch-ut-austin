import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd

p = pd.read_csv(_os.path.join(_R, 'data/company_and_industry/raw/yahoo_daily_close_JBLU_ULCC_JETS_SPY_2025-11-10_2026-11-09.csv'), index_col=0, parse_dates=True)
w = pd.concat([p.iloc[[0]], p.resample('W-FRI').last()])
idx = w / p.iloc[0] * 100
print(f'weekly points  {len(idx)}')
for c in ['ULCC', 'JBLU', 'JETS']:
    a, b, e = p[c].iloc[0], p[c].iloc[-1], idx[c].iloc[-1]
    print(f'{c:<5} {a:7.2f} {b:7.2f}   index {e:5.1f}  {e - 100:+4.0f}%')
