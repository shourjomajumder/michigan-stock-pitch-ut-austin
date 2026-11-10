import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
_O = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'out'); _os.makedirs(_O, exist_ok=True)  # intermediates
_L = _os.path.join(_R, 'data/hedge_and_macro_risk/labor')
import pandas as pd, numpy as np
from scipy import stats
a=pd.read_csv(_os.path.join(_O, 'merged.csv'),parse_dates=['amendable','deal','talks_start'])
# 1 Seasonality of deal month
a['m']=a.deal.dt.month; a['q']=a.deal.dt.quarter
print('Deals by quarter (all 51 clean):'); print(a.q.value_counts().sort_index())
obs=a.q.value_counts().sort_index().values; print('chi2 vs uniform p=',round(stats.chisquare(obs).pvalue,3))
print('Share in Q2+Q3:',round(a.q.isin([2,3]).mean(),2))
# 2 Survival: share settled by month 9 / 12 / 18 by early opener (ex-COVID)
s=a.dropna(subset=['early'])
for e in [1,0]:
    t=s[s.early==e].months_adj
    print(f"early={e} n={len(t)}  by 9mo {np.mean(t<=9):.0%}  by 12mo {np.mean(t<=12):.0%}  by 18mo {np.mean(t<=18):.0%}")
# 3 Interim / bridge / extension deals across all agent + original data
rows=[]
for f in ['agent1','agent2','agent3','agent4','agent5']:
    x=pd.read_csv(_os.path.join(_L, f+'.csv')); rows.append(x)
n=pd.concat(rows)
fl=n['flags'].fillna('')
ext=n[fl.str.contains('extension|bridge|early',case=False)].copy()
for c in ['amendable','talks_start','deal']: ext[c]=pd.to_datetime(ext[c],errors='coerce')
ext['months_before_amend']=(ext.amendable-ext.deal).dt.days/30.44
ext['talks_to_deal']=(ext.deal-ext.talks_start).dt.days/30.44
print('\nInterim / extension / bridge deals:',len(ext))
print(ext[['airline','group','amendable','deal','months_before_amend','talks_to_deal','flags']].round(1).to_string(index=False))
