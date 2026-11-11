import os as _os; _D = _os.path.dirname(_os.path.abspath(__file__))  # output -> out/ next to this script
# a10_entry_ramp: event-time entrant/incumbent share paths from DOT Table 6 (values transcribed from SODA API pulls 2026-11-11)
import numpy as np, csv
N=np.nan
SRC="https://data.transportation.gov/resource/yj5y-b2ir.json (DOT Consumer Airfare Report Table 6; city-pair query via SODA)"
def q(y,qq): return y*4+qq-1
def lab(i): return f"{i//4}Q{i%4+1}"
# (case, route, incumbent, entrant, start yr,q, incumbent series, entrant series (nan=not shown), event (y,q), last usable (y,q), note)
C=[
("Delta SEA hub build vs Alaska","SEA-GEG","AS","DL",2013,1,
 [99,99,99,99,99,99,99,94,93.9,93.5,93.1,92.5,90.4,92.3,90.7,88.2,89.3,87.1,84.3,79.2,88.0,87.0,83.5,80.0,79.9,75.0,83.5,84.8,81.5],
 [N,N,N,N,N,N,N,5.0,5.9,6.3,N,N,9.4,7.4,N,11.6,N,N,15.5,N,N,12.9,16.3,19.9,20.0,24.9,16.3,N,18.0],(2014,4),(2019,4),"AS ~monopoly pre; DL visible only when lowest-fare"),
("Delta SEA hub build vs Alaska","SEA-BOI","AS","DL",2014,1,
 [99,99,99,98,98.8,87.2,82.2,80.3,76.7,80.4,77.6,75.3,73.0,74.1,67.6,70.5,76.7,75.8,72.5,72.4,76.6,75.2,78.0,77.1,78.0],
 [N,N,N,N,N,12.5,17.5,19.5,22.9,19.3,22.2,24.4,26.9,25.6,32.0,29.1,N,24.0,27.2,27.4,23.2,24.5,21.8,N,N],(2015,2),(2019,4),"AS ~monopoly pre; partial reversal 2018-19"),
("Delta SEA hub build vs Alaska","SEA-EUG","AS","DL",2016,1,
 [98.3,98.5,98.6,98.5,98.3,75.8,71.9,73.7,70.8,66.7,67.6,70.5,65.4,65.0,69.1,69.8,69.5],
 [N,N,N,N,N,21.8,26.5,25.0,28.2,32.4,31.2,28.5,33.4,34.1,29.8,29.2,29.6],(2017,2),(2020,1),"AS ~monopoly pre; 2020Q1 last pre-COVID"),
("Delta SEA hub build vs Alaska","SEA-PDX","AS","DL",2013,1,
 [93,86,92,90,92,92,93,93,94.5,94.0,93.5,93.5,93.3,92.6,89.0,86.8,91.7,92.3,87.6,84.9,89.5,89.3,89.8,85.6,86.3,79.9,84.5,86.0],
 [N,N,N,N,N,N,3.0,6.0,N,6.0,6.4,6.4,6.7,7.4,11.0,13.2,N,N,N,N,N,10.6,N,14.4,N,20.1,15.5,14.0],(2014,3),(2019,4),"DL replaced exiting UA (UA 7-15% in 2012-14); AS loss delayed ~2 yrs"),
("Delta BOS build vs JetBlue","BOS-PIT","B6","DL",2016,1,
 [55.8,51.0,53.3,53.9,59.0,57.3,60.0,58.8,60.3,55.6,52.6,52.8,59.3,53.5,56.2,54.7],
 [N,N,N,N,N,N,N,15.6,13.5,18.5,22.1,21.3,27.9,34.9,31.1,31.7],(2017,4),(2019,4),"DL share came mostly from AA/others; B6 loss small"),
("Delta BOS build vs JetBlue","BOS-BUF","B6","DL",2016,1,
 [64.2,75.1,78.2,76.2,73.4,78.0,79.4,75.0,67.6,71.1,69.7,69.5,62.6,67.5,67.0,65.6],
 [N,N,N,N,N,N,13.8,18.0,N,23.0,24.9,24.3,31.2,27.8,27.6,29.1],(2017,3),(2019,4),"B6 lost ~10pt"),
("Southwest enters Denver (Jan 2006)","DEN-PHX","HP/UA","WN",2005,1,
 [N]*20,
 [N,N,N,N,20,26,27,N,N,28,28,31,32,31,35,38,44,45,47,45],(2006,1),(2009,4),"LCC entry; incumbent split HP/UA/F9 not trackable"),
("Southwest enters Denver (Jan 2006)","DEN-LAS","UA","WN",2005,1,
 [35,38,38,43,30,29,31,N,34,N,N,N,N,N,N,N,N,N,N,N],
 [N,N,N,N,25,29,N,28,26,34,35,36,32,35,38,41,44,45,45,46],(2006,1),(2009,4),"UA n/a once WN/F9 hold both slots"),
("Southwest enters Denver (Jan 2006)","DEN-CHI","UA","WN",2005,1,
 [37,45,48,53,46,44,45,42,42,36,34,35,40,39,33,34,36,35,33,35],
 [N,N,N,N,12,12,13,N,N,18,19,N,N,N,N,N,N,N,N,N],(2006,1),(2009,4),"Chicago = ORD+MDW; WN later hidden by F9 as low-fare"),
]
rows=[];summ=[]
def sm(a):  # centered 3q mean ignoring nan
    return np.array([np.nanmean(a[max(0,i-1):i+2]) if np.any(~np.isnan(a[max(0,i-1):i+2])) else N for i in range(len(a))])
for case,rt,inc,ent,y0,q0,I,E,ev,last,note in C:
    I=np.array(I,float);E=np.array(E,float); e=q(*ev)-q(y0,q0); L=q(*last)-q(y0,q0)
    pre=np.nanmean(I[e-4:e]) if e>=4 else N
    epre=0.0
    for k in range(0,13):
        i=e+k
        if i>L or i>=len(I): break
        yq=lab(q(y0,q0)+i)
        if not np.isnan(E[i]): rows.append([case,rt,ent,lab(q(*ev)),k,E[i],round(E[i]-epre,1),f"entrant share (lowest-fare slot) {yq}; "+note,SRC])
        if not np.isnan(I[i]) and not np.isnan(pre):
            # yoy same-quarter change too
            yoy = I[i]-I[i-4] if i>=4 and not np.isnan(I[i-4]) else N
            rows.append([case,rt,inc,lab(q(*ev)),k,I[i],round(I[i]-pre,1),f"incumbent share (largest slot) {yq}; pre4avg={pre:.1f}; YoY={'' if np.isnan(yoy) else round(yoy,1)}",SRC])
    # mature entrant share = mean of visible entrant values in last 4 usable quarters (pre-COVID)
    if pre>=98: E=np.where(np.isnan(I),E,pre-I)  # monopoly pre: implied entrant = incumbent loss
    Ew=E[:L+1]; mat=np.nanmean(Ew[L-3:L+1])
    Es=sm(Ew)
    path=[Es[e+k] if e+k<=L else N for k in range(L-e+1)]
    f50=next((k for k in range(len(path)) if not np.isnan(path[k]) and path[k]>=0.5*mat),None)
    f90=next((k for k in range(len(path)) if not np.isnan(path[k]) and path[k]>=0.9*mat),None)
    # incumbent loss
    loss=[pre-I[e+k] if e+k<=L and e+k<len(I) else N for k in range(13)]
    Il=I[:L+1]; matloss=pre-np.nanmean(Il[L-3:L+1]) if not np.isnan(pre) else N
    summ.append((rt,lab(q(*ev)),mat,f50,f90,[None if np.isnan(x) else round(x,1) for x in path],pre,matloss,[None if np.isnan(x) else round(x,1) for x in loss],L-e))
_os.makedirs(_os.path.join(_D, 'out'), exist_ok=True)
with open(_os.path.join(_D, 'out', 'a10_core.csv'),'w',newline='') as f:
    w=csv.writer(f);w.writerow(['case','route','carrier','event_quarter','k','share','change_vs_pre','note','source'])
    w.writerows(rows)
for s in summ:
    print(f"{s[0]} ev {s[1]} kmax {s[9]} mature_entrant {s[2]:.1f} k50 {s[3]} k90 {s[4]}\n  entrant sm path {s[5]}\n  inc pre {s[6]:.1f} mature loss {s[7]:.1f} loss path {s[8]}")
# normalized typical path
P=[];Lp=[]
for s in summ:
    m=s[2]; P.append([N if x is None else x/m for x in (s[5]+[None]*13)[:13]])
    if not np.isnan(s[7]) and s[7]>2: Lp.append([N if x is None else x/s[7] for x in s[8]])
P=np.array(P,float);Lp=np.array(Lp,float)
print('median entrant frac of mature by k',np.round(np.nanmedian(P,0),2), 'n',np.sum(~np.isnan(P),0))
print('median incumbent loss frac by k',np.round(np.nanmedian(Lp,0),2),'n',np.sum(~np.isnan(Lp),0))

# NYC (UA JFK) rows were appended to switch/a10_entry_ramp.csv separately; values from Table 6 NYC-SFO/NYC-LAX 2019-2024.
