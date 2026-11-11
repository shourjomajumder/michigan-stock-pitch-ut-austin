import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import os as _os
_REPO = _os.environ.get('DATA_REPO', _os.path.abspath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..')))
import pandas as pd, numpy as np
L=pd.read_csv(_os.path.join(_REPO,_os.path.join(_R, 'data/flights_and_fares/raw/google_flights/shared_routes/Shared_routes_fares_full.csv')))
for c in ['JetBlue','United']: L[c]=pd.to_numeric(L[c],errors='coerce')
L['gap']=L.JetBlue-L.United
L['pair']=L.route.str.split('-').apply(lambda r:'-'.join(sorted(r)))
a=pd.read_csv(_os.path.join(_REPO,_os.path.join(_R, 'data/flights_and_fares/raw/dot/dot_car_table1a_bos_ewr_2023_2026q1.csv')))
a['pair']=a[['airport_1','airport_2']].apply(lambda r:'-'.join(sorted(r)),axis=1)
a=a[a.year>=2024]
rows=[]
for _,r in a.iterrows():
    f={};role={}
    if r.carrier_lg in('B6','UA'): f[r.carrier_lg]=r.fare_lg; role[r.carrier_lg]='largest'
    if r.carrier_low in('B6','UA') and r.carrier_low not in f: f[r.carrier_low]=r.fare_low; role[r.carrier_low]='lowest'
    if 'B6' in f and 'UA' in f:
        rows.append(dict(pair=r.pair,q=f'{r.year}Q{r.quarter}',b6=f['B6'],ua=f['UA'],dot_gap=f['B6']-f['UA'],roles=f"B6 {role['B6']} / UA {role['UA']}"))
D=pd.DataFrame(rows)
D=D[D.pair.isin(set(L.pair))]
D.to_csv(_os.path.join(_R, 'data/flights_and_fares/processed/calibration_dot_rows.csv'),index=False)
out=[]
for p,g in D.groupby('pair'):
    l=L[L.pair==p]
    g4=g[g.q>='2025Q2']
    out.append(dict(pair=p,dot_q=len(g),dot_mean=g.dot_gap.mean(),dot_last4=g4.dot_gap.mean() if len(g4) else np.nan,
        roles='; '.join(g.roles.value_counts().index),dot_pct=(g.dot_gap/g.ua).mean()*100,
        live_n=len(l),live_med=l.gap.median(),live_mean=l.gap.mean(),live_within10=(l.gap.abs()<=10).mean()*100,
        b6_live_med=l.JetBlue.median(),ua_live_med=l.United.median()))
O=pd.DataFrame(out); O['bias_med']=O.dot_mean-O.live_med; O['bias_mean']=O.dot_mean-O.live_mean
O.to_csv(_os.path.join(_R, 'data/flights_and_fares/processed/calibration_table.csv'),index=False)
pd.set_option('display.width',250); print(O.round(1).to_string(index=False))
neg=O[O.roles.str.startswith('B6 lowest')]
print('B6-lowest/UA-largest pairs: mean DOT gap %.1f, mean live median %.1f, mean bias %.1f, median bias %.1f'%(neg.dot_mean.mean(),neg.live_med.mean(),neg.bias_med.mean(),neg.bias_med.median()))
print('all: mean bias(med) %.1f, median %.1f'%(O.bias_med.mean(),O.bias_med.median()))
print(D.groupby(D.roles).dot_gap.agg(['count','mean']))
