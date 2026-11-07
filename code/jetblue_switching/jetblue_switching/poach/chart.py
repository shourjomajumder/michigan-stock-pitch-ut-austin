import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import glob
for f in glob.glob('/usr/share/texmf/fonts/opentype/public/tex-gyre/texgyrepagella*.otf')+glob.glob('/usr/share/fonts/truetype/crosextra/Carlito*.ttf'): fm.fontManager.addfont(f)
S='TeX Gyre Pagella'; N='Carlito'; G='#0F6E46'; GR='#A6A6A6'
yrs=[2013,2014,2015,2016,2017,2018,2019]; v=[0.0,0.83,0.52,-0.29,-0.99,-0.94,-0.34]
col=[GR,G,G,GR,GR,GR,GR]
fig,ax=plt.subplots(figsize=(6.4,3.9),dpi=250)
ax.bar(yrs,v,0.62,color=col,edgecolor='white',linewidth=2)
for x,y in zip(yrs,v):
    ax.text(x,y+(0.06 if y>=0 else -0.06),f'{y:+.1f}' if y!=0 else '0.0',ha='center',va='bottom' if y>=0 else 'top',family=N,weight='bold',fontsize=10,color='#333')
ax.axhline(0,color='#888',lw=0.9)
ax.axvline(2016.5,color='#555',lw=1,ls=(0,(3,3)))
ax.text(2016.55,1.02,'Partnership ends\n(May 2017)',family=S,fontsize=8.5,color='#555',va='top')
ax.text(2014.5,1.27,'Delta floods Alaska\'s routes\nwhile still loyalty partners',family=S,fontsize=8.5,color=G,ha='center',va='top',weight='bold')
ax.set_ylim(-1.25,1.3); ax.set_xticks(yrs)
for t in ax.get_xticklabels(): t.set_family(N)
ax.set_yticks([]); [ax.spines[s].set_visible(False) for s in ['top','right','left','bottom']]
ax.tick_params(length=0,labelsize=10,colors='#444')
ax.set_ylabel('Delta passenger share above its seat share\n(pp, vs. 2013, United-vs-Alaska control)',family=S,fontsize=8.5,color='#666')
plt.tight_layout(); fig.savefig('Delta_Alaska_poaching.png',facecolor='white')
