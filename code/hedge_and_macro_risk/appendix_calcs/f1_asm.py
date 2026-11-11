import pandas as pd

routes = [('LAS-OAK', '2026-08-20', 11, 407),
          ('LAS-BOI', '2026-09-10', 4, 520),
          ('BNA-TPA', '2026-10-09', 2, 612),
          ('DEN-FLL', '2026-11-20', 7, 1703),
          ('ONT-OAK', '2026-11-21', 4, 361),
          ('MCO-CTG', '2026-12-19', 1, 1340)]
months = pd.period_range('2026-10', '2027-09', freq='M')
rows = []
for name, start, weekly, miles in routes:
    s = pd.Timestamp(start)
    first = s.to_period('M')
    for m in months:
        if m < first: continue
        part = 0.4 if m == first and s.day > 15 else 1
        seats = weekly * 2 * 230 * 30.4 / 7 * part
        q = str(m.asfreq('Q'))
        rows.append((name, q, seats * miles / 1e6))
t = pd.DataFrame(rows, columns=['route', 'q', 'asm'])
t = t.pivot_table('asm', 'route', 'q', 'sum',
                  sort=False).round(2)
t = t.rename_axis(None).rename_axis(None, axis=1)
t.loc['Total'] = t.sum()
print(t.to_string(float_format='{:.2f}'.format))
cap = t.loc['Total', '2027Q1'] / 11419
print('added capacity:', f'{cap:.1%}')
