import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../..')  # repo root
_O = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'out'); _os.makedirs(_O, exist_ok=True)  # outputs
import pandas as pd, numpy as np
H=1.163
p=pd.read_csv(__import__('os').environ.get('PAIR_DAILY',_os.path.join(_R, 'data/hedge_and_macro_risk/macro/work/pair_daily.csv')),parse_dates=['Date']).set_index('Date'); p.columns=['U','J']
r=p.pct_change().dropna(); r['P']=r.U-H*r.J
w=r.loc['2025-11-04':'2026-10-27']; sd=w.std()*np.sqrt(252)
sU,sJ,sP=sd.U,sd.J,sd.P
# leg correlations from prior factor work (nonoil/c.py), same window; pair corr re-derived with sign
F={ # name: (corrU, corrJ, factor ann vol, vol source)
 'SPY':(0.422,0.451,0.130,'60d rolling avg, nonoil/volroll.txt'),
 'JETS':(0.770,0.757,0.336,'60d rolling avg, nonoil/volroll.txt'),
 'XLY':(0.424,0.468,0.20,'ASSUMED'),
 'IWM':(0.501,0.521,0.22,'ASSUMED'),
 'HYG':(0.411,0.489,0.065,'ASSUMED'),
 'UST10Y_bp':(-0.278,-0.269,95.0,'ASSUMED (bp/yr, ~6bp/day)')}
rows=[]
for k,(ru,rj,sf,src) in F.items():
    bU=ru*sU/sf; bJ=rj*sJ/sf; bP=bU-H*bJ; rp=(ru*sU-H*rj*sJ)/sP
    rows.append(dict(factor=k,corr_ULCC=ru,corr_JBLU=rj,corr_pair=round(rp,3),beta_ULCC=bU,beta_JBLU=bJ,beta_pair=bP,
        resid_vol_pair_ann=sP*np.sqrt(1-rp**2),factor_vol=sf,factor_vol_source=src))
B=pd.DataFrame(rows).set_index('factor'); B.round(4).to_csv(_os.path.join(_O, 'factor_betas.csv'))
print(B.round(3).drop(columns='factor_vol_source').to_string())
S=[('Recession / equity bear: S&P 500 -20% over 3 mo','SPY',-0.20,63),
   ('Equity correction: S&P 500 -10% over 1 mo','SPY',-0.10,21),
   ('Consumer spending shock: XLY -15% over 2 mo','XLY',-0.15,42),
   ('Credit stress: HYG -5% over 1 mo (~+150-200bp HY spread, est.)','HYG',-0.05,21),
   ('Small-cap risk-off: Russell 2000 -15% over 1 mo','IWM',-0.15,21),
   ('Rates shock: 10y +100bp over 3 mo','UST10Y_bp',100,63),
   ('Airline-sector shock ex-fuel (ATC/shutdown/demand): JETS -20% over 1 mo','JETS',-0.20,21),
   ('Soft landing / risk-on: S&P 500 +10% over 3 mo','SPY',0.10,63)]
out=[]
for name,f,sh,h in S:
    b=B.loc[f]; u=b.beta_ULCC*sh; j=b.beta_JBLU*sh; pr=b.beta_pair*sh
    rs=b.resid_vol_pair_ann*np.sqrt(h/252)
    out.append(dict(scenario=name,factor=f,shock=sh,horizon_days=h,ULCC_leg_ret=u,JBLU_leg_ret=j,
       pair_pnl_per_1_long=pr,minus_1sd=pr-rs,plus_1sd=pr+rs,resid_1sd=rs))
O=pd.DataFrame(out); O.round(4).to_csv(_os.path.join(_O, 'pair_macro_scenarios.csv'),index=False)
pd.set_option('display.width',250); print(O.drop(columns='scenario').round(3).to_string()); print([o['scenario'][:30] for o in out])
# in-sample stress windows (buy and hold, $1 long ULCC / $1.163 short JBLU at start)
Wn=[('Feb-Mar 2026 airline drawdown (Middle East conflict; includes oil)','2026-02-06','2026-03-20'),
    ('May 2026 Spirit shutdown month','2026-04-30','2026-05-29'),
    ('Oct 2026 JetBlue liquidity/credit scare','2026-10-02','2026-10-23'),
    ('Post-3Q relief (Oct 23 - Nov 2, 2026)','2026-10-23','2026-11-02')]
ev=[]
for n,a,b in Wn:
    pa=p.loc[:a].iloc[-1]; pb=p.loc[:b].iloc[-1]; ru=pb.U/pa.U-1; rj=pb.J/pa.J-1
    ev.append(dict(window=n,start=a,end=b,ULCC=ru,JBLU=rj,pair_pnl_per_1_long=ru-H*rj))
E=pd.DataFrame(ev); E.round(4).to_csv(_os.path.join(_O, 'pair_stress_windows.csv'),index=False); print(E.round(3).to_string())
# worst / best rolling 21d pair (buy-hold)
R21=(p.U.pct_change(21)-H*p.J.pct_change(21)).dropna()
print('21d pair: worst',R21.min().round(3),R21.idxmin().date(),'best',R21.max().round(3),R21.idxmax().date(),'5th pct',R21.quantile(.05).round(3),'95th',R21.quantile(.95).round(3))
print('pair ann vol',round(sP,3),'monthly 1sd',round(sP*np.sqrt(21/252),3))
