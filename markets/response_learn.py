"""RESPONSE LEARNER (self-correcting). Separates 'is the signal good' from 'is the agent's response to it good'. Replays every practice buy the agent really made against the real
second-by-second book with different loss-cut levels, and keeps a level ONLY if it beats plain holding in BOTH the older and the newer half by a clear margin. Each run re-checks the
level currently in use: if it stops beating holding on the newest entries it is dropped and the default comes back. Every decision is written in plain English to response_log.jsonl,
with the old value kept. The agent reads learned_response.json (stop_pct only, clamped 0.15-0.8). Read-only otherwise. Usage: python3 response_learn.py [days=14]"""
import bisect, json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hypothesis import fee

D = os.environ.get("MARKET_DIR", os.path.join(os.path.expanduser("~"), "market-data"))
DEFAULT = 0.35
LEVELS = (0.25, 0.35, 0.50, 0.70)
MARGIN = 1.0      # cents per contract better than holding, in both halves


def log(msg, **kw):
    print(msg)
    try:
        with open(os.path.join(D, "response_log.jsonl"), "a") as fh: fh.write(json.dumps(dict(kw, t=int(time.time()), msg=msg)) + "\n")
    except OSError: pass


def main():
    days = float(sys.argv[1]) if len(sys.argv) > 1 else 14
    import replay
    use, cand, btc = replay.load_ticks(days)
    res = {r["ticker"]: r for r in use if r.get("result") in ("UP", "DOWN")}
    cut = time.time() - days * 86400
    first = {}
    try:
        for l in open(os.path.join(D, "trades.jsonl")):
            try: r = json.loads(l)
            except ValueError: continue
            if r.get("a") == "BUY" and not r.get("live") and r.get("ticker") in res and (r.get("t") or 0) > cut and r.get("s") != "hold" and (r.get("d") or 0) >= 5:
                first.setdefault((r["s"], r["ticker"]), r)
    except OSError: pass
    ents = sorted(first.values(), key=lambda r: r["t"])
    sp = os.path.join(D, "learned_response.json")
    try: cur = json.load(open(sp)).get("stop_pct", DEFAULT)
    except Exception: cur = DEFAULT
    if len(ents) < 60:
        log("Response learner: only %d usable practice entries (need 60). Keeping stop level %.0f%%." % (len(ents), 100 * cur), keep=cur); return
    cutT = ents[int(len(ents) * 0.6)]["t"]
    def run(e, stop):
        r = res[e["ticker"]]; c = cand[e["ticker"]]; ts = [x[0] for x in c]
        side, px_in = e["side"], float(e["px"])
        if not .03 <= px_in <= .97: return None
        cost = px_in + fee(px_in)
        for j in range(bisect.bisect_right(ts, e["t"]), len(ts)):
            if ts[j] >= r["close"] - 5: break
            po = c[j][1] if side == "UP" else 1 - c[j][2]
            nn = po - fee(po) - cost
            if stop is not None and nn <= -stop * cost: return nn
        return (1.0 if (r["result"] == "UP") == (side == "UP") else 0.0) - cost
    def score(stop):
        O, N = [], []
        for e in ents:
            v = run(e, stop)
            if v is not None: (O if e["t"] < cutT else N).append(100 * v)
        return (sum(O) / len(O) if O else 0.0, sum(N) / len(N) if N else 0.0, len(O) + len(N))
    base = score(None)
    table = {s: score(s) for s in LEVELS}
    ok = {s: v for s, v in table.items() if v[0] > base[0] + MARGIN and v[1] > base[1] + MARGIN}
    new = max(ok, key=lambda s: ok[s][0] + ok[s][1]) if ok else DEFAULT
    line = "; ".join("cut at -%d%%: older %+.1f newer %+.1f" % (100 * s, v[0], v[1]) for s, v in table.items())
    if ok:
        log("Response learner: holding scores older %+.1f / newer %+.1f cents per contract. %s. Best that beat holding in BOTH halves: cut at -%d%% (was %d%%)." % (base[0], base[1], line, 100 * new, 100 * cur), old=cur, new=new)
    else:
        log("Response learner: holding scores older %+.1f / newer %+.1f cents per contract. %s. No loss-cut level beat holding in BOTH halves by %.0f cent, so the default %d%% stays (was %d%%)." % (base[0], base[1], line, MARGIN, 100 * DEFAULT, 100 * cur), old=cur, new=DEFAULT)
    json.dump({"made": int(time.time()), "stop_pct": new, "previous": cur, "entries": len(ents)}, open(sp, "w"))


if __name__ == "__main__":
    main()
