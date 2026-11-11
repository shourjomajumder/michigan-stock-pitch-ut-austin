import pandas as pd
import os
# consensus revenue per passenger Q4'26 (Bloomberg) is NOT distributed: set REV_PER_PAX_Q426
SEAT=230; RPS=0.81*float(os.environ['REV_PER_PAX_Q426'])  # system revenue per seat (LF x consensus rev/pax Q4'26)
routes=[('Las Vegas–Oakland','2026-08-20',11),('Las Vegas–Boise','2026-09-10',4),('Nashville–Tampa','2026-10-09',2),
        ('Denver–Fort Lauderdale','2026-11-20',7),('Ontario–Oakland','2026-11-21',4),('Orlando–Cartagena','2026-12-19',1)]
# age bucket -> (LF, yield index); RASM index = LF/0.81*yield
curve={0:(0.72,0.62),1:(0.77,0.68),2:(0.81,0.75),3:(0.81,0.85),4:(0.81,1.00)}
months=pd.period_range('2026-08','2027-12',freq='M'); rows=[]
for name,start,f in routes:
    s=pd.Period(start,'M'); 
    for m in months:
        if m<s: continue
        age=(m-s).n; b=min(age//3,4); lf,y=curve[b]
        seats=f*2*SEAT*(30.4/7)*(0.4 if m==s and pd.Timestamp(start).day>15 else 1)
        idx=lf/0.81*y
        rows.append(dict(route=name,q=str(m.asfreq('Q')),seats=seats,rev=seats*RPS*idx,mat=seats*RPS))
d=pd.DataFrame(rows); q=d.groupby('q')[['seats','rev','mat']].sum()
q['idx']=q.rev/q.mat; q['gap']=q.mat-q.rev
print((q/[1e3,1e6,1e6,1,1e6]).round(2))
for b,(lf,y) in curve.items(): print(b, lf, y, round(lf/0.81*y,2))
