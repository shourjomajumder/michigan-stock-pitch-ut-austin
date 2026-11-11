import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../..')  # repo root
import collections, csv
def load(p, scope):
    rows=[]
    for tok in open(p).read().replace('\n',';').split(';'):
        if not tok.strip(): continue
        h,x,c,pax,deps=tok.split(','); rows.append((h,x,c,int(pax),int(deps),scope))
    return rows
R=load(_os.path.join(_R, 'data/nyc_and_jfk/raw/nyc/dom_raw.txt'),'dom')+load(_os.path.join(_R, 'data/nyc_and_jfk/raw/nyc/intl_raw.txt'),'intl')
NYC={'JFK','LGA','EWR','HPN','ISP','SWF'}
R=[r for r in R if r[1] not in NYC and not (r[1]=='PHL')]  # drop intra-NYC and PHL (bus-distance, both tiny)
METRO={'LAX':'LA','BUR':'LA','ONT':'LA','SNA':'LA','LGB':'LA','SFO':'SF','OAK':'SF','SJC':'SF',
       'FLL':'MIA','MIA':'MIA','DCA':'WAS','IAD':'WAS','BWI':'WAS'}
ua=collections.defaultdict(lambda:[0,0,[]]); b6=collections.defaultdict(dict)
scope={}
for h,x,c,p,d,s in R:
    scope[x]=s
    if c=='UA': u=ua[x]; u[0]+=p; u[1]+=d; u[2].append(f"{h}({p})")
    else: b6[x][h]=b6[x].get(h,0)+p
uam=collections.defaultdict(lambda:[0,0,[]])
for x,u in ua.items():
    m=METRO.get(x,x); uam[m][0]+=u[0]; uam[m][1]+=u[1]; uam[m][2]+= [f"{x}:{s}" for s in u[2]]
FLOOR19=['LAX','MCO','SJU','FLL','SFO','BOS','LAS','PBI','TPA','BUF','RDU','JAX','RSW','BQN','PHX','CHS','DEN','SAV','MSY']
out=[]
for x,hs in sorted(b6.items(), key=lambda kv:-sum(kv[1].values())):
    for h,p in sorted(hs.items()):
        strict = x in ua
        m=METRO.get(x,x); metro = m in uam
        u = ua[x] if strict else (uam[m] if metro else [0,0,[]])
        thin = (u[1]<250) if (strict or metro) else ''
        match = 'strict' if strict else ('metro_only' if metro else 'none')
        out.append(dict(route=f"{h}-{x}",nyc_airport=h,dest=x,dest_metro=m,scope=s if (s:=scope[x]) else '',
            b6_pax_L4Q=p, match=match, ua_pax_from_nyc=(u[0] if match!='none' else 0), ua_deps_from_nyc=(u[1] if match!='none' else 0),
            ua_airport=(' '.join(u[2]) if match!='none' else ''), ua_thin_lt250deps=thin,
            in_jfk_top19_floor=(h=='JFK' and x in FLOOR19)))
# include ua_airport detail for strict uses airport-level; fine
with open(_os.path.join(_R, 'data/nyc_and_jfk/processed/nyc/4_full_overlap.csv'),'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
def S(f): return sum(r['b6_pax_L4Q'] for r in out if f(r))
tot=lambda sc: S(lambda r:r['scope']==sc)
print('B6 NYC total dom',tot('dom'),'intl',tot('intl'))
for sc in ['dom','intl']:
  for lab,f in [('strict',lambda r:r['match']=='strict'),('strict_nonthin',lambda r:r['match']=='strict' and not r['ua_thin_lt250deps']),
                ('metro(strict+metro)',lambda r:r['match']!='none'),('metro_nonthin',lambda r:r['match']!='none' and not r['ua_thin_lt250deps']),
                ('JFK strict',lambda r:r['match']=='strict' and r['nyc_airport']=='JFK'),('floor19',lambda r:r['in_jfk_top19_floor'])]:
    print(sc,lab,S(lambda r,f=f:r['scope']==sc and f(r)))
print('--- by NYC airport, dom strict / metro')
for h in ['JFK','LGA','EWR','HPN','ISP']:
    print(h, S(lambda r:r['scope']=='dom' and r['nyc_airport']==h), S(lambda r:r['scope']=='dom' and r['nyc_airport']==h and r['match']=='strict'), S(lambda r:r['scope']=='dom' and r['nyc_airport']==h and r['match']!='none'))
print('--- rows')
for r in out: print(r['scope'],r['route'],r['b6_pax_L4Q'],r['match'],r['ua_pax_from_nyc'],r['ua_deps_from_nyc'],r['ua_thin_lt250deps'],r['in_jfk_top19_floor'])
