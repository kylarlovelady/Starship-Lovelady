#!/usr/bin/env python3
"""STRATEGY LAB (read-only, never touches the running agent). Replays the second-by-second rounds the Pi recorded and tests thousands of complete trading
rules, every decision on the table at once:
  WHEN to buy (which signal, with or against it, how strong, which part of the round)  | WHICH SIDE (also an optional slow-trend lean that must agree or disagree)
  HOW MUCH to buy                                                                       | ADD MORE when a bet is winning (multiply profits), how often and how soon
  WHEN TO CUT a loss (stop level)                                                       | WHEN TO SELL a winner (bank at a target, trail the peak, sell when the move slows, or hold)
  MINIMUM PROFIT before any sale of a winner ($)
Real Kalshi prices at every step, real fees (rounded up per order), no look-ahead. Rules are SELECTED on the older rounds by evolution (the best survive and are mutated) and then
CHECKED on the newest rounds that selection never saw. Every rule tried is logged to lab_log.jsonl; the best are kept in lab_state.json and refined on every run.
Usage: python3 lab.py [days=14] [budget_seconds=240]"""
import bisect, json, math, os, random, sys, time

HOME = os.path.expanduser("~")
D = os.environ.get("MARKET_DIR", os.path.join(HOME, "market-data"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SIGNALS = ["bmom10", "bmom60", "bmom180", "kmom30", "kmom60", "bslow", "kslow", "z", "hr", "tr15m", "tr4h", "tr24h", "tr7d", "xdiv", "xdiv2", "flow", "bookimb",
           "oichg", "liq", "cbbook", "funding", "a_news", "a_whales", "a_bigtrades", "a_fng", "a_trend_h", "a_trend_w", "a_levels", "a_book", "a_momentum", "a_SCORE"]
GENES = {"sig": SIGNALS, "dir": [1, -1], "q": [.6, .75, .85, .93], "lo": [60, 120, 240, 360, 480], "hi": [300, 420, 540, 660, 780],
         "lean": [None, "tr24h", "hr", "tr4h"], "agree": [True, False], "stake": [25, 50, 100, 200], "adds": [0, 1, 2], "add_at": [5, 10, 20],
         "stop": [None, .2, .35, .5], "tp": [None, 10, 20, 30, 50], "minp": [0, 3, 5], "exit": ["hold", "trail", "slow"], "trail": [5, 10, 15]}


def fee_total(c, p):
    return math.ceil(0.07 * c * p * (1 - p) * 100 - 1e-9) / 100.0


def rand_genome(rng):
    g = {k: rng.choice(v) for k, v in GENES.items()}
    if g["hi"] <= g["lo"]: g["hi"] = min(x for x in GENES["hi"] if x > g["lo"])
    return g


def mutate(g, rng, n=None):
    g = dict(g)
    for k in rng.sample(list(GENES), n or rng.choice((1, 1, 2, 3))): g[k] = rng.choice(GENES[k])
    if g["hi"] <= g["lo"]: g["hi"] = min(x for x in GENES["hi"] if x > g["lo"])
    return g


def key(g):
    return json.dumps(g, sort_keys=True, default=str)


def prepare(days):
    """Rows per round: every 10 s, every signal, the real bid and ask."""
    import replay, signals as G
    use, cand, btc = replay.load_ticks(days)
    use = [r for r in use if r.get("result") in ("UP", "DOWN")]
    rows = G.build(use, cand, G.with_history(btc), G.extras(days))
    by = {}
    for r in rows: by.setdefault(r["open"], []).append(r)
    rounds = [sorted(v, key=lambda r: r["el"]) for k, v in sorted(by.items())]
    return rounds


def thresholds(train):
    th = {}
    for s in SIGNALS:
        v = sorted(abs(r["S"][s]) for rd in train for r in rd if r["S"].get(s))
        th[s] = [v[int(len(v) * q)] for q in GENES["q"]] if len(v) >= 150 else None
    return th


def simulate(g, rd, th):
    """One variant on one round. Returns (profit dollars, dollars put in) or None if it never traded."""
    t_ = th.get(g["sig"])
    if not t_: return None
    thr = t_[GENES["q"].index(g["q"])]
    res = rd[0]["res"]
    pos = None; done = False; last_add = -999
    for r in rd:
        el = r["el"]
        if pos is None and not done:
            if not (g["lo"] <= el < g["hi"]): continue
            s = r["S"].get(g["sig"])
            if s is None or abs(s) < thr: continue
            if g["lean"]:
                ln = r["S"].get(g["lean"])
                if ln is None or ((ln > 0) == (s > 0)) != g["agree"]: continue
            side = "UP" if (s > 0) == (g["dir"] > 0) else "DOWN"
            px = r["ask"] if side == "UP" else 1 - r["bid"]
            if not .08 <= px <= .92: continue
            c = int(g["stake"] / (px + .07 * px * (1 - px)))
            if c < 1: continue
            pos = {"side": side, "c": c, "cost": c * px + fee_total(c, px), "peak": 0.0, "adds": 0, "slowed": False}
            continue
        if pos is None: continue
        side = pos["side"]
        pout = r["bid"] if side == "UP" else 1 - r["ask"]
        now = pos["c"] * pout - fee_total(pos["c"], max(.01, min(.99, pout))) - pos["cost"]
        pos["peak"] = max(pos["peak"], now)
        pc = now / pos["c"]
        need = max(g["minp"], 0.02 * pos["cost"]) if g["minp"] else 0.0
        sell = None
        if g["stop"] and now <= -g["stop"] * pos["cost"]: sell = "cut"
        elif now > 0 and now >= need:
            if g["tp"] and pc >= g["tp"] / 100.0: sell = "take"
            elif g["exit"] == "trail" and pos["peak"] / pos["c"] >= .05 and pos["peak"] - now >= g["trail"] / 100.0 * pos["c"]: sell = "trail"
            elif g["exit"] == "slow":
                kv = r["S"].get("kmom30")
                if kv is not None:
                    fav = kv if side == "UP" else -kv
                    if fav >= 3: pos["slowed"] = True
                    elif pos["slowed"] and fav <= 0.5: sell = "slow"
        if sell:
            return now, pos["cost"]
        if g["adds"] and pos["adds"] < g["adds"] and pc >= g["add_at"] / 100.0 and el - last_add >= 40 and el < 660:
            px = r["ask"] if side == "UP" else 1 - r["bid"]
            if .08 <= px <= .92:
                c = int(g["stake"] / 2 / (px + .07 * px * (1 - px)))
                if c >= 1:
                    pos["c"] += c; pos["cost"] += c * px + fee_total(c, px); pos["adds"] += 1; last_add = el
    if pos is None: return None
    won = (res == "UP") == (pos["side"] == "UP")
    return pos["c"] * (1.0 if won else 0.0) - pos["cost"], pos["cost"]


def evaluate(g, rounds, th):
    R = []
    for rd in rounds:
        o = simulate(g, rd, th)
        if o: R.append((o[0], o[1]))
    n = len(R)
    if n < 20: return None
    rets = [p / c for p, c in R]
    m = sum(rets) / n; sd = (sum((x - m) ** 2 for x in rets) / (n - 1)) ** 0.5 or 1e-9
    return {"n": n, "roi": 100 * m, "t": m / (sd / n ** 0.5), "pnl": sum(p for p, c in R), "win": 100.0 * sum(1 for p, c in R if p > 0) / n, "lcb": 100 * (m - sd / n ** 0.5)}


def main():
    days = float(sys.argv[1]) if len(sys.argv) > 1 else 14
    budget = float(sys.argv[2]) if len(sys.argv) > 2 else 240
    t0 = time.time(); rng = random.Random(int(t0))
    rounds = prepare(days)
    if len(rounds) < 40:
        print("Only %d recorded rounds usable. Let it record longer." % len(rounds)); return
    cut = int(len(rounds) * 0.6); train, test = rounds[:cut], rounds[cut:]
    th = thresholds(train)
    sp = os.path.join(D, "lab_state.json")
    try: archive = json.load(open(sp)).get("elite", [])
    except Exception: archive = []
    pop = [g for g in archive if all(k in g for k in GENES)][:40] + [rand_genome(rng) for _ in range(300)]
    seen, scored, tried = {}, [], 0
    logf = open(os.path.join(D, "lab_log.jsonl"), "a")
    gen = 0
    while time.time() - t0 < budget * 0.8 and gen < 6:
        gen += 1
        for g in pop:
            k = key(g)
            if k in seen: continue
            r = evaluate(g, train, th); tried += 1
            seen[k] = (g, r)
            if r: scored.append((r["lcb"], g, r))
        scored.sort(key=lambda x: -x[0])
        elite = [g for _, g, _ in scored[:25]]
        pop = elite[:] + [mutate(rng.choice(elite), rng) for _ in range(250)] if elite else [rand_genome(rng) for _ in range(300)]
    top = scored[:15]
    finals = []
    for lcb, g, r in top:
        rt = evaluate(g, test, th)
        finals.append((g, r, rt))
        logf.write(json.dumps({"t": int(t0), "rounds": len(rounds), "g": g, "train": r, "test": rt}) + "\n")
    for k, (g, r) in list(seen.items())[:4000]:
        if r and (g, r) not in [(f[0], f[1]) for f in finals]:
            logf.write(json.dumps({"t": int(t0), "rounds": len(rounds), "g": g, "train": r}) + "\n")
    logf.close()
    def desc(g):
        s = "%s %s the signal (top %d%%), minutes %d-%d" % (g["sig"], "WITH" if g["dir"] > 0 else "AGAINST", round(100 * (1 - g["q"])), g["lo"] // 60, g["hi"] // 60)
        if g["lean"]: s += ", only if it %s the %s" % ("agrees with" if g["agree"] else "disagrees with", g["lean"])
        s += "; stake $%d" % g["stake"]
        if g["adds"]: s += ", add up to %d times when up %d cents" % (g["adds"], g["add_at"])
        s += "; " + ("cut at -%d%%" % round(100 * g["stop"]) if g["stop"] else "no stop")
        s += "; sell: " + ("bank at +%dc, " % g["tp"] if g["tp"] else "") + {"hold": "hold to the end", "trail": "trail the peak by %dc" % g["trail"], "slow": "when the move slows"}[g["exit"]]
        if g["minp"]: s += ", min profit $%d" % g["minp"]
        return s
    print("LAB: %d recorded rounds (%d to select on, %d newest to check). %d rules tried this run over %d generations in %ds. Return = profit / money put in, per round.\n" % (len(rounds), len(train), len(test), tried, gen, time.time() - t0))
    print("BEST RULES (picked on older rounds, then tested on the newest):")
    ok = 0
    for g, r, rt in finals[:8]:
        flag = ""
        if rt and rt["roi"] > 0 and rt["t"] >= 2: flag, ok = "  <-- holds up", ok + 1
        print("  %s\n     older: %+.1f%% over %d rounds (win %.0f%%)   newest: %s%s" % (desc(g), r["roi"], r["n"], r["win"], ("%+.1f%% over %d rounds (t %+.1f)" % (rt["roi"], rt["n"], rt["t"])) if rt else "too few trades", flag))
    # what matters: average older-round return by choice, across ALL rules tried
    print("\nWHAT MATTERS (average older-round return of every rule that used each choice, so no single lucky rule decides it):")
    for gene, label in (("exit", "how to sell winners"), ("stop", "loss cut"), ("tp", "bank profit at"), ("adds", "adds to winners"), ("stake", "stake"), ("dir", "with(+1)/against(-1)"), ("lo", "earliest minute (sec)"), ("minp", "min profit $")):
        agg = {}
        for k, (g, r) in seen.items():
            if r: agg.setdefault(g[gene], []).append(r["roi"])
        print("  %-24s %s" % (label, "   ".join("%s: %+.1f%% (%d)" % (v, sum(x) / len(x), len(x)) for v, x in sorted(agg.items(), key=lambda kv: str(kv[0])) if len(x) >= 8)))
    sig = {}
    for k, (g, r) in seen.items():
        if r: sig.setdefault(g["sig"], []).append(r["roi"])
    best = sorted(((sum(v) / len(v), s, len(v)) for s, v in sig.items() if len(v) >= 6), reverse=True)
    print("  best signals to trigger on: " + ", ".join("%s %+.1f%% (%d)" % (s, m, n) for m, s, n in best[:6]))
    print("\n%d of the top %d rules held up on the newest rounds. With %d rules tried, some look good by luck alone: trust only a rule that keeps winning as more rounds arrive (check again tomorrow)." % (ok, len(finals), tried))
    json.dump({"made": int(t0), "rounds": len(rounds), "tried": tried, "elite": [g for _, g, _ in scored[:40]],
               "final": [{"rule": desc(g), "g": g, "train": r, "test": rt} for g, r, rt in finals]}, open(sp, "w"))


if __name__ == "__main__":
    main()
