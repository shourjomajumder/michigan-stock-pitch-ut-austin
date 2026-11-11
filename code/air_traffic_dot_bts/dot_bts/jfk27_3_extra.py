"""Extra checks: (1) TWFE with Alaska seat share as covariate (Alaska left JFK-LAX 2021-22); (2) sharp monthly exit test Oct->Nov 2022."""
import numpy as np, pandas as pd, itertools
import os as _os
src = open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'jfk27_3_history.py')).read()
exec(src[:src.index('results = []')])
R5 = TREAT + CTRL
def twfe2(d, y, xs, routes):
    d = d[d.x.isin(routes)].dropna(subset=[y] + xs).copy(); d['rq'] = d.x + '_' + d.quarter.astype(str)
    X = pd.get_dummies(d[['rq']].astype(str)).astype(float)
    X = pd.concat([X, pd.get_dummies(d.yq.astype(str), prefix='t', drop_first=True).astype(float)], axis=1)
    for i, x in enumerate(xs): X.insert(i, x, d[x].values)
    return np.linalg.lstsq(X.values, d[y].values, rcond=None)[0][:len(xs)]
rows = []
for sub_lab, sub in [('all', S), ('end2024_no2021H1', S[(S.yq <= 20244) & ~S.yq.isin([20211, 20212])])]:
    for y in ['B6_share', 'B6_seat_share', 'DL_share', 'AA_share']:
        b = twfe2(sub, y, ['UA_seat_share', 'AS_seat_share'], R5)
        # route placebo for UA dose holding AS covariate
        paths = {t: sub[sub.x == t].set_index('yq').UA_seat_share for t in TREAT}
        pl = []
        for a, c in itertools.permutations(R5, 2):
            if {a, c} == set(TREAT): continue
            d = sub.copy(); d['pd'] = 0.0
            for tgt, s in [(a, 'LAX'), (c, 'SFO')]:
                m = d.x == tgt; d.loc[m, 'pd'] = d.loc[m, 'yq'].map(paths[s]).fillna(0).values
            pl.append(twfe2(d, y, ['pd', 'UA_seat_share', 'AS_seat_share'], R5)[0])
        pl = np.array(pl)
        rows.append(dict(sample=sub_lab, y=y, UA_per10=b[0] * 10, AS_seat_coef_per10=b[1] * 10,
                         placebo_sd=pl.std() * 10, placebo_p=(np.sum(np.abs(pl) >= abs(b[0])) + 1) / (len(pl) + 1)))
A = pd.DataFrame(rows); print(A.round(2).to_string())
A.round(3).to_csv(OUT + 'did_with_alaska_control.csv', index=False)

# sharp monthly exit: mean(Nov-Dec) - mean(Sep-Oct), 2022 (UA leaves end Oct) vs same window 2019, 2021, 2023
M2 = M[M.route.isin(['JFK-LAX', 'JFK-SFO', 'BOS-LAX', 'BOS-SFO'])]
out = []
for r, g in M2.groupby('route'):
    for yr in [2019, 2021, 2022, 2023]:
        a = g[(g.year == yr) & g.month.isin([9, 10])]; b = g[(g.year == yr) & g.month.isin([11, 12])]
        if len(a) == 2 and len(b) == 2:
            row = dict(route=r, year=yr)
            for v in ['UA_seat_share', 'B6_share', 'B6_seat_share', 'DL_share', 'AA_share', 'B6_LF']:
                row['d_' + v] = b[v].mean() - a[v].mean()
            out.append(row)
X = pd.DataFrame(out)
base = X[X.year != 2022].groupby('route').mean(numeric_only=True).drop(columns='year')
ex = X[X.year == 2022].set_index('route').drop(columns='year') - base
ex.columns = [c + '_2022_minus_avg_2019_21_23' for c in ex.columns]
X.round(2).to_csv(OUT + 'monthly_exit_sepoct_to_novdec.csv', index=False)
ex.round(2).to_csv(OUT + 'monthly_exit_2022_excess.csv')
print(X.round(2).to_string()); print(ex.round(2).to_string())
