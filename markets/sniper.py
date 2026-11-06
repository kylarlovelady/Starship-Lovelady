#!/usr/bin/env python3
"""$1K-Snipe (Kylar's name): PRACTICE-ONLY end-of-round sniper with its OWN pretend $1,000 wallet. It never touches Kalshi orders or the real account.
Why separate from the strategy list: the agent's main loop looks only every 5 seconds, too slow for a 1-second window. This module is called by the recorder once per second with the live
Kalshi order book; on the tick that lands about 1 second before the close it bets the WHOLE wallet on the favourite, sweeping the book levels it can see (price up to 99c), holds to the result.
Everything is logged (fills, how much of $1,000 filled, skipped rounds and why, missed rounds) so misses and losses can be investigated.
Files in the market-data folder: snipe.json (wallet + totals), snipe_log.jsonl (one line per round). Reset the wallet: python3 sniper.py reset"""
import json, math, os, sys, threading, time, urllib.request
DIR = os.path.expanduser(os.environ.get("MARKET_DIR", "~/market-data"))
START = 1000.0
FIRE_LEFT = 1.3          # trade on the first fresh book that comes back with at most this many seconds left (the order lands about 1 s before the close)
MAX_PX = 0.99            # never pay more than this per contract
_L = threading.Lock()
_ST = {"fired": set(), "cur": None, "thread": None}
def _path(n): return os.path.join(DIR, n)
def load():
    try: return json.load(open(_path("snipe.json")))
    except Exception: return {"bal": START, "start": START, "rounds": 0, "bets": 0, "wins": 0, "losses": 0, "skips": 0, "misses": 0, "pnl": 0.0, "staked": 0.0, "busts": 0, "pending": [], "since": int(time.time())}
def save(s):
    tmp = _path("snipe.json.tmp"); json.dump(s, open(tmp, "w")); os.replace(tmp, _path("snipe.json"))
def log(rec):
    with open(_path("snipe_log.jsonl"), "a") as f: f.write(json.dumps(rec, separators=(",", ":")) + "\n")
def claim(tk, tag="bet"):
    """cross-process once-only marker (two agent processes can overlap for a moment after a restart): True only for the first caller"""
    try:
        d = _path("snipe_claims"); os.makedirs(d, exist_ok=True)
        fd = os.open(os.path.join(d, "%s.%s" % (tk, tag)), os.O_CREAT | os.O_EXCL | os.O_WRONLY); os.close(fd); return True
    except FileExistsError: return False
    except Exception: return True
def seen(tk, tag="bet"): return os.path.exists(os.path.join(_path("snipe_claims"), "%s.%s" % (tk, tag)))
def fee_c(p): return 0.07 * p * (1 - p)
def levels(x, scale):
    out = []
    for a in x or []:
        try: out.append((float(a[0]) / scale, float(a[1])))
        except Exception: pass
    return out
def enabled():
    """OFF by default since 2026-11-06 (Kylar: stop the sniper, go back to experimenting with every strategy). To turn it on again: create the file ~/market-data/sniper.on and restart the agent (bump the marker in collector.py line 2). All its records stay."""
    return os.path.exists(_path("sniper.on"))
def hook(row):
    """Called by the recorder each second: only tells the sniper which round is live, its close time and the target. Never raises."""
    if not enabled(): return
    try:
        k = row.get("k") or {}; tk = k.get("ticker")
        if not tk: return
        from calendar import timegm
        ce = timegm(time.strptime((k.get("close_time") or "")[:19], "%Y-%m-%dT%H:%M:%S"))
        with _L:
            prev = _ST.get("cur")
            if prev and prev["tk"] != tk and _ST.get("zmax"):
                zm = _ST["zmax"]; log({"t": int(time.time()), "ticker": prev["tk"], "result": "ROUND", "max_abs_z": round(zm[0], 2), "left_at_max_z": round(zm[1], 1), "z_ever_ge_min": zm[0] >= Z_MIN, "bought": prev["tk"] in _ST["fired"] and zm[2]})
                _ST["zmax"] = None
            _ST["cur"] = {"tk": tk, "ce": ce, "strike": k.get("floor_strike"), "px": row.get("px")}
            if row.get("px") is not None:
                h = _ST.setdefault("hist", []); h.append((row["t"], float(row["px"]))); del h[:-90]
                zz, _sg = zscore(_ST["cur"], ce - row["t"])
                if zz is not None:
                    zm = _ST.get("zmax")
                    if not zm or abs(zz) > zm[0]: _ST["zmax"] = (abs(zz), ce - row["t"], zm[2] if zm else False)
    except Exception: pass
def _get(url, timeout=2.5):
    req = urllib.request.Request(url, headers={"User-Agent": "starship-market-agent/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r: return json.loads(r.read().decode("utf-8", "replace"))
BASE = "https://api.elections.kalshi.com/trade-api/v2/markets/"
def fetch_book(tk):
    t0 = time.time(); d = _get(BASE + tk + "/orderbook?depth=10")
    ob = d.get("orderbook_fp") or d.get("orderbook") or d
    return ob, t0, time.time()
def fetch_status(tk):
    m = (_get(BASE + tk) or {}).get("market") or {}
    return {k: m.get(k) for k in ("status", "close_time", "can_close_early", "early_close_condition", "yes_bid_dollars", "yes_ask_dollars", "no_bid_dollars", "no_ask_dollars") if m.get(k) is not None}
def fire(tk, ce, strike, px, ob, t_req, t_resp, status, side_seen, mode="close", maxpx=None, force_side=None, extra=None):
    left = ce - t_resp                       # seconds before the close when the book answer came back (the order would land about now)
    if mode == "close" and not claim(tk, "round"): return "DUP"
    s = load(); s["rounds"] += 1
    yl, nl = ob.get("yes_dollars") or ob.get("yes"), ob.get("no_dollars") or ob.get("no")
    both = list(yl or []) + list(nl or [])
    scale = 1.0 if both and max(float(a[0]) for a in both) <= 1.0 else 100.0
    yb, nb = levels(yl, scale), levels(nl, scale)
    base = {"t": int(time.time()), "ticker": tk, "left_at_book": round(left, 2), "book_ms": int((t_resp - t_req) * 1000), "status": status, "px": px, "strike": strike}
    if not yb or not nb:
        if mode == "z": return "NOBOOK"
        s["skips"] += 1; save(s)
        log(dict(base, result="SKIP", why="one side of the book is empty (nobody to buy from): yes levels %d, no levels %d" % (len(yb), len(nb)))); return
    ybest, nbest = max(a for a, b in yb), max(a for a, b in nb)
    side = "YES" if ybest >= nbest else "NO"
    base["mode"] = mode
    if extra: base.update(extra)
    if force_side and force_side != side:
        base["why"] = "model side %s but market favourite %s" % (force_side, side); return "SKIPPED"
    maxpx = maxpx or MAX_PX
    sell_side = nb if side == "YES" else yb              # buy YES by hitting the NO bids: ask = 1 - NO bid
    asks = sorted(((1.0 - p, q) for p, q in sell_side), key=lambda x: x[0])
    budget = s["bal"]; c_tot = 0; cost = 0.0
    for ask, qty in asks:
        if ask > maxpx + 1e-9 or budget < 1: break
        per = ask + fee_c(ask)
        n = int(min(qty, math.floor(budget / per + 1e-9)))
        if n >= 1: c_tot += n; spend = n * per; cost += spend; budget -= spend
    if c_tot < 1:
        if mode == "z": return "NOASK"
        s["skips"] += 1; save(s)
        log(dict(base, result="SKIP", side=side, why="nothing to buy at or below %.1fc (best ask %s)" % (maxpx * 100, round(asks[0][0], 3) if asks else None))); return
    if not claim(tk):
        return "DUP"          # another process already traded this round
    s["bal"] -= cost; s["bets"] += 1; s["staked"] += cost
    s["pending"].append({"ticker": tk, "close": ce, "side": side, "c": c_tot, "cost": round(cost, 4), "t": int(time.time())})
    save(s)
    log(dict(base, result="BOUGHT", side=side, c=c_tot, cost=round(cost, 2), avg_px=round(cost / c_tot, 4), best_ask=round(asks[0][0], 4),
             filled_of_wallet=round(cost / (cost + budget), 3), unfilled_cash=round(budget, 2), levels=[[round(a, 3), q] for a, q in asks[:5]]))
    return "BOUGHT"
Z_MIN = 4.0              # model: price is this many standard deviations from the target (z = gap / (sigma_per_second * sqrt(seconds left)))
Z_ASK_MAX = 0.985        # and the favourite can still be bought at or below this price
Z_LEFT_MIN = 4.0         # never fire the z-rule inside the last 4 s (the 1.3 s close rule covers that)
def zlog(c, left, z, sg, r, base_why=""):
    """log the FIRST z-rule attempt of a round that did not buy (so every round is explained)"""
    if c["tk"] in _ST.setdefault("zlogged", set()): return
    _ST["zlogged"].add(c["tk"])
    log({"t": int(time.time()), "ticker": c["tk"], "result": "Z_NOBUY", "z": round(z, 2), "left": round(left, 1), "sigma_per_s": round(sg, 2), "why": {"NOASK": "z reached the trigger but nothing for sale at or below %.1fc" % (Z_ASK_MAX * 100), "NOBOOK": "z reached the trigger but one side of the book was empty", "SKIPPED": "model side and market favourite disagreed"}.get(r, r)})
def zscore(c, left):
    h = list(_ST.get("hist") or [])[-61:]
    if len(h) < 40 or c.get("strike") is None or c.get("px") is None or left < 1: return None, None
    d = [b[1] - a[1] for a, b in zip(h, h[1:])]
    m = sum(d) / len(d); sg = math.sqrt(sum((x - m) ** 2 for x in d) / len(d))
    if sg <= 0: return None, None
    return (float(c["px"]) - float(c["strike"])) / (sg * math.sqrt(left)), sg
def watch_loop():
    """Two rules, one bet per round, whole wallet, practice only.
    1) Z-RULE (Kylar 21:21, the 'formula'): from 5 min out, read the live book about once a second; the moment the price is >= Z_MIN standard deviations from the target
       (sigma = measured BTC move per second over the last minute) and the favourite is still for sale at <= Z_ASK_MAX, buy what the book offers up to the wallet.
    2) CLOSE RULE: if nothing was bought, from 9 s out read the book about 4x a second and try again on the first fresh book with <= FIRE_LEFT s left (usually nothing for sale)."""
    last_status, st_t, z_t = None, 0.0, 0.0
    while True:
        try:
            with _L: c = dict(_ST.get("cur") or {})
            if not c or c["tk"] in _ST["fired"]: time.sleep(0.2); continue
            left = c["ce"] - time.time()
            if left > 300: time.sleep(min(1.0, max(0.05, left - 300))); continue
            if left < -3:
                _ST["fired"].add(c["tk"])
                if seen(c["tk"], "round") or seen(c["tk"]) or not claim(c["tk"], "miss"): continue
                s = load(); s["rounds"] += 1; s["misses"] += 1; save(s)
                log({"t": int(time.time()), "ticker": c["tk"], "result": "MISSED", "why": "no book reply landed with %.1f s or less to go; last status %s" % (FIRE_LEFT, last_status)}); continue
            if left > 9:
                if time.time() - z_t < 1.0: time.sleep(0.1); continue
                z_t = time.time()
                z, sg = zscore(c, left)
                if z is None or abs(z) < Z_MIN or left < Z_LEFT_MIN: continue
                try: ob, t0, t1 = fetch_book(c["tk"])
                except Exception: continue
                r = fire(c["tk"], c["ce"], c.get("strike"), c.get("px"), ob, t0, t1, last_status, None, mode="z", maxpx=Z_ASK_MAX, force_side="YES" if z > 0 else "NO",
                         extra={"z": round(z, 2), "sigma_per_s": round(sg, 2), "left_at_decision": round(left, 1)})
                if r == "BOUGHT": _ST["fired"].add(c["tk"]); (_ST.get("zmax") and _ST.__setitem__("zmax", (_ST["zmax"][0], _ST["zmax"][1], True)))
                else: zlog(c, left, z, sg, r)
                continue
            if time.time() - st_t >= 1.0:
                st_t = time.time()
                try: last_status = fetch_status(c["tk"])
                except Exception: pass
                if last_status and last_status.get("status") not in (None, "active", "open", "initialized"):
                    _ST["fired"].add(c["tk"]); s = load(); s["rounds"] += 1; s["misses"] += 1; save(s)
                    log({"t": int(time.time()), "ticker": c["tk"], "result": "MISSED", "why": "Kalshi closed the round early (status %s) with %.1f s on our clock" % (last_status.get("status"), left), "status": last_status}); continue
            try: ob, t0, t1 = fetch_book(c["tk"])
            except Exception: time.sleep(0.05); continue
            z, sg = zscore(c, c["ce"] - t1)
            if z is not None and abs(z) >= Z_MIN and (c["ce"] - t1) >= Z_LEFT_MIN:
                r = fire(c["tk"], c["ce"], c.get("strike"), c.get("px"), ob, t0, t1, last_status, None, mode="z", maxpx=Z_ASK_MAX, force_side="YES" if z > 0 else "NO", extra={"z": round(z, 2), "sigma_per_s": round(sg, 2)})
                if r == "BOUGHT": _ST["fired"].add(c["tk"]); (_ST.get("zmax") and _ST.__setitem__("zmax", (_ST["zmax"][0], _ST["zmax"][1], True))); continue
                else: zlog(c, c["ce"] - t1, z, sg, r)
            if c["ce"] - t1 <= FIRE_LEFT and c["ce"] - t1 > -0.5:
                _ST["fired"].add(c["tk"]); fire(c["tk"], c["ce"], c.get("strike"), c.get("px"), ob, t0, t1, last_status, None, mode="close")
            time.sleep(0.05)
        except Exception as e:
            try: log({"t": int(time.time()), "result": "ERROR", "why": repr(e)[:160]})
            except Exception: pass
            time.sleep(0.5)
def settle_loop():
    while True:
        time.sleep(5)
        try:
            with _L: s = load(); pend = list(s.get("pending") or [])
            if not pend: continue
            done = []
            for p in pend:
                if time.time() < p["close"] + 3: continue
                try: m = (_get("https://api.elections.kalshi.com/trade-api/v2/markets/%s" % p["ticker"]) or {}).get("market") or {}
                except Exception: continue
                res = m.get("result")
                if res not in ("yes", "no"):
                    if time.time() - p["close"] > 3600: done.append((p, None))
                    continue
                done.append((p, res))
            if not done: continue
            with _L:
                s = load()
                for p, res in done:
                    s["pending"] = [x for x in s["pending"] if x["ticker"] != p["ticker"]]
                    if res is None: log({"t": int(time.time()), "ticker": p["ticker"], "result": "UNSETTLED", "why": "no result from Kalshi after an hour"}); continue
                    won = (res == "yes") == (p["side"] == "YES")
                    pay = float(p["c"]) if won else 0.0; pnl = pay - p["cost"]
                    s["bal"] += pay; s["pnl"] = round(s["pnl"] + pnl, 2); s["wins" if won else "losses"] += 1
                    if s["bal"] < 5.0: s["bal"] = START; s["busts"] += 1
                    log({"t": int(time.time()), "ticker": p["ticker"], "result": "WON" if won else "LOST", "side": p["side"], "c": p["c"], "cost": p["cost"], "pnl": round(pnl, 2), "kalshi_result": res, "bal": round(s["bal"], 2)})
                save(s)
        except Exception: pass
def start():
    if _ST["thread"]: return
    if enabled(): threading.Thread(target=watch_loop, daemon=True, name="sniper-watch").start()   # no new bets while off; the settle thread below still settles any open one
    th = threading.Thread(target=settle_loop, daemon=True, name="sniper-settle"); th.start(); _ST["thread"] = th
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "reset":
        os.makedirs(DIR, exist_ok=True)
        if os.path.exists(_path("snipe.json")): os.replace(_path("snipe.json"), _path("snipe.%d.json" % int(time.time())))
        if os.path.exists(_path("snipe_log.jsonl")): os.replace(_path("snipe_log.jsonl"), _path("snipe_log.%d.jsonl" % int(time.time())))
        save(load()); print("$1K-Snipe wallet reset to $%d (old files kept)" % START)
    else:
        s = load(); print({k: s[k] for k in ("bal", "rounds", "bets", "wins", "losses", "skips", "misses", "pnl", "staked", "busts")})
