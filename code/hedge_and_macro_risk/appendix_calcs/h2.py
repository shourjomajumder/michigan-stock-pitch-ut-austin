import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import os as _os
_REPO = _os.environ.get('DATA_REPO', _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..')))
import numpy as np, pandas as pd
df = pd.read_csv(_os.path.join(_REPO, _os.path.join(_R, 'data/air_traffic_dot_bts/processed/parity_points_25_cases.csv')))
slope, icpt = np.polyfit(df.depth, df.loss_yr, 1)
r = np.corrcoef(df.depth, df.loss_yr)[0, 1]
blue_sky = round(icpt + slope * 1, 1)
print(f'loss = {icpt:.2f} + {slope:.2f} x depth, r {r:.2f}')
print(f'by Q3 2027: {blue_sky * 22 / 12:.1f}%')
