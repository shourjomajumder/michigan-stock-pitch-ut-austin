# fares/ : base-fare parity data (JetBlue vs United)

Supports JetBlue Thesis 1 (switching passenger base 2.316M): appendix slide E2 "Shared-Route Base-Fare Parity"
(same-airport list avg -$4.83 with FLL-IAH at -$27 from the recheck, see SOURCES_fares_recheck.md; NYC 18-route list avg -$1.94), slide JFK1 (JFK-SFO / JFK-LAX checks), the international
pair check, and the DOT-vs-live calibration. No Bloomberg or broker data in this folder.

Rebuild: `python3 code/calibration.py && python3 code/nyc_parity.py && python3 code/jfk27_5_fares_build.py && python3 code/build_nyc_parity.py write && python3 code/build_fare_tables.py`
(all paths repo-relative; pandas only).

Gap convention everywhere: JetBlue minus United, USD one-way, lowest posted nonstop economy fare (basic allowed).
NB: column `diff` in Shared_routes_fares_full.csv is United minus JetBlue.

## Slide-number reconciliation
| Slide number | Status | File |
|---|---|---|
| NYC 18 routes, avg -$1.94 (10 shown + BQN +7, PHX -3, CHS 0, DEN 0, SLC -6, MSY 0, IAH 0, CLE 0) | REBUILT 18/18 from raw quotes. Rule: per route-date gap = JetBlue lowest at JFK/LGA minus United lowest at EWR (LGA for DEN, IAH); route gap = mean over all dates after dropping the single largest-abs-gap date, rounded to $1; average of 18 rounded gaps = -35/18 = -1.944 | processed/nyc_18_route_gaps.csv, nyc_18_route_date_gaps.csv |
| 5.533M JetBlue JFK+LGA passengers on the 18 routes | REBUILT (5,532,906) | processed/nyc_18_route_gaps.csv (from raw/t100_context/bluesky_nyc_overlap.csv) |
| Same airports: EWR-FLL -1, EWR-PBI -2 | REBUILT with the same rule (JetBlue EWR vs United EWR, 8 dates) | processed/same_airport_6_routes.csv |
| Same airports: BOS-LAX 0, BOS-SFO +3, FLL-SFO -2, FLL-IAH -9 | NOT REPRODUCED: no rule applied to the 458-quote file (or fares_scrape/live.csv) gives all four; per-route quote set behind them not on disk. Slide values kept; closest file-based stats (mean/median/share within $15) shown alongside | processed/same_airport_6_routes.csv, shared_routes_458_quotes_pair_stats.csv |
| Same-airport avg -$1.83 = (0+3-2-9-1-2)/6 | arithmetic on the 6 slide values | same_airport_6_routes.csv |
| 1.616M same-airport passengers | T-100 Aug25-Jul26 sum = 1,616,302 (slide uses EWR-PBI 188.8k from bluesky_nyc_overlap L4Q instead of 189.1k; both round to 1.616M) | same_airport_6_routes.csv |
| JFK-SFO within $15 on 6 of 6 dates; JFK-LAX 3 of 6 | REBUILT | processed/jfk_transcon_check_summary.csv, jfk_transcon_check_by_date.csv |
| International: match PUJ, MBJ, NAS; no match STI, SDQ, CUN, AUA, SXM, LHR, PLS, SJO | REBUILT (median within 10% and >=3 dates within 10%) | processed/intl_pairs_fare_check.csv |
| "Live base fares, 458 quotes" (data-sources slide) | file | raw/google_flights/shared_routes/Shared_routes_fares_full.csv |
| Old slide 28 monthly transcon gaps (+$0.20 over 10 route-months) | SUPERSEDED, no source file found | archive/slide28_old_transcon_monthly_gaps_SUPERSEDED.csv |

## Files
| file | what it is | source | used on slide(s) |
|---|---|---|---|
| raw/google_flights/t1s2/live_jfk_ewr.csv/.md | round 1: 12 NYC routes x 4 dates, JetBlue vs United lowest nonstop | Google Flights, searched 2026-11-11 (our collection) | E2 |
| raw/google_flights/t1s2/raw.txt, batch_*.json, ext.js | raw per-search lines and the in-page extractor | Google Flights (our collection) | E2 (input) |
| raw/google_flights/t1s2/calibration.md, nyc_parity.md/.csv | write-ups: DOT Table 1a gap is mix-biased (~-$75) so live quotes are used | our analysis | E2 rationale |
| raw/google_flights/rv_fares/agent_01..21,23 (.csv/.md/_raw.txt), BRIEF.md, work02/, work23/ | round 2: 40 route-sets x 4 dates (new routes Dec-Jan, re-tests Feb-Mar 2027), agent 21/23 EWR same-airport checks (agent 22 output never saved) | Google Flights, 2026-11-11 (our collection) | E2, international check |
| raw/google_flights/jfk27/5_fares.csv/.md, 5_work/, _orig_scripts/ | JFK-LAX/SFO, 6 dates, JetBlue/Delta/American/Alaska JFK vs United EWR, fare tiers, business | Google Flights, 2026-11-11 | JFK1 |
| raw/google_flights/shared_routes/Shared_routes_fares_full.csv | 458 quotes, 13 BOS/FLL/EWR shared pairs both directions, travel 2026-11-18 to 2027-04-10 | Google Flights (our collection) | E2, data-sources slide, calibration |
| raw/google_flights/shared_routes/Shared_routes_live_fares.csv, Shared_routes_premium_fares.csv | 40-quote 4-date economy pass and premium-cabin pass on shared pairs | Google Flights (our collection) | supporting |
| raw/google_flights/fares_scrape/* | live.csv / premium.csv (= the two files above) plus browser navigation/extraction logs (b_*.json, nav_*.json, ex.json) | Google Flights (our collection) | supporting |
| raw/google_flights/fares2/raw.txt | index-coded dump (route idx, date idx, fare, fare); key not found, kept for completeness | Google Flights (our collection) | none |
| raw/dot/dot_car_table1a_jfk_ewr_2019_2026q1.csv, dot_car_table1a_bos_ewr_2023_2026q1.csv | DOT Consumer Airfare Report Table 1a pulls | DOT, https://data.transportation.gov (Consumer Airfare Report Table 1a) | calibration, nyc_parity |
| raw/dot/DOT_paid_fares_JetBlue_vs_United_Jul2025-Jul2026.csv, Base_fare_DOT_task_prompt.md | DB1C paid-fare comparison on 19 shared pairs and the method used to build it | BTS DB1C public market files (bts.gov) | supporting |
| raw/t100_context/same_airport_pairs.*, intl_pairs.*, bluesky_nyc_overlap.csv, 4_full_overlap.csv | T-100 passenger counts by pair (JetBlue/United) | BTS TranStats T-100, pulled 2026-11-11 | E2 passenger columns |
| processed/nyc_18_route_gaps.csv, nyc_18_route_date_gaps.csv | rebuilt NYC 18-route gaps + passengers | code/build_nyc_parity.py | E2 |
| processed/same_airport_6_routes.csv | 6 same-airport routes: slide gap, rebuilt gap where possible, 458-quote stats, passengers | code/build_fare_tables.py | E2 |
| processed/shared_routes_458_quotes_pair_stats.csv | per-pair stats of the 458 quotes | code/build_fare_tables.py | supporting |
| processed/jfk_transcon_check_by_date.csv, _summary.csv, jfk_transcon_quotes_5_fares.csv | JFK-SFO/LAX checks | code/build_fare_tables.py, code/jfk27_5_fares_build.py | JFK1 |
| processed/intl_pairs_fare_check.csv | international pairs: gaps, verdicts, T-100 pax | code/build_fare_tables.py | E2 international line, SUMMARY verdicts |
| processed/google_flights_nyc_quotes_long.csv | every NYC quote from round 1 + agents in one table | code/build_fare_tables.py | all |
| processed/calibration_table.csv, calibration_dot_rows.csv | DOT Table 1a vs live calibration | code/calibration.py | E2 rationale |
| processed/dot_table1a_nyc_parity.csv | DOT Table 1a JFK/LGA vs EWR pairs | code/nyc_parity.py | rationale (DOT not used for parity) |
| processed/table1a_b6_fare_panel.csv | JetBlue Table 1a fare panel by route-quarter | DOT Table 1a (our build in bsky/) | supporting |
| processed/same_fare_routes.csv, parity_points.csv | 25 same-fare route precedent cases (share lost vs depth) | DOT Consumer Airfare Report Tables 1 and 6 (our analysis) | "25 same-fare route cases" / partnership scatter |
| code/bluesky_fares_pipeline/ | optional daily collector (SerpApi; key read from .env, none included) + DOT DB1B/DB1C ingest | our code | not on slides |
| archive/* | superseded: old slide 28 monthly table, v2844 lists (avg -$1.78), 4.746M and 3.104M base write-ups | our analysis | none (superseded) |

Paths inside copied write-ups were replaced with `<workdir>/...`; browser device IDs redacted.
