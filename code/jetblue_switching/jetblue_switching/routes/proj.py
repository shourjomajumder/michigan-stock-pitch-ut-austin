import os as _os; _D = _os.path.dirname(_os.path.abspath(__file__)); _os.makedirs(_os.path.join(_D, 'out'), exist_ok=True)  # outputs go to out/ next to this script
import numpy as np, matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'serif','font.serif':['EB Garamond','Garamond','DejaVu Serif']})
N,UB,R,G='#0B2265','#1414D2','#C0392B','#E6E6E6'
t=np.arange(0,15);a0=1.5;base=3.14;lo=0.98;hi=5.29;up=5.98
lab=['Jul 26','','','','Nov 26\n(now)','','Jan 27','','','Apr 27','','','Jul 27','','Sep 27']
fig,ax=plt.subplots(figsize=(8.2,5.6))
for s in['top','right']:ax.spines[s].set_visible(False)
ax.axvspan(12,14,color=G,zorder=0);ax.text(13,.35,'Q3 2027',ha='center',fontsize=10.5)
ax.fill_between(t,a0+lo*t/12,a0+hi*t/12,color='#E3EDF9',label='95% range of base case')
ax.plot(t,a0+base*t/12,color=N,lw=2.8,label='Base: loyalty-only rate (3.1% / yr)')
ax.plot(t,a0+up*t/12,color=UB,lw=2.4,ls='--',label='Upside: codeshare-level rate (6.0% / yr)')
need=(10-a0)/13*12
ax.plot([0,13],[a0,10],color=R,lw=1.6,ls=':',label=f'Pace needed for 10% ({need:.1f}% / yr)')
ax.plot(0,a0,'s',ms=10,color='black',zorder=6);ax.text(.3,a0-.75,'Actual: 1.5%',fontsize=10.5)
for y,c,txt in[(a0+base*13/12,N,'Base'),(a0+up*13/12,UB,'Upside'),(10,R,'Our case')]:
    ax.plot(13,y,'o',ms=11,color=c,zorder=6);ax.text(13.35,y,f'{txt}: {y:.1f}%' if y<10 else 'Our case: 10%',fontsize=11,weight='bold',va='center')
ax.set_xticks(t);ax.set_xticklabels(lab,fontsize=9.5);ax.set_xlim(0,16.6);ax.set_ylim(0,11.5)
ax.set_ylabel('JetBlue passengers switched to United (%)',fontsize=12)
ax.set_title('Switching Path From Now to Q3 2027',fontsize=17,weight='bold',pad=12)
ax.legend(frameon=False,loc='upper left',fontsize=10.5)
plt.tight_layout();plt.savefig(_os.path.join(_D, 'out', 'Switching_path_to_Q3_2027.png'),dpi=220)
print(a0+base*13/12,a0+lo*13/12,a0+hi*13/12,a0+up*13/12,need)
