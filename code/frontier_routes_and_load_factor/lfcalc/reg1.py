import numpy as np, statsmodels.formula.api as smf
exec(open('data.py').read())
d['qtr']=d.q.str[5]; d['t']=range(len(d))
for c in ['ASM','farepp','revpp','yield','Fuel','stage','RPM','Pax']: d['l'+c]=np.log(d[c])
# YoY diffs
for c in ['LF']: d['d'+c]=d[c]-d[c].shift(4)
for c in ['lASM','lfarepp','lrevpp','lyield','lFuel','lstage']: d['g'+c[1:]]=(d[c]-d[c].shift(4))*100
covid=d.q.isin(['2020Q1','2020Q2','2020Q3','2020Q4','2021Q1','2021Q2','2021Q3','2021Q4','2022Q1'])
spirit=d.q.isin(['2026Q2','2026Q3'])
est=d.q.str.endswith('E')
# levels sample: 2019 + 2022Q2..2026Q1
L=d[~covid & ~spirit & ~est]
print('LEVELS n=',len(L))
for p in ['lfarepp','lrevpp','lyield']:
    m=smf.ols(f'LF ~ {p} + lASM + lFuel + C(qtr)',L).fit(cov_type='HC1')
    print(p, 'coef(pp per +10%%)=%.2f se=%.2f | ASM coef per+10%%=%.2f se=%.2f  R2=%.2f'%(m.params[p]*np.log(1.1),m.bse[p]*np.log(1.1),m.params['lASM']*np.log(1.1),m.bse['lASM']*np.log(1.1),m.rsquared))
# YoY sample: both quarters non-covid: 2023Q2.. (base 2022Q2+) to 2026Q1
Y=d[(d.index>=17)&(d.index<=28)]
Y2=d[((d.index>=17)&(d.index<=28))|(d.index.isin([13,14,15,16]))]  # 2022Q2-Q4/2023Q1 vs covid-ish base? exclude
print('YOY n=',len(Y), Y.q.iloc[0], Y.q.iloc[-1])
for p in ['gfarepp','grevpp','gyield']:
    for f in [f'dLF ~ {p} + gASM', f'dLF ~ {p} + gASM + gFuel']:
        m=smf.ols(f,Y).fit(cov_type='HC1')
        print(f,' price per+10%%=%.2f se=%.2f  ASM per+10%%=%.2f se=%.2f R2=%.2f'%(m.params[p]*10,m.bse[p]*10,m.params['gASM']*10,m.bse['gASM']*10,m.rsquared))
print(d[['q','dLF','gfarepp','grevpp','gyield','gASM','gFuel']].iloc[16:].round(1).to_string())
