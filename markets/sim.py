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
FLOOR = 5.0             # smallest bet: never less than $5 (Kylar)
MAX_TRADES = 6          # per window per strategy, so fees cannot be churned away
MIN_PRICE, MAX_PRICE = 0.08, 0.92   # bigger-than-minimum bets only in this price range (no 1-cent long shots)
ENTRY_MIN = 0.15        # never pay less than this per contract (15 cents): cheap long shots almost always expire worthless
ENTRY_MAX = 0.80        # never pay more than this per contract (80 cents): above it one miss costs several wins
STAGE_FIRST = 0.40      # the first buy of a round is this share of the intended size; the rest is added later if the edge holds
STAGE_GAP = 45          # seconds to wait between buys in one round, so a position is built over minutes, not in one go
ENTRY_BLOCK = []       # price ranges (cents) that the agent's own recordings show lose money after fees
BLACKOUT = None         # name of a big scheduled news event happening now: no new bets
PATTERN_BAD = []        # (feature, bucket) pairs that lost money in training and in later test rounds
MIN_HOLD = 0            # seconds: optional hard timer after a buy (off; the profit rule below replaces it)
MIN_PROFIT_USD = 5.0    # never sell a winner for less than this much profit AFTER fees (a few cents of profit is eaten by the cost of trading)
STOP_SMALL = 10.0   # a bet costing less than this is never cut: losing it is fine, so let it ride
STOP_ON, STOP_PCT = 1, 0.35   # cut a loss: once a bet is down this share of its cost (after fees, at the price it could sell for), sell it instead of riding it to the end
MIN_PROFIT_PCT = 0.02   # ...or this share of the money in the bet, whichever is bigger (so big bets need proportionally more)
_QSRC = None           # where the current Kalshi quote came from: "book" (live order book) or "list" (lagging market list)
_FEAT = {}              # what the market looks like right now: seconds into the round, model odds, signal score
EXIT_ON, EXIT_P, EXIT_D = 1, 8.0, 4.0   # take-profit: once up EXIT_P cents per contract, sell if it falls EXIT_D cents from the best point
SKIPPED = {}            # entries refused by the price cap, for the log
SIM_VERSION = 5
_EV, _CUR, _T = [], "", 0
_DIR = None
_QUOTE = (None, None)  # (ask, bid) of Up when the trade was decided
_SZ = (None, None)      # contracts available at the best ask and best bid right now
EDGE_MIN = 0.03         # must beat price + fee by 3 cents per dollar before acting
STRATS = {
    "swing": "Ride the swings (Kylar's strategy)",
    "distance": "Distance to target only",
    "signals": "Distance plus all signals",
    "trend": "Price trend",
    "flow": "Order book and whale flow",
    "mood": "News and market mood",
    "hold": "Control: open once, hold to the end",
}
# REACTION TESTS: the same entry logic ("distance") with a different way of reacting once in a bet. Each has its own pretend $1,000 and trades live beside the others,
# so the scoreboard shows which response (hold, trail, cut tight or loose, add or not, wait to buy) actually earns the most after fees.
ODDS_MARGIN = 0.04      # sell on its own odds only if selling beats holding by this much (selling on a 1c edge lost money in the 24h review)
UNPROVEN_CAP = 25.0     # no strategy may put more than this into one round until the evidence earns it (0 = off); lift with config "unproven_cap". Was 50; bets over $25 lost, under $25 broke even (24 h review 2026-11-05)
AUTO_MIN_ROUNDS = 80    # rounds a strategy needs before the Auto wallet may follow it
FLIP = 0                # reaction test: bet the OPPOSITE of what the strategy thinks
ODDS_SELL = 1           # sell when its own odds say selling beats holding (off for the pure-hold test)
FLAT_BET = 0.0          # size test: bet exactly this many dollars per round (in steps) whenever the strategy wants in, ignoring the edge-based sizing (0 = off)
TAKE_PCT = 0.0          # reaction test (Kylar 2026-11-07): sell the whole bet as soon as it is up this share of its cost after fees at the price it can sell for (0 = off)
ENTRY_AFTER = 0         # do not open a bet until this many seconds into the round
ALL_IN = 0              # reaction test only: bet the WHOLE wallet on the favourite, every round, no edge test, no staging (sniping test); the book depth still limits the fill
VARIANTS = {
    "v_hold": ("Reaction test: never sell early, hold to the end", "distance", {"STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0}),
    "v_trail": ("Reaction test: trail the profit (up 30\u00a2, sell if it falls 10\u00a2)", "distance", {"EXIT_P": 30.0, "EXIT_D": 10.0}),
    "v_trail_wide": ("Reaction test: trail wide (up 50\u00a2, sell if it falls 15\u00a2)", "distance", {"EXIT_P": 50.0, "EXIT_D": 15.0}),
    "v_cut_tight": ("Reaction test: cut losses tight (20%, even small bets)", "distance", {"STOP_PCT": 0.20, "STOP_SMALL": 5.0}),
    "v_cut_loose": ("Reaction test: cut losses loose (60%)", "distance", {"STOP_PCT": 0.60}),
    "v_no_cut": ("Reaction test: never cut a loss", "distance", {"STOP_ON": 0}),
    "v_one_shot": ("Reaction test: one bet per round, no adding", "distance", {"MAX_TRADES": 1}),
    "v_adds": ("Reaction test: keep adding to a winner (up to 8 buys)", "distance", {"MAX_TRADES": 8, "STAGE_GAP": 25}),
    "v_mood_flip": ("Reaction test: bet the opposite of the Mood strategy", "mood", {"FLIP": 1}),
    "v_flow_flip": ("Reaction test: bet the opposite of the Flow strategy", "flow", {"FLIP": 1}),
    "v_late": ("Reaction test: wait 5 minutes before the first bet", "distance", {"ENTRY_AFTER": 300}),
    # TAKE-PROFIT EARLY (Kylar, 2026-11-07 10:20): bet early, sell everything the moment the bet is up X% after fees, otherwise hold to the end. No loss-cutting, no odds-selling.
    "v_take25": ("Reaction test: bet early, sell at +25% (Kylar's idea), else hold", "distance", {"TAKE_PCT": 0.25, "STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "MIN_PROFIT_USD": 0.25}),
    "v_take15": ("Reaction test: bet early, sell at +15%, else hold", "distance", {"TAKE_PCT": 0.15, "STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "MIN_PROFIT_USD": 0.25}),
    "v_take40": ("Reaction test: bet early, sell at +40%, else hold", "distance", {"TAKE_PCT": 0.40, "STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "MIN_PROFIT_USD": 0.25}),
    "v_take5": ("Reaction test: bet early, sell at +5%, else hold", "distance", {"TAKE_PCT": 0.05, "STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "MIN_PROFIT_USD": 0.25}),
    "v_take10": ("Reaction test: bet early, sell at +10%, else hold", "distance", {"TAKE_PCT": 0.1, "STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "MIN_PROFIT_USD": 0.25}),
    "v_take20": ("Reaction test: bet early, sell at +20%, else hold", "distance", {"TAKE_PCT": 0.2, "STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "MIN_PROFIT_USD": 0.25}),
    "v_take30": ("Reaction test: bet early, sell at +30%, else hold", "distance", {"TAKE_PCT": 0.3, "STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "MIN_PROFIT_USD": 0.25}),
    "v_take50": ("Reaction test: bet early, sell at +50%, else hold", "distance", {"TAKE_PCT": 0.5, "STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "MIN_PROFIT_USD": 0.25}),
    "v_take75": ("Reaction test: bet early, sell at +75%, else hold", "distance", {"TAKE_PCT": 0.75, "STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "MIN_PROFIT_USD": 0.25}),
    "v_take100": ("Reaction test: bet early, sell at +100%, else hold", "distance", {"TAKE_PCT": 1.0, "STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "MIN_PROFIT_USD": 0.25}),
    # LATER-ENTRY HOLD TESTS (2026-11-07 backtest: favourite bought 120 s in and held was the best cell, +4.9% per $, still inside the noise): same distance entry, no selling, wait before the first bet.
    "v_hold_after60": ("Reaction test: hold to the end, first bet after 1 minute", "distance", {"STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "ENTRY_AFTER": 60}),
    "v_hold_after120": ("Reaction test: hold to the end, first bet after 2 minutes", "distance", {"STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "ENTRY_AFTER": 120}),
    "v_take25_cheap": ("Reaction test: early bet only up to 55c, sell at +25%, else hold", "distance", {"TAKE_PCT": 0.25, "STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "MIN_PROFIT_USD": 0.25, "ENTRY_MAX": 0.55}),
    # BET SIZE TESTS (Kylar, 2026-11-07 10:22-10:23): the same entry and rule with a flat bet of $5 up to $500 per round (built in steps like any bet). Compare profit PER DOLLAR staked: size cannot create an edge, it only scales the result and the fees. A big bet can also move the price or bust the wallet; the sim limits fills to what the book shows.
    "v_hold_s5": ("Size test: hold to the end, $5 per round", "distance", {"STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "CAP": 5.0, "FLAT_BET": 5.0}),
    "v_hold_s10": ("Size test: hold to the end, $10 per round", "distance", {"STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "CAP": 10.0, "FLAT_BET": 10.0}),
    "v_hold_s25": ("Size test: hold to the end, $25 per round", "distance", {"STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "CAP": 25.0, "FLAT_BET": 25.0}),
    "v_hold_s50": ("Size test: hold to the end, $50 per round", "distance", {"STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "CAP": 50.0, "FLAT_BET": 50.0}),
    "v_hold_s100": ("Size test: hold to the end, $100 per round", "distance", {"STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "CAP": 100.0, "FLAT_BET": 100.0}),
    "v_hold_s250": ("Size test: hold to the end, $250 per round", "distance", {"STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "CAP": 250.0, "FLAT_BET": 250.0}),
    "v_hold_s500": ("Size test: hold to the end, $500 per round", "distance", {"STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "CAP": 500.0, "FLAT_BET": 500.0}),
    "v_take25_s10": ("Size test: sell at +25%, $10 per round", "distance", {"TAKE_PCT": 0.25, "STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "MIN_PROFIT_USD": 0.25, "CAP": 10.0, "FLAT_BET": 10.0}),
    "v_take25_s50": ("Size test: sell at +25%, $50 per round", "distance", {"TAKE_PCT": 0.25, "STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "MIN_PROFIT_USD": 0.25, "CAP": 50.0, "FLAT_BET": 50.0}),
    "v_take25_s250": ("Size test: sell at +25%, $250 per round", "distance", {"TAKE_PCT": 0.25, "STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "MIN_PROFIT_USD": 0.25, "CAP": 250.0, "FLAT_BET": 250.0}),
    "v_take25_s500": ("Size test: sell at +25%, $500 per round", "distance", {"TAKE_PCT": 0.25, "STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "MIN_PROFIT_USD": 0.25, "CAP": 500.0, "FLAT_BET": 500.0}),
    # SNIPING (Kylar, 2026-11-05): one favourite buy in the last ~2 minutes (13+ min into the 15), price allowed up to 97c, hold to the end. Practice only; the cap stays at UNPROVEN_CAP.
    "v_snipe": ("Reaction test: SNIPE one late favourite buy (last 2 min, up to 97\u00a2), hold to the end", "distance", {"STOP_ON": 0, "EXIT_ON": 0, "ODDS_SELL": 0, "ENTRY_AFTER": 780, "MAX_TRADES": 1, "ENTRY_MAX": 0.97, "MAX_PRICE": 0.97}),
    # SNIPING ALL-IN (Kylar, 2026-11-05 19:41): the whole $1,000 wallet on the favourite in the last ~15 s of every round, hold to the end. Practice only. Whatever the book cannot fill stays in cash.
}
STRATS.update({k: v[0] for k, v in VARIANTS.items()})
_STATIC_V = set(VARIANTS)
_DYN = {"mt": None, "keys": set()}
_OV_OK = {"STOP_ON": (0, 1), "STOP_PCT": (0.1, 0.9), "STOP_SMALL": (0, 100), "EXIT_ON": (0, 1), "EXIT_P": (3, 80), "EXIT_D": (2, 40), "MAX_TRADES": (1, 12),
          "STAGE_GAP": (5, 300), "ODDS_SELL": (0, 1), "ODDS_MARGIN": (0.0, 0.2), "ENTRY_AFTER": (0, 600), "FLIP": (0, 1), "TAKE_PCT": (0.0, 2.0), "FLAT_BET": (0.0, 1000.0), "MIN_PROFIT_USD": (0.0, 10.0)}
_BASES = ("distance", "signals", "trend", "flow", "mood")


def load_dynamic(DIR):
    """Experiments the innovator (innovate.py) invented or retired: variants.json = {key: {label, base, ov}}. Applied live, validated and clamped."""
    p = os.path.join(DIR, "variants.json")
    try:
        mt = os.path.getmtime(p)
    except OSError:
        mt = None
    if mt == _DYN["mt"]:
        return
    _DYN["mt"] = mt
    try:
        raw = json.load(open(p)) if mt else {}
    except (OSError, ValueError):
        raw = {}
    new = {}
    for k, v in (raw or {}).items():
        try:
            if not str(k).startswith("v_") or k in _STATIC_V or v.get("base") not in _BASES:
                continue
            ov = {n: min(hi, max(lo, float(x))) for n, x in (v.get("ov") or {}).items() if n in _OV_OK for lo, hi in [_OV_OK[n]]}
            new[k] = ("Experiment: " + str(v.get("label") or k)[:90], v["base"], ov)
        except Exception:
            continue
    for k in _DYN["keys"] - set(new):
        VARIANTS.pop(k, None); STRATS.pop(k, None)
    for k, v in new.items():
        VARIANTS[k] = v; STRATS[k] = v[0]
    _DYN["keys"] = set(new)
STRATS_OLD = {}
AGG = 0.3             # aggression dial 0..1, also drives how eagerly the swing strategy moves
PRACTICE = "auto"       # "auto": every practice strategy trades and learns; or one strategy key: only that one trades


def log_trade(e):
    """Append every buy, sell and refused buy to trades.jsonl, with the quote it saw, for later study."""
    try:
        if not _DIR:
            return
        rec = {k: e.get(k) for k in ("t", "s", "a", "side", "c", "px", "d", "bal", "why", "g")}
        rec["ticker"] = _TK; rec["live"] = bool(_LIVE); rec["ask"] = _QUOTE[0]; rec["bid"] = _QUOTE[1]; rec["v"] = SIM_VERSION; rec["q"] = _QSRC
        if _FEAT and e.get("a") == "BUY":
            rec["f"] = {k: (round(v, 4) if isinstance(v, float) else v) for k, v in _FEAT.items() if v is not None}
        with open(os.path.join(_DIR, "trades.jsonl"), "a") as fh:
            fh.write(json.dumps(rec) + "\n")
    except Exception:
        pass


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
        "trend_h": 0.0, "trend_w": 0.0, "levels": 0.06,
        "trend_1h": 0.04, "trend_4h": 0.03, "trend_24h": 0.04, "trend_7d": 0.03}
REFILL = 100.0         # (old) fixed refill; pretend wallets are now topped back up to their starting amount


def log_refill(who, amt, before):
    """Every top-up of a pretend wallet is written down, and never counted as profit."""
    try:
        if _DIR:
            with open(os.path.join(_DIR, "refills.jsonl"), "a") as fh:
                fh.write(json.dumps({"t": int(time.time()), "who": who, "added": round(amt, 2), "before": round(before, 2)}) + "\n")
    except OSError:
        pass
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
            "Hourly and daily trend": "trend_h", "Weekly and monthly trend": "trend_w", "Support and resistance": "levels",
            "Trend, 1 hour": "trend_1h", "Trend, 4 hours": "trend_4h", "Trend, 24 hours": "trend_24h", "Trend, 7 days": "trend_7d"}
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
    """For the Auto wallet: follow a practice strategy only once it has a proven POSITIVE record (40+ rounds, record shrunk toward zero so a lucky streak
    of a few rounds cannot win it). Until one earns that, hold to the end (the cheapest way to take part: no sell fee, no second spread). Changed 2026-11-05:
    before, it followed whichever strategy looked best after only 20 rounds, which with ~40 variants in the race mostly picks luck."""
    base = "v_hold" if "v_hold" in sim["acc"] else ("hold" if "hold" in sim["acc"] else ("distance" if "distance" in sim["acc"] else (next(iter(sim["acc"])) if sim["acc"] else "swing")))
    # base (hold) is the default. A variant must beat the base clearly (1.5x per round, and positive) over a long record, and once chosen it is kept for at
    # least 6 hours unless something beats it by 25%: with ~40 variants the "best" one changes every round and hopping between them is just chasing luck.
    def val(n):
        a = sim["acc"].get(n)
        return None if not a or a["windows"] < AUTO_MIN_ROUNDS else a["pnl"] / (a["windows"] + float(AUTO_MIN_ROUNDS))
    bval = val(base); best, bv, found = base, max(bval or 0.0, 0.0), False
    for n in sim["acc"]:
        if n not in STRATS or n == base: continue
        v = val(n)
        if bval is not None and v is not None and v > 0 and v > bv * 1.5 and v > (bv if found else 0.0):
            best, bv, found = n, v, True
    cur, last = sim.get("auto_pick"), (sim.get("autolog") or [{}])[-1].get("t", 0)
    if cur and cur != best and cur in STRATS and (time.time() - last < 6 * 3600 or not found or (val(cur) is not None and val(cur) * 1.25 >= bv)):
        if val(cur) is not None and val(cur) > 0 or cur == base:
            best = cur
    pick = sim.get("auto_pick")
    if pick != best:
        sim.setdefault("autolog", []).append({"t": int(time.time()), "from": pick, "to": best,
            "why": ("Best positive record so far per round after fees (%d+ rounds each)." % AUTO_MIN_ROUNDS) if found else "No strategy has a proven positive record over %d+ rounds yet, so it holds to the end (least cost)." % AUTO_MIN_ROUNDS})
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
    if not _LIVE and _QSRC == "list":                  # no live order-book price this second: do not trade on the lagging list quote
        return False
    if px > ENTRY_MAX + 1e-9 and _CUR != "hold":
        if not any(e.get("a") == "SKIP" and e.get("s") == _CUR and _T - e["t"] < 60 for e in _EV[-6:]):
          log_trade({"t": _T, "s": _CUR, "a": "SKIP", "side": side, "c": 0, "px": round(px, 3), "d": 0, "bal": round(a["bal"], 2), "why": "entry cap"})
          _EV.append({"t": _T, "s": _CUR, "a": "SKIP", "side": side, "c": 0, "px": round(px, 3), "d": 0, "bal": round(a["bal"], 2),
                      "why": "Not buying %s at %d\u00a2: that is above your %d\u00a2 entry cap (one miss would cost several wins)." % (side, round(px * 100), round(ENTRY_MAX * 100)), "mix": _MIX, "trace": _TRACE})
        if a.get("w") is not None:
            a["w"]["capped"] = a["w"].get("capped", 0) + 1
        return False
    why_no = None
    if _CUR != "hold":
        if _CUR == "swing":                            # swing has its own price rules; only the news blackout applies to it
            if BLACKOUT:
                why_no = "a big US news release is due or just out (%s)" % BLACKOUT
        elif px < ENTRY_MIN - 1e-9:
            why_no = "the price %d\u00a2 is below your %d\u00a2 minimum (cheap long shots rarely pay)" % (round(px * 100), round(ENTRY_MIN * 100))
        elif BLACKOUT:
            why_no = "a big US news release is due or just out (%s)" % BLACKOUT
        else:
            for lo, hi in ENTRY_BLOCK:
                if lo <= px * 100 < hi:
                    why_no = "your own recordings show buying at %d-%d\u00a2 has lost money after fees" % (lo, hi)
            if not why_no and PATTERN_BAD and _FEAT.get("pm") is not None and _FEAT.get("score") is not None:
                pm_ = _FEAT["pm"] if side == "UP" else 1 - _FEAT["pm"]
                el_ = _FEAT["el"]; edge_ = pm_ - px - fee(px); sc_ = _FEAT["score"] * (1 if side == "UP" else -1)
                bk_ = {"time": "t%d" % min(4, int(max(0, el_) // 180)), "edge": "e0" if edge_ < 0 else "e1" if edge_ < 0.05 else "e2" if edge_ < 0.10 else "e3",
                       "score": "s0" if sc_ < -10 else "s1" if sc_ <= 10 else "s2"}
                for f_, b_ in PATTERN_BAD:
                    if bk_.get(f_) == b_:
                        why_no = "its hindsight memory shows entries like this (%s: %s) lost money on rounds it was tested on" % (f_, b_)
                        break
    if why_no:
        if not any(e.get("a") == "SKIP" and e.get("s") == _CUR and _T - e["t"] < 60 for e in _EV[-6:]):
            _EV.append({"t": _T, "s": _CUR, "a": "SKIP", "side": side, "c": 0, "px": round(px, 3), "d": 0, "bal": round(a["bal"], 2), "why": "Not buying %s: %s." % (side, why_no), "mix": _MIX, "trace": _TRACE})
            log_trade({"t": _T, "s": _CUR, "a": "SKIP", "side": side, "c": 0, "px": round(px, 3), "d": 0, "bal": round(a["bal"], 2), "why": why_no})
        return False
    if not (MIN_PRICE <= px <= MAX_PRICE):
        dollars = min(dollars, max(MIN_BET, FLOOR))   # no big bets on long shots or near-sure things
    dollars = min(dollars, a["bal"] / (1 + fee(px) / px), (CAP - used) / (1 + fee(px) / px))   # cap counts fees
    avail = _SZ[0] if side == "UP" else _SZ[1]       # cannot buy more than Kalshi has on offer at that price
    if avail is not None:
        dollars = min(dollars, avail * px)
    if dollars < FLOOR - 1e-9:                         # hard rule: no bet smaller than the minimum
        return False
    c = math.floor(dollars / px + 1e-9)                # Kalshi sells whole contracts only
    if c * px < FLOOR - 1e-9:                          # whole contracts can land just under the minimum (10 x 48c = $4.80): buy enough to reach it
        c = int(math.ceil(FLOOR / px - 1e-9))
    while c >= 1 and (c * px + fee_total(c, px) > a["bal"] + 1e-9 or c * px + fee_total(c, px) > (CAP - used) + 1e-9):
        c -= 1
    if c < 1 or c * px < FLOOR - 1e-9:
        return False
    if _LIVE:                                          # real money: check the real order book first, never buy off a stale quote
        rp = BROKER.real_price(_TK, side)
        why_skip = None
        if rp is None:
            why_skip = "could not read Kalshi's order book"
        elif rp < ENTRY_MIN - 1e-9 and _CUR != "hold":
            why_skip = "the real price is %d\u00a2, below your %d\u00a2 minimum" % (round(rp * 100), round(ENTRY_MIN * 100))
        elif rp > ENTRY_MAX + 1e-9:
            why_skip = "the real price is %d\u00a2, above your %d\u00a2 cap" % (round(rp * 100), round(ENTRY_MAX * 100))
        elif rp > px + 0.03:
            why_skip = "the quote said %d\u00a2 but the order book says %d\u00a2" % (round(px * 100), round(rp * 100))
        if why_skip:
            if not any(e.get("a") == "SKIP" and e.get("s") == _CUR and _T - e["t"] < 30 for e in _EV[-6:]):
                _EV.append({"t": _T, "s": _CUR, "a": "SKIP", "side": side, "c": 0, "px": round(px, 3), "d": 0, "bal": round(a["bal"], 2), "why": "Not buying %s: %s." % (side, why_skip), "mix": _MIX, "trace": _TRACE})
                log_trade({"t": _T, "s": _CUR, "a": "SKIP", "side": side, "c": 0, "px": round(px, 3), "d": 0, "bal": round(a["bal"], 2), "why": why_skip})
            return False
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
    w["trades"] += 1; w["staked"] = max(w["staked"], a["pos"]["cost"]); w["last_buy"] = _T
    if w["first"] is None:
        w["first"] = {"side": side, "c": c, "cost": dollars + f}
    a["trades"] += 1
    log_trade({"t": _T, "s": _CUR, "a": "BUY", "side": side, "c": round(c, 1), "px": round(px, 3), "d": round(dollars, 2), "bal": round(a["bal"], 2), "why": why})
    _EV.append({"t": _T, "s": _CUR, "a": "BUY", "side": side, "c": round(c, 1), "px": round(px, 3), "d": round(dollars, 2), "bal": round(a["bal"], 2), "why": why, "mix": _MIX, "trace": _TRACE})
    return True


def sell(a, ask_up, bid_up, why=""):
    p = a["pos"]
    lb = (a.get("w") or {}).get("last_buy")
    if MIN_HOLD > 0 and lb is not None and _T - lb < MIN_HOLD and _FEAT.get("left", 999) > 45:     # optional hard timer (off by default)
        return False
    px = bid_up if p["side"] == "UP" else 1 - ask_up
    px = min(0.99, max(0.01, px))
    n = p["c"]
    gain = n * px - fee_total(n, px) - p["cost"]                       # profit after fees if we sell now (negative = a loss)
    need = max(MIN_PROFIT_USD, MIN_PROFIT_PCT * p["cost"])
    if 0 < gain < need and _FEAT.get("left", 999) > 45:                # a few cents of profit does not beat the cost of trading: keep holding
        return False
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
    log_trade({"t": _T, "s": _CUR, "a": "SELL", "side": side, "c": round(n, 1), "px": round(px, 3), "d": round(got, 2), "bal": round(a["bal"], 2), "why": why, "g": round(gain, 2)})
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
    if ALL_IN:
        return max(0.0, bal)                                  # sniping all-in test: the whole wallet; the book depth and the cash left decide the fill
    if FLAT_BET > 0:
        return max(0.0, min(FLAT_BET - pos_cost, bal))       # size test: the same dollar amount every round, whatever the edge
    mult *= max(0.35, min(1.0, (bal + pos_cost) / ref))     # a shrinking wallet bets smaller, so it lasts more rounds
    if mult <= 0:
        return 0.0
    frac = min(SLICE, KELLY * max(0.0, edge)) * mult   # share of the wallet: bigger edge, bolder dial, higher conviction = bigger bet
    room = ROUND_FRAC * (bal + pos_cost) - pos_cost    # adds in one round cannot stack past this share of the wallet
    if room < FLOOR:
        return 0.0
    return max(FLOOR, min(frac * bal, CAP - pos_cost, room))


def stage(dollars, pname, first):
    """Build a position in steps: the first buy of a round is only a share of the intended size."""
    if ALL_IN:
        return dollars
    if first and pname != "hold" and dollars > FLOOR:
        return max(FLOOR, dollars * STAGE_FIRST)
    return dollars


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
        amt = max(0.0, START - a["bal"])                 # top back up to the starting $1,000
        log_refill(name, amt, a["bal"])
        a["bal"] += amt; a["busts"] += 1
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
          "trend_h": "Hourly and daily trend", "trend_w": "Weekly and monthly trend", "levels": "Support and resistance",
          "trend_1h": "Trend, 1 hour", "trend_4h": "Trend, 4 hours", "trend_24h": "Trend, 24 hours", "trend_7d": "Trend, 7 days"}


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
            amt = max(0.0, run["start"] - a["bal"])          # top back up to the amount it started with
            log_refill("wallet", amt, a["bal"])
            a["bal"] += amt; run["added"] = run.get("added", 0.0) + amt
            run.setdefault("refills", []).append({"t": int(time.time()), "amt": round(amt, 2), "after": rd["t"]})


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


# ---------- Kylar's swing strategy ----------
SW_STAKE = 20.0         # dollars per entry
SW_OPEN_SECS = 150      # the first entry must come in the first 2.5 minutes of a round (he looks as soon as it opens)
SW_LAST_ENTRY = 480     # no new swing entries after 8 minutes
SW_LAST_SELL = 60       # no swing sales in the last minute
SW_MAX_ENTRIES = 4      # swing entries per round (fees add up)
SW_TREND = 0.0003       # BTC must have moved this much (0.03%) in the last 10 minutes, and the last 5 minutes the same way
SW_MOVE = 5.0           # the Up price must have moved this many cents in our favour before a slowdown counts
SW_MIN_V = 0.05         # cents per second: the move must have reached at least this speed
SW_SLOW = 0.35          # slowed = current speed is under this share of the fastest speed of the move
SW_SLOW_SECS = 8        # it has to stay slow for this long
SW_HOLD_EDGE = 0.05     # near the end it only places a hold-to-the-end bet if its model sees at least this edge after fees


def _tape_at(tape, t):
    r = None
    for x in tape:
        if x[0] <= t:
            r = x
        else:
            break
    return r


SW_OVR = {}             # test overrides (the replay sweep sets these); empty in normal use
SW_STOP = 20.0         # cents per contract: a swing bet that has lost this much is cut instead of being held to the end (0 = never cut)
SW_CONFIRM = 2.0        # cents the price must turn back before it buys the other side after a sale


def swing_params(ag):
    """How eager the swing strategy is. Low aggression = patient (needs a clear trend, a big move, a clear slowdown);
    high aggression = makes moves on small trends, takes profit on small moves, re-enters fast, more swings per round."""
    P = {"trend": SW_TREND * (1 - 0.9 * ag), "open": SW_OPEN_SECS + 330 * ag, "move": max(4.0, SW_MOVE - 2.5 * ag), "min_v": SW_MIN_V * (1 - 0.5 * ag),
         "slow": SW_SLOW + 0.25 * ag, "slow_secs": max(5, round(SW_SLOW_SECS - 5 * ag)), "entries": SW_MAX_ENTRIES + int(round(4 * ag)),
         "min_profit": 0.015 - 0.005 * ag, "hold_edge": SW_HOLD_EDGE - 0.04 * ag, "need_min": 150 - 60 * ag, "confirm": max(1.0, SW_CONFIRM - ag), "stop": SW_STOP, "entry_cap": 0.80}
    P.update(SW_OVR)
    return P


def swing_trend(tape, now, thr=None):
    """(+1 up / -1 down / 0 none, plain reason) from BTC's last 5 and 10 minutes."""
    thr = SW_TREND if thr is None else thr
    if not tape:
        return 0, "no price history yet"
    a5, a10 = _tape_at(tape, now - 300), _tape_at(tape, now - 600)
    if a5 and now - 300 - a5[0] > 120:             # the history has a hole (for example after a restart): do not trust it
        a5 = None
    if a10 and now - 600 - a10[0] > 120:
        a10 = None
    cur = tape[-1][1]
    if not a5 or not cur:
        return 0, "not enough price history yet (needs 5 minutes)"
    c5 = cur / a5[1] - 1
    c10 = (cur / a10[1] - 1) if a10 else c5
    txt = "BTC %+.2f%% in 5 min, %+.2f%% in 10 min" % (100 * c5, 100 * c10)
    if c5 > 0 and c10 >= thr:
        return 1, txt
    if c5 < 0 and c10 <= -thr:
        return -1, txt
    return 0, txt + " (no clear trend)"


def _swing_log(rec):
    try:
        if _DIR:
            with open(os.path.join(_DIR, "swings.jsonl"), "a") as fh:
                fh.write(json.dumps(rec) + "\n")
    except OSError:
        pass


def swing_step(a, w, now, el, left, price, mid, ask, bid, pm, sigs, score, sim, why):
    """Kylar's way of trading a round:
    1. Right after the open, look at the trend. If BTC has been rising, buy $20 of DOWN (it is due to turn); if falling, buy $20 of UP.
    2. Watch the price move in our favour. When its speed slows right down, sell and take the profit, then buy the other side.
    3. Only start another swing if there is enough time left for the price to come back (based on how long its swings have been taking).
    4. Near the end, if the model sees a real edge, place one hold-to-the-end bet; otherwise sit out.
    The higher the aggression dial, the smaller the trend / move it acts on and the more swings it allows."""
    P = swing_params(AGG)
    sw = w.setdefault("sw", {"entries": 0, "pk_v": 0.0, "best": 0.0, "slow_t": None, "mid_in": None, "want": None, "hold": False, "t_in": None})
    tape = sim.get("tape") or []
    m15 = _tape_at(tape, now - 15)
    v = ((mid - m15[2]) / max(1.0, now - m15[0])) * 100.0 if m15 else 0.0      # Up price speed, cents per second
    pos = a["pos"]
    dur = sim.get("sw_dur", 150.0)                                              # how long one swing usually takes (seconds)
    need = min(360.0, max(P["need_min"], 1.3 * dur))                            # time that must be left to start a swing
    if pos:
        s = pos["side"]
        if sw.get("hold"):
            return "holding to the end", "Holding its end-of-round bet (%s) to the finish." % s
        if sw["mid_in"] is None:
            sw["mid_in"] = mid; sw["t_in"] = sw["t_in"] or now
        d = 1 if s == "UP" else -1
        mv = d * (mid - sw["mid_in"]) * 100.0
        fv = d * v
        sw["best"] = max(sw["best"], mv); sw["pk_v"] = max(sw["pk_v"], fv)
        pxb = bid if s == "UP" else 1 - ask
        prof = pxb - fee(pxb) - pos["cost"] / pos["c"]
        if P["stop"] and prof <= -P["stop"] / 100.0 and left > SW_LAST_SELL:
            c0, avg0 = pos["c"], pos["cost"] / pos["c"]
            if sell(a, ask, bid, "Cutting the loss: this %s swing is down %d\u00a2 per contract after fees (your limit is %d\u00a2), so it sells instead of holding to the end." % (s, round(-prof * 100), round(P["stop"]))):
                _swing_log({"t": int(now), "ticker": _TK, "side": s, "c": round(c0, 1), "avg_cost": round(avg0, 4), "mid_in": round(sw["mid_in"], 4), "mid_out": round(mid, 4),
                            "best_cents": round(sw["best"], 1), "profit_pc": round(prof, 4), "el": int(el), "cut": True, "live": bool(_LIVE)})
                sw.update({"want": None, "cut": True, "best": 0.0, "pk_v": 0.0, "slow_t": None, "mid_in": None, "t_in": None})
                return "sold", "Cut the loss on %s. No more swings this round." % s
        slow = sw["best"] >= P["move"] and sw["pk_v"] >= P["min_v"] and fv <= P["slow"] * sw["pk_v"]
        sw["slow_t"] = (sw["slow_t"] or now) if slow else None
        base = "Riding %s: price is %d\u00a2 %s (best so far %d\u00a2 in its favour), moving %.2f\u00a2/s our way (fastest %.2f). " % (s, abs(round(mv)), "in its favour" if mv >= 0 else "against it", round(sw["best"]), fv, sw["pk_v"])
        if slow and now - sw["slow_t"] >= P["slow_secs"] and left > SW_LAST_SELL:
            if prof >= P["min_profit"]:
                c0, avg0 = pos["c"], pos["cost"] / pos["c"]
                if sell(a, ask, bid, "The move slowed (speed %.2f\u00a2/s, fastest was %.2f), so it sells %s and takes the profit: %+d\u00a2 per contract after fees." % (fv, sw["pk_v"], s, round(prof * 100))):
                    took = now - (sw["t_in"] or now)
                    if took > 20:
                        sim["sw_dur"] = round(0.7 * dur + 0.3 * took, 1)
                    _swing_log({"t": int(now), "ticker": _TK, "side": s, "c": round(c0, 1), "avg_cost": round(avg0, 4), "mid_in": round(sw["mid_in"], 4), "mid_out": round(mid, 4),
                                "best_cents": round(sw["best"], 1), "pk_v": round(sw["pk_v"], 3), "v": round(fv, 3), "profit_pc": round(prof, 4), "el": int(el), "took": int(took), "live": bool(_LIVE)})
                    sw.update({"want": ("DOWN" if s == "UP" else "UP"), "best": 0.0, "pk_v": 0.0, "slow_t": None, "mid_in": None, "t_in": None, "ext": mid})
                    return "sold", "Sold %s on the slowdown. Next it buys %s, but only once the price really turns." % (s, sw["want"])
                return "waiting", base + "Wanted to sell but the sale did not go through; trying again."
            return "holding", base + "It has slowed but selling now would not clear fees yet, so it waits."
        return "holding", base + ("Slowing, waiting to be sure." if slow else "Still moving, so it keeps riding.")
    # flat
    if left <= 5 or sw.get("hold"):
        return "waiting", why
    room = left >= need and not sw.get("cut")
    side, reason = None, None
    if sw.get("want") and sw["entries"] < P["entries"] and room:
        ext = sw.get("ext", mid)
        ext = min(ext, mid) if sw["want"] == "UP" else max(ext, mid)       # the low (or high) the price has reached since the sale
        sw["ext"] = ext
        turned = ((mid - ext) if sw["want"] == "UP" else (ext - mid)) * 100.0
        if turned < P["confirm"]:
            return "waiting", "Sold, now waiting for the price to really turn before buying %s: it has come back %.1f\u00a2 off its %s and needs %.1f\u00a2." % (sw["want"], turned, "low" if sw["want"] == "UP" else "high", P["confirm"])
        side, reason = sw["want"], "Swing: the price has turned %.1f\u00a2 since the sale and there are %ds left (it needs %ds for a swing), so it buys %s." % (turned, left, need, sw["want"])
    elif sw["entries"] == 0 and el <= P["open"] and room:
        t, txt = swing_trend(tape, now, P["trend"])
        if t == 0:
            return "waiting", "Looking at the trend: %s. Not clear enough yet; it keeps looking for the first %ds." % (txt, int(P["open"]))
        side = "DOWN" if t > 0 else "UP"
        reason = "Opening swing: %s, so it bets the trend turns and buys %s." % (txt, side)
    elif sw["entries"] > 0 and not sw.get("want") and sw["entries"] < P["entries"] and room:
        t, txt = swing_trend(tape, now, P["trend"])
        if t:
            side = "DOWN" if t > 0 else "UP"
            reason = "New swing: %s, so it bets the trend turns and buys %s." % (txt, side)
    if side is None and not room and left > 45:
        p = prob_up("distance", pm, sigs, score, sim.get("mood", 0.0))
        best = None
        for s_, p_, px_ in (("UP", p, ask), ("DOWN", 1 - p, 1 - bid)):
            e_ = p_ - px_ - fee(px_)
            if e_ >= P["hold_edge"] and ENTRY_MIN <= px_ <= ENTRY_MAX and (best is None or e_ > best[1]):
                best = (s_, e_)
        if not best:
            return "waiting", ("Cut its loss earlier, so no more swings this round" if sw.get("cut") else "Not enough time left for another swing (%ds, it needs %ds)" % (left, need)) + " and no bet worth holding to the finish, so it sits this one out."
        if buy(a, best[0], SW_STAKE, ask, bid, "End of round: its model sees a %d\u00a2 edge on %s after fees, so it places one bet and holds to the end." % (round(best[1] * 100), best[0])):
            sw["hold"] = True
            return "opened", "Placed an end-of-round bet and will hold it."
        return "waiting", why
    if not side:
        return "waiting", "Watching for the next swing (%d of %d used, %ds left)." % (sw["entries"], P["entries"], left)
    px_ = ask if side == "UP" else 1 - bid
    if px_ > P["entry_cap"] + 1e-9:
        return "waiting", reason + " But %s costs %d\u00a2, over the swing price limit of %d\u00a2, so it waits." % (side, round(px_ * 100), round(P["entry_cap"] * 100))
    if buy(a, side, SW_STAKE, ask, bid, reason):
        sw.update({"entries": sw["entries"] + 1, "want": None, "mid_in": mid, "t_in": now, "best": 0.0, "pk_v": 0.0, "slow_t": None})
        if w.get("mix") is None:
            w["mix"] = _MIX
        return "opened", reason
    return "waiting", reason + " (the buy was refused by a price rule)"


def run_equity(a, bid, ask):
    p = a["pos"]
    return a["bal"] + (p["c"] * (bid if p["side"] == "UP" else 1 - ask) if p else 0.0)


def step(S, now, win, window_len, price, strike, pm, kal, sigs, score, enabled, DIR, C=None, run_cfg=None, result_fn=None):
    global AGG, PRACTICE, _DIR, _QUOTE, BROKER, _LIVE, _SIM, _TK, ROUND_FRAC, KELLY, MIN_BET, CAP, SLICE, MAX_TRADES, EDGE_MIN, MIN_PRICE, MAX_PRICE, ENTRY_MIN, ENTRY_MAX, STAGE_FIRST, STAGE_GAP, ENTRY_BLOCK, BLACKOUT, EXIT_ON, EXIT_P, EXIT_D, STOP_ON, STOP_PCT, STOP_SMALL, UNPROVEN_CAP, PATTERN_BAD, _FEAT, _QSRC, MIN_HOLD, MIN_PROFIT_USD, MIN_PROFIT_PCT, _SZ, _EV, _CUR, _T, _W, _MIX, _TRACE, _TRUST
    if C:
        MIN_BET, MAX_TRADES = C["min_bet"], int(C["max_trades"])
        CAP = C["cap"] if C["cap"] > 0 else 1e9               # 0 = no limit: it may use the whole wallet
        UNPROVEN_CAP = float(C.get("unproven_cap", UNPROVEN_CAP))
        if UNPROVEN_CAP > 0:
            CAP = min(CAP, UNPROVEN_CAP)                       # nothing has proven an edge yet, so no big bets (bigger bets only multiply the cost of trading)
        ag = min(1.0, max(0.0, float(C.get("aggression", 30)) / 100.0))
        AGG = ag
        SLICE = 0.04 + 0.96 * ag * ag                          # most of the wallet one bet may use
        EDGE_MIN = 0.06 - 0.05 * ag                            # how thin an edge it will act on
        ROUND_FRAC = 0.05 + 0.95 * ag * ag                    # total stake in one round, as a share of the wallet
        KELLY = 0.5 + 4.5 * ag                                 # how hard it leans into an edge
        MIN_PRICE, MAX_PRICE = C.get("min_price", MIN_PRICE), C.get("max_price", MAX_PRICE)
        ENTRY_MAX = C.get("entry_max", ENTRY_MAX)
        ENTRY_MIN = C.get("entry_min", ENTRY_MIN)
        STAGE_FIRST = C.get("stage_first", STAGE_FIRST)
        STAGE_GAP = C.get("stage_gap", STAGE_GAP)
        ENTRY_BLOCK = C.get("entry_block") or []
        BLACKOUT = C.get("blackout")
        PATTERN_BAD = [(r["feature"], r["bucket"]) for r in (C.get("pattern_bad") or [])]
        MIN_HOLD = int(C.get("min_hold_secs", MIN_HOLD))
        STOP_ON, STOP_PCT = int(C.get("stop_on", STOP_ON)), float(C.get("stop_pct", STOP_PCT)); STOP_SMALL = float(C.get("stop_small", STOP_SMALL))
        MIN_PROFIT_USD = float(C.get("min_profit_usd", MIN_PROFIT_USD)); MIN_PROFIT_PCT = float(C.get("min_profit_pct", MIN_PROFIT_PCT))
        EXIT_ON, EXIT_P, EXIT_D = int(C.get("exit_on", EXIT_ON)), float(C.get("exit_peak", EXIT_P)), float(C.get("exit_drop", EXIT_D))
        if isinstance(C.get("weights"), dict):
            _W = dict(DEFW, **C["weights"])
        _TRUST = C.get("trust") or {}
        PRACTICE = C.get("practice") if C.get("practice") in STRATS else "auto"
    _SZ = ((kal or {}).get("yes_ask_size"), (kal or {}).get("yes_bid_size"))
    _QSRC = (kal or {}).get("qsrc")
    _DIR = DIR

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
        sim.update({"ver": SIM_VERSION, "acc": {}, "win": None, "hours": {}, "joined": False, "run": None, "pending": [], "events": [], "tape": sim.get("tape", [])})
    _SIM = sim
    load_dynamic(DIR)
    for n in list(STRATS):
        sim["acc"].setdefault(n, new_acc())
    sim.setdefault("events", [])
    _EV, _T = sim["events"], now
    g = lambda k: (sigs.get(k) or {}).get("score") or 0.0
    sim["mood"] = 0.9 * sim["mood"] + 0.1 * (0.7 * g("news") + 0.3 * g("fng"))   # slow mood
    bid, ask, synth = prices(kal, pm)
    _QUOTE = (round(ask, 3), round(bid, 3))
    if not synth and price:
        tp = sim.setdefault("tape", [])
        if not tp or now - tp[-1][0] >= 2.0:
            tp.append([round(now, 1), round(price, 2), round((bid + ask) / 2.0, 4)])
        if len(tp) > 600 or (tp and tp[0][0] < now - 2400):
            sim["tape"] = [x for x in tp if x[0] >= now - 2400][-600:]
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
    _FEAT = {"el": window_len - left, "left": left, "pm": pm, "score": score}
    if kal and strike and kal.get("ticker"):             # only ever use Kalshi's own target for this round
        sim["strike"] = float(strike); sim["ticker"] = kal["ticker"]
        if kal.get("yes_bid") is not None and kal.get("yes_ask") is not None:
            sim["last_yes"] = (kal["yes_bid"] + kal["yes_ask"]) / 2.0
        if not sim.get("ready"):
            sim["ready"] = True
            sim["joined"] = now - win <= 150             # practice strategies only join near the start
            for a in sim["acc"].values():
                a["w"] = newwin(win, sigs) if sim["joined"] else None
            r_ = sim.get("run")
            if r_ and r_["status"] == "running" and left > 45 and not r_["acc"]["w"]:
                r_["acc"]["w"] = newwin(win, sigs)
    # the user's own wallet run (Start / Stop on the Live View)
    rc = run_cfg or {}
    run = sim.get("run")
    if rc.get("active") and (not run or run["id"] != rc.get("id")):
        st = rc.get("strategy") if (rc.get("strategy") in STRATS or rc.get("strategy") in (list(STRATS_OLD) + ["auto"])) else "swing"
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
    if run and run["status"] == "running" and not run.get("live") and rc.get("active") and rc.get("strategy") and rc.get("strategy") != run["strategy"] \
            and (rc["strategy"] in STRATS or rc["strategy"] in (list(STRATS_OLD) + ["auto"])):
        run["strategy"] = rc["strategy"]                   # the pretend wallet can be switched without restarting it
    items = [(n, n, a, enabled and (PRACTICE == "auto" or n == PRACTICE)) for n, a in sim["acc"].items() if n in STRATS]
    if run and run["status"] == "running":
        items.append(("run", auto_pick(sim) if run["strategy"] == "auto" else run["strategy"], run["acc"], True))
    _OVK = ("STOP_ON", "STOP_PCT", "STOP_SMALL", "EXIT_ON", "EXIT_P", "EXIT_D", "MAX_TRADES", "STAGE_GAP", "ODDS_SELL", "ODDS_MARGIN", "ENTRY_AFTER", "FLIP", "ENTRY_MAX", "MAX_PRICE", "ALL_IN", "CAP", "TAKE_PCT", "MIN_PROFIT_USD", "FLAT_BET")
    _g = globals()
    _BASE = {k: _g[k] for k in _OVK}
    for name, pname, a, enabled in items:
        _g.update(_BASE)                                   # every strategy starts from the normal settings...
        if pname in VARIANTS:                              # ...and a reaction test changes only its own response settings
            _g.update(VARIANTS[pname][2]); pname = VARIANTS[pname][1]
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
        if FLIP:
            p = 1.0 - p
        _MIX = mix(pname, pm, sigs, score, sim["mood"])
        if not enabled:                                   # switched off: close out safely, then idle
            if a["pos"]:
                sell(a, ask, bid, "Switched off: closing the open bet")
            continue
        if left <= 5:
            continue
        gate = pname in ("signals", "hold")                   # only the strategies that use the signals are gated by conviction
        ref = run["start"] if name == "run" else START
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
        if pname == "swing":
            act, why = swing_step(a, w, now, window_len - left, left, price, (bid + ask) / 2.0, ask, bid, pm, sigs, score, sim, why)
        elif w["first"] is None and w["trades"] == 0 and window_len - left < ENTRY_AFTER:
            act = "waiting"; why += " Waiting %d s before the first bet (reaction test)." % int(ENTRY_AFTER - (window_len - left))
        elif w["first"] is None and w["trades"] == 0 and (MIN_BET > 0 or ALL_IN or max(eU, eD) > EDGE_MIN):   # min bet above 0 = must bet every round
            s = "UP" if p >= 0.5 else "DOWN"
            e = side_p(s) - ask_s(s) - fee(ask_s(s))
            if MIN_BET <= 0:
                s = "UP" if eU >= eD else "DOWN"; e = max(eU, eD)
            if ALL_IN:
                s = "UP" if (ask + bid) / 2.0 >= 0.5 else "DOWN"; e = 1.0      # the market's favourite; no edge test
            cm, cwhy = conv_mult(sigs, s, e) if (gate and not ALL_IN) else (1.0, "")
            if gate and cm == 0.0 and MIN_BET <= 0:
                act = "waiting"; why += " Sitting out: not enough agreement between its sources (" + cwhy + ")."
            else:
                buy(a, s, stage(size(e, a["bal"], 0.0, max(cm, 0.4) if MIN_BET > 0 else cm, ref) if e > EDGE_MIN else max(MIN_BET, FLOOR), pname, True), ask, bid,
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
                if EXIT_ON and pname != "hold" and pos["c"] > 0:      # take-profit: learned from the look-back of its own recordings
                    prof_ = sell_now - pos["cost"] / pos["c"]
                    pos["pk"] = max(pos.get("pk", -9.0), prof_)
                    if pos["pk"] >= EXIT_P / 100.0 and prof_ <= pos["pk"] - EXIT_D / 100.0:
                        c0, avg0, pk0 = pos["c"], pos["cost"] / pos["c"], pos["pk"]
                        if sell(a, ask, bid, "Take-profit exit: it was up %d\u00a2 per contract, now only %d\u00a2 (fell %d\u00a2 from the best point), so it sells and keeps the gain." % (
                                round(pk0 * 100), round(prof_ * 100), round((pk0 - prof_) * 100))):
                            sold = True; act = "sold"; w["no_more"] = True
                            try:
                                with open(os.path.join(DIR, "exits.jsonl"), "a") as fh:
                                    fh.write(json.dumps({"t": int(now), "s": name, "ticker": _TK, "side": s, "c": round(c0, 2), "avg_cost": round(avg0, 4),
                                                         "sale_net": round(sell_now - 0.0, 4), "peak": round(pk0, 4), "live": bool(_LIVE)}) + "\n")
                            except OSError:
                                pass
                if not sold and TAKE_PCT > 0 and pname != "hold" and pos["c"] > 0:      # take profit early at a fixed gain (reaction test v_take*)
                    avg_t = pos["cost"] / pos["c"]
                    if sell_now - avg_t >= TAKE_PCT * avg_t:
                        if sell(a, ask, bid, "Taking profit: the bet is up %d%% after fees (paid %s\u00a2, can sell for %s\u00a2), so it sells now and keeps the gain." % (round(100 * (sell_now - avg_t) / avg_t), c_(avg_t), c_(sell_now))):
                            sold = True; act = "sold"; w["no_more"] = True
                if not sold and STOP_ON and pname != "hold" and pos["c"] > 0:      # cut the loss: do not ride a losing bet to the end just because the round is ending
                    loss_ = pos["cost"] / pos["c"] - sell_now
                    avg_ = pos["cost"] / pos["c"]
                    # How willing to cut depends on (1) how much money is at risk, (2) how much time is left, (3) distance to target, via the model's odds for this side.
                    big = max(0.0, min(1.0, (pos["cost"] - STOP_SMALL) / 90.0))           # 0 at $10 or less, 1 at $100+
                    allow = STOP_PCT * (1.45 - 0.9 * big)                                  # $10-ish: very patient (~50%), $100+: tight (~19%)
                    allow *= 1.5 if left > 540 else (1.0 if left > 300 else 0.75)          # lots of time left: it can still swing back
                    need_p = 0.25 if left > 540 else (0.33 if left > 300 else 0.40)         # cut only if its own odds of winning have fallen this low (distance + time left)
                    pw = side_p(s)
                    if pos["cost"] > STOP_SMALL and loss_ >= allow * avg_ and pw <= need_p:
                        if sell(a, ask, bid, "Cutting the loss: $%d bet is down %d%% with %d:%02d left and only a %d%% chance left of winning (BTC too far from the target), so it sells now instead of riding it to the end." % (
                                round(pos["cost"]), round(100 * loss_ / avg_), int(left) // 60, int(left) % 60, round(100 * pw))):
                            sold = True; act = "sold"; w["cut"] = True
                if not sold and ODDS_SELL and sell_now > side_p(s) + ODDS_MARGIN:           # selling beats holding by our own odds
                    sell(a, ask, bid, "Selling %s: it can sell at %s\u00a2 but by its own odds holding is worth only %s\u00a2 per contract." % (s, c_(sell_now), c_(side_p(s))))
                    sold = True; act = "sold"
            if not sold:
                for s, e in (("UP", eU), ("DOWN", eD)):
                    if w.get("no_more") or w.get("cut"):           # it took profit or cut a loss this round: done until the next one
                        why += (" Cut a loss already this round, so no more buying." if w.get("cut") else " Took profit already this round, so no more buying.")
                        break
                    if a["pos"] and a["pos"]["side"] != s:
                        continue
                    if not a["pos"] and ENTRY_AFTER and window_len - left < ENTRY_AFTER:
                        break
                    if e > EDGE_MIN:
                        cm, cwhy = conv_mult(sigs, s, e) if gate else (1.0, "")
                        if cm == 0.0:
                            why += " Not adding: " + cwhy + "."
                            continue
                        if pname != "hold" and now - w.get("last_buy", 0) < STAGE_GAP:
                            why += " Adding slowly: last buy was %ds ago." % int(now - w.get("last_buy", 0))
                            continue
                        buy(a, s, stage(size(e, a["bal"], a["pos"]["cost"] if a["pos"] else 0.0, cm, ref), pname, False), ask, bid,
                            "Edge: it thinks %s is %s%% likely but Kalshi asks %s\u00a2 (+%d\u00a2 after fees)." % (s, c_(side_p(s)), c_(ask_s(s)), round(e * 100)) + ((" Bet size set by " + cwhy + ".") if gate else ""))
                        act = "bought"
                        break
                else:
                    act = "holding" if a["pos"] else "waiting"
        a["now"] = {"p": round(p, 3), "ask": round(ask, 3), "bid": round(bid, 3), "eU": round(eU, 3), "eD": round(eD, 3), "act": act, "why": why, "mix": _MIX, "trace": _TRACE, "conv": (round(conviction(sigs)[0], 2) if gate else None)}
    _g.update(_BASE)                                       # put the normal settings back after the reaction tests
    ranked = []
    for name, a in sim["acc"].items():
        if name not in STRATS:
            continue
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
        runout = {"id": run["id"], "strategy": run["strategy"], "label": STRATS.get(run["strategy"]) or STRATS_OLD.get(run["strategy"]) or "Auto: follows the best-performing strategy", "using": (sim.get("auto_pick") if run["strategy"] == "auto" else run["strategy"]), "autolog": sim.get("autolog", [])[-6:], "status": run["status"],
                  "live": bool(run.get("live")), "slip_avg": (round(sum(BROKER.slips) / len(BROKER.slips), 2) if (BROKER and BROKER.slips) else None), "warn": run.get("warn"), "halt": run.get("halt") or (rc.get("detail") if rc.get("halted") else None), "start": run["start"], "bal": round(a_["bal"], 2), "equity": round(eq, 2), "inflight": round(infl, 2), "k_age": round(max(0.0, now - sim.get("k_ok", now)), 1), "pnl": round(eq - run.get("added", 0.0) - run["start"], 2), "added": round(run.get("added", 0.0), 2), "refills": len(run.get("refills", [])),
                  "windows": a_["windows"], "wins": a_["wins"], "trades": a_["trades"], "started": run["started"],
                  "stopped": run["stopped"], "in_round": bool(a_["w"]), "round_cash": round(a_["w"]["cash"], 2) if a_["w"] else None,
                  "now": a_.get("now"), "rounds": run["rounds"][-15:], "events": [e for e in sim["events"] if e["s"] == "run"][-40:], "curve": run["curve"][-300:],
                  "pos": ({"side": a_["pos"]["side"], "c": round(a_["pos"]["c"], 1), "cost": round(a_["pos"]["cost"], 2),
                           "value": round(a_["pos"]["c"] * (bid if a_["pos"]["side"] == "UP" else 1 - ask), 2)} if a_["pos"] else None)}
    sim["events"] = sim["events"][-120:]
    return {"events": sim["events"][-60:], "strike": sim["strike"], "win": sim["win"], "yes": [round(bid, 3), round(ask, 3)],
            "on": enabled, "synthetic": False, "live": bool(kal and sim.get("ready")), "start": START, "min_bet": MIN_BET, "cap": (CAP if CAP < 1e8 else 0),
            "strategies": ranked, "hours": sim["hours"], "run": runout, "practice": PRACTICE}
