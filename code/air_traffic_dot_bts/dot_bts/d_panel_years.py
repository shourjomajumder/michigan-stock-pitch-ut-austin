import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd
P=pd.read_csv(_os.path.join(_R, 'data/air_traffic_dot_bts/raw/t100/t100_panel_jfk_transcon_hub_routes_2019_2026m7.csv'))
P=P[P.x.isin(['LAX','SFO'])]
P['per']=P.year.astype(str); P.loc[(P.year==2025)&(P.quarter>=3)|(P.year==2026),'per']='L4Q'
P.loc[(P.year==2025)&(P.quarter<3),'per']='25H1'
g=P.groupby(['hub','x','per','carrier'])[['pax','seats']].sum().unstack('carrier').fillna(0)
ps=(g['pax'].div(g['pax'].sum(1),axis=0)*100).round(1); ss=(g['seats'].div(g['seats'].sum(1),axis=0)*100).round(1)
pd.set_option('display.width',250)
print(pd.concat({'pax':ps,'seat':ss},axis=1).to_string())
print(P[P.per=='L4Q'][['year','quarter']].drop_duplicates().values.tolist())
# pax-seat share gap stats
d=(ps-ss).abs().stack(); print('abs(pax share - seat share): median',d[d>0].median(),'p90',d[d>0].quantile(.9),'max',d.max())
