import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../..')  # repo root
import numpy as np, csv
# Table 6 values seen via SODA (yj5y-b2ir). Each route: carrier tracked, start (year,q), comma series (blank=carrier not shown; ub=upper bound note)
SRC="https://data.transportation.gov/resource/yj5y-b2ir.json?$where=city1 like '{a}%' AND city2 like '{b}%'"
def S(s): return [np.nan if v=='' else float(v) for v in s.split(',')]
# 1996Q1..2005Q4 (40 q) for CO-NW routes
R = {
 # route: (case, carrier, series, c1,c2, note)
 'Cleveland-Detroit':('CO-NW','NW',S(".8,.77,.76,.78,.79,.78,.77,.69,.79,.72,.65,.77,.79,.73,.71,.77,.77,.8,.77,.71,.69,.69,.68,.78,.74,.79,.78,.85,.83,.87,.86,.88,.83,.83,.82,.83,.83,.93,.92,.92"),'Clev','Detr','NW always largest; CO 0.18-0.20 pre, 0.19-0.27 in 1999 when shown'),
 'Cleveland-Minneapolis':('CO-NW','NW',S(".73,.73,.7,.7,.7,.67,.7,.69,.68,.62,.49,.62,.61,.58,.54,.54,.54,.53,.54,.59,.57,.6,.53,.57,.57,.6,.58,.6,.61,.59,.61,.59,.64,.61,.56,.6,.57,.54,.52,.44"),'Clev','Minn','CO 0.16-0.19 pre (1996-98Q1), 0.27-0.32 in 1999 when shown'),
 'Detroit-New York':('CO-NW','NW',S(".68,.69,.68,.71,.69,.69,.68,.68,.63,.58,.48,.63,.65,.66,.64,.68,.71,.71,.66,.72,.68,.64,.58,.56,.52,.52,.56,.65,.71,.66,.64,.65,.65,.64,.61,.61,.62,.61,.57,.59"),'Detr','New York','NYC metro incl. EWR; P9/NK low-fare entry 1998Q3, 2001Q3+'),
 'Minneapolis-New York':('CO-NW','NW',S(".72,.72,.71,.73,.75,.71,.67,.7,.71,.64,.5,.71,.68,.67,.58,.65,.63,.63,.57,.61,.63,.62,.59,.68,.61,.61,.59,.62,.61,.58,.53,.57,.56,.55,.52,.59,.63,.56,.54,.57"),'Minn','New York','CO 0.10-0.12 pre, 0.15-0.17 1998Q2-1999Q2; Sun Country (SY) entry 1999Q3'),
 'Cleveland-Memphis':('CO-NW','NW',S(".58,.62,.67,.64,.66,.71,.68,.58,.47,.5,.46,.52,.55,.43,.37,.41,.33,,,,,.24,.3,,,.24,.22,.14,,,,,,.18,,.32,,,,"),'Clev','Memp','DL low-fare 0.34 in 1998Q1; CO largest from 2000Q2 (0.47-0.55): likely CO capacity entry; NW blank = below CO and not lowest-fare'),
 'Detroit-Houston':('CO-NW','CO',S(".47,.47,.47,.38,.44,.46,.48,.44,.45,.48,.53,.5,.43,.43,.45,.42,,,.44,.41,.42,.45,.44,.45,.44,.46,.44,.48,.43,.45,.51,.5,.38,.39,.45,.42,.4,.45,.46,.56"),'Detr','Hous','CO loser here; NW low-fare 0.33-0.36 Q1 pre, 0.39-0.41 in 1999, largest 0.46/0.42 in 2000H1'),
 'Houston-Memphis':('CO-NW','NW',S(".71,.77,.57,.54,.5,.49,.5,.43,.44,.43,.32,.41,.4,.38,,.36,.35,.36,,.39,.38,.42,.37,.34,.29,.33,.4,.41,.43,.37,.37,.41,.36,.33,,,.39,.37,.35,.14"),'Hous','Memp','NW share falling since 1996 (pretrend); CO largest from 1998Q3 at 0.40-0.50'),
 'Houston-Minneapolis':('CO-NW','CO',S(",.41,.48,.41,.36,.43,.42,.39,.37,.41,.53,.42,,,,,,,.27,.32,,,.33,,,,,,,,.37,.36,,,,,,,.47,.42"),'Hous','Minn','Sun Country (SY) entry 1999Q3 hits both partners; NW largest 1999Q1-2000Q2 at 0.30-0.41'),
}
# 2003 DL-CO-NW: 2001Q1..2005Q4 (20 q)
R3 = {
 'Cincinnati-Houston':('DL-CO-NW','DL',S(".53,.23,.35,.49,.59,.56,.53,.53,.56,.52,.49,.51,.54,.5,.52,.48,.52,.49,.45,.37"),'Cinc','Hous','CO low-fare 0.32-0.42 2002Q4-2004Q4; DL Ch.11 Sep 2005'),
 'Atlanta-Minneapolis':('DL-CO-NW','NW',S(".57,.55,.56,.52,.55,.45,,.42,.5,.45,,.42,.47,.43,,.39,.43,,,"),'Atl','Minn','AirTran (FL) low-fare share 0.10-0.20 rising; blank = DL largest'),
 'Atlanta-Detroit':('DL-CO-NW','NW',S(".54,.5,,,.46,,,.48,.53,.54,.47,.51,.51,.52,.45,.55,.54,.47,.44,.44"),'Atl','Det','duplicate NK rows (0.88-0.99) in feed ignored'),
 'Atlanta-Houston':('DL-CO-NW','DL',S(".46,.43,.45,.49,.5,.53,.54,.51,.5,.49,.52,.52,.5,.49,.49,.45,.46,.4,.38,.39"),'Atl','Hous','CO never shown; AirTran (FL) 0.13-0.24 rising'),
}
def lab(y0,i): return f"{y0+i//4}Q{i%4+1}"
rows=[]; summ=[]
def run(name,case,car,v,y0,e,pre_idx,a,b,note,evq):
    v=np.array(v); pre=np.nanmean(v[pre_idx])
    ks=range(-8,17)
    ch={}
    for k in ks:
        i=e+k
        if i<0 or i>=len(v): continue
        q=lab(y0,i); s=v[i]; c=round((s-pre)*100,1) if not np.isnan(s) else ''
        ch[k]=np.nan if c=='' else c
        fl=[]
        if q=='1998Q3': fl.append('NW pilot strike Aug29-Sep12 1998')
        if q in('2001Q3','2001Q4','2002Q1'): fl.append('9/11 demand shock')
        if q in('1998Q1','1998Q2','1998Q3') and case=='CO-NW': fl.append('post-announcement pre-implementation')
        if q=='2003Q2' and case=='DL-CO-NW': fl.append('benefits from Jun 18 2003 only')
        rows.append([case,name,car,evq,k,'' if np.isnan(s) else s,c,'; '.join(fl+([note] if k==0 else [])),SRC.format(a=a,b=b)+' (1995 not in feed)'])
    return pre,ch
for n,(case,car,v,a,b,note) in R.items():
    # 1996Q1 index0; event 1998Q4 = idx 11; pre = 1997Q1-Q4 (idx4-7) avoids announcement (Jan98) and strike
    pre,ch=run(n,case,car,v,1996,11,slice(4,8),a,b,note,'1998Q4')
    summ.append((n,car,pre,ch))
for n,(case,car,v,a,b,note) in R3.items():
    # 2001Q1 idx0; event 2003Q2 idx 9; pre 2002Q2-2003Q1 idx5-8
    pre,ch=run(n,case,car,v,2001,9,slice(5,9),a,b,note,'2003Q2')
    summ.append((n,car,pre,ch))
with open(_os.path.join(_R, 'data/jetblue_switching/processed/switch/a2_co_nw.csv'),'w',newline='') as f:
    w=csv.writer(f); w.writerow(['case','route','carrier','event_quarter','k','share','change_vs_pre','note','source']); w.writerows(rows)
for n,car,pre,ch in summ:
    print(f"{n:22}{car} pre {pre*100:5.1f} | "+' '.join(f"{k}:{ch[k]:+.0f}" if not np.isnan(ch[k]) else f"{k}:." for k in sorted(ch) if -4<=k<=14))
