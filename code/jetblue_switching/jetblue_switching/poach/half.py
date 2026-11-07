import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import glob
for f in glob.glob('/usr/share/texmf/fonts/opentype/public/tex-gyre/texgyrepagella*.otf'): fm.fontManager.addfont(f)
S='TeX Gyre Pagella'
W,H=6.2,6.0
fig=plt.figure(figsize=(W,H),dpi=250); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,100); ax.set_ylim(0,100); ax.axis('off')
ax.text(3,96,'What History Says About Switching',family=S,weight='bold',fontsize=13)
ax.plot([3,97],[93,93],color='#222',lw=1.6)
ax.text(3,88.6,'Switching shows up as fuller planes: with the same seats, the airline flyers prefer fills more of them,',family=S,style='italic',fontsize=8.6)
ax.text(3,85.4,'so its share of passengers rises above its share of seats. That extra share is the "pts" below.',family=S,style='italic',fontsize=8.6)
cases=[('Delta & Alaska (Seattle, 2004–2017)',[
 ('Alliance:','shared codes, miles and elite perks; Delta then built a Seattle hub'),
 ('Effect:','Delta\'s planes filled up more than Alaska\'s on the same routes'),
 ('Why:','Alaska flyers could try Delta at no cost to miles or status'),
 ('Size:','+0.6 pts extra passenger share by ~4 qtrs; peak +1.2 pts; gone ~3 yrs')]),
 ('American & JetBlue (Northeast Alliance, 2021–2023)',[
 ('Alliance:','shared codes, miles (May 2021) and elite perks (Oct 2021)'),
 ('Effect:','American\'s planes filled up more than JetBlue\'s on the same routes'),
 ('Why:','JetBlue flyers kept miles and perks on American\'s bigger network'),
 ('Size:','~+1.2 pts extra passenger share in 1–2 qtrs; faded in ~1 yr (weaker)')])]
y=79.5
for t,bs in cases:
    ax.text(3,y,t,family=S,weight='bold',fontsize=11); y-=6
    for a,b in bs:
        ax.text(4.5,y,'•',family=S,fontsize=10); ax.text(7.5,y,a,family=S,weight='bold',fontsize=9.6); ax.text(22,y,b,family=S,fontsize=9.6); y-=5.1
    y-=2.0
ax.plot([3,97],[y+3,y+3],color='#999',lw=0.6); y-=1.5
ax.text(3,y,'Applied to JetBlue & United (revenue lost through 2027)',family=S,weight='bold',fontsize=11); y-=6
for a,b in [('Bear:','0.25 pts, starts after ~4 qtrs  →  ~$3M'),('Base:','0.5 pts, starts after ~2 qtrs  →  ~$14M'),('Bull:','1.0 pts, starts after ~1 qtr  →  ~$39M')]:
    ax.text(4.5,y,'•',family=S,fontsize=10); ax.text(7.5,y,a,family=S,weight='bold',fontsize=9.6); ax.text(16,y,b,family=S,fontsize=9.6); y-=5.4
ax.text(3,max(y-1,1.5),'Source: BTS T-100, team analysis. 1 pt ≈ 27,300 passengers/qtr on 13 shared routes at $284 avg. fare.',family=S,style='italic',fontsize=7,color='#555')
plt.savefig('Switching_history_lefthalf.png',facecolor='white')
