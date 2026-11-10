"""Fare-gap analysis: JetBlue vs United on shared nonstop routes, before vs since Blue Sky.

Outputs (output/):
  monthly_gap.csv        route x month: pax-weighted avg fare B6, UA, gap ($ and %)
  route_ranking.csv      routes ranked by smallest post-partnership gap, with pre-period gap and change
  live_gap.csv           same comparison from the daily live snapshots (once they exist)
  gap_trend.png          monthly |gap %| per route, partnership start marked
"""
import os
import duckdb, pandas as pd, yaml
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

CFG = yaml.safe_load(open("config.yaml"))
P = CFG["paths"]; os.makedirs(P["out"], exist_ok=True)
B6, UA = CFG["carriers"]["jetblue"], CFG["carriers"]["united"]
START = pd.Timestamp(CFG["partnership_start"])
con = duckdb.connect(P["db"], read_only=True)
pairs = {tuple(sorted(r)) for r in CFG["routes"]}

def pair(o, d):
    return "-".join(sorted([o, d]))

# ---------- DOT history ----------
t = con.execute(f"""
    SELECT period, origin, dest, carrier, sum(fare*pax)/sum(pax) AS fare, sum(pax) AS pax
    FROM dot_tickets WHERE period >= '{CFG['baseline_start']}'
    GROUP BY ALL""").df()
t["route"] = [pair(o, d) for o, d in zip(t.origin, t.dest)]

# auto-discover any other pair where both carriers carry nonstop traffic in the post period
post = t[t.period >= START].groupby(["route", "carrier"]).pax.sum().unstack()
both = post.dropna().index[(post.dropna() > 500).all(axis=1)]
routes = sorted(set("-".join(p) for p in pairs) | set(both))
t = t[t.route.isin(routes)]

m = (t.assign(w=t.fare * t.pax).groupby(["route", "period", "carrier"])[["w", "pax"]].sum())
m = (m.w / m.pax).unstack("carrier").dropna(subset=[B6, UA]).reset_index()
m["gap"] = m[UA] - m[B6]                       # + = United more expensive
m["gap_pct"] = m.gap / m[[B6, UA]].mean(axis=1) * 100
m["abs_gap_pct"] = m.gap_pct.abs()
m["phase"] = ["post" if p >= START else "pre" for p in m.period]
m.round(2).to_csv(f"{P['out']}/monthly_gap.csv", index=False)

r = m.groupby(["route", "phase"]).agg(B6=(B6, "mean"), UA=(UA, "mean"), gap=("gap", "mean"),
                                      abs_gap_pct=("abs_gap_pct", "mean"), months=("gap", "size")).unstack("phase")
r.columns = [f"{a}_{b}" for a, b in r.columns]
r["abs_gap_change_pts"] = r.abs_gap_pct_post - r.abs_gap_pct_pre       # negative = fares converged
r = r.sort_values("abs_gap_pct_post")
r.round(1).to_csv(f"{P['out']}/route_ranking.csv")
print(r[["UA_post", "B6_post", "gap_post", "abs_gap_pct_post", "abs_gap_pct_pre", "abs_gap_change_pts"]].round(1).to_string())

fig, ax = plt.subplots(figsize=(11, 6))
for rt, g in m.groupby("route"):
    ax.plot(g.period, g.abs_gap_pct, marker="o", ms=3, lw=1.2, label=rt)
ax.axvline(START, color="black", ls="--"); ax.text(START, ax.get_ylim()[1] * .95, " Blue Sky", va="top")
ax.set_ylabel("|United − JetBlue| avg fare gap (%)"); ax.set_title("JetBlue vs United fare gap on shared nonstop routes")
ax.legend(fontsize=7, ncol=2); fig.tight_layout(); fig.savefig(f"{P['out']}/gap_trend.png", dpi=160)

# ---------- live snapshots ----------
if con.execute("SELECT count(*) FROM information_schema.tables WHERE table_name='live_fares'").fetchone()[0]:
    l = con.execute("SELECT * FROM live_fares").df()
    l["route"] = [pair(o, d) for o, d in zip(l.origin, l.dest)]
    w = l.pivot_table(index=["scraped", "depart", "origin", "dest", "route"], columns="carrier", values="fare").dropna().reset_index()
    w["gap"] = w[UA] - w[B6]
    s = w.groupby("route").agg(n=("gap", "size"), B6=(B6, "mean"), UA=(UA, "mean"), avg_gap=("gap", "mean"),
                               median_gap=("gap", "median"), pct_identical=("gap", lambda x: (x == 0).mean() * 100),
                               pct_within_10=("gap", lambda x: (x.abs() <= 10).mean() * 100)).sort_values("pct_identical", ascending=False)
    s.round(1).to_csv(f"{P['out']}/live_gap.csv")
    print("\nLive snapshots:\n", s.round(1).to_string())
