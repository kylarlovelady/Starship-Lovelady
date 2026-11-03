"""Reads the per-second recording (ticks-*.jsonl[.gz]) and answers, with real numbers:
  1. How complete is the recording?
  2. If you bought the favourite and held to the end, what did each entry price range really pay (after fees)?
     This is the evidence behind the entry price cap.
  3. For every order the agent sent: what did the market do 30 and 60 seconds later?
Read-only. Usage: python3 ticks_report.py [data_dir]"""
import glob, gzip, json, math, os, sys
from collections import defaultdict

D = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.expanduser("~"), "market-data")


def fee(p):
    return 0.07 * p * (1 - p)


def lines(path):
    op = gzip.open if path.endswith(".gz") else open
    try:
        with op(path, "rt") as f:
            for ln in f:
                try:
                    yield json.loads(ln)
                except ValueError:
                    pass
    except OSError:
        return


def cents(k, name):
    v = k.get(name)
    if v is None:
        v = k.get(name + "_dollars")
        if v is None:
            return None
        return float(v) * 100
    v = float(v)
    return v * 100 if isinstance(k.get(name), str) and v <= 1.0 else v


def load_ticks():
    rows = []
    for p in sorted(glob.glob(os.path.join(D, "ticks-*.jsonl*"))):
        rows.extend(lines(p))
    rows.sort(key=lambda r: r["t"])
    return rows


def outcomes():
    out = {}
    for c in lines(os.path.join(D, "calls.jsonl")):
        if c.get("ticker") and c.get("outcome") in ("UP", "DOWN") and c.get("src") == "kalshi":
            out[c["ticker"]] = c["outcome"]
    return out


def quote(r):
    k = r.get("k") or {}
    b, a = cents(k, "yes_bid"), cents(k, "yes_ask")
    return (b, a) if b is not None and a is not None else (None, None)


def main():
    rows = load_ticks()
    if not rows:
        print("No ticks recorded yet (the recorder starts when the collector restarts with the new code).")
        return
    span = rows[-1]["t"] - rows[0]["t"]
    gaps = sum(1 for a, b in zip(rows, rows[1:]) if b["t"] - a["t"] > 5)
    errs = defaultdict(int)
    for r in rows:
        for n in (r.get("err") or {}):
            errs[n] += 1
    print("RECORDING: %d seconds of data over %.1f hours, %d gaps longer than 5 s" % (len(rows), span / 3600, gaps))
    print("  with Kalshi prices: %d%%, order book: %d%%, other exchanges: %d%%, trade flow: %d%%, open interest: %d%%" % tuple(
        round(100 * sum(1 for r in rows if r.get(k)) / len(rows)) for k in ("k", "ob", "x", "flow", "oi")))
    if errs:
        print("  feeds that failed at times (seconds failing):", dict(errs))
    res = outcomes()
    byk = defaultdict(list)
    for r in rows:
        tk = (r.get("k") or {}).get("ticker")
        if tk:
            byk[tk].append(r)
    # 2. favourite held to the end, by entry price range and by minutes into the round
    BU = [(0, 60), (60, 70), (70, 80), (80, 90), (90, 100)]
    stat = defaultdict(lambda: [0, 0, 0.0])
    for tk, rs in byk.items():
        if tk not in res:
            continue
        up = res[tk] == "UP"
        for sec_left in (840, 720, 600, 480, 360, 240, 120):
            r = min(rs, key=lambda x: abs((x.get("left") or 9e9) - sec_left))
            if abs((r.get("left") or 9e9) - sec_left) > 6:
                continue
            b, a = quote(r)
            if b is None:
                continue
            side_up = a >= (100 - b)                     # the favourite is the dearer side
            px = (a if side_up else 100 - b) / 100.0
            won = (up if side_up else not up)
            prof = (1 - px - fee(px)) if won else (-px - fee(px))
            for lo, hi in BU:
                if lo <= px * 100 < hi or (hi == 100 and px * 100 >= 100):
                    s = stat[(lo, hi)]
                    s[0] += 1; s[1] += int(won); s[2] += prof
    if stat:
        print("\nBUY THE FAVOURITE AND HOLD (all recorded rounds, entries 2-14 minutes in), per contract after fees:")
        print("  price      entries  wins   avg result")
        for lo, hi in BU:
            n, w, p = stat.get((lo, hi), (0, 0, 0.0))
            if n:
                print("  %2d-%3d c   %5d   %3d%%   %+5.1f c" % (lo, hi, n, round(100 * w / n), 100 * p / n))
    else:
        print("\n(no finished rounds with both ticks and Kalshi results yet)")
    # 3. orders and what happened after
    orders = []
    for r in lines(os.path.join(D, "trades.jsonl")):
        if r.get("a") in ("BUY", "SELL") and r.get("ticker"):
            orders.append(r)
    if orders:
        print("\nTRADES AND THE MARKET 30 / 60 SECONDS LATER (Up-contract price in cents, change shown for the side traded):")
        idx = {tk: rs for tk, rs in byk.items()}
        shown = 0
        for o in orders[-40:]:
            rs = idx.get(o["ticker"])
            if not rs:
                continue
            def mid_at(dt):
                r = min(rs, key=lambda x: abs(x["t"] - (o["t"] + dt)))
                if abs(r["t"] - (o["t"] + dt)) > 6:
                    return None
                b, a = quote(r)
                return None if b is None else (b + a) / 2
            m0, m30, m60 = mid_at(0), mid_at(30), mid_at(60)
            sign = 1 if o["side"] == "UP" else -1
            def chg(m):
                return "   n/a" if m is None or m0 is None else "%+5.1f" % (sign * (m - m0))
            print("  %s %-4s %-4s %3dx @%2d c  after 30s %s  after 60s %s   [%s]" % (
                __import__("time").strftime("%m-%d %H:%M:%S", __import__("time").localtime(o["t"])), o.get("s"), o["a"] + " " + o["side"],
                int(o.get("c") or 0), round((o.get("px") or 0) * 100), chg(m30), chg(m60), "live" if o.get("live") else "practice"))
            shown += 1
        if not shown:
            print("  (none of the logged trades overlap the recording yet)")


main()
