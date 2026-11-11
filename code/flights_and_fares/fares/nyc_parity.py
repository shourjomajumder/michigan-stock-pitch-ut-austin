import pandas as pd, numpy as np
import os; R=os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../../data/flights_and_fares'))  # data root
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'out'); os.makedirs(OUT,exist_ok=True)  # output is not in data/processed
J=pd.read_csv(R+'/raw/dot/dot_car_table1a_jfk_ewr_2019_2026q1.csv')
B=pd.read_csv(R+'/raw/dot/dot_car_table1a_bos_ewr_2023_2026q1.csv')
B=B.rename(columns={'passengers':'passengers_per_day'})
A=pd.concat([J,B[J.columns]]).drop_duplicates(['year','quarter','airport_1','airport_2'])
A['q']=A.year*10+A.quarter
A=A[A.q>=20242]  # last 8 quarters max, keep 2024Q2-2026Q1
def fare(r,c):
    if r.carrier_lg==c: return r.fare_lg,'largest'
    if r.carrier_low==c: return r.fare_low,'lowest-fare'
    return np.nan,None
rows=[]
for _,r in A.iterrows():
    ap=[r.airport_1,r.airport_2]; nyc=[a for a in ap if a in('JFK','LGA','EWR')]
    if len(nyc)!=1: continue
    dest=[a for a in ap if a!=nyc[0]][0]
    for c in('B6','UA'):
        f,role=fare(r,c)
        if role: rows.append(dict(q=r.q,year=r.year,quarter=r.quarter,nyc=nyc[0],dest=dest,carrier=c,fare=f,role=role,pax_day=r.passengers_per_day))
F=pd.DataFrame(rows)
b6=F[(F.carrier=='B6')]; ua=F[(F.carrier=='UA')&(F.nyc=='EWR')]
M=b6.merge(ua,on=['q','year','quarter','dest'],suffixes=('_b6','_ua'))
M['type']=np.where(M.nyc_b6=='EWR','Newark same-airport','JFK vs EWR')
M['gap']=(M.fare_b6-M.fare_ua).round(2)
M['within10']=M.gap.abs()<=10
M['quarter_lbl']=M.year.astype(str)+'Q'+M.quarter.astype(str)
M['route_b6']=M.nyc_b6+'-'+M.dest; M['route_ua']='EWR-'+M.dest
out=M[['type','dest','quarter_lbl','route_b6','role_b6','fare_b6','route_ua','role_ua','fare_ua','gap','within10']].sort_values(['type','dest','quarter_lbl'])
out['fare_b6']=out.fare_b6.round(2); out['fare_ua']=out.fare_ua.round(2)
out.to_csv(OUT+'/dot_table1a_nyc_parity.csv',index=False)
print(out.to_string())
for t,g in out.groupby('type'):
    print(t,len(g),'mean',g.gap.mean().round(2),'median',g.gap.median().round(2),'within10',g.within10.sum())
    print(g.groupby('dest').gap.agg(['mean','count']).round(1))
# which 6.147M destinations lack usable pairs
ov=pd.read_csv(R+'/raw/t100_context/4_full_overlap.csv')
print(ov.groupby(['nyc_airport']).b6_pax_L4Q.sum())
used=set(out.dest)
print('covered pax', ov[ov.dest.isin(used)].groupby('nyc_airport').b6_pax_L4Q.sum())
print(ov[ov.nyc_airport.isin(['JFK','LGA','EWR'])].sort_values('b6_pax_L4Q',ascending=False)[['route','b6_pax_L4Q','scope']].head(30).to_string())
# B6 at JFK vs UA EWR where UA not shown
print('UA at EWR shown for dests:',sorted(ua.dest.unique()))
print('B6 at JFK shown for dests:',sorted(b6[b6.nyc=='JFK'].dest.unique()))
