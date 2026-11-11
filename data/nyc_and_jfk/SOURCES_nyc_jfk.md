# nyc_jfk: New York passenger base (JetBlue Thesis 1) and United's JFK return (Thesis 2)

Run every script from this folder (`data_repo/nyc_jfk`). `python3 code/build_key_tables.py` rebuilds and asserts the
headline numbers: **0.553M = 10% of 5.533M**, **0.147M = 10% of 1.474M**, base **2.316M**, JFK switching revenue
**$0.5 / 4.4 / 8.1 / 8.4M** (FY27-30) and **x60% = $0.3 / 2.6 / 4.8 / 5.1M**, Thesis 2 **-$0.0586 ≈ -$0.06/share**.

Excluded on purpose: all valuation workbooks (`JBLU_Model_Valuation.xlsx`, incl. the 10 `rv/jfk27/out/*` scenario
workbooks) and their numbers/rows json (lead decision: valuation models are not in the repo; they also hold Bloomberg
consensus/comps sheets); `jfk/JetBlue_Driver2_JFK_2027.zip` (duplicate of files below, contained Bloomberg text).
Redacted: Bloomberg 12.8x EV/EBITDA multiple and Bloomberg-attributed price label (archive/jfk_nov8 md, csv5, calcD,
scenarios.json, scenarios.py), a Barclays estimate and file reference (archive md), two sell-side analyst bullets
(docs/jfk27/10_review.md s.1.7). Absolute paths rewritten to repo-relative or `<workspace>/`.
Paths beginning `../EXTERNAL_bsky/`, `../EXTERNAL_routes/`, `../EXTERNAL_switch/` (only in code/jfk27/4_work) point to
source folders collected by other repo agents (Blue Sky / routes / switching).

file | what it is | source | used on slide(s)
---|---|---|---
**raw/** | | |
raw/nyc/dom_raw.txt, intl_raw.txt | B6 + UA NYC-airport segment pax/deps, L4Q Q3'25-Q2'26 | BTS T-100 Domestic / International Segment (transtats.bts.gov) | E5, E2 (via 4_full_overlap)
raw/t100_aug2025_jul2026/same_airport_pairs.csv | B6/UA pax on same-airport pairs, Aug'25-Jul'26 | BTS T-100 Domestic Segment, pulled 2026-11-11 | E5, E2 (1.616M)
raw/t100_aug2025_jul2026/intl_pairs.csv | B6/UA international pairs, Aug'25-Jul'26 | BTS T-100 International Segment, pulled 2026-11-11 | E5 (1.474M)
raw/jfk/t100_panel_jfk_transcon_hub_routes_2019_2026m7.csv | JFK/EWR transcon+hub route panel by carrier-quarter | BTS T-100 Domestic Segment | E7, history DiD
raw/jfk/dot_car_table1a_jfk_ewr_2019_2026q1.csv | fares/shares JFK & EWR markets | DOT Consumer Airfare Report Table 1a (data.transportation.gov) | E7 fares, history
raw/jfk/t100_ua_jfk_monthly_by_aircraft_2021_2022.csv | United JFK flying 2021-22 by aircraft | BTS T-100 | history (United 2021-22 JFK return)
raw/jfk/t100_b6_jfk_vs_system_by_quarter.csv, t100_jfk_top_b6_routes_L4Q_2025q3_2026q2.csv | JetBlue JFK exposure, top JFK routes | BTS T-100 | E7, model inputs
raw/jfk/t100.csv, t100q.csv, t100q.txt | monthly/quarterly JFK/EWR/BOS-LAX/SFO T-100 2019-2024 | BTS T-100 | history DiD
raw/jfk27/7_market_raw.txt | T-100 market extract for agent 7 | BTS T-100 | E7 market context
raw/jfk27/google_flights_quotes/*.txt | JFK-LAX/SFO fare quotes, JetBlue vs United, 6 dates | Google Flights quotes we collected (Nov 2026) | E7 "Fares" row
raw/jfk27/dot_table6_typed/vx.py | DOT Table 6 city-market values 2015-2020 typed into Python | DOT CAR Table 6 (data.transportation.gov/resource/yj5y-b2ir) | history (2015 exit)
**processed/** | | |
processed/nyc_passenger_base.csv | 2.316M base: 6 same-airport routes 100% + NYC domestic 5.533M x10% + NYC intl 1.474M x10% | our analysis (build_key_tables.py) | E5, main deck 37/40, model input pax_ov
processed/nyc_domestic_18_routes.csv | the 18 JFK+LGA domestic routes summed to 5.533M | our analysis | E5, E2
processed/jfk_switching_revenue_by_fy.csv | United JFK return L27Q3_base, switching pax and revenue by FY, and x60% | our analysis from 8_scenarios.csv | E7 table, slide 8 stack
processed/t2_per_share.csv | Thesis 2 DCF: 60% revenue x88% flow-through, 24% tax, mid-year at 12.95% WACC, value-driver TV, ke stub -> -$0.0586/sh | our analysis (replicates model DCF!C73 exactly) | slide 8, E7, valuation stacks
processed/source_references.csv | every URL cited in the NYC and JFK research notes (DOJ/court opinions, Escobari 2017 MPRA, Port Authority ATR, FAA, news) | public sources | E4-E7 evidence tables
processed/nyc/4_full_overlap.csv | every JetBlue NYC route with United NYC match flag (strict/metro), thin-route flag | BTS T-100 via code/nyc/build_full_overlap.py | E5, E2
processed/nyc/5_ewr_2025_shift.csv | 2025 Newark outage: JFK/LGA pax vs trend (24% recapture) | Port Authority monthly traffic reports; our analysis | main deck 37/40 "24%"
processed/jfk27/3_*.csv | United 2021-22 JFK return and 2022-23 exit: DiD vs controls, dose, sensitivity, monthly event study, 2015 exit (Table 6) | BTS T-100 / DOT CAR; code/jfk27/3_history.py | E7 "Left out: capacity effect"
processed/jfk27/4_precedents.csv (+4_work screens) | carrier-entry precedents table | DOT CAR / T-100; code/jfk27/4_work/e_table.py | E7 evidence
processed/jfk27/5_fares.csv | JFK-LAX/SFO fare parity, JetBlue vs United | Google Flights quotes; code/jfk27/5_scripts/build.py | E7 "Fares" (6/6 SFO, 3/6 LAX)
processed/jfk27/7_market.csv | JFK/EWR transcon market shares by carrier-quarter | BTS T-100; code/jfk27/7_market_build.py | E7 context
processed/jfk27/8_scenarios.csv, 8_scenarios_by_route.csv, 8_annual.csv, 8_sensitivity.csv, 8_results.json | United JFK return scenario model (9 scenarios L27Q2/L27Q3/L28Q1 x low/base/high), quarterly and annual; lost_rev_sw60_M = 0.6 x switching | our model, code/jfk27/model.py + model_inputs.json | E7, slide 8 (L27Q3_base row)
processed/jfk27/model_inputs.json | inputs to model.py (slot pairs, seats, LF, leakage, fares, switching ramp) | our assumptions from T-100 / Blue Sky terms | E7
processed/jfk27/scenario_outputs/scenario_summary.csv | per-share outputs (T1, T2, base, bull/bear, weighted) for the 10 scenario runs plus FINAL (switching-only x60%) | our model outputs (consensus-derived fields omitted) | slide 8, E7; only L27Q3_base, none and FINAL are current
processed/jfk27/scenario_outputs/thesis_dcf_inputs.csv | WACC 12.9491%, g 2.5%, ke, diluted shares 377.3M, tax 24%, stub, 12% variable cost, model T1/T2 | our JetBlue model (inputs only) | used by build_key_tables.py
**code/** | | |
code/build_key_tables.py | rebuilds the four headline tables above and asserts deck numbers | our code | E5, E2, E7, slide 8
code/nyc/build_full_overlap.py | raw T-100 extracts -> 4_full_overlap.csv | our code | E5
code/jfk27/model.py | scenario model -> 8_*.csv/json (re-run reproduces processed files exactly) | our code | E7
code/jfk27/3_history.py, 3_extra.py, 3_sensitivity.py | United JFK 2021-22 DiD history (re-run reproduces processed/jfk27/3_*) | our code | E7
code/jfk27/4_work/*.py, 5_scripts/build.py, 7_market_build.py | precedents, fares, market tables | our code | E7
code/jfk27_review/chk8.py, chk8b.py | independent recompute of the agent-8 scenario numbers (review agent 10) | our code | QA
code/jfk_nov8/hist_check.py, browser_extract_t100_table1a.js | first-run history check; DOT Table 1a browser extractor | our code | inputs
**docs/** | | |
docs/nyc/1-10_*.md, BRIEF.md | 10 research notes: antitrust market (DOJ NEA complaint, Young 2024), academic airport choice (Escobari 2017), adjacent-airport fares, full overlap, natural experiments (Newark 2025), catchment (Port Authority: Manhattan ~40% of JFK O&D), alliance precedents, Blue Sky NYC mechanics, counter-evidence, correlation basis | public sources cited inside; our analysis | E5, E6, main deck 37/40 (40%, 24%)
docs/jfk27/1_news ... 10_review.md, BRIEF.md, 8_READY.txt | 10-agent JFK-return work: news, slots, history, precedents, fares, product, market, model, valuation summary table (9_valuation.md), review (P = 0.60) | public sources; our analysis | E7, slide 8
docs/intl_pairs.md, same_airport_pairs.md | notes on the Aug'25-Jul'26 T-100 pulls | BTS | E5
**archive/** (superseded, not used in final deck) | | |
archive/nyc/SYNTHESIS_superseded_2.338M_30pct.md | first NYC synthesis: 2.338M Boston base + EWR + 30% JFK/LGA (6.15M) | SUPERSEDED by 2.316M | -
archive/nyc/bluesky_e5_superseded_30pct_rule.py | old base calc with the 30% rule | SUPERSEDED | -
archive/8_scenarios.bak_superseded.csv | earlier scenario run | SUPERSEDED | -
archive/jfk_nov8/* | Nov-8 JFK sizing (EV/EBITDAR multiple approach, $1,192M cap, Bloomberg multiple removed) | SUPERSEDED by rv/jfk27 model | -
