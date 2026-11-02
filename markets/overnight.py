"""Plain-English overnight report for the fake-money wallet run, checked against Kalshi's real results.
Usage: python3 ~/starship/markets/overnight.py   (read-only; changes nothing)"""
import glob, json, os, sys, time, calendar, urllib.request

D = os.environ.get("MARKET_DIR", os.path.expanduser("~/market-data"))
fee = lambda p: 0.07 * p * (1 - p)


def rows_of(path):
    out = []
    for l in open(path):
        try:
            out.append(json.loads(l))
        except Exception:
            pass
    return out


cands = [p for p in glob.glob(D + "/run_log*.jsonl") + glob.glob(D + "/archive/*/run_log*.jsonl") if os.path.getsize(p) > 0]
rows = []
if cands:
    path = sorted(cands, key=lambda p: rows_of(p)[-1]["t"])[-1]
    rows = rows_of(path)
    rid = rows[-1]["run"]
    rows = [r for r in rows if r["run"] == rid]
sw = []
for p in glob.glob(D + "/sim_windows*.jsonl") + glob.glob(D + "/archive/*/sim_windows*.jsonl"):
    sw += rows_of(p)
cl = []
for p in glob.glob(D + "/calls*.jsonl") + glob.glob(D + "/archive/*/calls*.jsonl"):
    cl += [c for c in rows_of(p) if c.get("outcome") in ("UP", "DOWN")]
tmin = [x for x in ([rows[0]["t"]] if rows else []) + [min([r["t"] for r in sw] or [0]) or 1e12, min([c["start"] for c in cl] or [0]) or 1e12]]
t0 = int(min(tmin)) if tmin else 0
if not rows and not sw and not cl:
    print("Nothing recorded yet."); sys.exit()
res = {}
try:
    url = "https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXBTC15M&status=settled&limit=1000&min_close_ts=%d" % (t0 - 1800)
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=20))
    for m in d.get("markets", []):
        ce = calendar.timegm(time.strptime(m["close_time"][:19], "%Y-%m-%dT%H:%M:%S"))
        if m.get("result") in ("yes", "no"):
            res[ce - 900] = ("UP" if m["result"] == "yes" else "DOWN", m.get("floor_strike"))
except Exception as e:
    print("Could not reach Kalshi for the check (%s). Showing the bot's own numbers only." % e)


def replay(r, true):
    pos = None; cash = 0.0
    for m in r.get("moves") or []:
        if m["a"] == "BUY":
            c = m["d"] / m["px"]; cash -= m["d"] + fee(m["px"]) * c
            pos = (m["side"], (pos[1] if pos and pos[0] == m["side"] else 0) + c)
        else:
            cash += m["d"]; pos = None
    if pos and pos[0] == true:
        cash += pos[1]
    return cash


if not rows:
    print("No wallet run was started overnight, so there is no wallet to report. Here is what the bot did on its own:\n")
n = len(rows); wins = sum(1 for r in rows if r["pnl"] > 0)
logged = sum(r["pnl"] for r in rows) if rows else 0
chk = [r for r in rows if r["t"] in res]
mism = [r for r in chk if res[r["t"]][0] != r["outcome"]]
true_pnl = sum(replay(r, res[r["t"]][0]) for r in chk if r.get("moves"))
true_wins = sum(1 for r in chk if r.get("moves") and replay(r, res[r["t"]][0]) > 0)
print("OVERNIGHT REPORT  (from %s)" % time.strftime("%a %-I:%M %p", time.localtime(t0)))
if rows:
    print("Wallet: $%.2f to $%.2f. The bot's own count: %d rounds, %d won, %+.2f." % (rows[0]["bal"] - rows[0]["pnl"], rows[-1]["bal"], n, wins, logged))
if chk:
    print("\nACCURACY CHECK against Kalshi's real results (%d rounds matched):" % len(chk))
    print("  Our outcome matched Kalshi's in %d of %d rounds. %d did not match." % (len(chk) - len(mism), len(chk), len(mism)))
    if sum(1 for r in chk if r.get("moves")):
        print("  Replaying the same bets with Kalshi's real results: %d rounds won, %+.2f (vs %+.2f recorded)." % (true_wins, true_pnl, sum(r["pnl"] for r in chk if r.get("moves"))))
    if mism:
        print("  First mismatches (our result vs Kalshi's):")
        for r in mism[:5]:
            print("   ", time.strftime("%-I:%M %p", time.localtime(r["t"])), r["outcome"], "vs", res[r["t"]][0])
if rows:
    print("\nSignals it leaned on at the opening bet, average share of the decision:")
    tot, cnt = {}, 0
    for r in rows:
        if r.get("mix"):
            cnt += 1
            for lab, pc, sg in r["mix"]:
                tot[lab] = tot.get(lab, 0) + pc
    for k, v in sorted(tot.items(), key=lambda x: -x[1]):
        print("  %-34s %d%%" % (k, round(v / cnt)))
    fr = [r for r in chk if r.get("first")]
    if fr:
        ok = sum(1 for r in fr if r["first"] == res[r["t"]][0])
        print("\nIts first read matched Kalshi's real result in %d of %d rounds (%d%%). A coin flip is about 50%%." % (ok, len(fr), round(100 * ok / len(fr))))
    print("\nWorst 3 rounds:")
    for r in sorted(rows, key=lambda r: r["pnl"])[:3]:
        print(" ", time.strftime("%-I:%M %p", time.localtime(r["t"])), "%+.2f" % r["pnl"], "-", r["why"][:200])
    print("\nBest 3 rounds:")
    for r in sorted(rows, key=lambda r: -r["pnl"])[:3]:
        print(" ", time.strftime("%-I:%M %p", time.localtime(r["t"])), "%+.2f" % r["pnl"], "-", r["why"][:200])

# ---- the six practice strategies and the scorecard, checked against Kalshi ----
if sw:
    print("\nSIX PRACTICE STRATEGIES (fake $1,000 each), as the bot recorded them:")
    by = {}
    for r in sw:
        e = by.setdefault(r["strat"], {"n": 0, "pnl": 0.0, "wins": 0, "bad": 0, "chk": 0})
        e["n"] += 1; e["pnl"] += r["pnl"]; e["wins"] += 1 if r["pnl"] > 0 else 0
        if r["t"] in res:
            e["chk"] += 1; e["bad"] += 1 if res[r["t"]][0] != r["outcome"] else 0
    for k, e in sorted(by.items(), key=lambda x: -x[1]["pnl"]):
        print("  %-9s %+9.2f over %3d rounds, won %2d%%   | its round result disagreed with Kalshi's in %d of %d rounds" % (k, e["pnl"], e["n"], round(100 * e["wins"] / max(1, e["n"])), e["bad"], e["chk"]))
    print("  (Because the target and the scoring were wrong, treat these profits as unreliable.)")
if cl:
    sc = [c for c in cl if c.get("call") in ("UP", "DOWN")]
    ch = [c for c in sc if c["start"] in res]
    if ch:
        ok_true = sum(1 for c in ch if c["call"] == res[c["start"]][0]); ok_rec = sum(1 for c in ch if c["call"] == c["outcome"])
        print("\nTHE 15-MINUTE CALLS: %d calls matched to Kalshi. Recorded accuracy %d%%; against Kalshi's real result %d%%. (50%% is a coin flip.)" % (len(ch), round(100 * ok_rec / len(ch)), round(100 * ok_true / len(ch))))
