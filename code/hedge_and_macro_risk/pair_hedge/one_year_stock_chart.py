import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, matplotlib.dates as md
plt.rcParams.update({'font.family':'serif','font.serif':['EB Garamond','Garamond','TeX Gyre Pagella','DejaVu Serif']})
d=pd.read_csv(_os.path.join(_R, 'data/hedge_and_macro_risk/raw/yahoo/yahoo_1yr_closes_JBLU_ULCC_JETS_SPY.csv'),parse_dates=['Date'],index_col='Date')
x=d/d.iloc[0]*100
N='#0B2265'
fig,ax=plt.subplots(figsize=(6.3,2.75),dpi=250)
ax.plot(x.index,x.ULCC,color='#9A9A9A',lw=1.4,label='Frontier (ULCC)')
ax.plot(x.index,x.JETS,color='#BFBFBF',lw=1.3,ls='--',label='Airline sector (JETS)')
ax.plot(x.index,x.JBLU,color=N,lw=2.2,label='JetBlue (JBLU)')
ax.axhline(100,color='#888',lw=0.7)
for s,c,dy in [('ULCC','#6E6E6E',0),('JETS','#8C8C8C',0),('JBLU',N,0)]:
    v=x[s].iloc[-1]; ax.text(x.index[-1]+pd.Timedelta(days=4),v+dy,f'{v-100:+.0f}%'.replace('-','−'),color=c,fontsize=9,weight='bold',va='center')
pk=d.JBLU.idxmax(); lo=d.JBLU.idxmin()
ax.annotate(f'Peak ${d.JBLU.max():.2f}',(pk,x.JBLU[pk]),xytext=(pk-pd.Timedelta(days=45),x.JBLU[pk]+28),fontsize=7.5,color=N,arrowprops=dict(arrowstyle='-',color=N,lw=0.6))
ax.annotate(f'Low ${d.JBLU.min():.2f} (−63% from peak)',(lo,x.JBLU[lo]),xytext=(lo-pd.Timedelta(days=150),x.JBLU[lo]-8),fontsize=7.5,color=N,arrowprops=dict(arrowstyle='-',color=N,lw=0.6),va='center')
for dt,t in [('2026-05-02','Spirit shuts down')]:
    ax.axvline(pd.Timestamp(dt),color='#BFBFBF',lw=0.8,ls=':'); ax.text(pd.Timestamp(dt)+pd.Timedelta(days=3),205,t,fontsize=7,color='#666',style='italic')
ax.set_ylim(40,230); ax.set_xlim(x.index[0],x.index[-1]+pd.Timedelta(days=22))
ax.xaxis.set_major_locator(md.MonthLocator(bymonth=[1,3,5,7,9,11])); ax.xaxis.set_major_formatter(md.DateFormatter("%b '%y"))
ax.tick_params(labelsize=7.5,length=0)
for s in['top','right','left']: ax.spines[s].set_visible(False)
ax.grid(axis='y',color='#E6E6E6',lw=0.6); ax.set_ylabel('Indexed (Nov 10 2025 = 100)',fontsize=7.5,color='#555')
ax.legend(frameon=False,fontsize=7.5,loc='upper left',ncol=3,bbox_to_anchor=(0,1.08))
plt.tight_layout();_os.makedirs(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'out'), exist_ok=True); plt.savefig(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'out', 'JBLU_1yr_stock_chart.png'),facecolor='white')
