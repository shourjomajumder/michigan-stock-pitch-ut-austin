# frontier/ — Frontier (ULCC) overview, Thesis 1 (load factor) and Thesis 2 (new routes)

Run scripts from `frontier/code/`. Each `*.expected.out` is the output the slide numbers were taken from; all re-run and match (Nov 11, 2026).
No Bloomberg exports, screenshots, consensus tables or broker/analyst text are included (see "Excluded").

| file | what it is | source | used on slide(s) |
|---|---|---|---|
| raw/frontier_quarterly_ops_2019Q1_2026Q3.csv | Frontier reported RPM, ASM, load factor, passenger and fare revenue, passengers (actuals only; estimate rows dropped) | Frontier 10-Q/10-K and earnings releases (Q4 2025 checked against https://s21.q4cdn.com/257736825/files/doc_financials/2025/q4/Frontier-Airlines-Reports-Fourth-Quarter-2025-Financial-Results.pdf, fetched 2026-11-11) | Frontier Thesis 1; C1, C2 |
| raw/allegiant_quarterly_ops_2018Q3_2026Q3.csv | Allegiant reported RPM, ASM, LF, passenger revenue, passengers, fare/pax | Allegiant 10-Q/10-K (scheduled service) | Thesis 1 regression; C1 |
| raw/suncountry_quarterly_ops_2022Q2_2026Q1.csv | Sun Country reported RPM, total ASM, LF, passenger revenue | Sun Country 10-Q/10-K | Thesis 1 regression; C1 |
| raw/routemap_dom.txt, routemap_intl.txt | F9/B6 routes: carrier+airport pair, departures Jan–Jul 2026, second count | BTS T-100 segment data (our pull) | Company Overview route maps |
| raw/routemap_carib_dom.txt, routemap_carib_intl.txt, routemap_carib_rows.json | Caribbean/Latin routes, seats/passengers by carrier | BTS T-100 | Company Overview route maps |
| raw/routemap_data.json | airports (lat/lon) + route list used to draw the maps | our analysis from the files above | Company Overview route maps |
| processed/lcc_quarters.csv | 32 low-cost-airline quarters: YoY % fare per mile (yield), traffic (RPM), seats (ASM) | our analysis; rebuilt exactly by code/build_lcc_quarters.py | Frontier Thesis 1; C1 |
| processed/fare_vs_traffic_scatter.csv | scatter points (lcc_quarters rounded) | our analysis | Thesis 1 "Fare Changes vs. Traffic Growth"; C1 |
| processed/thesis1_inputs_reported.csv | Q2 2026 traffic +8.96% (shown +9.0%), prior-year LF 78.9/78.4, Q3 2026 ASM 11,419M | Frontier filings | Thesis 1; C2; D1 |
| processed/thesis1_load_factor_build.csv | 78.9 +8.7 −0.3 −4.5 = 82.8; 78.4 +8.6 −0.4 −5.0 = 81.6 (11% traffic growth) | our analysis (code/e2_build.py logic) | Thesis 1 waterfalls; C2 |
| processed/thesis1_results.csv | our LF, extra pts, extra pax 380,000/290,000, extra revenue $51.5M/$40.9M ($92.4M; deck $51M/$41M/$92M), extra EBIT $45.28M/$36.00M ($81.28M; deck $45.3M/$36.0M/$81.3M) | our analysis; EBIT = revenue × (1 − 12% variable cost, model assumption) | Thesis 1 Results table; C2 |
| processed/booking_factor_survey.csv | #1 ticket-buying factor: Price 57, Airline 14, Stops 9, Other 20 (%) | Reuters/Ipsos poll, Apr 30–May 2 2019, n=2,008: https://www.ipsos.com/en-us/news-polls/reuters-ipsos-data-airline-poll-2019-05-16 | Thesis 1 pie |
| processed/thesis2_new_routes.csv | six routes: launch dates, weekly flights, miles, 230 seats, weekly seats, seat-miles | Frontier route announcements, e.g. DEN–FLL: https://news.flyfrontier.com/frontier-announces-four-new-routes-launching-late-2026/ | Company Overview; Thesis 2; D1 |
| processed/thesis2_ramp_assumption.csv | RASM ramp 85/105/115/120% | our assumption | Thesis 2; D2 |
| processed/thesis2_summary.csv | RASM 11.87¢, Q3'27 $3,009K, run-rate $12.04M/yr, net $4,469K, +1.2% capacity | Frontier Q3 2026 10-Q + our analysis | Thesis 2; D1, D2 |
| processed/fleet_mix.csv, fleet_seats.csv | A320ceo/A321ceo/A320neo/A321neo at Dec '23, '24, '25, Sep '26; seats per type | Frontier 10-K FY2023–25 and Q3 2026 10-Q | Company Overview |
| processed/fy2025_revenue_mix.csv | FY2025 fare 1,481 / non-fare 2,117 / other 126 ($M) | Frontier FY2025 release/10-K (33.2M pax × $44.60 fare; 3,598 passenger revenue; 126 other) | Company Overview |
| code/build_lcc_quarters.py | raw 10-Q panels → lcc_quarters (sample rules in docstring) | our code | C1 |
| code/e1.py | regression: traffic ~ fare + seats → fare −0.16 (R² 0.84); fares only −0.74 | our code | Thesis 1; C1 |
| code/e2_build.py | load factor build | our code | Thesis 1; C2 |
| code/e2_rev.py | extra pax/revenue from LF uplift; consensus inputs read from an un-published `private/` file | our code | Thesis 1 Results; C2 |
| code/f1_asm.py | new-route seat-miles by quarter, +1.2% capacity | our code | D1 |
| code/f2_ramp.py, f2_ramp_k.py | route RASM effect ($M, $K), net $4,469K, run-rate $12.04M | our code | Thesis 2 table; D2 |
| code/tables.py | writes the small processed tables above | our code | — |

## Notes and caveats
- Fare drag and added-capacity inputs in e2_build.py (fare rise 2.2%/2.9%, seat growth 5.4%/6.1%) are team inputs; Q4's 5.4% sits inside management's guidance of capacity up 5-6% vs Q4 2025 (Q3 2026 earnings call), Q1's 6.1% has no traced source. The valuation model uses the same seat growth for its Q4 2026E / Q1 2027E ASMs (Bloomberg consensus ASMs imply 6.3%/7.1%). Elasticity 0.16 is from e1.py.
- Consensus LF (79.5%/79.0%), consensus ASM/RPM/pax/yield used by e2_rev.py are Bloomberg consensus: not included (column dropped from thesis1_results.csv; e2_rev.expected.out still prints the two consensus LFs that appear on the slide).
- The 10-Q/10-K panels for Allegiant, Sun Country and Frontier were originally transcribed from photos of Bloomberg terminal screens showing company-reported actuals. The photos are excluded. Frontier Q4 2025 (ASM 9,803, RPM 7,736, LF 78.9%, pax 8,537) was checked against the earnings release. Check the rest against SEC EDGAR before publishing.
- Survey: Ipsos page confirms 57% price, n=2,008; the 14/9/20 split was not found on that page (it may be in the topline PDF).
- Route launch dates: only DEN–FLL (Nov 20, daily) checked against a press release; the other five are from the team's route table.
