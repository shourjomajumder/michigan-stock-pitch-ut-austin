import pandas as pd, numpy as np, statsmodels.formula.api as smf
from linearmodels.iv import IV2SLS
rows="""2022Q2 1126.03 1632.50 83.80 195.36 4.39
2022Q3 1101.01 1553.48 87.60 195.36 3.93
2022Q4 1141.49 1645.66 84.40 199.68 3.58
2023Q1 1432.13 1625.73 88.10 267.27 3.45
2023Q2 1216.26 1417.78 85.80 227.87 2.71
2023Q3 1252.58 1791.49 86.60 214.36 3.19
2023Q4 1316.88 1554.04 84.74 210.63 3.07
2024Q1 1654.85 2211.89 87.40 274.66 3.01
2024Q2 1392.31 2011.92 83.10 216.40 2.86
2024Q3 1288.46 1884.89 84.20 207.76 2.69
2024Q4 1312.73 1963.25 81.60 215.26 2.47
2025Q1 1686.48 2370.76 83.50 285.89 2.66
2025Q2 1285.93 1933.87 81.80 214.67 2.43
2025Q3 1165.18 1770.57 84.80 201.10 2.55
2025Q4 1224.94 1450.56 84.40 221.48 2.56
2026Q1 1501.17 2112.94 85.50 285.26 nan"""
s=pd.DataFrame([r.split() for r in rows.split('\n')],columns='q RPM ASMtot LF PaxRev Fuel'.split())
for c in s.columns[1:]: s[c]=s[c].astype(float)
s['ASM']=s.RPM/(s.LF/100); s['yield']=s.PaxRev/s.RPM*100; s['firm']='SNCY'
P=pd.read_pickle('P.pkl')
s['qtr']=s.q.str[5]; s['yr']=s.q.str[:4].astype(int)
for c in ['ASM','yield','Fuel']: s['l'+c]=np.log(s[c])
for c in ['lASM','lyield','lFuel']: s['g'+c[1:]]=s[c].diff(4)
s['dLF']=s.LF.diff(4); s['bad']=False; s['bad4']=pd.Series([np.nan]*4+[False]*(len(s)-4),dtype=object)
P=pd.concat([P,s],ignore_index=True)
L10=np.log(1.1)
Y=P[(~P.bad)&(P.bad4==False)].dropna(subset=['dLF','gyield','gASM'])
Y=Y[~((Y.firm=='ALGT')&(Y.q>='2026Q2'))]
print('obs by firm',Y.firm.value_counts().to_dict())
for f in ['dLF~gyield+gASM+C(firm)','dLF~gyield+gASM+gFuel+C(firm)']:
    m=smf.ols(f,Y.dropna(subset=['gFuel']) if 'Fuel' in f else Y).fit(cov_type='HC1')
    print('%-38s yield/10%%: %+.2f (se %.2f) ASM/10%%: %+.2f (se %.2f) n=%d'%(f,m.params['gyield']*L10,m.bse['gyield']*L10,m.params['gASM']*L10,m.bse['gASM']*L10,m.nobs))
Y2=Y.dropna(subset=['gFuel']).copy(); Y2['const']=1.0
for f in ['ALGT','SNCY']: Y2['f'+f]=(Y2.firm==f).astype(float)
m=IV2SLS(Y2.dLF,Y2[['const','fALGT','fSNCY','gASM']],Y2[['gyield']],Y2[['gFuel']]).fit(cov_type='robust')
print('IV(fuel) yield/10%%: %+.2f (se %.2f) ASM/10%%: %+.2f (se %.2f) firstF=%.1f'%(m.params['gyield']*L10,m.std_errors['gyield']*L10,m.params['gASM']*L10,m.std_errors['gASM']*L10,m.first_stage.diagnostics['f.stat'].iloc[0]))
# SNCY alone
S=Y[Y.firm=='SNCY']; m=smf.ols('dLF~gyield+gASM',S).fit(cov_type='HC1'); print('SNCY alone yield/10%%: %+.2f (se %.2f) n=%d'%(m.params['gyield']*L10,m.bse['gyield']*L10,m.nobs))
# by-firm slopes
for f in ['ULCC','ALGT','SNCY']:
    S=Y[Y.firm==f]; m=smf.ols('dLF~gyield+gASM',S).fit(); print(f,'yield/10%%: %+.2f (se %.2f) n=%d'%(m.params['gyield']*L10,m.bse['gyield']*L10,m.nobs))
