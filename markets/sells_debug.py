"""Read-only. For the last unfilled sells: what the market looked like (from the per-second recording) and what Kalshi says about each order.
Only GET requests, nothing is sent or changed."""
import glob, gzip, json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
D = os.path.expanduser("~/market-data")
hm = lambda t: time.strftime("%H:%M:%S", time.localtime(t))

orders = []
for l in open(os.path.join(D, "live_orders.jsonl")):
    try:
        o = json.loads(l)
    except ValueError:
        continue
    if o.get("action") == "sell" and float((o.get("reply") or {}).get("fill_count") or 0) == 0:
        orders.append(o)
orders = orders[-4:]
ticks = {}
for p in sorted(glob.glob(os.path.join(D, "ticks-*.jsonl*"))):
    try:
        for ln in (gzip.open(p, "rt") if p.endswith(".gz") else open(p)):
            try:
                r = json.loads(ln); ticks[int(r["t"])] = r
            except ValueError:
                pass
    except OSError:
        pass
try:
    import kalshi_trade as kt
    c = kt.Kalshi()
except BaseException as e:
    c = None; print("no Kalshi client:", e)
for o in orders:
    print("\nSELL at", hm(o["t"]), "side", o.get("side"), "count", o.get("count"), "limit", o.get("price"), "book_side", o.get("book_side"), "quote bid/ask", o.get("quote_bid"), o.get("quote_ask"))
    r = ticks.get(int(o["t"])) or ticks.get(int(o["t"]) - 1) or ticks.get(int(o["t"]) + 1)
    if r:
        k = r.get("k") or {}
        print("  recording then: bid", k.get("yes_bid_dollars"), "ask", k.get("yes_ask_dollars"), "bid size", k.get("yes_bid_size_fp"), "| book yes:", (r.get("ob") or {}).get("yes_dollars"), "no:", (r.get("ob") or {}).get("no_dollars"))
    else:
        print("  no recorded second at that time")
    oid = (o.get("reply") or {}).get("order_id")
    if c and oid:
        for path in ("/portfolio/events/orders/" + oid, "/portfolio/orders/" + oid):
            try:
                st, j = c.call("GET", path)
                print("  Kalshi", path.split("/portfolio/")[1][:12], "->", st, json.dumps(j)[:500])
                if st == 200:
                    break
            except Exception as e:
                print("  lookup failed:", str(e)[:80])
if c:
    try:
        st, j = c.call("GET", "/portfolio/positions?count_filter=position")
        print("\nKalshi positions now:", st, json.dumps(j)[:300])
    except Exception as e:
        print("positions failed", e)
