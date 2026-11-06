import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd
SEAT=230; SYS_ASM=11103e6
routes=[('Las Vegas–Oakland','2026-08-20',11,407,'Aug 20'),('Las Vegas–Boise','2026-09-10',4,520,'Sep 10'),('Nashville–Tampa','2026-10-09',2,612,'Oct 9'),
        ('Denver–Fort Lauderdale','2026-11-20',7,1703,'Nov 20'),('Ontario–Oakland','2026-11-21',4,361,'Nov 21'),('Orlando–Cartagena','2026-12-19',1,1340,'Dec 19')]
curve=[0.55,0.65,0.75,0.85,1.00]; rows=[]
for name,start,f,dist,lab in routes:
    s=pd.Period(start,'M')
    for m in pd.period_range('2026-10','2027-12',freq='M'):
        if m<s: continue
        idx=curve[min((m-s).n//3,4)]
        seats=f*2*SEAT*(30.4/7)*(0.4 if m==s and pd.Timestamp(start).day>15 else 1)
        rows.append(dict(route=name,q=str(m.asfreq('Q')),eff=-(seats*dist*(1-idx))/SYS_ASM*100))
d=pd.DataFrame(rows); t=d.pivot_table(index='route',columns='q',values='eff',aggfunc='sum').reindex([r[0] for r in routes])
t.loc['Total']=t.sum(); print(t.round(3)); t.to_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/byroute_base.csv'))
