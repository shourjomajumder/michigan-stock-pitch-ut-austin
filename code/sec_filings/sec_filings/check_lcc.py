"""Compare hand-typed LCC panels (frontier/raw/*_quarterly_ops_*.csv) and frontier/processed/lcc_quarters.csv
with values from earnings releases / 10-Qs (code/filing_values.py, raw extracts in ../raw/).
Run from sec_filings/code:  python3 check_lcc.py   -> ../processed/lcc_quarters_check.csv"""
import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from filing_values import FRONTIER, ALLEGIANT, SUNCOUNTRY

FR = _os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier') + '/'
f = pd.read_csv(FR + 'raw/frontier_quarterly_ops_2019Q1_2026Q3.csv').set_index('quarter')
a = pd.read_csv(FR + 'raw/allegiant_quarterly_ops_2018Q3_2026Q3.csv').set_index('quarter')
s = pd.read_csv(FR + 'raw/suncountry_quarterly_ops_2022Q2_2026Q1.csv').set_index('quarter')
lcc = pd.read_csv(FR + 'processed/lcc_quarters.csv')
rows = []
def add(airline, field, q, ours, filing, ok, note, url):
    rows.append(dict(airline=airline, field=field, quarter=q, our_value=ours, filing_value=filing,
                     match=ok, note=note, source_url=url))
def cmp(airline, field, q, ours, filing, tol, url, note=''):
    add(airline, field, q, ours, filing, 'yes' if abs(ours - filing) <= tol + 1e-9 else 'NO', note, url)

# Frontier
for q, r in f.iterrows():
    if q not in FRONTIER:
        for c in ['rpm_m', 'asm_m', 'load_factor_pct', 'passenger_revenue_usd_m', 'fare_revenue_usd_m', 'passengers_k']:
            add('Frontier', c, q, r[c], '', 'not checked', 'no filing fetched (quarter not used in lcc_quarters)', '')
        continue
    pax, rpm, asm, lf, prev, fpp, url = FRONTIER[q]
    cmp('Frontier', 'rpm_m', q, r.rpm_m, rpm, 0, url)
    cmp('Frontier', 'asm_m', q, r.asm_m, asm, 0, url)
    cmp('Frontier', 'load_factor_pct', q, r.load_factor_pct, lf, 0.05, url)
    cmp('Frontier', 'passenger_revenue_usd_m', q, r.passenger_revenue_usd_m, prev, 0, url)
    cmp('Frontier', 'passengers_k', q, r.passengers_k, pax, 0, url)
    cmp('Frontier', 'fare_revenue_usd_m', q, r.fare_revenue_usd_m, round(fpp * pax / 1000, 1), 1.0, url,
        f'filing value derived = fare revenue per passenger ${fpp} x passengers (no quarterly fare-revenue line); tolerance $1M')

# Allegiant
for q, r in a.iterrows():
    if q not in ALLEGIANT:
        for c in ['rpm_m', 'asm_m', 'load_factor_pct', 'passenger_revenue_usd_m', 'passengers_k', 'fare_per_pax_usd']:
            add('Allegiant', c, q, r[c], '', 'not checked', 'no filing fetched (quarter not used in lcc_quarters)', '')
        continue
    paxt, asmt, rpm, asms, lf, prev, fare, url = ALLEGIANT[q]
    cmp('Allegiant', 'rpm_m', q, r.rpm_m, rpm, 0.006, url, 'scheduled service RPM')
    if abs(r.asm_m - asms) <= 0.006:
        add('Allegiant', 'asm_m', q, r.asm_m, round(asms, 2), 'yes (scheduled)',
            f'equals SCHEDULED-service ASM; total-system ASM is {asmt:.2f}. Basis differs across quarters (see README)', url)
    elif abs(r.asm_m - asmt) <= 0.006:
        add('Allegiant', 'asm_m', q, r.asm_m, round(asmt, 2), 'yes (total system)',
            f'equals TOTAL-SYSTEM ASM; scheduled ASM (same basis as RPM/LF) is {asms:.2f}. Basis differs across quarters (see README)', url)
    else:
        add('Allegiant', 'asm_m', q, r.asm_m, round(asms, 2), 'NO', f'matches neither scheduled nor total ({asmt:.2f})', url)
    note = 'scheduled service LF'
    if abs(r.load_factor_pct - lf) > 0.05 and abs(r.load_factor_pct - r.rpm_m / r.asm_m * 100) < 0.05:
        note += '; our value = RPM / total-system ASM, not the reported LF'
    cmp('Allegiant', 'load_factor_pct', q, r.load_factor_pct, lf, 0.05, url, note)
    tol = 0.05 if prev == round(prev, 1) and abs(prev * 1000 - round(prev * 1000)) < 1e-6 and len(str(prev).split('.')[-1]) <= 1 else 0.006
    cmp('Allegiant', 'passenger_revenue_usd_m', q, r.passenger_revenue_usd_m, prev, tol, url,
        'filing rounded to $0.1M' if tol == 0.05 else '')
    cmp('Allegiant', 'passengers_k', q, r.passengers_k, paxt, 0.006, url, 'total-system passengers')
    cmp('Allegiant', 'fare_per_pax_usd', q, r.fare_per_pax_usd, fare, 0.006, url, 'average fare - total')

# Sun Country
for q, r in s.iterrows():
    rpm, asms, asmt, lf, prev, url = SUNCOUNTRY[q]
    cmp('Sun Country', 'rpm_m', q, r.rpm_m, rpm, 0.006, url, 'scheduled service RPM')
    if abs(r.asm_total_m - asmt) <= 0.006:
        add('Sun Country', 'asm_total_m', q, r.asm_total_m, round(asmt, 2), 'yes', 'total-system ASM (not used by build script)', url)
    elif abs(r.asm_total_m - asms) <= 0.006:
        add('Sun Country', 'asm_total_m', q, r.asm_total_m, round(asmt, 2), 'NO',
            f'our value is SCHEDULED ASM ({asms:.2f}), column is labelled total; not used by build script (ASM = RPM/LF)', url)
    else:
        add('Sun Country', 'asm_total_m', q, r.asm_total_m, round(asmt, 2), 'NO',
            f'matches neither total nor scheduled ({asms:.2f}); not used by build script', url)
    cmp('Sun Country', 'load_factor_pct', q, r.load_factor_pct, lf, 0.05, url, 'scheduled service LF')
    cmp('Sun Country', 'passenger_revenue_usd_m', q, r.passenger_revenue_usd_m, prev, 0.006, url,
        'total passenger revenue (scheduled + charter + ancillary)')

# lcc_quarters re-derived from filings (same formulas as frontier/code/build_lcc_quarters.py)
def series(name):
    out = {}
    if name == 'Frontier':
        for q, v in FRONTIER.items(): out[q] = (v[4] / v[1], v[1], v[2], v[6])
    elif name == 'Allegiant':   # scheduled ASM, consistent with RPM and LF
        for q, v in ALLEGIANT.items(): out[q] = (v[5] / v[2], v[2], v[3], v[7])
    else:                       # build script uses ASM = RPM / LF
        for q, v in SUNCOUNTRY.items(): out[q] = (v[4] / v[0], v[0], v[0] / (v[3] / 100), v[5])
    return out
g = lambda n, o: round((n / o - 1) * 100, 2)
for _, r in lcc.iterrows():
    d = series(r.airline); q = r.quarter; b = f'{int(q[:4]) - 1}{q[4:]}'
    if q not in d or b not in d:
        for c in ['fare', 'traffic', 'seats']:
            add(r.airline, 'lcc_quarters.' + c, q, r[c], '', 'not checked', 'filing missing', '')
        continue
    url = d[q][3] + ' ; ' + d[b][3]
    tol = 0.15 if r.airline == 'Sun Country' else 0.05
    for c, i in [('fare', 0), ('traffic', 1), ('seats', 2)]:
        new = g(d[q][i], d[b][i])
        if r.airline == 'Allegiant' and c == 'seats':
            tot = g(ALLEGIANT[q][1], ALLEGIANT[b][1])
            if abs(r[c] - tot) <= tol:
                add(r.airline, 'lcc_quarters.seats', q, r[c], tot, 'yes (total system)',
                    f'YoY % of total-system ASM; scheduled-service basis would be {new}', url)
            elif abs(r[c] - new) <= tol:
                add(r.airline, 'lcc_quarters.seats', q, r[c], new, 'yes (scheduled)',
                    f'YoY % of scheduled ASM; total-system basis would be {tot}', url)
            else:
                add(r.airline, 'lcc_quarters.seats', q, r[c], tot, 'NO',
                    f'mixes bases (scheduled ASM this year / total-system ASM prior year). Consistent: total {tot}, scheduled {new}', url)
            continue
        note = 'YoY %, recomputed from filings'
        if r.airline == 'Sun Country' and c == 'seats': note += ' using ASM = RPM / reported LF (1-dp LF; tolerance 0.15pp); reported scheduled ASM growth = ' + str(g(SUNCOUNTRY[q][1], SUNCOUNTRY[b][1]))
        cmp(r.airline, 'lcc_quarters.' + c, q, r[c], new, tol, url, note)

out = pd.DataFrame(rows)
out.to_csv(_os.path.join(_R, 'data/sec_filings/processed/lcc_quarters_check.csv'), index=False)
print(out.match.value_counts().to_string())
print(out[~out.match.str.startswith(('yes','not'))][['airline', 'field', 'quarter', 'our_value', 'filing_value', 'note']].to_string())
