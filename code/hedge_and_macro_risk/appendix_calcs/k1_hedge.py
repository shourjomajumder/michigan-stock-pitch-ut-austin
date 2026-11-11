import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import numpy as np, pandas as pd

r = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/daily_returns.csv'), index_col=0)
jet, ulcc, jblu = r.jet_fuel, r.frontier, r.jetblue

b_u, a_u = np.polyfit(jet, ulcc, 1)
b_j, a_j = np.polyfit(jet, jblu, 1)
ratio = b_u / b_j
print(f'Frontier  y = {b_u:.2f}x {a_u:+.2f}   beta {b_u:.3f}')
print(f'JetBlue   y = {b_j:.2f}x {a_j:+.2f}   beta {b_j:.3f}')
print(f'hedge ratio     {ratio:.2f}')
print(f'pair fuel beta  {abs(b_u - ratio * b_j):.2f}')
