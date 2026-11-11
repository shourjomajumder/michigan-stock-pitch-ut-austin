"""Build processed/same_airport_gaps.csv from raw Google Flights captures.

Method = fares/README.md (NYC 18 routes):
  per route-date gap = JetBlue lowest posted nonstop economy fare (Blue Basic allowed)
                       minus United lowest posted nonstop economy fare (Basic Economy allowed),
                       same airports, same date, one-way USD;
  route gap = mean over dates after dropping the single date with the largest |gap|, rounded to $1.
Run from repo root or anywhere: python3 code/build_same_airport_gaps.py
"""
import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import csv, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RAW = os.path.join(ROOT, 'raw', _os.path.join(_R, 'data/flights_and_fares/fares_recheck/raw/google_flights_same_airport_captures.jsonl'))
OUT = os.path.join(ROOT, 'processed', _os.path.join(_R, 'data/flights_and_fares/fares_recheck/processed/same_airport_gaps.csv'))
OUT_SUM = os.path.join(ROOT, 'processed', _os.path.join(_R, 'data/flights_and_fares/fares_recheck/processed/same_airport_route_summary.csv'))
SLIDE = {'BOS-LAX': 0, 'BOS-SFO': 3, 'FLL-SFO': -2, 'FLL-IAH': -9}

rows = []
for line in open(RAW, encoding='utf-8'):
    c = json.loads(line)
    ap = c['route'].replace('-', '–')
    jb = [r[2] for r in c['rows'] if r[0] == 'JetBlue' and r[1] == ap]
    ua = [r[2] for r in c['rows'] if r[0] == 'United' and r[1] == ap]
    if not jb or not ua:
        continue
    rows.append(dict(route=c['route'], date=c['date'], jetblue_fare=min(jb), united_fare=min(ua),
                     gap=min(jb) - min(ua), n_obs=len(jb) + len(ua), capture_ts=c['capture_ts']))
rows.sort(key=lambda r: (r['route'], r['date']))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['route', 'date', 'jetblue_fare', 'united_fare', 'gap', 'n_obs', 'capture_ts'])
    w.writeheader(); w.writerows(rows)

summ = []
for route in SLIDE:
    g = [r for r in rows if r['route'] == route]
    gaps = [r['gap'] for r in g]
    drop = max(range(len(g)), key=lambda i: abs(gaps[i]))
    kept = [x for i, x in enumerate(gaps) if i != drop]
    m = sum(kept) / len(kept)
    rg = int(m + 0.5) if m >= 0 else -int(-m + 0.5)
    summ.append(dict(route=route, n_dates=len(g), n_obs=sum(r['n_obs'] for r in g),
                     mean_all=round(sum(gaps) / len(gaps), 2), dropped_date=g[drop]['date'], dropped_gap=gaps[drop],
                     gap_mean_ex_largest=round(m, 2), rerun_gap_rounded=rg, slide_gap=SLIDE[route],
                     matches_slide=rg == SLIDE[route]))
with open(OUT_SUM, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(summ[0])); w.writeheader(); w.writerows(summ)
for s in summ:
    print(s)
