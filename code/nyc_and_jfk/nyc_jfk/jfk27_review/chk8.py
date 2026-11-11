# independent recompute of agent 8 L27Q3_base, LAX+SFO, selected quarters
b6={'LAX':{1:209123,2:242674,3:234185,4:235067},'SFO':{1:116866,2:140845,3:142090,4:127760}}
tot={'LAX':3015438,'SFO':1906792}
days={1:90,2:91,3:92,4:92}
pairs={'LAX':4,'SFO':3}; seats=172; lf=0.825; leak=0.25; fare=180; W=0.10
def sw(k): return 0 if k<1 else min(0.031*(k-0.5)/4,0.06)
L=2027*4+2
for y,q in [(2027,3),(2027,4),(2028,4),(2030,4)]:
    k=y*4+q-1-L+1; capf=0 if k<1 else (0.5 if k==1 else 1)
    totl=0
    for r in b6:
        sh=sum(b6[r].values())/tot[r]; pax=b6[r][q]
        s=pax*(1-W)*sw(k); ua=pairs[r]*2*days[q]*seats*lf*capf; c=ua*(1-leak)*sh
        lost=min(s+c,0.5*pax); totl+=lost
    print(y,q,k,round(totl),round(totl*fare/1e6,3))
# run-rate base pax facing United JFK option and $/share
base=921049+527561
print('JFK base pax',base,'x0.9 incremental',base*0.9,'$/sh @0.138/M full',-0.138*base/1e6,'incr',-0.138*base*0.9/1e6)
print('rule check',0.85/6.147)
