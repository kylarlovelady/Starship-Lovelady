#!/usr/bin/env python3
"""BTC 15-minute call engine. PAPER MODE ONLY: it reads public data, makes one
call per 15-minute window (UP / DOWN / NONE), scores itself, and writes
market.json for the Markets page. It never places orders and never touches
Kalshi accounts or keys. Standard library only."""
import json, math, os, re, sys, time, urllib.request
import threading
import xml.etree.ElementTree as ET
from http.server import BaseHTTPRequestHandler, HTTPServer
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
EVERY = {"whales": 60, "news": 300, "fng": 3600, "funding": 120, "kalshi": 20, "recent": 300}
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


def to_cents(m, *names):
    """Read a Kalshi price that may be whole cents (56), or dollars as text ("0.5600") or number."""
    for n in names:
        v = m.get(n)
        if v is None or v == "":
            continue
        try:
            x = float(v)
        except Exception:
            continue
        return x * 100 if ("dollars" in n or isinstance(v, str) and "." in v and x <= 1.0) else x
    return None


def get_kalshi():
    d = fetch_json("https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXBTC15M&status=open&limit=5")
    ms = sorted(d.get("markets", []), key=lambda m: m.get("close_time", ""))
    if not ms:
        raise ValueError("no open market")
    m = ms[0]
    try:                                   # keep one raw market so field names can be checked
        save_atomic(os.path.join(DIR, "kalshi_raw.json"), m)
    except Exception:
        pass
    bid = to_cents(m, "yes_bid", "yes_bid_dollars")
    ask = to_cents(m, "yes_ask", "yes_ask_dollars")
    last = to_cents(m, "last_price", "last_price_dollars")
    yes = (bid + ask) / 2 if bid is not None and ask is not None else last
    return {"ticker": m.get("ticker"), "yes_pct": yes, "yes_bid": bid, "yes_ask": ask, "close_time": m.get("close_time"),
            "strike": m.get("floor_strike") if m.get("floor_strike") is not None else m.get("cap_strike")}


def p_up_model(price, strike, secs_left, history, now):
    """Chance BTC finishes above the strike, from how far it is now, time left and recent choppiness
    (normal-distribution model). Near the start this is about 50 percent; late in the window it is
    close to 0 or 100, which is what Kalshi's own price shows too."""
    if not strike or secs_left <= 0:
        return None
    pts = [h for h in history if h[0] > now - 1800]
    rs = []
    for (t0, a), (t1, b) in zip(pts, pts[1:]):
        if t1 > t0:
            rs.append((math.log(b / a)) ** 2 / (t1 - t0))
    if len(rs) < 10:
        return None
    sig = math.sqrt(sum(rs) / len(rs)) * math.sqrt(secs_left)     # expected size of the move left
    if sig <= 0:
        return None
    z = math.log(price / float(strike)) / sig
    return round(0.5 * (1 + math.erf(z / math.sqrt(2))), 4)


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


def get_recent_markets():
    """Results of the last 10 finished Kalshi 15-minute markets, newest first (UP or DOWN)."""
    d = fetch_json("https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXBTC15M&status=settled&limit=10")
    ms = sorted(d.get("markets", []), key=lambda m: m.get("close_time", ""), reverse=True)
    out = ["UP" if m.get("result") == "yes" else "DOWN" for m in ms if m.get("result") in ("yes", "no")]
    if not out:
        raise ValueError("no settled markets")
    return out


def review(o):
    """Plain-English post-mortem of one finished call."""
    out, call, p0 = o["outcome"], o["call"], o["price0"]
    if out not in ("UP", "DOWN"):
        return None
    fin = (o["price1"] / p0 - 1) * 100
    hi, lo = (o.get("hi", p0) / p0 - 1) * 100, (o.get("lo", p0) / p0 - 1) * 100
    sig = o.get("signals") or {}
    agree = [LABELS[k] for k, v in sig.items() if abs(v) >= 0.1 and (v > 0) == (out == "UP")]
    against = [LABELS[k] for k, v in sig.items() if abs(v) >= 0.1 and (v > 0) != (out == "UP")]
    if call not in ("UP", "DOWN"):
        txt = "No lean. BTC went %s %+.2f%%. Signals that had it right: %s." % (out, fin, ", ".join(agree) or "none")
        return {"start": o["start"], "call": call, "outcome": out, "won": None, "text": txt}
    won = call == out
    fav = hi if call == "UP" else -lo               # best move our way during the window
    ours = fin if call == "UP" else -fin             # where it finished, our way
    if won:
        txt = "Won. Backed by: %s." % (", ".join(agree) or "none")
        if against:
            txt += " Pointed the other way: %s." % ", ".join(against)
        if fav - ours > 0.1:
            txt += " Price went %+.2f%% our way at the best point but finished at %+.2f%%, so selling earlier would have won more." % (fav, ours)
        else:
            txt += " It finished near its best point, so holding was right."
    else:
        txt = "Lost. Signals that had it right but were outvoted: %s." % (", ".join(agree) or "none")
        txt += " Signals that misled it: %s." % (", ".join(against) or "none")
        if not agree:
            txt += " Every signal leaned the wrong way, so either bad luck or an input is missing."
        if fav > 0.1:
            txt += " Price first went %+.2f%% our way, so an earlier exit would have cut the loss." % fav
    return {"start": o["start"], "call": call, "outcome": out, "won": won, "text": txt}


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


def read_tail(name, n):
    out = []
    try:
        with open(os.path.join(DIR, name)) as f:
            for line in f.readlines()[-n:]:
                try:
                    out.append(json.loads(line))
                except Exception:
                    pass
    except FileNotFoundError:
        pass
    return out


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
    if due("recent"):
        try:
            cache["recent_markets"] = get_recent_markets()
        except Exception:
            cache["recent_markets"] = None
        cache["recent_t"] = now
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

    for o in S.get("open", []):
        o["hi"] = max(o.get("hi", o["price0"]), price)
        o["lo"] = min(o.get("lo", o["price0"]), price)

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
                rv = review(o)
                if rv:
                    with open(os.path.join(DIR, "reviews.jsonl"), "a") as f:
                        f.write(json.dumps(rv) + "\n")
                with open(os.path.join(DIR, "calls.jsonl"), "a") as f:
                    f.write(json.dumps(o) + "\n")
    if not any(o["start"] == win for o in S.setdefault("open", [])) and win not in S.get("skipped", []) \
            and now - win <= 90 and win != S.get("last_win"):
        S["open"].append({"start": win, "price0": price, "score": score, "call": lean, "conf": conf,
                          "signals": {k: v["score"] for k, v in avail.items()}, "locked_at": now,
                          "kalshi_yes": (cache.get("kalshi") or {}).get("yes_pct"), "strike": (cache.get("kalshi") or {}).get("strike")})
        S["last_win"] = win
    cur = next((o for o in S["open"] if o["start"] == win), None)

    k = cache.get("kalshi") or {}
    pm = p_up_model(price, k.get("strike"), win + WINDOW - now, hist, now)
    simout = None
    try:
        import sim as _sim
        simout = _sim.step(S, now, win, WINDOW, price, k.get("strike"), pm, cache.get("kalshi"), sigs, score,
                           load(os.path.join(DIR, "control.json"), {"on": True}).get("on", True), DIR)
    except Exception as e:
        simout = {"error": str(e)[:100]}
    if now - S.get("snap_t", 0) >= 60:
        S["snap_t"] = now
        with open(os.path.join(DIR, "snapshots.jsonl"), "a") as f:
            f.write(json.dumps({"t": now, "price": price, "score": score, "conf": conf,
                                "sig": {k: v["score"] for k, v in avail.items()},
                                "kalshi_yes": (cache.get("kalshi") or {}).get("yes_pct"),
                                "yes_bid": (cache.get("kalshi") or {}).get("yes_bid"),
                                "yes_ask": (cache.get("kalshi") or {}).get("yes_ask"),
                                "strike": k.get("strike"), "p_model": pm, "secs_left": win + WINDOW - now,
                                "recent_up": (cache.get("recent_markets") or []).count("UP") if cache.get("recent_markets") else None}) + "\n")
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
        "kalshi": cache.get("kalshi"), "p_model": pm, "sim": simout, "headlines": cache.get("headlines", []),
        "scorecard": sc, "recent": recent,
        "lessons": read_tail("reviews.jsonl", 6)[::-1], "learning": load(os.path.join(DIR, "learn_report.json"), None),
        "recent_markets": cache.get("recent_markets"), "weights": w,
        "note": "Paper mode: no real money. Information only, not financial advice.",
    }


class Control(BaseHTTPRequestHandler):
    """Tiny on/off switch for the simulator, reachable only on the Tailscale address."""
    def _send(self, obj, code=200):
        b = json.dumps(obj).encode()
        self.send_response(code)
        for h, v in (("Content-Type", "application/json"), ("Access-Control-Allow-Origin", "*"),
                     ("Access-Control-Allow-Headers", "content-type"), ("Content-Length", str(len(b)))):
            self.send_header(h, v)
        self.end_headers(); self.wfile.write(b)

    def do_OPTIONS(self):
        self._send({})

    def do_GET(self):
        self._send(load(os.path.join(DIR, "control.json"), {"on": True}))

    def do_POST(self):
        try:
            n = int(self.headers.get("Content-Length", 0))
            on = bool(json.loads(self.rfile.read(n) or b"{}").get("on"))
            save_atomic(os.path.join(DIR, "control.json"), {"on": on, "changed": int(time.time())})
            self._send({"on": on})
        except Exception:
            self._send({"error": "bad request"}, 400)

    def log_message(self, *a):
        pass


def start_control():
    try:
        srv = HTTPServer((os.environ.get("MARKET_BIND", "127.0.0.1"), int(os.environ.get("MARKET_PORT", "8097"))), Control)
        threading.Thread(target=srv.serve_forever, daemon=True).start()
    except Exception as e:
        print("control server not started:", e, flush=True)


def main():
    os.makedirs(DIR, exist_ok=True)
    spath = os.path.join(DIR, "state.json")
    S = load(spath, {})
    me = os.path.abspath(__file__)
    mtime = os.path.getmtime(me)
    start_control()
    print("market agent started (paper mode)", flush=True)
    while True:
        now = int(time.time())
        try:
            save_atomic(OUT, run_cycle(now, S))
            save_atomic(spath, S)
            lt = time.localtime(now)
            if lt.tm_hour == 4 and S.get("learn_day") != lt.tm_yday:   # nightly at 4 AM local time
                S["learn_day"] = lt.tm_yday
                sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
                import learner
                learner.learn(DIR, weights(), now)
        except Exception as e:
            print("cycle failed:", e, flush=True)
        time.sleep(CYCLE)
        if os.path.getmtime(me) != mtime:       # new version pulled from GitHub
            print("collector updated, restarting", flush=True)
            os.execv(sys.executable, [sys.executable, me])


if __name__ == "__main__":
    main()
