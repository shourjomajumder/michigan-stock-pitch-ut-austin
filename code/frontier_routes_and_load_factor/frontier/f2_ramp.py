import pandas as pd
SEAT, RASM, ramp = 230, 0.1187, [0.85, 1.05, 1.15, 1.20]
routes = [('Las Vegas–Oakland', '2026-08-20', 11, 407), ('Las Vegas–Boise', '2026-09-10', 4, 520),
          ('Nashville–Tampa', '2026-10-09', 2, 612), ('Denver–Fort Lauderdale', '2026-11-20', 7, 1703),
          ('Ontario–Oakland', '2026-11-21', 4, 361), ('Orlando–Cartagena', '2026-12-19', 1, 1340)]
rows = []
for name, start, flights, miles in routes:
    s = pd.Period(start, 'M')
    for m in [m for m in pd.period_range('2026-10', '2027-09', freq='M') if m >= s]:
        part = 0.4 if m == s and pd.Timestamp(start).day > 15 else 1
        asm = flights * 2 * SEAT * 30.4 / 7 * part * miles
        idx = ramp[min((m - s).n // 3, 3)]
        rows.append((name, str(m.asfreq('Q')), asm * RASM * (idx - 1) / 1e6))
t = pd.DataFrame(rows, columns=['route', 'q', 'usd_m']).pivot_table('usd_m', 'route', 'q', 'sum')
t = t.reindex([r[0] for r in routes]).fillna(0).rename_axis(None).rename_axis(None, axis=1)
t.loc['Total'] = t.sum()
print(t.round(1) + 0.0)
print(t.loc['Total'].round(2).to_dict(), 'net', round(t.loc['Total'].sum(), 1))
