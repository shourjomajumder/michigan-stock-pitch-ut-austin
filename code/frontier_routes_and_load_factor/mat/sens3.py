import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd, numpy as np
src=open('m5.py').read().split('for nm,c in')[0]; exec(src)
def curve(mid,end): return [0.55,(0.55+mid)/2,mid,(mid+end)/2,end]
mids=[0.70,0.75,0.80,0.85,0.90,0.95]; ends=[0.95,1.00,1.05,1.10,1.15,1.20]
Q4=pd.DataFrame(index=mids,columns=ends,dtype=float); UP=Q4.copy(); FY=Q4.copy(); BP=Q4.copy()
for m in mids:
  for e in ends:
    t,r=run(curve(m,e)); Q4.loc[m,e]=r['2027Q4']; BP.loc[m,e]=t.loc['Total','2027Q4']*100
    FY.loc[m,e]=r[['2027Q1','2027Q2','2027Q3','2027Q4']].sum(); UP.loc[m,e]=(r[['2027Q1','2027Q2','2027Q3','2027Q4']]-r['2026Q4']).sum()
for n,d in [('Q4 $M',Q4),('Q4 bps',BP),('FY27',FY),('UPvsQ4',UP)]: print(n); print(d.round(1))
Q4.to_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/sens_q4.csv')); FY.to_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/sens_fy27.csv')); UP.to_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/sens_uplift.csv')); BP.to_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/sens_bps.csv'))
