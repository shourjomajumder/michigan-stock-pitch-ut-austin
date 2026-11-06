import pandas as pd
SEAT=230; SYS_ASM=11103e6
routes=[('Las Vegas–Oakland','2026-08-20',11,407),('Las Vegas–Boise','2026-09-10',4,520),('Nashville–Tampa','2026-10-09',2,612),
        ('Denver–Fort Lauderdale','2026-11-20',7,1703),('Ontario–Oakland','2026-11-21',4,361),('Orlando–Cartagena','2026-12-19',1,1340)]
curve=[0.55,0.65,0.75,0.85,1.00]
months=pd.period_range('2026-10','2027-12',freq='M'); rows=[]
for name,start,f,dist in routes:
    s=pd.Period(start,'M')
    for m in months:
        if m<s: continue
        age=(m-s).n; idx=curve[min(age//3,4)]
        seats=f*2*SEAT*(30.4/7)*(0.4 if m==s and pd.Timestamp(start).day>15 else 1)
        rows.append(dict(route=name,q=str(m.asfreq('Q')),asm=seats*dist,w=seats*dist*idx))
d=pd.DataFrame(rows); g=d.groupby(['route','q'])[['asm','w']].sum(); g['idx']=g.w/g.asm
t=g.idx.unstack().reindex([r[0] for r in routes]); print((t*100).round(0))
s=d.groupby('q')[['asm','w']].sum(); s['share%']=s.asm/SYS_ASM*100; s['idx']=s.w/s.asm
s['drag_bp']=-(s.asm-s.w)/SYS_ASM*10000  # bp of system RASM (relative, x100 = % )
s['qoq_tail_bp']=s.drag_bp.diff()
print(s[['share%','idx','drag_bp','qoq_tail_bp']].round(2))
