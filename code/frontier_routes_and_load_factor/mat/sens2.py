import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd, numpy as np
src=open('m5.py').read().split('for nm,c in')[0]; exec(src)
def curve(T,peak):  # T = months to reach system-average RASM; linear ramp from 55%, then same slope up to peak
    slope=0.45/(T/3); return [min(0.55+slope*q,peak) if 0.55+slope*q<1 else min(0.55+slope*q,peak) for q in range(5)]
Ts=[6,8,10,12,15,18]; peaks=[1.00,1.05,1.10,1.15,1.20]
Q4=pd.DataFrame(index=Ts,columns=peaks,dtype=float); UP=Q4.copy(); FY=Q4.copy()
for T in Ts:
  for p in peaks:
    t,r=run(curve(T,p)); Q4.loc[T,p]=r['2027Q4']; FY.loc[T,p]=r[['2027Q1','2027Q2','2027Q3','2027Q4']].sum()
    UP.loc[T,p]=(r[['2027Q1','2027Q2','2027Q3','2027Q4']]-r['2026Q4']).sum()
for n,d in [('Q4',Q4),('FY27',FY),('UPvsQ4',UP)]: print(n); print(d.round(1))
print([round(x,3) for x in curve(8,1.15)],[round(x,3) for x in curve(12,1.0)])
Q4.to_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/sens_q4.csv')); FY.to_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/sens_fy27.csv')); UP.to_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/sens_uplift.csv'))
