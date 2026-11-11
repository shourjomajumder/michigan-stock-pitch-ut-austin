"""Sensitivity of the headline dose estimate (B6 pax share per +10pp UA seat share). Reuses 3_history.py definitions."""
import numpy as np, pandas as pd
import os as _os
src = open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '3_history.py')).read()
exec(src[:src.index('results = []')])
R5 = TREAT + CTRL; R8 = TREAT + CTRL_ALT
S0 = S.copy(); rows = []
def est(label, sub, routes, y='B6_share'):
    global S
    S = sub
    bh = twfe(S, y, 'UA_seat_share', routes)[0]
    pv, p = placebo_routes(S, y, 'UA_seat_share', routes, bh)
    tv = placebo_time(S, y, 'UA_seat_share', routes) if (S.yq >= 20231).sum() > 0 and len(sorted(q for q in S.yq.unique() if q >= 20231)) >= 8 else np.array([np.nan])
    rows.append(dict(variant=label, y=y, per10=bh * 10, route_placebo_p=p, route_placebo_sd=np.std(pv) * 10, time_placebo_sd=np.nanstd(tv) * 10, n=len(S[S.x.isin(routes)])))
    S = S0
for y in ['B6_share', 'B6_seat_share', 'B6_LF', 'DL_share', 'AA_share', 'AS_share', 'B6AA_share']:
    est('A all 2019,2021Q1-2026Q2; 5 ctrl', S0, R5, y)
    est('B drop 2021H1 ramp', S0[~S0.yq.isin([20211, 20212])], R5, y)
    est('C end 2024Q4 (pre-specified POST)', S0[S0.yq <= 20244], R5, y)
    est('D end 2024Q4, drop 2021H1', S0[(S0.yq <= 20244) & ~S0.yq.isin([20211, 20212])], R5, y)
    est('E 8 controls, all', S0, R8, y)
    est('F 8 controls, end 2024Q4, drop 2021H1', S0[(S0.yq <= 20244) & ~S0.yq.isin([20211, 20212])], R8, y)
    est('G LAX only treated (SFO dropped)', S0[S0.x != 'SFO'], ['LAX'] + CTRL, y) if False else None
out = pd.DataFrame(rows); out.round(3).to_csv(OUT + 'did_sensitivity.csv', index=False)
print(out.round(2).to_string())
# per-route dose estimate (LAX vs controls, SFO vs controls), simple TWFE without placebo
for t in TREAT:
    for y in ['B6_share', 'B6_seat_share', 'DL_share', 'AS_share']:
        print(t, y, round(twfe(S0, y, 'UA_seat_share', [t] + CTRL)[0] * 10, 2))
