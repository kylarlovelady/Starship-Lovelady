#!/usr/bin/env python3
"""Independent safety net, run every minute by cron. If a LIVE session is active but the agent has stopped updating
(frozen, crashed, or cannot reach Kalshi), this closes out: turns live off, cancels resting orders, sells any open
15-minute BTC position, and alerts the phone. It does nothing at all when no live session is active."""
import json, os, sys, time, urllib.request

HOME = os.path.expanduser("~")
DIR = os.environ.get("MARKET_DIR", os.path.join(HOME, "market-data"))
OUT = os.environ.get("MARKET_OUT", os.path.join(HOME, "crew-web", "market.json"))
STALE = 90
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def load(p, d):
    try:
        return json.load(open(p))
    except Exception:
        return d


def main():
    rc = load(os.path.join(DIR, "run.json"), {})
    if not (rc.get("live") and rc.get("active")):
        return
    try:
        age = time.time() - os.path.getmtime(OUT)
    except OSError:
        age = 1e9
    if age < STALE:
        return
    import alerts, kalshi_trade as kt
    alerts.send("WATCHDOG: the agent stopped updating for %d seconds during a live session. Closing out now." % age, "Market agent: watchdog", wait=True)
    tmp = os.path.join(DIR, "run.json.tmp")
    json.dump({"active": False, "live": True, "halted": "watchdog", "detail": "The agent froze or stopped; the watchdog closed out.", "t": int(time.time())}, open(tmp, "w"))
    os.replace(tmp, os.path.join(DIR, "run.json"))
    b = kt.Broker(kt.Kalshi(), DIR)
    print("cancel all:", b.cancel_all())
    st, p = b.c.call("GET", "/portfolio/positions?count_filter=position")
    closed = []
    for m in (p.get("market_positions") or []) if st == 200 else []:
        t = m.get("ticker", "")
        q = float(m.get("position_fp") or 0)
        if not t.startswith("KXBTC15M") or abs(q) < 0.005:
            continue
        mk = json.loads(urllib.request.urlopen("https://api.elections.kalshi.com/trade-api/v2/markets/" + t, timeout=10).read())["market"]
        px = lambda k: float(mk[k + "_dollars"]) if mk.get(k + "_dollars") is not None else float(mk[k]) / 100.0
        bid, ask = px("yes_bid"), px("yes_ask")
        n = b.trade("sell", t, "UP" if q > 0 else "DOWN", abs(q), ask, bid)
        closed.append((t, q, n))
    msg = "Watchdog closed out: %s" % (closed or "no open 15-minute positions found")
    print(msg)
    alerts.send(msg, "Market agent: watchdog", wait=True)


if __name__ == "__main__":
    main()
