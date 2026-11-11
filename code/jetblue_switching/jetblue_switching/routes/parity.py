import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../..')  # repo root
_D = _os.path.dirname(_os.path.abspath(__file__)); _os.makedirs(_os.path.join(_D, 'out'), exist_ok=True)  # chart goes to out/ next to this script
import numpy as np, pandas as pd, matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'serif','font.serif':['EB Garamond','Garamond','DejaVu Serif']})
# (group, route, depth, share_before, share_after, months) for the incumbent/losing-side carrier, fare gap <=10%, window >=12 mo
P=[('Delta vs JetBlue (Boston)','BOS-BUF',0,75.00,65.64,24),('Delta vs JetBlue (Boston)','BOS-PIT',0,60.27,54.69,21),('Delta vs JetBlue (Boston)','BOS-TPA',0,36.78,40.22,15),
('Delta vs JetBlue (Boston)','BOS-RDU',0,41.79,37.31,33),('Delta vs JetBlue (Boston)','BOS-RIC',0,49.00,59.32,51),('Delta vs JetBlue (Boston)','BOS-CHS',0,41.35,55.16,48),('Delta vs JetBlue (Boston)','BOS-PBI',0,68.46,70.32,54),
('Delta vs Alaska (Seattle)','SEA-GEG',0,93.9,79.9,48),('Delta vs Alaska (Seattle)','SEA-PDX',0,93.0,86.0,60),('Delta vs Alaska (Seattle)','SEA-LAX',0,58.9,60.9,45),('Delta vs Alaska (Seattle)','SEA-SFO',0,47.0,50.0,36),
('Delta vs Alaska (Seattle)','SEA-SAN',0,58.8,51.5,24),('Delta vs Alaska (Seattle)','SEA-BOI',0,82.2,78.0,48),('Delta vs Alaska (Seattle)','SEA-PSC',0,90.7,81.1,36),('Delta vs Alaska (Seattle)','SEA-EUG',0,71.9,65.4,18),
('Delta vs Alaska (Seattle)','SEA-DEN',0,35.5,34.8,12),('Delta vs Alaska (Seattle)','SEA-AUS',0,54.2,54.6,21),('Delta vs Alaska (Seattle)','SEA-SLC',0,33.0,39.8,54),
('JetBlue Mint vs United','NYC-LAX',0,29.0,28.86,24),
('Continental / Northwest','CLE-DTW',1,77.98,69.48,33),('Continental / Northwest','DTW-IAH',1,36.58,34.32,57),('Continental / Northwest','IAH-MEM',1,42.94,39.58,33),
('Delta / Continental / Northwest','CVG-IAH',2,54.41,49.86,24),('Delta / Continental / Northwest','MSP-SLC',2,48.99,42.06,24),('American / Alaska','SEA-PHL',2,56.0,37.3,60)]
d=pd.DataFrame(P,columns=['case','route','depth','before','after','months']);d['loss_yr']=-(d.after/d.before-1)*100/d.months*12
d.to_csv(_os.path.join(_R, 'data/jetblue_switching/processed/routes/parity_points.csv'),index=False)
print(d.groupby('depth').loss_yr.agg(['mean','median','count']).round(2))
b=np.polyfit(d.depth,d.loss_yr,1);r=np.corrcoef(d.depth,d.loss_yr)[0,1];p=np.polyval(b,1)
n=len(d);res=d.loss_yr-np.polyval(b,d.depth);sd=res.std(ddof=2);se=sd*np.sqrt(1/n+(1-d.depth.mean())**2/((d.depth-d.depth.mean())**2).sum())
print('fit',b,r,'pred',p,'se',se,'cum22',p*22/12,(p-1.96*se)*22/12,(p+1.96*se)*22/12)
col={'Delta vs JetBlue (Boston)':'#7F7F7F','Delta vs Alaska (Seattle)':'#2E9E44','JetBlue Mint vs United':'#17BECF','Continental / Northwest':'#9467BD','Delta / Continental / Northwest':'#0B2265','American / Alaska':'#F08A24'}
fig,ax=plt.subplots(figsize=(11,5.6))
for s in['top','right']:ax.spines[s].set_visible(False)
rng=np.random.default_rng(5);seen=set()
for _,q in d.iterrows():
    j=rng.uniform(-.2,.2) if q.depth==0 else rng.uniform(-.1,.1)
    ax.scatter(q.depth+j,q.loss_yr,s=90,color=col[q.case],edgecolor='black',lw=.6,zorder=4,label=None if q.case in seen else q.case);seen.add(q.case)
xs=np.linspace(-.3,2.3,10);ax.plot(xs,np.polyval(b,xs),color='#1414D2',lw=2.6,zorder=3)
ax.scatter(1,p,s=300,marker='D',color='black',zorder=5,label='JetBlue + United (Blue Sky)')
ax.text(1.12,p+1.6,f'{p:.1f}% / year',fontsize=14,weight='bold')
ax.axhline(0,color='#999',lw=.8)
ax.set_xticks([0,1,2]);ax.set_xticklabels(['No link\n(just a better product)','Shared loyalty points','Codeshare +\nshared loyalty'],fontsize=11)
ax.set_ylabel('Share lost per year on same-fare routes (%)',fontsize=12)
ax.set_title(' ',fontsize=17,pad=12)
h,l=ax.get_legend_handles_labels();o=[len(l)-1]+list(range(len(l)-1))
ax.legend([h[i] for i in o],[l[i] for i in o],frameon=False,loc='center left',bbox_to_anchor=(1.02,.5),fontsize=11,title='Cases',title_fontproperties={'weight':'bold','size':12},alignment='left')
plt.tight_layout();plt.savefig(_os.path.join(_D, 'out', 'Switching_same_fare_routes.png'),dpi=220,bbox_inches='tight')
