import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../..')  # repo root
import numpy as np, pandas as pd
df = pd.read_csv(_os.path.join(_R, 'data/jetblue_switching/processed/routes/parity_points.csv'))
slope, icpt = np.polyfit(df.depth, df.loss_yr, 1)
r = np.corrcoef(df.depth, df.loss_yr)[0, 1]
rate = round(icpt + slope * 1, 1)
window = rate * 4 / 4
eventual = 6.0
print(f'fit {icpt:.2f} + {slope:.2f} x link, r {r:.2f}, n {len(df)}')
print(f'loyalty link: {rate:.1f}% a year')
print(f'Q4 2026 to Q3 2027: {window:.1f}%')
print(f'share of eventual {eventual:.0f}%: {window / eventual:.0%}')
