import json as _json, os as _os
# Consensus load factor (Bloomberg) and broker estimate are NOT distributed. Provide {"Q4-26": {"cons": x, "db": y}, "Q1-27": {...}}
_P = _json.load(open(_os.environ.get('LF_CONSENSUS_JSON', 'consensus_private.json')))
import numpy as np
L10=np.log(1.1); dom=0.93; rng=np.random.default_rng(1); N=50000
bs,bse=8.92,1.20; cap,capse=-2.12,0.5; fare,farese=0.0,0.8
for q,base,X,asm,price,cons in [('Q4-26',78.9,0.169,(0.05,0.06),137.73/112.69-1,_P['Q4-26']['cons']),('Q1-27',78.4,0.161,(0.05,0.07),140.71/114.37-1,_P['Q1-27']['cons'])]:
    a=np.mean(asm); s=bs*X*dom; c=cap*np.log(1+a)/L10; f=fare*np.log(1+price)/L10
    sims=base+rng.normal(bs,bse,N)*X*dom+rng.normal(cap,capse,N)*np.log(1+rng.uniform(*asm,N))/L10+rng.normal(fare,farese,N)*np.log(1+price)/L10
    bear=base+s+c+(-1.22)*np.log(1+price)/L10
    print(q,'base %.1f spirit %+.1f cap %+.1f fare %+.1f => %.1f | 80%% range %.1f-%.1f | cons %.2f | P(>cons) %.0f%% | bear(fare -1.2/10%%) %.1f'%(base,s,c,f,base+s+c+f,*np.percentile(sims,[10,90]),cons,100*(sims>cons).mean(),bear))
for q,base,act,ga,gp,xb,xt in [('Q2-26',79.3,80.3,11103/10313-1,126.93/105.66-1,0.221,0.076),('Q3-26',80.7,78.8,11419/9689-1,135.34/102.58-1,0.200,0)]:
    p=base+bs*(xb-xt)*dom+cap*np.log(1+ga)/L10; print('backtest',q,'pred %.1f actual %.1f'%(p,act))
