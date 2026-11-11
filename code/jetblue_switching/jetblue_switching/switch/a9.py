import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../..')  # repo root
import csv, numpy as np
T6="https://data.transportation.gov/resource/yj5y-b2ir.csv (DOT Table 6)"
def Q(y,q): return y*4+q-1
def lab(i): return f"{i//4}Q{i%4+1}"
# raw rows: (y,q,lg,lgms,low,lfms)
R={}
def add(case,route,carrier,start,rows):
    s={}
    for i,(lg,a,lo,b) in enumerate(rows):
        t=start+i
        s[t]= a if lg==carrier else (b if lo==carrier else np.nan)
    R[(case,route,carrier)]=s
# WN meltdown, 2021Q1..2024Q4
W=Q(2021,1)
add('WN_Dec2022_meltdown','CHI-WAS','WN',W,[('WN',.3701,'WN',.3701),('WN',.4014,'WN',.4014),('WN',.3988,'WN',.3988),('UA',.3801,'WN',.3680),('UA',.3733,'WN',.3546),('WN',.3799,'WN',.3799),('WN',.3701,'WN',.3701),('UA',.3742,'WN',.3625),('UA',.3956,'WN',.3354),('UA',.3667,'WN',.3639),('UA',.3986,'WN',.3688),('UA',.4336,'WN',.3670),('UA',.4530,'WN',.3388),('UA',.4183,'WN',.3740),('UA',.4244,'WN',.3503),('UA',.4259,'WN',.3400)])
add('WN_Dec2022_meltdown','CHI-DFW','WN',W,[('AA',.4855,'WN',.3765),('AA',.4599,'WN',.4042),('AA',.4656,'WN',.3839),('AA',.4335,'WN',.3881),('AA',.4226,'WN',.3785),('WN',.3934,'WN',.3934),('WN',.3681,'WN',.3681),('WN',.3756,'WN',.3756),('AA',.3506,'WN',.3251),('WN',.3594,'WN',.3594),('WN',.3819,'WN',.3819),('WN',.3759,'WN',.3759),('WN',.3519,'WN',.3519),('WN',.3590,'WN',.3590),('AA',.3584,'F9',.1074),('AA',.3672,'F9',.1118)])
add('WN_Dec2022_meltdown','CHI-MCO','WN',W,[('WN',x,'',0) for x in [.3758,.3719,.4057,.3551,.3372,.3340,.3784,.3043,.3203,.3678,.3764,.3683,.3569,.3839,.3545]]+[('UA',.3196,'F9',.1108)])
add('WN_Dec2022_meltdown','DEN-LAX','WN',W,[('WN',x,'',0) for x in [.5142,.5044,.4784,.4803,.4844,.4847,.4694,.4360,.4292,.4312,.4412,.4489,.4788,.4478,.4241,.4039]])
add('WN_Dec2022_meltdown','MCO-WAS','WN',W,[('WN',x,'',0) for x in [.4894,.4768,.4626,.4140,.3950,.3305,.3569,.3326,.3574,.3705,.3639,.3505,.3572,.3638,.3407,.3310]])
add('WN_Dec2022_meltdown','AUS-LAX','WN',W,[('DL',.2834,'B6',.1226),('AA',.2736,'WN',.2658),('AA',.3104,'AA',.3104),('AA',.3034,'DL',.1779)]+[('WN',x,'',0) for x in [.3500,.3922,.3880,.3763,.3747,.3787,.3885,.4340,.4206,.4426,.4191,.4788]])
add('WN_Dec2022_meltdown','CHI-PHX','WN',W,[('WN',.3656,'WN',.3656),('WN',.3881,'WN',.3881),('AA',.3973,'WN',.3677),('AA',.3870,'WN',.3413),('AA',.3790,'WN',.3156),('WN',.3792,'WN',.3792),('WN',.4097,'F9',.1051)]+[('WN',x,'',0) for x in [.3751,.3458,.4015,.4178,.3808,.3645,.4132,.3955,.3555]])
# DL CrowdStrike, 2023Q1..2026Q1
D=Q(2023,1)
add('DL_Jul2024_CrowdStrike','ATL-NYC','DL',D,[('DL',x,'',0) for x in [.5145,.5157,.4946,.4840,.5239,.4810,.4751,.4996,.5389,.5459,.5069,.4851,.5156]])
add('DL_Jul2024_CrowdStrike','ATL-WAS','DL',D,[('DL',x,'',0) for x in [.5562,.4990,.4629,.4269,.4736,.4595,.4736,.4684,.5005,.4747,.4586,.4756,.5209]])
add('DL_Jul2024_CrowdStrike','ATL-CHI','DL',D,[('DL',x,'',0) for x in [.3699,.3616,.3540,.3318,.3654,.3862,.3669,.3823,.3799,.3591,.3599,.3489,.3764]])
add('DL_Jul2024_CrowdStrike','ATL-DFW','DL',D,[('DL',x,'',0) for x in [.3748,.3843,.4044,.3665,.3654,.3689,.3755,.3662,.3835,.3655,.3767,.3762,.3842]])
add('DL_Jul2024_CrowdStrike','ATL-HOU','DL',D,[('DL',x,'',0) for x in [.4254,.3964,.3891,.3797,.3837,.4241,.4052,.3738,.3779,.3741,.3692,.3677,.3740]])
# AA 2016-18 ops problems, CHI-DFW 2015Q1..2019Q4
add('AA_2016_2018_ops','CHI-DFW','AA',Q(2015,1),[('AA',x,'',0) for x in [.4513,.4790,.5344,.5605,.5266,.4825,.4637,.4989,.4625,.4783,.4674,.4868,.5035,.4968,.4738,.5084,.5207,.5153,.4746,.4971]])
# B6 at BOS vs DL, 2019Q1..2026Q1 (B6 observed share)
B=Q(2019,1)
bra=[('B6',.4639,'B6',.4639),('B6',.4312,'B6',.4312),('B6',.3920,'B6',.3920),('DL',.4060,'B6',.3731),('DL',.4449,'B6',.3734),('B6',.4958,'WN',.1914),('B6',.4525,'WN',.1268),('DL',.3960,'B6',.3819),('DL',.4589,'B6',.3463),('DL',.4811,'DL',.4811),('DL',.4843,'B6',.3366),('DL',.4591,'B6',.3280),('DL',.4743,'B6',.3363),('DL',.4155,'B6',.3832),('DL',.4019,'B6',.3965),('DL',.4214,'B6',.3883),('DL',.4317,'B6',.3997),('DL',.4450,'B6',.3315),('B6',.4136,'B6',.4136),('B6',.3805,'B6',.3805),('DL',.4407,'B6',.3006),('DL',.4157,'B6',.2798),('DL',.3810,'B6',.3342),('B6',.3847,'B6',.3847),('DL',.4531,'B6',.3534),('DL',.3787,'B6',.3713),('DL',.4250,'B6',.2791),('DL',.3839,'B6',.3573),('DL',.4715,'MX',.1211)]
add('B6_reliability_vs_DL_BOS','BOS-RDU','B6',B,bra)
add('B6_reliability_vs_DL_BOS','BOS-RDU','DL',B,bra)
bat=[('DL',.6007,'B6',.2378),('DL',.6551,'B6',.2142),('DL',.6604,'B6',.2287),('DL',.7194,'B6',.1854),('DL',.7215,'B6',.1877),('DL',.6031,'AA',.1280),('DL',.6644,'B6',.1229),('DL',.7055,'B6',.1086),('DL',.6911,'B6',.1170),('DL',.7507,'B6',.1187),('DL',.7884,'B6',.1150),('DL',.7926,'B6',.1251),('DL',.7670,'B6',.1438),('DL',.7425,'F9',.0190),('DL',.7392,'B6',.1019),('DL',.7273,'B6',.1242),('DL',.6223,'B6',.2215),('DL',.6647,'B6',.1710),('DL',.6344,'B6',.1952),('DL',.6256,'B6',.1833),('DL',.6189,'NK',.1030),('DL',.6570,'NK',.1018),('DL',.6290,'NK',.1074),('DL',.6161,'NK',.1031),('DL',.6377,'B6',.1855),('DL',.6183,'B6',.2146),('DL',.6510,'B6',.2146),('DL',.6445,'B6',.1959),('DL',.6528,'B6',.1762)]
add('B6_reliability_vs_DL_BOS','BOS-ATL','DL',B,bat)
add('B6_reliability_vs_DL_BOS','BOS-ATL','B6',B,bat)
bny=[('DL',.2956,'B6',.2426),('DL',.3062,'B6',.2368),('DL',.3139,'B6',.2543),('DL',.3526,'B6',.2448),('DL',.3768,'B6',.2191),('DL',.3892,'B6',.3114),('DL',.4034,'UA',.2644),('DL',.4158,'UA',.3185),('DL',.3514,'UA',.3470),('B6',.3353,'B6',.3353),('UA',.3204,'UA',.3204),('B6',.3139,'B6',.3139),('DL',.3560,'B6',.3333),('DL',.3581,'B6',.3148),('DL',.3751,'B6',.3340),('DL',.3794,'B6',.2877),('DL',.3998,'B6',.2584),('DL',.4054,'B6',.2476),('UA',.3458,'B6',.2569),('UA',.3355,'B6',.2931),('DL',.3780,'B6',.2641),('DL',.3667,'B6',.2598),('DL',.3430,'B6',.2713),('DL',.3315,'B6',.2552),('DL',.4104,'B6',.1907),('DL',.4647,'B6',.1880),('DL',.4422,'B6',.1587),('DL',.3930,'B6',.1523),('DL',.4454,'AA',.1633)]
add('B6_reliability_vs_DL_BOS','BOS-NYC','B6',B,bny)
add('B6_reliability_vs_DL_BOS','BOS-NYC','DL',B,bny)
EV={'WN_Dec2022_meltdown':(Q(2022,4),None),'DL_Jul2024_CrowdStrike':(Q(2024,3),None),'AA_2016_2018_ops':(Q(2016,1),None),'B6_reliability_vs_DL_BOS':(Q(2022,1),Q(2019,1))}
rows=[];summ={}
for (case,route,car),s in R.items():
    e,prestart=EV[case]
    ps=prestart if prestart is not None else e-4
    pre=np.nanmean([s.get(t,np.nan) for t in range(ps,ps+4)])
    yo={}
    for t in sorted(s):
        k=t-e
        if k<-4: continue
        v=s[t]; yoy=v-s.get(t-4,np.nan)
        if k>=0: yo[k]=yoy
        note=f"yoy {yoy*100:+.1f}pp" if not np.isnan(yoy) else "yoy n/a"
        if case.startswith('B6'): note+="; pre=2019 avg (2021 COVID-distorted)"
        rows.append([case,route,car,lab(e),k,'' if np.isnan(v) else round(v*100,1),'' if np.isnan(v) else round((v-pre)*100,1),note,T6])
    summ[(case,route,car)]=(pre,yo)
with open(_os.path.join(_R, 'data/jetblue_switching/processed/switch/a9_reliability.csv'),'w',newline='') as f:
    w=csv.writer(f);w.writerow(['case','route','carrier','event_quarter','k','share','change_vs_pre','note','source']);w.writerows(rows)
for key,(pre,yo) in summ.items():
    print(key, f"pre {pre*100:.1f}", ' '.join(f"k{k}:{v*100:+.1f}" for k,v in yo.items() if not np.isnan(v)))
# WN panel average yoy
for case in EV:
    ks={}
    for key,(pre,yo) in summ.items():
        if key[0]!=case: continue
        if case.startswith('B6') and key[2]!='B6': continue
        for k,v in yo.items():
            if not np.isnan(v): ks.setdefault(k,[]).append(v)
    print(case,' '.join(f"k{k}:{np.mean(v)*100:+.1f}(n{len(v)})" for k,v in sorted(ks.items())))
