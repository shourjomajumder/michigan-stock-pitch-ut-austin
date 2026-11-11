import os as _os; _D = _os.path.dirname(_os.path.abspath(__file__)); _os.makedirs(_os.path.join(_D, 'out'), exist_ok=True)  # outputs go to out/ next to this script
import numpy as np, matplotlib.pyplot as plt
exec(open(_os.path.join(_D, 'fit.py')).read().split("for lab")[0])
plt.rcParams.update({'font.family':'serif','font.serif':['EB Garamond','Garamond','DejaVu Serif']})
N,UB,R,G='#0B2265','#1414D2','#C0392B','#E6E6E6'
m=x<=2;b=np.polyfit(x[m],y[m],1);p=np.polyval(b,1);se=1.0037;sd=3.278
# Chart 1: case model
fig,ax=plt.subplots(figsize=(8.2,5.6))
for s in['top','right']:ax.spines[s].set_visible(False)
jit={0:[-.12,-.04,.04,.12],2:[-.2,-.14,-.08,-.02,.04,.1,.16,.22]};k={0:0,2:0}
for c,xx,yy in cases:
  if xx==3: continue
  j=jit[xx][k[xx]];k[xx]+=1
  ax.plot(xx+j,yy,'o',ms=8,color=N,alpha=.85)
xs=np.linspace(-.3,2.3,50);ax.plot(xs,np.polyval(b,xs),color=UB,lw=2.4)
ax.fill_between(xs,np.polyval(b,xs)-1.96*se,np.polyval(b,xs)+1.96*se,color='#E3EDF9',zorder=0)
ax.plot(1,p,'o',ms=14,color=R,zorder=5);ax.text(1.08,p-1.2,f'Blue Sky (loyalty only)\n{p:.1f}% per year',fontsize=11.5,weight='bold')
ax.text(-.25,-6.3,'Better product only\n(Delta vs JetBlue BOS,\nDelta vs Alaska SEA, LAX)',fontsize=9.5)
ax.text(1.55,15.2,'Codeshare + loyalty\n(USAir/BA, Delta/WestJet)',fontsize=9.5)
ax.axhline(0,color='#999',lw=.8)
ax.set_xticks([0,1,2]);ax.set_xticklabels(['Product gap only','Loyalty link only','Codeshare + loyalty'],fontsize=11)
ax.set_ylabel('Rival passengers lost per year (%)',fontsize=12)
ax.set_title('12 Case Studies: Deeper Ties Move More Passengers',fontsize=16,weight='bold',pad=12)
ax.text(2.3,-5.8,f'r = {np.corrcoef(x[m],y[m])[0,1]:.2f}, n = 12',fontsize=10.5,ha='right')
ax.set_ylim(-7,17);plt.tight_layout();plt.savefig(_os.path.join(_D, 'out', 'Case_model_depth.png'),dpi=220)
# Chart 2: projection line
t=np.arange(0,25);mo=['Oct 25','','','Jan 26','','','Apr 26','','','Jul 26','','','Oct 26','','','Jan 27','','','Apr 27','','','Jul 27','','','Oct 27']
fig,ax=plt.subplots(figsize=(8.2,5.6))
for s in['top','right']:ax.spines[s].set_visible(False)
c=p*t/12;lo=(p-1.96*se)*t/12;hi=(p+1.96*se)*t/12
ax.fill_between(t,lo,hi,color='#E3EDF9',label='95% range from case model')
ax.plot(t,c,color=N,lw=2.8,label=f'Case model: {p:.1f}% per year')
ax.plot([9],[1.5],'s',ms=10,color=UB,zorder=5,label='Actual, Jul 2026 (DOT tickets)')
ax.axvspan(21,23,color=G,zorder=0);ax.text(22,.4,'Q3 2027',ha='center',fontsize=10.5)
ax.plot(22,hi[22],'o',ms=13,color=R,zorder=6);ax.text(21.6,hi[22]+.5,'Our case: 10%',fontsize=12,weight='bold',ha='right')
ax.plot(22,c[22],'o',ms=9,color=N,zorder=6);ax.text(21.6,c[22]-.6,f'Base: {c[22]:.1f}%',fontsize=11,ha='right',va='top')
ax.set_xticks(t);ax.set_xticklabels(mo,fontsize=9.5);ax.set_xlim(0,24);ax.set_ylim(0,12)
ax.set_ylabel('JetBlue passengers switched to United (%)',fontsize=12)
ax.set_title('Projected Switching Since Blue Sky Launch',fontsize=16,weight='bold',pad=12)
ax.legend(frameon=False,loc='upper left',fontsize=10.5)
plt.tight_layout();plt.savefig(_os.path.join(_D, 'out', 'Case_model_projection.png'),dpi=220)
print(c[22],hi[22],lo[22])
