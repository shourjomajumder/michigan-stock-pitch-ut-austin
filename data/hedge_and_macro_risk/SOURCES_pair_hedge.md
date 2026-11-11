# pair_hedge: Pair Overview, Hedge Overview, Hedge Sizing and appendix B1-B6

Trade: long Frontier (ULCC) / short JetBlue (JBLU), $1.16 short per $1 long (jet fuel beta ratio).
Data: Yahoo Finance daily closes, FRED/EIA jet fuel spot, Yahoo NYMEX ULSD futures (HO=F), SEC filings. No Bloomberg data.

Rebuild everything: `sh code/run_all.sh` (from this folder). It rebuilds `processed/` from `raw/` and writes the
printed output of every script to `code/outputs/<script>.out`. The scripts in `code/` that appear as screenshots on
the slides (k2, k1_hedge, k4, a4_miss, a5_*, i1_weekly) are unchanged copies and read bare file names, so they
run from inside `processed/` (`cd processed && python ../code/k2.py`).

## Deviation from the deck (read first)
The deck's daily price file used a **non-public (Bloomberg) close for 2 Nov 2026** for both stocks. It is
replaced here by the Yahoo Finance close. Every other price is identical. This moves only the numbers that use the
last day:

| Number on slide (Pair Overview, B2) | Deck | Public rerun (`k2.out`, `chart_series.out`) |
|---|---|---|
| Pair volatility | 62.9% | 62.8% |
| Sharpe ratio | 1.71 | 1.69 |
| Sortino ratio | 2.54 | 2.50 |
| Price ratio / z-score | 2.37x / 3.0 | 2.34x / 2.96 (still 3.0 rounded) |
| Frontier one-week rise to 2 Nov | 53% | 51% |
| Last weekly return (scatter) | ULCC 14.95 / JBLU 10.33 | 14.14 / 10.64 |
| Correlation 0.83, beta 1.1, 43 of 52 weeks, 79% / 69% leg vol | same | same |

The deck-run outputs (made with that close) are kept in `archive/deck_run_outputs/` for comparison.

## raw/
| file | what it is | source | used on slide(s) |
|---|---|---|---|
| raw/yahoo/yahoo_daily_closes_2025-10-31_2026-11-09.csv | daily closes JETS, SPY, IWM, XLY, HYG, ULCC, JBLU | Yahoo Finance (finance.yahoo.com), pulled Nov 2026 | Pair Overview, Hedge Sizing, B2, B4-B6 |
| raw/yahoo/yahoo_1yr_closes_JBLU_ULCC_JETS_SPY.csv | 1-year daily closes 10 Nov 2025 - 9 Nov 2026 | Yahoo Finance | JetBlue stock chart, B1 |
| raw/yahoo/yahoo_1yr_JBLU_ULCC_JETS_SPY_capture.txt | earlier partial capture of the same series (244 of 251 days; yymmdd, prices x100) | Yahoo Finance | reference only |
| raw/yahoo/yahoo_HO=F_front_month_capture.txt | NYMEX ULSD front-month futures closes (yymmdd:$/gal x1000), Sep 2025 - 2 Nov 2026 | Yahoo Finance HO=F, pulled 3 Nov 2026 | Hedge Overview oil chart, B4 |
| raw/fred/DJFUELUSGULF_capture_2025-08-01_2025-10-31.txt | US Gulf Coast kerosene-type jet fuel spot, $/gal | FRED DJFUELUSGULF (EIA), https://fred.stlouisfed.org/series/DJFUELUSGULF | 60-day jet-ULSD gap |
| raw/fred/DJFUELUSGULF_capture_2025-11-03_2026-10-27.txt | same, mm-dd,value; blanks = holidays | FRED DJFUELUSGULF | all fuel betas, hedge ratio, B3-B6 |
| raw/fred/DJFUELUSGULF_2026-10-28_2026-11-03.csv | later FRED prints | FRED, re-checked against https://fred.stlouisfed.org/data/DJFUELUSGULF.txt on 2026-11-11 | B4 event 7 |
| raw/filings/fuel_and_revenue_2026_quarters.csv | revenue and aircraft fuel, Q2/H1/Q3/9M 2026 | SEC 10-Qs and Q3 releases (URLs in file), fetched 2026-11-11 | Hedge Overview "Fuel as % of revenue" |

## processed/ (all rebuilt by code)
| file | what it is | made by | used on slide(s) |
|---|---|---|---|
| daily_prices.csv | ULCC, JBLU closes 3 Nov 2025 - 2 Nov 2026 (251 days) | build_inputs.py | Pair Overview chart, B2 |
| yahoo_prices.csv | ULCC, JBLU closes 10 Nov 2025 - 9 Nov 2026 | build_inputs.py | B4 event moves, B1 |
| live_etfs.csv | copy of the Yahoo raw file | build_inputs.py | B5, B6 |
| i1_yahoo_1yr.csv | copy of the Yahoo 1-year file | build_inputs.py | B1 |
| jet_fuel_gulf.csv | FRED jet fuel, 3 Nov 2025 - 3 Nov 2026 | build_inputs.py | B4 |
| daily_returns.csv | daily log returns (%), jet fuel / ULCC / JBLU, 244 days 4 Nov 2025 - 27 Oct 2026 | build_inputs.py | fuel betas -0.49 / -0.42, hedge ratio 1.16, B3, B5 |
| weekly_returns.csv | weekly log returns (%), 52 weeks | build_inputs.py | correlation 0.83, beta 1.1, 43 of 52, scatter |
| jet_fuel_vs_expected.csv | jet fuel vs. futures-implied price 30 days earlier (HO=F close at t-30d + 60-day avg jet-ULSD gap); `actual` = deck version (28 Oct - 2 Nov estimated from HO=F), `actual_fred_final` = later FRED prints | build_inputs.py | Hedge Overview oil chart, B4 "vs. forecast" |
| fuel_share_of_revenue_2026.csv | fuel % of revenue Q1-Q3 2026 (27.0/34.1/31.4 and 25.6/33.8/30.9) | fuel_share_of_revenue.py | Hedge Overview |
| series_price_ratio_bands.csv / _chart.csv | ULCC/JBLU price ratio, 60-day mean, +/-2 sigma, z (chart = every 2nd day from 29 Jan) | chart_series.py | Pair Overview, B2 |
| series_rolling60_corr_jet_fuel.csv | 60-day correlation with jet fuel, ULCC / JBLU / pair | chart_series.py | Hedge Sizing, B3 |
| series_rolling60_volatility.csv | 60-day total vol and S&P- / JETS-driven vol, legs and pair | chart_series.py | Hedge Sizing "Market volatility", B6 |
| series_rolling60_corr_spy.csv, series_rolling60_corr_jets.csv | 60-day correlation with SPY / JETS | chart_series.py | backup |
| series_jet_fuel_monthly_gap.csv | monthly average jet fuel vs. expected; Sept 2026 +$0.54 | chart_series.py | Hedge Overview |
| macro_exposure_boxes.csv, macro_factor_betas.csv, macro_demand_episodes.csv | four non-oil exposure boxes and their workings | macro_exposure.py | Hedge Sizing "Exposure", B5 |

## code/
| file | prints | slide |
|---|---|---|
| build_inputs.py | rebuilds processed inputs from raw | all |
| k2.py | correlation 0.83, beta 1.1, 43 of 52, vol 79%/69%/pair, Sharpe, Sortino, ratio and z | Pair Overview, B2 |
| k1.py, k1_hedge.py | fuel betas -0.489 / -0.420, hedge ratio 1.16, pair fuel beta 0.00 | Hedge Sizing, B3 |
| k3_fuel.py | abs. correlation with jet fuel 0.41 / 0.41 / 0.00 | B5 |
| k4.py | one-day moves on the 7 oil events (jet fuel, ULCC, JBLU, pair) | Hedge Overview, B4 |
| a4_miss.py | jet fuel vs. forecast on the 7 event dates (+$0.25 ... +$0.09) | Hedge Overview, B4 |
| a5_corr.py | correlation of legs and pair with jet fuel, JETS, IWM, SPY, XLY, HYG | Hedge Sizing, B5 |
| a5_vol.py | S&P-driven vol, alone 32% vs pair 9%, by quarter | Hedge Sizing, B6 |
| a5_fuelvol.py | fuel-driven vol by quarter (bar chart) | Hedge Sizing, B6 |
| i1_weekly.py, i1_index.py, one_year_stock_chart.py | one-year index: ULCC +119%, JBLU -11%, JETS +21% | JetBlue stock slide, B1 |
| chart_series.py | chart series above; ratio bands 2.06 / 0.86, Sept gap +$0.54 | Pair / Hedge slides |
| fuel_share_of_revenue.py | fuel % of revenue table | Hedge Overview |
| macro_exposure.py | wage +10.8%, credit +6.5%, rates +3.5% (range 2.7-3.7), demand -4.5% (range -2.7 to -5.7) | Hedge Sizing, B5 |
| run_all.sh | runs all of the above | |
| screenshots/*.png | the code screenshots placed on the appendix slides | B1-B6 |
| outputs/*.out | output of the latest rerun | |

## Notes on specific numbers
- Wage inflation: the appendix (B5) recomputes it as +10.8% (FY2025 salaries, wages and benefits $1,016M / $3,454M,
  9 Nov prices $8.35 / $3.94, shares 230.24M / 377.3M). The main deck box still says 14.5%, which came from
  older prices and assumed share counts: superseded.
- Credit, rates and demand boxes are rounded midpoints of ranges our scripts produce (see macro_exposure.py
  docstring); they are judgment calls, not single model outputs.
- Oil event 7 (2 Nov 2026) "vs. forecast +$0.09" uses the HO=F-based estimate of jet fuel because FRED had not yet
  published. The final FRED print (4.019) gives -$0.00 vs. forecast. The event's -8.2% jet fuel move already uses
  the FRED print.
- Measured factor vols in macro_exposure.py (XLY 17.5%, IWM 19.5%, HYG 4.5%) are realized 60-day vols read from
  public option-analytics pages; the "assumed" set (20%, 22%, 6.5%) is our assumption.

## archive/ (superseded, kept for reference only)
- deck_run_outputs/: script outputs as run for the deck (with the non-public 2 Nov close).
- macro_first_pass/: first factor-beta and scenario scripts and tables (ratio 1.163); scripts expect a
  `pair_daily.csv` = processed/daily_prices.csv.
- nonoil_rolling_capture/: earlier rolling-window captures; reproduced by chart_series.py (within 1 pt rounding).
- brent_version/: the earlier Brent-based hedge chart (FRED DCOILBRENTEU), replaced by jet fuel.
- superseded_scripts/: earlier fuel-volatility bar chart with older numbers.
