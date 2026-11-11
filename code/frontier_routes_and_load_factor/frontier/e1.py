import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd
import statsmodels.formula.api as smf

df = pd.read_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier/processed/lcc_quarters.csv'))
print(df.airline.value_counts().to_dict())

raw = smf.ols('traffic ~ fare', df).fit()
fix = smf.ols('traffic ~ fare + seats', df).fit()

for name, m in [('fares only', raw), ('seats fixed', fix)]:
    print(f'{name:12} fare {m.params.fare:.2f}  R2 {m.rsquared:.2f}')
print(fix.params.round(2).to_dict())
