import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd
src=open('m5.py').read().split('for nm,c in')[0]; exec(src)
c=[0.55,0.70,0.90,1.05,1.15]; rows=[]
for name,start,f,dist in routes:
    s=pd.Period(start,'M')
    for m in pd.period_range('2026-10','2027-12',freq='M'):
        if m<s: continue
        idx=c[min((m-s).n//3,4)]; seats=f*2*SEAT*(30.4/7)*(0.4 if m==s and pd.Timestamp(start).day>15 else 1)
        a=seats*dist; rows.append(dict(route=name,q=str(m.asfreq('Q')),asm=a,idx=idx,rev=a*RASM*(idx-1)/1e6))
d=pd.DataFrame(rows)
g=d.groupby(['route','q']).apply(lambda x: pd.Series({'idx':(x.idx*x.asm).sum()/x.asm.sum(),'rev':x.rev.sum(),'asm':x.asm.sum()})).reset_index()
I=g.pivot(index='route',columns='q',values='idx').reindex([r[0] for r in routes]); R=g.pivot(index='route',columns='q',values='rev').reindex(I.index)
info=pd.DataFrame([dict(route=n,start=s,f=f,dist=dist,wkseats=f*2*SEAT,qasm=f*2*SEAT*dist*13/1e6) for n,s,f,dist in routes]).set_index('route')
info['share']=info.qasm*1e6/(SYS_ASM)*100
info['fy27']=R[[q for q in R.columns if q.startswith('2027')]].sum(axis=1)
print(info.round(3)); print(I.round(3)); print(R.round(2)); print(R.sum().round(2), info[['wkseats','qasm','share','fy27']].sum().round(3))
g.pivot(index='route',columns='q',values='asm').reindex(I.index).to_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/detail_asm.csv')); info.to_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/detail_info.csv')); I.to_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/detail_idx.csv')); R.to_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/detail_rev.csv'))
