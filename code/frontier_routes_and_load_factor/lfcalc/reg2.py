import numpy as np, pandas as pd
from linearmodels.iv import IV2SLS
exec(open('reg1.py').read().split("print('LEVELS")[0])
L=d[~covid & ~spirit & ~est].copy()
L=pd.concat([L,pd.get_dummies(L.qtr,prefix='Q',drop_first=True).astype(float)],axis=1); L['const']=1
ex=['const','lASM','Q_2','Q_3','Q_4']
for p in ['lfarepp','lrevpp','lyield']:
    m=IV2SLS(L.LF,L[ex],L[[p]],L[['lFuel']]).fit(cov_type='robust')
    fs=m.first_stage.diagnostics
    print(p,'IV per+10%%: %.2f se %.2f  firststage F=%.1f'%(m.params[p]*np.log(1.1),m.std_errors[p]*np.log(1.1),fs['f.stat'].iloc[0]))
# demand-equation view: log RPM on log price, log ASM, Q FE
import statsmodels.formula.api as smf
for p in ['lrevpp','lyield','lfarepp']:
    m=smf.ols(f'np.log(RPM) ~ {p} + lASM + C(qtr)',d[~covid&~spirit&~est]).fit(cov_type='HC1')
    print('RPM on',p,'elast %.2f se %.2f'%(m.params[p],m.bse[p]))
