# jetblue_switching

Everything behind JetBlue Thesis 1 (Blue Sky switching): the 25 same-fare route case studies, the 3.1%/yr fit
(0.52 + 2.62 x link), the eventual 6%, switching-pace precedents and S-curves (median k50 = 5, scale 0.455), Blue Sky terms,
product/reliability comparison, and the revenue-lost grids ($8.1M Q4'26-Q3'27 window, $23.0M FY2028, -$0.32/share).
Slide refs: Main = UIC_Michigan_ULCC-JBLU_deck (27 = JetBlue Thesis 1 Blue Sky, 28 = Thesis 1 switching); App = appendix test_build (36 E1 ... 41 E6).

Run the rebuilt pipeline from this folder: `python code/pipeline/fit_switch_rate.py; python code/pipeline/switch_pace.py; python code/pipeline/revenue_lost.py; python code/pipeline/parity_crosswalk.py`.
Original scripts were copied as-is with absolute workspace paths stripped (they reference the original working folders such as routes/, switch/).

## Notes
- Final inputs (JetBlue model Assumptions): base 2.316M pax/yr, 3.1%/yr from Q4'26, eventual 6%, fare $180, 12% variable cost, 24% tax, 377.3M shares. Rebuilt FY revenue path matches the model exactly (FY28 T1 revenue $23.0066M); equity -$120.87M and -$0.3204/share are read from the model DCF (thesis1_model_rows.csv).
- MAIN DECK slide 28 heat map shows $6.8/$7.5/$8.2/$8.8M on the 3.1% row: those equal the SUPERSEDED 2.338M base. With the final 2.316M base the row is $6.7/$7.4/$8.1/$8.8M (appendix E6 shows $8.1M). The current slide builder (code/slides/main_deck_slide28_build_t1s2.py) hard-codes PAX = 1.616 + 0.553 = 2.169M, a third value. Needs fixing on the slide.
- S-curve quarter convention: k0 = Q2 2026 (Blue Sky elite perks, May 2026); Q4'26 = quarter 2, Q3'27 = quarter 5 (50% of eventual). The model itself uses a linear 0.775%/qtr ramp from Q4'26.
- Precedent pace quarters (k10, k50, k90) are our judgment read off the a1-a5 study summaries; they are not a mechanical output of those scripts.
- Cancellation rates: United 1.36% is network (incl. regionals; mainline 0.82%); JetBlue 1.65%. On-time 77.65 vs 72.34 (DOT ATCR full-year 2025).
- Raw DOT pulls for r01-r10 were fetched through WebFetch and transcribed into the r*.csv files (each row carries its source URL); no raw download was saved for those cases. Raw Table 6 pulls exist only for a1, a3, a5, a7 (raw/).
- Removed for licensing: two Deutsche Bank estimate sentences (processed/switch/agent09.md); Bloomberg EV/EBITDA multiple, Bloomberg price source and the rows using them (archive/bsky_driver2_2338M: sizing.py, calc8_equity.csv, verification_table.csv, verification md); the full Motley Fool transcript (excerpt only kept). Consensus columns of the model are not copied.

## Files

file | what it is | source | used on slide(s)
--- | --- | --- | ---
README.md | this file | our analysis | -
archive/appendix_6147M/bluesky_e5.out | SUPERSEDED: older E5/E6 code using a 6.147M passenger base ($21.4M window) | our code | none (superseded)
archive/appendix_6147M/bluesky_e5.png | SUPERSEDED: older E5/E6 code using a 6.147M passenger base ($21.4M window) | our code | none (superseded)
archive/appendix_6147M/bluesky_e5.py | SUPERSEDED: older E5/E6 code using a 6.147M passenger base ($21.4M window) | our code | none (superseded)
archive/appendix_6147M/bluesky_e6.out | SUPERSEDED: older E5/E6 code using a 6.147M passenger base ($21.4M window) | our code | none (superseded)
archive/appendix_6147M/bluesky_e6.png | SUPERSEDED: older E5/E6 code using a 6.147M passenger base ($21.4M window) | our code | none (superseded)
archive/appendix_6147M/bluesky_e6.py | SUPERSEDED: older E5/E6 code using a 6.147M passenger base ($21.4M window) | our code | none (superseded)
archive/bsky_driver2_2338M/JetBlue_Driver2_BlueSky_Verification_2026-11-08.md | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/calc3.py | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/chunks.py | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/delta_alaska.py | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/out/calc3_5.json | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/out/calc5_detection.csv | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/out/calc6_loss_per_switcher.csv | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/out/calc7_scenarios.csv | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/out/calc8_equity.csv | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/out/delta_alaska_annual_recomputed.csv | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/out/delta_alaska_quarterly_recomputed.csv | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/out/jetblue_lf_fare_revenue_by_quarter.csv | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/out/quarterly_effect_lf.csv | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/out/regression_lf.csv | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/out/route_sets.csv | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/out/sizing.json | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/out/table1a_b6_fare_panel.csv | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/out/tables.json | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/out/united_share_crosscheck.csv | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/out/verification_table.csv | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/out/verify.json | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/prep.py | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/sizing.py | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/tables.py | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/bsky_driver2_2338M/verify.py | SUPERSEDED: earlier Blue Sky "Driver 2" verification/sizing (2.338M base); Bloomberg multiples and price source removed | our code + public DOT data | none (superseded)
archive/switch_2338M/opt3.py | SUPERSEDED: pace/heat-map option scripts using the 2.338M base | our code | none (superseded)
archive/switch_2338M/opt4.py | SUPERSEDED: pace/heat-map option scripts using the 2.338M base | our code | none (superseded)
archive/switch_2338M/opt5.py | SUPERSEDED: pace/heat-map option scripts using the 2.338M base | our code | none (superseded)
archive/switch_2338M/opt6.py | SUPERSEDED: pace/heat-map option scripts using the 2.338M base | our code | none (superseded)
archive/switch_2338M/opts.py | SUPERSEDED: pace/heat-map option scripts using the 2.338M base | our code | none (superseded)
archive/switch_2338M/scale.py | SUPERSEDED: pace/heat-map option scripts using the 2.338M base | our code | none (superseded)
archive/switch_2338M/surf.py | SUPERSEDED: pace/heat-map option scripts using the 2.338M base | our code | none (superseded)
code/appendix/bluesky_e3.out | printed output of the fit script | our code | App 38
code/appendix/bluesky_e3.png | code screenshot placed on slide | our code | App 38
code/appendix/bluesky_e3.py | Original appendix code for the 3.1% fit (reads same_fare_routes.csv in its own dir) + .out/.png screenshots shown on slides | our code | App 38
code/appendix/bluesky_e3_fit.out | printed output of the fit script | our code | App 38
code/appendix/bluesky_e3_fit.png | code screenshot placed on slide | our code | App 38
code/appendix/bluesky_e3_fit.py | Original appendix code for the 3.1% fit (reads same_fare_routes.csv in its own dir) + .out/.png screenshots shown on slides | our code | App 38
code/appendix/bluesky_e4.out | Original appendix code for S-curve pace (k50, scale 0.455) + output/screenshot | our code | App 39
code/appendix/bluesky_e4.png | Original appendix code for S-curve pace (k50, scale 0.455) + output/screenshot | our code | App 39
code/appendix/bluesky_e4.py | Original appendix code for S-curve pace (k50, scale 0.455) + output/screenshot | our code | App 39
code/appendix/h3.out | Original appendix code: P(>=1 cancel in 20 flights) 24% vs 28%, on-time gap 5.3 | our code | App 36
code/appendix/h3.png | Original appendix code: P(>=1 cancel in 20 flights) 24% vs 28%, on-time gap 5.3 | our code | App 36
code/appendix/h3.py | Original appendix code: P(>=1 cancel in 20 flights) 24% vs 28%, on-time gap 5.3 | our code | App 36
code/cases/charts.py | Scripts behind cases/k* tables and charts | our code | background
code/cases/fit.py | Scripts behind cases/k* tables and charts | our code | background
code/cases/model.py | Scripts behind cases/k* tables and charts | our code | background
code/cases/simple.py | Scripts behind cases/k* tables and charts | our code | background
code/cases/simple_corr.py | Scripts behind cases/k* tables and charts | our code | background
code/cases/simple_corr2.py | Scripts behind cases/k* tables and charts | our code | background
code/cases/simple_corr3.py | Scripts behind cases/k* tables and charts | our code | background
code/cases/simple_corr4.py | Scripts behind cases/k* tables and charts | our code | background
code/pipeline/extract_thesis1_from_model.py | REBUILT: pulls thesis rows from the model workbook (path as argument) | our code | App 41
code/pipeline/fit_switch_rate.py | REBUILT runnable: parity_points -> switch_rate_fit | our code | App 38
code/pipeline/parity_crosswalk.py | REBUILT: traces the 25 parity points to route csvs | our code | App 38
code/pipeline/revenue_lost.py | REBUILT runnable: 2.316M x rate x fare grids and FY path | our code | App 41
code/pipeline/switch_pace.py | REBUILT runnable: precedents -> S-curves, model ramp | our code | App 39
code/poach/cases.py | Scripts behind poach/ charts and sensitivity | our code | background
code/poach/chart.py | Scripts behind poach/ charts and sensitivity | our code | background
code/poach/data.py | Scripts behind poach/ charts and sensitivity | our code | background
code/poach/half.py | Scripts behind poach/ charts and sensitivity | our code | background
code/poach/half2.py | Scripts behind poach/ charts and sensitivity | our code | background
code/poach/sens.py | Scripts behind poach/ charts and sensitivity | our code | background
code/routes/parity.py | Builds parity_points.csv (points hand-entered from r*.csv) and the original scatter | our code | Main 28, App 38
code/routes/proj.py | route-case projection helper | our code | background
code/routes/r04_mk.py | writes r04_bos_dl_b6.csv from fetched Table 6 values | our code | App 38
code/slides/bluesky_E1.py | Appendix slide builders E1-E6 (show which file each number is read from; E5/E6 read the final model) | our code | App 36-41
code/slides/bluesky_E2.py | Appendix slide builders E1-E6 (show which file each number is read from; E5/E6 read the final model) | our code | App 36-41
code/slides/bluesky_E3.py | Appendix slide builders E1-E6 (show which file each number is read from; E5/E6 read the final model) | our code | App 36-41
code/slides/bluesky_E4.py | Appendix slide builders E1-E6 (show which file each number is read from; E5/E6 read the final model) | our code | App 36-41
code/slides/bluesky_E5.py | Appendix slide builders E1-E6 (show which file each number is read from; E5/E6 read the final model) | our code | App 36-41
code/slides/bluesky_E6.py | Appendix slide builders E1-E6 (show which file each number is read from; E5/E6 read the final model) | our code | App 36-41
code/slides/bsappx_build_test.py | Blue Sky appendix test-build script | our code | App 36-41
code/slides/main_deck_slide28_build_t1s2.py | Main-deck JetBlue Thesis 1 slide builder (scatter, S-curve, heat map). NOTE: hard-codes PAX = 1.616 + 0.10 x 5.533 | our code | Main 28
code/switch/a1.py | Scripts behind a1-a10 event-time studies (Table 6 parsing, DiD, timing) | our code | App 39
code/switch/a10_calc.py | Scripts behind a1-a10 event-time studies (Table 6 parsing, DiD, timing) | our code | App 39
code/switch/a2_build.py | Scripts behind a1-a10 event-time studies (Table 6 parsing, DiD, timing) | our code | App 39
code/switch/a3_aa_as.py | Scripts behind a1-a10 event-time studies (Table 6 parsing, DiD, timing) | our code | App 39
code/switch/a3_aa_as_data.py | Scripts behind a1-a10 event-time studies (Table 6 parsing, DiD, timing) | our code | App 39
code/switch/a4_vx.py | Scripts behind a1-a10 event-time studies (Table 6 parsing, DiD, timing) | our code | App 39
code/switch/a5_an.py | Scripts behind a1-a10 event-time studies (Table 6 parsing, DiD, timing) | our code | App 39
code/switch/a7_did.py | Scripts behind a1-a10 event-time studies (Table 6 parsing, DiD, timing) | our code | App 39
code/switch/a8_build.py | Scripts behind a1-a10 event-time studies (Table 6 parsing, DiD, timing) | our code | App 39
code/switch/a9.py | Scripts behind a1-a10 event-time studies (Table 6 parsing, DiD, timing) | our code | App 39
code/switch/ev.py | Scripts behind a1-a10 event-time studies (Table 6 parsing, DiD, timing) | our code | App 39
processed/bluesky/8_bluesky_nyc_mechanics.md | How Blue Sky works for a NYC customer (booking flows, status credit, one airline per ticket) | jetblue.com, TPG, OMAAT, AwardFares (URLs inline) | Main 27
processed/bluesky/BlueSky_terms_verification_2026-11-08.md | Blue Sky terms verified on official pages: Mosaic credit on United only when booked on jetblue.com, United Premier earns nothing on JetBlue, dates (earn/redeem Oct 2025, cross-booking Feb 2026, elite perks May 2026). Sizing sections use the superseded 2.338M base; third-party multiples removed | jetblue.com / united.com pages, press releases (URLs inline) | Main 27, App 36-37
processed/bluesky/fares_SUMMARY_intl_coverage_check.md | Fare-parity summary incl. Blue Sky international coverage check (international excluded: coverage unconfirmed) | Google Flights quotes; jetblue.com | App 37
processed/bluesky/jb_reframed.png | JetBlue cabin photo used for the screens panel | JetBlue media | Main 27
processed/bluesky/jfk27_10_review_bluesky_dates.md | Date check: Blue Sky announced May 29 2025; DOT review completed Jul 29 2025 | https://www.businesswire.com/news/home/20250729944822/en/JetBlue-and-United-Complete-DOT-Review-of-Blue-Sky-Collaboration | Main 27 / catalyst slide
processed/bluesky/jfk27_6_product_comparison.md | Product comparison JetBlue vs United (seats, screens, Wi-Fi, legroom) | SeatCompare, Live and Let's Fly, JetBlue/United releases (URLs inline) | Main 27, App 36
processed/bluesky/product_reliability_comparison.csv | REBUILT: on-time 77.65/72.34, cancels 1.36/1.65 (UA network), Starlink 340 mi vs GEO 22,000 mi, screens | DOT ATCR Feb 2026; earthsims.com; satelliteinternet.com (fetched 2026-11-11) | Main 27, App 36 (E1)
processed/cases/BRIEF_cases.md | brief for the case studies | our analysis | -
processed/cases/k1_intl.csv | Case-study tables: k1 international, k2 domestic, k3 hubs, k4 mergers, k5 product, k6 loyalty | public sources (URLs in csv) | background for Main 28 / App 38
processed/cases/k1_intl.md | Case-study summaries matching the k* csv files | our analysis | background
processed/cases/k2_domestic.csv | Case-study tables: k1 international, k2 domestic, k3 hubs, k4 mergers, k5 product, k6 loyalty | public sources (URLs in csv) | background for Main 28 / App 38
processed/cases/k2_domestic.md | Case-study summaries matching the k* csv files | our analysis | background
processed/cases/k3_hubs.csv | Case-study tables: k1 international, k2 domestic, k3 hubs, k4 mergers, k5 product, k6 loyalty | public sources (URLs in csv) | background for Main 28 / App 38
processed/cases/k3_hubs.md | Case-study summaries matching the k* csv files | our analysis | background
processed/cases/k4_mergers.csv | Case-study tables: k1 international, k2 domestic, k3 hubs, k4 mergers, k5 product, k6 loyalty | public sources (URLs in csv) | background for Main 28 / App 38
processed/cases/k4_mergers.md | Case-study summaries matching the k* csv files | our analysis | background
processed/cases/k5_product.csv | Case-study tables: k1 international, k2 domestic, k3 hubs, k4 mergers, k5 product, k6 loyalty | public sources (URLs in csv) | background for Main 28 / App 38
processed/cases/k5_product.md | Case-study summaries matching the k* csv files | our analysis | background
processed/cases/k6_loyalty.csv | Case-study tables: k1 international, k2 domestic, k3 hubs, k4 mergers, k5 product, k6 loyalty | public sources (URLs in csv) | background for Main 28 / App 38
processed/cases/k6_loyalty.md | Case-study summaries matching the k* csv files | our analysis | background
processed/model/model_ramp_quarterly.csv | REBUILT: model ramp 0.775%/qtr from Q4'26, 3.10% by Q3'27, capped 6.00% | our analysis | App 39 table
processed/model/revenue_lost_fy.csv | REBUILT: FY revenue lost FY26 $0.8M, FY27 $11.3M, FY28 $23.0M, FY29-30 $25.0M (matches model Operating Model row 40) | our analysis | App 41, valuation snapshot
processed/model/revenue_lost_quarterly.csv | REBUILT: quarterly revenue lost path | our analysis | App 41
processed/model/revenue_lost_window_grid_usd_m.csv | REBUILT: revenue lost Q4'26-Q3'27 by switch rate x fare at 2.316M base; base $8.08M | our analysis | App 41 heat map; Main 28 heat map (see note)
processed/model/switch_pace_precedents.csv | REBUILT: k10/k50/k90 quarters and logistic scale per precedent; median k50=5, scale 0.455 | our reading of processed/switch/a1-a5 | Main 28 pace chart, App 39
processed/model/switch_pace_s_curves.csv | REBUILT: S-curve series (share of eventual switching by quarter) | our analysis | Main 28, App 39
processed/model/switch_rate_by_depth.csv | REBUILT: mean/median share lost by link depth | our analysis | App 38
processed/model/switch_rate_fit.csv | REBUILT: fit 0.52 + 2.62 x link, r 0.42, n 25; 3.1%/yr at link 1; 52% of eventual 6%; best-fit line endpoints (-0.266, 6.546) | our analysis | Main 28, App 38
processed/model/thesis1_model_rows.csv | Thesis 1 inputs and DCF bridge from final JetBlue model (EBIT, PV, TV, equity -$120.9M, -$0.32/share); thesis rows only, no consensus columns | our model (rv/appx4/models_final/JBLU_Model_Valuation.xlsx) | App 41, Main valuation
processed/poach/Delta_Alaska_poaching.png | Charts from the earlier poaching analysis (Delta/Alaska, switching history) | our analysis | earlier deck versions
processed/poach/README_JetBlue_Driver2.md | README of the earlier United-poaching package | our analysis | -
processed/poach/Switching_history_cases.png | Charts from the earlier poaching analysis (Delta/Alaska, switching history) | our analysis | earlier deck versions
processed/poach/Switching_history_lefthalf.png | Charts from the earlier poaching analysis (Delta/Alaska, switching history) | our analysis | earlier deck versions
processed/poach/findings.csv | Historical poaching cases results (earlier "Driver 2" pass) | our analysis of DOT Table 6 | background
processed/poach/sens.csv | Sensitivity of revenue lost by quarter (earlier pass) | our analysis | background
processed/routes/BRIEF_routes.md | research brief for the route cases (column definitions, depth codes) | our analysis | -
processed/routes/Shared_routes_fares_full.csv | Google Flights base-fare quotes, JetBlue vs United on shared routes | Google Flights quotes we collected (Nov 2026) | App 37 (E2), Main 28 parity table context
processed/routes/bluesky_nyc_overlap.csv | JetBlue NYC routes overlapping United, L4Q passengers (input to App 37 tables) | our analysis of BTS T-100 / DB1B | App 37 (E2)
processed/routes/parity_points.csv | THE 25 same-fare route case studies: incumbent share before/after, months, share lost per year, link depth (0 none, 1 shared loyalty, 2 codeshare+loyalty) | our analysis of r02/r04/r05/r07/r10 (DOT Table 1/6) | Main 28 scatter; App 38 table + scatter
processed/routes/parity_points_crosswalk.csv | REBUILT: maps each of the 25 points to its source row in r*.csv (SEA-BOI and SEA-SLC chain two windows) | our analysis | App 38 audit
processed/routes/r01_bcn.csv | Route case: Bamberger-Carlton-Neumann / Gayle alliance studies (0 parity routes) | NBER/academic, GAO RCED-99-37 (URLs in csv) | background
processed/routes/r01_bcn.md | Route case: Bamberger-Carlton-Neumann / Gayle alliance studies (0 parity routes) | NBER/academic, GAO RCED-99-37 (URLs in csv) | background
processed/routes/r02_conwdl.csv | Route case: Continental/Northwest 1998 and Delta/Continental/Northwest 2003 overlap routes | DOT Consumer Airfare Report Table 1 PDFs (URLs in csv) | Main 28, App 38 (5 points)
processed/routes/r02_conwdl.md | Route case: Continental/Northwest 1998 and Delta/Continental/Northwest 2003 overlap routes | DOT Consumer Airfare Report Table 1 PDFs (URLs in csv) | Main 28, App 38 (5 points)
processed/routes/r04_bos_dl_b6.csv | Route case: Delta vs JetBlue at Boston 2013-2020 (11 routes, 7 parity points) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | Main 28, App 38
processed/routes/r04_bos_dl_b6.md | Route case: Delta vs JetBlue at Boston 2013-2020 (11 routes, 7 parity points) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | Main 28, App 38
processed/routes/r05_sea_dl_as.csv | Route case: Delta vs Alaska at Seattle 2012-2020 (11 parity points) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | Main 28, App 38
processed/routes/r05_sea_dl_as.md | Route case: Delta vs Alaska at Seattle 2012-2020 (11 parity points) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | Main 28, App 38
processed/routes/r06_b6_ua.csv | Route case: JetBlue vs United before/after Blue Sky 2024Q1-2026Q1 | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | background
processed/routes/r06_b6_ua.md | Route case: JetBlue vs United before/after Blue Sky 2024Q1-2026Q1 | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | background
processed/routes/r07_dlws_aaas.csv | Route case: Alaska/Delta partnership end 2017, American/Alaska alliance 2020-21 (SEA-PHL point) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6); DOT orders | Main 28, App 38
processed/routes/r07_dlws_aaas.md | Route case: Alaska/Delta partnership end 2017, American/Alaska alliance 2020-21 (SEA-PHL point) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6); DOT orders | Main 28, App 38
processed/routes/r08_vx.csv | Route case: Virgin America product entry and Alaska/Virgin merger | https://data.transportation.gov/resource/4f3n-jbg2 (Table 6, Q2 snapshots) | App 39 (Alaska/Virgin)
processed/routes/r08_vx.md | Route case: Virgin America product entry and Alaska/Virgin merger | https://data.transportation.gov/resource/4f3n-jbg2 (Table 6, Q2 snapshots) | App 39 (Alaska/Virgin)
processed/routes/r09_intl.csv | Route case: international alliances / ATI (no parity routes) | GAO RCED-95-99, DOT/DOJ ATI filings (URLs in csv) | background
processed/routes/r09_intl.md | Route case: international alliances / ATI (no parity routes) | GAO RCED-95-99, DOT/DOJ ATI filings (URLs in csv) | background
processed/routes/r10_product.csv | Route case: JetBlue Mint vs United NYC-LAX/SFO, BOS-SFO (Mint vs United point) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | Main 28, App 38
processed/routes/r10_product.md | Route case: JetBlue Mint vs United NYC-LAX/SFO, BOS-SFO (Mint vs United point) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | Main 28, App 38
processed/routes/same_fare_routes.csv | identical copy of parity_points.csv as read by the appendix code | our analysis | App 38
processed/switch/BRIEF_switch.md | research brief for switching-pace studies (old 2.338M base mentioned in context only) | our analysis | -
processed/switch/a10_entry_ramp.csv | Entrant share ramp timing (8 entrant paths) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | background (Thesis 2 ramp)
processed/switch/a10_entry_ramp.md | Entrant share ramp timing (8 entrant paths) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | background (Thesis 2 ramp)
processed/switch/a1_delta_alaska.csv | Event-time study: Delta entry at Seattle vs Alaska (timing of loss, loyalty excess onset k4, peak k6) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6); Delta press releases | App 39 pace dot (4,5,6)
processed/switch/a1_delta_alaska.md | Event-time study: Delta entry at Seattle vs Alaska (timing of loss, loyalty excess onset k4, peak k6) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6); Delta press releases | App 39 pace dot (4,5,6)
processed/switch/a2_co_nw.csv | Event-time study: Continental/Northwest 1998 and DL/CO/NW 2003 (50% by k0-1, 90% by k2-4) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6); GAO RCED-99-37 | App 39 fastest curve (0,0.5,3)
processed/switch/a2_co_nw.md | Event-time study: Continental/Northwest 1998 and DL/CO/NW 2003 (50% by k0-1, 90% by k2-4) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6); GAO RCED-99-37 | App 39 fastest curve (0,0.5,3)
processed/switch/a3_aa_as.csv | Event-time study: American/Alaska WCIA Seattle DiD (first k7, 50% k8, 90% k9-10) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | App 39 slowest curve (7,8,9.5)
processed/switch/a3_aa_as.md | Event-time study: American/Alaska WCIA Seattle DiD (first k7, 50% k8, 90% k9-10) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | App 39 slowest curve (7,8,9.5)
processed/switch/a4_vx_merge.csv | Event-time study: Alaska/Virgin loyalty fold 2018 (rival gains 3-5 quarters) | https://data.transportation.gov/resource/yj5y-b2ir | App 39 (2,3,4)
processed/switch/a4_vx_merge.md | Event-time study: Alaska/Virgin loyalty fold 2018 (rival gains 3-5 quarters) | https://data.transportation.gov/resource/yj5y-b2ir | App 39 (2,3,4)
processed/switch/a5_nea.csv | Event-time study: American/JetBlue NEA build-up and unwind (50% k5, 90% k6) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | App 39 (4,5,6)
processed/switch/a5_nea.md | Event-time study: American/JetBlue NEA build-up and unwind (50% k5, 90% k6) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | App 39 (4,5,6)
processed/switch/a6_loyalty_events.csv | Loyalty-shock events (Delta 2023, Southwest, Cathay, etc.), Mosaic/Premier qualification mechanics | press releases, filings, news (URLs in csv) | App 39 context
processed/switch/a6_loyalty_events.md | Loyalty-shock events (Delta 2023, Southwest, Cathay, etc.), Mosaic/Premier qualification mechanics | press releases, filings, news (URLs in csv) | App 39 context
processed/switch/a7_bluesky_now.csv | Blue Sky switching measured so far (2025Q4-2026Q1 DiD; no measurable switching yet) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | background / risk
processed/switch/a7_bluesky_now.md | Blue Sky switching measured so far (2025Q4-2026Q1 DiD; no measurable switching yet) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | background / risk
processed/switch/a7_did_b6.csv | a7 difference-in-differences output | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | background
processed/switch/a7_t6_panel.csv | a7 cleaned Table 6 panel (treated vs control) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | background
processed/switch/a8_literature.csv | Literature on lag structure (Lederman, Goolsbee-Syverson, Liu, Hess...) | academic papers (URLs in csv) | background
processed/switch/a8_literature.md | Literature on lag structure (Lederman, Goolsbee-Syverson, Liu, Hess...) | academic papers (URLs in csv) | background
processed/switch/a9_reliability.csv | Reliability shocks and share (Southwest 2022, Delta CrowdStrike) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6); SEC 8-K | background
processed/switch/a9_reliability.md | Reliability shocks and share (Southwest 2022, Delta CrowdStrike) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6); SEC 8-K | background
processed/switch/agent01.md | NEA trial record: no public switching rate | D. Mass. opinion 2023, JetBlue calls | background
processed/switch/agent02.md | Desk research notes (agents 02-10): OTP, Wi-Fi/Starlink, management statements, JV precedents; one broker estimate removed from agent09 | public sources cited inline | Main 27 product bullets; background
processed/switch/agent03.md | Desk research notes (agents 02-10): OTP, Wi-Fi/Starlink, management statements, JV precedents; one broker estimate removed from agent09 | public sources cited inline | Main 27 product bullets; background
processed/switch/agent04.md | Desk research notes (agents 02-10): OTP, Wi-Fi/Starlink, management statements, JV precedents; one broker estimate removed from agent09 | public sources cited inline | Main 27 product bullets; background
processed/switch/agent05.md | Desk research notes (agents 02-10): OTP, Wi-Fi/Starlink, management statements, JV precedents; one broker estimate removed from agent09 | public sources cited inline | Main 27 product bullets; background
processed/switch/agent06.md | Desk research notes (agents 02-10): OTP, Wi-Fi/Starlink, management statements, JV precedents; one broker estimate removed from agent09 | public sources cited inline | Main 27 product bullets; background
processed/switch/agent07.md | Desk research notes (agents 02-10): OTP, Wi-Fi/Starlink, management statements, JV precedents; one broker estimate removed from agent09 | public sources cited inline | Main 27 product bullets; background
processed/switch/agent08.md | Desk research notes (agents 02-10): OTP, Wi-Fi/Starlink, management statements, JV precedents; one broker estimate removed from agent09 | public sources cited inline | Main 27 product bullets; background
processed/switch/agent09.md | Desk research notes (agents 02-10): OTP, Wi-Fi/Starlink, management statements, JV precedents; one broker estimate removed from agent09 | public sources cited inline | Main 27 product bullets; background
processed/switch/agent10.md | Desk research notes, agent 10 | public sources cited inline | background
raw/company/jblu_q3_2026_call_bluesky_excerpt.txt | Blue Sky lines from JetBlue Q3 2026 call (1.1B TrueBlue points redeemed on United; record Mosaic qualifications); excerpt only | https://www.fool.com/earnings/call-transcripts/2026/10/27/jetblue-jblu-q3-2026-earnings-call-transcript/ | Main 27 context
raw/dot_t100/t100_bos_ewr_routes_B6_UA_AA_DL_2023_2026m7.csv | BTS T-100 segment passengers/seats, BOS/EWR routes for B6/UA/AA/DL 2023-2026m7, and carrier-month totals | https://www.transtats.bts.gov (T-100 Domestic Segment) | background (load-factor test)
raw/dot_t100/t100_carrier_month_totals.csv | BTS T-100 segment passengers/seats, BOS/EWR routes for B6/UA/AA/DL 2023-2026m7, and carrier-month totals | https://www.transtats.bts.gov (T-100 Domestic Segment) | background (load-factor test)
raw/dot_table6/a1_delta_alaska_t6.json | Table 6 rows, 15 Seattle city pairs 2010Q1-2019Q4 (Delta entry vs Alaska) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | App 39 (pace precedent)
raw/dot_table6/a3_aa_as_seattle/SEA-ATL.csv | Table 6 quarterly rows 2017Q1-2026Q1 per Seattle city pair (American/Alaska WCIA) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | App 39; parity point SEA-PHL
raw/dot_table6/a3_aa_as_seattle/SEA-BOS.csv | Table 6 quarterly rows 2017Q1-2026Q1 per Seattle city pair (American/Alaska WCIA) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | App 39; parity point SEA-PHL
raw/dot_table6/a3_aa_as_seattle/SEA-CHI.csv | Table 6 quarterly rows 2017Q1-2026Q1 per Seattle city pair (American/Alaska WCIA) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | App 39; parity point SEA-PHL
raw/dot_table6/a3_aa_as_seattle/SEA-CLT.csv | Table 6 quarterly rows 2017Q1-2026Q1 per Seattle city pair (American/Alaska WCIA) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | App 39; parity point SEA-PHL
raw/dot_table6/a3_aa_as_seattle/SEA-DEN.csv | Table 6 quarterly rows 2017Q1-2026Q1 per Seattle city pair (American/Alaska WCIA) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | App 39; parity point SEA-PHL
raw/dot_table6/a3_aa_as_seattle/SEA-DFW.csv | Table 6 quarterly rows 2017Q1-2026Q1 per Seattle city pair (American/Alaska WCIA) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | App 39; parity point SEA-PHL
raw/dot_table6/a3_aa_as_seattle/SEA-IAH.csv | Table 6 quarterly rows 2017Q1-2026Q1 per Seattle city pair (American/Alaska WCIA) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | App 39; parity point SEA-PHL
raw/dot_table6/a3_aa_as_seattle/SEA-LAS.csv | Table 6 quarterly rows 2017Q1-2026Q1 per Seattle city pair (American/Alaska WCIA) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | App 39; parity point SEA-PHL
raw/dot_table6/a3_aa_as_seattle/SEA-LAX.csv | Table 6 quarterly rows 2017Q1-2026Q1 per Seattle city pair (American/Alaska WCIA) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | App 39; parity point SEA-PHL
raw/dot_table6/a3_aa_as_seattle/SEA-MIA.csv | Table 6 quarterly rows 2017Q1-2026Q1 per Seattle city pair (American/Alaska WCIA) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | App 39; parity point SEA-PHL
raw/dot_table6/a3_aa_as_seattle/SEA-MSP.csv | Table 6 quarterly rows 2017Q1-2026Q1 per Seattle city pair (American/Alaska WCIA) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | App 39; parity point SEA-PHL
raw/dot_table6/a3_aa_as_seattle/SEA-NYC.csv | Table 6 quarterly rows 2017Q1-2026Q1 per Seattle city pair (American/Alaska WCIA) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | App 39; parity point SEA-PHL
raw/dot_table6/a3_aa_as_seattle/SEA-PHL.csv | Table 6 quarterly rows 2017Q1-2026Q1 per Seattle city pair (American/Alaska WCIA) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | App 39; parity point SEA-PHL
raw/dot_table6/a3_aa_as_seattle/SEA-SLC.csv | Table 6 quarterly rows 2017Q1-2026Q1 per Seattle city pair (American/Alaska WCIA) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | App 39; parity point SEA-PHL
raw/dot_table6/a5_nea_t6_raw.txt | Table 6 raw cells, 35 BOS/NYC city pairs 2019Q1-2026Q1 (AA-JetBlue NEA) | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | App 39 (American/JetBlue pace)
raw/dot_table6/a7_bluesky_t6.csv | Table 6 2022Q1-2026Q1, Blue Sky treated vs control city pairs | https://data.transportation.gov/resource/yj5y-b2ir (DOT Consumer Airfare Report Table 6) | background (Blue Sky measured so far)
raw/dot_table6/dot_car_table1a_bos_ewr_2023_2026q1.csv | DOT Consumer Airfare Report Table 1a (airport pairs) BOS/EWR 2023-2026Q1 | https://data.transportation.gov (Consumer Airfare Report Table 1a) | background / archive sizing
