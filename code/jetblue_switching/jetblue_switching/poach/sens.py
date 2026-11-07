import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../..')  # repo root
import pandas as pd
PAX=2.73e6; FARE=284
qs=["Q3'26","Q4'26","Q1'27","Q2'27","Q3'27","Q4'27"]  # trigger = May 14 2026 (Q2'26); index 1 = first full qtr after
sc={'Bear':(0.25,4,4),'Base':(0.5,2,4),'Bull':(1.0,1,3)}
rows=[]
for n,(peak,lag,ramp) in sc.items():
    for i,q in enumerate(qs, start=1):
        pts=0 if i<lag else min(1,(i-lag+1)/ramp)*peak
        rows.append(dict(sc=n,q=q,pts=pts,pax=pts/100*PAX,rev=pts/100*PAX*FARE/1e6))
d=pd.DataFrame(rows)
for c in ['pts','pax','rev']: print(d.pivot(index='sc',columns='q',values=c)[qs].round(2 if c!='pax' else -2))
print(d.groupby('sc').rev.sum().round(1))
print('two-way annual $M at full effect')
for p in [0.25,0.5,0.75,1.0]: print(p,[round(p/100*PAX*4*f/1e6,1) for f in [148,220,284]])
d.to_csv(_os.path.join(_R, 'data/jetblue_switching/processed/poach/sens.csv'),index=False)
