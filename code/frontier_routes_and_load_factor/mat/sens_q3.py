import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd
src=open('m5.py').read().split('for nm,c in')[0]; exec(src)
src=src  # run() spans 2026-10..2027-12; we only read through 2027Q3
def curve(mid,end): return [0.55,(0.55+mid)/2,mid,end,end+0.10]
mids=[0.70,0.75,0.80,0.85,0.90,0.95]; ends=[0.85,0.90,0.95,1.00,1.05,1.10]
BP=pd.DataFrame(index=mids,columns=ends,dtype=float); UP=BP.copy(); REV=BP.copy()
for m in mids:
  for e in ends:
    t,r=run(curve(m,e)); BP.loc[m,e]=t.loc['Total','2027Q3']*100; REV.loc[m,e]=r['2027Q3']
    UP.loc[m,e]=(r[['2027Q1','2027Q2','2027Q3']]-r['2026Q4']).sum()
print(BP.round(1)); print(REV.round(2)); print(UP.round(1))
BP.to_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/sensq3_bps.csv')); UP.to_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/sensq3_uplift.csv'))
