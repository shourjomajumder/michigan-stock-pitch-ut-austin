import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import numpy as np, pandas as pd

fuel = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/daily_returns.csv'), index_col=0, parse_dates=True)
ratio = np.polyfit(fuel.jet_fuel, fuel.frontier, 1)[0] / np.polyfit(fuel.jet_fuel, fuel.jetblue, 1)[0]
fuel['pair'] = fuel.frontier - ratio * fuel.jetblue

r = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/raw/yahoo/yahoo_daily_closes_2025-10-31_2026-11-09.csv'), index_col=0, parse_dates=True).pct_change()
r = r.loc['2025-11-04':'2026-10-27']
r['pair'] = r.frontier - ratio * r.jetblue
print(f'hedge ratio {ratio:.2f}')

legs = ['frontier', 'jetblue', 'pair']
print('jet fuel       ' + '  '.join(f'{abs(fuel[l].corr(fuel.jet_fuel)):.2f}' for l in legs))
for col, name in {'jets': 'airline sector', 'iwm': 'small caps', 'spy': 'stock market',
                  'xly': 'consumer', 'hyg': 'credit'}.items():
    print(f'{name:15}' + '  '.join(f'{abs(r[l].corr(r[col])):.2f}' for l in legs))
