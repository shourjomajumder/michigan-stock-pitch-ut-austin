import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, pandas as pd
S='TeX Gyre Pagella'; N='Carlito'; G='#1E6B3A'
info=pd.read_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/detail_info.csv'),index_col=0)
fig,ax=plt.subplots(figsize=(8.2,5.4)); ax.set_xlim(0,8.2); ax.set_ylim(0,5.4); ax.axis('off')
ax.text(0.05,5.15,'Our Breakdown of the New Routes',family=S,weight='bold',fontsize=15,va='center')
ax.plot([0.05,8.15],[4.92,4.92],color=G,lw=2)
cols=[('Launched',3.1),('Weekly\nround trips',4.1),('Miles',4.95),('Weekly\nseats',5.7),('% of system\nASMs',6.7),('Fully\nmature',7.7)]
yh=4.5; top=4.1; rh=0.5
for t,x in cols: ax.text(x,yh,t,family=S,weight='bold',fontsize=10.5,ha='center',va='center',linespacing=1.1)
ax.plot([0.05,8.15],[top,top],color='black',lw=1)
for i,r in enumerate(list(info.index)+['Total']):
    y=top-(i+0.5)*rh; tot=r=='Total'; w='bold' if tot else 'normal'
    if tot: ax.plot([0.05,8.15],[y+rh/2,y+rh/2],color='black',lw=1)
    ax.text(0.05,y,'Total' if tot else r,family=S,fontsize=11.5,weight=w,va='center')
    if tot: vals=['','','',f'{int(info.wkseats.sum()):,}',f'{info.share.sum():.2f}%','']
    else:
        o=info.loc[r]; d=pd.Timestamp(o.start); m=d+pd.DateOffset(months=12)
        vals=[d.strftime('%b %Y'),f'{int(o.f)}',f'{int(o.dist):,}',f'{int(o.wkseats):,}',f'{o.share:.2f}%',f"Q{(m.month-1)//3+1} '{m.strftime('%y')}"]
    for (t,x),v in zip(cols,vals): ax.text(x,y,v,family=N,fontsize=11.5,weight=w,ha='center',va='center')
yb=top-7*rh; ax.plot([0.05,8.15],[yb,yb],color=G,lw=2)
ax.text(0.05,yb-0.15,'Seats = round trips × 2 × 230. Share of system ASMs uses a full quarter of flying vs. 11.1B system ASMs.\nFully mature = 12 months after launch. Source: team model.',family=S,fontsize=8.5,color='#555555',va='top',linespacing=1.3)
plt.savefig('Thesis2_route_breakdown.png',dpi=220,bbox_inches='tight',facecolor='white')
