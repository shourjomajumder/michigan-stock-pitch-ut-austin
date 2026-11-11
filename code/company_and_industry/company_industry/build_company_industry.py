"""Build processed tables for the company / industry overview slides and risk/catalyst slides.

Run from the repo folder:  cd company_industry/code && python build_company_industry.py
Inputs are in ../raw (public data: Yahoo Finance, FRED/EIA, FRED/BTS, FRED/BLS, company filings).
Outputs go to ../processed.
"""
import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import os
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, '..', 'raw')
OUT = os.path.join(HERE, '..', 'processed')
os.makedirs(OUT, exist_ok=True)


def out(df, name):
    df.to_csv(os.path.join(OUT, name), index=False)
    print(f'wrote {name} ({len(df)} rows)')


# 1. One-year share price, weekly (Friday close) indexed to 2025-11-10 = 100  -> main slide 6, appendix slide 26
p = pd.read_csv(os.path.join(RAW, _os.path.join(_R, 'data/company_and_industry/raw/yahoo_daily_close_JBLU_ULCC_JETS_SPY_2025-11-10_2026-11-09.csv')),
                index_col=0, parse_dates=True)
w = pd.concat([p.iloc[[0]], p.resample('W-FRI').last()])
w = w[~w.index.duplicated()] if w.index.duplicated().any() else w
idx = (w / p.iloc[0] * 100).round(1)
idx.index.name = 'week_ending'
out(idx.reset_index()[['week_ending', 'JBLU', 'ULCC', 'JETS', 'SPY']], _os.path.join(_R, 'data/company_and_industry/processed/share_price_weekly_indexed.csv'))
summ = pd.DataFrame({'ticker': ['JBLU', 'ULCC', 'JETS', 'SPY'],
                     'close_2025_11_10': [p[c].iloc[0] for c in ['JBLU', 'ULCC', 'JETS', 'SPY']],
                     'close_last': [p[c].iloc[-1] for c in ['JBLU', 'ULCC', 'JETS', 'SPY']]})
summ['last_date'] = p.index[-1].date()
summ['change_pct'] = ((summ.close_last / summ.close_2025_11_10 - 1) * 100).round(1)
out(summ, _os.path.join(_R, 'data/company_and_industry/processed/share_price_1yr_summary.csv'))

# 2. Jet fuel: last pre-war close vs latest high  -> main slide 3 ($2.43 -> $4.63, +91%)
j = pd.read_csv(os.path.join(RAW, _os.path.join(_R, 'data/company_and_industry/raw/fred_DJFUELUSGULF_jet_fuel_gulf_coast_daily.csv')),
                parse_dates=['Date'], index_col='Date').iloc[:, 0]
pre, post = j.loc['2026-02-27'], j.loc['2026-10-20']
fuel = pd.DataFrame([
    {'point': 'last close before Iran war (2026-02-27)', 'usd_per_gal': pre},
    {'point': 'deck end point (2026-10-20)', 'usd_per_gal': post},
    {'point': 'change_pct', 'usd_per_gal': round((post / pre - 1) * 100, 1)},
])
out(fuel, _os.path.join(_R, 'data/company_and_industry/processed/jet_fuel_prewar_vs_oct2026.csv'))
m = j.resample('ME').mean().round(3).reset_index()
m.columns = ['month_end', 'jet_fuel_usgc_avg_usd_gal']
out(m, _os.path.join(_R, 'data/company_and_industry/processed/jet_fuel_monthly_avg.csv'))

# 3. CPI airline fares, Q3 2026 vs Q3 2025  -> main slide 3 ("US airfares rose 23% YoY in Q3 2026")
c = pd.read_csv(os.path.join(RAW, _os.path.join(_R, 'data/company_and_industry/raw/fred_CUUR0000SETG01_cpi_airline_fares_2024-01_2026-10.csv')),
                comment='#', parse_dates=['date'], index_col='date').iloc[:, 0]
rows = []
for mth in ['07', '08', '09']:
    a, b = c.loc[f'2025-{mth}-01'], c.loc[f'2026-{mth}-01']
    rows.append({'period': f'2026-{mth}', 'cpi_2025': a, 'cpi_2026': b, 'yoy_pct': round((b / a - 1) * 100, 1)})
qa = c.loc['2025-07-01':'2025-09-01'].mean(); qb = c.loc['2026-07-01':'2026-09-01'].mean()
rows.append({'period': 'Q3 avg', 'cpi_2025': round(qa, 3), 'cpi_2026': round(qb, 3), 'yoy_pct': round((qb / qa - 1) * 100, 1)})
out(pd.DataFrame(rows), _os.path.join(_R, 'data/company_and_industry/processed/cpi_airline_fares_q3_2026_yoy.csv'))

# 4. US domestic load factor 2025 annual  -> main slide 3 (81.7%)
lf = pd.read_csv(os.path.join(RAW, _os.path.join(_R, 'data/company_and_industry/raw/fred_LOADFACTORDD11_2024-01_2026-05.csv')),
                 comment='#', parse_dates=['date'], index_col='date').iloc[:, 0]
yr = lf.groupby(lf.index.year).agg(['mean', 'count']).round(2).reset_index()
yr.columns = ['year', 'mean_monthly_load_factor_pct', 'months']
out(yr, _os.path.join(_R, 'data/company_and_industry/processed/us_domestic_load_factor_annual.csv'))

# 5. Company tables transcribed from filings (see ../raw/public_sources_register.csv)
out(pd.DataFrame({
    'region': ['Domestic & Canada', 'Caribbean & Latin America', 'Atlantic (Europe)'],
    'fy2025_usd_m': [5452, 3139, 471], 'fy2024_usd_m': [5640, 3169, 470], 'fy2023_usd_m': [6072, 3282, 261]}),
    _os.path.join(_R, 'data/company_and_industry/processed/jblu_operating_revenue_by_region.csv'))

pax = 33.2  # millions, FY2025
fare, nonfare, other = round(44.60 * pax), 3598 - round(44.60 * pax), 126
out(pd.DataFrame({'line': ['Fare', 'Non-fare passenger', 'Other', 'Total'],
                  'fy2025_usd_m': [fare, nonfare, other, fare + nonfare + other],
                  'basis': ['fare/pax $44.60 x 33.2M pax', 'passenger revenue $3,598M less fare',
                            'reported', 'reported $3,724M']}), _os.path.join(_R, 'data/company_and_industry/processed/ulcc_fy2025_revenue_mix.csv'))

out(pd.DataFrame({
    'as_of': ["Dec '23", "Dec '24", "Dec '25", "Jun '26", "Sep '26"],
    'A320ceo': [8, 8, 6, 6, 6], 'A321ceo': [21, 21, 21, 21, 21],
    'A320neo': [82, 82, 89, 72, 68], 'A321neo': [25, 48, 60, 66, 69],
    'total': [136, 159, 176, 165, 164],
    'note': ['total public (Q4 2024 8-K); type split from team model, not re-verified',
             'Q4 2024 8-K', 'Q4 2025 release', 'Q2 2026 8-K', 'Q3 2026 release']}),
    _os.path.join(_R, 'data/company_and_industry/processed/ulcc_fleet_by_type.csv'))

out(pd.DataFrame({
    'year': ['2026', '2027', '2028', '2029', '2030', 'thereafter', 'total'],
    'fy25_10k_maturities_usd_m': [755, 411, 516, 1768, 589, 4459, 8498],
    'oct2026_reuters_usd_m': [None, 477, 582, 1800, None, None, 8400]}),
    _os.path.join(_R, 'data/company_and_industry/processed/jblu_debt_maturities.csv'))

out(pd.DataFrame([
    ['JetBlue', "Q4 '26", 'Jan 2027', 'prior-year analog 2026-01-27'],
    ['JetBlue', "Q1 '27", 'Apr 2027', 'prior-year analog 2026-04-28'],
    ['JetBlue', "Q2 '27", 'Jul 2027', 'prior-year analog 2026-07-28'],
    ['JetBlue', "Q3 '27", 'Oct 2027', 'prior-year analog 2026-10-26'],
    ['Frontier', "Q4 '26", 'Feb 2027', 'prior-year analog 2026-02-11'],
    ['Frontier', "Q1 '27", 'Apr 2027', 'prior-year analog late Apr 2026 (exact date not re-verified)'],
    ['Frontier', "Q2 '27", 'Jul 2027', 'prior-year analog 2026-07-29'],
    ['Frontier', "Q3 '27", 'Oct 2027', 'prior-year analog 2026-10-28'],
], columns=['company', 'quarter', 'expected_month', 'basis']), _os.path.join(_R, 'data/company_and_industry/processed/catalyst_earnings_dates.csv'))
