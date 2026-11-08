import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd, numpy as np, io, contextlib
src=open('m5.py').read().split('for nm,c in')[0]; exec(src)
shape=np.array([0,0.25,7/12,5/6,1.0])   # shape of our aggressive ramp (55→70→90→105→115)
starts=[0.45,0.50,0.55,0.60,0.65]; peaks=[1.00,1.05,1.10,1.15,1.20]
A=pd.DataFrame(index=starts,columns=peaks,dtype=float); B=A.copy()
for s in starts:
  for p in peaks:
    c=list(s+(p-s)*shape); t,r=run(c)
    A.loc[s,p]=r['2027Q4']; B.loc[s,p]=(r[['2027Q1','2027Q2','2027Q3','2027Q4']]-r['2026Q4']).sum()
print(A.round(1)); print(B.round(1))
A.to_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/sens_q4.csv')); B.to_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/sens_uplift.csv'))
