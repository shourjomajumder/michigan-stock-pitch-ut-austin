"""Fit share lost per year vs partnership depth on the 25 same-fare routes.
Reproduces: 0.52 + 2.62 x link, r 0.42, n 25 -> 3.1%/yr at link=1 (shared loyalty), 52% of an eventual 6%.
Run from repo root of this folder:  python code/pipeline/fit_switch_rate.py"""
import numpy as np, pandas as pd, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
df = pd.read_csv(ROOT / 'processed/routes/parity_points.csv')
slope, icpt = np.polyfit(df.depth, df.loss_yr, 1)
r = np.corrcoef(df.depth, df.loss_yr)[0, 1]
rate = round(icpt + slope * 1, 1)
by = df.groupby('depth').loss_yr.agg(['mean', 'median', 'count']).round(2)
out = pd.DataFrame([
    ('n_routes', len(df)), ('intercept', icpt), ('slope_per_link_level', slope), ('r', r),
    ('fitted_loss_pct_yr_at_link1', icpt + slope), ('model_rate_pct_yr_rounded', rate),
    ('window_Q4_26_to_Q3_27_pct', rate * 4 / 4), ('eventual_pct', 6.0), ('share_of_eventual', rate / 6.0),
    ('line_endpoint_y_at_x-0.3', icpt + slope * -0.3), ('line_endpoint_y_at_x2.3', icpt + slope * 2.3)],
    columns=['metric', 'value'])
(ROOT / 'processed/model').mkdir(exist_ok=True)
out.to_csv(ROOT / 'processed/model/switch_rate_fit.csv', index=False)
by.to_csv(ROOT / 'processed/model/switch_rate_by_depth.csv')
print(out.to_string(index=False)); print(by)
