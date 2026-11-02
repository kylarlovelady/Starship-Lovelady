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


cands = [p for p in glob.glob(D + "/run_log*.jsonl") if os.path.getsize(p) > 0]
if not cands:
    print("No wallet run found. Press Start on the Live View first."); sys.exit()
cands.sort(key=os.path.getmtime)
path = cands[-1] if len(cands) == 1 else sorted(cands, key=lambda p: rows_of(p)[-1]["t"])[-1]
rows = rows_of(path)
rid = rows[-1]["run"]
rows = [r for r in rows if r["run"] == rid]
t0 = rows[0]["t"]
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


n = len(rows); wins = sum(1 for r in rows if r["pnl"] > 0)
logged = sum(r["pnl"] for r in rows)
chk = [r for r in rows if r["t"] in res]
mism = [r for r in chk if res[r["t"]][0] != r["outcome"]]
true_pnl = sum(replay(r, res[r["t"]][0]) for r in chk if r.get("moves"))
true_wins = sum(1 for r in chk if r.get("moves") and replay(r, res[r["t"]][0]) > 0)
print("OVERNIGHT REPORT  (%s to %s)" % (time.strftime("%a %-I:%M %p", time.localtime(t0)), time.strftime("%a %-I:%M %p", time.localtime(rows[-1]["t"] + 900))))
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
