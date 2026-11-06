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
def fee_c(p): return 0.07 * p * (1 - p)
def levels(x, scale):
    out = []
    for a in x or []:
        try: out.append((float(a[0]) / scale, float(a[1])))
        except Exception: pass
    return out
def hook(row):
    """Called by the recorder each second: only tells the sniper which round is live, its close time and the target. Never raises."""
    try:
        k = row.get("k") or {}; tk = k.get("ticker")
        if not tk: return
        from calendar import timegm
        ce = timegm(time.strptime((k.get("close_time") or "")[:19], "%Y-%m-%dT%H:%M:%S"))
        with _L: _ST["cur"] = {"tk": tk, "ce": ce, "strike": k.get("floor_strike"), "px": row.get("px")}
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
def fire(tk, ce, strike, px, ob, t_req, t_resp, status, side_seen):
    left = ce - t_resp                       # seconds before the close when the book answer came back (the order would land about now)
    s = load(); s["rounds"] += 1
    yl, nl = ob.get("yes_dollars") or ob.get("yes"), ob.get("no_dollars") or ob.get("no")
    both = list(yl or []) + list(nl or [])
    scale = 1.0 if both and max(float(a[0]) for a in both) <= 1.0 else 100.0
    yb, nb = levels(yl, scale), levels(nl, scale)
    base = {"t": int(time.time()), "ticker": tk, "left_at_book": round(left, 2), "book_ms": int((t_resp - t_req) * 1000), "status": status, "px": px, "strike": strike}
    if not yb or not nb:
        s["skips"] += 1; save(s)
        log(dict(base, result="SKIP", why="one side of the book is empty (nobody to buy from): yes levels %d, no levels %d" % (len(yb), len(nb)))); return
    ybest, nbest = max(a for a, b in yb), max(a for a, b in nb)
    side = "YES" if ybest >= nbest else "NO"
    sell_side = nb if side == "YES" else yb              # buy YES by hitting the NO bids: ask = 1 - NO bid
    asks = sorted(((1.0 - p, q) for p, q in sell_side), key=lambda x: x[0])
    budget = s["bal"]; c_tot = 0; cost = 0.0
    for ask, qty in asks:
        if ask > MAX_PX + 1e-9 or budget < 1: break
        per = ask + fee_c(ask)
        n = int(min(qty, math.floor(budget / per + 1e-9)))
        if n >= 1: c_tot += n; spend = n * per; cost += spend; budget -= spend
    if c_tot < 1:
        s["skips"] += 1; save(s)
        log(dict(base, result="SKIP", side=side, why="nothing to buy at or below %dc (best ask %s)" % (int(MAX_PX * 100), round(asks[0][0], 3) if asks else None))); return
    s["bal"] -= cost; s["bets"] += 1; s["staked"] += cost
    s["pending"].append({"ticker": tk, "close": ce, "side": side, "c": c_tot, "cost": round(cost, 4), "t": int(time.time())})
    save(s)
    log(dict(base, result="BOUGHT", side=side, c=c_tot, cost=round(cost, 2), avg_px=round(cost / c_tot, 4), best_ask=round(asks[0][0], 4),
             filled_of_wallet=round(cost / (cost + budget), 3), unfilled_cash=round(budget, 2), levels=[[round(a, 3), q] for a, q in asks[:5]]))
def watch_loop():
    """Own clock, own Kalshi requests. From 9 s before the close it re-reads the live order book about 4 times a second (and the market status once a second);
    the first book that comes back with <= FIRE_LEFT seconds to go is the one it trades on."""
    last_status, st_t, st_fail = None, 0.0, 0
    while True:
        try:
            with _L: c = dict(_ST.get("cur") or {})
            if not c or c["tk"] in _ST["fired"]: time.sleep(0.2); continue
            left = c["ce"] - time.time()
            if left > 9: time.sleep(min(1.0, max(0.05, left - 9))); continue
            if left < -3:                                   # the round ended and we never traded it
                _ST["fired"].add(c["tk"]); s = load(); s["rounds"] += 1; s["misses"] += 1; save(s)
                log({"t": int(time.time()), "ticker": c["tk"], "result": "MISSED", "why": "no book reply landed with %.1f s or less to go; last status %s" % (FIRE_LEFT, last_status)}); continue
            if time.time() - st_t >= 1.0:
                st_t = time.time()
                try: last_status = fetch_status(c["tk"]); st_fail = 0
                except Exception: st_fail += 1
                if last_status and last_status.get("status") not in (None, "active", "open", "initialized"):
                    _ST["fired"].add(c["tk"]); s = load(); s["rounds"] += 1; s["misses"] += 1; save(s)
                    log({"t": int(time.time()), "ticker": c["tk"], "result": "MISSED", "why": "Kalshi closed the round early (status %s) with %.1f s on our clock" % (last_status.get("status"), left), "status": last_status, "px": c.get("px"), "strike": c.get("strike")}); continue
            try: ob, t0, t1 = fetch_book(c["tk"])
            except Exception: time.sleep(0.05); continue
            if c["ce"] - t1 <= FIRE_LEFT and c["ce"] - t1 > -0.5:
                _ST["fired"].add(c["tk"]); fire(c["tk"], c["ce"], c.get("strike"), c.get("px"), ob, t0, t1, last_status, None)
            elif c["ce"] - t1 <= -0.5:
                pass
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
    threading.Thread(target=watch_loop, daemon=True, name="sniper-watch").start()
    th = threading.Thread(target=settle_loop, daemon=True, name="sniper-settle"); th.start(); _ST["thread"] = th
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "reset":
        os.makedirs(DIR, exist_ok=True)
        if os.path.exists(_path("snipe.json")): os.replace(_path("snipe.json"), _path("snipe.%d.json" % int(time.time())))
        if os.path.exists(_path("snipe_log.jsonl")): os.replace(_path("snipe_log.jsonl"), _path("snipe_log.%d.jsonl" % int(time.time())))
        save(load()); print("$1K-Snipe wallet reset to $%d (old files kept)" % START)
    else:
        s = load(); print({k: s[k] for k in ("bal", "rounds", "bets", "wins", "losses", "skips", "misses", "pnl", "staked", "busts")})
