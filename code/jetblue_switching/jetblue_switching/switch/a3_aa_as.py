import csv, glob, os, numpy as np
D=os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../../data/jetblue_switching/raw/dot_table6/a3_aa_as_seattle')  # SEA-*.csv Table 6 pulls
def load(r):
    out={}
    for row in csv.DictReader(open(f'{D}/{r}.csv')):
        t=(int(row['year']),int(row['quarter'])); s={}
        s[row['carrier_lg']]=float(row['large_ms']); s[row['carrier_low']]=float(row['lf_ms'])
        out[t]=s
    return out
Q=[(y,q) for y in range(2017,2027) for q in range(1,5) if (y,q)<=(2026,1)]
def idx(t): return (t[0]-2020)*4+(t[1]-2)   # k, 0=2020Q2
OV=['SEA-PHL','SEA-DFW','SEA-MIA','SEA-CHI','SEA-NYC','SEA-BOS','SEA-CLT']
CT=['SEA-DEN','SEA-ATL','SEA-IAH','SEA-SLC','SEA-LAS','SEA-LAX','SEA-MSP']
data={r:load(r) for r in OV+CT}
def ser(r,c): return {t:data[r][t].get(c) for t in Q if t in data[r]}
def yoy19(r,c):
    s=ser(r,c); o={}
    for t,v in s.items():
        b=s.get((2019,t[1]))
        o[t]=None if v is None or b is None else v-b
    return o
def pre4(r,c):
    s=ser(r,c); v=[s.get(t) for t in [(2019,2),(2019,3),(2019,4),(2020,1)]]
    v=[x for x in v if x is not None]; return np.mean(v) if len(v)>=3 else None
# control AS YoY-2019 average
ctl={}
for t in Q:
    v=[yoy19(r,'AS')[t] for r in ['SEA-DEN','SEA-ATL','SEA-SLC','SEA-LAS','SEA-LAX'] if yoy19(r,'AS').get(t) is not None]
    ctl[t]=(np.mean(v),len(v)) if v else (None,0)
rows=[]
for r in OV+CT:
    for c in ['AS','AA','DL','UA']:
        s=ser(r,c); n=sum(v is not None for v in s.values())
        if n<10: continue
        p=pre4(r,c); y=yoy19(r,c)
        for t in Q:
            v=s.get(t)
            if v is None: continue
            k=idx(t); did=None
            if c=='AS' and r in OV and y[t] is not None and ctl[t][0] is not None: did=y[t]-ctl[t][0]
            rows.append(dict(case='AA-AS WCIA (earn/burn 2020-04-01; oneworld 2021-03-31)',route=r,carrier=c,
              event_quarter='2020Q2',k=k,period=f'{t[0]}Q{t[1]}',share=round(v*100,2),
              change_vs_pre=None if p is None else round((v-p)*100,2),
              change_vs_2019_sameq=None if y[t] is None else round(y[t]*100,2),
              did_vs_control=None if did is None else round(did*100,2),
              group='overlap' if r in OV else 'control'))
import pandas as pd
df=pd.DataFrame(rows)
os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out'), exist_ok=True)
df.to_pickle(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out', 'a3.pkl'))
print(pd.DataFrame({f'{t[0]}Q{t[1]}':[None if ctl[t][0] is None else round(ctl[t][0]*100,1),ctl[t][1]] for t in Q}).T.to_string())
