import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import numpy as np, pandas as pd

px = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/raw/yahoo/yahoo_daily_closes_2025-10-31_2026-11-09.csv'), index_col=0, parse_dates=True)[['frontier', 'jetblue']]
jet = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/jet_fuel_gulf.csv'), index_col=0, parse_dates=True)
r = px.join(jet, how='inner').pct_change().dropna()
fuel = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/daily_returns.csv'), index_col=0)
ratio = np.polyfit(fuel.jet_fuel, fuel.frontier, 1)[0] / np.polyfit(fuel.jet_fuel, fuel.jetblue, 1)[0]
r['pair'] = r.frontier - ratio * r.jetblue

rows = {}
for q, x in r.groupby(r.index.to_period('Q')):
    beta = {leg: np.polyfit(x.jet_fuel, x[leg], 1)[0] for leg in ['frontier', 'jetblue', 'pair']}
    rows[str(q)] = {leg: abs(b) * x.jet_fuel.std() * np.sqrt(252) * 100 for leg, b in beta.items()}
print(pd.DataFrame(rows).round(0).astype(int).to_string())
