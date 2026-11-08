import os as _os; _D = _os.path.dirname(_os.path.abspath(__file__)); _O = _os.path.join(_D, 'out'); _os.makedirs(_O, exist_ok=True)  # script dir / outputs
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np, pandas as pd, matplotlib.dates as md
plt.rcParams.update({'font.family':'DejaVu Serif'})
rows=[r.split(',') for r in open(_os.path.join(_D, 'rolljets.txt')).read().strip().split(';')]
d=pd.DataFrame(rows,columns=['d','u','j','p']); d['d']=pd.to_datetime(d.d,format='%y%m%d'); d[['u','j','p']]=d[['u','j','p']].astype(float)/100
air=(d.u+d.j)/2; print(round(d.p.mean(),3), round(air.mean(),2))
fig,ax=plt.subplots(figsize=(6.2,3.0),dpi=300)
ax.plot(d.d,air,color='#BFBFBF',lw=1.4,ls='--',label='Frontier & JetBlue alone (average)')
ax.plot(d.d,d.p,color='#1A1A1A',lw=1.9,label='Jet fuel-neutral pair, ratio 1.16')
ax.axhline(0,color='#777777',lw=0.9)
ax.set_ylim(-0.4,1.0); ax.set_yticks([-0.4,-0.2,0,0.2,0.4,0.6,0.8,1.0])
ax.set_ylabel('Correlation with JETS airline ETF (60-day)',fontsize=7,color='#555555')
ax.tick_params(labelsize=7.5,colors='#555555',length=0)
ax.xaxis.set_major_locator(md.MonthLocator(bymonth=[2,4,6,8,10])); ax.xaxis.set_major_formatter(md.DateFormatter("%b '%y"))
ax.yaxis.grid(True,color='#E3E3E3',lw=0.6); ax.set_axisbelow(True)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#BBBBBB'); ax.legend(frameon=False,fontsize=7.5,loc='upper center',bbox_to_anchor=(0.5,-0.1),ncol=2)
plt.tight_layout(); fig.savefig(_os.path.join(_O, 'NonOil_top_rolling_JETS.png'),facecolor='white'); plt.close(fig)
q=['Jet\nfuel','Airline\nsector','Small\ncaps','Stock\nmarket','Consumer\nspending','Credit\nmarkets']
u=[0.41,0.77,0.50,0.42,0.42,0.41]; j=[0.41,0.76,0.52,0.45,0.47,0.49]; p=[0.00,0.01,0.04,0.05,0.07,0.11]
x=np.arange(len(q)); w=0.27
fig,ax=plt.subplots(figsize=(6.2,3.4),dpi=300)
for off,v,c,l in [(-w,u,'#8C8C8C','Frontier (ULCC)'),(0,j,'#C8C8C8','JetBlue (JBLU)'),(w,p,'#1A1A1A','Hedged pair')]:
    b=ax.bar(x+off,v,w*0.8,color=c,label=l,edgecolor='#1A1A1A',linewidth=1.4)
    for bb,vv in zip(b,v): ax.text(bb.get_x()+bb.get_width()/2,vv+0.012,f'{vv:.2f}',ha='center',fontsize=7.5,color='#333333')
ax.set_xticks(x); ax.set_xticklabels(q,fontsize=8.5); ax.set_ylim(0,0.92); ax.set_yticks([])
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#BBBBBB'); ax.tick_params(length=0)
ax.legend(frameon=False,fontsize=8,loc='upper right',ncol=3)
plt.tight_layout(); fig.savefig(_os.path.join(_O, 'NonOil_bottom_bars.png'),facecolor='white')
