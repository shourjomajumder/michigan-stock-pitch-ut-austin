import numpy as np
pace = {'Delta / Alaska': (4, 5, 6), 'Continental / Northwest': (0, 0.5, 3),
        'American / JetBlue': (4, 5, 6), 'American / Alaska': (7, 8, 9.5),
        'Alaska / Virgin': (2, 3, 4)}
pace['Median'] = tuple(np.median(list(pace.values()), axis=0))
for name in ('Continental / Northwest', 'Median', 'American / Alaska'):
    k10, k50, k90 = pace[name]
    print(f'{name}: 50% at {k50:g}, scale {(k90 - k50) / np.log(9):.3f}')
k50, s = 5, (6 - 5) / np.log(9)
f = lambda k: 1 / (1 + np.exp(-(k - k50) / s))
for q, k in [('Q4 2026', 2), ('Q3 2027', 5), ('Q4 2027', 6)]:
    print(f'{q}, quarter {k}: {f(k):.0%} of eventual')
