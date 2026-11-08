import os as _os; _D = _os.path.dirname(_os.path.abspath(__file__)); _O = _os.path.join(_D, 'out'); _os.makedirs(_O, exist_ok=True)  # script dir / outputs
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, pandas as pd, matplotlib.dates as md
plt.rcParams.update({'font.family':'DejaVu Serif'})
c=['d','spy','jets','pair','u','j','u_s','j_s','p_s','u_j','j_j','p_j']
d=pd.DataFrame([r.split(',') for r in open(_os.path.join(_D, 'volroll.txt')).read().strip().split(';')],columns=c)
d['d']=pd.to_datetime(d.d,format='%y%m%d'); 
for k in c[1:]: d[k]=d[k].astype(float)
d['a_s']=(d.u_s+d.j_s)/2; d['a_j']=(d.u_j+d.j_j)/2
print(d[['spy','jets','pair','a_s','p_s','a_j','p_j']].mean().round(1))
def chart(fn,a,al,ac,als,p,pl,ylab,ymax):
    fig,ax=plt.subplots(figsize=(6.2,3.0),dpi=300)
    ax.plot(d.d,d[a],color=ac,lw=1.7,ls=als,label=al); ax.plot(d.d,d[p],color='#1A1A1A',lw=1.9,label=pl)
    ax.set_ylim(0,ymax); ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v,_:f'{v:.0f}%'))
    ax.set_ylabel(ylab,fontsize=7,color='#555555'); ax.tick_params(labelsize=7.5,colors='#555555',length=0)
    ax.xaxis.set_major_locator(md.MonthLocator(bymonth=[2,4,6,8,10])); ax.xaxis.set_major_formatter(md.DateFormatter("%b '%y"))
    ax.yaxis.grid(True,color='#E3E3E3',lw=0.6); ax.set_axisbelow(True)
    for s in ['top','right','left']: ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color('#BBBBBB'); ax.legend(frameon=False,fontsize=7.5,loc='upper center',bbox_to_anchor=(0.5,-0.1),ncol=2)
    plt.tight_layout(); fig.savefig(_os.path.join(_O, fn),facecolor='white'); plt.close(fig)
P='Jet fuel-neutral pair, ratio 1.16'
chart('V1_SPY_vs_pair_totalvol.png','spy','S&P 500','#8C8C8C','-','pair',P,'Annualized volatility (60-day)',100)
chart('V2_JETS_vs_pair_totalvol.png','jets','JETS airline ETF','#8C8C8C','-','pair',P,'Annualized volatility (60-day)',100)
chart('V3_SPY_driven_vol.png','a_s','Frontier & JetBlue alone (average)','#8C8C8C','-','p_s',P,'Volatility from S&P 500 moves (60-day)',50)
chart('V4_JETS_driven_vol.png','a_j','Frontier & JetBlue alone (average)','#8C8C8C','-','p_j',P,'Volatility from airline-sector moves (60-day)',80)
from PIL import Image, ImageDraw, ImageFont
ims=[Image.open(_os.path.join(_O, f)) for f in ['V1_SPY_vs_pair_totalvol.png','V2_JETS_vs_pair_totalvol.png','V3_SPY_driven_vol.png','V4_JETS_driven_vol.png']]
W,H=ims[0].size; g=Image.new('RGB',(W*2,H*2+160),'white'); dr=ImageDraw.Draw(g)
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf',46)
labs=['A. As asked: S&P 500 vs. pair (total volatility)','B. As asked: JETS vs. pair (total volatility)','C. Recommended: volatility from S&P 500 moves','D. Recommended: volatility from airline-sector moves']
for i,(im,l) in enumerate(zip(ims,labs)):
    x=(i%2)*W; y=(i//2)*(H+80); dr.text((x+40,y+10),l,fill='#222',font=f); g.paste(im,(x,y+80))
g.save(_os.path.join(_O, 'Vol_options.png'))
