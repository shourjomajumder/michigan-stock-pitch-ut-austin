import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd

d = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/appendix_calcs/jet_fuel_vs_expected.csv'), index_col=0, parse_dates=True)
d['miss'] = d.actual - d.expected_30d_earlier

events = ['2026-03-02', '2026-03-23', '2026-05-26', '2026-07-13',
          '2026-08-03', '2026-09-10', '2026-11-02']
for e in events:
    row = d.loc[:e].iloc[-1]
    print(f'{e}  actual {row.actual:.2f}  expected {row.expected_30d_earlier:.2f}  miss {row.miss:+.2f}')
