import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import numpy as np, pandas as pd

fuel = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/daily_returns.csv'), index_col=0)
ratio = np.polyfit(fuel.jet_fuel, fuel.frontier, 1)[0] / np.polyfit(fuel.jet_fuel, fuel.jetblue, 1)[0]

r = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/raw/yahoo/yahoo_daily_closes_2025-10-31_2026-11-09.csv'), index_col=0, parse_dates=True).pct_change().loc['2025-11-04':]
r['pair'] = r.frontier - ratio * r.jetblue

def from_spy(leg):
    beta = r[leg].rolling(60).cov(r.spy) / r.spy.rolling(60).var()
    return (beta * r.spy.rolling(60).std() * np.sqrt(252) * 100).abs()

alone = (from_spy('frontier') + from_spy('jetblue')) / 2
hedged = from_spy('pair')
out = pd.DataFrame({'alone': alone, 'pair': hedged}).dropna()
print(out.mean().round(0).astype(int).to_dict())
print(out.resample('QE').mean().round(0).astype(int).T.to_string())
