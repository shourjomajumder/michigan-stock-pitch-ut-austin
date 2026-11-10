import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import numpy as np, pandas as pd

w = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/weekly_returns.csv'))
f, j = w.frontier, w.jetblue
print(f'correlation  {np.corrcoef(f, j)[0, 1]:.2f}')
print(f'beta         {np.polyfit(j, f, 1)[0]:.1f}')
print(f'same way     {((f * j) > 0).sum()} of {len(w)} weeks')

px = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/daily_prices.csv'), index_col=0)
r = px.pct_change().dropna()
pair = r.frontier - 1.16 * r.jetblue
vol = r.std() * np.sqrt(252)
print(f'vol          frontier {vol.frontier:.0%}  jetblue {vol.jetblue:.0%}  pair {pair.std() * np.sqrt(252):.1%}')
print(f'sharpe       {pair.mean() / pair.std() * np.sqrt(252):.2f}')
print(f'sortino      {pair.mean() / pair[pair < 0].std() * np.sqrt(252):.2f}')

ratio = px.frontier / px.jetblue
mean, sd = ratio.rolling(60).mean(), ratio.rolling(60).std()
print(f'ratio {ratio.iloc[-1]:.2f}x   z {(ratio.iloc[-1] - mean.iloc[-1]) / sd.iloc[-1]:.1f}')
