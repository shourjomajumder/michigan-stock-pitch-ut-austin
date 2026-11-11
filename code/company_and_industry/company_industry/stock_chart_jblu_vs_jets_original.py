import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, matplotlib.dates as md
plt.rcParams.update({'font.family':'serif','font.serif':['EB Garamond','Garamond','TeX Gyre Pagella','DejaVu Serif']})
d=pd.read_csv(_os.path.join(_R, 'data/company_and_industry/raw/yahoo_daily_close_JBLU_ULCC_JETS_SPY_2025-11-10_2026-11-09.csv'),parse_dates=['Date'],index_col='Date')
x=d/d.iloc[0]*100; N='#0B2265'
fig,ax=plt.subplots(figsize=(6.3,2.75),dpi=250)
ax.plot(x.index,x.JETS,color='#9A9A9A',lw=1.5,ls='--',label='Airline sector (JETS)')
ax.plot(x.index,x.JBLU,color=N,lw=2.2,label='JetBlue (JBLU)')
ax.axhline(100,color='#888',lw=0.7)
for s,c in [('JETS','#7F7F7F'),('JBLU',N)]:
    v=x[s].iloc[-1]; ax.text(x.index[-1]+pd.Timedelta(days=4),v,f'{v-100:+.0f}%'.replace('-','−'),color=c,fontsize=9,weight='bold',va='center')
ax.set_ylim(45,160); ax.set_xlim(x.index[0],x.index[-1]+pd.Timedelta(days=24))
ax.xaxis.set_major_locator(md.MonthLocator(bymonth=[1,3,5,7,9,11])); ax.xaxis.set_major_formatter(md.DateFormatter("%b '%y"))
ax.tick_params(labelsize=7.5,length=0)
for s in['top','right','left']: ax.spines[s].set_visible(False)
ax.grid(axis='y',color='#E6E6E6',lw=0.6)
ax.legend(frameon=False,fontsize=7.5,loc='upper left',ncol=2,bbox_to_anchor=(0,1.08))
plt.tight_layout();plt.savefig('../processed/JBLU_1yr_stock_chart.png',facecolor='white')
