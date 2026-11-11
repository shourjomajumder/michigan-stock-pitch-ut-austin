import os as _os; _D = _os.path.dirname(_os.path.abspath(__file__)); _os.makedirs(_os.path.join(_D, 'out'), exist_ok=True)  # outputs go to out/ next to this script
import numpy as np, matplotlib.pyplot as plt
exec(open(_os.path.join(_D, 'fit.py')).read().split("for lab")[0])
plt.rcParams.update({'font.family':'serif','font.serif':['EB Garamond','Garamond','DejaVu Serif']})
R='#C0392B'
m=x<=2;b=np.polyfit(x[m],y[m],1);p=np.polyval(b,1)
grp=lambda c:('Delta vs JetBlue (Boston)' if 'JetBlue' in c else 'Delta vs Alaska (Seattle)' if 'Alaska' in c else
 'Delta vs American (LAX)' if 'LAX' in c else 'USAir / British Airways' if 'USAir' in c else 'Delta / WestJet')
col={'Delta vs JetBlue (Boston)':'#7F7F7F','Delta vs Alaska (Seattle)':'#2E9E44','Delta vs American (LAX)':'#17BECF','USAir / British Airways':'#0B2265','Delta / WestJet':'#F08A24'}
off={0:[-.15,-.05,.05,.15],2:[-.22,-.16,-.1,-.04,.02,.08,.14,.2]};k={0:0,2:0}
fig,ax=plt.subplots(figsize=(11,5.6))
for s in['top','right']:ax.spines[s].set_visible(False)
seen=set()
for c,xx,yy in cases:
  if xx==3: continue
  g=grp(c);ax.scatter(xx+off[xx][k[xx]],yy,s=90,color=col[g],edgecolor='black',lw=.6,zorder=4,label=None if g in seen else g);seen.add(g);k[xx]+=1
xs=np.linspace(-.3,2.3,10);ax.plot(xs,np.polyval(b,xs),color='#1414D2',lw=2.6,zorder=3)
ax.scatter(1,p,s=320,color=R,edgecolor='black',zorder=5,label='JetBlue + United (Blue Sky)')
ax.text(1.1,p-.4,f'{p:.1f}% / year',fontsize=14,weight='bold',va='top')
ax.axhline(0,color='#999',lw=.8)
ax.set_xticks([0,1,2]);ax.set_xticklabels(['No link\n(just a better product)','Shared loyalty points','Codeshare +\nshared loyalty'],fontsize=11)
ax.set_ylabel('Passengers lost to rival per year (%)',fontsize=12)
ax.set_title('Tighter Airline Ties = More Passengers Switch',fontsize=17,weight='bold',pad=12)
h,l=ax.get_legend_handles_labels();o=[len(l)-1]+list(range(len(l)-1))
ax.legend([h[j] for j in o],[l[j] for j in o],frameon=False,loc='center left',bbox_to_anchor=(1.02,.5),fontsize=11,title='Cases',title_fontproperties={'weight':'bold','size':12},alignment='left')
plt.tight_layout();plt.savefig(_os.path.join(_D, 'out', 'Switching_correlation_legend.png'),dpi=220,bbox_inches='tight')
