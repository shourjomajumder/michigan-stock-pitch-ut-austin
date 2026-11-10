import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import numpy as np, pandas as pd

d = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/daily_returns.csv'))
d['pair'] = d.frontier - 1.16 * d.jetblue
for leg in ['frontier', 'jetblue', 'pair']:
    r = np.corrcoef(d[leg], d.jet_fuel)[0, 1]
    print(f'{leg:<10}{abs(r):.2f}')
