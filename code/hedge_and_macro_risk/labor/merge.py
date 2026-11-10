import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
_O = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'out'); _os.makedirs(_O, exist_ok=True)  # intermediates
_L = _os.path.join(_R, 'data/hedge_and_macro_risk/labor')
import pandas as pd, numpy as np
from scipy import stats
import statsmodels.formula.api as smf
rows=[]
for f in ['agent1','agent2','agent3','agent4','agent5']:
    x=pd.read_csv(_os.path.join(_L, f+'.csv')); x['src']=f; rows.append(x)
n=pd.concat(rows,ignore_index=True)
for c in ['amendable','talks_start','deal','ratified']: n[c]=pd.to_datetime(n[c],errors='coerce')
g=n.group.str.lower()
n['grp']=np.where(g.str.startswith('pilot'),'pilot',np.where(g.str.contains('fa|flight'),'fa','other'))
n['flags']=n['flags'].fillna('')
excl='extension|merger|JCBA|bridge|bankrupt|arbitration|first|open|no_ratified'
n['excl']=n['flags'].str.contains(excl,case=False)|n.amendable.isna()|n.deal.isna()
n['early_regular']=n['flags'].str.contains('early_deal')&~n['flags'].str.contains('extension')
# original clean set
o=pd.read_csv(_os.path.join(_O, 'dataset_computed.csv'),parse_dates=['amendable','deal','talks_start'])
o=o[o.flag.isna()|(o.flag=='proxy_amendable')].copy()
o['grp']=o.group; o['segment']='mainline'; o['src']='orig'
n['segment']=np.where(n.src.isin(['agent1','agent2']),'regional',np.where(n.src=='agent3','cargo','mainline'))
keep=n[~n.excl | n.early_regular].copy()
keep=keep[~keep['flags'].str.contains('extension|merger|JCBA|bridge|bankrupt|arbitration|first|open|no_ratified',case=False)]
cols=['airline','grp','segment','amendable','talks_start','deal','src']
allr=pd.concat([o[cols],keep[cols]],ignore_index=True)
c0,c1=pd.Timestamp('2020-03-01'),pd.Timestamp('2022-01-01')
mo=lambda a,b:(b-a).days/30.44
allr['months']=[mo(a,b) for a,b in zip(allr.amendable,allr.deal)]
allr['covid']=[max(mo(max(a,c0),min(b,c1)),0) for a,b in zip(allr.amendable,allr.deal)]
allr['months_adj']=allr.months-allr.covid
allr['lead']=[mo(t,a) if pd.notna(t) else np.nan for t,a in zip(allr.talks_start,allr.amendable)]
allr['early']=np.where(allr.lead.isna(),np.nan,(allr.lead>=3).astype(float))
allr.to_csv(_os.path.join(_O, 'merged.csv'),index=False)
print(len(allr),'clean deals;', allr.lead.notna().sum(),'with talks-start')
print(allr.groupby(['segment','grp']).size())
def t(s,lab):
    s=s.dropna(subset=['lead','months_adj']); r,p=stats.pearsonr(s.lead,s.months_adj); rho,ps=stats.spearmanr(s.lead,s.months_adj)
    k,b=np.polyfit(s.lead,s.months_adj,1)
    print(f"{lab:40s} n={len(s):2d} r={r:+.2f} p={p:.3f} rho={rho:+.2f} p={ps:.3f} slope={k:+.2f} int={b:.1f}")
print()
t(allr,'ALL segments')
t(allr[allr.segment=='mainline'],'Mainline')
t(allr[allr.segment!='mainline'],'Regional+cargo')
t(allr[allr.grp=='pilot'],'Pilots')
t(allr[allr.grp=='fa'],'FAs')
t(allr[allr.grp=='other'],'Other groups')
t(allr[allr.months<120],'ALL excl >10yr outliers')
s=allr.dropna(subset=['early'])
print('\nEarly opener medians (ex-COVID months):'); print(s.groupby('early').months_adj.agg(['count','median','mean']).round(1))
print('MannWhitney p',round(stats.mannwhitneyu(s[s.early==1].months_adj,s[s.early==0].months_adj).pvalue,4))
m=smf.ols('months_adj ~ lead + C(grp) + C(segment)',data=s).fit(); print(m.summary().tables[1]); print('R2',round(m.rsquared,2))
print('\nDeals <=9 months after amendable:'); print(allr[allr.months_adj<=9][['airline','grp','segment','months_adj','lead']].round(1).to_string(index=False))
print('\nFA deals sorted:'); print(allr[allr.grp=='fa'][['airline','segment','months_adj','lead']].sort_values('months_adj').round(1).to_string(index=False))
