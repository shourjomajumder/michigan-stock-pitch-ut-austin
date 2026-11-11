# dot_bts — DOT / BTS / FAA public data behind the Hook Em pitch

Everything here is public US government data (BTS T-100, DOT Consumer Airfare Report, DOT Air Travel Consumer Report,
DOT ticket samples, BTS market share via TranStats, FRED copy of the BTS load factor) or our own scripts and tables built from it.
No Bloomberg or broker data. Absolute workspace paths in text files were replaced with "(orig workspace)".

Rebuild the slide numbers: `cd code && python build_slide_tables.py` (asserts every number below).

## Slide numbers and where they come from

| Slide number | Value | File | Note |
|---|---|---|---|
| Industry Overview pie, US domestic market share | DL 17.9, AA 17.7, UA 17.2, WN 17.1, AS 7.1, B6 4.6, F9 3.9, Other 14.5 | processed/slide03_us_domestic_market_share_pie.csv | BTS TranStats home page "Airline Domestic Market Share", Aug 2025 - Jul 2026, fetched 2026-11-11. Other = SkyWest 2.6 + Spirit 2.0 + Envoy 1.2 + Other 8.7. The deck says "June 2026"; the current BTS window is Aug 2025 - Jul 2026, but the values are the same. |
| Industry Overview, US domestic load factor 2025 | 81.7% | processed/slide03_us_domestic_load_factor_2025.csv | REBUILT: mean of the 12 monthly 2025 values of FRED LOADFACTORDD11 (BTS, seasonally adjusted) = 81.68. |
| JetBlue Thesis 1 / appendix E1, on-time 2025 | UA 77.6%, B6 72.3% | processed/slide27_E1_reliability_2025.csv | ATCR Feb 2026. Raw values are UA 77.65 (mainline) and B6 72.34. 77.65 rounds to 77.7, but the slide shows 77.6 (truncated). |
| JetBlue Thesis 1 / E1, cancellations 2025 | UA 1.36%, B6 1.65% | same | UA 1.36 is the NETWORK rate (includes United Express). UA mainline is 0.82. On-time uses mainline, so the two rows use different bases. (1-1.36%)^20 gives 24% and (1-1.65%)^20 gives 28%, both checked. |
| E2 / E5, same-airport routes | 1.616M | processed/slideE2_E5_same_airport_6_routes.csv | T-100 Aug 2025 - Jul 2026 (raw/t100/t100_same_airport_pairs_...). EWR-PBI uses 188,843 from the Q3'25-Q2'26 pull; the Aug-Jul pull has 189,149. |
| E2 / E5, NYC domestic, 18 routes | 5.533M | processed/slideE5_nyc_domestic_18_routes.csv | JFK + LGA JetBlue passengers, T-100 Q3'25-Q2'26 (processed/bluesky_nyc_overlap.csv) |
| E5, NYC international, 5 routes | 1.474M | processed/slideE5_nyc_international_5_routes.csv | JFK-SDQ/PUJ/MBJ/LHR/NAS, T-100 International Aug 2025 - Jul 2026 |
| E5, switching base | 2.316M = 1.616 + 0.553 + 0.147 | processed/slideE5_switching_passenger_base_2316k.csv | FINAL base |
| Slide 28, monthly fare-gap table (BOS-LAX, FLL-SFO, 10 route-months, avg +$0.20) | values only | processed/slide28_monthly_fare_gap_table_VALUES_ONLY.csv | NOT SOURCED: no underlying DOT monthly ticket file was found. Only the slide values are recorded. |
| E3, 25 same-fare route cases | slope 2.62, intercept 0.52, 3.1%/yr at depth 1 | processed/parity_points_25_cases.csv, code/parity.py | Shares come from DOT Consumer Airfare Report Table 6 extracts in raw/dot_car_table6_cases (r04-r08, r10, r02, a1-a5) |
| E4, switching pace, 5 precedents | milestones | raw/dot_car_table6_cases/a1..a5, a10 | Table 6 quarterly shares; the milestone tuples are hard-coded in the appendix slide code (switching model folder) |
| JetBlue Thesis 2 (JFK 2027), JFK transcon history and market | see md files | processed/jfk27_3_*, jfk27_7_market*, jfk27_4_precedents*, hist_* | T-100 panel 2019-2026m7 + Table 1a + Table 6 2015 exit |
| JFK slots (7 daily RT, about 360 JetBlue JFK slots, FAA 10% waiver to Oct 30 2027) | text | raw/faa_slots/jfk_slot_mechanics_notes_2026-11-11.md | Our research notes citing FAA and press sources. No raw FAA file. |

## raw/
| file | what it is | source | used on |
|---|---|---|---|
| t100/t100_nyc_dom_segment_B6_UA_L4Q_2025q3_2026q2.txt | B6 and UA pax/deps by NYC airport-destination, Q3'25-Q2'26 | BTS T-100 Domestic Segment (US carriers), class F, https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FIM | E2, E5 |
| t100/t100_nyc_intl_segment_B6_UA_L4Q_2025q3_2026q2.txt | same, international | BTS T-100 International Segment, gnoyr_VQ=FJE | E5 (memo) |
| t100/t100_same_airport_pairs_B6_UA_aug2025_jul2026.csv/.md | B6 vs UA pax/deps on same-airport pairs | BTS T-100 Domestic Segment, pulled 2026-11-11 | E2, E5 (1.616M) |
| t100/t100_intl_pairs_B6_UA_aug2025_jul2026.csv/.md | B6 vs UA international pairs | BTS T-100 International Segment, pulled 2026-11-11 | E5 (1.474M) |
| t100/t100_panel_jfk_transcon_hub_routes_2019_2026m7.csv | quarterly pax/seats/deps by carrier, JFK/EWR/BOS hub routes | BTS T-100 Domestic Segment | JetBlue Thesis 2, JFK history |
| t100/t100_jfk_top_b6_routes_L4Q_2025q3_2026q2.csv | JetBlue's top JFK routes with carrier split | BTS T-100 | Thesis 2 |
| t100/t100_b6_jfk_vs_system_by_quarter.csv | B6 JFK vs system pax/seats/deps | BTS T-100 | Thesis 2 |
| t100/t100_ua_jfk_monthly_by_aircraft_2021_2022.csv | United JFK 2021-22 by aircraft type | BTS T-100 | Thesis 2 (UA JFK gauge 172 seats) |
| t100/t100_bos_jfk_ewr_transcon_monthly_2019_2026.csv | monthly BOS/JFK/EWR to LAX/SFO by carrier | BTS T-100 | Thesis 2 history |
| t100/t100_jfk_ewr_lax_sfo_monthly_2025_2026m7_raw.txt | fresh monthly re-pull (Nov 11) | BTS T-100 | Thesis 2 market check |
| t100/t100_bos_ewr_routes_B6_UA_AA_DL_2023_2026m7.csv | Boston/Newark routes, 4 carriers, monthly | BTS T-100 | Blue Sky verification, precedent screen |
| t100/t100_carrier_month_totals.csv | carrier monthly totals | BTS T-100 | checks |
| dot_car_table1a/*.csv | Consumer Airfare Report Table 1a rows (JFK/EWR 2019-26Q1, BOS/EWR 2023-26Q1, UA-B6 pairs, 2024 calibration rows) | https://data.transportation.gov (Consumer Airfare Report Table 1a) | Thesis 1/2 fare context, calibration |
| dot_car_table6_cases/* | Table 6 largest/low-fare carrier share extracts for switching precedents | data.transportation.gov resource yj5y-b2ir and 4f3n-jbg2; older PDFs and GAO, as each md says | E3, E4, Thesis 1 slide 28 |
| atcr/c1_ontime.csv, c4_cancel.csv (+md) | annual on-time and cancellation by carrier, 2006-2025 | DOT Air Travel Consumer Report (Feb issues; 2025 = Feb 2026 ATCR) | Thesis 1, E1 |
| bts_market_share/bts_airline_domestic_market_share_aug2025_jul2026.csv | carrier domestic shares | https://www.transtats.bts.gov/ (home page panel), fetched 2026-11-11 (REBUILT, deck chart was linked to a personal workbook) | Industry Overview pie |
| fred/LOADFACTORDD11_2025_2026.csv | monthly US domestic load factor, SA | https://fred.stlouisfed.org/data/LOADFACTORDD11, fetched 2026-11-11 (REBUILT) | Industry Overview 81.7% |
| db1b_paid_fares/DOT_paid_fares_JetBlue_vs_United_Jul2025-Jul2026.csv | average paid fare by route, B6 vs UA, from DOT ticket samples | DOT DB1B/DB1C (via the bluesky_fares pipeline) | supporting only; not on final slides (older appendix H1) |
| faa_slots/jfk_slot_mechanics_notes_2026-11-11.md | JFK slot terms, FAA waiver, capacity math | our research notes (FAA and press citations inside) | Thesis 2 |

## processed/
| file | what it is | source | used on |
|---|---|---|---|
| slide03_*, slide27_*, slideE2_E5_*, slideE5_*, slide28_* | slide-ready tables (see above) | code/build_slide_tables.py | as named |
| bluesky_nyc_overlap.csv/.md | every JetBlue NYC route with United overlap flag, Q3'25-Q2'26 | code/nyc_overlap_build.py from raw/t100 L4Q txt | E2, E5 |
| jfk27_3_*.csv, jfk27_3_history.md | JFK 2021-22 United entry/exit, DiD panels, 2015 exit (Table 6) | code/jfk27_3_history.py (+3_extra, 3_sensitivity) | Thesis 2 |
| jfk27_7_market.csv/.md | JFK-LAX/SFO and EWR-LAX/SFO market by carrier, quarterly | code/jfk27_7_market_build.py | Thesis 2 |
| jfk27_4_precedents.csv/.md | capacity-entry precedents (T-100 + Table 6) | code/e_table.py with a_/b_/c_/d_ helpers | Thesis 2 |
| hist_route_quarter_panel.csv, hist_period_means.csv, csv3_2021_22_united_jfk_entry_vs_jetblue.csv | first-pass JFK history (Nov 8) | code/hist_check.py | Thesis 2 background |
| jetblue_top25_jfk_routes_full.csv | JetBlue top 25 JFK routes | T-100 | Thesis 2 background |
| t100_bos_jfk_ewr_transcon_quarterly.csv | quarterly hub share and LF, BOS/JFK/EWR transcon | T-100 | Thesis 2 background |
| parity_points_25_cases.csv | 25 same-fare route cases | code/parity.py | E3, slide 28 scatter |
| table1a_b6_fare_panel.csv, united_share_crosscheck.csv | Blue Sky verification panels (Nov 8) | Table 1a, T-100 | background |

## code/
build_slide_tables.py (new, asserts all slide numbers); nyc_overlap_build.py; hist_check.py; jfk27_3_history.py,
jfk27_3_extra.py, jfk27_3_sensitivity.py, jfk27_7_market_build.py; e_table.py, a_ua_jfk.py, b_t100_annual.py,
c_bos_ewr.py, c2_bos_ewr_entry.py, d_panel_years.py; parity.py; vx_table6_values.py (Table 6 values used by
jfk27_3_history.py); browser extract helpers (*.js) used in the browser to pull T-100 / Table 1a from TranStats.
Paths are repo-relative. Run from code/. hist_check.py, jfk27_3_history.py, jfk27_7_market_build.py and nyc_overlap_build.py
were re-run on a scratch copy and reproduced the processed files, differing only in the scrubbed path text.

## archive/ (SUPERSEDED, do not use)
- SUPERSEDED_bsky_route_sets_boston_2.338M_base.csv: old Boston route set (any route with UA > 0), which gave the 2.338M Boston base
- SUPERSEDED_bluesky_e5_boston2.338M_plus_30pct.py: old base formula (Boston 2.338M + EWR + 30% of JFK/LGA)
- SUPERSEDED_fares_summary_3.104M_base.md: intermediate 3.104M base
