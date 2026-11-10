import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
_O = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'out'); _os.makedirs(_O, exist_ok=True)  # intermediates
import pandas as pd, numpy as np
from scipy import stats
import statsmodels.formula.api as smf
d = pd.read_csv(_os.path.join(_O, "dataset_computed.csv"), parse_dates=["amendable","deal","talks_start"])
s = pd.read_csv(_os.path.join(_R, "data/hedge_and_macro_risk/labor/settle.csv"), parse_dates=["ratified"])
def peers_at(r, when):
    t = r[when]
    return len(s[(s.cycle==r.cycle)&(s.airline!=r.airline)&(s.ratified<t)])
d["peers_at_amend"] = d.apply(lambda r: peers_at(r,"amendable"), axis=1)
d["start"] = d[["amendable","talks_start"]].min(axis=1)
d["peers_at_start"] = d.apply(lambda r: peers_at(r,"start"), axis=1)
A = d[d.flag.isna() | (d.flag=="proxy_amendable")].copy()
A["fa"]=(A.group=="fa").astype(int)
print(A[["id","months","months_adj","peers_at_amend","peers_at_start","early"]].round(1).to_string(index=False))
def t(sub,y,x,lab):
    sub=sub.dropna(subset=[y,x]); r,p=stats.pearsonr(sub[x],sub[y]); rho,_=stats.spearmanr(sub[x],sub[y])
    rng=np.random.default_rng(1); perm=[stats.spearmanr(rng.permutation(sub[x].values),sub[y])[0] for _ in range(5000)]
    pp=np.mean(np.abs(perm)>=abs(rho)); sl=np.polyfit(sub[x],sub[y],1)[0]
    print(f"{lab:52s} n={len(sub):2d} r={r:+.2f} (p={p:.2f}) rho={rho:+.2f} (perm p={pp:.2f}) slope={sl:+.1f} mo/peer")
print("\n=== Peers settled when the clock STARTED vs months to deal ===")
t(A,"months","peers_at_amend","Raw months, peers at amendable date")
t(A,"months_adj","peers_at_amend","COVID-adj, peers at amendable date")
t(A,"months_adj","peers_at_start","COVID-adj, peers at talks start")
t(A[A.group=="pilot"],"months_adj","peers_at_amend","Pilots, COVID-adj")
t(A[A.group=="fa"],"months_adj","peers_at_amend","FAs, COVID-adj")
m=smf.ols("months_adj ~ peers_at_amend + fa",data=A).fit()
print("\nOLS months_adj ~ peers_at_amend + fa"); print(m.summary().tables[1]); print("n",int(m.nobs),"R2",round(m.rsquared,2))
Ae=A.dropna(subset=["early"])
m2=smf.ols("months_adj ~ peers_at_amend + early + fa",data=Ae).fit()
print("\nOLS months_adj ~ peers_at_amend + early + fa"); print(m2.summary().tables[1]); print("n",int(m2.nobs),"R2",round(m2.rsquared,2))
print("\nGroup medians (COVID-adj months):")
A["late_mover"]=np.where(A.peers_at_amend>=3,"3+ peers already settled","0-2 peers settled")
print(A.groupby("late_mover").months_adj.agg(["count","median","mean","min","max"]).round(1))
d.to_csv(_os.path.join(_O, "dataset_computed.csv"),index=False)
