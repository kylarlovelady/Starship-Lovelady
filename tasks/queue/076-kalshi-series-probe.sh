#!/bin/bash
# QUEUE-OK
# read-only: which short-term crypto series exist on Kalshi, and what their order books look like right now
python3 - <<'PY'
import json, urllib.request
def get(u):
    r = urllib.request.Request(u, headers={"User-Agent": "starship-market-agent/1.0"})
    return json.loads(urllib.request.urlopen(r, timeout=10).read().decode())
base = "https://api.elections.kalshi.com/trade-api/v2"
try:
    s = get(base + "/series?category=Crypto")
    ser = s.get("series", [])
    print("crypto series:", len(ser))
    for x in ser:
        t = x.get("ticker", "")
        if any(k in t for k in ("15M", "1H", "HOUR", "60M", "30M", "5M")):
            print(" ", t, "|", (x.get("title") or "")[:60], "|", x.get("frequency"))
except Exception as e:
    print("series list failed:", e)
for t in ("KXBTC15M", "KXETH15M", "KXSOL15M", "KXXRP15M", "KXDOGE15M", "KXBTCD", "KXETHD", "KXBTC", "KXETH"):
    try:
        d = get(base + "/markets?series_ticker=%s&status=open&limit=3" % t)
        ms = d.get("markets", [])
        if not ms:
            print(t, "no open markets"); continue
        for m in ms[:2]:
            print(t, m.get("ticker"), "close", m.get("close_time"), "strike", m.get("floor_strike") or m.get("cap_strike"), "yes", m.get("yes_bid_dollars"), m.get("yes_ask_dollars"), "vol", m.get("volume_fp"), "oi", m.get("open_interest"))
    except Exception as e:
        print(t, "error", str(e)[:80])
PY
