import json as _json, os as _os
# Consensus load factor (Bloomberg) and broker estimate are NOT distributed. Provide {"Q4-26": {"cons": x, "db": y}, "Q1-27": {...}}
_P = _json.load(open(_os.environ.get('LF_CONSENSUS_JSON', 'consensus_private.json')))
import numpy as np
L10=np.log(1.1)
dom=0.93; b_sp=8.92; b_sp_se=1.20
cap=-2.12; cap_se=0.41          # pp LF per +10% ASM (MODL levels reg, Q FE, ex-COVID)
fareIV=-0.20; fareIV_se=0.48    # pp per +10% total rev/pax (IV: fuel)
fareOLS=-1.22                   # pp per +10% fare/pax (OLS YoY) - conservative
# Spirit exposure X (ASM-weighted Spirit seat share in F9 dom mkts), BTS T-100
X={'2025Q2':0.221,'2026Q2':0.076,'2025Q3':0.200,'2026Q3':0.0,'2025Q4':0.169,'2026Q1':0.161}
def pred(base,gasm,gprice,Xb,Xt,fc=fareIV,cc=cap,bs=b_sp,gfare=None):
    s=bs*(Xb-Xt)*dom; c=cc*np.log(1+gasm)/L10
    f=fc*np.log(1+gprice)/L10 if gfare is None else fc*np.log(1+gfare)/L10
    return base+s+c+f,s,c,f
print('BACKTEST')
for q,base,act,ga,gp,xb,xt in [('Q2-26',79.3,80.3,11103/10313-1,126.93/105.66-1,X['2025Q2'],X['2026Q2']),('Q3-26',80.7,78.8,11419/9689-1,135.34/102.58-1,X['2025Q3'],0)]:
    p,s,c,f=pred(base,ga,gp,xb,xt); print(q,'pred %.1f actual %.1f | spirit %+.2f cap %+.2f fare %+.2f | resid %+.2f'%(p,act,s,c,f,act-p))
    p2,_,_,f2=pred(base,ga,gp,xb,xt,fc=fareOLS,gfare={'Q2-26':63.0/40.95-1,'Q3-26':67.82/39.64-1}[q]); print('   OLS fare/pax version pred %.1f fare %+.2f'%(p2,f2))
print('FORECAST')
cases={'Q4-26':dict(base=78.9,xb=X['2025Q4'],asm=[0.05,0.055,0.06],price=137.73/112.69-1,fare=71.29/53.06-1,cons=_P['Q4-26']['cons'],db=_P['Q4-26']['db']),
       'Q1-27':dict(base=78.4,xb=X['2026Q1'],asm=[0.05,0.06,0.07],price=140.71/114.37-1,fare=63.98/53.94-1,cons=_P['Q1-27']['cons'],db=_P['Q1-27']['db'])}
rng=np.random.default_rng(0)
for q,c in cases.items():
    p,s,cc,f=pred(c['base'],c['asm'][1],c['price'],c['xb'],0)
    print(q,'BASE %.2f = %.1f %+.2f spirit %+.2f cap %+.2f fare | cons %.2f DB %.1f'%(p,c['base'],s,cc,f,c['cons'],c['db']))
    for a in c['asm']: print('   asm %+.0f%% -> %.2f'%(a*100,pred(c['base'],a,c['price'],c['xb'],0)[0]))
    print('   conservative OLS fare/pax: %.2f'%pred(c['base'],c['asm'][1],0,c['xb'],0,fc=fareOLS,gfare=c['fare'])[0])
    print('   +2026 avg residual (+1.25): %.2f'%(p+1.25))
    N=20000; sims=(c['base']+rng.normal(b_sp,b_sp_se,N)*c['xb']*dom+rng.normal(cap,cap_se,N)*np.log(1+rng.uniform(c['asm'][0],c['asm'][2],N))/L10+rng.normal(fareIV,fareIV_se,N)*np.log(1+c['price'])/L10)
    print('   MC 10/50/90: %.2f %.2f %.2f  P(>cons)=%.0f%%'%(*np.percentile(sims,[10,50,90]),100*(sims>c['cons']).mean()))
