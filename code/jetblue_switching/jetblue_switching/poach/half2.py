import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, textwrap
from matplotlib import font_manager as fm
import glob
for f in glob.glob('/usr/share/texmf/fonts/opentype/public/tex-gyre/texgyrepagella*.otf'): fm.fontManager.addfont(f)
S='TeX Gyre Pagella'
fig=plt.figure(figsize=(6.2,5.7),dpi=250); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,100); ax.set_ylim(0,100); ax.axis('off')
ax.text(3,95.5,'What History Says About Switching',family=S,weight='bold',fontsize=13)
ax.plot([3,97],[92.3,92.3],color='#222',lw=1.6)
cases=[('Delta & Alaska (Seattle, 2004–2017)',[
 ('Alliance:','shared codes, miles and elite perks; Delta then built a Seattle hub'),
 ('Effect:','on routes both airlines flew, Delta\'s planes ran fuller (higher load factor) than Alaska\'s, so Delta carried a bigger share of passengers than its share of seats'),
 ('Why:','Alaska flyers could try Delta at no cost to miles or status'),
 ('Size:','+0.6 pts extra passenger share by ~4 qtrs; peak +1.2 pts; gone ~3 yrs')]),
 ('American & JetBlue (Northeast Alliance, 2021–2023)',[
 ('Alliance:','shared codes, miles (May 2021) and elite perks (Oct 2021)'),
 ('Effect:','on routes both airlines flew, American\'s planes ran fuller (higher load factor) than JetBlue\'s, so American carried a bigger share of passengers than its share of seats'),
 ('Why:','JetBlue flyers kept miles and perks on American\'s bigger network'),
 ('Size:','~+1.2 pts extra passenger share in 1–2 qtrs; faded in ~1 yr (weaker)')])]
y=85
for t,bs in cases:
    ax.text(3,y,t,family=S,weight='bold',fontsize=11); y-=6.2
    for a,b in bs:
        ax.text(4.5,y,'•',family=S,fontsize=10); ax.text(7.5,y,a,family=S,weight='bold',fontsize=9.6)
        for k,l in enumerate(textwrap.wrap(b,72)):
            ax.text(22,y,l,family=S,fontsize=9.6); y-=4.4
        y-=1.4
    y-=3
ax.text(3,max(y+1,1.5),'Source: BTS T-100 route data, team analysis.',family=S,style='italic',fontsize=7,color='#555')
plt.savefig('Switching_history_lefthalf.png',facecolor='white')
