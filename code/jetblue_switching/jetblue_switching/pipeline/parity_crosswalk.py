"""Trace each of the 25 parity points (processed/routes/parity_points.csv, hand-entered in code/routes/parity.py)
back to a row of the route-case CSVs r02/r04/r05/r07/r10. Two points chain two windows (SEA-BOI 2015Q3->2019Q3,
SEA-SLC 2014Q4->2019Q2): matched on the before of the first window and the after of the second."""
import pandas as pd, glob, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
P = pd.read_csv(ROOT / 'processed/routes/parity_points.csv')
R = pd.concat([pd.read_csv(f).assign(file=pathlib.Path(f).name) for f in sorted(glob.glob(str(ROOT / 'processed/routes/r*.csv')))], ignore_index=True)
out = []
for _, p in P.iterrows():
    m = R[(abs(R.share_before_pct - p.before) < 0.06) & (abs(R.share_after_pct - p.after) < 0.06)]
    if len(m):
        x = m.iloc[0]; out.append((p.case, p.route, x.file, x.route, x.carrier, x.role, x.period_before, x.period_after, 'direct'))
    else:
        a = R[(abs(R.share_before_pct - p.before) < 0.06) & R.route.str.contains(p.route)]
        b = R[(abs(R.share_after_pct - p.after) < 0.06) & R.route.str.contains(p.route)]
        out.append((p.case, p.route, a.file.iloc[0], p.route, a.carrier.iloc[0], 'loser/winner chained',
                    a.period_before.iloc[0], b.period_after.iloc[0], 'chained two windows'))
pd.DataFrame(out, columns=['case', 'route', 'source_file', 'source_route', 'carrier_tracked', 'role', 'period_before',
                           'period_after', 'match']).to_csv(ROOT / 'processed/routes/parity_points_crosswalk.csv', index=False)
print(pd.read_csv(ROOT / 'processed/routes/parity_points_crosswalk.csv').to_string(index=False))
