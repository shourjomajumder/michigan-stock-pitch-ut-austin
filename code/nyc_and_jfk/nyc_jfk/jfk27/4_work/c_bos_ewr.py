import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../../..')  # repo root
# Screen BOS/EWR routes 2023 (CY) vs L4Q (2025m8-2026m7): change in rival seat share vs B6 pax share. Universe = AA,B6,DL,UA only (file scope).
import pandas as pd, numpy as np
B=pd.read_csv(_os.path.join(_R, 'data/air_traffic_dot_bts/raw/t100/t100_bos_ewr_routes_B6_UA_AA_DL_2023_2026m7.csv'))
B['ym']=B.year*100+B.month
def win(ym): 
    if 202301<=ym<=202312: return 'Y23'
    if 202508<=ym<=202607: return 'L4Q'
B['w']=B.ym.map(win); B=B[B.w.notna()]
g=B.groupby(['route','w','carrier'])[['pax','seats']].sum().unstack('carrier').fillna(0)
ps=g['pax'].div(g['pax'].sum(1),axis=0)*100; ss=g['seats'].div(g['seats'].sum(1),axis=0)*100
rows=[]
for r in ps.index.get_level_values(0).unique():
    if (r,'Y23') not in ps.index or (r,'L4Q') not in ps.index: continue
    a=ps.loc[(r,'Y23')]; b=ps.loc[(r,'L4Q')]; sa=ss.loc[(r,'Y23')]; sb=ss.loc[(r,'L4Q')]
    if a['B6']<5: continue
    tot=g['seats'].sum(1)
    for riv in ['UA','DL','AA']:
        d=sb[riv]-sa[riv]
        if d>=5:
            rows.append(dict(route=r,rival=riv,rival_seat_sh_pre=round(sa[riv],1),rival_seat_add=round(d,1),B6_pax_pre=round(a['B6'],1),B6_pax_chg=round(b['B6']-a['B6'],1),B6_seat_chg=round(sb['B6']-sa['B6'],1),ratio=round(-(b['B6']-a['B6'])/d,2),tot_seats_chg_pct=round((tot[(r,'L4Q')]/tot[(r,'Y23')]-1)*100,1)))
R=pd.DataFrame(rows); pd.set_option('display.width',250); print(R.to_string())
print('median ratio',R.ratio.median(),'mean',R.ratio.mean().round(2),'n',len(R))
R.to_csv(_os.path.join(_R, 'data/nyc_and_jfk/processed/jfk27/4_work/c_bos_ewr_screen.csv'),index=False)
