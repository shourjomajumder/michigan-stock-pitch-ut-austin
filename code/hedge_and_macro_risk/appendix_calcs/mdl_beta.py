import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import numpy as np
import pandas as pd

px = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/raw/yahoo/yahoo_daily_closes_2025-10-31_2026-11-09.csv'), index_col=0)
r = px.pct_change().dropna()

for t, de in [('frontier', 487.3 / 1903.0), ('jetblue', 8648.3 / 1512.6)]:
    raw = np.cov(r[t], r.spy)[0, 1] / r.spy.var()
    adj = 0.67 * raw + 0.33
    bottom_up = 0.76 * (1 + 0.76 * de)
    print(f'{t:9} raw {raw:.2f}  adjusted {adj:.2f}  bottom-up {bottom_up:.2f}')
