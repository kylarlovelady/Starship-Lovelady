"""STOP-LOSS AND PROFIT-TAKING TEST (read-only). Takes every practice buy the agent really made and replays what would have happened with different rules, using the real
second-by-second Kalshi book after that buy: hold to the end, cut the loss when the bet is down X% (selling at the real bid, fees in), and bank profit when the bet is up Y cents per contract.
Older rounds vs newer rounds. Shows the average cents per contract after fees for each rule, and how often it fires.
Usage: python3 stops.py [days=14]"""
import bisect, json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hypothesis import fee

D = os.environ.get("MARKET_DIR", os.path.join(os.path.expanduser("~"), "market-data"))
STOPS = (None, 0.20, 0.35, 0.50, 0.70)
TAKES = (None, 0.10, 0.20, 0.30)            # bank profit once up this many dollars per contract (after fees)


def mean_t(v):
    n = len(v)
    if n < 5: return (0.0, 0.0, n)
    m = sum(v) / n; sd = (sum((x - m) ** 2 for x in v) / (n - 1)) ** 0.5 or 1e-9
    return (m, m / (sd / n ** 0.5), n)


def main():
    days = float(sys.argv[1]) if len(sys.argv) > 1 else 14
    import replay
    use, cand, btc = replay.load_ticks(days)
    res = {r["ticker"]: r for r in use}
    buys = []
    cut = time.time() - days * 86400
    try:
        for l in open(os.path.join(D, "trades.jsonl")):
            try: r = json.loads(l)
            except ValueError: continue
            if r.get("a") == "BUY" and not r.get("live") and r.get("ticker") in res and (r.get("t") or 0) > cut and r.get("s") not in ("hold",):
                buys.append(r)
    except OSError:
        pass
    # one entry per strategy per round (the first buy), so a rule is judged on decisions, not on adds
    first = {}
    for b in sorted(buys, key=lambda r: r["t"]): first.setdefault((b["s"], b["ticker"]), b)
    ents = list(first.values())
    if len(ents) < 40:
        print("Only %d practice entries that match fully recorded rounds. Let it run longer." % len(ents)); return
    cutT = sorted(e["t"] for e in ents)[int(len(ents) * 0.6)]
    print("%d practice entries on %d fully recorded rounds (older to choose, newer to check). Cents per contract after fees.\n" % (len(ents), len(res)))
    paths = {}
    def path(tk):
        if tk not in paths:
            c = cand[tk]; paths[tk] = ([x[0] for x in c], c)
        return paths[tk]
    def run(e, stop, take):
        r = res[e["ticker"]]; ts, c = path(e["ticker"])
        side, px_in = e["side"], float(e["px"])
        if not .03 <= px_in <= .97: return None
        cost = px_in + fee(px_in)
        i0 = bisect.bisect_right(ts, e["t"])
        for j in range(i0, len(ts)):
            if ts[j] >= r["close"] - 5: break
            bid, ask = c[j][1], c[j][2]
            px_out = bid if side == "UP" else 1 - ask                  # what we could sell for
            net_now = px_out - fee(px_out) - cost
            if take is not None and net_now >= take: return net_now, "take"
            if stop is not None and net_now <= -stop * cost: return net_now, "stop"
        won = (r["result"] == "UP") == (side == "UP")
        return (1.0 if won else 0.0) - cost, "hold"
    print("rule                                  | older  newer  all  (t)   | fired%  | n")
    rows = []
    for stop in STOPS:
        for take in TAKES:
            O, N, A, fired = [], [], [], 0
            for e in ents:
                o = run(e, stop, take)
                if o is None: continue
                v = 100 * o[0]; A.append(v); (O if e["t"] < cutT else N).append(v); fired += (o[1] != "hold")
            if len(A) < 20: continue
            m = mean_t(A)
            rows.append((m[0], stop, take, mean_t(O)[0], mean_t(N)[0], m[1], 100 * fired / len(A), len(A)))
    name = lambda stop, take: "%s, %s" % ("no stop" if stop is None else "cut at -%d%%" % round(100 * stop), "no profit-taking" if take is None else "bank at +%dc" % round(100 * take))
    for r in sorted(rows, key=lambda r: -r[0]):
        print("%-37s | %+5.1f  %+5.1f  %+5.1f (t %+.1f) | %5.0f%%  | %d" % (name(r[1], r[2]), r[3], r[4], r[0], r[5], r[6], r[7]))
    base = [r for r in rows if r[1] is None and r[2] is None]
    if base: print("\nbaseline (just hold to the end): %+.1f cents per contract. A rule only helps if it beats this in BOTH older and newer, by more than luck (t above 2)." % base[0][0])
    json.dump({"made": int(time.time()), "entries": len(ents), "rows": [{"stop": r[1], "take": r[2], "older": r[3], "newer": r[4], "all": r[0], "t": r[5], "fired_pct": r[6]} for r in rows]},
              open(os.path.join(D, "history", "stops.json"), "w")) if os.path.isdir(os.path.join(D, "history")) else None


if __name__ == "__main__":
    main()
