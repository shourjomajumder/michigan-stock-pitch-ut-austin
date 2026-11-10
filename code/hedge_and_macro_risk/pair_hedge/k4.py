import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd

px = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/yahoo_prices.csv'), index_col=0, parse_dates=True)
jet = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/jet_fuel_gulf.csv'), index_col=0, parse_dates=True)
moves = px.join(jet, how='outer').pct_change(fill_method=None) * 100
moves['pair'] = moves.frontier - 1.16 * moves.jetblue

events = ['2026-03-02', '2026-03-23', '2026-05-26', '2026-07-13',
          '2026-08-03', '2026-09-10', '2026-11-02']
print(moves.loc[events, ['jet_fuel', 'frontier', 'jetblue', 'pair']].round(1))
