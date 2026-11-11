import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd
T=pd.read_csv(_os.path.join(_R, 'data/air_traffic_dot_bts/raw/t100/t100_bos_jfk_ewr_transcon_monthly_2019_2026.csv')); T['pax']=pd.to_numeric(T.pax,errors='coerce'); T['seats']=pd.to_numeric(T.seats,errors='coerce'); T=T.dropna(subset=['pax','seats'])
g=T.groupby(['route','year','carrier'])[['pax','seats']].sum().unstack('carrier').fillna(0)
ps=g['pax'].div(g['pax'].sum(1),axis=0)*100; ss=g['seats'].div(g['seats'].sum(1),axis=0)*100
pd.set_option('display.width',250)
print('PAX SHARE');print(ps.round(1).to_string());print('SEAT SHARE');print(ss.round(1).to_string())
print(T.groupby(['year']).month.nunique())
