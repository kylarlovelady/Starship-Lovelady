"""Builds report.json: the 'what happened while I slept' report for the wallet run.
Reads the logs the agent already writes. Nothing here trades or changes any setting."""
import json, math, os, time

LAB = {"book": "Order book", "momentum": "Price momentum", "whales": "Whale moves",
       "bigtrades": "Big exchange trades", "news": "News vibe", "fng": "Fear & Greed", "funding": "Funding rate"}


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


def _wilson(k, n, z=1.96):
    if n == 0:
        return 0.0, 1.0
    p = k / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return max(0.0, c - h), min(1.0, c + h)


NAMES = {"distance": "Distance only", "signals": "Distance plus all signals", "trend": "Price trend",
         "flow": "Order book and whales", "mood": "News and mood", "hold": "Hold the first bet"}


def trust_text(lab, g):
    n, pct, lo, hi = g["n"], g["pct"], g["low"], g["high"]
    if g["verdict"] == "still learning":
        return "%s: too early to judge (%d tests so far, it needs 20)." % (lab, n)
    if g["verdict"] == "trusted":
        return "We like %s. When it leaned, Kalshi agreed %s%% of %d times (likely %s%% to %s%%). It helps predict the move, so it gets more say." % (lab, pct, n, round(lo), round(hi))
    if g["verdict"] == "not trusted":
        return "We can't trust %s. When it leaned, Kalshi agreed only %s%% of %d times (likely %s%% to %s%%). That is worse than a coin flip, so it gets less say." % (lab, pct, n, round(lo), round(hi))
    return "%s shows no clear edge yet: %s%% of %d (likely %s%% to %s%%). It keeps a normal say, nudged slightly." % (lab, pct, n, round(lo), round(hi))


def strategy_verdicts(DIR):
    by = {}
    for x in _rows(os.path.join(DIR, "sim_windows.jsonl")):
        e = by.setdefault(x["strat"], {"n": 0, "pnl": 0.0, "wins": 0})
        e["n"] += 1; e["pnl"] += x["pnl"]; e["wins"] += 1 if x["pnl"] > 0 else 0
    out = []
    for k, e in by.items():
        lo, hi = _wilson(e["wins"], e["n"])
        per = e["pnl"] / e["n"]
        if e["n"] < 20:
            v, s = "too early", "%s: only %d rounds so far, too early to judge." % (NAMES.get(k, k), e["n"])
        elif e["pnl"] > 0 and lo > 0.5:
            v, s = "like", "We like %s: it won %d of %d rounds (likely %d%% to %d%%) and made $%.2f after fees." % (NAMES.get(k, k), e["wins"], e["n"], round(100 * lo), round(100 * hi), e["pnl"])
        elif e["pnl"] < 0 and hi < 0.5:
            v, s = "dont trust", "We can't trust %s: it won only %d of %d rounds and lost $%.2f after fees." % (NAMES.get(k, k), e["wins"], e["n"], -e["pnl"])
        elif e["pnl"] > 0:
            v, s = "maybe", "%s is ahead $%.2f over %d rounds but that could still be luck (won %d%%, likely %d%% to %d%%)." % (NAMES.get(k, k), e["pnl"], e["n"], round(100 * e["wins"] / e["n"]), round(100 * lo), round(100 * hi))
        else:
            v, s = "no edge", "%s is behind $%.2f over %d rounds. No proven edge, fees are eating it." % (NAMES.get(k, k), -e["pnl"], e["n"])
        out.append({"key": k, "name": NAMES.get(k, k), "n": e["n"], "pnl": round(e["pnl"], 2), "per_round": round(per, 3),
                    "wins": e["wins"], "verdict": v, "text": s})
    out.sort(key=lambda z: -z["pnl"])
    return out


def build(DIR, now=None):
    now = now or int(time.time())
    rows = _rows(os.path.join(DIR, "run_log.jsonl"))
    rep = {"updated": now, "run": None}
    changes = []
    for l in _rows(os.path.join(DIR, "learn_log.jsonl"))[-10:]:
        changes.append({"t": l.get("time"), "adopted": l.get("adopted"), "scored": l.get("scored"),
                        "notes": l.get("notes", []), "holdout": l.get("holdout")})
    rep["changes"] = changes
    lr = None
    try:
        with open(os.path.join(DIR, "learn_report.json")) as f:
            lr = json.load(f)
    except Exception:
        pass
    LABS = {"book": "Order book", "momentum": "Price momentum", "whales": "Whale moves", "bigtrades": "Big exchange trades", "news": "News vibe", "fng": "Fear & Greed", "funding": "Funding rate"}
    rep["trust"] = [dict(key=k, label=LABS.get(k, k), text=trust_text(LABS.get(k, k), g), **g) for k, g in ((lr or {}).get("signals") or {}).items()]
    rep["learn_notes"] = (lr or {}).get("notes", [])
    rep["learn_scored"] = (lr or {}).get("scored", 0)
    rep["strategies_trust"] = strategy_verdicts(DIR)
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
    dec = {}
    for r in rs:
        if r.get("mix") and r.get("first"):
            top = max(r["mix"], key=lambda m: m[1])[0]
            e = dec.setdefault(top, {"n": 0, "wins": 0, "pnl": 0.0})
            e["n"] += 1; e["wins"] += 1 if r["pnl"] > 0 else 0; e["pnl"] = round(e["pnl"] + r["pnl"], 2)
    dec_text = ["When %s was the biggest push, the bot won %d of %d rounds (%+.2f)." % (k, e["wins"], e["n"], e["pnl"]) for k, e in sorted(dec.items(), key=lambda x: -x[1]["n"])]
    missing = {}
    for r in rs:
        for k, lab in LABS.items():
            if r.get("sigs") is not None and k not in r["sigs"]:
                missing[lab] = missing.get(lab, 0) + 1
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
        "tags": tags, "deciders": dec_text, "no_data": missing, "hours": hours, "stake": stake, "signals": score, "strategies": strat,
        "list": [{k: r.get(k) for k in ("t", "pnl", "bal", "outcome", "first", "end", "hold", "trades", "why", "tag", "mix", "moves")} for r in rs[-150:]]}})
    return rep


if __name__ == "__main__":
    D = os.environ.get("MARKET_DIR", os.path.expanduser("~/market-data"))
    print(json.dumps(build(D), indent=1)[:3000])
