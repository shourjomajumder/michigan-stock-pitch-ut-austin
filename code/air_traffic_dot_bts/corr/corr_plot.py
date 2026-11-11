import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd, numpy as np, matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'serif','font.serif':['EB Garamond','Garamond','DejaVu Serif']})
N,UB,R='#0B2265','#1414D2','#C0392B'
exec(open('an.py').read().split("print('----')")[0].replace('print(','(lambda *a,**k:None)('))
o2=o;s2=s
rows=[]
for y in range(2005,2018):
  if y not in o.index: continue
  avg=o.loc[y].mean()
  for c in ['AA','DL','UA','B6','WN','AS','VX']:
    if any((c,yy) in merge for yy in (y,y+1)): continue
    if c in o and pd.notna(o.loc[y,c]) and y+2 in s.index and pd.notna(s.loc[y,c]) and pd.notna(s.loc[y+2,c]):
      rows.append(dict(c=c,y=y,gap=o.loc[y,c]-avg,chg=(s.loc[y+2,c]/s.loc[y,c]-1)*100))
d=pd.DataFrame(rows); d['rel']=d.chg-d.groupby('y').chg.transform('mean')
b=np.polyfit(d.gap,d.rel,1); r=np.corrcoef(d.gap,d.rel)[0,1]
print(len(d),r,b, b[0]*6.6+b[1])
d.to_csv(_os.path.join(_R, 'data/air_traffic_dot_bts/corr_ontime_share/panel_2yr.csv'),index=False)
fig,ax=plt.subplots(figsize=(8.2,5.6))
for s_ in ['top','right']: ax.spines[s_].set_visible(False)
ax.scatter(d.gap,d.rel,s=38,color=N,alpha=.75,label=f'Airline-years, 2006–2017 ({len(d)})')
xx=np.linspace(-9,9,50); ax.plot(xx,np.polyval(b,xx),color=UB,lw=2.4,label=f'Trend (r = {r:.2f})')
pu=np.polyval(b,6.6); ax.plot([6.6],[pu],'o',ms=13,color=R,zorder=5)
ax.text(6.9,pu+1.0,f'United +6.6 pts\n→ +{pu:.1f}% vs peers',fontsize=11,weight='bold')
ax.axhline(0,color='#999',lw=.8); ax.axvline(0,color='#999',lw=.8)
ax.set_xlabel('On-time % minus industry average (points)',fontsize=12)
ax.set_ylabel('2-yr domestic share growth vs peers (%)',fontsize=12)
ax.set_title('Better On-Time Airlines Gain Share',fontsize=17,weight='bold',pad=12)
ax.legend(frameon=False,loc='lower right',fontsize=10.5)
plt.tight_layout(); plt.savefig('Corr_ontime_vs_share.png',dpi=220)
