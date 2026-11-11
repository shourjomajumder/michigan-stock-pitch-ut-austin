"""Export the data behind every pair / hedge chart and print the chart call-out numbers.

    cd processed && python ../code/chart_series.py

Writes processed/series_*.csv. Hedge ratio = Frontier fuel beta / JetBlue fuel beta (k1_hedge.py) = 1.16.
"""
import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
_O = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'out'); _os.makedirs(_O, exist_ok=True)  # outputs that differ from data/
import numpy as np, pandas as pd

fuel = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/daily_returns.csv'), index_col=0, parse_dates=True)
H = np.polyfit(fuel.jet_fuel, fuel.frontier, 1)[0] / np.polyfit(fuel.jet_fuel, fuel.jetblue, 1)[0]
print(f'hedge ratio {H:.4f}')

# 1. Pair Overview: price ratio vs 60-day mean +/- 2 sigma (deck charts the last 97 days)
px = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/daily_prices.csv'), index_col=0, parse_dates=True)
ratio = px.frontier / px.jetblue
m, s = ratio.rolling(60).mean(), ratio.rolling(60).std()
band = pd.DataFrame({'ratio': ratio, 'mean60': m, 'upper_2sd': m + 2 * s, 'lower_2sd': m - 2 * s,
                     'z': (ratio - m) / s}).round(4)
band.to_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/series_price_ratio_bands.csv'))
i0 = band.index.get_loc(pd.Timestamp('2026-01-29'))            # deck chart: every 2nd trading day from 29 Jan
pick = band.index[i0::2].union(band.index[[-1]])
band.loc[pick, ['ratio', 'upper_2sd', 'lower_2sd']].round(3).to_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/series_price_ratio_bands_chart.csv'))
last = band.iloc[-1]
print(f'ratio {last.ratio:.3f}  +2sd {last.upper_2sd:.2f}  -2sd {last.lower_2sd:.2f}  mean {last.mean60:.4f}  '
      f'sd {(last.upper_2sd - last.mean60) / 2:.4f}  z {last.z:.2f}')
wk = px.frontier.iloc[-1] / px.frontier.loc[:px.index[-1] - pd.Timedelta(days=7)].iloc[-1] - 1
print(f'Frontier one-week move to {px.index[-1].date()}: {wk:+.0%}')

# 2. Rolling 60-day correlation with jet fuel (daily log returns, 4 Nov 2025 - 27 Oct 2026)
fuel['pair'] = fuel.frontier - H * fuel.jetblue
rc = pd.DataFrame({k: fuel[k].rolling(60).corr(fuel.jet_fuel) for k in ['frontier', 'jetblue', 'pair']}).dropna()
rc.round(4).to_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/series_rolling60_corr_jet_fuel.csv'))
print('rolling 60d corr with jet fuel, mean:', rc.mean().round(2).to_dict())

# 3. Rolling 60-day volatility and correlation vs S&P 500 (SPY) and airline ETF (JETS), Yahoo closes
r = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/raw/yahoo/yahoo_daily_closes_2025-10-31_2026-11-09.csv'), index_col=0, parse_dates=True).pct_change().loc['2025-11-03':]
r['pair'] = r.frontier - H * r.jetblue
tv = lambda c: r[c].rolling(60).std() * np.sqrt(252) * 100
def driven(leg, f):          # volatility explained by the factor = |rolling beta| x factor vol
    b = r[leg].rolling(60).cov(r[f]) / r[f].rolling(60).var()
    return (b * r[f].rolling(60).std() * np.sqrt(252) * 100).abs()
vol = pd.DataFrame({'spy_vol': tv('spy'), 'jets_vol': tv('jets'), 'pair_vol': tv('pair'),
                    'frontier_vol': tv('frontier'), 'jetblue_vol': tv('jetblue'),
                    'frontier_from_spy': driven('frontier', 'spy'), 'jetblue_from_spy': driven('jetblue', 'spy'),
                    'pair_from_spy': driven('pair', 'spy'),
                    'frontier_from_jets': driven('frontier', 'jets'), 'jetblue_from_jets': driven('jetblue', 'jets'),
                    'pair_from_jets': driven('pair', 'jets')}).dropna()
vol['alone_from_spy_avg'] = (vol.frontier_from_spy + vol.jetblue_from_spy) / 2
vol.round(2).to_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/series_rolling60_volatility.csv'))
print('market (S&P 500) driven vol, mean: alone %.0f%%  pair %.0f%%' % (vol.alone_from_spy_avg.mean(), vol.pair_from_spy.mean()))
for f in ['spy', 'jets']:
    c = pd.DataFrame({k: r[k].rolling(60).corr(r[f]) for k in ['frontier', 'jetblue', 'pair']}).dropna()
    c.round(4).to_csv(_os.path.join(_R, f'data/hedge_and_macro_risk/processed/series_rolling60_corr_{f}.csv'))
    print(f'rolling 60d corr with {f}, mean:', c.mean().round(2).to_dict())

# 4. Jet fuel vs. futures-implied expectation 30 days earlier; monthly average gap
e = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/appendix_calcs/jet_fuel_vs_expected.csv'), index_col=0, parse_dates=True)
mo = e.resample('MS').mean()
mo['gap'] = mo.actual - mo.expected_30d_earlier
mo.round(3).to_csv(_os.path.join(_O, 'series_jet_fuel_monthly_gap.csv'))
sep = mo.loc['2026-09-01']
print(f'September 2026: actual {sep.actual:.2f}  expected {sep.expected_30d_earlier:.2f}  gap {sep.gap:+.2f} $/gal')
j = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/jet_fuel_gulf.csv'), index_col=0, parse_dates=True).jet_fuel
print(f'jet fuel 27 Feb 2026 {j.loc["2026-02-27"]:.2f} -> peak {j.max():.2f} on {j.idxmax().date()}; '
      f'Sept-2026 high {j.loc["2026-09"].max():.2f}')
