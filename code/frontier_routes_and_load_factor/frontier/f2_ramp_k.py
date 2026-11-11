import pandas as pd

SEAT, RASM, ramp = 230, 0.1187, [0.85, 1.05, 1.15, 1.20]
routes = [('LAS-OAK', '2026-08-20', 11, 407), ('LAS-BOI', '2026-09-10', 4, 520),
          ('BNA-TPA', '2026-10-09', 2, 612), ('DEN-FLL', '2026-11-20', 7, 1703),
          ('ONT-OAK', '2026-11-21', 4, 361), ('MCO-CTG', '2026-12-19', 1, 1340)]
rows = []
for name, start, weekly, miles in routes:
    s = pd.Timestamp(start); first = s.to_period('M')
    for m in pd.period_range('2026-10', '2027-09', freq='M'):
        if m < first: continue
        part = 0.4 if m == first and s.day > 15 else 1
        asm = weekly * 2 * SEAT * 30.4 / 7 * part * miles
        idx = ramp[min((m - first).n // 3, 3)]
        rows.append((name, str(m.asfreq('Q')), asm * RASM * (idx - 1) / 1e3))
t = pd.DataFrame(rows, columns=['route', 'q', 'k'])
t = t.pivot_table('k', 'route', 'q', 'sum', sort=False).fillna(0).round().astype(int)
t = t.rename_axis(None).rename_axis(None, axis=1)
t['Net'] = t.sum(axis=1)
t.loc['Total'] = t.sum()
print(t.to_string())
print('run-rate ($M/yr):', round(t.loc['Total', '2027Q3'] * 4 / 1e3, 2))
