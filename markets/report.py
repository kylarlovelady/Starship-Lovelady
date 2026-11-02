"""Builds report.json: the 'what happened while I slept' report for the wallet run.
Reads the logs the agent already writes. Nothing here trades or changes any setting."""
import json, os, time

LAB = {"book": "Order book", "momentum": "Price momentum", "whales": "Whale moves",
       "news": "News vibe", "fng": "Fear & Greed", "funding": "Funding rate"}


def _rows(path):
    out = []
    try:
        with open(path) as f:
            for line in f:
                try:
                    out.append(json.loads(line))
                except Exception:
                    pass
    except FileNotFoundError:
        pass
    return out


def _tag(r):
    """One plain reason for how the round went."""
    p, h, f, o = r["pnl"], r.get("hold"), r.get("first"), r["outcome"]
    if f is None:
        return "no bet"
    first_ok = f == o
    if p >= 0:
        if h is not None and p - h > 0.5 and r.get("trades", 0) > 1:
            return "won, and moving around beat holding"
        return "won on a correct first read" if first_ok else "won after switching sides in time"
    if not first_ok and r.get("end") != o:
        return "lost: first read wrong and never recovered"
    if first_ok and h is not None and p < h - 0.5:
        return "lost: first read was right, but extra trades and fees ate it"
    if h is not None and p < h - 0.5:
        return "lost: moving around did worse than holding"
    return "lost: small loss, price went against it late"


def build(DIR, now=None):
    now = now or int(time.time())
    rows = _rows(os.path.join(DIR, "run_log.jsonl"))
    rep = {"updated": now, "run": None}
    changes = []
    for l in _rows(os.path.join(DIR, "learn_log.jsonl"))[-10:]:
        changes.append({"t": l.get("time"), "adopted": l.get("adopted"), "scored": l.get("scored"),
                        "notes": l.get("notes", []), "holdout": l.get("holdout")})
    rep["changes"] = changes
    try:
        with open(os.path.join(DIR, "weights.json")) as f:
            rep["weights"] = json.load(f)
    except Exception:
        rep["weights"] = None
    if not rows:
        rep["headline"] = "No wallet run yet. Press Start on the Live View and come back after some rounds."
        return rep
    rid = rows[-1]["run"]
    rs = [r for r in rows if r["run"] == rid]
    first_t = rs[0]["t"]
    n = len(rs)
    pnl = round(sum(r["pnl"] for r in rs), 2)
    wins = sum(1 for r in rs if r["pnl"] > 0)
    start_bal = round(rs[0]["bal"] - rs[0]["pnl"], 2)
    streak = cur = 0
    for r in rs:
        cur = cur + 1 if r["pnl"] < 0 else 0
        streak = max(streak, cur)
    best = max(rs, key=lambda r: r["pnl"]); worst = min(rs, key=lambda r: r["pnl"])
    tags = {}
    for r in rs:
        r["tag"] = _tag(r)
        e = tags.setdefault(r["tag"], {"n": 0, "pnl": 0.0}); e["n"] += 1; e["pnl"] = round(e["pnl"] + r["pnl"], 2)
    hours = {}
    for r in rs:
        h = hours.setdefault(str(r.get("hour", time.localtime(r["t"]).tm_hour)), {"n": 0, "pnl": 0.0, "wins": 0})
        h["n"] += 1; h["pnl"] = round(h["pnl"] + r["pnl"], 2); h["wins"] += 1 if r["pnl"] > 0 else 0
    # how much of its decision each piece of information carried at the opening bet
    stake, cnt = {}, 0
    for r in rs:
        if r.get("mix"):
            cnt += 1
            for lab, pc, sg in r["mix"]:
                stake[lab] = stake.get(lab, 0) + pc
    stake = {k: round(v / cnt) for k, v in stake.items()} if cnt else {}
    # did each signal point the right way?
    score = {}
    for r in rs:
        for k, v in (r.get("sigs") or {}).items():
            if abs(v) >= 0.1:
                e = score.setdefault(LAB.get(k, k), {"n": 0, "right": 0})
                e["n"] += 1; e["right"] += 1 if (v > 0) == (r["outcome"] == "UP") else 0
    for e in score.values():
        e["pct"] = round(100 * e["right"] / e["n"])
    # side-by-side strategies over the same stretch
    strat = {}
    for r in _rows(os.path.join(DIR, "sim_windows.jsonl")):
        if r.get("t", 0) >= first_t:
            e = strat.setdefault(r["strat"], {"n": 0, "pnl": 0.0, "wins": 0})
            e["n"] += 1; e["pnl"] = round(e["pnl"] + r["pnl"], 2); e["wins"] += 1 if r["pnl"] > 0 else 0
    first_ok = sum(1 for r in rs if r.get("first") and r["first"] == r["outcome"])
    bet = sum(1 for r in rs if r.get("first"))
    head = "Since %s it played %d rounds and won %d (%d%%). Wallet %s%s: $%.2f to $%.2f." % (
        time.strftime("%-I:%M %p", time.localtime(first_t)), n, wins, round(100 * wins / n), "up " if pnl >= 0 else "down ", "$%.2f" % abs(pnl), start_bal, rs[-1]["bal"])
    if bet:
        head += " Its first read was right %d%% of the time." % round(100 * first_ok / bet)
    rep.update({"headline": head, "run": {
        "id": rid, "started": first_t, "start": start_bal, "bal": rs[-1]["bal"], "pnl": pnl, "rounds": n, "wins": wins,
        "first_right_pct": round(100 * first_ok / bet) if bet else None, "worst_streak": streak,
        "best": {k: best[k] for k in ("t", "pnl", "outcome", "why")}, "worst": {k: worst[k] for k in ("t", "pnl", "outcome", "why")},
        "tags": tags, "hours": hours, "stake": stake, "signals": score, "strategies": strat,
        "list": [{k: r.get(k) for k in ("t", "pnl", "bal", "outcome", "first", "end", "hold", "trades", "why", "tag", "mix", "moves")} for r in rs[-150:]]}})
    return rep


if __name__ == "__main__":
    D = os.environ.get("MARKET_DIR", os.path.expanduser("~/market-data"))
    print(json.dumps(build(D), indent=1)[:3000])
