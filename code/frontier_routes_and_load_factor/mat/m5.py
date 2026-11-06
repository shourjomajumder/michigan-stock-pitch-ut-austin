import pandas as pd
SEAT=230; SYS_ASM=11103e6; RASM=0.1187
routes=[('Las Vegas–Oakland','2026-08-20',11,407),('Las Vegas–Boise','2026-09-10',4,520),('Nashville–Tampa','2026-10-09',2,612),
        ('Denver–Fort Lauderdale','2026-11-20',7,1703),('Ontario–Oakland','2026-11-21',4,361),('Orlando–Cartagena','2026-12-19',1,1340)]
def run(curve):
    rows=[]
    for name,start,f,dist in routes:
        s=pd.Period(start,'M')
        for m in pd.period_range('2026-10','2027-12',freq='M'):
            if m<s: continue
            idx=curve[min((m-s).n//3,4)]; seats=f*2*SEAT*(30.4/7)*(0.4 if m==s and pd.Timestamp(start).day>15 else 1)
            a=seats*dist; rows.append(dict(route=name,q=str(m.asfreq('Q')),eff=-(a*(1-idx))/SYS_ASM*100,rev=a*RASM*(idx-1)/1e6))
    d=pd.DataFrame(rows); t=d.pivot_table(index='route',columns='q',values='eff',aggfunc='sum').reindex([r[0] for r in routes])
    t.loc['Total']=t.sum(); r=d.groupby('q').rev.sum(); return t,r
for nm,c in [('base',[0.55,0.65,0.75,0.85,1.0]),('aggr',[0.55,0.70,0.90,1.05,1.15])]:
    t,r=run(c); print(nm); print(t.round(3)); print('rev vs avg $M',r.round(2).to_dict()); t.to_csv(f'byroute_{nm}.csv'); r.to_csv(f'rev_{nm}.csv')
