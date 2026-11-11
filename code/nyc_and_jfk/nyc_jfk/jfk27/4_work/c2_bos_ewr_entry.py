import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../../..')  # repo root
# Rival ADDS seats (absolute +>=20%, and +>=3 pts seat share) while B6 holds own seats (abs change within +/-15%). 2023 CY vs L4Q 2025m8-2026m7. Universe AA,B6,DL,UA.
import pandas as pd, numpy as np
B=pd.read_csv(_os.path.join(_R, 'data/air_traffic_dot_bts/raw/t100/t100_bos_ewr_routes_B6_UA_AA_DL_2023_2026m7.csv'))
B['ym']=B.year*100+B.month
B['w']=np.where((B.ym>=202301)&(B.ym<=202312),'Y23',np.where((B.ym>=202508)&(B.ym<=202607),'L4Q',None)); B=B[B.w.notna()]
g=B.groupby(['route','w','carrier'])[['pax','seats']].sum().unstack('carrier').fillna(0)
rows=[]
for r in g.index.get_level_values(0).unique():
    if (r,'Y23') not in g.index or (r,'L4Q') not in g.index: continue
    pa,pb=g['pax'].loc[(r,'Y23')],g['pax'].loc[(r,'L4Q')]; sa,sb=g['seats'].loc[(r,'Y23')],g['seats'].loc[(r,'L4Q')]
    if sa['B6']<20000: continue
    b6abs=sb['B6']/sa['B6']-1
    if abs(b6abs)>0.15: continue
    for riv in ['UA','DL','AA']:
        if sa[riv]<=0 and sb[riv]<20000: continue
        add=(sb[riv]/sa[riv]-1) if sa[riv]>0 else np.inf
        dsh=(sb[riv]/sb.sum()-sa[riv]/sa.sum())*100
        if add>=0.20 and dsh>=3:
            b6p0=pa['B6']/pa.sum()*100; b6p1=pb['B6']/pb.sum()*100
            rows.append(dict(route=r,rival=riv,rival_seats_abs_chg_pct=round(add*100,0) if np.isfinite(add) else 'new',rival_seat_sh_pre=round(sa[riv]/sa.sum()*100,1),rival_seat_sh_add=round(dsh,1),B6_seats_abs_chg_pct=round(b6abs*100,1),B6_pax_sh_pre=round(b6p0,1),B6_pax_sh_chg=round(b6p1-b6p0,1),ratio=round(-(b6p1-b6p0)/dsh,2),ratio_over_B6pre=round(-(b6p1-b6p0)/dsh/(b6p0/100),2)))
R=pd.DataFrame(rows); pd.set_option('display.width',250); print(R.to_string())
print('n',len(R),'median ratio',R.ratio.median(),'median rel',R.ratio_over_B6pre.median())
R.to_csv(_os.path.join(_R, 'data/nyc_and_jfk/processed/jfk27/4_work/c2_entry_screen.csv'),index=False)
