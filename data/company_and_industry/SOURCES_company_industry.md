# company_industry

Data behind the Industry Overview (main slide 3), the Frontier and JetBlue Company Overviews (main 5, 6; appendix 26),
and the catalyst and risk slides (main 24, 29). Everything here comes from public sources or our own analysis.
Rebuild: `cd code && python build_company_industry.py`, which reads raw/ and writes processed/.

**Left out (Bloomberg):** the slide 3 Valuation Comps table uses Bloomberg peer multiples and is not in this repo.
Frontier's revenue mix and fleet were first read from the Bloomberg-based model snapshot (`merged.json`).
We rebuilt both from Frontier's earnings releases. No broker text was used. JetBlue's $477M due in 2027 also appears
in a JP Morgan note, but the public source here is the Reuters interview of 2026-10-28.

| file | what it is | source | slide(s) |
|---|---|---|---|
| raw/public_sources_register.csv | Every fact with its value, source, URL and fetch date (S01–S22) | see URLs inside | 3, 5, 6, 24, 29 |
| raw/yahoo_daily_close_JBLU_ULCC_JETS_SPY_2025-11-10_2026-11-09.csv | Daily closes for JBLU, ULCC, JETS, SPY | Yahoo Finance (team pull) | 6; appx 26 |
| raw/fred_DJFUELUSGULF_jet_fuel_gulf_coast_daily.csv | US Gulf Coast jet fuel spot price, daily, Nov 2025 – Oct 2026 | EIA via FRED DJFUELUSGULF | 3 |
| raw/fred_DJFUELUSGULF_raw_pull.txt | The raw FRED pull behind the file above | EIA via FRED | 3 |
| raw/fred_LOADFACTORDD11_2024-01_2026-05.csv | US domestic scheduled load factor, monthly (rebuilt) | BTS via FRED, https://fred.stlouisfed.org/data/LOADFACTORDD11, fetched 2026-11-11 | 3 |
| raw/fred_CUUR0000SETG01_cpi_airline_fares_2024-01_2026-10.csv | CPI-U airline fares, NSA, monthly (rebuilt) | BLS via FRED, https://fred.stlouisfed.org/data/CUUR0000SETG01, fetched 2026-11-11 | 3 |
| raw/jblu_q3_2026_earnings_call_transcript_motleyfool.txt | JetBlue Q3 2026 earnings call transcript (Paisly, Blue Sky, TrueBlue) | fool.com (URL in header); one PR email address removed | 6, 27, 29 |
| code/build_company_industry.py | Builds every processed/ table | our analysis | — |
| code/i1_weekly_original.py | Original appendix script that resamples prices to weekly and indexes them (paths made repo-relative) | our analysis | appx 26 |
| code/stock_chart_3line_original.py, code/stock_chart_jblu_vs_jets_original.py | Original matplotlib mock-ups of the share-price chart (paths made repo-relative) | our analysis | 6 |
| processed/share_price_weekly_indexed.csv | 54 weekly points, 2025-11-10 = 100. Matches the deck series exactly (JBLU 89.3, JETS 121.1, ULCC 219.2) | Yahoo, our calc | 6; appx 26 |
| processed/share_price_1yr_summary.csv | One-year change: JBLU −10.7%, ULCC +119.2%, JETS +21.1%, SPY +11.6% | Yahoo, our calc | 6 |
| processed/jblu_vs_jets_indexed_daily_1yr.csv | Daily indexed JBLU vs JETS (original team output) | Yahoo, our calc | 6 |
| processed/jet_fuel_prewar_vs_oct2026.csv | $2.428 on 2026-02-27 → $4.632 on 2026-10-20, +90.8% (deck: $2.43 → $4.63, +91%) | EIA/FRED, our calc | 3 |
| processed/jet_fuel_monthly_avg.csv | Monthly average jet fuel price | EIA/FRED, our calc | context |
| processed/cpi_airline_fares_q3_2026_yoy.csv | Q3 2026 vs Q3 2025 airline fare CPI: +23.8% (Jul +25.5, Aug +23.4, Sep +22.4) | BLS/FRED, our calc | 3 |
| processed/us_domestic_load_factor_annual.csv | 2025 mean of 12 months = 81.68% → 81.7% | BTS/FRED, our calc | 3 |
| processed/jblu_operating_revenue_by_region.csv | FY2025 revenue by region: 5,452 / 3,139 / 471 ($M), with FY23–24 | JetBlue FY2025 10-K | 6 |
| processed/jblu_debt_maturities.csv | Debt maturities from the 10-K and from the Oct 2026 Reuters interview (2027 = $477M) | 10-K; Reuters/AJOT | 29 |
| processed/ulcc_fy2025_revenue_mix.csv | Fare 1,481 / Non-fare 2,117 / Other 126 ($M) | Frontier Q4 2025 release, our calc | 5 |
| processed/ulcc_fleet_by_type.csv | Fleet by type, Dec '23 – Sep '26 (Sep '26: 6/21/68/69 = 164) | Frontier releases and 8-Ks | 5 |
| processed/catalyst_earnings_dates.csv | Catalyst months, set from the prior year's report dates | company releases | 24, 29 |

## Notes and gaps
- **Debt figure.** The deck's slide 29 says "$8.5B of debt". That matches the 10-K carrying value of $8,498M at 12/31/25. The Q3 2026 release gives $8,393M at 9/30/26, and Reuters says about $8.4B. The $8.66B in the brief is our model's 12/31/26E forecast (models folder), not a reported number. The "$1.2B equity value" is also from the model or market cap and is not in this folder.
- **Airfares.** Public CPI data give +23.8% for Q3. The deck's "23%" is slightly low; "24%" would match better. The September month alone is +22.4%.
- **Tax on add-on fees.** No 2026 bill was found. The public basis is IRS Chief Counsel memo PMTA 2024-04: seat-selection and booking fees count as taxable transportation under IRC §4261, which carries the 7.5% domestic ticket tax. The audit's suggested wording, "a proposed bill", has no source we could find. Suggested wording: "IRS guidance treats some add-on fees as taxable at the 7.5% ticket-tax rate."
- **Competing seats −4 points (slide 3).** NOT SOURCED. No public release, call or article we could find gives this number. It needs a BTS T-100 or schedule calculation (see the dot_bts folder) or should be removed. The Frontier Q3 call only says about 30% of its business overlapped Spirit and Frontier backfilled about a quarter of it.
- **"Opened 4% of the market".** Supported by Cirium via NPR: Spirit had 3.9% of US passengers in Feb 2026.
- **Load factor benchmarks.** "Average 78% / Strong 85% / Full 87%" are our own framing. Only the 81.7% is sourced.
- **Frontier Dec '23 fleet by type** (8/21/82/25). Only the total of 136 was confirmed from a public filing.
- **Catalyst months** are estimates based on the prior year's report dates. Frontier reported Q2 2026 on Jul 29, so "Jul 2027" for its Q2 '27 report is consistent.
- **Union / flight-attendant contract facts** are not used on the current company or risk slides, so they were not collected here.
