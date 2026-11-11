import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../..')  # repo root
import pandas as pd, numpy as np
p=pd.read_csv(__import__('os').environ.get('PAIR_DAILY',_os.path.join(_R, 'data/hedge_and_macro_risk/macro/work/pair_daily.csv')),parse_dates=['Date']).set_index('Date'); p.columns=['U','J']
r=p.pct_change().dropna(); H=1.163
r['P']=r.U-H*r.J
w=r.loc['2025-11-04':'2026-10-27']
print(len(r),len(w)); sd=w.std()*np.sqrt(252); print('ann vol',sd.round(3).to_dict())
print('corr U,J',w.U.corr(w.J).round(3))
v=[x.split(',') for x in open(__import__('os').environ.get('VOLROLL',_os.path.join(_R, 'code/hedge_and_macro_risk/nonoil/volroll.txt'))).read().strip().split(';')]
v=pd.DataFrame(v).iloc[:,1:].astype(float); print('volroll mean spy,jets,pair,u,j',v.iloc[:,:5].mean().round(1).tolist())
# implied pair corr from leg corrs
F={'JETS':(0.770,0.757,0.007),'IWM':(0.501,0.521,0.040),'SPY':(0.422,0.451,0.050),'XLY':(0.424,0.468,0.070),'HYG':(0.411,0.489,0.112),'VIX':(-0.337,-0.401,0.092),'10y':(-0.278,-0.269,0.002)}
for k,(ru,rj,rp) in F.items():
    num=ru*sd.U-H*rj*sd.J; print(k,'implied pair corr',round(num/sd.P,3),'reported |',rp)
