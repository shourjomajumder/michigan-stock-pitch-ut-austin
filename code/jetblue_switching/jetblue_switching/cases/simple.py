import os as _os; _D = _os.path.dirname(_os.path.abspath(__file__)); _os.makedirs(_os.path.join(_D, 'out'), exist_ok=True)  # outputs go to out/ next to this script
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'serif','font.serif':['EB Garamond','Garamond','DejaVu Serif']})
N,R,G='#0B2265','#C0392B','#BFBFBF'
lab=['Better product only\n(Delta vs JetBlue in Boston)','Shared loyalty points\n(JetBlue + United Blue Sky)','Codeshare + loyalty\n(USAir + British Airways)']
v=[0,3.6,8.7];col=[G,R,N]
fig,ax=plt.subplots(figsize=(8.2,5.2))
b=ax.bar(range(3),v,color=col,width=.6)
for i,x in enumerate(v): ax.text(i,x+.25,f'{x:.1f}%' if x else '~0%',ha='center',fontsize=16,weight='bold')
ax.set_xticks(range(3));ax.set_xticklabels(lab,fontsize=11)
ax.set_ylabel('Passengers lost to rival per year',fontsize=12);ax.set_ylim(0,10.5)
for s in['top','right','left']:ax.spines[s].set_visible(False)
ax.set_yticks([])
ax.set_title('How Fast Do Passengers Switch Airlines?',fontsize=17,weight='bold',pad=12)
plt.tight_layout();plt.savefig(_os.path.join(_D, 'out', 'Switching_simple.png'),dpi=220)
