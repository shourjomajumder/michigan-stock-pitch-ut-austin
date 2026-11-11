import json, numpy as np, csv, sys
import os as _os; _D = _os.path.dirname(_os.path.abspath(__file__)); _R = _os.path.join(_D, '../../../..')  # repo root
# defaults when run without args: input = raw Table 6 pull, output = out/ next to this script
_IN = sys.argv[1] if len(sys.argv) > 1 else _os.path.join(_R, 'data/jetblue_switching/raw/dot_table6/a1_delta_alaska_t6.json')
if len(sys.argv) > 2: _OUT = sys.argv[2]
else: _os.makedirs(_os.path.join(_D, 'out'), exist_ok=True); _OUT = _os.path.join(_D, 'out', 'a1_delta_alaska.csv')
d = json.load(open(_IN))
Q = [(y, q) for y in range(2010, 2020) for q in range(1, 5)]
idx = {yq: i for i, yq in enumerate(Q)}
def as_share(rows):
    out = []
    for r in rows.split(';'):
        lg, lms, lo, lfm = r.split(',')
        v = float(lms) if lg == 'AS' else (float(lfm) if lo == 'AS' else np.nan)
        out.append(100 * v)
    return np.array(out)
# event = first quarter of Delta nonstop (quarter of start date; next quarter if <15 days left)
EV = {  # route: (event yq, group, launch note, eventual window k)
 'SFO': ((2014,2),'big','6 daily E175 from 2014-03-29 (3 days in Q1 -> k0=Q2), 7 daily Jun-2014',(8,10)),
 'SAN': ((2014,2),'big','4 daily CRJ900 from 2014-06-02',(9,12)),
 'PDX': ((2014,3),'big','4 daily CRJ900 from 2014-09-02',(9,12)),
 'GEG': ((2014,4),'big','4 daily CRJ700 from 2014-11-03',(9,12)),
 'PHX': ((2015,1),'big','5 daily 76-seat from 2014-12-20 (12 days in Q4 -> k0=2015Q1)',(9,12)),
 'BOI': ((2015,2),'big','4 daily from 2015-05-04',(9,12)),
 'SMF': ((2015,2),'big','4 daily from 2015-05-04',(9,12)),
 'DEN': ((2015,2),'big','5 daily from 2015-06-04',(9,12)),
 'PSC': ((2015,4),'big','3 daily CRJ700 from 2015-11-01 (into a 99% AS monopoly)',(9,12)),
 'EUG': ((2017,2),'big','3 daily CRJ700 from 2017-04-01 (into a 98% AS monopoly)',(8,10)),
 'LAX': ((2013,2),'slow','3 daily CRJ900 from 2013-04-08, 7 daily by 2014-06-05',(9,12)),
 'LAS': ((2014,1),'slow','1 daily pre-2014 (start unseen) -> 3 daily 2014-01-06 -> 5 daily 2014-04-01',(9,12)),
 'AUS': ((2017,2),'slow','1 daily A319 from 2017-06-12',(8,10)),
 'ORD': ((2017,2),'slow','3 daily A319 from 2017-06-19 (year per aviation24 URL)',(8,10)),
}
SRC = {'t6': 'https://data.transportation.gov/resource/yj5y-b2ir.csv (DOT Consumer Airfare Report Table 6, city2=Seattle WA)',
 'SFO':'https://worldairlinenews.com/2013/10/01/delta-to-expand-seattletacoma-operations-with-new-flights-to-las-vegas-los-angeles-and-san-francisco/',
 'LAS':'https://worldairlinenews.com/2013/10/01/delta-to-expand-seattletacoma-operations-with-new-flights-to-las-vegas-los-angeles-and-san-francisco/',
 'SAN':'https://prnewswire.com/news-releases/delta-continues-to-build-seattle-market-with-new-and-additional-service-230673171.html',
 'PDX':'https://prnewswire.com/news-releases/delta-continues-to-build-seattle-market-with-new-and-additional-service-230673171.html',
 'GEG':'https://worldairlinenews.com/2014/05/22/delta-continues-to-add-seattletacoma-routes-this-time-to-calgary-and-spokane/',
 'PHX':'https://worldairlinenews.com/2014/02/10/delta-adds-even-more-feeder-routes-to-seattletacoma/',
 'BOI':'https://worldairlinenews.com/2014/11/20/delta-continues-its-seattletacoma-expansion-announces-5-new-routes/',
 'SMF':'https://worldairlinenews.com/2014/11/20/delta-continues-its-seattletacoma-expansion-announces-5-new-routes/',
 'DEN':'https://worldairlinenews.com/2014/11/20/delta-continues-its-seattletacoma-expansion-announces-5-new-routes/',
 'PSC':'https://prnewswire.com/news-releases/delta-adds-boston-orlando-victoria-and-pasco-service-from-seattle-300088631.html',
 'EUG':'https://www.aviationpros.com/airports/press-release/12294414/delta-air-lines-delta-kicks-off-fifth-consecutive-year-of-growth-in-seattle-with-seven-new-destinations',
 'AUS':'https://www.aviationpros.com/airports/press-release/12294414/delta-air-lines-delta-kicks-off-fifth-consecutive-year-of-growth-in-seattle-with-seven-new-destinations',
 'LAX':'https://benzinga.com/z/3213454',
 'ORD':'https://www.travelagentcentral.com/transportation/delta-to-add-new-flights-to-chicago-from-seattle'}
VXFLAG = {'SFO','LAX','SAN','LAS'}
rows = []; paths = {}
for r,(ev,g,note,win) in EV.items():
    s = as_share(d[r]); e = idx[ev]
    pre_q = s[e-4:e]; pre = np.nanmean(pre_q)
    yoy = []  # change vs same quarter of pre-event year (seasonality removed)
    for k in range(-4, 13):
        i = e + k
        if i >= len(s): yoy.append(np.nan); continue
        base = s[e - 4 + (k % 4)]
        yoy.append(s[i] - (base if not np.isnan(base) else pre))
    yoy = np.array(yoy)  # index k+4
    chg = np.array([s[e+k]-pre if e+k < len(s) else np.nan for k in range(-4,13)])
    paths[r] = (g, pre, chg, yoy, win)
    for k in range(-4, 13):
        i = e + k
        if i >= len(s): continue
        y, q = Q[i]
        n = []
        if r in VXFLAG and (y, q) >= (2017, 1): n.append('AS share may include Virgin America after merger (Dec 2016)')
        if (y, q) >= (2017, 2): n.append('after DL-AS partnership end (May 2017)')
        if np.isnan(s[i]): n.append('AS not largest or lowest-fare carrier: share not reported')
        if k == 0: n.append('Delta launch: ' + note)
        rows.append([ 'Delta entry SEA vs Alaska (a1_delta_alaska)', 'SEA-'+r, 'AS', f'{ev[0]}Q{ev[1]}', k,
            '' if np.isnan(s[i]) else round(s[i],2), '' if np.isnan(chg[k+4]) else round(chg[k+4],2),
            f'group={g}; yoy_vs_same_q_pre_year={"" if np.isnan(yoy[k+4]) else round(yoy[k+4],2)}; ' + '; '.join(n),
            SRC['t6'] + ' ; launch: ' + SRC[r]])
with open(_OUT, 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['case','route','carrier','event_quarter','k','share','change_vs_pre','note','source']); w.writerows(rows)

def timing(p, win):
    # loss = -change; smooth with centered 3q mean of yoy series; eventual = mean over window
    loss = -p
    ev = np.nanmean(loss[win[0]+4:win[1]+5])
    sm = np.array([np.nanmean(loss[max(0,j-1):j+2]) for j in range(len(loss))])
    fr = sm / ev
    k_of = lambda t: next((j-4 for j in range(4, len(fr)) if fr[j] >= t), None)
    first = next((j-4 for j in range(4, len(loss)) if loss[j] >= 2.0), None)  # first quarter loss >=2pp
    return ev, k_of(0.5), k_of(0.9), first, fr
print(f"{'route':5} grp  pre   loss k0  k1  k2  k4  k8  k12 | eventual 50% 90% first>=2pp  peak_k")
res = {}
for r,(g,pre,chg,yoy,win) in paths.items():
    ev, k50, k90, first, fr = timing(yoy, win)
    loss = -yoy
    pk = int(np.nanargmax(loss[4:]))
    res[r] = (g, ev, k50, k90, first, pk, pre)
    L = lambda k: f"{loss[k+4]:5.1f}" if not np.isnan(loss[k+4]) else "  nan"
    print(f"{r:5} {g:4} {pre:5.1f} {L(0)} {L(1)} {L(2)} {L(4)} {L(8)} {L(12)} | {ev:5.1f}  {k50}  {k90}  {first}  {pk}")
for g in ['big','slow']:
    rs = [r for r in paths if paths[r][0]==g]
    M = np.nanmean(np.array([-paths[r][3] for r in rs]), axis=0)
    ev = np.nanmean(M[9+4:12+5]); ev2=np.nanmean(M[8+4:10+5])
    sm = np.array([np.nanmean(M[max(0,j-1):j+2]) for j in range(len(M))])
    fr = sm/ev
    k50 = next((j-4 for j in range(4,len(fr)) if fr[j]>=.5),None); k90=next((j-4 for j in range(4,len(fr)) if fr[j]>=.9),None)
    print(g, rs, 'mean loss path k-4..12:', np.round(M,1))
    print('   eventual(k9-12)', round(ev,1), 'eventual(k8-10)', round(ev2,1), 'k50', k50, 'k90', k90, 'frac', np.round(fr[4:],2))
    print('   per-route median k50', np.median([res[r][2] for r in rs if res[r][2] is not None]), 'k90', np.median([res[r][3] for r in rs if res[r][3] is not None]))
print('--- loss routes only (eventual>=3pp) ---')
for g in ['big','slow']:
    rs=[r for r in paths if paths[r][0]==g and res[r][1]>=3]
    M=np.nanmean(np.array([-paths[r][3] for r in rs]),axis=0)
    ev=np.nanmean(M[13:17])
    r4=np.array([np.nanmean(M[max(4,j-3):j+1]) for j in range(len(M))])  # trailing 4q avg from k0
    sm=np.array([np.nanmean(M[max(0,j-1):j+2]) for j in range(len(M))])
    print(g, rs, 'path', np.round(M[4:],1), 'eventual', round(ev,1))
    print('  frac(3q centered)', np.round(sm[4:]/ev,2))
    print('  per-route k50', [res[r][2] for r in rs], 'k90', [res[r][3] for r in rs], 'eventual', [round(res[r][1],1) for r in rs])
