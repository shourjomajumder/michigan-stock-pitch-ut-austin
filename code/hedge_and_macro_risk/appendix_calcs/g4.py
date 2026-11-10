import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import numpy as np, pandas as pd
from scipy import stats

d = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/appendix_calcs/labor_deals.csv'))
x, y = d.months_early, d.months_to_deal

slope, icpt = np.polyfit(x, y, 1)
r, p = stats.pearsonr(x, y)
print(d.group.value_counts().to_dict(), '| n =', len(d))
print(f'months to deal = {icpt:.1f} {slope:+.2f} x months early')
print(f'r = {r:.2f}   p = {p:.5f}')
