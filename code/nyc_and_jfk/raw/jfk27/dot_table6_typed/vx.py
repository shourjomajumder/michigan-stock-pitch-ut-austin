import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../../..')  # repo root
import numpy as np, csv
nan=np.nan
Q=[f"{y}Q{q}" for y in range(2015,2021) for q in range(1,5)]
S={ # (case-label, route, carrier, measure): 24 quarterly values 2015Q1..2020Q4, nan=not visible in Table 6
('NYC-SFO','UA','large_ms'):[.347757,.346433,.347576,.293452,.277618,.330658,.328667,.339866,.307427,.317266,.317680,.337592,.308287,.328279,.320887,.317529,.311648,.347507,.345562,.342858,.325616,.354614,.375074,.428916],
('NYC-SFO','VX/AS','lf_ms'):[nan,nan,nan,nan,nan,.176180,.172441,.185040,nan,.161007,nan,nan,.127526,.204793,.194188,.207463,.191896,.202069,.208823,.214522,.192361,.267104,.140875,nan],
('NYC-SFO','B6','lf_ms'):[.145225,.154493,.146575,.163876,.167172,nan,nan,nan,.159359,nan,.156974,.149782]+[nan]*12,
('LAX-NYC','UA','large_ms'):[.263292,.277890,.288587,.239578,.223798,.258817,.256956,.257748,.233474,.231834,.233930,.239475,nan,.238876,.253002,.254323,nan,.260093,.249343,.261914,nan,.299980,.309054,.299314],
('LAX-NYC','VX/AS','lf_ms'):[nan]*4+[.169232,.152728,.150384,.165047,.156373,.148205,.136439,.129892,.114222,.158808,.145629,.142528,.125075,.141671,.146493,.141930,.151515,.109360,nan,nan],
('LAX-NYC','B6','large_or_lf'):[.191075,.185345,.178833,.195234]+[nan]*8+[.230020,nan,nan,nan,.255140,nan,nan,nan,.244627,nan,nan,nan],
('BOS-SFO','UA','large_ms'):[.394556,.412426,.386189,.414596,.379709,.383293,.352964,.388517,.357427,.429436,.353437,.372966,nan,.384118,.364048,.360517]+[nan]*7+[.365342],
('BOS-SFO','B6','large_or_lf'):[.229438,.228366,.234152,.227179,.211922,.219119,.241139,.242591,.271801,nan,nan,nan,.352282,nan,nan,nan,.385100,.335512,.329795,.354509,.357832,.376825,.326852,nan],
('BOS-SFO','VX/AS','lf_ms'):[nan]*9+[.123460,nan,.110134,nan,.119165,.117776,.112426,.110959,.103231,nan,.112484,.117351,nan,.115991,nan],
('BOS-LAX','AA','large_ms'):[nan,nan,.274408,.310347,.347114,.302025,.255402,.298893,.317358,.272720,.258598,nan,.330775,.305020,.283091,nan,nan,nan,nan,nan,nan,nan,nan,nan],
('BOS-LAX','B6','large_or_lf'):[.270623,.223804,.213081,.239659,.244581,.210795,.202001,.233454,nan,nan,nan,.276598,.301959,nan,nan,.332697,.358484,.295996,.285819,.333474,.342040,.402910,.459884,.438277],
('BOS-LAX','VX/AS','lf_ms'):[nan]*8+[.104114,.112417,.111989,nan,nan,nan,.109408]+[nan]*9,
('SFO-SEA','AS(+VX from 2018)','large_ms'):[.509576,.479017,.464180,.453865,.512661,.475429,.450783,.473764,.584256,.536096,.499979,.551838,.543326,.583720,.519357,.541962,.587689,.532931,.507785,.534838,.555440,.537392,.550292,.552520],
('SFO-SEA','VX','lf_ms'):[nan]*5+[.109861,.109056]+[nan]*17,
('SFO-SEA','WN','lf_ms'):[nan]*11+[.182460,.186513,.173807,.182217,.184376,.173947,.182869,.179765,.182587,.171944,.267327,.226884,.214675],
('LAX-SFO','WN','large_ms'):[.641201,.647252,.636871,.625692,.627811,.611921,.594567,.613180,.595699,.586777,.579950,.593354,.579055,.550350,.547397,.569984,.588557,.586958,.584376,.591736,.621931,.654912,.649765,.621630],
('LAX-SFO','AS','lf_ms'):[nan]*13+[.111944,.123377,.132293,.131895,.136355,.146640,.139887,.114840,nan,.123248,.159106],
('LAS-SFO','WN','large_ms'):[.558329,.530833,.505812,.511064,.519081,.507407,.488369,.509205,.549875,.516347,.501048,.537103,.555138,.517005,.500645,.529828,.549363,.539755,.511887,.533070,.547077,.752828,.675007,.566104],
('LAS-SFO','VX/AS','lf_ms'):[nan,nan,.217889,.208338,.181411,nan,nan,nan,nan,nan,.159183,.156544,nan,.173076,.161915,.176558,nan,.156500,.158858,.183836,.169645,nan,nan,.134365],
('CHI-SFO','UA','large_ms'):[.401954,.332435,.318287,.358143,.395593,.368665,.376625,.367026,.469815,.426019,.422473,.423664,.459297,.471502,.454955,.449405,.465894,.470068,.433023,.436041,.474599,.382393,.352821,.515221],
('CHI-SFO','VX','lf_ms'):[nan,nan,.124964,.116759,nan,.109952,.111924,.123257]+[nan]*16,
('SFO-WAS','UA','large_ms'):[.449923,.451198,.430785,.439688,.435703,.450446,.420423,.448038,.432414,.426841,.389606,.441669,.435559,.395823,.374049,.452721,.458949,.452832,.426960,.478630,.488215,.359292,.399288,.398091],
}
city={'NYC-SFO':"city1 like 'New York%' AND city2 like '%Francisco%'",'LAX-NYC':"city1 like 'Los Angeles%' AND city2 like 'New York%'",'BOS-SFO':"city1 like 'Boston%' AND city2 like '%Francisco%'",'BOS-LAX':"city1 like 'Boston%' AND city2 like 'Los Angeles%'",'SFO-SEA':"city1 like 'San Francisco%' AND city2 like 'Seattle%'",'LAX-SFO':"city1 like 'Los Ang%' AND city2 like 'San Fr%'",'LAS-SFO':"city1 like 'Las Veg%' AND city2 like 'San Fr%'",'CHI-SFO':"city1 like 'Chicago%' AND city2 like '%Francisco%'",'SFO-WAS':"city1 like 'San Fr%' AND city2 like 'Washington%'"}
EV={'E1_close':Q.index('2017Q1'),'E2_elevate_fold_SOC':Q.index('2018Q1'),'E3_brand_retired':Q.index('2019Q2')}
rows=[]
summ=[]
for (r,c,m),v in S.items():
    v=np.array(v,float); assert len(v)==24,(r,c)
    for en,e in EV.items():
        pre=np.nanmean(v[e-4:e]) if np.isfinite(v[e-4:e]).sum()>=3 else nan
        for k in range(-4,9):
            i=e+k
            if i<0 or i>=24 or not np.isfinite(v[i]): continue
            yoy = v[i]-v[i-4] if i>=4 and np.isfinite(v[i-4]) else nan
            note=f"{m}; Table6 shows carrier only when largest or lowest-fare; yoy_pts={yoy*100:.1f}" if np.isfinite(yoy) else f"{m}; Table6 shows carrier only when largest or lowest-fare"
            if Q[i]>='2020Q1': note+='; COVID quarter, exclude'
            rows.append([en,r,c,Q[i],k,round(v[i]*100,2),round((v[i]-pre)*100,2) if np.isfinite(pre) else '',note,
              "https://data.transportation.gov/resource/yj5y-b2ir.json?$where="+city[r]+" (2015-2020)"])
        if np.isfinite(pre):
            path=[(v[e+k]-pre)*100 if e+k<20 and np.isfinite(v[e+k]) else nan for k in range(0,9)]
            summ.append((en,r,c,round(pre*100,1),[None if np.isnan(x) else round(x,1) for x in path]))
with open(_os.path.join(_R, 'data/air_traffic_dot_bts/raw/dot_car_table6_cases/a4_vx_merge.csv'),'w',newline='') as f:
    w=csv.writer(f); w.writerow(['case','route','carrier','event_quarter','k','share','change_vs_pre','note','source']); w.writerows(rows)
for s in summ: print(s)
