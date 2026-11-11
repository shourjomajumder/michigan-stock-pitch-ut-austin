"""Revenue JetBlue loses to Blue Sky switching (Thesis 1), FINAL inputs from the JetBlue model Assumptions sheet:
base 2.316M passengers/yr, 3.1%/yr switching from Q4'26 (0.775%/qtr), eventual 6% cap, $180 average fare.
Outputs: window grid Q4'26-Q3'27 (base $8.1M), fiscal-year revenue lost (FY27 $11.3M, FY28 $23.0M, FY29+ $25.0M)."""
import numpy as np, pandas as pd, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]; OUT = ROOT / 'processed/model'; OUT.mkdir(exist_ok=True)
PAX, RATE, CAP, FARE = 2.316, 0.031, 0.06, 180.0
BUILD = np.mean([0.25, 0.50, 0.75, 1.00])                     # share builds evenly through the 4 quarters
rates, fares = [0.01, 0.02, 0.031, 0.04, 0.05, 0.06], [150, 165, 180, 195]
G = pd.DataFrame([[PAX * r * f * BUILD for f in fares] for r in rates],
                 index=[f'{r:.1%}' for r in rates], columns=[f'${f}' for f in fares]).round(2)
G.index.name = 'switch_per_yr'; G.to_csv(OUT / 'revenue_lost_window_grid_usd_m.csv')
# quarterly path, FY totals
qs = [(y, q) for y in range(2026, 2031) for q in range(1, 5)]
i0 = qs.index((2026, 4))
path = [(y, q, 0.0 if i < i0 else min(RATE / 4 * (i - i0 + 1), CAP)) for i, (y, q) in enumerate(qs)]
Q = pd.DataFrame(path, columns=['year', 'quarter', 'switched'])
Q['revenue_lost_usd_m'] = PAX * Q.switched * FARE / 4
Q.to_csv(OUT / 'revenue_lost_quarterly.csv', index=False)
FY = Q.groupby('year').agg(avg_switched=('switched', 'mean'), revenue_lost_usd_m=('revenue_lost_usd_m', 'sum')).reset_index()
FY.to_csv(OUT / 'revenue_lost_fy.csv', index=False)
print(G.to_string()); print(f"window base case 3.1% x $180: ${G.loc['3.1%', '$180']:.2f}M")
print(FY.round(4).to_string(index=False))
