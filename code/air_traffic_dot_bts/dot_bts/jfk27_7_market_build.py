"""Agent 7: JFK-LAX / JFK-SFO (+ EWR-LAX / EWR-SFO context) market by carrier, quarterly 2019Q1-2026Q3(Jul only).
Source: ../raw/t100/t100_panel_jfk_transcon_hub_routes_2019_2026m7.csv (BTS T-100 Domestic Segment, class F,
both directions, quarter rows with <3 deps dropped, minor carriers -> OT). Re-verified Nov 11 2026: 2026Q2 and Jul-2026
cells match a fresh BTS download exactly (7_market_raw.txt). Latest BTS month = July 2026."""
import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd, numpy as np, calendar
P = pd.read_csv(_os.path.join(_R, 'data/air_traffic_dot_bts/raw/t100/t100_panel_jfk_transcon_hub_routes_2019_2026m7.csv'))
P = P[((P.hub=='JFK')&P.x.isin(['LAX','SFO'])) | ((P.hub=='EWR')&P.x.isin(['LAX','SFO']))].copy()
P['route'] = P.hub+'-'+P.x
def days(y,q,partial):
    ms = [7] if partial else range(3*q-2,3*q+1)
    return sum(calendar.monthrange(y,m)[1] for m in ms)
out=[]
for (rt,y,q),g in P.groupby(['route','year','quarter']):
    partial = (y==2026 and q==3)
    d = days(y,q,partial)
    tp, ts, td = g.pax.sum(), g.seats.sum(), g.deps.sum()
    b6 = g[g.carrier=='B6'].pax.sum(); b6s = g[g.carrier=='B6'].seats.sum()
    for _,r in g.iterrows():
        out.append(dict(route=rt, year=y, quarter=q, period_note='Jul 2026 only' if partial else '',
            carrier=r.carrier, passengers=r.pax, seats=r.seats, departures=r.deps,
            load_factor_pct=round(r.pax/r.seats*100,1) if r.seats else np.nan,
            daily_rt_avg=round(r.deps/2/d,2), pax_share_pct=round(r.pax/tp*100,1), seat_share_pct=round(r.seats/ts*100,1),
            route_total_pax=tp, route_total_seats=ts, route_total_deps=td, route_LF_pct=round(tp/ts*100,1),
            B6_pax_share_pct=round(b6/tp*100,1), B6_seat_share_pct=round(b6s/ts*100,1)))
O = pd.DataFrame(out)
order = {'B6':0,'UA':1,'DL':2,'AA':3,'AS':4,'OT':5}
O['o']=O.carrier.map(order); O=O.sort_values(['route','year','quarter','o']).drop(columns='o')
O.to_csv(_os.path.join(_R, 'data/air_traffic_dot_bts/processed/jfk27_7_market.csv'), index=False)
# summaries for md
T = O.drop_duplicates(['route','year','quarter'])
print(T.pivot_table(index=['year','quarter'], columns='route', values='B6_pax_share_pct').to_string())
for rt in ['JFK-LAX','JFK-SFO','EWR-LAX','EWR-SFO']:
    for yrs,lab in [([2019],'2019'),([2025],'2025')]:
        s=O[(O.route==rt)&O.year.isin(yrs)].groupby('carrier')[['passengers','seats','departures']].sum()
        s['LF']=(s.passengers/s.seats*100).round(1); s['share']=(s.passengers/s.passengers.sum()*100).round(1); s['daily_rt']=(s.departures/2/365).round(2)
        print(rt,lab,'total',s.passengers.sum()); print(s.to_string())
u=O[(O.carrier=='UA')&O.route.str.startswith('JFK')]
print(u[['route','year','quarter','passengers','seats','departures','load_factor_pct','daily_rt_avg','pax_share_pct']].to_string())
