# fares_recheck/ : rerun of the 4 unsourced same-airport base-fare gaps (JetBlue vs United)

Re-collects the four same-airport routes on appendix slide E2 that had no quote set on disk (see fares/README.md,
"NOT REPRODUCED" row): BOS-LAX, BOS-SFO, FLL-SFO, FLL-IAH. EWR-FLL and EWR-PBI were already rebuilt in fares/ and are not repeated.
No Bloomberg or broker data in this folder.

Method (same as fares/README.md, NYC 18 routes): one-way, nonstop, same origin and destination airports, same travel date;
per route-date gap = JetBlue lowest posted economy fare (Blue Basic allowed) minus United lowest posted economy fare
(Basic Economy allowed), USD; route gap = mean over the 8 dates after dropping the single largest-|gap| date, rounded to $1.
Dates: the 8 Wednesdays used for the EWR same-airport rebuild (2026-12-02, 12-09, 2027-01-13, 01-27, 02-03, 02-10, 02-24, 03-03).
Rebuild: `python3 code/build_same_airport_gaps.py` (standard library only).

## Files
| file | what it is | source | used on slide(s) |
|---|---|---|---|
| raw/google_flights_same_airport_captures.jsonl | 32 captures (4 routes x 8 dates): search URL, capture timestamp (UTC), page inputs echo, every nonstop row (airline, airports, price, carry-on/checked bag icons, departure time) | Google Flights, google.com/travel/flights, captured 2026-11-11 20:16-20:32 UTC (our collection, not signed in) | E2 |
| raw/gf_raw_log.jsonl | original capture from the stopped run (BOS-LAX 2026-12-02 only, no URL field); copied into the file above with its URL taken from _tmp/batch_2026-12-02.json | Google Flights, 2026-11-11 (our collection) | E2 (input) |
| code/build_same_airport_gaps.py | builds both processed files from raw/google_flights_same_airport_captures.jsonl | our code | E2 |
| code/ext.js | in-page extractor run on each Google Flights results page (the rerun used the same logic with the URL dropped from the returned JSON) | our code | none (collection tool) |
| processed/same_airport_gaps.csv | route, date, jetblue_fare, united_fare, gap, n_obs (= number of JetBlue + United nonstop rows on the page), capture_ts | code/build_same_airport_gaps.py | E2 |
| processed/same_airport_route_summary.csv | per route: mean of all dates, dropped date, mean ex largest, rounded rerun gap, slide gap, match flag | code/build_same_airport_gaps.py | E2 |
| _tmp/batch_*.json | browser command plans (navigate + extractor) prepared by the stopped run; they contain no results | our code | none |

## Rerun vs slide
| route | slide gap | rerun gap (mean ex largest, rounded) | mean of all 8 dates | dropped date (gap) | match? |
|---|---|---|---|---|---|
| BOS-LAX | 0 | +1 (+1.43) | +4.50 | 2027-02-10 (+26) | no, off by $1 (5 of 8 dates exactly $0) |
| BOS-SFO | +3 | 0 (0.00) | +6.25 | 2026-12-02 (+50) | no, off by $3 (7 of 8 dates exactly $0) |
| FLL-SFO | -2 | 0 (0.00) | 0.00 | 2026-12-02 (0) | no, off by $2 (8 of 8 dates exactly $0) |
| FLL-IAH | -9 | -27 (-27.14) | -27.50 | 2026-12-02 (-30) | no: JetBlue $49-59 vs United $79 on every date |

Four-route average: slide (0+3-2-9)/4 = -2.00; rerun (1+0+0-27)/4 = -6.50. Six-route same-airport average with the rebuilt
EWR-FLL -1 and EWR-PBI -2: slide -1.83, rerun (1+0+0-27-1-2)/6 = -4.83.
Reading: BOS-LAX, BOS-SFO and FLL-SFO confirm near-parity (within $3 of the slide; the slide's sign/size is not reproduced
exactly). FLL-IAH does not match: JetBlue is about $20-30 cheaper than United on every date checked.

Caveats: quotes are as posted on 2026-11-11 for Dec 2026-Mar 2027 travel, so they differ from whenever the slide quotes
were taken. Google Flights shows one price per flight (the lowest fare); United rows show a 0 carry-on icon (Basic Economy),
JetBlue rows a 1 carry-on icon, so both are each carrier's lowest fare product. Frontier also flies FLL-IAH nonstop
($19-70) but is outside the JetBlue-vs-United comparison.
