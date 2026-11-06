import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd
SEAT=230; SYS_ASM=11103e6; RASM=0.1187
routes=[('Las Vegas–Oakland','2026-08-20',11,407),('Las Vegas–Boise','2026-09-10',4,520),('Nashville–Tampa','2026-10-09',2,612),
        ('Denver–Fort Lauderdale','2026-11-20',7,1703),('Ontario–Oakland','2026-11-21',4,361),('Orlando–Cartagena','2026-12-19',1,1340)]
curve=[0.55,0.65,0.75,0.85,1.00]
rows=[]
for name,start,f,dist in routes:
    s=pd.Period(start,'M')
    for m in pd.period_range('2026-10','2027-12',freq='M'):
        if m<s: continue
        idx=curve[min((m-s).n//3,4)]
        seats=f*2*SEAT*(30.4/7)*(0.4 if m==s and pd.Timestamp(start).day>15 else 1)
        rows.append(dict(q=str(m.asfreq('Q')),asm=seats*dist,w=seats*dist*idx))
s=pd.DataFrame(rows).groupby('q')[['asm','w']].sum()
s['share']=s.asm/SYS_ASM*100; s['idx']=s.w/s.asm*100
s['rasm_pct']=-(s.asm-s.w)/SYS_ASM*100; s['rasm_c']=s.rasm_pct/100*RASM*100
s['rev']=s.w*RASM/1e6; s['mature']=s.asm*RASM/1e6; s['gap']=s.rev-s.mature; s['qoq']=s.rev.diff()
print(s[['share','idx','rasm_pct','rasm_c','rev','gap','qoq']].round(3)); s.to_csv(_os.path.join(_R, 'data/frontier_routes_and_load_factor/frontier_route_maturity/maturity.csv'))
