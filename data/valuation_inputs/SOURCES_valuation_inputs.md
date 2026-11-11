# valuation_inputs

Public inputs used for the discount rates and share data. The valuation models themselves are kept by the team
and are not part of this repository (their base forecast is built on licensed consensus data).

| file | what it is | source | used on |
|---|---|---|---|
| raw/damodaran_air_transport_beta_jan2026.csv | Air Transport unlevered beta (cash-corrected 0.76) | Damodaran Online, Jan 2026 | cost of capital |
| raw/damodaran_implied_erp_riskfree_2026-11-01.csv | Implied equity risk premium 4.41%, risk-free 5.29% | Damodaran Online, Nov 1, 2026 | cost of capital |
| raw/damodaran_synthetic_rating_table_large_nonfinancial_jan2026.csv | Interest-coverage rating and default-spread table | Damodaran Online, Jan 2026 | cost of debt |
| raw/prices_daily_yahoo_ULCC_JBLU_SPY.csv | Daily closes used for the regression betas | Yahoo Finance | beta |
| processed/share_counts_prices.csv | Diluted shares (Frontier 230.24M, JetBlue 377.3M) and prices ($8.35, $3.94) | Q3 2026 earnings releases; Yahoo Finance | valuation |
