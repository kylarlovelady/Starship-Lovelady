"""Fake-money simulator for the market agent. No real orders, no Kalshi account.
Several strategies, each with its own pretend account, trade Kalshi's LIVE 15-minute BTC prices:
open a small bet every round, then keep re-thinking: sell, add, or flip sides, with Kalshi's fee
and the buy/sell price gap counted on every trade. A plain hold-to-the-end control runs alongside,
so we can measure whether the active trading really adds anything."""
import json, math, os, time

START, MIN_BET, CAP, SLICE = 1000.0, 1.0, 100.0, 0.10    # fake dollars; bet limits
MAX_TRADES = 6          # per window per strategy, so fees cannot be churned away
MIN_PRICE, MAX_PRICE = 0.08, 0.92   # bigger-than-minimum bets only in this price range (no 1-cent long shots)
SIM_VERSION = 2
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
        shift = 0.6 * g("book") + 0.4 * g("whales")
    else:
        shift = mood
    return sigm(base + shift)


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
        dollars = min(dollars, MIN_BET)              # no big bets on long shots or near-sure things
    dollars = min(dollars, a["bal"] / (1 + fee(px) / px), (CAP - used) / (1 + fee(px) / px))   # cap counts fees
    avail = _SZ[0] if side == "UP" else _SZ[1]       # cannot buy more than Kalshi has on offer at that price
    if avail is not None:
        dollars = min(dollars, avail * px)
    if dollars < 0.5:
        return False
    c = dollars / px
    f = fee(px) * c
    a["bal"] -= dollars + f
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
    _EV.append({"t": _T, "s": _CUR, "a": "BUY", "side": side, "c": round(c, 1), "px": round(px, 3), "d": round(dollars, 2), "why": why})
    return True


def sell(a, ask_up, bid_up, why=""):
    p = a["pos"]
    px = bid_up if p["side"] == "UP" else 1 - ask_up
    px = min(0.99, max(0.01, px))
    got = p["c"] * px - fee(px) * p["c"]
    a["bal"] += got
    a["w"]["cash"] += got; a["w"]["trades"] += 1
    side = p["side"]
    a["pos"] = None
    a["trades"] += 1
    _EV.append({"t": _T, "s": _CUR, "a": "SELL", "side": side, "c": round(p["c"], 1), "px": round(px, 3), "d": round(got, 2), "why": why})


def size(edge, bal, pos_cost):
    d = MIN_BET + 400 * max(0.0, edge - EDGE_MIN)
    return max(MIN_BET, min(d, CAP - pos_cost, SLICE * bal if bal * SLICE > MIN_BET else MIN_BET))


def settle(sim, up_won, DIR, hour, synthetic):
    for name, a in sim["acc"].items():
        w = a["w"]
        if not w:
            continue
        pos = a["pos"]
        if pos:
            pay = pos["c"] if (pos["side"] == "UP") == up_won else 0.0
            a["bal"] += pay; w["cash"] += pay
            a["pos"] = None
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
        if a["bal"] < MIN_BET:                   # fake account ran dry: refill and count it
            a["bal"] = START; a["busts"] += 1
        h = sim["hours"].setdefault(str(hour), {"n": 0, "pnl": 0.0})
        h["n"] += 1; h["pnl"] = round(h["pnl"] + pnl, 3)
        with open(os.path.join(DIR, "sim_windows.jsonl"), "a") as f:
            f.write(json.dumps({"t": w["start"], "hour": hour, "strat": name, "pnl": pnl,
                                "hold_pnl": None if hold is None else round(hold, 4),
                                "trades": w["trades"], "staked": round(w["staked"], 2),
                                "outcome": "UP" if up_won else "DOWN", "synthetic": synthetic}) + "\n")
        a["w"] = None


def step(S, now, win, window_len, price, strike, pm, kal, sigs, score, enabled, DIR, C=None):
    global MIN_BET, CAP, SLICE, MAX_TRADES, EDGE_MIN, MIN_PRICE, MAX_PRICE, _SZ, _EV, _CUR, _T
    if C:
        MIN_BET, CAP, SLICE, EDGE_MIN, MAX_TRADES = C["min_bet"], C["cap"], C["slice"], C["edge_min"], int(C["max_trades"])
        MIN_PRICE, MAX_PRICE = C.get("min_price", MIN_PRICE), C.get("max_price", MAX_PRICE)
    _SZ = ((kal or {}).get("yes_ask_size"), (kal or {}).get("yes_bid_size"))

    sim = S.setdefault("sim", {"acc": {}, "win": None, "strike": None, "hours": {}, "mood": 0.0, "synth": False, "joined": False})
    if sim.get("ver") != SIM_VERSION:                 # rules changed: start the fake accounts fresh, keep the old log
        try:
            os.replace(os.path.join(DIR, "sim_windows.jsonl"), os.path.join(DIR, "sim_windows.v%s.jsonl" % sim.get("ver", 1)))
        except OSError:
            pass
        sim.update({"ver": SIM_VERSION, "acc": {}, "win": None, "hours": {}, "joined": False})
    for n in STRATS:
        sim["acc"].setdefault(n, new_acc())
    sim.setdefault("events", [])
    _EV, _T = sim["events"], now
    g = lambda k: (sigs.get(k) or {}).get("score") or 0.0
    sim["mood"] = 0.9 * sim["mood"] + 0.1 * (0.7 * g("news") + 0.3 * g("fng"))   # slow mood
    bid, ask, synth = prices(kal, pm)
    if sim["win"] != win:
        if sim["win"] is not None and sim["strike"]:
            hour = time.localtime(sim["win"]).tm_hour
            settle(sim, price > sim["strike"], DIR, hour, sim["synth"])
        sim["win"] = win
        k = float(strike) if strike and abs(float(strike) / price - 1) < 0.02 else price
        sim["strike"] = k
        sim["synth"] = synth
        sim["joined"] = now - win <= 90                  # only join a window near its start
        for a in sim["acc"].values():
            a["w"] = {"start": win, "cash": 0.0, "trades": 0, "staked": 0.0, "first": None} if sim["joined"] else None
    left = win + window_len - now
    for name, a in sim["acc"].items():
        w = a["w"]
        if not w:
            continue
        _CUR = name
        p = prob_up(name, pm, sigs, score, sim["mood"])
        if not enabled:                                   # switched off: close out safely, then idle
            if a["pos"]:
                sell(a, ask, bid, "Switched off: closing the open bet")
            continue
        if left <= 5:
            continue
        side_p = lambda s: p if s == "UP" else 1 - p
        ask_s = lambda s: ask if s == "UP" else 1 - bid
        bid_s = lambda s: bid if s == "UP" else 1 - ask
        eU = side_p("UP") - ask_s("UP") - fee(ask_s("UP"))
        eD = side_p("DOWN") - ask_s("DOWN") - fee(ask_s("DOWN"))
        c_ = lambda x: "%d" % round(x * 100)
        act = "waiting"
        why = "It thinks Up is %s%%. Kalshi sells Up at %s\u00a2 and Down at %s\u00a2. Edge after fees: Up %+d\u00a2, Down %+d\u00a2 (needs +%d\u00a2 to trade)." % (
            c_(p), c_(ask_s("UP")), c_(ask_s("DOWN")), round(eU * 100), round(eD * 100), round(EDGE_MIN * 100))
        if w["first"] is None and w["trades"] == 0:       # bet every round, smallest size unless the edge is big
            s = "UP" if p >= 0.5 else "DOWN"
            e = side_p(s) - ask_s(s) - fee(ask_s(s))
            buy(a, s, size(e, a["bal"], 0.0) if e > EDGE_MIN else MIN_BET, ask, bid,
                "Opening bet: it thinks %s is more likely (%s%% up) and has to bet every round." % (s, c_(p)))
            act = "opened"
        elif name == "hold":
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
                        buy(a, s, size(e, a["bal"], a["pos"]["cost"] if a["pos"] else 0.0), ask, bid,
                            "Edge: it thinks %s is %s%% likely but Kalshi asks %s\u00a2 (+%d\u00a2 after fees)." % (s, c_(side_p(s)), c_(ask_s(s)), round(e * 100)))
                        act = "bought"
                        break
                else:
                    act = "holding" if a["pos"] else "waiting"
        a["now"] = {"p": round(p, 3), "ask": round(ask, 3), "bid": round(bid, 3), "eU": round(eU, 3), "eD": round(eD, 3), "act": act, "why": why}
    ranked = []
    for name, a in sim["acc"].items():
        ranked.append({"key": name, "label": STRATS[name], "bal": round(a["bal"], 2), "pnl": round(a["pnl"], 2),
                       "windows": a["windows"], "win_pct": round(100 * a["wins"] / a["windows"], 1) if a["windows"] else None,
                       "trades": a["trades"], "mgmt": round(a["mgmt"], 2), "busts": a["busts"],
                       "open": (a["pos"]["side"] if a["pos"] else None), "now": a.get("now"), "hist": a.get("hist", [])[-8:],
                       "pos": ({"side": a["pos"]["side"], "c": round(a["pos"]["c"], 1), "cost": round(a["pos"]["cost"], 2),
                                "value": round(a["pos"]["c"] * (bid if a["pos"]["side"] == "UP" else 1 - ask), 2)} if a["pos"] else None)})
    ranked.sort(key=lambda r: -r["pnl"])
    sim["events"] = sim["events"][-120:]
    return {"events": sim["events"][-60:], "strike": sim["strike"], "win": sim["win"], "yes": [round(bid, 3), round(ask, 3)],
            "on": enabled, "synthetic": sim["synth"], "start": START, "min_bet": MIN_BET, "cap": CAP,
            "strategies": ranked, "hours": sim["hours"]}
