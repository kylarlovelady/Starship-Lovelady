"""Look-back and exit learning.
After rounds finish, the agent replays its own second-by-second recording and asks: if I had been in, when would selling have beaten holding?
  learn(d)   tries take-profit rules on every recorded round (hypothetical entries at many moments, both sides) and keeps the best one that
             beats simply holding to the end by a clear margin. Writes exit_rules.json. Until there is enough data the starting guess stays.
  audit(d)   checks every REAL early exit the agent made: what would holding to the end have paid? If the rule keeps losing, it is switched off.
  review(d)  for the agent's real positions: the best moment to sell, and how much profit it left on the table.
The rule: once a position has been up at least `peak` cents per contract (after fees), sell if the sale value then falls `drop` cents below
that best point. It only ever sells sooner, so it cannot make a bet bigger."""
import glob, gzip, json, math, os, threading, time

DEFAULT = {"peak": 8, "drop": 4}
P_GRID = (4, 6, 8, 10, 12, 15, 20)       # cents of profit that must be reached first
D_GRID = (2, 3, 4, 6, 8)                  # cents of give-back that triggers the sale
SLIP = 0.01                               # assume the sale fills 1 cent worse than the quote
MIN_ROUNDS = 20
MIN_GAIN = 0.005                          # must beat holding by half a cent per entry, after fees
AUDIT_MIN = 15                            # real exits needed before the auto-off check can act
AUDIT_FLOOR = -0.01                       # average (sale minus hold) per contract below this switches the rule off


def fee(p):
    return 0.07 * p * (1 - p)


def _lines(path):
    op = gzip.open if path.endswith(".gz") else open
    try:
        with op(path, "rt") as f:
            for ln in f:
                try:
                    yield json.loads(ln)
                except ValueError:
                    pass
    except OSError:
        return


def _book(r):
    ob = r.get("ob") or {}
    yl, nl = ob.get("yes_dollars") or ob.get("yes"), ob.get("no_dollars") or ob.get("no")
    if not yl or not nl:
        return None
    try:
        yb = max(float(x[0]) for x in yl); nb = max(float(x[0]) for x in nl)
    except (TypeError, ValueError, IndexError):
        return None
    yb = yb / 100.0 if yb > 1.0 else yb
    nb = nb / 100.0 if nb > 1.0 else nb
    return yb, 1.0 - nb


def outcomes(d):
    out = {}
    for c in _lines(os.path.join(d, "calls.jsonl")):
        if c.get("outcome") in ("UP", "DOWN") and c.get("src") == "kalshi" and c.get("ticker"):
            out[c["ticker"]] = c["outcome"]
    return out


def series(d, days=3):
    """{ticker: [(t, yes_bid, yes_ask), ...]} from the live order book in the per-second recording."""
    files = sorted(glob.glob(os.path.join(d, "ticks-*.jsonl*")))[-days:]
    out = {}
    for p in files:
        for r in _lines(p):
            tk = (r.get("k") or {}).get("ticker")
            b = _book(r)
            if tk and b and r.get("t"):
                out.setdefault(tk, []).append((r["t"], b[0], b[1]))
    return out


def _vals(rows, side):
    """sale value per contract after the sell fee, for each second."""
    if side == "UP":
        return [(t, b - fee(b)) for t, b, a in rows]
    return [(t, (1 - a) - fee(1 - a)) for t, b, a in rows]


def _sim_rule(vals, i0, cost, P, D):
    """Returns the sale value (net of slippage) if the rule fires after entry index i0, else None."""
    pk = -9.0
    for _, v in vals[i0 + 1:]:
        prof = v - cost
        if prof > pk:
            pk = prof
        if pk >= P / 100.0 and prof <= pk - D / 100.0:
            return v - SLIP
    return None


def learn(d, now=None):
    now = now or time.time()
    res = outcomes(d)
    ser = series(d)
    rounds = [(tk, rs) for tk, rs in ser.items() if tk in res and len(rs) > 300]
    out = {"updated": int(now), "rounds": len(rounds), "source": "default", "peak": DEFAULT["peak"], "drop": DEFAULT["drop"], "enabled": True}
    old = {}
    try:
        old = json.load(open(os.path.join(d, "exit_rules.json")))
    except (OSError, ValueError):
        pass
    if old.get("audit"):
        out["audit"] = old["audit"]
        out["enabled"] = old.get("enabled", True)
    if len(rounds) < MIN_ROUNDS:
        out["note"] = "only %d finished rounds with a full recording; keeping the starting guess until %d" % (len(rounds), MIN_ROUNDS)
        _save(d, out)
        return out
    # per (P, D): per-round average improvement over holding, so correlated entries in one round count once
    imp = {(P, D): [] for P in P_GRID for D in D_GRID}
    holdres, ruleres = {(P, D): [] for P in P_GRID for D in D_GRID}, {(P, D): [] for P in P_GRID for D in D_GRID}
    for tk, rs in rounds:
        rs = sorted(rs)[::2]                                    # every other second is plenty
        t0 = rs[0][0]
        won_up = res[tk] == "UP"
        for side in ("UP", "DOWN"):
            vals = _vals(rs, side)
            won = won_up if side == "UP" else not won_up
            hold_v = 1.0 if won else 0.0
            ents = [i for i, (t, _) in enumerate(vals) if 40 <= t - t0 <= 560 and (t - t0) % 60 < 2]
            per = {k: [] for k in imp}
            for i in ents:
                px = (rs[i][2] if side == "UP" else 1 - rs[i][1])
                if not (0.20 <= px <= 0.80):
                    continue
                cost = px + fee(px)
                for (P, D) in per:
                    v = _sim_rule(vals, i, cost, P, D)
                    per[(P, D)].append(((v if v is not None else hold_v) - cost, hold_v - cost))
            for k, lst in per.items():
                if lst:
                    imp[k].append(sum(a - b for a, b in lst) / len(lst))
                    ruleres[k].append(sum(a for a, _ in lst) / len(lst)); holdres[k].append(sum(b for _, b in lst) / len(lst))
    best = None
    table = []
    for k, xs in imp.items():
        if len(xs) < MIN_ROUNDS:
            continue
        m = sum(xs) / len(xs)
        sd = math.sqrt(sum((x - m) ** 2 for x in xs) / max(1, len(xs) - 1))
        se = sd / math.sqrt(len(xs))
        table.append({"peak": k[0], "drop": k[1], "gain": round(m, 4), "se": round(se, 4), "rounds": len(xs),
                      "rule": round(sum(ruleres[k]) / len(ruleres[k]), 4), "hold": round(sum(holdres[k]) / len(holdres[k]), 4)})
        if m >= MIN_GAIN and m >= 1.0 * se and (best is None or m > best["gain"]):
            best = table[-1]
    table.sort(key=lambda r: -r["gain"])
    out["table"] = table[:6]
    if best:
        out.update({"source": "measured", "peak": best["peak"], "drop": best["drop"], "gain": best["gain"], "se": best["se"]})
    else:
        out["note"] = "no take-profit rule beat holding by a clear margin yet; keeping the starting guess" if table else "not enough data"
        # no rule beats holding: do not let the guess run unsupervised on measured evidence alone
        if table and table[0]["gain"] < 0 and len(rounds) >= 3 * MIN_ROUNDS:
            out["enabled"] = False
            out["audit"] = "switched off: over %d rounds every tested take-profit rule did worse than holding" % len(rounds)
    _save(d, out)
    return out


def audit(d, now=None):
    """Judge the agent's REAL early exits against holding to the end. Updates `enabled` in exit_rules.json."""
    res = outcomes(d)
    diffs = []
    for e in _lines(os.path.join(d, "exits.jsonl")):
        tk = e.get("ticker")
        if tk not in res or not e.get("c"):
            continue
        won = (res[tk] == "UP") == (e.get("side") == "UP")
        hold = (1.0 if won else 0.0) - e["avg_cost"]
        sold = e["sale_net"] - e["avg_cost"]
        diffs.append(sold - hold)
    path = os.path.join(d, "exit_rules.json")
    try:
        r = json.load(open(path))
    except (OSError, ValueError):
        r = dict(DEFAULT, enabled=True, source="default", rounds=0)
    r["exits_checked"] = len(diffs)
    if diffs:
        r["exit_vs_hold"] = round(sum(diffs) / len(diffs), 4)
    if len(diffs) >= AUDIT_MIN:
        m = sum(diffs) / len(diffs)
        if m < AUDIT_FLOOR:
            r["enabled"] = False
            r["audit"] = "switched off: %d early exits averaged %.1f cents per contract WORSE than holding to the end" % (len(diffs), -100 * m)
    _save(d, r)
    return r


def review(d, last=8):
    """The agent's own real positions, one line per (round, side): what it paid, the best moment to sell, and what it actually made."""
    res = outcomes(d)
    ser = series(d)
    pos = {}
    for r in _lines(os.path.join(d, "trades.jsonl")):
        if r.get("s") != "run" or r.get("a") not in ("BUY", "SELL") or not r.get("ticker") or not r.get("live"):
            continue
        p = pos.setdefault((r["ticker"], r["side"]), {"c": 0.0, "cost": 0.0, "t0": r["t"], "got": 0.0, "sold_c": 0.0, "t_sell": None})
        if r["a"] == "BUY":
            p["c"] += r["c"]; p["cost"] += r["d"]
        else:
            p["sold_c"] += r["c"]; p["got"] += r["d"]; p["t_sell"] = r["t"]
    out = []
    for (tk, side), p in list(pos.items())[-last:]:
        if not p["c"]:
            continue
        avg = p["cost"] / p["c"]
        left = max(0.0, p["c"] - p["sold_c"])
        done = tk in res
        won = done and ((res[tk] == "UP") == (side == "UP"))
        pnl = p["got"] - p["cost"] + (left * (1.0 if won else 0.0) if done else 0.0)
        best = ""
        rows = ser.get(tk)
        if rows:
            vals = _vals(sorted(rows), side)
            end_t = p["t_sell"] or 9e18
            after = [(t, v) for t, v in vals if p["t0"] <= t <= end_t]
            if after:
                tpk, vpk = max(after, key=lambda x: x[1])
                best = "; best moment to sell %s at %d c (%+.1f c vs cost)" % (time.strftime("%H:%M:%S", time.localtime(tpk)), round(100 * vpk), 100 * (vpk - avg))
        how = ("sold %d" % p["sold_c"] if p["sold_c"] else "") + (" and " if p["sold_c"] and left > 0.5 else "") + ("held %d to the end (%s)" % (left, "won" if won else "lost") if left > 0.5 and done else "held %d, round not finished" % left if left > 0.5 else "")
        out.append("%s %s %d contracts at about %d c%s; %s -> %s$%.2f" % (
            time.strftime("%H:%M", time.localtime(p["t0"])), side, p["c"], round(100 * avg), best, how, "+" if pnl >= 0 else "-", abs(pnl)))
    return out


def _save(d, obj):
    tmp = os.path.join(d, "exit_rules.json.tmp")
    try:
        with open(tmp, "w") as f:
            json.dump(obj, f)
        os.replace(tmp, os.path.join(d, "exit_rules.json"))
    except OSError:
        pass


def _loop(d):
    time.sleep(120)
    while True:
        try:
            learn(d)
            audit(d)
        except Exception:
            pass
        time.sleep(1200)


def start(d):
    threading.Thread(target=_loop, args=(d,), daemon=True, name="exit-learn").start()


def current(d, now=None, cache={}):
    """Rules in force: {"on": bool, "peak": cents, "drop": cents, "source": str}. Cached for a minute."""
    now = now or time.time()
    if cache.get("t", 0) > now - 60:
        return cache["v"]
    try:
        r = json.load(open(os.path.join(d, "exit_rules.json")))
    except (OSError, ValueError):
        r = {}
    v = {"on": bool(r.get("enabled", True)), "peak": r.get("peak", DEFAULT["peak"]), "drop": r.get("drop", DEFAULT["drop"]),
         "source": r.get("source", "default"), "audit": r.get("audit")}
    cache.update({"t": now, "v": v})
    return v
