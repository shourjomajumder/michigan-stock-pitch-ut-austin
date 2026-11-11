import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../..')  # repo root
import numpy as np, pandas as pd
df = pd.read_csv(_os.path.join(_R, 'data/jetblue_switching/processed/routes/parity_points.csv'))
b, a = np.polyfit(df.depth, df.loss_yr, 1)
rate = a + b * 1
print(f'routes {len(df)}, fit {a:.2f} + {b:.2f} x link')
print(f'loyalty link: {rate:.1f}% a year')
print(f'share of eventual 6%: {rate / 6:.0%}')
