# Blue Sky fare-gap pipeline (JetBlue vs United)

Finds the shared nonstop routes where JetBlue and United fares have stayed closest since Blue Sky started. It also compares each route with the gap before the partnership.

## Two data sources
1. **History (DOT ticket samples, free).** These are real fares people paid.
   - DB1B: quarterly 10% sample, up to Jun 2025. This is the before-partnership baseline.
   - DB1C: monthly 40% sample, from Jul 2025 onward. This lines up with Blue Sky's start.
   - Download the zip files from bts.gov (Origin and Destination Survey Data → Market, plus the DB1C pages). Put them in `data/raw_dot/`.
   - DOT releases them with a delay of a few months.
2. **Live (daily snapshots).** These are the cheapest posted nonstop fares on each airline, for every shared route in both directions, at 7–120 days out.
   - They come from the SerpApi Google Flights API. You need a paid key.
   - Cost scales with: 13 routes × 2 directions × 8 horizons = 208 searches/day.

## Setup on the Vultr server
```
scp -r bluesky_fares root@YOUR_SERVER_IP:~/
ssh root@YOUR_SERVER_IP
cd bluesky_fares && bash setup.sh
nano .env                      # paste SERPAPI_KEY
# copy the DOT zip files into data/raw_dot/
.venv/bin/python ingest_dot.py
.venv/bin/python analyze.py
```
`setup.sh` installs everything and adds two cron jobs:
- the live collector runs daily at 6:15
- the analysis re-runs every Sunday

## Outputs (`output/`)
- `route_ranking.csv`: routes ranked by smallest average gap since the partnership. It shows the pre-partnership gap and the change; a negative change means the fares converged.
- `monthly_gap.csv`: passenger-weighted average fare for each route and month, by carrier.
- `gap_trend.png`: the gap per route over time, with the Blue Sky start marked.
- `live_gap.csv`: average and median gap, % of days with identical fares, and % within $10, from the daily snapshots.

## Notes
- **Settings:** routes, dates and fare filters live in `config.yaml`. The analysis also adds any other route where both airlines carry real nonstop traffic.
- **Fare cleaning:** DOT fares outside $25–$2,500 are dropped (award, employee and bad records). Nonstop means a single-coupon market.
- **New column names:** if a DOT file uses a column name the script doesn't know, it stops and names the missing field. Add that name to `COLS` in `ingest_dot.py`.
- **What the two sources measure:** DOT fares are averages across all cabins and fare types actually sold. The live snapshot is the lowest posted economy fare. They measure different things, so keep the two analyses separate.
