import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../..')  # repo root
import csv
U="https://data.transportation.gov/resource/yj5y-b2ir.csv (DOT Consumer Airfare Report Table 6, SODA API; Boston citymarketid 30721)"
# route, pb, pa, (carrierA, shareA_b, shareA_a, fareA_b, fareA_a), (carrierB,...), parity flag, note
R=[
("BOS-BUF","2017Q4","2019Q4",("DL",18.02,29.12,126.56,137.24),("B6",75.00,65.64,128.28,154.48),1,"Delta entered ~2017Q3 (13.8% share at 18.5% discount), then priced within 1.3% of B6; after-gap 11.2%"),
("BOS-PIT","2018Q1","2019Q4",("DL",13.49,31.68,145.69,153.82),("B6",60.27,54.69,145.75,159.38),1,"Fares identical at start (0.05% gap), 3.5% gap at end; Delta share +18.2pts"),
("BOS-TPA","2018Q4","2020Q1",("DL",22.42,21.85,167.62,174.82),("B6",36.78,40.22,180.85,178.55),1,"Gap 7.3% -> 2.1%; JetBlue held/gained, Delta flat (peaked 29.5% in 2019Q3 at 0.4% gap)"),
("BOS-RDU","2017Q1","2019Q4",("DL",42.47,40.60,168.71,182.53),("B6",41.79,37.31,161.62,171.70),1,"Near 50/50 duopoly at parity; both lost a little share, B6 more; only 5 quarters reported with this pair"),
("BOS-RIC","2014Q2","2018Q3",("DL",21.0,29.72,138.43,145.13),("B6",49.0,59.32,141.64,151.36),1,"Both gained (third carrier shrank); B6 +10.3pts vs DL +8.7pts; only 3 quarters reported"),
("BOS-CHS","2015Q2","2019Q2",("DL",11.41,19.20,220.59,199.00),("B6",41.35,55.16,227.34,202.65),1,"Both gained; B6 +13.8pts vs DL +7.8pts; gap 3.1% -> 1.8%"),
("BOS-PBI","2015Q3","2020Q1",("DL",11.39,15.11,179.50,194.21),("B6",68.46,70.32,190.67,197.61),1,"Gap 6.2% -> 1.8%; Delta +3.7pts, B6 +1.9pts"),
("BOS-SAV","2015Q2","2015Q4",("DL",20.40,22.30,206.95,194.09),("B6",52.50,55.72,217.92,200.51),1,"Short window; essentially stable"),
("BOS-ATL","2017Q2","2020Q1",("DL",51.62,72.15,187.94,186.65),("B6",26.08,18.77,121.34,144.42),0,"NOT parity: B6 22-35% cheaper yet lost 7.3pts after 2017 entry; contrast case"),
("BOS-DTW","2014Q2","2020Q1",("DL",64.0,73.20,214.82,188.65),("B6",23.0,21.11,169.08,148.29),0,"NOT parity: B6 ~21% cheaper throughout, share flat/down; Delta hub route"),
("BOS-NYC","2013Q1","2020Q1",("DL",28.0,37.68,250.94,209.10),("B6",24.0,21.91,137.33,170.40),0,"NOT parity: gap narrowed 45% -> 18.5%; Delta +9.7pts, B6 -2.1pts; city-market level (all NYC airports)"),
]
def mo(a,b):
    ya,qa=int(a[:4]),int(a[5]); yb,qb=int(b[:4]),int(b[5]); return ((yb-ya)*4+(qb-qa))*3
rows=[]
for rt,pb,pa,A,B,par,note in R:
    for c,o in ((A,B),(B,A)):
        role="winner" if (c[2]-c[1])>(o[2]-o[1]) else "loser"
        gap=abs(c[3]-o[3])/o[3]*100
        rows.append(["Delta vs JetBlue Boston buildup (%s)"%("fare parity" if par else "non-parity contrast"),rt,c[0],role,pb,pa,c[1],c[2],c[3],c[4],o[3],o[4],round(gap,1),mo(pb,pa),0,U,note])
with open(_os.path.join(_R, "data/jetblue_switching/processed/routes/r04_bos_dl_b6.csv"),"w",newline="") as f:
    w=csv.writer(f)
    w.writerow("case,route,carrier,role,period_before,period_after,share_before_pct,share_after_pct,fare_before_usd,fare_after_usd,rival_fare_before_usd,rival_fare_after_usd,fare_gap_pct,months_elapsed,depth,source_url,note".split(","))
    w.writerows(rows)
print(len(rows))
