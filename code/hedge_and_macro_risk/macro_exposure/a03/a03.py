import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../..')  # repo root
_O = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'out'); _os.makedirs(_O, exist_ok=True)  # outputs
import pandas as pd, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
H=1.163; SRC=_os.path.join(_R, 'data/hedge_and_macro_risk/macro/work/pair_daily.csv')
p=pd.read_csv(SRC,parse_dates=['Date']).set_index('Date'); p.columns=['U','J']
r=p.pct_change().dropna(); r['P']=r.U-H*r.J
out=pd.DataFrame(index=r.index)
for w in (60,120):
    c=r.U.rolling(w).cov(r.J); v=r.J.rolling(w).var()
    out[f'beta{w}']=c/v; out[f'corr{w}']=r.U.rolling(w).corr(r.J)
    out[f'pairvol{w}_ann']=r.P.rolling(w).std()*np.sqrt(252)
out['pair_ret']=r.P; out['pair_cum']=(1+r.P).cumprod()  # daily-rebalanced $1/$1.163
out.round(5).to_csv(_os.path.join(_O, 'rolling_series.csv'))
print('N returns',len(r),r.index[0].date(),r.index[-1].date())
for w in (60,120):
    b=out[f'beta{w}'].dropna(); d=b-H
    print(f'beta{w}: last {b.iloc[-1]:.3f} mean {b.mean():.3f} min {b.min():.3f} ({b.idxmin().date()}) max {b.max():.3f} ({b.idxmax().date()}) mean|dev| {d.abs().mean():.3f} maxdev {d.abs().max():.3f} %days|dev|>0.2 {(d.abs()>0.2).mean()*100:.0f}%')
    cc=out[f'corr{w}'].dropna(); pv=out[f'pairvol{w}_ann'].dropna()
    print(f'corr{w}: last {cc.iloc[-1]:.3f} mean {cc.mean():.3f} min {cc.min():.3f} max {cc.max():.3f} | pairvol{w}: last {pv.iloc[-1]:.3f} mean {pv.mean():.3f} min {pv.min():.3f} max {pv.max():.3f}')
print('legs ann vol U %.3f J %.3f, full corr %.3f'%(r.U.std()*252**.5,r.J.std()*252**.5,r.U.corr(r.J)))
def vares(x,a):
    q=np.quantile(x,1-a); return -q,-x[x<=q].mean()
P=r.P.values; P21=(np.log1p(r.U)-H*np.log1p(r.J)).rolling(21).sum().dropna()  # placeholder
# 21d: overlapping 21-day sums of daily pair P&L (per $1 long notional, static hedge)
P21=r.P.rolling(21).sum().dropna().values
for a in (.95,.99):
    v1,e1=vares(P,a); v21,e21=vares(P21,a)
    print(f'{a:.0%}: 1d VaR {v1:.4f} ES {e1:.4f} | 21d VaR {v21:.4f} ES {e21:.4f} | sqrt21 VaR {v1*21**.5:.4f}')
print('N 21d overlapping windows',len(P21))
cum=np.cumsum(P); eq=1+cum; dd=eq/np.maximum.accumulate(np.r_[1,eq])[1:]-1  # static notional P&L
peak=np.maximum.accumulate(np.r_[0,cum])[1:]; ddabs=cum-peak
i=ddabs.argmin(); j=np.argmax(cum[:i+1]) if i>0 else 0
print(f'MaxDD (static, per $1 long): {ddabs.min():.4f} peak {r.index[j].date()} trough {r.index[i].date()}')
cp=out.pair_cum.values; ddr=cp/np.maximum.accumulate(cp)-1; print(f'MaxDD (daily-rebal compounding): {ddr.min():.4f} trough {r.index[ddr.argmin()].date()}')
bmv=r.U.cov(r.J)/r.J.var(); vU=r.U.var()
for h,n in ((H,'1.163'),(bmv,'minvar')):
    rv=(r.U-h*r.J).var(); print(f'h={h:.3f} ({n}): pair var {rv:.6f} ann vol {np.sqrt(rv*252):.3f} resid/ULCC var {rv/vU:.3f} var reduction {1-rv/vU:.1%}')
print('extra var at 1.163 vs minvar: %.2f%%'%(((r.U-H*r.J).var()/(r.U-bmv*r.J).var()-1)*100))
fig,ax=plt.subplots(figsize=(9,4.5)); plt.rcParams['font.family']='serif'
for a_ in [ax]: pass
ax.plot(out.index,out.beta60,color='#0B2265',lw=2,label='60-day OLS beta')
ax.plot(out.index,out.beta120,color='#0B2265',lw=2,alpha=.45,label='120-day OLS beta')
ax.axhline(H,color='#0B2265',ls='--',lw=1.2); ax.text(out.beta60.first_valid_index(),H+0.012,'1.163 trade hedge',color='#333',fontfamily='serif',fontsize=9)
ax.set_title('Rolling hedge ratio: ULCC daily returns on JBLU',fontfamily='serif',loc='left')
ax.set_ylabel('Beta (ULCC on JBLU)',fontfamily='serif'); ax.legend(frameon=False,prop={'family':'serif'})
for s in ('top','right'): ax.spines[s].set_visible(False)
ax.grid(axis='y',color='#ddd',lw=.6); [t.set_fontfamily('serif') for t in ax.get_xticklabels()+ax.get_yticklabels()]
fig.text(0.01,0.01,'Source: pair_daily.csv daily closes, simple returns',fontsize=7,fontfamily='serif',color='#666')
fig.tight_layout(); fig.savefig(_os.path.join(_O, 'rolling_hedge_ratio.png'),dpi=200)
