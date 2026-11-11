import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../..')  # repo root
import csv, math
GS="https://www.nber.org/papers/w11072.pdf (Goolsbee-Syverson 2008 QJE WP, Table II)"
DF="https://myweb.fsu.edu/gfournier/papers/Daraban_Fournier_RTE_2009_Final.pdf (Daraban-Fournier 2008 RTE, Table 2 SAR)"
BCN="https://users.nber.org/~confer/2003/iow03/carlton.pdf (Bamberger-Carlton-Neumann 2004 JLE)"
GA="https://www.k-state.edu/economics/pdfs/websitefiles/gayle/dlconw-october-2007.pdf (Gayle 2008 DL/CO/NW)"
IL="https://economics.brown.edu/sites/default/files/papers/2003-22.pdf (Ito-Lee 2003)"
LIU="https://scispace.com/pdf/the-long-term-impact-of-loyalty-programs-on-consumer-5767edkddx.pdf (Liu 2007 J Marketing)"
LE="https://pubsonline.informs.org/doi/fpi/10.1287/mksc.14.3.G141 (Leone 1995 Marketing Science)"
VZ="https://www.verizon.com/about/node/928919 (Verizon 1Q25 release)"
BK="https://www.bankingexchange.com/news-feed/item/10262-on-average-customers-keep-the-same-checking-account-for-19-years (Bankrate survey 2025)"
HS="https://eprints.whiterose.ac.uk/77193/1/hesss2.pdf (Hess 2008 JATM)"
SZ="https://iaorifors.com/paper/30743 (Suzuki 2000 TR-E abstract)"
LD="https://ideas.repec.org/a/bla/randje/v38y2007i4p1134-1158.html ; https://dspace.mit.edu/handle/1721.1/17626"
rows=[]
def r(case,route,car,eq,k,share,chg,note,src): rows.append([case,route,car,eq,k,share,chg,note,src])
# Goolsbee-Syverson: incumbent passengers ln(Q) and fares ln(P), k relative to t0 (WN at both endpoints)
gsq={-1:0.165,0:0.196,1:0.240,2:0.123,'3to12':0.167}
gsp={-3:-0.142,-1:-0.135,0:-0.186,1:-0.215,2:-0.228,'3to12':-0.277}
for k,v in gsq.items(): r("GS2008 WN entry threat","pooled incumbent routes","incumbent","t0=WN serves both endpoints",k,"",v,"ln(passengers) coef vs t-9..t-12; imprecise/insignificant; supply-side event",GS)
for k,v in gsp.items(): r("GS2008 WN entry threat","pooled incumbent routes","incumbent","t0=WN serves both endpoints",k,"",v,f"ln(fare) coef; share of t+3..12 level={v/-0.277:.0%}",GS)
r("GS2008 actual WN entry","pooled","incumbent","te",0,"",0.267,"ln(passengers) at entry quarter (n.s.)",GS)
r("GS2008 actual WN entry","pooled","incumbent","te","3to12","",0.329,"ln(passengers) te+3..12 (n.s.); fares -0.344; no reversal",GS)
# Daraban-Fournier (magnitudes; signs negative = fare cuts)
for k,v in {0:0.157,1:0.214,2:0.213,3:0.214,'4+':0.205}.items(): r("DF2008 WN entry","pooled","legacy incumbent","entry q",k,"",-v,f"fare coef magnitude; {v/0.214:.0%} of plateau; no decay",DF)
for k,v in {0:0.055,1:0.073,2:0.073,3:0.074,'4+':0.104}.items(): r("DF2008 other-LCC entry","pooled","legacy incumbent","entry q",k,"",-v,f"fare coef; {v/0.104:.0%} of k4+ level; gradual build",DF)
for k,v in {0:0.051,1:0.030,2:0.014,3:0.048,'4+':0.096}.items(): r("DF2008 WN exit","pooled","legacy incumbent","exit q",k,"",v,"fare rebound; ~half of entry cut recovered; mostly n.s. until k4+",DF)
# Alliances / codeshares (single pre/post windows)
r("BCN2004 CO/HP codeshare","pooled alliance city pairs","total","1994Q4",3,"","+6.5% to +7.2%","total traffic vs non-alliance pairs, 1995Q3 vs 1994Q3; fares -7.1 to -8.2%; segments added over following months",BCN)
r("BCN2004 NW/AS codeshare","pooled alliance city pairs","total","1995Q3",4,"","positive n.s.","traffic 1996Q3 vs 1994Q3; fares -5.1 to -6.1%; many segments added over next 2 yrs (phased)",BCN)
r("Gayle2008 DL/CO/NW codeshare","pooled alliance city pairs","partners","2003Q2 (June 2003)",2,"","+19.8% to +24.4%","partners' traffic 2003Q4 vs 2002Q4; total pair traffic +10.7 to +12.3%; already full-size at k=2",GA)
r("Ito-Lee2003 LCC entry","pooled","incumbent","entry q","1to4 avg","","+16.2% O&D pax (median)","4 quarters after vs 4 before; seats +4.0%, fares -15.1%; no quarterly path",IL)
r("Lederman2007/2008 FFP partnerships","airline-airport","partner","late 1990s","n/a","","n/a","effects documented (share up where partner dominant; FFPs >=25% of hub premium; ~5% fare rise) but lag structure NOT verifiable from public sources",LD)
# Loyalty / consumer marketing
r("Liu2007 retail loyalty program","convenience chain","light/moderate buyers","Mar 2002 enrollment","0 (first 3 months)","","largest jump","'most visible jump ... within three months of joining'; then slower continued rise for 24 months; moderate buyers ~2x by month 24",LIU)
r("Leone1995 ad carryover meta","n/a","n/a","n/a","90% within 6-9 months","","lambda_q 0.32-0.46","derived: 0.1=lam^n, n=6..9 months -> lam_m 0.68-0.77, lam_q 0.32-0.46, half-life 1.8-2.7 months",LE)
# Inertia / churn
r("Hess2008 SP air choice","US 2005 SP n=532","n/a","n/a","n/a","","inertia const 1.09 (t~5.7)","118/532 (22%) always kept current trip; FF benefit WTP ~$21; dropping a tier needs ~$31 fare cut",HS)
r("Suzuki2000 OTP-share Markov","US DOT data","n/a","n/a","n/a","","mechanism","delayed pax more likely to switch next trip; OTP moves share via experience not advertising -> adjustment speed set by trip frequency",SZ)
lm=1-0.009; hl=math.log(0.5)/math.log(lm)
r("Telecom churn VZ consumer postpaid phone","US","VZ","1Q25","n/a","",f"0.90%/month",f"derived: annual {1-lm**12:.1%}; cohort half-life {hl:.0f} months ({hl/3:.0f} quarters)",VZ)
r("Banking checking tenure","US","banks","2025","n/a","","19 yr avg tenure (branch); 6 yr online",f"derived (exponential): annual hazard ~{1/19:.1%}; half-life ~{19*math.log(2):.1f} yrs",BK)
# implied adjustment paths F(k)=1-lam^(k+1)
for lam,lab in [(0.30,"fast (WN entry/Leone low)"),(0.45,"central"),(0.65,"slow (other-LCC entry/phased)")]:
    for k in range(0,9):
        r("IMPLIED partial-adjustment path",lab,"loser share loss",f"lambda_q={lam}",k,"",round(1-lam**(k+1),3),"fraction of eventual shift reached by end of event quarter k","derived from rows above")
with open(_os.path.join(_R, "data/jetblue_switching/processed/switch/a8_literature.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow("case,route,carrier,event_quarter,k,share,change_vs_pre,note,source".split(",")); w.writerows(rows)
for lam in (0.3,0.45,0.65):
    k50=next(k for k in range(20) if 1-lam**(k+1)>=0.5); k90=next(k for k in range(20) if 1-lam**(k+1)>=0.9)
    print(lam,k50,k90)
print(len(rows))
