#!/bin/bash
# Read-only. Checks which numbers the agent really gets from Kalshi and which it assumes. Places no orders, changes nothing.
cd ~/starship/markets 2>/dev/null || exit 1
python3 - <<'PY'
import glob, gzip, json, math, os, sys, time, collections
sys.path.insert(0, ".")
D = os.path.expanduser("~/market-data")
def lines(p):
    op = gzip.open if p.endswith(".gz") else open
    try:
        with op(p, "rt") as f:
            for l in f:
                try: yield json.loads(l)
                except ValueError: pass
    except OSError:
        return
print("1. PRICES: where did the agent's Kalshi price come from? (snapshots, one per minute)")
c = collections.Counter(r.get("qsrc", "old") for r in lines(os.path.join(D, "snapshots.jsonl")))
print("   ", dict(c), "(book = live order book, list = the lagging market list, old = before the fix)")
fs = sorted(glob.glob(os.path.join(D, "ticks-*.jsonl*")))[-2:]
n = ob = k = 0
for p in fs:
    for r in lines(p):
        n += 1; ob += 1 if r.get("ob") else 0; k += 1 if r.get("k") else 0
print("    per-second recording: %d seconds, order book present %d%%, market data present %d%%" % (n, 100 * ob // max(1, n), 100 * k // max(1, n)))
print("2. RESULTS: how were finished rounds settled in the practice scoreboard?")
c = collections.Counter(r.get("src") for r in lines(os.path.join(D, "sim_windows.jsonl")))
print("   ", dict(c), "(kalshi = Kalshi's official result; anything else is an assumption)")
c = collections.Counter(r.get("src") for r in lines(os.path.join(D, "calls.jsonl")))
print("    calls log:", dict(c))
print("3. BITCOIN PRICE: Kalshi settles on its own reference price; the agent uses Coinbase plus an offset.")
try:
    S = json.load(open(os.path.join(D, "state.json"))); A = S.get("audit") or {}
    print("    current offset: $%s over %s rounds checked" % (A.get("offset"), A.get("n")))
except Exception as e:
    print("    could not read:", e)
print("4. FEES: the agent assumes 7% x price x (1 - price) per contract. What did Kalshi really charge on your real fills?")
try:
    import kalshi_trade as K
    c = K.Kalshi()
    rows, cur = [], None
    for _ in range(10):
        st, d = c.call("GET", "/portfolio/fills?limit=200" + ("&cursor=" + cur if cur else ""))
        if st != 200: break
        rows += d.get("fills") or []; cur = d.get("cursor")
        if not cur or not d.get("fills"): break
    real = formula = 0.0; n = 0; maker = 0
    for r in rows:
        try:
            side = r.get("side"); px = float(r.get("yes_price_dollars") if side == "yes" else r.get("no_price_dollars"))
            cnt = float(r.get("count_fp") if r.get("count_fp") is not None else r.get("count")); fee = float(r.get("fee_cost") or 0)
        except (TypeError, ValueError):
            continue
        n += 1; real += fee; formula += 0.07 * cnt * px * (1 - px)
        if r.get("is_taker") is False: maker += 1
    print("    %d fills: Kalshi charged $%.2f in total, the agent's formula says $%.2f (ratio %.2f; 1.00 = exact), %d fills were maker fills" % (n, real, formula, real / formula if formula else 0, maker))
except SystemExit as e:
    print("    skipped:", e)
except Exception as e:
    print("    skipped:", e)
print("5. SLIPPAGE: practice assumes every buy and sell fills at the quote. What did real orders do?")
sl = [json.loads(l) for l in open(os.path.join(D, "live_orders.jsonl")) if '"slip_cents"' in l] if os.path.exists(os.path.join(D, "live_orders.jsonl")) else []
if sl: print("    %d real fills, average %.2f cents worse than the quote, worst %.1f" % (len(sl), sum(x["slip_cents"] for x in sl) / len(sl), max(x["slip_cents"] for x in sl)))
else: print("    no real fills logged")
PY
