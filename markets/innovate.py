#!/usr/bin/env python3
"""INNOVATOR: keeps the experiment board moving. Reads how every live practice strategy and reaction test has done (cents per dollar staked, real fills, fees in),
reports experiments that lag the strategy they modify (they keep trading; nothing is removed), and invents new ones by changing one thing about the best performers (how it cuts losses, when it sells,
how often it adds, how long it waits, which entry it uses, whether it bets the opposite). New experiments start trading on pretend money within seconds (variants.json -> sim.py).
Every move is written in plain English to innovations.jsonl and shown on the Live View. It never touches real money, the hard rules ($5 minimum bet, $5 minimum profit) or the stake cap,
and an experiment is NOT a promoted strategy: promotion still needs wins on unseen rounds.   python3 innovate.py [hours=72]"""
import json, math, os, random, sys, time
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
D = os.environ.get("MARKET_DIR", os.path.join(os.path.expanduser("~"), "market-data"))
MAXDYN = 40         # nothing is ever retired: experiments only get added. When the board is full it stops inventing and says so.
MIN_RETIRE_ROUNDS = 40
LADDER = {"STOP_PCT": (0.15, 0.25, 0.35, 0.5, 0.65, 0.8), "EXIT_P": (5, 8, 15, 30, 50), "EXIT_D": (3, 4, 8, 12, 20), "MAX_TRADES": (1, 2, 3, 6, 10), "STAGE_GAP": (10, 25, 45, 90, 180),
          "ODDS_MARGIN": (0.0, 0.02, 0.04, 0.08, 0.15), "ENTRY_AFTER": (0, 60, 120, 240, 360, 480), "STOP_SMALL": (0, 5, 10, 25), "STOP_ON": (0, 1), "ODDS_SELL": (0, 1), "EXIT_ON": (0, 1), "FLIP": (0, 1)}
NAMES = {"STOP_PCT": "cut at {:.0%} down", "EXIT_P": "trail starts when up {:g}c", "EXIT_D": "sell if it falls {:g}c from the peak", "MAX_TRADES": "at most {:g} buys per round",
         "STAGE_GAP": "{:g}s between buys", "ODDS_MARGIN": "sell on its own odds only with a {:.0%} edge", "ENTRY_AFTER": "wait {:g}s before the first bet",
         "STOP_SMALL": "never cut bets under ${:g}", "STOP_ON": "loss cut {}", "ODDS_SELL": "odds-based selling {}", "EXIT_ON": "trailing sell {}", "FLIP": "bet the opposite {}"}
BOOL = ("STOP_ON", "ODDS_SELL", "EXIT_ON", "FLIP")
BUILT_IN = {  # the base entry strategies, so a variant can be compared with the strategy it modifies
    "distance": "distance", "signals": "signals", "trend": "trend", "flow": "flow", "mood": "mood"}


def say(msg, **kw):
    print(msg)
    try:
        with open(os.path.join(D, "innovations.jsonl"), "a") as fh: fh.write(json.dumps(dict(kw, t=int(time.time()), msg=msg)) + "\n")
    except OSError:
        pass


def fee_total(c, p): return math.ceil(0.07 * c * p * (1 - p) * 100 - 1e-9) / 100.0


def stats(hours):
    """{strategy: [rounds, profit, staked]} from the practice trade log, settled rounds only (Kalshi result known)."""
    import exit_learn as X
    res = X.outcomes(D)
    try:
        for ln in open(os.path.join(D, "history", "rounds.jsonl")):
            r = json.loads(ln); res.setdefault(r["ticker"], r["result"])
    except OSError:
        pass
    cut = time.time() - hours * 3600
    ev = defaultdict(list)
    try:
        for l in open(os.path.join(D, "trades.jsonl")):
            try: r = json.loads(l)
            except ValueError: continue
            if r.get("live") or r.get("a") not in ("BUY", "SELL") or not r.get("c") or not r.get("px") or (r.get("t") or 0) < cut or r.get("ticker") not in res: continue
            ev[(r["s"], r["ticker"])].append(r)
    except OSError:
        return {}
    out = defaultdict(lambda: [0, 0.0, 0.0])
    for (s, tk), rs in ev.items():
        rs.sort(key=lambda r: r["t"]); won = {"UP": res[tk] == "UP", "DOWN": res[tk] == "DOWN"}
        pos = {"UP": 0, "DOWN": 0}; cash = 0.0; stake = 0.0
        for r in rs:
            c, p, sd = int(r["c"]), float(r["px"]), r["side"]
            if r["a"] == "BUY": cash -= c * p + fee_total(c, p); stake += c * p; pos[sd] += c
            else:
                c = min(c, pos[sd])
                if c > 0: cash += c * p - fee_total(c, p); pos[sd] -= c
        cash += sum(pos[sd] * (1.0 if won[sd] else 0.0) for sd in pos)
        if stake > 0:
            o = out[s]; o[0] += 1; o[1] += cash; o[2] += stake
    return out


def label(base, ov):
    parts = [NAMES[k].format("on" if v else "off") if k in BOOL else NAMES[k].format(v) for k, v in ov.items() if k in NAMES]
    return "%s entry, %s" % (base, ", ".join(parts) if parts else "default responses")


def main():
    hours = float(sys.argv[1]) if len(sys.argv) > 1 else 72
    rng = random.Random(int(time.time()))
    st = stats(hours)
    vp = os.path.join(D, "variants.json")
    try: dyn = json.load(open(vp))
    except Exception: dyn = {}
    try:
        import sim
        static = {k: (v[1], dict(v[2])) for k, v in sim.VARIANTS.items() if k in sim._STATIC_V}
    except Exception:
        static = {}
    ret = {k: (v[1] / v[2], v[0]) for k, v in st.items() if v[2] > 0}
    if sum(v[0] for v in st.values()) < 60:
        say("Innovator: only %d settled strategy-rounds in the last %d h, too little to judge anything. Keeping the current %d experiments running." % (sum(v[0] for v in st.values()), hours, len(dyn))); 
        if dyn: return
    changed = False
    # 1) nothing is taken off the table. Experiments that are lagging are only reported, and they keep trading.
    lag = []
    for k in dyn:
        r = ret.get(k); refv = ret.get(dyn[k]["base"])
        if r and refv and r[1] >= MIN_RETIRE_ROUNDS and r[0] < refv[0] - 0.10:
            lag.append("%s %+.1f%% vs %+.1f%% for plain %s (%d rounds)" % (dyn[k]["label"], 100 * r[0], 100 * refv[0], dyn[k]["base"], r[1]))
    if lag:
        say("Lagging experiments (still trading, nothing is removed): " + "; ".join(lag[:3]), action="lag")
    if len(dyn) >= MAXDYN:
        say("Experiment board is full (%d). Not inventing more until you clear space; every experiment keeps trading." % len(dyn), action="board")
    # 3) invent up to 2 new experiments by changing one thing about the best performers
    pool = []
    for k, (b, ov) in static.items():
        if k in ret and ret[k][1] >= 25: pool.append((ret[k][0], k, b, dict(ov)))
    for k, v in dyn.items():
        if k in ret and ret[k][1] >= 25: pool.append((ret[k][0], k, v["base"], dict(v["ov"])))
    for b in BUILT_IN:
        if b in ret and ret[b][1] >= 25: pool.append((ret[b][0], b, b, {}))
    pool.sort(reverse=True)
    existing = {(v["base"], json.dumps(v["ov"], sort_keys=True)) for v in dyn.values()} | {(b, json.dumps(o, sort_keys=True)) for b, o in static.values()} | {(b, "{}") for b in BUILT_IN}
    made = 0
    bases_ranked = [b for b in sorted((b for b in BUILT_IN if b in ret and ret[b][1] >= 25 and True), key=lambda b: -ret[b][0])]
    for _ in range(12):
        if len(dyn) >= MAXDYN or made >= 2: break
        if pool:
            _, pk, base, ov = rng.choice(pool[:3])
            parent = "%s (%+.1f%% per dollar, %d rounds)" % (pk, 100 * ret[pk][0], ret[pk][1])
        else:
            base, ov, pk, parent = "distance", {}, "distance", "no results yet, so it starts from the default"
        ov = dict(ov)
        if rng.random() < 0.3:
            nb = rng.choice([b for b in BUILT_IN if b != base] or [base]); why = "it moves the same responses onto the %s entry (every entry stays on the table)" % nb; base = nb
        else:
            gene = rng.choice(list(LADDER)); cur = ov.get(gene)
            opts = [x for x in LADDER[gene] if x != cur]
            ov[gene] = rng.choice(opts); why = "it changes one thing: %s" % (NAMES[gene].format("on" if ov[gene] else "off") if gene in BOOL else NAMES[gene].format(ov[gene]))
        key = (base, json.dumps(ov, sort_keys=True))
        if key in existing: continue
        existing.add(key); made += 1
        nk = "v_x%d%d" % (int(time.time() * 1000) % 10000000, made)
        dyn[nk] = {"label": label(base, ov), "base": base, "ov": ov}; changed = True
        say("New experiment %s: starts from %s and %s. It trades pretend money from the next round; judged against %s over many rounds." % (dyn[nk]["label"], parent, why, base), action="new", key=nk, base=base, ov=ov)
    if changed:
        json.dump(dyn, open(vp, "w"))
    best = sorted(ret.items(), key=lambda kv: -kv[1][0])
    say("Scoreboard (per dollar staked, last %d h): best %s; worst %s. %d experiments live." % (hours, ", ".join("%s %+.1f%% (%d)" % (k, 100 * v[0], v[1]) for k, v in best[:3]), ", ".join("%s %+.1f%% (%d)" % (k, 100 * v[0], v[1]) for k, v in best[-2:]), len(dyn)), action="board")


if __name__ == "__main__":
    main()
