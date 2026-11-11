import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../../../..')  # repo root
import re,statistics as st,csv
W=_os.path.join(_R, 'data/flights_and_fares/raw/google_flights/jfk27/5_work/')
rows=[]
for line in open(W+'raw.txt'):
    r,d,rest=line.strip().split('|',2)
    for m in re.finditer(r'(\w+)@(\w+)=(\d+)\((\d)/(\d)\)',rest):
        a,ap,f,c,b=m.groups()
        ft={'United':'Basic Economy (no carry-on)'}.get(a,'lowest economy shown; 1 carry-on')
        if a=='JetBlue': ft='lowest shown (Blue/Main Base, 1 carry-on)'
        rows.append(dict(section='economy_lowest',route='JFK-'+r if ap=='JFK' else ap+'-'+r,dest=r,date=d,airline=a,airport=ap,fare=int(f),fare_type=ft))
tiers=[('LAX','2027-01-13','JetBlue','JFK',144,'Main Base (airline direct; $140 headline via OTA)'),('LAX','2027-01-13','JetBlue','JFK',199,'Main'),
('LAX','2027-01-13','United','EWR',149,'Basic Economy'),('LAX','2027-01-13','United','EWR',214,'Economy'),
('SFO','2027-06-16','JetBlue','JFK',214,'Main Base'),('SFO','2027-06-16','JetBlue','JFK',269,'Main'),
('SFO','2027-06-16','United','EWR',221,'Basic Economy'),('SFO','2027-06-16','United','EWR',286,'Economy')]
for r,d,a,ap,f,t in tiers: rows.append(dict(section='fare_tier',route=ap+'-'+r,dest=r,date=d,airline=a,airport=ap,fare=f,fare_type=t))
for line in open(W+'prem.txt'):
    _,r,d,rest=line.strip().split('|',3)
    for m in re.finditer(r'(\w+)@(\w+)=(\d+)',rest):
        a,ap,f=m.groups()
        t={'JetBlue':'Mint','United':'United business (Polaris-branded on p.s. routes)'}.get(a,'business/first lowest')
        rows.append(dict(section='business',route=ap+'-'+r,dest=r,date=d,airline=a,airport=ap,fare=int(f),fare_type=t))
with open(_os.path.join(_R, 'data/flights_and_fares/raw/google_flights/jfk27/5_fares.csv'),'w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=['section','dest','date','airline','airport','route','fare','fare_type','source','searched'])
    w.writeheader()
    for x in rows: x['source']='Google Flights (public), NYC all airports, one-way, nonstop, 1 adult';x['searched']='2026-11-11';w.writerow(x)
eco=[x for x in rows if x['section']=='economy_lowest']
dates=sorted({x['date'] for x in eco})
out=[]
for dest in ['LAX','SFO']:
    out.append(f'\n### NYC-{dest}\n\n| Date | JetBlue JFK | Delta JFK | American JFK | Alaska | United EWR | JFK spread (max-min of B6/DL/AA) | JFK cluster ≤$15 | B6 − UA |\n|---|---|---|---|---|---|---|---|---|')
    for d in dates:
        g={}
        for x in eco:
            if x['dest']==dest and x['date']==d:
                k=x['airline']; 
                if x['airport']=='JFK' or k in('United','Alaska'): 
                    if k not in g or x['fare']<g[k][0]: g[k]=(x['fare'],x['airport'])
        jfk=[g[k][0] for k in ('JetBlue','Delta','American') if k in g]
        sp=max(jfk)-min(jfk)
        al=f"{g['Alaska'][0]} ({g['Alaska'][1]})" if 'Alaska' in g else 'none'
        out.append(f"| {d} | {g['JetBlue'][0]} | {g['Delta'][0]} | {g['American'][0]} | {al} | {g['United'][0]} | {sp} | {'yes' if sp<=15 else 'no'} | {g['JetBlue'][0]-g['United'][0]:+d} |")
    meds={}
    for a in ['JetBlue','Delta','American','Alaska','United']:
        v=[min(x['fare'] for x in eco if x['dest']==dest and x['date']==d and x['airline']==a and (x['airport']=='JFK' or a in('United','Alaska'))) for d in dates if any(x['dest']==dest and x['date']==d and x['airline']==a and (x['airport']=='JFK' or a in('United','Alaska')) for x in eco)]
        meds[a]=(st.median(v),len(v))
    out.append('\nMedians: '+'; '.join(f'{a} {m[0]:g} (n={m[1]})' for a,m in meds.items()))
    out.append('Median gap JetBlue minus: '+'; '.join(f'{a} {meds["JetBlue"][0]-m[0]:+g}' for a,m in meds.items() if a!='JetBlue'))
print('\n'.join(out))
