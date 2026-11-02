#!/bin/bash
# Safe Kalshi connection test. It checks the balance, rests a 1-contract bid at 1 cent (it will not fill), then cancels it.
cd ~/starship/markets && python3 - <<'PY'
import json, kalshi_trade as k
c = k.Kalshi()
print("environment:", c.mode)
s, b = c.balance(); print("balance ->", s, json.dumps(b)[:300])
if s != 200: raise SystemExit("Could not read the balance. Send me this output.")
import urllib.request
m = json.loads(urllib.request.urlopen("https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXBTC15M&status=open", timeout=10).read())["markets"]
print("open BTC 15m markets:", [x["ticker"] for x in m][:3])
if c.mode != "demo":
    print("REAL account. Place a 1 contract bid at 1 cent and cancel it right away? Type yes: ", end="", flush=True)
    if open("/dev/tty").readline().strip().lower() != "yes":
        raise SystemExit("Skipped the order test. Balance check was fine.")
t = m[0]["ticker"]
s, o = c.order(t, "bid", 1, 0.01); print("order ->", s, json.dumps(o)[:500])
oid = (o.get("order") or o).get("order_id") or (o.get("order") or o).get("id")
if oid:
    s, x = c.cancel(oid); print("cancel ->", s, json.dumps(x)[:300])
s, p = c.positions(); print("positions ->", s, json.dumps(p)[:300])
PY
