"""Switching pace: logistic S-curves fitted to 5 precedents (quarter of 10% / 50% / 90% of eventual shift),
median 50% at quarter 5 with scale (6-5)/ln 9 = 0.455; and the model ramp actually used (linear 0.775%/qtr, capped 6%).
Precedent quarters are our reading of processed/switch/a1..a5 *.md (event-time Table 6 studies)."""
import numpy as np, pandas as pd, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]; OUT = ROOT / 'processed/model'; OUT.mkdir(exist_ok=True)
pace = {'Delta / Alaska': (4, 5, 6, 'a1_delta_alaska.md (loyalty-driven excess: sustained k4, peak k6)'),
        'Continental / Northwest': (0, 0.5, 3, 'a2_co_nw.md (50% by k0-k1, 90% by k2-k4)'),
        'American / JetBlue': (4, 5, 6, 'a5_nea.md (first k5, 50% k5, 90% k6)'),
        'American / Alaska': (7, 8, 9.5, 'a3_aa_as.md (first k7, 50% k8, 90% k9-10)'),
        'Alaska / Virgin': (2, 3, 4, 'a4_vx_merge.md (first k2-5, 50% k2-5, 90% k3-5)')}
rows = []
for n, (k10, k50, k90, src) in pace.items():
    rows.append((n, k10, k50, k90, (k90 - k50) / np.log(9), src))
med = np.median([v[:3] for v in pace.values()], axis=0)
rows.append(('Median', *med, (med[2] - med[1]) / np.log(9), 'median of the 5 precedents'))
P = pd.DataFrame(rows, columns=['case', 'k10', 'k50', 'k90', 'scale', 'source_note']); P.to_csv(OUT / 'switch_pace_precedents.csv', index=False)
lg = lambda k, k50, s: 1 / (1 + np.exp(-(k - k50) / s))
kk = np.round(np.arange(0, 11.25, 0.1), 2)
C = pd.DataFrame({'k': kk})
for n, k10, k50, k90, s, _ in rows: C[n] = 100 * lg(kk, k50, s)
C.to_csv(OUT / 'switch_pace_s_curves.csv', index=False)
# model ramp: 3.1%/yr -> 0.775%/qtr from Q4'26, cap 6%
q = [f"Q{(i + 3) % 4 + 1}'{26 + (i + 3) // 4}" for i in range(8)]
ramp = pd.DataFrame({'quarter': q, 'k_from_Q4_26': range(8), 'switched_pct': [min(0.775 * (i + 1), 6.0) for i in range(8)]})
ramp.to_csv(OUT / 'model_ramp_quarterly.csv', index=False)
print(P.round(3).to_string(index=False)); print(ramp.to_string(index=False))
print('3.1/4 =', 3.1 / 4, ' (6-5)/ln9 =', round(1 / np.log(9), 3))
