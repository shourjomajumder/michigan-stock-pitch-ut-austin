import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd

p = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/processed/yahoo_prices.csv'), index_col=0)
p['jets'] = pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/raw/yahoo/yahoo_1yr_closes_JBLU_ULCC_JETS_SPY.csv'), index_col=0).JETS
idx = p / p.iloc[0] * 100
for c in idx:
    end = idx[c].iloc[-1]
    print(f'{c:<9}{end:6.1f}{end - 100:+5.0f}%')
