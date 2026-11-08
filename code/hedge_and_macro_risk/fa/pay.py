import os as _os; _D = _os.path.dirname(_os.path.abspath(__file__)); _O = _os.path.join(_D, 'out'); _os.makedirs(_O, exist_ok=True)  # script dir / outputs
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np
S='TeX Gyre Pagella'; N='Carlito'
al=['Southwest','American','Delta','United','Alaska','JetBlue']
top=[82.14,84.50,86.30,84.92,76.50,57.53]; y1=[32.62,36.81,38.40,37.10,33.50,26.03]
pt=np.mean(top[:5]); py=np.mean(y1[:5]); print(round(pt,2),round(py,2),round(1-top[5]/pt,3),round(1-y1[5]/py,3))
fig,ax=plt.subplots(figsize=(6.2,3.6),dpi=300); x=np.arange(6); w=0.36
ct=['#595959']*5+['#0B2265']; cy=['#BFBFBF']*5+['#9DB3E0']
b1=ax.bar(x-w/2,top,w,color=ct,label='Top of scale'); b2=ax.bar(x+w/2,y1,w,color=cy,label='Year 1')
for bb,v in list(zip(b1,top))+list(zip(b2,y1)): ax.text(bb.get_x()+bb.get_width()/2,v+1.2,f'${v:.0f}',ha='center',fontsize=7.5,family=N,color='#333')
ax.axvline(4.5,color='#999',lw=0.8,ls=(0,(2,2)))
ax.set_xticks(x); ax.set_xticklabels(al,family=S,fontsize=9); ax.set_ylim(0,100); ax.set_yticks([0,20,40,60,80,100]); ax.set_yticklabels([f'${v}' for v in [0,20,40,60,80,100]],family=N,fontsize=8,color='#555')
for s in ['top','right','left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#BBBBBB'); ax.tick_params(length=0)
ax.legend(prop={'family':S,'size':8.5},frameon=False,loc='upper left',ncol=2)
ax.text(5.45,99,f'~{round((1-top[5]/pt)*100)}% below peers at top of scale\n~{round((1-y1[5]/py)*100)}% below peers at Year 1',family=S,fontsize=8.5,ha='right',va='top')
plt.tight_layout(); fig.savefig(_os.path.join(_O, 'FA_pay_2026.png'),facecolor='white')
