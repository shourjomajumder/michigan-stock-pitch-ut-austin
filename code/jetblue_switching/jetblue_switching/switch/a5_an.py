import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../..')  # repo root
import re, numpy as np, csv
Q=[f"{y}Q{q}" for y in range(2019,2027) for q in range(1,5)][:29]
R={}
for line in open(_os.path.join(_R, 'data/air_traffic_dot_bts/raw/dot_car_table6_cases/a5_nea_data/raw.txt')):
    a,b,tr,pax,cells=line.rstrip('\n').split('|')
    cells=cells.split(' ')
    s=[];r=[];rc=[]
    for c in cells:
        m=re.match(r'^(L?)([\d.]+)?(x\w\w)?([ud])?([\d.]+)?$',c)
        v=float(m.group(2)) if m and m.group(2) else np.nan
        s.append(v); r.append(float(m.group(5)) if m and m.group(5) else np.nan); rc.append({'u':'UA','d':'DL'}.get(m.group(4),'') if m else '')
    R[f"{a.replace('Boston','BOS')}-{b.replace('Boston','BOS')}"]=(tr,int(pax),np.array(s),np.array(r),rc,cells)
def dev(s):  # vs 2019 same quarter
    return np.array([s[i]-s[i%4] if i>=4 else np.nan for i in range(len(s))])
iS=Q.index('2021Q1'); iU=Q.index('2023Q3')
D={k:dev(v[2]) for k,v in R.items()}
print('route tr pax | pre19 | dev 2021Q1..: by year means')
for k,(tr,pax,s,r,rc,c) in R.items():
    d=D[k]
    print(f"{k:22}{tr} {pax:5} 19avg {np.nanmean(s[:4]):5.1f} | "+' '.join(f"{np.nanmean(d[i:i+4]):5.1f}" for i in range(4,29,4)))

ctl={'WAS-CLT':[74.8,75.4,74.8,76.1,75.2,77.7,75.9,73.1,73.7,74.9,72.1,71.3,77.9,75.4,75.1,73.3,72.1,73.1,72.1,69.7,67.8,63.4,67.7,67.2,71.2,66.4,65.3,73.1,73.1],
'WAS-DFW':[53.7,51.6,49.5,48.5,49.7,58.4,56.9,58.0,54.8,53.5,49.2,49.5,49.3,47.4,44.6,45.0,46.4,42.8,42.2,40.5,42.3,42.5,42.3,44.8,45.3,43.6,44.6,45.6,50.1],
'CHI-CLT':[69.5,69.0,69.2,69.5,71.4,78.7,79.6,71.0,67.3,77.7,76.7,74.2,73.3,63.1,52.8,46.1,56.2,59.1,58.5,49.4,54.2,53.8,57.3,59.9,63.0,61.2,62.8,63.1,64.1]}
C=np.nanmean([dev(np.array(v)) for v in ctl.values()],axis=0)
print('AA control dev by year', [round(np.nanmean(C[i:i+4]),1) for i in range(4,29,4)])
# exclude routes with heavy censoring: need tracked share in >=75% of 2021Q1-2026Q1
keep={k:v for k,v in R.items() if np.isfinite(v[2][8:]).mean()>=0.75}
print('kept',len(keep),'dropped',[k for k in R if k not in keep])
rows=[]
SRC="https://data.transportation.gov/resource/yj5y-b2ir.json (DOT Consumer Airfare Report Table 6)"
def agg(group, adj):
    st=[];un=[]
    for k,(tr,pax,s,r,rc,c) in keep.items():
        if tr not in group: continue
        d=D[k]-(C if adj else 0)
        st.append(d[iS:iS+10]); 
        pre=np.nanmean(d[iU-4:iU]); un.append(d[iU-4:]-pre)
    return np.array(st),np.array(un)
def timing(p,lo,hi):
    end=np.nanmean(p[lo:hi+1]); sm=np.array([np.nanmean(p[max(0,i-1):i+2]) for i in range(len(p))]); f=sm/end
    g=lambda t: next((i for i in range(len(f)) if f[i]>=t),None)
    return end, g(0.25), g(0.5), g(0.9), f
for lab,grp,adj in [('B6 routes',['B6'],False),('AA routes raw',['AA'],False),('AA routes DiD',['AA'],True)]:
    st,un=agg(grp,adj)
    ms=np.nanmean(st,0); mu=np.nanmean(un,0)
    e,f25,f50,f90,f=timing(ms,4,9)
    print(f"\n{lab} n={len(st)} START path k0..9:",np.round(ms,1)," end(k4-9)",round(e,1),"25/50/90%:",f25,f50,f90)
    print('   pos share of routes k4-9 mean>0:', (np.nanmean(st[:,4:10],1)>0).sum(),'/',len(st))
    uk=mu[4:]; e2,g25,g50,g90,f2=timing(uk,4,10)
    print(f"{lab} UNWIND path k-4..: pre=0;", np.round(mu,1), ' end(k4-10)',round(e2,1),'25/50/90%:',g25,g50,g90)
    print('   neg routes:', (np.nanmean(un[:,8:15],1)<0).sum(),'/',len(un))

print()
for k,(tr,pax,s,r,rc,c) in keep.items():
    if tr!='AA': continue
    d=D[k]-C; pre=np.nanmean(d[iU-4:iU])
    print(k, 'startDiD k4-9', round(np.nanmean(d[iS+4:iS+10]),1), 'unwind DiD path', np.round(d[iU:]-pre,1))
st,un=agg(['B6'],False); print('B6 median start k4-9',round(np.nanmedian(np.nanmean(st[:,4:10],1)),1),'median unwind k4-10',round(np.nanmedian(np.nanmean(un[:,8:15],1)),1))
st,un=agg(['AA'],True); print('AA DiD median start',round(np.nanmedian(np.nanmean(st[:,4:10],1)),1),'median unwind k4-10',round(np.nanmedian(np.nanmean(un[:,8:15],1)),1))
# write CSV
out=[]
for k,(tr,pax,s,r,rc,c) in R.items():
    d=D[k]; kept=k in keep
    for i in range(29):
        if i<4: continue
        for case,e in (('NEA start (codeshare 2021-02-25)',iS),('NEA unwind (codeshare/earning end 2023-07-21)',iU)):
            kk=i-e
            if case.startswith('NEA start') and not (-0<=kk<=9): continue
            if case.startswith('NEA unwind') and kk<-4: continue
            if case.startswith('NEA unwind'):
                pre=np.nanmean(d[iU-4:iU]); chg=d[i]-pre; base='vs 2022Q3-2023Q2 avg of (share - 2019 same-q)'
            else:
                chg=d[i]; base='vs 2019 same quarter'
            note=f"tracked={tr} (2019 largest); cell={c[i]}; {base}"
            if tr=='AA': note+=f"; AA control (WAS-CLT,WAS-DFW,CHI-CLT) dev={C[i]:.1f}"
            if not kept: note+="; EXCLUDED from averages (tracked carrier not visible >25% of quarters)"
            out.append([case,k,tr,Q[i],kk,'' if np.isnan(s[i]) else s[i],'' if np.isnan(chg) else round(chg,1),note,SRC])
with open(_os.path.join(_R, 'data/jetblue_switching/processed/switch/a5_nea.csv'),'w',newline='') as f:
    w=csv.writer(f); w.writerow(['case','route','carrier','event_quarter','k','share','change_vs_pre','note','source']); w.writerows(out)
print(len(out))
