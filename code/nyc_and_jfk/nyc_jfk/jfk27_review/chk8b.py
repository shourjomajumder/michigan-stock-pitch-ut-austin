b6={'LAX':{1:209123,2:242674,3:234185,4:235067},'SFO':{1:116866,2:140845,3:142090,4:127760}}
tot={'LAX':3015438,'SFO':1906792}; days={1:90,2:91,3:92,4:92}
pairs={'LAX':4,'SFO':3}; par={'LAX':0.5,'SFO':1.0}; fare={'LAX':167.5,'SFO':166.5}
def sw(k): return 0 if k<1 else min(0.031*(k-0.5)/4,0.06)
L=2027*4+2; ann={}
for y in range(2027,2031):
  for q in (1,2,3,4):
    k=y*4+q-1-L+1; capf=0 if k<1 else (0.5 if k==1 else 1); rev=0; lp=0
    for r in b6:
        sh=sum(b6[r].values())/tot[r]; pax=b6[r][q]
        s=pax*(par[r]-0.1)*sw(k); c=pairs[r]*2*days[q]*172*capf*0.825*0.75*sh
        lp+=s+c; rev+=(s+c)*fare[r]/1e6
    ann[y]=ann.get(y,0)+rev
    if (y,q) in [(2027,3),(2027,4),(2028,1),(2030,4)]: print(y,q,round(lp),round(rev,3))
print({k:round(v,2) for k,v in ann.items()})
# $/share cross-checks
t1_per_M_rev=0.320354/(2.316*0.06*180)   # $/share per $1M run-rate revenue
print('per $1M run-rate rev',t1_per_M_rev,'T2 implied',35.08*t1_per_M_rev)
print('pax-equiv: 210k/0.06=',0.21/0.06,'M ->',-0.138*0.21/0.06,'fare adj',-0.138*0.21/0.06*167/180)
print('switch-only 2030 rev 8.45 ->',-8.45*t1_per_M_rev, ' base-pax view 0.843M ->',-0.138*0.843*167/180)
print('weighted w/ P=0.6 and switch-only base:',0.6*0.439)
