import os as _os; _D = _os.path.dirname(_os.path.abspath(__file__)); _os.makedirs(_os.path.join(_D, 'out'), exist_ok=True)  # outputs go to out/ next to this script
import numpy as np, matplotlib.pyplot as plt
exec(open(_os.path.join(_D, 'fit.py')).read().split("for lab")[0])
plt.rcParams.update({'font.family':'serif','font.serif':['EB Garamond','Garamond','DejaVu Serif']})
N,UB,R='#0B2265','#1414D2','#C0392B'
m=x<=2;b=np.polyfit(x[m],y[m],1);r=np.corrcoef(x[m],y[m])[0,1]
fig,ax=plt.subplots(figsize=(8.2,5.4))
for s in['top','right']:ax.spines[s].set_visible(False)
rng=np.random.default_rng(3)
ax.scatter(x[m]+rng.uniform(-.12,.12,m.sum()),y[m],s=70,color=N,alpha=.85,label='Past airline cases (12)')
xs=np.linspace(-.2,2.2,10);ax.plot(xs,np.polyval(b,xs),color=UB,lw=2.6,label=f'Trend line (r = {r:.2f})')
p=np.polyval(b,1);ax.plot(1,p,'o',ms=16,color=R,zorder=5,label='JetBlue + United (Blue Sky)')
ax.text(1.1,p-.4,f'{p:.1f}% / year',fontsize=14,weight='bold',va='top')
ax.axhline(0,color='#999',lw=.8)
ax.set_xticks([0,1,2]);ax.set_xticklabels(['No link\n(just a better product)','Shared loyalty points','Codeshare +\nshared loyalty'],fontsize=11)
ax.set_ylabel('Passengers lost to rival per year (%)',fontsize=12)
ax.set_title('Tighter Airline Ties = More Passengers Switch',fontsize=17,weight='bold',pad=12)
ax.legend(frameon=False,loc='upper left',fontsize=11)
plt.tight_layout();plt.savefig(_os.path.join(_D, 'out', 'Switching_correlation_simple.png'),dpi=220)
