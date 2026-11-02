#!/bin/bash
# Real-money order test, a few cents at most. It buys 1 Up and sells it, then buys 1 Down and sells it,
# using the exact same code the live wallet uses, and prints what Kalshi says each time.
cd ~/starship/markets && python3 - <<'PY'
import json, time, urllib.request, kalshi_trade as k
c = k.Kalshi(); b = k.Broker(c)
print("environment:", c.mode)
if c.mode != "prod": print("(this is the demo environment)")
m = json.loads(urllib.request.urlopen("https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXBTC15M&status=open", timeout=10).read())["markets"][0]
def cents(x): return float(x) if float(x) <= 1 else float(x) / 100
bid = cents(m.get("yes_bid_dollars", m.get("yes_bid"))); ask = cents(m.get("yes_ask_dollars", m.get("yes_ask")))
print("market", m["ticker"], "yes bid", bid, "ask", ask)
if not (0.08 <= bid <= 0.92 and ask - bid <= 0.05): raise SystemExit("Market is too lopsided or too wide right now. Try again in a few minutes.")
print("Cost: a few cents (spread plus fees). Type yes to place 1 Up and 1 Down test trades: ", end="", flush=True)
if open("/dev/tty").readline().strip().lower() != "yes": raise SystemExit("Cancelled. Nothing placed.")
def pos():
    s, p = c.positions(); print("   positions ->", s, json.dumps(p)[:400])
bal0 = b.balance(0); print("balance before:", bal0)
for action, side in (("buy", "UP"), ("sell", "UP"), ("buy", "DOWN"), ("sell", "DOWN")):
    n = b.trade(action, m["ticker"], side, 1, ask, bid)
    print(action.upper(), side, "-> filled", n, "| last reply:", json.dumps(json.loads(open(k.DIR + "/live_orders.jsonl").read().strip().splitlines()[-1]))[:420])
    pos(); time.sleep(1.5)
    if n < 1 and action == "buy": print("   did not fill, skipping the matching sell"); 
bal1 = b.balance(0); print("balance after:", bal1, "| test cost: $%.2f" % (bal0 - bal1))
PY
