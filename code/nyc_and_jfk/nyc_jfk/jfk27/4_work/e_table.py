import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../../..')  # repo root
# Assemble precedent rows; ratio = incumbent share pts lost per pt of rival share added; rel = ratio / incumbent pre-share (1.0 = proportional draw)
import pandas as pd, numpy as np
T1A='DOT Consumer Airfare Report Table 1a (data.transportation.gov tfrh-tu9e), fetched 2026-11-11'
T6=_os.path.join(_R, 'data/air_traffic_dot_bts/raw/dot_car_table6_cases/r05_sea_dl_as.csv')
T6B=_os.path.join(_R, 'data/air_traffic_dot_bts/raw/dot_car_table6_cases/a10_entry_ramp.csv')
T100J=_os.path.join(_R, 'data/nyc_and_jfk/raw/jfk/t100_panel_jfk_transcon_hub_routes_2019_2026m7.csv')
T100B=_os.path.join(_R, 'data/nyc_and_jfk/raw/jfk/t100.csv')
T100C=_os.path.join(_R, 'data/air_traffic_dot_bts/raw/t100/t100_bos_ewr_routes_B6_UA_AA_DL_2023_2026m7.csv')
R=[ # case, route, years, rival, rival_add, incumbent, inc_pre, inc_chg, basis, inc_capacity, clean, source
('United returns to JFK (raw)','JFK-SFO','2019 vs 2021Q3-22Q3','UA',11.25,'B6',28.65,-4.30,'seat','B6 cut (seat sh -4.0)',1,T100J),
('United returns to JFK (DiD vs 5 B6 control routes, ctrl +1.66)','JFK-SFO','same','UA',11.25,'B6',28.65,-5.96,'seat','B6 cut',0,T100J),
('United returns to JFK (raw)','JFK-LAX','2019 vs 2021Q3-22Q3','UA',7.85,'B6',30.01,+0.41,'seat','B6 held (+1.4 seat sh); AS exited -14.5',1,T100J),
('United returns to JFK (DiD)','JFK-LAX','same','UA',7.85,'B6',30.01,-1.25,'seat','B6 held',0,T100J),
('Delta JFK transcon build','JFK-LAX','2010 vs 2019','DL',14.0,'AA',30.5,-10.5,'pax','AA downgauged 168->102 seats/dep (A321T 2014)',1,T1A+' + '+T100J),
('Delta JFK transcon build','JFK-LAX','2010H2 vs 2019','DL',14.0,'B6',13.5,+16.5,'pax','B6 grew (Mint 2014)',1,T1A+' + '+T100J),
('Delta JFK transcon build','JFK-SFO','2010Q1-11Q1 vs 2019','DL',18.4,'AA',24.3,-10.2,'pax','AA downgauged',1,T1A+' + '+T100J),
('Delta JFK transcon build','JFK-SFO','2011Q3-12 vs 2019','DL',18.4,'B6',12.8,+15.9,'pax','B6 grew',1,T1A+' + '+T100J),
('Virgin America enters JFK','JFK-LAX','2007H1 vs 2008','VX',22.75,'AA',52.0,-15.75,'pax','unknown',1,T1A),
('Virgin America + JetBlue enter JFK (approx.)','JFK-SFO','2007Q1 vs 2008','VX+B6',43.0,'AA',43.0,-15.7,'pax','unknown',0,T1A),
('Alaska upgauges JFK-SFO post-merger','JFK-SFO','2019 vs 2023','AS',4.7,'B6',28.7,-2.0,'seat','B6 seat sh -1.0',1,T100J),
('Alaska cuts JFK-SFO (exit-recapture, sign flipped)','JFK-SFO','2023 vs 2025Q3-26m7','AS',-8.2,'B6',26.7,+1.1,'seat','B6 held',1,T100J),
('Delta Boston build (full entry)','BOS-BUF','2017Q2 vs 2019Q4 (k9)','DL',29.1,'B6',76.4,-10.9,'pax','unknown',1,T6B),
('Delta Boston build (full entry)','BOS-PIT','2017Q3 vs 2019Q4 (k8)','DL',31.7,'B6',57.6,-2.8,'pax','unknown',1,T6B),
('Delta Boston build','BOS-RIC','2014Q2 vs 2018Q3','DL',8.7,'B6',49.0,+10.3,'pax','B6 grew',1,'../EXTERNAL_routes/r04_bos_dl_b6.csv (DOT Table 6)'),
('Delta Boston build','BOS-CHS','2015Q2 vs 2019Q2','DL',7.8,'B6',41.35,+13.8,'pax','B6 grew',1,'../EXTERNAL_routes/r04_bos_dl_b6.csv (DOT Table 6)'),
('Delta Boston build','BOS-PBI','2015Q3 vs 2020Q1','DL',3.7,'B6',68.46,+1.9,'pax','unknown',1,'../EXTERNAL_routes/r04_bos_dl_b6.csv (DOT Table 6)'),
('Delta Boston build','BOS-SFO','2019 vs 2024','DL',7.5,'B6',35.3,-0.2,'seat','B6 held',1,T100B),
('Delta Boston build (4-carrier universe)','BOS-SFO','2023 vs 2025Q3-26m7','DL',5.8,'B6',36.5,-1.7,'seat','B6 +3% seats',1,T100C),
('Delta Seattle build','SEA-LAX','2015Q2 vs 2017Q3','DL',9.7,'AS',58.9,-5.7,'pax','unknown',1,T6),
('Delta Seattle build','SEA-SAN','2017Q3 vs 2019Q3','DL',13.4,'AS',58.8,-7.3,'pax','unknown',1,T6),
('Delta Seattle build','SEA-PDX','2014Q4 vs 2019Q4','DL',8.0,'AS',93.0,-7.0,'pax','unknown',1,T6),
('Delta Seattle build','SEA-GEG','2015Q1 vs 2019Q1','DL',14.1,'AS',93.9,-14.0,'pax','unknown',1,T6),
('Delta Seattle build','SEA-BOI','2015Q3 vs 2017Q4','DL',11.6,'AS',82.2,-11.7,'pax','unknown (partly reversed by 2019Q3)',1,T6),
('Delta Seattle build','SEA-PSC','2015Q4 vs 2018Q4','DL',9.7,'AS',90.7,-9.6,'pax','unknown',1,T6),
('Delta Seattle build','SEA-EUG','2017Q3 vs 2019Q1','DL',6.9,'AS',71.9,-6.5,'pax','unknown',1,T6),
('JetBlue enters United EWR hub route','EWR-LAX','2019 vs 2022','B6+NK',20.4,'UA',82.8,-18.7,'seat','UA cut abs. seats -15%',1,T100J),
('JetBlue enters United EWR hub route','EWR-SFO','2019 vs 2022','B6',5.0,'UA',85.5,-3.7,'seat','UA cut abs. seats -17%',1,T100J),
('United adds FLL-SFO (Blue Sky period)','FLL-SFO','2023 vs 2025Q3-26m7','UA',8.1,'B6',67.4,-8.8,'seat','B6 held (+1.7% seats)',1,T100C),
]
D=pd.DataFrame(R,columns=['case','route','years','rival','rival_add','incumbent','inc_pre','inc_chg','basis','inc_capacity','clean','source'])
D['ratio']=(-D.inc_chg/D.rival_add).round(2); D['rel']=(D.ratio/(D.inc_pre/100)).round(2)
pd.set_option('display.width',300); print(D[['case','route','rival_add','incumbent','inc_pre','inc_chg','ratio','rel','inc_capacity']].to_string())
C=D[D.clean==1]
def s(x,lab): print(lab,'n',len(x),'median ratio',x.ratio.median(),'median rel',x.rel.median(),'IQR rel',x.rel.quantile(.25).round(2),x.rel.quantile(.75).round(2))
s(C,'ALL clean')
multi=C[C.inc_pre<70]; s(multi,'multi-carrier (inc pre <70%)')
held=C[C.inc_capacity.str.contains('held')]; s(held,'incumbent held seats')
grew=C[C.inc_capacity.str.contains('grew')]; s(grew,'incumbent grew')
nyc=C[C.route.str.contains('JFK|EWR')]; s(nyc,'NYC airports')
D.to_csv(_os.path.join(_R, 'data/nyc_and_jfk/processed/jfk27/4_precedents.csv'),index=False)
