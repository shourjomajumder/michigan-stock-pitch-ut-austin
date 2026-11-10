"""Daily snapshot of the cheapest nonstop one-way fare on JetBlue and United for every
shared route (both directions) at several days-ahead horizons. Uses SerpApi's Google
Flights engine (needs SERPAPI_KEY in .env). Run once a day from cron.
"""
import os, datetime as dt, time
import duckdb, requests, yaml
from dotenv import load_dotenv

load_dotenv()
CFG = yaml.safe_load(open("config.yaml"))
KEY = os.environ["SERPAPI_KEY"]
NAME = {"JetBlue": "B6", "United": "UA"}

def cheapest(o, d, date):
    r = requests.get("https://serpapi.com/search.json", timeout=60, params=dict(
        engine="google_flights", departure_id=o, arrival_id=d, outbound_date=date,
        type=2, stops=1, currency=CFG["live"]["currency"], hl="en", api_key=KEY))
    r.raise_for_status()
    js = r.json()
    best = {}
    for it in js.get("best_flights", []) + js.get("other_flights", []):
        legs = it.get("flights", [])
        if len(legs) != 1 or "price" not in it:
            continue
        code = NAME.get(legs[0].get("airline"))
        if code and (code not in best or it["price"] < best[code]):
            best[code] = it["price"]
    return best

def main():
    con = duckdb.connect(CFG["paths"]["db"])
    con.execute("""CREATE TABLE IF NOT EXISTS live_fares(
        scraped DATE, depart DATE, origin VARCHAR, dest VARCHAR, carrier VARCHAR, fare DOUBLE)""")
    today = dt.date.today()
    for a, b in CFG["routes"]:
        for o, d in [(a, b), (b, a)]:
            for k in CFG["live"]["days_ahead"]:
                day = today + dt.timedelta(days=k)
                try:
                    for c, p in cheapest(o, d, day.isoformat()).items():
                        con.execute("INSERT INTO live_fares VALUES (?,?,?,?,?,?)", [today, day, o, d, c, p])
                except Exception as e:
                    print("fail", o, d, day, e)
                time.sleep(1)
    print(con.execute("SELECT count(*) FROM live_fares WHERE scraped = ?", [today]).fetchone()[0], "rows today")

if __name__ == "__main__":
    main()
