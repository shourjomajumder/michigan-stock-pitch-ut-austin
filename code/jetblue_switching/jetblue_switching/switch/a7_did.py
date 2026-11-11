import os as _os; _D = _os.path.dirname(_os.path.abspath(__file__)); _R = _os.path.join(_D, '../../../..')  # repo root
_os.makedirs(_os.path.join(_D, 'out'), exist_ok=True)  # outputs -> out/ next to this script
import pandas as pd, numpy as np
import statsmodels.formula.api as smf
T=pd.read_csv(_os.path.join(_R, 'data/jetblue_switching/raw/dot_table6/a7_bluesky_t6.csv'))
TREAT=['BOS-LAX','BOS-SFO','BOS-CHI','BOS-HOU','BOS-DEN','NYC-LAX','NYC-LAS','NYC-RSW','NYC-TPA','NYC-PBI','NYC-MCO','MIA-SFO']
CTRL=['BOS-MCO','BOS-TPA','BOS-RSW','BOS-PBI','BOS-JAX','BOS-LAS','BOS-BUF','BOS-PIT','BOS-RDU','BOS-SYR','BOS-RIC','NYC-BUF','NYC-ROC','NYC-SYR']
def share(r,c):
    if r.carrier_lg==c: return r.large_ms*100
    if r.carrier_low==c: return r.lf_ms*100
    return np.nan
for c in ['B6','UA']: T[c]=T.apply(lambda r: share(r,c),axis=1)
T['t']=T.year*4+T.quarter-1
T['yq']=T.year.astype(str)+'Q'+T.quarter.astype(str)
T['grp']=np.where(T.pair.isin(TREAT),'T',np.where(T.pair.isin(CTRL),'C','x'))
T['region']=T.pair.str[:3]
T=T.sort_values(['pair','t'])
for c in ['B6','UA']:
    T['d'+c]=T.groupby('pair')[c].diff(4)  # rows consecutive quarters, all 17 present
T.to_csv(_os.path.join(_D, 'out', 'a7_t6_panel.csv'),index=False)
POST=['2025Q4','2026Q1']
def did(D, var, treat, ctrl):
    rows=[]
    for yq,g in D[D.year>=2023].groupby('yq'):
        t=g[g.pair.isin(treat)]['d'+var].dropna(); c=g[g.pair.isin(ctrl)]['d'+var].dropna()
        if len(t)<2 or len(c)<2: continue
        rows.append(dict(yq=yq,treat=t.mean(),ctrl=c.mean(),did=t.mean()-c.mean(),
            se=np.sqrt(t.var(ddof=1)/len(t)+c.var(ddof=1)/len(c)),nT=len(t),nC=len(c)))
    return pd.DataFrame(rows)
pd.set_option('display.width',200)
out={}
for name,tr,ct in [('all',TREAT,CTRL),('BOS',[p for p in TREAT if p.startswith('BOS')],[p for p in CTRL if p.startswith('BOS')]),
                   ('NYC',[p for p in TREAT if p.startswith('NYC')],[p for p in CTRL if p.startswith('NYC')])]:
    E=did(T,'B6',tr,ct); E['post']=E.yq.isin(POST)
    pre=E[~E.post].did
    print('==',name,'B6 YoY DiD (share pts)'); print(E.round(2).to_string(index=False))
    print(f' pre mean {pre.mean():.2f} sd {pre.std():.2f} n={len(pre)}')
    out[name]=E
# UA share YoY on treated routes (where visible)
U=T[T.pair.isin(TREAT)&(T.year>=2023)].groupby('yq').dUA.agg(['mean','std','count'])
U['se']=U['std']/np.sqrt(U['count']); print('== UA YoY on treated'); print(U.round(2))
# regression: event-study with pair FE, quarter FE, cluster by pair
D=T[(T.year>=2023)&T.grp.isin(['T','C'])].dropna(subset=['dB6']).copy()
D['tr']=(D.grp=='T').astype(int)
for q in POST: D['T_'+q[-2:]]=((D.yq==q)&(D.tr==1)).astype(int)
m=smf.ols('dB6 ~ T_Q4 + T_Q1 + tr + C(yq)',D).fit(cov_type='cluster',cov_kwds={'groups':D.pair.astype('category').cat.codes})
print(m.params[['T_Q4','T_Q1','tr']].round(2)); print(m.bse[['T_Q4','T_Q1','tr']].round(2)); print('nobs',m.nobs, D.pair.nunique())
# pooled post
D['P']=D.T_Q4+D.T_Q1
m2=smf.ols('dB6 ~ P + tr + C(yq)',D).fit(cov_type='cluster',cov_kwds={'groups':D.pair.astype('category').cat.codes})
print('pooled',m2.params['P'].round(2),m2.bse['P'].round(2))
# level version vs 4q pre avg: share in post minus same-quarter-year-ago, already = YoY. Also vs 2-year-ago (2024 same q) to check
T['d8']=T.groupby('pair').B6.diff(8)
for q in POST:
    g=T[T.yq==q]; t=g[g.grp=='T'].d8.dropna(); c=g[g.grp=='C'].d8.dropna()
    print(q,'2yr DiD',round(t.mean()-c.mean(),2),'se',round(np.sqrt(t.var()/len(t)+c.var()/len(c)),2),len(t),len(c))
pd.concat([e.assign(sample=k) for k,e in out.items()]).to_csv(_os.path.join(_D, 'out', 'a7_did_b6.csv'),index=False)
print(T[(T.yq.isin(['2025Q1','2026Q1','2024Q4','2025Q4']))&(T.grp!='x')].pivot(index='pair',columns='yq',values='B6').round(1))
