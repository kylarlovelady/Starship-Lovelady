#!/usr/bin/env python3
"""BTC 15-minute call engine. PAPER MODE ONLY: it reads public data, makes one
call per 15-minute window (UP / DOWN / NONE), scores itself, and writes
market.json for the Markets page. It never places orders and never touches
Kalshi accounts or keys. Standard library only."""
import json, math, os, re, sys, time, urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

HOME = os.path.expanduser("~")
DIR = os.environ.get("MARKET_DIR", os.path.join(HOME, "market-data"))
OUT = os.environ.get("MARKET_OUT", os.path.join(HOME, "crew-web", "market.json"))
WINDOW = 900            # 15 minutes
CYCLE = 20              # seconds between looks
THRESHOLD = 12          # |score| needed to lean; below that the call is NONE
WEIGHTS = {"book": 0.30, "momentum": 0.20, "whales": 0.25, "news": 0.15, "fng": 0.05, "funding": 0.05}
LABELS = {"book": "Order book", "momentum": "Price momentum", "whales": "Whale moves",
          "news": "News vibe", "fng": "Fear & Greed", "funding": "Funding rate"}
EVERY = {"whales": 60, "news": 300, "fng": 3600, "funding": 120, "kalshi": 60}
FEEDS = ["https://www.coindesk.com/arc/outboundfeeds/rss/", "https://cointelegraph.com/rss",
         "https://decrypt.co/feed", "https://bitcoinmagazine.com/.rss/full/"]
BULL = ["surge", "rally", "soar", "jump", "record high", "all-time high", "approve", "approval",
        "inflow", "adoption", "accumulat", "bullish", "breakout", "gains", "rises", "climb",
        "upgrade", "partnership", "buys", "buying", "rebound", "recover"]
BEAR = ["crash", "plunge", "drop", "falls", "slump", "hack", "exploit", "ban", "lawsuit", "sues",
        "outflow", "sell-off", "selloff", "liquidat", "bearish", "fear", "dump", "warning",
        "probe", "fraud", "arrest", "bankrupt", "tumble", "sinks", "rejects", "delay"]


# ---------- fetching (monkeypatched in tests) ----------
def fetch(url, timeout=10):
    req = urllib.request.Request(url, headers={"User-Agent": "starship-market-agent/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def fetch_json(url, timeout=10):
    return json.loads(fetch(url, timeout))


def clamp(x, lo=-1.0, hi=1.0):
    return max(lo, min(hi, x))


# ---------- signals: each returns (score -1..1, detail) or raises ----------
def get_price():
    try:
        return float(fetch_json("https://api.exchange.coinbase.com/products/BTC-USD/ticker")["price"])
    except Exception:
        d = fetch_json("https://api.kraken.com/0/public/Ticker?pair=XBTUSD")["result"]
        return float(list(d.values())[0]["c"][0])


def sig_book(price):
    try:
        b = fetch_json("https://api.exchange.coinbase.com/products/BTC-USD/book?level=2")
        bids = [(float(p), float(s)) for p, s, *_ in b["bids"]]
        asks = [(float(p), float(s)) for p, s, *_ in b["asks"]]
    except Exception:
        b = list(fetch_json("https://api.kraken.com/0/public/Depth?pair=XBTUSD&count=50")["result"].values())[0]
        bids = [(float(p), float(s)) for p, s, *_ in b["bids"]]
        asks = [(float(p), float(s)) for p, s, *_ in b["asks"]]
    mid = (bids[0][0] + asks[0][0]) / 2
    bv = sum(s for p, s in bids if p >= mid * 0.997)
    av = sum(s for p, s in asks if p <= mid * 1.003)
    imb = (bv - av) / (bv + av) if bv + av else 0
    return clamp(imb * 2), "%.0f BTC of buyers vs %.0f BTC of sellers within 0.3%%" % (bv, av)


def sig_momentum(history, now):
    def ago(sec):
        older = [p for t, p in history if t <= now - sec]
        return older[-1] if older else None
    p = history[-1][1]
    a5, a15 = ago(300), ago(900)
    if a5 is None:
        raise ValueError("needs 5 minutes of history")
    r5 = p / a5 - 1
    s = 0.6 * math.tanh(r5 / 0.0012)
    txt = "5 min %+.2f%%" % (r5 * 100)
    if a15 is not None:
        r15 = p / a15 - 1
        s += 0.4 * math.tanh(r15 / 0.002)
        txt += ", 15 min %+.2f%%" % (r15 * 100)
    else:
        s /= 0.6
    return clamp(s), txt


def sig_whales(now):
    key = os.environ.get("WHALE_ALERT_KEY")
    if not key:
        raise ValueError("no Whale Alert key set")
    d = fetch_json("https://api.whale-alert.io/v1/transactions?api_key=%s&min_value=10000000&currency=btc&start=%d" % (key, now - 1800))
    inflow = outflow = 0.0
    for t in d.get("transactions", []):
        fo, to = (t.get("from") or {}).get("owner_type"), (t.get("to") or {}).get("owner_type")
        usd = float(t.get("amount_usd", 0))
        if to == "exchange" and fo != "exchange":
            inflow += usd
        elif fo == "exchange" and to != "exchange":
            outflow += usd
    net = outflow - inflow
    return clamp(math.tanh(net / 50e6)), "last 30 min: $%.0fM moved onto exchanges, $%.0fM off" % (inflow / 1e6, outflow / 1e6)


def lex(title):
    t = title.lower()
    s = sum(1 for w in BULL if w in t) - sum(1 for w in BEAR if w in t)
    return max(-2, min(2, s))


def read_feed(url, now):
    root = ET.fromstring(fetch(url))
    out = []
    for it in root.iter("item"):
        title = (it.findtext("title") or "").strip()
        try:
            ts = parsedate_to_datetime(it.findtext("pubDate")).timestamp()
        except Exception:
            continue
        if title and now - ts < 6 * 3600:
            out.append({"title": title, "ts": ts, "src": url.split("/")[2].replace("www.", "")})
    return out


def sig_news(now, cache):
    items = []
    for u in FEEDS:
        try:
            items += read_feed(u, now)
        except Exception:
            pass
    if not items:
        raise ValueError("no news feeds reachable")
    seen, uniq = set(), []
    for i in sorted(items, key=lambda x: -x["ts"]):
        if i["title"] not in seen:
            seen.add(i["title"]); uniq.append(i)
    total, scored = 0.0, []
    for i in uniq:
        s = lex(i["title"])
        rel = 1.0 if re.search(r"bitcoin|btc", i["title"], re.I) else 0.5
        w = math.exp(-((now - i["ts"]) / 3600) / 2) * rel
        total += s * w
        scored.append((abs(s * w), i, s))
    scored.sort(key=lambda x: -x[0])
    cache["headlines"] = [{"title": i["title"], "src": i["src"], "mood": "bull" if s > 0 else "bear" if s < 0 else "flat",
                           "age_min": int((now - i["ts"]) / 60)} for _, i, s in scored[:6]]
    return clamp(math.tanh(total / 2.5)), "%d stories in the last 6 hours" % len(uniq)


def sig_fng():
    v = int(fetch_json("https://api.alternative.me/fng/?limit=1")["data"][0]["value"])
    return clamp((v - 50) / 50 * 0.6), "Fear & Greed index %d" % v


def sig_funding():
    r = float(fetch_json("https://www.okx.com/api/v5/public/funding-rate?instId=BTC-USDT-SWAP")["data"][0]["fundingRate"])
    return clamp(-math.tanh(r / 0.0003) * 0.5), "funding rate %+.4f%% (crowded longs lean bearish)" % (r * 100)


def get_kalshi():
    d = fetch_json("https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXBTC15M&status=open&limit=5")
    ms = sorted(d.get("markets", []), key=lambda m: m.get("close_time", ""))
    if not ms:
        raise ValueError("no open market")
    m = ms[0]
    bid, ask = m.get("yes_bid"), m.get("yes_ask")
    yes = (bid + ask) / 2 if bid is not None and ask is not None else m.get("last_price")
    return {"ticker": m.get("ticker"), "yes_pct": yes, "close_time": m.get("close_time")}


def paper_pnl(o):
    """Paper profit per 1-dollar contract if we had bought the called side at Kalshi's price
    when the call was locked, after Kalshi's taker fee 0.07*p*(1-p). None if no call or no price."""
    y = o.get("kalshi_yes")
    if o["call"] not in ("UP", "DOWN") or y is None or o["outcome"] not in ("UP", "DOWN"):
        return None
    y = y / 100.0
    cost = y if o["call"] == "UP" else 1 - y
    fee = 0.07 * y * (1 - y)
    return round((1.0 if o["call"] == o["outcome"] else 0.0) - cost - fee, 4)


# ---------- state ----------
def load(path, default):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return default


def save_atomic(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(obj, f)
    os.replace(tmp, path)


def weights():
    w = dict(WEIGHTS)
    w.update(load(os.path.join(DIR, "weights.json"), {}))
    return w


def read_calls():
    out = []
    try:
        with open(os.path.join(DIR, "calls.jsonl")) as f:
            for line in f:
                try:
                    out.append(json.loads(line))
                except Exception:
                    pass
    except FileNotFoundError:
        pass
    return out


def tally(calls):
    scored = [c for c in calls if c["call"] in ("UP", "DOWN") and c["outcome"] in ("UP", "DOWN")]
    right = sum(1 for c in scored if c["call"] == c["outcome"])
    pn = [c["pnl"] for c in calls if c.get("pnl") is not None]
    return {"calls": len(calls), "scored": len(scored), "right": right,
            "pct": round(100 * right / len(scored), 1) if scored else None,
            "pnl": round(sum(pn), 2) if pn else None, "pnl_n": len(pn)}


def scorecard(calls, now):
    lt = time.localtime(now)
    day0 = time.mktime((lt.tm_year, lt.tm_mon, lt.tm_mday, 0, 0, 0, 0, 0, -1))
    by = {}
    for c in calls:
        if c["outcome"] not in ("UP", "DOWN"):
            continue
        for k, s in (c.get("signals") or {}).items():
            if abs(s) >= 0.1:
                d = by.setdefault(k, {"n": 0, "right": 0})
                d["n"] += 1
                d["right"] += 1 if (s > 0) == (c["outcome"] == "UP") else 0
    for d in by.values():
        d["pct"] = round(100 * d["right"] / d["n"], 1)
    return {"today": tally([c for c in calls if c["start"] >= day0]),
            "week": tally([c for c in calls if c["start"] >= now - 7 * 86400]),
            "all": tally(calls), "by_signal": by}


# ---------- one cycle ----------
def run_cycle(now, S):
    """S = persistent state dict. Returns the market.json dict."""
    os.makedirs(DIR, exist_ok=True)
    cache = S.setdefault("cache", {})
    price = get_price()
    S.setdefault("history", []).append([now, price])
    S["history"] = [h for h in S["history"] if h[0] > now - 2400]
    hist = S["history"]

    def due(name):
        return now - cache.get(name + "_t", 0) >= EVERY[name]

    sigs = {}
    def run(key, fn, every=None):
        if every and not due(key):
            if key in cache.get("last", {}):
                sigs[key] = cache["last"][key]
            return
        try:
            s, d = fn()
            sigs[key] = {"score": round(s, 3), "detail": d, "ok": True}
        except Exception as e:
            sigs[key] = {"score": None, "detail": str(e)[:80], "ok": False}
        if every:
            cache[key + "_t"] = now
    run("book", lambda: sig_book(price))
    run("momentum", lambda: sig_momentum([tuple(h) for h in hist], now))
    run("whales", lambda: sig_whales(now), True)
    run("news", lambda: sig_news(now, cache), True)
    run("fng", sig_fng, True)
    run("funding", sig_funding, True)
    cache["last"] = {k: v for k, v in sigs.items() if k in EVERY}
    if due("kalshi"):
        try:
            cache["kalshi"] = get_kalshi()
        except Exception:
            cache["kalshi"] = None
        cache["kalshi_t"] = now

    w = weights()
    avail = {k: v for k, v in sigs.items() if v["ok"]}
    tw = sum(w[k] for k in avail)
    score = round(100 * sum(w[k] * v["score"] for k, v in avail.items()) / tw, 1) if tw else 0.0
    conf = round(tw / sum(w.values()), 2)
    lean = "UP" if score >= THRESHOLD else "DOWN" if score <= -THRESHOLD else "NONE"
    if conf < 0.4:
        lean = "NONE"  # too little data to lean on

    # ---- 15-minute windows ----
    win = now // WINDOW * WINDOW
    done = S.setdefault("done", [])
    for o in list(S.get("open", [])):
        if now >= o["start"] + WINDOW:
            S["open"].remove(o)
            if now - (o["start"] + WINDOW) <= 120:
                o["price1"] = price
                o["outcome"] = "UP" if price > o["price0"] else "DOWN" if price < o["price0"] else "FLAT"
                o["pnl"] = paper_pnl(o)
                with open(os.path.join(DIR, "calls.jsonl"), "a") as f:
                    f.write(json.dumps(o) + "\n")
    if not any(o["start"] == win for o in S.setdefault("open", [])) and win not in S.get("skipped", []) \
            and now - win <= 90 and win != S.get("last_win"):
        S["open"].append({"start": win, "price0": price, "score": score, "call": lean, "conf": conf,
                          "signals": {k: v["score"] for k, v in avail.items()}, "locked_at": now,
                          "kalshi_yes": (cache.get("kalshi") or {}).get("yes_pct")})
        S["last_win"] = win
    cur = next((o for o in S["open"] if o["start"] == win), None)

    if now - S.get("snap_t", 0) >= 60:
        S["snap_t"] = now
        with open(os.path.join(DIR, "snapshots.jsonl"), "a") as f:
            f.write(json.dumps({"t": now, "price": price, "score": score, "conf": conf,
                                "sig": {k: v["score"] for k, v in avail.items()},
                                "kalshi_yes": (cache.get("kalshi") or {}).get("yes_pct")}) + "\n")
    calls = read_calls()
    sc = scorecard(calls, now)
    recent = [{"start": c["start"], "call": c["call"], "outcome": c["outcome"], "price0": c["price0"],
               "price1": c["price1"], "score": c["score"]} for c in calls[-12:]][::-1]
    order = ["book", "momentum", "whales", "news", "fng", "funding"]
    return {
        "updated": now, "sample": False, "price": price,
        "live": {"score": score, "lean": lean, "confidence": conf},
        "call": ({"start": cur["start"], "end": cur["start"] + WINDOW, "call": cur["call"], "score": cur["score"],
                  "price0": cur["price0"], "locked_at": cur["locked_at"]} if cur else None),
        "next_window": win + WINDOW,
        "signals": [dict(key=k, label=LABELS[k], weight=w[k], **sigs[k]) for k in order if k in sigs],
        "kalshi": cache.get("kalshi"), "headlines": cache.get("headlines", []),
        "scorecard": sc, "recent": recent,
        "note": "Paper mode: no real money. Information only, not financial advice.",
    }


def main():
    os.makedirs(DIR, exist_ok=True)
    spath = os.path.join(DIR, "state.json")
    S = load(spath, {})
    me = os.path.abspath(__file__)
    mtime = os.path.getmtime(me)
    print("market agent started (paper mode)", flush=True)
    while True:
        now = int(time.time())
        try:
            save_atomic(OUT, run_cycle(now, S))
            save_atomic(spath, S)
        except Exception as e:
            print("cycle failed:", e, flush=True)
        time.sleep(CYCLE)
        if os.path.getmtime(me) != mtime:       # new version pulled from GitHub
            print("collector updated, restarting", flush=True)
            os.execv(sys.executable, [sys.executable, me])


if __name__ == "__main__":
    main()
