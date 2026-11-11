import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../../..')  # repo root
# Case: United JFK-LAX/SFO 2021Q3-2022Q3 vs JetBlue; T-100 seat shares; DiD vs JetBlue control routes
import pandas as pd, numpy as np
P=pd.read_csv(_os.path.join(_R, 'data/nyc_and_jfk/raw/jfk/t100_panel_jfk_transcon_hub_routes_2019_2026m7.csv'))
J=P[P.hub=='JFK'].copy(); J['yq']=J.year*10+J.quarter
def per(yq):
    if 20191<=yq<=20194: return 'PRE'
    if 20213<=yq<=20223: return 'UA'
    if 20231<=yq<=20244: return 'POST'
J['per']=J.yq.map(per); J=J[J.per.notna()]
g=J.groupby(['x','per','carrier'])[['pax','seats']].sum().unstack('carrier').fillna(0)
tp=g['pax'].sum(1); ts=g['seats'].sum(1)
out=pd.DataFrame({c+'_pax_sh':g['pax'][c]/tp*100 for c in g['pax'].columns})
for c in g['seats'].columns: out[c+'_seat_sh']=g['seats'][c]/ts*100
out['tot_pax']=tp; out['tot_seats']=ts
pd.set_option('display.width',250)
print(out.round(2).to_string())
# DiD: B6 pax share change PRE->UA, treated minus control (route-equal mean)
T=['LAX','SFO']; C=['SEA','LAS','SAN','PHX','SLC']
o=out.reset_index()
def chg(x,col,a='PRE',b='UA'):
    s=o.set_index(['x','per'])[col]; return s[(x,b)]-s[(x,a)]
for col in ['B6_pax_sh','DL_pax_sh','AA_pax_sh','UA_seat_sh','UA_pax_sh','B6_seat_sh']:
    t=[chg(x,col) for x in T]; c=[chg(x,col) for x in C]
    print(col,'treated',np.round(t,2),'ctrl mean',round(np.mean(c),2),'ctrl sd',round(np.std(c,ddof=1),2))
for x in T:
    dB=chg(x,'B6_pax_sh'); dUs=chg(x,'UA_seat_sh'); ctrl=np.mean([chg(c,'B6_pax_sh') for c in C])
    print(x,'raw ratio',round(dB/dUs,3),'DiD ratio',round((dB-ctrl)/dUs,3), 'B6 pre share',round(o.set_index(['x','per']).B6_pax_sh[(x,'PRE')],1))
    # B6 pax share change net of B6 seat share change
    dBs=chg(x,'B6_seat_sh'); print('   B6 seat share chg',round(dBs,2),' pax-minus-seat',round(dB-dBs,2))
