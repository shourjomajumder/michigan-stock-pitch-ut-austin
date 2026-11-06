import pandas as pd, numpy as np, statsmodels.formula.api as smf
from linearmodels.iv import IV2SLS
P=pd.read_pickle('P.pkl'); L10=np.log(1.1)
def show(tag,m,p,a='gASM'):
    print('%-45s price/10%%: %+.2f (se %.2f) | ASM/10%%: %+.2f (se %.2f) n=%d'%(tag,m.params[p]*L10,m.bse[p]*L10,m.params[a]*L10,m.bse[a]*L10,m.nobs))
for excl26 in [True,False]:
  Y=P[(~P.bad)&(P.bad4==False)].dropna(subset=['dLF'])
  if excl26: Y=Y[~((Y.firm=='ALGT')&(Y.q>='2026Q2'))]
  print('--- YoY panel', 'excl ALGT Q2-26' if excl26 else 'incl ALGT Q2-26', 'quarters', sorted(Y.q.unique())[0],'..',sorted(Y.q.unique())[-1])
  for p in ['grevpp','gfarepp','gyield']:
    show('OLS dLF~'+p+'+gASM+firm',smf.ols(f'dLF~{p}+gASM+C(firm)',Y).fit(cov_type='HC1'),p)
    show('OLS dLF~'+p+'+gASM+gFuel+firm',smf.ols(f'dLF~{p}+gASM+gFuel+C(firm)',Y).fit(cov_type='HC1'),p)
    Y2=Y.assign(fA=(Y.firm=='ALGT').astype(float),const=1.0)
    m=IV2SLS(Y2.dLF,Y2[['const','fA','gASM']],Y2[[p]],Y2[['gFuel']]).fit(cov_type='robust')
    print('%-45s price/10%%: %+.2f (se %.2f) | ASM/10%%: %+.2f (se %.2f) firstF=%.1f'%('IV(fuel) '+p,m.params[p]*L10,m.std_errors[p]*L10,m.params['gASM']*L10,m.std_errors['gASM']*L10,m.first_stage.diagnostics['f.stat'].iloc[0]))
# levels panel
Lv=P[~P.bad]; Lv=Lv[~((Lv.firm=='ALGT')&(Lv.q>='2026Q2'))]
print('--- LEVELS panel n=',len(Lv))
for p in ['lrevpp','lfarepp','lyield']:
    m=smf.ols(f'LF~{p}+lASM+lFuel+C(firm):C(qtr)+C(firm):yr',Lv).fit(cov_type='HC1')
    print('%-45s price/10%%: %+.2f (se %.2f) | ASM/10%%: %+.2f (se %.2f)'%('OLS '+p,m.params[p]*L10,m.bse[p]*L10,m.params['lASM']*L10,m.bse['lASM']*L10))
    X=pd.get_dummies(Lv.firm+Lv.qtr,drop_first=False).astype(float)
    X['trA']=(Lv.firm=='ALGT')*Lv.yr; X['trU']=(Lv.firm=='ULCC')*Lv.yr; X['lASM']=Lv.lASM
    m=IV2SLS(Lv.LF,X,Lv[[p]],Lv[['lFuel']]).fit(cov_type='robust')
    print('%-45s price/10%%: %+.2f (se %.2f) | ASM/10%%: %+.2f (se %.2f) firstF=%.1f'%('IV '+p,m.params[p]*L10,m.std_errors[p]*L10,m.params['lASM']*L10,m.std_errors['lASM']*L10,m.first_stage.diagnostics['f.stat'].iloc[0]))
