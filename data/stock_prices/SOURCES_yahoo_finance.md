# yahoo_finance/

This folder holds every Yahoo Finance dataset used in the Hook Em pitch (long Frontier ULCC / short JetBlue JBLU, 1 : 1.16).
It is the canonical copy. To rebuild `processed/` from `raw/`, run `python3 code/build_yahoo.py` from this folder. Running it also re-checks the raw files against each other and writes the results to `processed/raw_consistency_checks.csv` (all OK).

No Bloomberg data is included. The deck's Pair Overview price series (`slides/pair_daily.csv`, `appx/code/daily_prices.csv`) used a **Bloomberg close for 2 Nov 2026 (ULCC 7.49 / JBLU 3.16)**. That row was dropped. The canonical `daily_prices.csv` uses the Yahoo close for 2 Nov 2026 (ULCC 7.43 / JBLU 3.17), and `weekly_returns.csv` was rebuilt from it. Only the last week changes, from 10.33 / 14.95 to 10.64 / 14.14. The slide's correlations do not change: weekly 0.83, daily 0.69.

Retrieval: these closes were pulled from Yahoo Finance quote/history pages in the browser. The first pulls ran 2–3 Nov 2026 (closes through 30 Oct / 2 Nov). The final pull ran 10 Nov 2026 (closes through 9 Nov 2026). The comps inputs are from Yahoo Finance quote, analysis and balance-sheet pages, 10 Nov 2026. Spot check: on 11 Nov 2026 the history page at https://finance.yahoo.com/quote/ULCC/history/ showed 31 Oct 2025 3.86, 3 Nov 2025 3.70 and 10 Nov 2025 3.81, the same as raw/. That page was cached to 15 Oct 2026. The query1 chart API is closed to automated fetching (robots).

## raw/
| file | what it is | tickers / fields / range / freq | source | used on slide(s) |
|---|---|---|---|---|
| yahoo_daily_close_JETS_SPY_IWM_XLY_HYG_ULCC_JBLU_2025-10-31_2026-11-09.csv | Master daily price file (= `live_etfs.csv`, models `prices.csv` superset) | JETS, SPY, IWM, XLY, HYG, ULCC (`frontier`), JBLU (`jetblue`); **Close, not dividend-adjusted**; 2025-10-31 to 2026-11-09, 257 trading days, daily | Yahoo Finance history pages, retrieved 2026-11-10 | Pair Overview, Hedge Sizing (correlation with each risk: airline sector = JETS, small caps = IWM, stock market = SPY, consumer spending = XLY, credit = HYG), rolling 60-day vol/corr, Beta/WACC, 52-week range, appendix A5/K/mdl_beta |
| yahoo_daily_adjclose_JBLU_ULCC_JETS_SPY_2025-11-10_2026-11-09.csv | One-year file (= `i1_yahoo_1yr.csv` = outputs `Yahoo_1yr_JBLU_ULCC_JETS_SPY.csv`) | JBLU, ULCC, JETS, SPY; **Adj Close** (JETS and SPY dividend-adjusted; ULCC and JBLU pay no dividend so Adj = Close); 2025-11-10 to 2026-11-09, 251 days, daily | Yahoo Finance, retrieved 2026-11-10 | Company Overview "One-Year Share Price: JetBlue vs. Airline Sector (Indexed to 100)"; appendix I1 (index chart and weekly) |
| yahoo_HO=F_front_month_close_2025-09-02_2026-11-02.txt | NYMEX ULSD front-month futures closes, format `yymmdd:price×1000` | HO=F; Close; 2025-09-02 to 2026-11-02, daily | Yahoo Finance HO=F history, retrieved 2026-11-03 | Hedge Overview jet-fuel "expected" line; 28 Oct–2 Nov jet fuel estimate (A4) |
| yahoo_comps_inputs_2026-11-10.csv | Comps sheet inputs as typed into the models (from `comps.py` PEERS) | ULCC, JBLU, ALGT, LUV, ALK, AAL, UAL, DAL; price, market cap, total debt incl. operating leases, cash, FY2027E revenue and EPS (analyst consensus shown on Yahoo), $mm | Yahoo Finance, 11/10/2026 | Model Comps sheet (EV/sales and P/E implied value), valuation snapshots |
| browser_captures/live_closes_base36_delta_JETS_SPY_IWM_XLY_HYG_ULCC_JBLU.txt | Compact page capture behind the master file: per ticker, the first close in cents in base 36, then day-to-day deltas | same as master file (HYG scale is coarse here; see next file) | Yahoo Finance, 2026-11-10 | decoded = master file (checked) |
| browser_captures/live_HYG_close_x1000_base36_delta.txt | HYG closes ×1000, same encoding | HYG | Yahoo Finance | decoded = master HYG (checked) |
| browser_captures/stock_1yr_compact_JBLU_ULCC_JETS_SPY_x100.txt | Compact capture behind the one-year file, `yymmdd,JBLU,ULCC,JETS,SPY` ×100 | Adj Close, 251 days | Yahoo Finance, 2026-11-10 | = one-year file (checked) |
| browser_captures/stocks_raw_ULCC_JBLU_2025-11-03_2026-10-30.txt | First pull of the pair closes, `yy-mm-dd,ULCC,JBLU` | Close, 250 days | Yahoo Finance, 2026-11-02 | Pair Overview first build; the 2 Nov Bloomberg row was removed |

## processed/ (all written by code/build_yahoo.py)
| file | what it is | source | used on slide(s) / by |
|---|---|---|---|
| prices_daily_ULCC_JBLU_SPY.csv | `date,frontier,jetblue,spy` 2025-10-31 to 2026-11-09 (byte-identical to the models' `prices.csv`) | master file | model Beta/WACC sheet (SPY = S&P 500 proxy; no ^GSPC used), share price $8.35 / $3.94 (11/09 close), 52-week range |
| yahoo_prices.csv | ULCC, JBLU closes 2025-11-10 to 2026-11-09 | master file | appendix i1_index.py, k4.py |
| daily_prices.csv | ULCC, JBLU closes 2025-11-03 to 2026-11-02, **Yahoo only** | master file | Pair Overview pair chart, k2.py |
| weekly_returns.csv | Weekly log returns (%), W-FRI, last partial week ends 2 Nov 2026 | daily_prices | Pair Overview "Correlated Weekly Returns" scatter, k2.py |
| daily_log_returns_ULCC_JBLU.csv | Daily log returns (%), 2025-11-04 to 2026-11-02 | daily_prices | equity part of `daily_returns.csv` (the jet-fuel version that adds FRED data lives in pair_hedge/) |
| live_etfs.csv, i1_yahoo_1yr.csv | Copies of the raw files under the names the appendix scripts read | raw | a5_*.py, mdl_beta.py, i1_*.py |
| JBLU_vs_JETS_indexed_1yr.csv | JBLU and JETS Adj Close indexed to 10 Nov 2025 = 100 (byte-identical to outputs file of the same name) | one-year file | Company Overview one-year share price chart (ends JBLU 89.3, JETS 121.1) |
| indexed_1yr_ULCC_JBLU_JETS_SPY.csv | All four tickers indexed to 100 | one-year file | reference |
| adjclose_over_close_JETS_SPY.csv | Adj Close / Close factor (shows the dividend adjustments) | both raw files | documents why i1 and live_etfs differ for JETS and SPY |
| pair_price_stats.csv | Weekly corr 0.83, daily corr 0.69, annualised daily log vol (ULCC 78.2%, JBLU 68.0%), 52-week high/low, 11/09 closes | our analysis | Pair Overview co-movement boxes, football field 52-week bar |
| comps_yahoo_2026-11-10.csv | Comps inputs plus EV, EV/FY27E sales, P/E, implied shares (market cap / price), and the final-model rows re-priced at the 11/09 close (ULCC $8.35, JBLU $3.94; market cap rescaled at the Yahoo share count, as in rv/gen/comps.py) | Yahoo + our analysis | Comps sheet |
| comps_peer_percentiles.csv | 25th/median/75th of peer EV/sales (0.61 / 0.76 / 0.93) and P/E (10.30 / 11.75 / 14.36), peers only | our analysis | Comps implied value rows |
| raw_consistency_checks.csv | Results of the cross-checks | our analysis | QA |

## archive/ (superseded)
| file | why superseded |
|---|---|
| superseded_weekly_returns_deck_version.csv | Deck version. Its last row (10.33 / 14.95) was computed from the 2 Nov Bloomberg close; replaced by processed/weekly_returns.csv |
| superseded_HO_capture_2025-12-01_2026-11-02_ho_raw.txt | Earlier HO capture (`mmdd:price×1000`, Dec 2025 to Nov 2026). Its level differs from HO=F front month, so it was likely a different contract month. Replaced by raw/yahoo_HO=F_front_month_close_* |

## Other folders that use these files (not edited here)
- `pair_hedge/raw/yahoo/`: same master close file, one-year file and HO=F capture (identical bytes). `pair_hedge/processed/` daily_prices, weekly_returns, yahoo_prices, live_etfs and i1_yahoo_1yr are byte-identical to the files here.
- `valuation_inputs/raw/prices_daily_yahoo_ULCC_JBLU_SPY.csv` = processed/prices_daily_ULCC_JBLU_SPY.csv. `valuation_inputs/processed/share_counts_prices.csv` uses the 11/09 Yahoo close.
- `code/analysis/appendix_calcs/daily_prices.csv` is still the **deck version with the 2 Nov Bloomberg close (7.49 / 3.16)**. Replace it with processed/daily_prices.csv here.

## Not included / not found
- No volume data, and no price histories for DAL, UAL, AAL, ALK, LUV, ALGT, SNCY or SAVE, were ever pulled. These tickers appear only as single-date comps inputs. No slide uses them, so none were rebuilt.
- ^GSPC was never used. SPY is the S&P 500 proxy everywhere.
- Brent (FRED DCOILBRENTEU) and jet fuel (FRED DJFUELUSGULF) are not Yahoo data and belong to pair_hedge/. The ICE Brent Dec-2027 futures series (BZZ27, `slides/futures_dec27_daily.csv`, archived Brent version of the oil slide) has no recorded source. It was left to pair_hedge/archive.
- Yahoo-hosted news articles cited in research notes (finance.yahoo.com/news/...) are citations, not datasets.
