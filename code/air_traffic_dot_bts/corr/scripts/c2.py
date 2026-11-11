import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../..')  # repo root
import csv
rows=[]
def add(c,y,m,v,u): rows.append((c,y,m,v,u))
# BTS domestic (T-100 segment, scheduled enplanements, millions)
R13="https://webarchive.library.unt.edu/web/20161104154015/https://www.rita.dot.gov/bts/press_releases/bts012_14"
for c,a,b in [("DL",98.372,95.439),("WN",115.323,112.234),("UA",65.113,67.534),("AA",65.052,65.010),("B6",25.838,24.871),("AS",17.867,16.747)]:
    add(c,2013,"dom_pax_millions",a,R13); add(c,2012,"dom_pax_millions",b,R13)
P15="https://www.bts.gov/archive/publications/passenger_travel_2015/chapter2/table2_8"
for c,v in [("WN",126.7),("DL",106.2),("AA",66.4),("UA",64.7),("B6",26.4),("AS",19.2)]: add(c,2014,"dom_pax_millions",v,P15)
P16="https://www.bts.gov/archive/publications/passenger_travel_2016/tables/table2_8"
for c,v in [("WN",142.5),("AA",118.1),("DL",115.1),("UA",69.3),("B6",28.8),("AS",21.3),("NK",16.0)]: add(c,2015,"dom_pax_millions",v,P16)
add("NK",2014,"dom_pax_millions",12.6,P16)
R18="https://www.bts.gov/newsroom/2018-traffic-data-us-airlines-and-foreign-airlines-us-flights"
for c,a,b in [("WN",159.045,153.809),("DL",126.473,120.735),("AA",119.471,116.471),("UA",85.896,80.434),("B6",33.965,32.394),("AS",31.493,24.063),("NK",26.319,21.971),("F9",18.669,15.970)]:
    add(c,2018,"dom_pax_millions",a,R18); add(c,2017,"dom_pax_millions",b,R18)
# BTS T-100 Domestic Market table (different basis; not comparable to segment series)
T36="https://www.bts.gov/archive/publications/passenger_travel/chapter3/table3-6"
for c,v in [("WN",110.6),("DL",102.5),("UA",82.8),("AA",75.7),("B6",24.7)]: add(c,2011,"dom_pax_millions_t100market",v,T36)
# BTS system scheduled enplanements (millions)
for c,a,b in [("DL",120.389,116.445),("WN",115.323,112.234),("UA",90.113,92.367),("AA",86.823,86.335),("B6",30.428,28.934),("AS",19.700,18.495)]:
    add(c,2013,"sys_pax_millions_bts",a,R13); add(c,2012,"sys_pax_millions_bts",b,R13)
R16="https://content.govdelivery.com/accounts/USDOT/bulletins/19042ff"
for c,a,b in [("WN",151.7,144.6),("AA",144.2,146.5),("DL",143.1,138.6),("UA",100.1,95.3),("B6",38.2,35.1),("AS",24.4,22.8),("NK",21.0,17.6),("F9",14.8,12.6)]:
    add(c,2016,"sys_pax_millions_bts",a,R16); add(c,2015,"sys_pax_millions_bts",b,R16)
for c,a,b in [("WN",163.606,157.677),("DL",152.029,145.647),("AA",148.181,144.864),("UA",113.197,107.243),("B6",42.236,40.015),("AS",33.503,26.067),("NK",28.683,23.813),("F9",19.433,16.800)]:
    add(c,2018,"sys_pax_millions_bts",a,R18); add(c,2017,"sys_pax_millions_bts",b,R18)
# MIT Airline Data Project, Form 41 T1 system enplaned passengers (thousands -> millions), 2005-2009 only
MIT="https://web.mit.edu/airlinedata/www/2020%2012%20Month%20Documents/Traffic%20and%20Capacity/System%20Total/System%20Total%20Enplaned%20Passengers.htm"
mit={"AA":[98098,98200,98212,92818,85783],"DL":[86105,73655,73051,71728,67852],"UA":[66802,69325,68386,63150,56083],
"WN":[88474,96349,101990,102042,101430],"B6":[14681,18507,21305,21863,22392],"AS":[16759,17165,17559,16809,15561],
"HA":[5840,6204,7099,7857,8345],"G4":[1204,2187,3272,4292,5320],"F9":[7350,8934,10400,10641,9408],"NK":[4508,4527,6903,6820,6089]}
for c,vs in mit.items():
    for y,v in zip(range(2005,2010),vs): add(c,y,"sys_enpl_millions_mit_form41",round(v/1000,3),MIT)
# Wikipedia key-trends tables (company-reported passengers, millions)
W="https://en.wikipedia.org/wiki/"
wk={"WN":("Southwest_Airlines",2015,[118,124,130,134,134,54,99,126,137,140,134]),
"AA":("American_Airlines",2015,[201,198,194,203,215,95,165,199,210,226,224]),
"UA":("United_Airlines",2011,[96,94,91,138,140,143,148,158,162,58,104,144,165,174,181]),
"B6":("JetBlue",2015,[35.1,38.3,40.0,42.1,42.7,14.3,30.1,39.6,42.5,40.5,39.3]),
"NK":("Spirit_Airlines",2010,[7.0,8.5,10.4,12.4,14.3,17.9,21.6,24.2,29.3,34.5,18.4,30.8,38.5,44.1,44.2,32.0]),
"F9":("Frontier_Airlines",2010,[9.3,10.6,10.3,10.2,11.7,12.6,14.8,16.8,19.4,22.7,11.2,20.7,25.5,30.2,33.3,33.2]),
"HA":("Hawaiian_Airlines",2014,[10.2,10.7,11.1,11.5,11.8,11.7,3.4,6.5,10.0,10.9]),
"SY":("Sun_Country_Airlines",2014,[1.6,1.9,1.8,2.5,2.6,3.6,1.7,2.7,3.6,4.1,4.5,4.2]),
"VX":("Virgin_America",2012,[6.2,6.3,6.5,7.0]),
"AS":("Alaska_Air_Group",2009,[15.5,23.3,24.8,25.9,27.4,29.3,31.9,41.9,44.0,45.8,46.7,17.9,32.4,41.5,44.6,49.2,58.6]),
"G4":("Allegiant_Travel_Company",2014,[8.2,9.5,11.1,12.3,13.8,15.0,8.6,13.6,16.8,17.3,16.8,18.5])}
for c,(p,y0,vs) in wk.items():
    for i,v in enumerate(vs): add(c,y0+i,"sys_pax_millions_wiki",v,W+p)
rows.sort(key=lambda r:(r[2],r[0],r[1]))
with open(_os.path.join(_R, "data/air_traffic_dot_bts/corr_ontime_share/c2_pax.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["carrier","year","metric","value","source_url"]); w.writerows(rows)
print(len(rows))
from collections import Counter; print(Counter(r[2] for r in rows))
