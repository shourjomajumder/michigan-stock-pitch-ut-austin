"""Load DOT airline ticket samples (DB1B quarterly <= Jun 2025, DB1C monthly >= Jul 2025)
into DuckDB, keeping JetBlue (B6) and United (UA) nonstop tickets.

Usage:  python ingest_dot.py            # loads every .zip / .csv in data/raw_dot
Column names differ between DB1B and DB1C files, so they are matched flexibly below.
"""
import glob, os, re, zipfile, io
import duckdb, pandas as pd, yaml

CFG = yaml.safe_load(open("config.yaml"))
P = CFG["paths"]
CARRIERS = set(CFG["carriers"].values())

# possible source names -> standard name (first match wins, case-insensitive)
COLS = {
    "year":     ["year"],
    "quarter":  ["quarter"],
    "month":    ["month"],
    "origin":   ["origin", "mktorigin"],
    "dest":     ["dest", "mktdest"],
    "carrier":  ["tkcarrier", "ticketingcarrier", "rpcarrier", "reportingcarrier", "opcarrier", "carrier"],
    "fare":     ["mktfare", "marketfare", "itinfare", "itineraryfare", "fareamount", "fare"],
    "pax":      ["passengers", "pax"],
    "coupons":  ["mktcoupons", "marketcoupons", "coupons", "numcoupons"],
}

def pick(cols):
    low = {c.lower().replace("_", "").replace(" ", ""): c for c in cols}   # MARKET_FARE -> marketfare
    out = {}
    for std, opts in COLS.items():
        for o in opts:
            if o in low:
                out[std] = low[o]; break
    return out

def read_any(path):
    if path.endswith(".zip"):
        z = zipfile.ZipFile(path)
        name = [n for n in z.namelist() if n.lower().endswith(".csv")][0]
        return pd.read_csv(io.BytesIO(z.read(name)), low_memory=False, chunksize=2_000_000)
    return pd.read_csv(path, low_memory=False, chunksize=2_000_000)

def main():
    os.makedirs(os.path.dirname(P["db"]), exist_ok=True)
    con = duckdb.connect(P["db"])
    con.execute("""CREATE TABLE IF NOT EXISTS dot_tickets(
        source VARCHAR, period DATE, origin VARCHAR, dest VARCHAR, carrier VARCHAR,
        fare DOUBLE, pax DOUBLE)""")
    done = {r[0] for r in con.execute("SELECT DISTINCT source FROM dot_tickets").fetchall()}
    for f in sorted(glob.glob(f"{P['raw_dot']}/*.zip") + glob.glob(f"{P['raw_dot']}/*.csv")):
        src = os.path.basename(f)
        if src in done:
            print("skip", src); continue
        n = 0
        for chunk in read_any(f):
            m = pick(chunk.columns)
            need = {"year", "origin", "dest", "carrier", "fare"}
            if not need <= m.keys():
                raise SystemExit(f"{src}: missing columns {need - m.keys()} — add the name to COLS")
            d = chunk.rename(columns={v: k for k, v in m.items()})
            if "coupons" in d:                       # nonstop = single-coupon market
                d = d[d.coupons == 1]
            d = d[d.carrier.isin(CARRIERS)]
            d = d[(d.fare >= CFG["fare_min"]) & (d.fare <= CFG["fare_max"])]
            if "month" in d:
                mon = d.month.astype(int)
            else:
                mon = (d.quarter.astype(int) - 1) * 3 + 1   # quarterly file -> first month of quarter
            d["period"] = pd.to_datetime(dict(year=d.year.astype(int), month=mon, day=1))
            d["pax"] = d["pax"] if "pax" in d else 1.0
            d["source"] = src
            d = d[["source", "period", "origin", "dest", "carrier", "fare", "pax"]]
            con.register("tmp", d); con.execute("INSERT INTO dot_tickets SELECT * FROM tmp"); con.unregister("tmp")
            n += len(d)
        print(f"loaded {src}: {n:,} B6/UA nonstop rows")
    print(con.execute("SELECT min(period), max(period), count(*) FROM dot_tickets").fetchone())

if __name__ == "__main__":
    main()
