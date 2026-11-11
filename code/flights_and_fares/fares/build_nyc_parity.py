"""Rebuild the NYC 18-route base-fare gap table (appendix slide E2, 'All 18 routes -$1.94').

Inputs (repo-relative, Google Flights quotes collected 2026-11-11):
  raw/google_flights/t1s2/live_jfk_ewr.csv        round 1: 12 routes x 4 dates (Dec 2026-Jan 2027)
  raw/google_flights/rv_fares/agent_01..20.csv    round 2: new routes (Dec-Jan dates) + re-tests (Feb-Mar 2027 dates)
Statistic (reverse-engineered, reproduces every slide value):
  per route-date gap = JetBlue lowest nonstop fare at JFK/LGA  minus  United lowest nonstop fare at the comparison airport
  (EWR; for DEN and IAH United LGA, as in the agent verdicts);
  route gap = mean of all dates after dropping the single date with the largest |gap|; slide shows it rounded to $1;
  18-route average = mean of the 18 rounded route gaps.
"""
import os as _os; _R = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../..')  # repo root
import os, sys, glob
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(_R, 'data', 'flights_and_fares'))  # data root (raw/, processed/)
RAW = os.path.join(ROOT, 'raw', 'google_flights')
OUT = os.path.join(ROOT, 'processed')

ROUTES = ['FLL', 'LAX', 'PBI', 'SFO', 'BOS', 'TPA', 'ATL', 'RDU', 'JAX', 'SAN',
          'BQN', 'PHX', 'CHS', 'DEN', 'SLC', 'MSY', 'IAH', 'CLE']
SLIDE = {'FLL': -2, 'LAX': -4, 'PBI': -14, 'SFO': -4, 'BOS': -2, 'TPA': -10, 'ATL': 0, 'RDU': 0, 'JAX': 0, 'SAN': 3,
         'BQN': 7, 'PHX': -3, 'CHS': 0, 'DEN': 0, 'SLC': -6, 'MSY': 0, 'IAH': 0, 'CLE': 0}
UA_AIRPORT = {'DEN': ['LGA'], 'IAH': ['LGA']}


def load(jb_airports=('JFK', 'LGA'), ua_default=('EWR',)):
    files = [os.path.join(RAW, 't1s2', 'live_jfk_ewr.csv')] + sorted(glob.glob(os.path.join(RAW, 'rv_fares', 'agent_[01][0-9].csv'))) \
        + [os.path.join(RAW, 'rv_fares', 'agent_20.csv')]
    q = pd.concat([pd.read_csv(f).assign(file=os.path.relpath(f, ROOT)) for f in files], ignore_index=True)
    q = q[pd.to_numeric(q.fare, errors='coerce').notna()].copy()
    q['fare'] = q.fare.astype(float)
    q['route'] = q.route.str.replace('NYC-', '', regex=False)
    q['carrier'] = q.airline.str.replace(' Express', '', regex=False)
    return q


def gaps(q, jb_airports=('JFK', 'LGA'), ua_default=('EWR',)):
    rows = []
    for r in ROUTES:
        x = q[q.route == r]
        jb = x[(x.carrier == 'JetBlue') & x.airport.isin(jb_airports)].groupby('date').fare.min()
        ua = x[(x.carrier == 'United') & x.airport.isin(UA_AIRPORT.get(r, ua_default))].groupby('date').fare.min()
        for d in sorted(set(jb.index) & set(ua.index)):
            rows.append(dict(route=f'NYC-{r}', dest=r, date=d, jetblue=jb[d], united=ua[d], gap=jb[d] - ua[d]))
    return pd.DataFrame(rows)


def summarise(g):
    out = []
    for r in ROUTES:
        s = g[g.dest == r].gap
        trimmed = s.drop(s.abs().idxmax()) if len(s) > 1 else s
        out.append(dict(route=f'NYC-{r}', n_dates=len(s), mean_all=round(s.mean(), 2), median_all=s.median(),
                        dropped_date=g.loc[s.abs().idxmax(), 'date'], dropped_gap=g.loc[s.abs().idxmax(), 'gap'],
                        gap_mean_ex_largest=round(trimmed.mean(), 2), gap_slide=round(trimmed.mean()),
                        slide_value=SLIDE[r]))
    return pd.DataFrame(out)


if __name__ == '__main__':
    q = load()
    g = gaps(q)
    s = summarise(g)
    print(s.to_string(index=False))
    ok = (s.gap_slide == s.slide_value).sum()
    avg = s.gap_slide.mean()
    print(f'matches slide: {ok}/18; 18-route average of rounded gaps = {avg:.4f}; unrounded = {s.gap_mean_ex_largest.mean():.4f}')
    if len(sys.argv) > 1 and sys.argv[1] == 'write':
        g.to_csv(os.path.join(OUT, 'nyc_18_route_date_gaps.csv'), index=False)
        ov = pd.read_csv(os.path.join(_R, 'data', 'air_traffic_dot_bts', 'processed', 'bluesky_nyc_overlap.csv'))
        ov = ov[(ov.scope == 'dom') & ov.nyc_airport.isin(['JFK', 'LGA']) & ov.dest.isin(ROUTES)]
        pax = ov.groupby('dest').b6_pax_L4Q.sum()
        s['jetblue_pax_jfk_lga_L4Q'] = s.route.str[4:].map(pax)
        s = s.sort_values('jetblue_pax_jfk_lga_L4Q', ascending=False)
        s['shown_on_slide_top10'] = range(1, 19)
        s['shown_on_slide_top10'] = s.shown_on_slide_top10 <= 10
        s.to_csv(os.path.join(OUT, 'nyc_18_route_gaps.csv'), index=False)
        print('total JetBlue JFK+LGA pax on the 18 routes =', pax.sum(), '(slide 5.533M)')
