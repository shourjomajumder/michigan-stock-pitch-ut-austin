import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import pandas as pd, numpy as np
o=pd.read_csv(__import__('os').environ.get('C1_ONTIME', _os.path.join(_R, 'data/air_traffic_dot_bts/raw/atcr/c1_ontime.csv'))).pivot_table(index='year',columns='carrier',values='value')
s=pd.read_csv(_os.path.join(_R, 'data/air_traffic_dot_bts/corr_ontime_share/c5_share.csv'));s=s[s.metric=='dom_share_rpm_pct'].pivot_table(index='year',columns='carrier',values='value')
a=pd.read_csv(_os.path.join(_R, 'data/air_traffic_dot_bts/corr/c3_acsi.csv'));a=a[a.metric=='acsi'].pivot_table(index='year',columns='carrier',values='value')
merge={('DL',2009),('UA',2011),('AA',2014),('AA',2015),('AS',2017),('VX',2017),('UA',2009),('DL',2008)}
rows=[]
for y in range(2005,2019):
  if y not in o.index or y+1 not in s.index: continue
  avg=o.loc[y].mean()
  for c in o.columns:
    if (c,y) in merge: continue
    if pd.notna(o.loc[y,c]) and c in s and pd.notna(s.loc[y,c]) and pd.notna(s.loc[y+1,c]):
      rows.append(dict(c=c,y=y,gap=o.loc[y,c]-avg,chg=(s.loc[y+1,c]/s.loc[y,c]-1)*100))
d=pd.DataFrame(rows)
for name,sub in [('all',d),('no ULCC',d[~d.c.isin(['NK','F9','G4'])]),('legacy+B6+WN+AS',d[d.c.isin(['AA','DL','UA','B6','WN','AS'])])]:
  r=np.corrcoef(sub.gap,sub.chg)[0,1];b=np.polyfit(sub.gap,sub.chg,1)
  print(name,len(sub),'r=%.2f slope=%.2f int=%.2f'%(r,b[0],b[1]))
d.to_csv(_os.path.join(_R, 'data/air_traffic_dot_bts/corr_ontime_share/panel_ontime.csv'),index=False)
print(d.sort_values('chg').to_string())
print('----')
sub=d[d.c.isin(['AA','DL','UA','B6','WN','AS','VX'])]
r=np.corrcoef(sub.gap,sub.chg)[0,1];b=np.polyfit(sub.gap,sub.chg,1);print('ex HA/ULCC',len(sub),r,b)
# 2-year forward
rows=[]
for y in range(2005,2018):
  if y not in o.index: continue
  avg=o.loc[y].mean()
  for c in ['AA','DL','UA','B6','WN','AS','VX']:
    if any((c,yy) in merge for yy in (y,y+1)): continue
    if c in o and pd.notna(o.loc[y,c]) and y+2 in s.index and pd.notna(s.loc[y,c]) and pd.notna(s.loc[y+2,c]):
      rows.append(dict(c=c,y=y,gap=o.loc[y,c]-avg,chg=(s.loc[y+2,c]/s.loc[y,c]-1)*100))
d2=pd.DataFrame(rows);r=np.corrcoef(d2.gap,d2.chg)[0,1];b=np.polyfit(d2.gap,d2.chg,1);print('2yr',len(d2),r,b)
# ACSI
rows=[]
for y in range(2006,2019):
  if y not in a.index: continue
  avg=a.loc[y].dropna().mean()
  for c in ['AA','DL','UA','B6','WN','AS','NK','F9','G4']:
    if (c,y) in merge or c not in a: continue
    if pd.notna(a.loc[y,c]) and y+1 in s.index and pd.notna(s.loc[y,c]) and pd.notna(s.loc[y+1,c]):
      rows.append(dict(c=c,y=y,gap=a.loc[y,c]-avg,chg=(s.loc[y+1,c]/s.loc[y,c]-1)*100))
d3=pd.DataFrame(rows);r=np.corrcoef(d3.gap,d3.chg)[0,1];b=np.polyfit(d3.gap,d3.chg,1);print('acsi',len(d3),r,b)
s3=d3[~d3.c.isin(['NK','F9','G4'])];print('acsi exULCC',len(s3),np.corrcoef(s3.gap,s3.chg)[0,1],np.polyfit(s3.gap,s3.chg,1))
