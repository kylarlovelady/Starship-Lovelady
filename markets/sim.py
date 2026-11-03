"""Fake-money simulator for the market agent. No real orders, no Kalshi account.
Several strategies, each with its own pretend account, trade Kalshi's LIVE 15-minute BTC prices:
open a small bet every round, then keep re-thinking: sell, add, or flip sides, with Kalshi's fee
and the buy/sell price gap counted on every trade. A plain hold-to-the-end control runs alongside,
so we can measure whether the active trading really adds anything."""
import json, math, os, time

START, MIN_BET, CAP, SLICE = 1000.0, 0.0, 100.0, 0.10    # fake dollars; bet limits (MIN_BET 0 = may skip a round)
ROUND_FRAC = 0.14      # most of the wallet one round may have at stake in total (set by the aggression dial)
KELLY = 1.85            # how hard it leans into an edge; set by the aggression dial
BROKER = None          # set by the collector while a live (real money) run exists
_LIVE = False
_SIM = None
_TK = None
FLOOR = 1.0             # smallest real bet: one contract is never more than $1
MAX_TRADES = 6          # per window per strategy, so fees cannot be churned away
MIN_PRICE, MAX_PRICE = 0.08, 0.92   # bigger-than-minimum bets only in this price range (no 1-cent long shots)
SIM_VERSION = 3
_EV, _CUR, _T = [], "", 0
_SZ = (None, None)      # contracts available at the best ask and best bid right now
EDGE_MIN = 0.03         # must beat price + fee by 3 cents per dollar before acting
STRATS = {
    "distance": "Distance to target only",
    "signals": "Distance plus all signals",
    "trend": "Price trend",
    "flow": "Order book and whale flow",
    "mood": "News and market mood",
    "hold": "Control: open once, hold to the end",
}


def fee(p):
    return 0.07 * p * (1 - p)


def fee_total(c, p):
    """Kalshi's fee on one order: 7% of contracts x price x (1 - price), rounded UP to the next cent."""
    return math.ceil(0.07 * c * p * (1 - p) * 100 - 1e-9) / 100.0


def logit(p):
    p = min(0.999, max(0.001, p))
    return math.log(p / (1 - p))


def sigm(x):
    return 1 / (1 + math.exp(-x))


def prob_up(name, pm, sigs, score, mood):
    g = lambda k: (sigs.get(k) or {}).get("score") or 0.0
    base = logit(pm) if pm is not None else 0.0
    if name == "distance":
        shift = 0.0
    elif name in ("signals", "hold"):
        shift = 1.2 * score / 100.0
    elif name == "trend":
        shift = 1.5 * g("momentum")
    elif name == "flow":
        shift = 0.5 * g("book") + 0.25 * g("whales") + 0.25 * g("bigtrades")
    else:
        shift = mood
    return sigm(base + shift)


DEFW = {"book": 0.20, "momentum": 0.15, "whales": 0.15, "bigtrades": 0.11, "news": 0.08, "fng": 0.04, "funding": 0.03,
        "trend_h": 0.12, "trend_w": 0.06, "levels": 0.06}
REFILL = 100.0         # fake dollars added when a pretend wallet runs dry (logged, and not counted as profit)
_W = dict(DEFW)
_MIX = []
_TRACE = []
_TRUST = {}


def mix(name, pm, sigs, score, mood):
    """How much each piece of information pushed the odds, as percent of the total push (sign shows direction)."""
    g = lambda k: (sigs.get(k) or {}).get("score") or 0.0
    terms = [("Distance to target and time left", logit(pm) if pm is not None else 0.0)]
    if name in ("signals", "hold"):
        shift = 1.2 * score / 100.0
        parts = {k: _W.get(k, 0.0) * g(k) for k in DEFW}
        tot = sum(parts.values())
        for k, v in parts.items():
            if tot and abs(v) > 1e-9:
                terms.append((SIGLAB[k], shift * v / tot))
    elif name == "trend":
        terms.append((SIGLAB["momentum"], 1.5 * g("momentum")))
    elif name == "flow":
        terms += [(SIGLAB["book"], 0.5 * g("book")), (SIGLAB["whales"], 0.25 * g("whales")), (SIGLAB["bigtrades"], 0.25 * g("bigtrades"))]
    elif name == "mood":
        a, b = 0.7 * g("news"), 0.3 * g("fng")
        tot = abs(a) + abs(b)
        if tot:
            terms += [(SIGLAB["news"], mood * a / tot), (SIGLAB["fng"], mood * b / tot)]
    tot = sum(abs(v) for _, v in terms) or 1.0
    out = [[l, round(100 * abs(v) / tot), 1 if v >= 0 else -1] for l, v in terms if abs(v) / tot >= 0.02]
    out.sort(key=lambda x: -x[1])
    return out



def build_trace(pm, p, price, strike, left, sigs, mix_, ask, bid, eU, eD):
    k_of = {"Order book": "book", "Price momentum": "momentum", "Whale moves": "whales", "News vibe": "news",
            "Fear & Greed": "fng", "Funding rate": "funding", "Big exchange trades": "bigtrades",
            "Hourly and daily trend": "trend_h", "Weekly and monthly trend": "trend_w", "Support and resistance": "levels"}
    L = []
    if strike:
        gap = price - strike
        L.append("BTC is $%s %s the target with %d:%02d left.%s" % (format(abs(gap), ",.0f"), "above" if gap >= 0 else "below", left // 60, left % 60,
                 (" From that alone the price model says Up %d%%." % round(pm * 100)) if pm is not None else ""))
    for lab, pc, sg in mix_:
        if lab.startswith("Distance"):
            continue
        k = k_of.get(lab)
        d = (sigs.get(k) or {}) if k else {}
        tr = _TRUST.get(k)
        L.append("%s%s: %s. It pushed the odds toward %s and carried %d%% of this decision.%s" % (
            lab, (" (%+d)" % round(100 * d["score"])) if d.get("score") is not None else "", d.get("detail", ""),
            "UP" if sg > 0 else "DOWN", pc, (" Learner's view: %s." % tr) if tr else ""))
    missing = [lab for lab, k in k_of.items() if not (sigs.get(k) or {}).get("ok")]
    if missing:
        L.append("No data from: %s. It could not use them." % ", ".join(missing))
    L.append("Putting it together it says Up %d%%. Kalshi sells Up at %d\u00a2 and Down at %d\u00a2." % (round(p * 100), round(ask * 100), round((1 - bid) * 100)))
    L.append("After fees the edge is Up %+d\u00a2, Down %+d\u00a2. It needs +%d\u00a2 to act." % (round(eU * 100), round(eD * 100), round(EDGE_MIN * 100)))
    return L


def auto_pick(sim):
    """For the Auto wallet: follow whichever practice strategy has the best proven record (needs 20 rounds first)."""
    best, bv = "signals", None
    for n, a in sim["acc"].items():
        if a["windows"] >= 20:
            v = a["pnl"] / (a["windows"] + 20.0)
            if bv is None or v > bv:
                best, bv = n, v
    pick = sim.get("auto_pick")
    if pick != best:
        sim.setdefault("autolog", []).append({"t": int(time.time()), "from": pick, "to": best,
            "why": ("Best record so far per round after fees (%d+ rounds each)." % 20) if bv is not None else "Not enough rounds yet, using the default."})
        sim["autolog"] = sim["autolog"][-20:]
        sim["auto_pick"] = best
    return best


def prices(kal, pm):
    """Return (bid, ask, synthetic) for the YES (up) side, as dollars."""
    if kal and kal.get("yes_pct") is not None:
        b = kal.get("yes_bid"); a = kal.get("yes_ask")
        m = kal["yes_pct"]
        b = (b if b is not None else m - 1) / 100.0
        a = (a if a is not None else m + 1) / 100.0
        return max(0.01, b), min(0.99, a), False
    m = pm if pm is not None else 0.5
    return max(0.01, m - 0.01), min(0.99, m + 0.01), True


def new_acc():
    return {"bal": START, "pnl": 0.0, "windows": 0, "wins": 0, "trades": 0, "mgmt": 0.0,
            "busts": 0, "pos": None, "w": None}


def buy(a, side, dollars, ask_up, bid_up, why=""):
    px = ask_up if side == "UP" else 1 - bid_up
    px = min(0.99, max(0.01, px))
    used = a["pos"]["cost"] if a["pos"] else 0.0
    if not (MIN_PRICE <= px <= MAX_PRICE):
        dollars = min(dollars, max(MIN_BET, FLOOR))   # no big bets on long shots or near-sure things
    dollars = min(dollars, a["bal"] / (1 + fee(px) / px), (CAP - used) / (1 + fee(px) / px))   # cap counts fees
    avail = _SZ[0] if side == "UP" else _SZ[1]       # cannot buy more than Kalshi has on offer at that price
    if avail is not None:
        dollars = min(dollars, avail * px)
    c = math.floor(dollars / px + 1e-9)                # Kalshi sells whole contracts only
    while c >= 1 and (c * px + fee_total(c, px) > a["bal"] + 1e-9 or c * px + fee_total(c, px) > (CAP - used) + 1e-9):
        c -= 1
    if c < 1:
        return False
    if _LIVE:                                          # real money: the order has to actually fill
        c = BROKER.trade("buy", _TK, side, c, ask_up, bid_up)
        if c < 1:
            return False
        _SIM["lt_t"] = _T; _SIM["unconf"] = True
    dollars = c * px
    f = fee_total(c, px)
    a["bal"] -= dollars + f
    if _LIVE:
        b_ = BROKER.balance(0)
        if b_ is not None:
            a["bal"] = b_
    p = a["pos"]
    if p and p["side"] == side:
        p["c"] += c; p["cost"] += dollars + f
    else:
        a["pos"] = {"side": side, "c": c, "cost": dollars + f}
    w = a["w"]
    w["cash"] -= dollars + f
    w["trades"] += 1; w["staked"] = max(w["staked"], a["pos"]["cost"])
    if w["first"] is None:
        w["first"] = {"side": side, "c": c, "cost": dollars + f}
    a["trades"] += 1
    _EV.append({"t": _T, "s": _CUR, "a": "BUY", "side": side, "c": round(c, 1), "px": round(px, 3), "d": round(dollars, 2), "bal": round(a["bal"], 2), "why": why, "mix": _MIX, "trace": _TRACE})
    return True


def sell(a, ask_up, bid_up, why=""):
    p = a["pos"]
    px = bid_up if p["side"] == "UP" else 1 - ask_up
    px = min(0.99, max(0.01, px))
    n = p["c"]
    if _LIVE:
        n = min(p["c"], BROKER.trade("sell", _TK, p["side"], p["c"], ask_up, bid_up))
        if n < 1:
            return False
        _SIM["lt_t"] = _T; _SIM["unconf"] = True
    got = n * px - fee_total(n, px)
    a["bal"] += got
    a["w"]["cash"] += got; a["w"]["trades"] += 1
    side = p["side"]
    if n < p["c"]:                                     # only part filled: keep the rest, try again next look
        p["cost"] *= (p["c"] - n) / p["c"]; p["c"] -= n
        why += " (only %d filled, the rest stays open)" % n
    else:
        a["pos"] = None
    a["trades"] += 1
    if _LIVE:
        b_ = BROKER.balance(0)
        if b_ is not None:
            a["bal"] = b_
    _EV.append({"t": _T, "s": _CUR, "a": "SELL", "side": side, "c": round(n, 1), "px": round(px, 3), "d": round(got, 2), "bal": round(a["bal"], 2), "why": why, "mix": _MIX, "trace": _TRACE})
    return True


def conviction(sigs):
    """How strongly the trusted sources agree. Returns (score 0..1, direction +1 Up / -1 Down / 0, plain-English reason).
    Strong lean + many trusted sources pointing the same way + the chart confirming it = high conviction."""
    tw = {"trusted": 1.3, "no clear edge": 0.9, "still learning": 0.8, "not trusted": 0.3}
    items = []
    for k, w in _W.items():
        v = (sigs.get(k) or {})
        if v.get("ok") and v.get("score") is not None:
            items.append((k, w * tw.get(_TRUST.get(k), 0.8), v["score"]))
    tot = sum(w for _, w, _ in items)
    if not tot:
        return 0.0, 0, "no data from any source"
    net = sum(w * s for _, w, s in items) / tot
    d = 1 if net > 0 else -1 if net < 0 else 0
    mass = sum(w * abs(s) for _, w, s in items)
    agree = sum(w * abs(s) for _, w, s in items if s * d > 0) / mass if mass and d else 0.0
    ch = [s for k, _, s in items if k in ("momentum", "trend_h") and abs(s) >= 0.05]
    confirm = (sum(1 for s in ch if s * d > 0) / len(ch)) if ch and d else 0.0
    strength = min(1.0, abs(net) / 0.30)
    c = 0.5 * strength + 0.3 * agree + 0.2 * confirm if abs(net) >= 0.03 else 0.0
    why = "conviction %d%% (lean %.0f%% of max, %d%% of the evidence agrees, chart %s)" % (
        round(100 * c), 100 * strength, round(100 * agree), "confirms" if confirm >= 0.99 else "partly confirms" if confirm > 0 else "does not confirm")
    return c, d, why


def conv_mult(sigs, side, edge):
    """Bet-size multiplier from conviction: sit out when weak, bet small on mild leans, full size on a hard signal.
    A big price edge alone (the target is nearly decided) still allows a small bet."""
    c, d, why = conviction(sigs)
    want = 1 if side == "UP" else -1
    m = 0.0 if (d != want and d != 0) or c < 0.25 else 0.4 if c < 0.45 else 0.7 if c < 0.65 else 1.0
    if m == 0.0 and edge >= 0.15:
        m = 0.4
        why += "; a large price edge still allows a small bet"
    return m, why


def size(edge, bal, pos_cost, mult=1.0, ref=None):
    ref = ref or START
    mult *= max(0.35, min(1.0, (bal + pos_cost) / ref))     # a shrinking wallet bets smaller, so it lasts more rounds
    if mult <= 0:
        return 0.0
    frac = min(SLICE, KELLY * max(0.0, edge)) * mult   # share of the wallet: bigger edge, bolder dial, higher conviction = bigger bet
    room = ROUND_FRAC * (bal + pos_cost) - pos_cost    # adds in one round cannot stack past this share of the wallet
    if room < FLOOR:
        return 0.0
    return max(FLOOR, min(frac * bal, CAP - pos_cost, room))


def settle_one(sim, name, a, w, pos, up_won, DIR, hour, src):
    """Pay out one account's finished round. The result comes from Kalshi (src says how we know)."""
    if pos:
        pay = pos["c"] if (pos["side"] == "UP") == up_won else 0.0
        a["bal"] += pay; w["cash"] += pay
    hold = None
    if w["first"]:
        f = w["first"]
        hold = (f["c"] if (f["side"] == "UP") == up_won else 0.0) - f["cost"]
    pnl = round(w["cash"], 4)
    a["pnl"] += pnl; a["windows"] += 1; a["wins"] += 1 if pnl > 0 else 0
    if hold is not None:
        a["mgmt"] += pnl - hold
    a.setdefault("hist", []).append({"t": w["start"], "pnl": round(pnl, 2), "outcome": "UP" if up_won else "DOWN",
                                     "hold": None if hold is None else round(hold, 2), "trades": w["trades"]})
    a["hist"] = a["hist"][-12:]
    if a["bal"] < max(MIN_BET, FLOOR, 5.0):  # fake account ran dry: add $100, count it (profit is judged on results, not the wallet)
        a["bal"] += REFILL; a["busts"] += 1
    h = sim["hours"].setdefault(str(hour), {"n": 0, "pnl": 0.0})
    h["n"] += 1; h["pnl"] = round(h["pnl"] + pnl, 3)
    with open(os.path.join(DIR, "sim_windows.jsonl"), "a") as f:
        f.write(json.dumps({"t": w["start"], "hour": hour, "strat": name, "pnl": pnl,
                            "hold_pnl": None if hold is None else round(hold, 4),
                            "trades": w["trades"], "staked": round(w["staked"], 2),
                            "outcome": "UP" if up_won else "DOWN", "src": src}) + "\n")


def finish_round(sim, pend, up_won, src, DIR):
    hour = time.localtime(pend["win"]).tm_hour
    for name, d in pend["accs"].items():
        a = sim["acc"].get(name)
        if a is not None and d.get("w"):
            settle_one(sim, name, a, d["w"], d.get("pos"), up_won, DIR, hour, src)
    r = pend.get("run")
    if r and r.get("w"):
        settle_run(sim, r, up_won, pend["last_price"], pend["strike"], hour, DIR, src)


def resolve_pending(sim, now, price, result_fn, DIR):
    """Settle finished rounds on Kalshi's official result. Wait up to 150 s for it; then fall back, and say so."""
    keep = []
    for pend in sim.get("pending", []):
        res = result_fn(pend["ticker"]) if (result_fn and pend.get("ticker")) else None
        src = "kalshi"
        if res is None and now >= pend["deadline"]:
            ly = pend.get("last_yes")
            if ly is not None and (ly >= 90 or ly <= 10):
                res, src = ("UP" if ly >= 90 else "DOWN"), "kalshi price at close"
            elif pend.get("strike"):
                res, src = ("UP" if pend["last_price"] > pend["strike"] else "DOWN"), "estimated"
        if res is None:
            keep.append(pend)
            continue
        finish_round(sim, pend, res == "UP", src, DIR)
    sim["pending"] = keep


SIGLAB = {"book": "Order book", "momentum": "Price momentum", "whales": "Whale moves",
          "bigtrades": "Big exchange trades", "news": "News vibe", "fng": "Fear & Greed", "funding": "Funding rate",
          "trend_h": "Hourly and daily trend", "trend_w": "Weekly and monthly trend", "levels": "Support and resistance"}


def newwin(win, sigs):
    return {"start": win, "cash": 0.0, "trades": 0, "staked": 0.0, "first": None, "side_end": None,
            "sigs": {k: round((v or {}).get("score") or 0.0, 2) for k, v in (sigs or {}).items() if (v or {}).get("ok")}}


def explain(run, w, up_won, price, strike, pnl, hold, src="kalshi"):
    """Plain-English account of one finished round of the user's wallet run."""
    out = "UP" if up_won else "DOWN"
    gap = abs(price - strike)
    if src == "kalshi":
        parts = ["Kalshi's official result: %s. BTC was about $%s %s the target at the close." % (out, format(gap, ",.0f"), "above" if up_won else "below")]
    else:
        parts = ["Kalshi had not posted its official result in time, so this is an estimate (%s): %s won." % (src, out)]
    f = w.get("first")
    end = w.get("side_end")
    if not f:
        parts.append("It never got a bet in this round, so nothing changed.")
        return " ".join(parts)
    if end:
        parts.append("It was holding %s at the end, so that bet %s." % (end, "paid out" if end == out else "lost"))
    else:
        parts.append("It had already sold everything before the round ended, so the result was locked in by its sells.")
    if f["side"] != out and (not end or end != out) and w["trades"] > 0:
        parts.append("Its first read (%s) was wrong." % f["side"])
    elif f["side"] != out and end == out:
        parts.append("Its first read (%s) was wrong, but it switched sides in time." % f["side"])
    agree, against = [], []
    for k, v in (w.get("sigs") or {}).items():
        if abs(v) >= 0.1:
            (agree if (v > 0) == up_won else against).append("%s (%+d)" % (SIGLAB.get(k, k), round(v * 100)))
    if agree:
        parts.append("Signals that pointed the right way: %s." % ", ".join(agree))
    if against:
        parts.append("Signals that pointed the wrong way: %s." % ", ".join(against))
    if hold is not None and w["trades"] > 1:
        d = pnl - hold
        if abs(d) < 0.005:
            parts.append("Same result as holding the first bet.")
        elif d > 0:
            parts.append("Moving around beat holding the first bet by $%.2f." % d)
        else:
            parts.append("Holding the first bet would have done $%.2f better; the extra trades and fees cost it." % -d)
    return " ".join(parts)


def settle_run(sim, r, up_won, price, strike, hour, DIR, src):
    run = sim.get("run")
    if not run or not r.get("w"):
        return
    a = run["acc"]; w = r["w"]; pos = r.get("pos")
    if pos:
        pay = pos["c"] if (pos["side"] == "UP") == up_won else 0.0
        if not run.get("live"):
            a["bal"] += pay
        w["cash"] += pay
        w["side_end"] = pos["side"]
    hold = None
    if w["first"]:
        f = w["first"]
        hold = (f["c"] if (f["side"] == "UP") == up_won else 0.0) - f["cost"]
    pnl = round(w["cash"], 4)
    a["pnl"] += pnl; a["windows"] += 1; a["wins"] += 1 if pnl > 0 else 0
    moves = [{k: e[k] for k in ("t", "a", "side", "d", "px", "bal", "why", "mix")} for e in sim["events"] if e["s"] == "run" and e["t"] >= w["start"]][-12:]
    rd = {"t": w["start"], "pnl": round(pnl, 2), "outcome": "UP" if up_won else "DOWN", "bal": round(a["bal"], 2), "src": src,
          "hold": None if hold is None else round(hold, 2), "trades": w["trades"], "moves": moves,
          "first": f["side"] if w["first"] else None, "end": w.get("side_end"), "mix": w.get("mix"), "sigs": w.get("sigs"),
          "p_open": w.get("p_open"), "staked": round(w["staked"], 2), "ticker": r.get("ticker"),
          "why": explain(run, w, up_won, price, strike, pnl, hold, src)}
    run["rounds"].append(rd); run["rounds"] = run["rounds"][-30:]
    try:
        with open(os.path.join(DIR, "run_log.jsonl"), "a") as fh:
            fh.write(json.dumps(dict(rd, run=run["id"], strat=run["strategy"], hour=hour)) + "\n")
    except OSError:
        pass
    if run["status"] == "running" and a["bal"] < max(MIN_BET, FLOOR, 5.0) and not a["pos"]:
        if run.get("live"):
            run["status"] = "broke"; run["stopped"] = time.time()
        else:                                                # pretend wallet ran dry: add $100 and log it, never counted as profit
            a["bal"] += REFILL; run["added"] = run.get("added", 0.0) + REFILL
            run.setdefault("refills", []).append({"t": int(time.time()), "amt": REFILL, "after": rd["t"]})


def save_run_off(DIR, reason, detail=""):
    """Turn the wallet run off (the normal stop path then closes any open bet)."""
    try:
        import alerts
        alerts.send("LIVE STOPPED (%s): %s" % (reason, detail or "see the Live view"), "Market agent: live stopped")
    except Exception:
        pass
    try:
        tmp = os.path.join(DIR, "run.json.tmp")
        with open(tmp, "w") as f:
            json.dump({"active": False, "live": True, "halted": reason, "detail": detail, "t": int(time.time())}, f)
        os.replace(tmp, os.path.join(DIR, "run.json"))
    except OSError:
        pass


def run_equity(a, bid, ask):
    p = a["pos"]
    return a["bal"] + (p["c"] * (bid if p["side"] == "UP" else 1 - ask) if p else 0.0)


def step(S, now, win, window_len, price, strike, pm, kal, sigs, score, enabled, DIR, C=None, run_cfg=None, result_fn=None):
    global BROKER, _LIVE, _SIM, _TK, ROUND_FRAC, KELLY, MIN_BET, CAP, SLICE, MAX_TRADES, EDGE_MIN, MIN_PRICE, MAX_PRICE, _SZ, _EV, _CUR, _T, _W, _MIX, _TRACE, _TRUST
    if C:
        MIN_BET, MAX_TRADES = C["min_bet"], int(C["max_trades"])
        CAP = C["cap"] if C["cap"] > 0 else 1e9               # 0 = no limit: it may use the whole wallet
        ag = min(1.0, max(0.0, float(C.get("aggression", 30)) / 100.0))
        SLICE = 0.04 + 0.96 * ag * ag                          # most of the wallet one bet may use
        EDGE_MIN = 0.06 - 0.05 * ag                            # how thin an edge it will act on
        ROUND_FRAC = 0.05 + 0.95 * ag * ag                    # total stake in one round, as a share of the wallet
        KELLY = 0.5 + 4.5 * ag                                 # how hard it leans into an edge
        MIN_PRICE, MAX_PRICE = C.get("min_price", MIN_PRICE), C.get("max_price", MAX_PRICE)
        if isinstance(C.get("weights"), dict):
            _W = dict(DEFW, **C["weights"])
        _TRUST = C.get("trust") or {}
    _SZ = ((kal or {}).get("yes_ask_size"), (kal or {}).get("yes_bid_size"))

    sim = S.setdefault("sim", {"acc": {}, "win": None, "strike": None, "hours": {}, "mood": 0.0, "synth": False, "joined": False})
    if sim.get("ver") != SIM_VERSION:                 # rules changed: start the fake accounts fresh, keep the old log
        try:
            os.replace(os.path.join(DIR, "sim_windows.jsonl"), os.path.join(DIR, "sim_windows.v%s.jsonl" % sim.get("ver", 1)))
        except OSError:
            pass
        try:
            os.replace(os.path.join(DIR, "run_log.jsonl"), os.path.join(DIR, "run_log.v%s.jsonl" % sim.get("ver", 1)))
        except OSError:
            pass
        sim.update({"ver": SIM_VERSION, "acc": {}, "win": None, "hours": {}, "joined": False, "run": None, "pending": [], "events": []})
    _SIM = sim
    for n in STRATS:
        sim["acc"].setdefault(n, new_acc())
    sim.setdefault("events", [])
    _EV, _T = sim["events"], now
    g = lambda k: (sigs.get(k) or {}).get("score") or 0.0
    sim["mood"] = 0.9 * sim["mood"] + 0.1 * (0.7 * g("news") + 0.3 * g("fng"))   # slow mood
    bid, ask, synth = prices(kal, pm)
    resolve_pending(sim, now, price, result_fn, DIR)
    if sim["win"] != win:
        if sim["win"] is not None:                       # park the finished round until Kalshi posts its result
            accs = {n: {"w": a["w"], "pos": a["pos"]} for n, a in sim["acc"].items() if a["w"]}
            rr = sim.get("run"); runp = None
            if rr and rr["acc"]["w"]:
                ra = rr["acc"]
                runp = {"w": ra["w"], "pos": ra["pos"], "ticker": sim.get("ticker")}
                ra["w"] = None; ra["pos"] = None
            for a in sim["acc"].values():
                a["w"] = None; a["pos"] = None
            if accs or runp:
                sim.setdefault("pending", []).append({"win": sim["win"], "ticker": sim.get("ticker"), "strike": sim.get("strike"),
                    "deadline": now + 150, "last_yes": sim.get("last_yes"), "last_price": price, "accs": accs, "run": runp})
        sim["win"] = win
        sim["strike"] = None; sim["ticker"] = None; sim["ready"] = False; sim["last_yes"] = None
    left = win + window_len - now
    if kal and strike and kal.get("ticker"):             # only ever use Kalshi's own target for this round
        sim["strike"] = float(strike); sim["ticker"] = kal["ticker"]
        if kal.get("yes_bid") is not None and kal.get("yes_ask") is not None:
            sim["last_yes"] = (kal["yes_bid"] + kal["yes_ask"]) / 2.0
        if not sim.get("ready"):
            sim["ready"] = True
            sim["joined"] = now - win <= 90              # the six practice strategies only join near the start
            for a in sim["acc"].values():
                a["w"] = newwin(win, sigs) if sim["joined"] else None
            r_ = sim.get("run")
            if r_ and r_["status"] == "running" and left > 45 and not r_["acc"]["w"]:
                r_["acc"]["w"] = newwin(win, sigs)
    # the user's own wallet run (Start / Stop on the Live View)
    rc = run_cfg or {}
    run = sim.get("run")
    if rc.get("active") and (not run or run["id"] != rc.get("id")):
        st = rc.get("strategy") if rc.get("strategy") in STRATS else "signals"
        acc = new_acc(); acc["bal"] = float(rc.get("start", 1000))
        run = sim["run"] = {"id": rc.get("id"), "strategy": st, "start": acc["bal"], "acc": acc, "rounds": [],
                            "curve": [], "started": now, "stopped": None, "status": "running", "live": bool(rc.get("live"))}
        sim["k_ok"] = now; sim["unconf"] = False
        if left > 45 and sim.get("ready"):
            acc["w"] = newwin(win, sigs)
    elif run and run["status"] == "running" and not rc.get("active"):
        a_ = run["acc"]
        _CUR = "run"; _LIVE = bool(run.get("live") and BROKER); _TK = sim.get("ticker")
        if a_["pos"]:
            a_["w"]["side_end"] = None
            sell(a_, ask, bid, "You pressed Stop: closing the open bet at today's price")
            if a_["pos"] and _LIVE:
                run["warn"] = "Could not close the open bet. Close it in the Kalshi app."
        w_ = a_["w"]
        if w_ and w_["trades"]:
            a_["pnl"] += round(w_["cash"], 4); a_["windows"] += 1
            run["rounds"].append({"t": w_["start"], "pnl": round(w_["cash"], 2), "outcome": "STOPPED", "bal": round(a_["bal"], 2),
                                  "hold": None, "trades": w_["trades"], "moves": [],
                                  "why": "You stopped it mid-round, so this round was cut short and settled at the sell price."})
        a_["w"] = None
        run["status"] = "stopped"; run["stopped"] = now
    items = [(n, n, a, enabled) for n, a in sim["acc"].items()]
    if run and run["status"] == "running":
        items.append(("run", auto_pick(sim) if run["strategy"] == "auto" else run["strategy"], run["acc"], True))
    for name, pname, a, enabled in items:
        w = a["w"]
        if not w or not kal or not sim.get("ready"):
            continue                                       # never trade without Kalshi's live price for this round
        _CUR = name
        _LIVE = bool(name == "run" and run and run.get("live") and BROKER)
        _TK = sim.get("ticker")
        if _LIVE:
            if BROKER.halt:                                # too many rejected orders: stop and say why
                save_run_off(DIR, "live_error", BROKER.halt)
                continue
            if now - sim.get("k_ok", now) > 60:             # watchdog: no clear reading from Kalshi for a minute
                save_run_off(DIR, "watchdog", "Lost contact with Kalshi for over a minute. Check your Kalshi account for an open bet.")
                run["warn"] = "Lost contact with Kalshi. Check the Kalshi app for an open bet."
                continue
            kp = BROKER.position(_TK) if _TK else {}
            if kp is None:                                   # never trade blind
                a["now"] = dict(a.get("now") or {}, act="waiting", why="Could not read your position from Kalshi just now, so it is not trading this second.")
                continue
            sim["k_ok"] = now
            loc = a["pos"]
            same = (not kp and not loc) or bool(kp and loc and kp["side"] == loc["side"] and abs(kp["c"] - loc["c"]) < 0.5)
            if same:
                sim["unconf"] = False
                if kp and loc:
                    loc["cost"] = kp["cost"] or loc["cost"]
            elif sim.get("unconf") and now - sim.get("lt_t", 0) < 10:     # Kalshi's list can lag a second or two behind a fill
                a["now"] = dict(a.get("now") or {}, act="waiting", why="Waiting for Kalshi to show the fill before it does anything else.")
                continue
            elif sim.get("unconf"):
                save_run_off(DIR, "mismatch", "After its own order, Kalshi's position (%s) still did not match what the agent expected (%s)." % (kp or "none", loc or "none"))
                run["warn"] = "Positions disagreed with Kalshi after an order. Check the Kalshi app."
                continue
            else:                                            # something changed outside the agent (for example a bet placed in the Kalshi app): Kalshi is right
                a["pos"] = ({"side": kp["side"], "c": kp["c"], "cost": kp["cost"]} if kp else None)
                try:
                    import alerts
                    alerts.send("Position changed outside the agent: Kalshi now shows %s. Agent is following Kalshi." % (kp or "none"))
                except Exception:
                    pass
            if not a["pos"] and now - sim.get("lb_t", 0) >= 10:     # real cash balance from Kalshi
                sim["lb_t"] = now
                b_ = BROKER.balance(0)
                if b_ is not None:
                    a["bal"] = b_
        p = prob_up(pname, pm, sigs, score, sim["mood"])
        _MIX = mix(pname, pm, sigs, score, sim["mood"])
        if not enabled:                                   # switched off: close out safely, then idle
            if a["pos"]:
                sell(a, ask, bid, "Switched off: closing the open bet")
            continue
        if left <= 5:
            continue
        gate = pname in ("signals", "hold")                   # only the strategies that use the signals are gated by conviction
        ref = (run["start"] + run.get("added", 0.0)) if name == "run" else START
        side_p = lambda s: p if s == "UP" else 1 - p
        ask_s = lambda s: ask if s == "UP" else 1 - bid
        bid_s = lambda s: bid if s == "UP" else 1 - ask
        eU = side_p("UP") - ask_s("UP") - fee(ask_s("UP"))
        eD = side_p("DOWN") - ask_s("DOWN") - fee(ask_s("DOWN"))
        c_ = lambda x: "%d" % round(x * 100)
        _TRACE = build_trace(pm, p, price, sim.get("strike"), int(max(0, left)), sigs, _MIX, ask, bid, eU, eD)
        act = "waiting"
        why = "It thinks Up is %s%%. Kalshi sells Up at %s\u00a2 and Down at %s\u00a2. Edge after fees: Up %+d\u00a2, Down %+d\u00a2 (needs +%d\u00a2 to trade)." % (
            c_(p), c_(ask_s("UP")), c_(ask_s("DOWN")), round(eU * 100), round(eD * 100), round(EDGE_MIN * 100))
        if w["first"] is None and w["trades"] == 0 and (MIN_BET > 0 or max(eU, eD) > EDGE_MIN):   # min bet above 0 = must bet every round
            s = "UP" if p >= 0.5 else "DOWN"
            e = side_p(s) - ask_s(s) - fee(ask_s(s))
            if MIN_BET <= 0:
                s = "UP" if eU >= eD else "DOWN"; e = max(eU, eD)
            cm, cwhy = conv_mult(sigs, s, e) if gate else (1.0, "")
            if gate and cm == 0.0 and MIN_BET <= 0:
                act = "waiting"; why += " Sitting out: not enough agreement between its sources (" + cwhy + ")."
            else:
                buy(a, s, size(e, a["bal"], 0.0, max(cm, 0.4) if MIN_BET > 0 else cm, ref) if e > EDGE_MIN else max(MIN_BET, FLOOR), ask, bid,
                    (("Opening bet: it thinks %s is more likely (%s%% up) and has to bet every round." if MIN_BET > 0 else "Opening bet: it sees a real edge on %s (it thinks %s%% up).") % (s, c_(p))) + ((" Bet size set by " + cwhy + ".") if gate else ""))
                act = "opened"
                if w.get("mix") is None:
                    w["mix"] = _MIX; w["p_open"] = round(p, 3)
        elif w["first"] is None and w["trades"] == 0 and not a["pos"]:
            act = "waiting"; why += " Smallest bet is $0, so it sits out until it sees a real edge."
        elif pname == "hold":
            act = "holding to the end"
        elif w["trades"] >= MAX_TRADES:
            act = "trade limit reached"
        else:
            pos = a["pos"]
            sold = False
            if pos:
                s = pos["side"]
                sell_now = bid_s(s) - fee(bid_s(s))
                if sell_now > side_p(s) + 0.01:           # selling beats holding by our own odds
                    sell(a, ask, bid, "Selling %s: it can sell at %s\u00a2 but by its own odds holding is worth only %s\u00a2 per contract." % (s, c_(sell_now), c_(side_p(s))))
                    sold = True; act = "sold"
            if not sold:
                for s, e in (("UP", eU), ("DOWN", eD)):
                    if a["pos"] and a["pos"]["side"] != s:
                        continue
                    if e > EDGE_MIN:
                        cm, cwhy = conv_mult(sigs, s, e) if gate else (1.0, "")
                        if cm == 0.0:
                            why += " Not adding: " + cwhy + "."
                            continue
                        buy(a, s, size(e, a["bal"], a["pos"]["cost"] if a["pos"] else 0.0, cm, ref), ask, bid,
                            "Edge: it thinks %s is %s%% likely but Kalshi asks %s\u00a2 (+%d\u00a2 after fees)." % (s, c_(side_p(s)), c_(ask_s(s)), round(e * 100)) + ((" Bet size set by " + cwhy + ".") if gate else ""))
                        act = "bought"
                        break
                else:
                    act = "holding" if a["pos"] else "waiting"
        a["now"] = {"p": round(p, 3), "ask": round(ask, 3), "bid": round(bid, 3), "eU": round(eU, 3), "eD": round(eD, 3), "act": act, "why": why, "mix": _MIX, "trace": _TRACE, "conv": (round(conviction(sigs)[0], 2) if gate else None)}
    ranked = []
    for name, a in sim["acc"].items():
        ranked.append({"key": name, "label": STRATS[name], "bal": round(a["bal"], 2), "pnl": round(a["pnl"], 2),
                       "windows": a["windows"], "win_pct": round(100 * a["wins"] / a["windows"], 1) if a["windows"] else None,
                       "trades": a["trades"], "mgmt": round(a["mgmt"], 2), "busts": a["busts"], "trust": round(100 * (a["wins"] + 5.0) / (a["windows"] + 10.0), 1),
                       "open": (a["pos"]["side"] if a["pos"] else None), "now": a.get("now"), "hist": a.get("hist", [])[-8:],
                       "pos": ({"side": a["pos"]["side"], "c": round(a["pos"]["c"], 1), "cost": round(a["pos"]["cost"], 2),
                                "value": round(a["pos"]["c"] * (bid if a["pos"]["side"] == "UP" else 1 - ask), 2)} if a["pos"] else None)})
    ranked.sort(key=lambda r: -r["pnl"])
    runout = None
    if run:
        a_ = run["acc"]
        if run.get("live") and BROKER and not a_["pos"] and now - sim.get("lb_t", 0) >= 10:   # keep the shown balance equal to Kalshi's
            sim["lb_t"] = now
            b_ = BROKER.balance(0)
            if b_ is not None:
                a_["bal"] = b_
        eq = run_equity(a_, bid, ask)
        infl = 0.0                                        # last round's bet still waiting for Kalshi's official result
        for pd_ in sim.get("pending", []):
            rp = pd_.get("run")
            if rp and rp.get("pos"):
                ly = (pd_.get("last_yes") if pd_.get("last_yes") is not None else 50.0) / 100.0
                infl += rp["pos"]["c"] * (ly if rp["pos"]["side"] == "UP" else 1 - ly)
        eq += infl
        fl = float((C or {}).get("floor") or 0)
        if run.get("live") and run["status"] == "running" and fl > 0 and eq < fl and rc.get("active"):
            save_run_off(DIR, "floor", "Account value $%.2f fell below your floor of $%.2f" % (eq, fl))
            run["halt"] = "Your loss floor of $%.2f was hit (account value $%.2f). It is closing the open bet and stopping." % (fl, eq)
        if run["status"] == "running":
            c_ = run["curve"]
            if not c_ or now - c_[-1][0] >= 10:
                c_.append([int(now), round(eq - run.get("added", 0.0), 2)])
            run["curve"] = c_[-500:]
        runout = {"id": run["id"], "strategy": run["strategy"], "label": STRATS.get(run["strategy"]) or "Auto: follows the best-performing strategy", "using": (sim.get("auto_pick") if run["strategy"] == "auto" else run["strategy"]), "autolog": sim.get("autolog", [])[-6:], "status": run["status"],
                  "live": bool(run.get("live")), "slip_avg": (round(sum(BROKER.slips) / len(BROKER.slips), 2) if (BROKER and BROKER.slips) else None), "warn": run.get("warn"), "halt": run.get("halt") or (rc.get("detail") if rc.get("halted") else None), "start": run["start"], "bal": round(a_["bal"], 2), "equity": round(eq, 2), "inflight": round(infl, 2), "k_age": round(max(0.0, now - sim.get("k_ok", now)), 1), "pnl": round(eq - run.get("added", 0.0) - run["start"], 2), "added": round(run.get("added", 0.0), 2), "refills": len(run.get("refills", [])),
                  "windows": a_["windows"], "wins": a_["wins"], "trades": a_["trades"], "started": run["started"],
                  "stopped": run["stopped"], "in_round": bool(a_["w"]), "round_cash": round(a_["w"]["cash"], 2) if a_["w"] else None,
                  "now": a_.get("now"), "rounds": run["rounds"][-15:], "events": [e for e in sim["events"] if e["s"] == "run"][-40:], "curve": run["curve"][-300:],
                  "pos": ({"side": a_["pos"]["side"], "c": round(a_["pos"]["c"], 1), "cost": round(a_["pos"]["cost"], 2),
                           "value": round(a_["pos"]["c"] * (bid if a_["pos"]["side"] == "UP" else 1 - ask), 2)} if a_["pos"] else None)}
    sim["events"] = sim["events"][-120:]
    return {"events": sim["events"][-60:], "strike": sim["strike"], "win": sim["win"], "yes": [round(bid, 3), round(ask, 3)],
            "on": enabled, "synthetic": False, "live": bool(kal and sim.get("ready")), "start": START, "min_bet": MIN_BET, "cap": (CAP if CAP < 1e8 else 0),
            "strategies": ranked, "hours": sim["hours"], "run": runout}
