import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm, Normalize, to_hex
src=open(_os.path.join(_R, 'code/frontier_routes_and_load_factor/mat/m5.py')).read().split('for nm,c in')[0]; exec(src)
def curve(mid,end): return [0.55,(0.55+mid)/2,mid,end,end+0.10]
mids=[0.75,0.80,0.85,0.90,0.95]; ends=[0.85,0.95,1.05,1.15]
BP=pd.DataFrame(index=mids,columns=ends,dtype=float); UP=BP.copy()
for m in mids:
  for e in ends:
    t,r=run(curve(m,e)); BP.loc[m,e]=t.loc['Total','2027Q3']; UP.loc[m,e]=(r[['2027Q1','2027Q2','2027Q3']]-r['2026Q4']).sum()
print(BP.round(3)); print(UP.round(1)); BP.to_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/small_bp.csv')); UP.to_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/small_up.csv'))
S='TeX Gyre Pagella'; N='Carlito'; G='#1E6B3A'
cm=LinearSegmentedColormap.from_list('x',['#F8696B','#FFEB84','#63BE7B'])
W,H=6.05,5.6
fig=plt.figure(figsize=(W,H),dpi=300); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,W); ax.set_ylim(0,H); ax.axis('off')
cw,ch=0.98,0.255; x0=1.95
sg=lambda v,f:('+' if v>0.0049 else ('−' if v<-0.0049 else ''))+f(abs(v))
def block(D,ytitle,title,fmt,norm):
    ax.text(W/2,ytitle,title,family=S,fontsize=15,ha='center',va='bottom'); ax.plot([0.02,W-0.02],[ytitle-0.06]*2,color='#222',lw=1.6)
    ycl=ytitle-0.36
    ax.text(x0+2*cw,ycl,'RASM at 9–11 months (Q3 2027), % of system avg',family=S,style='italic',fontsize=9.5,ha='center',va='center')
    yh=ycl-0.25
    for j,e in enumerate(ends): ax.text(x0+j*cw+cw/2,yh,f'{e:.0%}',family=N,weight='bold',fontsize=10,ha='center',va='center')
    top=yh-0.14; ax.plot([x0,x0+4*cw],[top,top],color='black',lw=0.9)
    for i,m in enumerate(mids):
        y=top-(i+1)*ch
        ax.text(x0-0.08,y+ch/2,f'{m:.0%}',family=N,weight='bold',fontsize=10,ha='right',va='center')
        for j,e in enumerate(ends):
            v=D.iloc[i,j]; ax.add_patch(Rectangle((x0+j*cw,y),cw,ch,fc=cm(norm(v)),ec='white',lw=1.2))
            ax.text(x0+j*cw+cw/2,y+ch/2,fmt(v),family=N,fontsize=10,ha='center',va='center')
    bot=top-5*ch; ax.plot([x0,x0+4*cw],[bot,bot],color='black',lw=0.9)
    ax.text(0.7,(top+bot)/2,'RASM at\n6–8 months\n(Q2 2027),\n% of system avg',family=S,style='italic',fontsize=9.5,ha='center',va='center',linespacing=1.25)
    for (m,e,c,ls) in [(0.90,1.05,G,'-')]:
        i=mids.index(m); j=ends.index(e)
        ax.add_patch(Rectangle((x0+j*cw+0.025,top-(i+1)*ch+0.025),cw-0.05,ch-0.05,fill=False,ec=c,lw=2.2,ls=ls,zorder=5))
    ax.add_patch(Rectangle((0.25,yh-0.085),0.3,0.17,fill=False,ec=G,lw=2.2)); ax.text(0.63,yh,'Our case',family=S,fontsize=9.5,va='center')
    return bot
b1=block(BP,H-0.38,'Q3 2027 Effect on System RASM',lambda v:sg(v,lambda a:f'{a:.2f}%'),TwoSlopeNorm(0,BP.values.min(),BP.values.max()))
b2=block(UP,b1-0.62,'Q1–Q3 2027 Revenue vs. Q4 2026 Run-Rate',lambda v:sg(v,lambda a:f'${a:.1f}M'),Normalize(UP.values.min(),UP.values.max()))
_OUT=_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),'out'); _os.makedirs(_OUT,exist_ok=True)
fig.savefig(_os.path.join(_OUT,'Sens_right_half_small.png'),facecolor='white',bbox_inches='tight',pad_inches=0.05)
# hex list for instructions
out=[]
for nm,D,n,f in [('Top',BP,TwoSlopeNorm(0,BP.values.min(),BP.values.max()),lambda v:sg(v,lambda a:f'{a:.2f}%')),('Bottom',UP,Normalize(UP.values.min(),UP.values.max()),lambda v:sg(v,lambda a:f'${a:.1f}M'))]:
    out.append(f'\n{nm} table (rows 75/80/85/90/95%; columns 85/95/105/115%)')
    for i,r in D.iterrows(): out.append(f'{float(i):.0%} | '+' | '.join(f'{f(v)} {to_hex(cm(n(v))).upper()}' for v in r))
open(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/cells_small.txt'),'w').write('\n'.join(out))
