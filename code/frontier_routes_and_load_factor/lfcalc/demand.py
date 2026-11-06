exec(open('sncy.py').read().split("L10=np.log(1.1)")[0])
import scipy.stats as st
P=P.sort_values(['firm','q']).reset_index(drop=True)
P['lRPM']=np.log(P.RPM)
if 'Pax' not in P: P['Pax']=np.nan
# pax for ULCC from data.py, ALGT from algt rows
exec(open('data.py').read()); pu=dict(zip(d.q,d.Pax))
import re
arows=open('algt.py').read().split('rows="""')[1].split('"""')[0].split('\n'); pa={r.split()[0]:float(r.split()[6]) for r in arows}
P.loc[P.firm=='ULCC','Pax']=P.loc[P.firm=='ULCC','q'].map(pu); P.loc[P.firm=='ALGT','Pax']=P.loc[P.firm=='ALGT','q'].map(pa)
P['lPax']=np.log(P.Pax.astype(float))
for c in ['lRPM','lPax','lrevpp','lyield','lASM']: P['g'+c[1:]]=P.groupby('firm')[c].diff(4)
P['base']=P.groupby('firm')['q'].shift(4)
ev=lambda q: (q>='2020Q1')&(q<='2022Q1')
# exclusions: COVID either end; Spirit liquidation/shrink era Q4'25+ (Spirit cut 28% of seats Q3->Q4'25, ceased May'26); ALGT/SNCY merger 2026
P['clean']=~(P.q.apply(ev)|P.base.fillna('').apply(ev)|(P.q>='2025Q4'))
DD=P[P.clean].dropna(subset=['gRPM','gyield','gASM']).copy()
print('clean obs',DD.firm.value_counts().to_dict(),'quarters',DD.q.min(),DD.q.max())
for c in ['gRPM','gPax','grevpp','gyield','gASM']: DD[c.replace('g','p',1)]=100*(np.exp(DD[c])-1)
# capacity-adjusted demand = traffic growth minus seat growth (log) = growth in LF
DD['xsd']=100*(DD.gRPM-DD.gASM)
def corr(x,y,lab):
    m=pd.concat([x,y],axis=1).dropna(); r,p=st.pearsonr(m.iloc[:,0],m.iloc[:,1]); rs,ps=st.spearmanr(m.iloc[:,0],m.iloc[:,1]); n=len(m)
    z=np.arctanh(r); lo,hi=np.tanh(z-1.96/np.sqrt(n-3)),np.tanh(z+1.96/np.sqrt(n-3))
    print('%-55s n=%2d r=%+.2f [95%% CI %+.2f,%+.2f] p=%.2f  R2=%.2f | spearman %+.2f p=%.2f'%(lab,n,r,lo,hi,p,r*r,rs,ps))
    return r,p,lo,hi,n
corr(DD.pyield,DD.pRPM,'Yield growth vs RPM growth (all 3)')
corr(DD.prevpp,DD.pPax,'Rev/pax growth vs passenger growth (ULCC+ALGT)')
corr(DD.pyield,DD.xsd,'Yield growth vs traffic-minus-seat growth (all 3)')
corr(DD.prevpp,DD.xsd,'Rev/pax growth vs traffic-minus-seat growth')
# partial corr controlling capacity
import statsmodels.formula.api as smf
for y in ['pRPM','pPax']:
    for x in ['pyield','prevpp']:
        D=DD.dropna(subset=[x,y]); ry=smf.ols(f'{y}~pASM+C(firm)',D).fit().resid; rx=smf.ols(f'{x}~pASM+C(firm)',D).fit().resid
        corr(rx,ry,f'PARTIAL {x} vs {y} | ASM, airline')
for f in ['ULCC','ALGT','SNCY']:
    D=DD[DD.firm==f]; corr(D.pyield,D.xsd,f'{f}: yield vs traffic-minus-seats')
DD.to_pickle('DD.pkl')
print(DD[['firm','q','pyield','prevpp','pRPM','pPax','pASM','xsd']].round(1).to_string())
