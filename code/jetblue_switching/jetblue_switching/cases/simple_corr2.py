import os as _os; _D = _os.path.dirname(_os.path.abspath(__file__)); _os.makedirs(_os.path.join(_D, 'out'), exist_ok=True)  # outputs go to out/ next to this script
import numpy as np, matplotlib.pyplot as plt
exec(open(_os.path.join(_D, 'fit.py')).read().split("for lab")[0])
plt.rcParams.update({'font.family':'serif','font.serif':['EB Garamond','Garamond','DejaVu Serif']})
UB,R='#1414D2','#C0392B'
m=x<=2;b=np.polyfit(x[m],y[m],1);r=np.corrcoef(x[m],y[m])[0,1]
names={'Delta vs JetBlue, BOS 2015-19':'Delta vs JetBlue, Boston (2015–19)','Delta vs Alaska, SEA 2015-19':'Delta vs Alaska, Seattle (2015–19)',
'Delta vs Alaska, SEA 2019-25':'Delta vs Alaska, Seattle (2019–25)','Delta vs American, LAX 2023-25':'Delta vs American, LAX (2023–25)',
'USAir/BA: United':'USAir/BA → United lost','USAir/BA: Delta':'USAir/BA → Delta lost','USAir/BA: Northwest':'USAir/BA → Northwest lost',
'USAir/BA: TWA':'USAir/BA → TWA lost','USAir/BA: Continental':'USAir/BA → Continental lost','USAir/BA: interior-city rival':'USAir/BA → interior-city rival lost',
'Delta/WestJet: United':'Delta/WestJet → United lost','Delta/WestJet: American':'Delta/WestJet → American lost'}
cols=['#7F7F7F','#2E9E44','#8BC34A','#17BECF','#0B2265','#3B5BDB','#9467BD','#E377C2','#F08A24','#8C564B','#D4A017','#BCBD22']
off={0:[-.15,-.05,.05,.15],2:[-.22,-.16,-.1,-.04,.02,.08,.14,.2]};k={0:0,2:0}
fig,ax=plt.subplots(figsize=(11,5.6))
for s in['top','right']:ax.spines[s].set_visible(False)
i=0
for c,xx,yy in cases:
  if xx==3: continue
  ax.scatter(xx+off[xx][k[xx]],yy,s=90,color=cols[i],edgecolor='black',lw=.6,label=names[c],zorder=4);k[xx]+=1;i+=1
xs=np.linspace(-.3,2.3,10);ax.plot(xs,np.polyval(b,xs),color=UB,lw=2.6,label=f'Trend line (r = {r:.2f})',zorder=3)
p=np.polyval(b,1);ax.scatter(1,p,s=320,color=R,edgecolor='black',zorder=5,label='JetBlue + United (Blue Sky)')
ax.text(1.1,p-.4,f'{p:.1f}% / year',fontsize=14,weight='bold',va='top')
ax.axhline(0,color='#999',lw=.8)
ax.set_xticks([0,1,2]);ax.set_xticklabels(['No link\n(just a better product)','Shared loyalty points','Codeshare +\nshared loyalty'],fontsize=11)
ax.set_ylabel('Passengers lost to rival per year (%)',fontsize=12)
ax.set_title('Tighter Airline Ties = More Passengers Switch',fontsize=17,weight='bold',pad=12)
h,l=ax.get_legend_handles_labels()
order=[l.index('JetBlue + United (Blue Sky)'),l.index(f'Trend line (r = {r:.2f})')]+[j for j in range(len(l)) if j not in (l.index('JetBlue + United (Blue Sky)'),l.index(f'Trend line (r = {r:.2f})'))]
ax.legend([h[j] for j in order],[l[j] for j in order],frameon=False,loc='center left',bbox_to_anchor=(1.02,.5),fontsize=10.5,title='Cases',title_fontproperties={'weight':'bold','size':12},alignment='left')
plt.tight_layout();plt.savefig(_os.path.join(_D, 'out', 'Switching_correlation_legend.png'),dpi=220,bbox_inches='tight')
