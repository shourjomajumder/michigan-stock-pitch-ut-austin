import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, textwrap
from matplotlib import font_manager as fm
import glob
for f in glob.glob('/usr/share/texmf/fonts/opentype/public/tex-gyre/texgyrepagella*.otf'): fm.fontManager.addfont(f)
S='TeX Gyre Pagella'
cases=[('Case 1: Delta and Alaska (Seattle, 2004–2017)',[
 'The alliance: Delta and Alaska shared codes and frequent flyer programs, so flyers could earn and use miles and get elite perks on either airline. Delta then built its own Seattle hub (2013–2015) on Alaska\'s home turf.',
 'What happened: Delta won more Seattle passengers than its added seats alone explain. The effect faded once Alaska fought back, and reversed after the partnership ended in May 2017.',
 'Why: Alaska flyers could try Delta at no cost to their miles or status, and Delta added many more flights on Alaska\'s best routes. When Alaska cut shared perks and offered bonus miles, flyers came back.',
 'Size and timing: first clear effect +0.6 pts after ~4 quarters; peak +1.1 to +1.2 pts after ~6–7 quarters; back to ~0 after ~3 years.']),
('Case 2: American and JetBlue (Northeast Alliance, 2021–2023)',[
 'The alliance: American and JetBlue shared codes in New York and Boston, with shared miles from May 2021 and shared elite perks from October 2021. A court ended it in July 2023.',
 'What happened: right after shared elite perks started, American carried more passengers than its share of seats on routes both airlines flew. The gap then faded.',
 'Why: JetBlue flyers could earn miles and keep elite perks on American\'s much bigger network, so trying American cost them nothing.',
 'Size and timing: about +1.2 pts within 1–2 quarters, then faded within about a year. Weaker evidence: the gap did not reverse when the alliance ended.'])]
fig=plt.figure(figsize=(8,10),dpi=220); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,100); ax.set_ylim(0,125); ax.axis('off')
ax.text(50,120.5,'What History Says About Switching',ha='center',family=S,weight='bold',fontsize=15)
ax.plot([4,96],[117.3,117.3],color='#222',lw=1.8)
y=112
for title,bul in cases:
    ax.text(4,y,title,family=S,weight='bold',fontsize=12.5); y-=4.8
    for b in bul:
        lab,rest=b.split(': ',1); lines=textwrap.wrap(rest,84)
        ax.text(5,y,'•',family=S,fontsize=11); ax.text(7.5,y,lab+':',family=S,weight='bold',fontsize=10.5)
        y-=3.4
        for l in lines: ax.text(7.5,y,l,family=S,fontsize=10.3); y-=3.2
        y-=1.0
    y-=1.5; ax.plot([4,96],[y+1.5,y+1.5],color='#999',lw=0.6); y-=3
ax.text(4,y,'How we use this for JetBlue and United',family=S,weight='bold',fontsize=12.5); y-=4.8
for l in ['Bear: 0.25 pts of share, starting after ~4 quarters  →  ~$3M of JetBlue revenue through 2027',
          'Base: 0.5 pts, starting after ~2 quarters (Delta–Alaska average)  →  ~$14M',
          'Bull: 1.0 pts, starting after ~1 quarter (Delta–Alaska peak, NEA speed)  →  ~$39M']:
    ax.text(5,y,'•',family=S,fontsize=11); ax.text(7.5,y,l,family=S,fontsize=10.5); y-=3.8
y-=1
ax.text(4,y,'Source: BTS T-100 route data, team analysis (passenger share above seat share on routes both airlines fly, vs. a non-partner',family=S,style='italic',fontsize=7.6,color='#555'); y-=2.6
ax.text(4,y,'airline over the same quarters). 1 pt ≈ 27,300 passengers a quarter on the 13 shared routes, at a $284 DOT average fare.',family=S,style='italic',fontsize=7.6,color='#555')
plt.savefig('Switching_history_cases.png',facecolor='white',bbox_inches='tight',pad_inches=0.3)
