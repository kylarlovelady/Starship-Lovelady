#!/usr/bin/env python3
# v8.5 restart: new practice-only reaction test v_snipe (one late favourite buy in the last 2 minutes, up to 97c, hold to end); ENTRY_MAX and MAX_PRICE can now be overridden per test (restart marker)
"""BTC 15-minute call engine. PAPER MODE ONLY: it reads public data, makes one
call per 15-minute window (UP / DOWN / NONE), scores itself, and writes
market.json for the Markets page. It never places orders and never touches
Kalshi accounts or keys. Standard library only."""
import calendar, json, math, os, re, sys, time, urllib.request
import threading
import xml.etree.ElementTree as ET
from http.server import BaseHTTPRequestHandler, HTTPServer
from email.utils import parsedate_to_datetime

HOME = os.path.expanduser("~")
DIR = os.environ.get("MARKET_DIR", os.path.join(HOME, "market-data"))
OUT = os.environ.get("MARKET_OUT", os.path.join(HOME, "crew-web", "market.json"))
WINDOW = 900            # 15 minutes
CYCLE = 5               # seconds between looks (numbers move fast)
THRESHOLD = 12          # |score| needed to lean; below that the call is NONE
WEIGHTS = {"book": 0.20, "momentum": 0.15, "whales": 0.15, "bigtrades": 0.11, "news": 0.08, "fng": 0.04, "funding": 0.03,
           "trend_h": 0.0, "trend_w": 0.0, "levels": 0.06,
           "trend_1h": 0.04, "trend_4h": 0.03, "trend_24h": 0.04, "trend_7d": 0.03}   # trend_h / trend_w are the old lumped blends: still shown and graded, no weight
LABELS = {"book": "Order book", "momentum": "Price momentum", "whales": "Whale moves",
          "bigtrades": "Big exchange trades", "news": "News vibe", "fng": "Fear & Greed", "funding": "Funding rate",
          "trend_h": "Hourly and daily trend", "trend_w": "Weekly and monthly trend", "levels": "Support and resistance",
          "trend_1h": "Trend, 1 hour", "trend_4h": "Trend, 4 hours", "trend_24h": "Trend, 24 hours", "trend_7d": "Trend, 7 days"}
EVERY = {"candles": 120, "whales": 60, "bigtrades": 20, "news": 300, "fng": 3600, "funding": 120, "kalshi": 5, "recent": 300, "xcheck": 30}
FEEDS = ["https://www.coindesk.com/arc/outboundfeeds/rss/", "https://cointelegraph.com/rss",
         "https://decrypt.co/feed", "https://bitcoinmagazine.com/.rss/full/"]
BULL = ["surge", "rally", "soar", "jump", "record high", "all-time high", "approve", "approval",
        "inflow", "adoption", "accumulat", "bullish", "breakout", "gains", "rises", "climb",
        "upgrade", "partnership", "buys", "buying", "rebound", "recover"]
BEAR = ["crash", "plunge", "drop", "falls", "slump", "hack", "exploit", "ban", "lawsuit", "sues",
        "outflow", "sell-off", "selloff", "liquidat", "bearish", "fear", "dump", "warning",
        "probe", "fraud", "arrest", "bankrupt", "tumble", "sinks", "rejects", "delay"]


# ---------- fetching (monkeypatched in tests) ----------
BROWSER_UA = "Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"


def fetch(url, timeout=10, ua=None):
    req = urllib.request.Request(url, headers={"User-Agent": ua or "starship-market-agent/1.0"})
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


def get_candles():
    """Hourly (last ~12 days) and daily (last ~90 days) BTC candles, oldest first: [time, low, high, open, close]."""
    out = {}
    for name, gran in (("h", 3600), ("d", 86400)):
        try:
            rows = fetch_json("https://api.exchange.coinbase.com/products/BTC-USD/candles?granularity=%d" % gran)
        except Exception:
            rows = fetch_json("https://api.kraken.com/0/public/OHLC?pair=XBTUSD&interval=%d" % (60 if gran == 3600 else 1440))
            rows = [[r[0], float(r[3]), float(r[2]), float(r[1]), float(r[4])] for r in list(rows["result"].values())[0]]
            out[name] = rows[-300:]
            continue
        out[name] = sorted([[r[0], float(r[1]), float(r[2]), float(r[3]), float(r[4])] for r in rows])
    return out


def _sd(xs):
    if len(xs) < 3:
        return None
    m = sum(xs) / len(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


def _pc(x):
    return "%+.1f%%" % (100 * x)


def trend_signals(cd, price):
    """Reads the chart the way a trader does: the trend on several time scales, then support and resistance.
    Returns {name: (score -1..1, plain-English detail)}. The learner decides afterwards which of these actually work."""
    h, d = cd.get("h") or [], cd.get("d") or []
    out = {}
    if len(h) >= 30:
        cl = [c[4] for c in h]
        sh = _sd([math.log(b / a) for a, b in zip(cl, cl[1:])][-72:]) or 0.004
        def ret(n):
            return price / cl[-1 - n] - 1 if len(cl) > n else None
        r1, r4, r24 = ret(1), ret(4), ret(24)
        z = lambda r, hrs: math.tanh((r / (sh * math.sqrt(hrs))) / 1.5)
        sc = 0.4 * z(r1, 1) + 0.3 * z(r4, 4) + 0.3 * z(r24, 24)
        sma24 = sum(cl[-24:]) / 24
        sc = clamp(sc + (0.15 if price > sma24 else -0.15))
        kind = "up on every time scale" if min(r1, r4, r24) > 0 else "down on every time scale" if max(r1, r4, r24) < 0 else \
            ("short-term bounce inside a bigger down-move" if r1 > 0 and r24 < 0 else "short-term dip inside a bigger up-move" if r1 < 0 and r24 > 0 else "mixed")
        out["trend_1h"] = (clamp(z(r1, 1)), "1 hour %s" % _pc(r1))
        out["trend_4h"] = (clamp(z(r4, 4)), "4 hours %s" % _pc(r4))
        out["trend_24h"] = (clamp(z(r24, 24)), "24 hours %s" % _pc(r24))
        out["trend_h"] = (sc, "1 hour %s, 4 hours %s, 24 hours %s, %s its 24-hour average: %s" % (_pc(r1), _pc(r4), _pc(r24), "above" if price > sma24 else "below", kind))
    if len(d) >= 31 and len(h) >= 168:
        cl = [c[4] for c in d]
        sd_ = _sd([math.log(b / a) for a, b in zip(cl, cl[1:])][-60:]) or 0.025
        r7 = price / cl[-7] - 1
        r30 = price / cl[-30] - 1
        hc = [c[4] for c in h]
        sma7 = sum(hc[-168:]) / 168
        sc = 0.4 * math.tanh(r7 / (sd_ * math.sqrt(7)) / 1.5) + 0.4 * math.tanh(r30 / (sd_ * math.sqrt(30)) / 1.5) + (0.2 if price > sma7 else -0.2)
        out["trend_7d"] = (clamp(math.tanh(r7 / (sd_ * math.sqrt(7)) / 1.5)), "7 days %s" % _pc(r7))
        out["trend_w"] = (clamp(sc), "7 days %s, 30 days %s, %s its 7-day average" % (_pc(r7), _pc(r30), "above" if price > sma7 else "below"))
    if len(h) >= 48:
        win_ = h[-72:]
        atr = sum(c[2] - c[1] for c in win_[-24:]) / 24 or price * 0.003
        sup, res = [], []
        for i in range(3, len(win_) - 3):
            lo, hi = win_[i][1], win_[i][2]
            if lo == min(c[1] for c in win_[i - 3:i + 4]):
                sup.append(lo)
            if hi == max(c[2] for c in win_[i - 3:i + 4]):
                res.append(hi)
        below = [x for x in sup if x < price]
        above = [x for x in res if x > price]
        s_ = max(below) if below else min(c[1] for c in win_)
        r_ = min(above) if above else max(c[2] for c in win_)
        ds, dr = (price - s_) / atr, (r_ - price) / atr
        sc = (1 - min(ds, 1.5) / 1.5) - (1 - min(dr, 1.5) / 1.5)             # near support pushes up, near resistance pushes down
        prior = win_[-25:-1]
        note = ""
        if price > max(c[2] for c in prior):
            sc, note = max(sc, 0) + 0.6, " Breakout above the last 24 hours' high."
        elif price < min(c[1] for c in prior):
            sc, note = min(sc, 0) - 0.6, " Breakdown below the last 24 hours' low."
        out["levels"] = (clamp(sc * 0.8), "Support near $%s (%.1f hourly ranges below), resistance near $%s (%.1f above).%s" % (
            format(s_, ",.0f"), ds, format(r_, ",.0f"), dr, note))
    return out


EXCHANGES = ("binance", "coinbase", "kraken", "bitfinex", "okx", "okex", "bybit", "huobi", "htx", "kucoin", "gemini", "bitstamp",
             "crypto.com", "bitget", "gate.io", "mexc", "upbit", "bithumb", "deribit", "robinhood", "bitflyer", "poloniex", "bitmex", "bullish", "bitso")


def parse_whale_page(html_text, now, window=7200, half=2700):
    """Whale Alert's public Telegram page: big BTC transfers with who sent and who received.
    Money moving ONTO an exchange leans bearish (about to sell); OFF an exchange leans bullish (being held)."""
    import html as _h
    inflow = outflow = 0.0
    n_in = n_out = 0
    for blk in html_text.split("tgme_widget_message_wrap")[1:]:
        m = re.search(r'<time[^>]*datetime="([^"]+)"', blk)
        tx = re.search(r'tgme_widget_message_text[^>]*>(.*?)</div>', blk, re.S)
        if not m or not tx:
            continue
        try:
            ts = parsedate_iso(m.group(1))
        except Exception:
            continue
        if now - ts > window or ts > now + 60:
            continue
        text = _h.unescape(re.sub(r"<[^>]+>", " ", tx.group(1)))
        text = re.sub(r"\s+", " ", text)
        mm = re.search(r"([\d,\.]+)\s*[#$]?BTC\s*\(([\d,]+)\s*USD\)\s*transferred from\s+(.+?)\s+to\s+(.+?)\s*(?:Details|$)", text)
        if not mm:
            continue
        usd = float(mm.group(2).replace(",", "")) * (0.5 ** ((now - ts) / half))
        fo, to = mm.group(3).lower(), mm.group(4).lower()
        fo_ex = any(x in fo for x in EXCHANGES)
        to_ex = any(x in to for x in EXCHANGES)
        if to_ex and not fo_ex:
            inflow += usd; n_in += 1
        elif fo_ex and not to_ex:
            outflow += usd; n_out += 1
    return inflow, outflow, n_in, n_out


def parsedate_iso(s):
    import calendar
    s = s.strip()
    off = 0
    mo = re.search(r"([+-])(\d\d):(\d\d)$", s)
    if mo:
        off = (1 if mo.group(1) == "+" else -1) * (int(mo.group(2)) * 3600 + int(mo.group(3)) * 60)
        s = s[:mo.start()]
    s = s.replace("Z", "")[:19]
    return calendar.timegm(time.strptime(s, "%Y-%m-%dT%H:%M:%S")) - off


def sig_whales(now):
    """Free: Whale Alert's public Telegram page (no key). Confirmed big BTC transfers, shortly after they land."""
    body = fetch("https://t.me/s/whale_alert_io", 10, BROWSER_UA)
    inflow, outflow, n_in, n_out = parse_whale_page(body, now)
    net = outflow - inflow
    detail = "last 2 hours (recent counts more): $%.0fM moved onto exchanges (%d), $%.0fM off (%d)" % (inflow / 1e6, n_in, outflow / 1e6, n_out)
    if n_in + n_out == 0:
        detail = "no big BTC transfers to or from exchanges in the last 2 hours"
    return clamp(math.tanh(net / 50e6)), detail


def sig_bigtrades(now):
    """Free: Coinlobster's public feed of very large BTC trades on exchanges, with buy or sell on each."""
    d = json.loads(fetch("https://coinlobster.com/api/public/crypto-whales", 10, BROWSER_UA))
    buy = sell = 0.0
    nb = ns = 0
    for t in d.get("whales", []):
        if not str(t.get("pair", "")).upper().startswith("BTC/"):
            continue
        ts = t.get("timestamp", 0) / 1000.0
        if now - ts > 10800 or ts > now + 60:        # the feed runs about 1.5 hours behind, so look back 3 hours
            continue
        q = float(t.get("quantity_quote") or 0) * (0.5 ** ((now - ts) / 2700.0))
        if t.get("isBuy"):
            buy += q; nb += 1
        else:
            sell += q; ns += 1
    net = buy - sell
    if nb + ns == 0:
        return 0.0, "no giant BTC trades in the last 3 hours"
    return clamp(math.tanh(net / 5e6)), "last 3 hours (recent counts more): $%.1fM of giant buys (%d), $%.1fM of giant sells (%d)" % (buy / 1e6, nb, sell / 1e6, ns)


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


def _num(v):
    try:
        return float(v)
    except Exception:
        return None


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
    qsrc, list_q, bsz, asz = "list", (bid, ask), _num(m.get("yes_bid_size_fp")), _num(m.get("yes_ask_size_fp"))
    try:                                   # the market list can lag by many cents: take the live order book instead
        d2 = fetch_json("https://api.elections.kalshi.com/trade-api/v2/markets/%s/orderbook?depth=1" % m.get("ticker"), 5)
        ob = d2.get("orderbook") or d2.get("orderbook_fp") or d2
        def _best(side):
            lv = ob.get(side + "_dollars") or ob.get(side)
            if not lv:
                return None
            row = max(lv, key=lambda x: float(x[0]))
            p_ = float(row[0]); p_ = p_ * 100 if p_ <= 1.0 else p_
            return p_, _num(row[1])
        yb, nb = _best("yes"), _best("no")
        if yb and nb:
            bid, ask, bsz, asz = yb[0], 100.0 - nb[0], yb[1], nb[1]
            qsrc = "book"
    except Exception:
        pass
    yes = (bid + ask) / 2 if bid is not None and ask is not None else last
    return {"ticker": m.get("ticker"), "yes_pct": yes, "yes_bid": bid, "yes_ask": ask, "close_time": m.get("close_time"), "close_ep": close_epoch(m),
            "yes_ask_size": asz, "yes_bid_size": bsz, "qsrc": qsrc, "list_bid": list_q[0], "list_ask": list_q[1],
            "strike": m.get("floor_strike") if m.get("floor_strike") is not None else m.get("cap_strike")}


def close_epoch(m):
    """Kalshi close_time like 2026-11-02T18:45:00Z as epoch seconds."""
    try:
        return calendar.timegm(time.strptime((m.get("close_time") or "")[:19], "%Y-%m-%dT%H:%M:%S"))
    except Exception:
        return None


def get_result(ticker):
    """Kalshi's official result for a finished market: UP, DOWN, or None if not posted yet."""
    try:
        d = fetch_json("https://api.elections.kalshi.com/trade-api/v2/markets/" + ticker)
        m = d.get("market", d)
        r = m.get("result")
        return "UP" if r == "yes" else "DOWN" if r == "no" else None
    except Exception:
        return None


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


DEFAULTS = {"threshold": THRESHOLD, "aggression": 30.0, "floor": 0.0, "min_bet": 0.0, "cap": 100.0, "edge_min": 0.03, "max_trades": 6, "slice": 0.10, "min_price": 0.08, "max_price": 0.92, "entry_max": 0.80, "entry_min": 0.15, "stage_first": 0.40, "stage_gap": 45, "exit_on": 1, "exit_peak": 8, "exit_drop": 4, "unproven_cap": 25.0}
LIMITS = {"threshold": (0, 50), "aggression": (0, 100), "floor": (0, 1000000), "min_bet": (0, 100), "cap": (0, 100000), "edge_min": (0, 0.3), "max_trades": (1, 20), "slice": (0.01, 0.5), "min_price": (0.01, 0.4), "max_price": (0.6, 0.99), "entry_max": (0.5, 0.99), "entry_min": (0.0, 0.5), "stage_first": (0.1, 1.0), "stage_gap": (0, 300), "exit_on": (0, 1), "exit_peak": (1, 50), "exit_drop": (1, 30), "unproven_cap": (0, 100000)}


def clean_cfg(raw):
    """Keep only known settings, as numbers, inside safe ranges."""
    out = {}
    for k, (lo, hi) in LIMITS.items():
        if k in raw:
            try:
                out[k] = min(hi, max(lo, float(raw[k])))
            except Exception:
                pass
    if isinstance(raw.get("weights"), dict):
        w = {}
        for k in WEIGHTS:
            try:
                if k in raw["weights"]:
                    w[k] = min(1.0, max(0.0, float(raw["weights"][k])))
            except Exception:
                pass
        out["weights"] = w
    return out


def cfg():
    c = dict(DEFAULTS)
    c.update({k: v for k, v in clean_cfg(load(os.path.join(DIR, "config.json"), {})).items() if k != "weights"})
    c["max_trades"] = int(c["max_trades"])
    if c["cap"] > 0:                       # 0 means no limit
        c["cap"] = max(c["cap"], c["min_bet"], 1.0)
    c["weights"] = weights()
    try:                                                   # response_learn.py: loss-cut level that beat plain holding in BOTH halves (else default)
        lr = load(os.path.join(DIR, "learned_response.json"), {})
        if "stop_pct" in lr and "stop_pct" not in clean_cfg(load(os.path.join(DIR, "config.json"), {})):
            c["stop_pct"] = min(0.8, max(0.15, float(lr["stop_pct"])))
    except Exception:
        pass
    return c


def weights():
    w = dict(WEIGHTS)
    w.update(load(os.path.join(DIR, "weights.json"), {}))                       # what the nightly learner chose
    try:                                                                       # Kylar's ratings x evidence from grades.py (separate, never lumped)
        sw = load(os.path.join(DIR, "signal_weights.json"), {}).get("signals", {})
        mp = {"momentum": "bmom60", "book": "bookimb", "whales": "a_whales", "bigtrades": "a_bigtrades", "news": "a_news", "fng": "a_fng", "funding": "funding",
              "levels": "a_levels", "trend_1h": "hr", "trend_4h": "tr4h", "trend_24h": "tr24h", "trend_7d": "tr7d"}
        new = {k: float(sw[g]["weight"]) for k, g in mp.items() if g in sw and sw[g].get("weight") is not None and k in w}
        if len(new) >= 6:
            mass, tot = sum(w[k] for k in new), sum(new.values()) or 1.0
            for k, v in new.items():
                w[k] = mass * v / tot
    except Exception as e:
        print("signal_weights not applied:", e, flush=True)
    w.update(clean_cfg(load(os.path.join(DIR, "config.json"), {})).get("weights", {}))   # Kylar's edits win
    t = sum(w.values()) or 1.0
    return {k: v / t for k, v in w.items()}


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


_LABC = {}


def lab_view():
    """What the strategy lab and response learner have been trying (read-only files written by lab.py / response_learn.py), for the Live view."""
    try:
        st = load(os.path.join(DIR, "lab_state.json"), None)
        gr = []
        try:
            for k_, v_ in ((load(os.path.join(DIR, "signal_weights.json"), {}) or {}).get("signals") or {}).items():
                b_ = v_.get("best") or {}
                gr.append({"label": v_.get("label") or k_, "rating": v_.get("rating"), "grade": v_.get("grade"), "weight": v_.get("weight"), "dir": b_.get("direction"), "older": b_.get("older"), "newer": b_.get("newer")})
        except Exception:
            gr = []
        if not st:
            return {"grades": gr, "final": [], "promoted": [], "response": [], "innov": []} if gr else None
        p = os.path.join(DIR, "lab_log.jsonl")
        try:
            sz = os.path.getsize(p)
        except OSError:
            sz = 0
        if _LABC.get("sz") != sz:
            try:
                with open(p, "rb") as fh:
                    _LABC["n"] = sum(1 for _ in fh)
            except OSError:
                _LABC["n"] = 0
            _LABC["sz"] = sz
        innov = []
        try:
            with open(os.path.join(DIR, "innovations.jsonl")) as fh:
                innov = [{"t": x.get("t"), "msg": x.get("msg"), "action": x.get("action")} for x in (json.loads(l) for l in fh.readlines()[-40:]) if x.get("action") in ("new", "retire")][-6:]
        except (OSError, ValueError):
            pass
        resp = []
        try:
            with open(os.path.join(DIR, "response_log.jsonl")) as fh:
                resp = [json.loads(x) for x in fh.readlines()[-3:]]
        except (OSError, ValueError):
            pass
        return {"grades": gr, "made": st.get("made"), "rounds": st.get("rounds"), "tried_run": st.get("tried"), "tried_total": _LABC.get("n", 0), "marginals": st.get("marginals"),
                "final": [{"rule": f.get("rule"), "train": f.get("train"), "test": f.get("test")} for f in [x for i, x in enumerate(st.get("final") or []) if x.get("rule") not in [y.get("rule") for y in (st.get("final") or [])[:i]]][:5]],
                "promoted": (load(os.path.join(DIR, "lab_promoted.json"), {}) or {}).get("rules", []), "innov": innov, "response": [{"t": r.get("t"), "msg": r.get("msg")} for r in resp]}
    except Exception:
        return None


def learn_health(cache, now):
    """How many of the last 24 hours' rounds actually became lessons (Kalshi-settled), so a quiet gap in learning is visible."""
    h = cache.get("lh")
    if h and now - h["t"] < 60:
        return h
    cut = now - 86400
    calls = [c for c in read_calls() if (c.get("start") or 0) >= cut]
    k = sum(1 for c in calls if c.get("src") == "kalshi")
    h = {"t": int(now), "kalshi": k, "estimated": len(calls) - k, "expected": min(96, int((now - (cache.get("first_t") or now)) // 900) + 1) if False else 96}
    cache["lh"] = h
    return h


def tally(calls):
    scored = [c for c in calls if c["call"] in ("UP", "DOWN") and c["outcome"] in ("UP", "DOWN") and c.get("src") == "kalshi"]
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


# ---------- live (real money) ----------
_BROKER = {"obj": None, "err": None}


def alert(msg, title="Market agent"):
    try:
        import alerts
        alerts.send(msg, title)
    except Exception:
        pass


def get_broker():
    """One shared broker for the real Kalshi account. None if the key or settings are missing."""
    if _BROKER["obj"] is None:
        try:
            import kalshi_trade as kt
            _BROKER["obj"] = kt.Broker(kt.Kalshi(), DIR)
            _BROKER["err"] = None
        except BaseException as e:                      # SystemExit from a missing key, or any import problem
            _BROKER["err"] = str(e)[:120]
            return None
    return _BROKER["obj"]


def live_tick(sim_mod):
    """Called every cycle: connect the wallet to the real broker while a live run exists, and honour the kill switch."""
    rc = load(os.path.join(DIR, "run.json"), {})
    kp = os.path.join(DIR, "kill.json")
    if os.path.exists(kp):
        b = get_broker()
        if b:
            print("KILL: cancelling every resting order:", b.cancel_all(), flush=True)
        try:
            os.remove(kp)
        except OSError:
            pass
    if rc.get("live"):
        b = get_broker()
        if b is None and rc.get("active"):
            sim_mod.save_run_off(DIR, "live_error", "Could not connect to Kalshi: %s" % _BROKER["err"])
        sim_mod.BROKER = b
    else:
        sim_mod.BROKER = None


# ---------- reset ----------
def do_reset(S, now):
    """Start over: archive everything it learned or earned (nothing is deleted), clear the wallet, the six
    practice accounts, the scorecard and the learner's weights. Your Settings and the price history stay."""
    import glob, shutil
    arch = os.path.join(DIR, "archive", time.strftime("%Y%m%d-%H%M%S", time.localtime(now)))
    os.makedirs(arch, exist_ok=True)
    for p in glob.glob(os.path.join(DIR, "*.jsonl")) + [os.path.join(DIR, n) for n in ("learn_report.json", "weights.json", "learn_state.json")]:
        if os.path.exists(p):
            shutil.move(p, os.path.join(arch, os.path.basename(p)))
    old = (S.get("sim") or {}).get("run") or {}
    for k in ("sim", "open", "done", "last_win", "skipped", "audit", "tg", "path", "learn_day", "report_t"):
        S.pop(k, None)
    S["score_ver"] = 2
    rp = os.path.join(DIR, "run.json")
    if old.get("status") == "running":                    # a run was going: begin a fresh $1,000 one right away
        save_atomic(rp, {"active": True, "id": int(now), "strategy": old.get("strategy", "auto"), "start": 1000.0})
    else:
        save_atomic(rp, {"active": False})
    print("reset done, old data archived in", arch, flush=True)


# ---------- self-check against Kalshi ----------
def avg60(hist, t_end):
    """Average of our price over the 60 seconds before t_end (Kalshi settles on a 60-second average)."""
    xs = [p for t, p in hist if t_end - 60 < t <= t_end]
    return sum(xs) / len(xs) if len(xs) >= 3 else None


def audit(S, now, win, sync, kal, hist):
    """At the start of every round: compare Kalshi's target with our own price average and learn the gap.
    At the end: compare our estimate of the result with Kalshi's official one. The gap is added to our
    price so numbers on screen stay close to Kalshi's."""
    A = S.setdefault("audit", {"offset": 0.0, "n": 0, "cur": None, "wait": [], "list": []})
    A.setdefault("wait", [])
    cur = A.get("cur")
    if cur and now >= cur["win"] + WINDOW:                                # END of a round: make our own call first
        ref = avg60(hist, cur["win"] + WINDOW)
        cur["est_final"] = None if ref is None else round(ref + cur["off_used"], 2)
        A["wait"].append(cur); A["cur"] = cur = None
    for w in list(A["wait"]):                                             # then compare with Kalshi's official result
        end = w["win"] + WINDOW
        res = get_result(w["ticker"]) if w.get("ticker") else None
        if res is not None or now - end >= 150:
            est = None if w["est_final"] is None else ("UP" if w["est_final"] > w["strike"] else "DOWN")
            w.update({"result": res, "est_result": est, "match": (est == res) if (est and res) else None,
                      "margin": None if w["est_final"] is None else round(w["est_final"] - w["strike"], 2)})
            A["list"] = (A["list"] + [w])[-60:]
            A["wait"].remove(w)
    if sync and kal and kal.get("strike") is not None:
        if cur is None or cur["win"] != win:                              # START of a round
            ref = avg60(hist, win)
            if ref is None:
                ref = avg60(hist, now)
            if ref is not None:
                obs = float(kal["strike"]) - ref
                used = A["offset"]
                A["offset"] = round(obs if A["n"] == 0 else 0.7 * A["offset"] + 0.3 * obs, 2)
                A["n"] += 1
                A["cur"] = {"win": win, "ticker": kal.get("ticker"), "strike": float(kal["strike"]), "our_ref": round(ref, 2),
                            "gap": round(obs, 2), "off_used": used,
                            "target_ok": bool(kal.get("close_ep") and abs(kal["close_ep"] - (win + WINDOW)) <= 5)}
        S.setdefault("tg", {})[str(win)] = float(kal["strike"])
        for kx in sorted(S["tg"])[:-8]:
            del S["tg"][kx]


def xcheck(S, cache, now, price):
    """Cross-check our price against a second exchange. If they disagree a lot, do not trade on it."""
    if now - cache.get("xcheck_t", 0) < EVERY["xcheck"]:
        return
    cache["xcheck_t"] = now
    try:
        d = fetch_json("https://api.kraken.com/0/public/Ticker?pair=XBTUSD")["result"]
        other = float(list(d.values())[0]["c"][0])
        diff = (price / other - 1) * 100
        cache["xc"] = {"t": now, "diff_pct": round(diff, 3), "other": round(other, 2), "ok": abs(diff) < 0.3}
    except Exception:
        cache["xc"] = {"t": now, "diff_pct": None, "ok": True, "note": "second exchange unreachable"}


def data_checks(S, cache, now, sync, k, price):
    xc = cache.get("xc") or {}
    out = []
    out.append({"name": "Kalshi data is for this exact round", "ok": bool(sync),
                "note": "target and close time match" if sync else "waiting for Kalshi's market for this round"})
    spread = None
    if k and k.get("yes_bid") is not None and k.get("yes_ask") is not None:
        spread = k["yes_ask"] - k["yes_bid"]
    out.append({"name": "Kalshi prices make sense", "ok": spread is None or (0 <= spread <= 20),
                "note": "buy-sell gap %s cents" % ("%.0f" % spread if spread is not None else "unknown")})
    out.append({"name": "Our price agrees with a second exchange", "ok": bool(xc.get("ok", True)),
                "note": ("differs by %.2f%%" % xc["diff_pct"]) if xc.get("diff_pct") is not None else "not checked yet"})
    age = now - cache.get("kalshi_t", 0)
    out.append({"name": "Kalshi looked at in the last 15 seconds", "ok": age <= 15, "note": "%d seconds ago" % age})
    return out


def audit_out(S):
    A = S.get("audit") or {}
    L = A.get("list", [])
    ch = [x for x in L if x.get("match") is not None]
    cur = A.get("cur")
    return {"offset": A.get("offset", 0.0), "rounds": A.get("n", 0), "checked": len(ch),
            "match_pct": round(100 * sum(1 for x in ch if x["match"]) / len(ch)) if ch else None,
            "avg_gap": round(sum(abs(x["gap"]) for x in L) / len(L), 2) if L else None,
            "cur": ({k: cur[k] for k in ("win", "ticker", "strike", "our_ref", "gap", "target_ok")} if cur else None),
            "last": [{k: x.get(k) for k in ("win", "strike", "gap", "est_final", "margin", "est_result", "result", "match")} for x in L[-6:]][::-1]}


# ---------- one cycle ----------
def run_cycle(now, S):
    """S = persistent state dict. Returns the market.json dict."""
    os.makedirs(DIR, exist_ok=True)
    cache = S.setdefault("cache", {})
    rs = load(os.path.join(DIR, "reset.json"), {})
    if rs.get("id") and rs["id"] != S.get("reset_id"):
        S["reset_id"] = rs["id"]
        do_reset(S, now)
    price = get_price()
    xcheck(S, cache, now, price)
    S.setdefault("history", []).append([now, price])
    S["history"] = [h for h in S["history"] if h[0] > now - 3900]
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
    run("bigtrades", lambda: sig_bigtrades(now), True)
    run("news", lambda: sig_news(now, cache), True)
    run("fng", sig_fng, True)
    run("funding", sig_funding, True)
    if due("candles") or not cache.get("candles"):
        try:
            cache["candles"] = get_candles()
        except Exception as e:
            print("candles failed:", e, flush=True)
        cache["candles_t"] = now
    ts_ = {}
    try:
        ts_ = trend_signals(cache.get("candles") or {}, price)
    except Exception as e:
        print("trend failed:", e, flush=True)
    for k_ in ("trend_h", "trend_w", "trend_1h", "trend_4h", "trend_24h", "trend_7d", "levels"):
        if k_ in ts_:
            sigs[k_] = {"score": round(ts_[k_][0], 3), "detail": ts_[k_][1], "ok": True}
        else:
            sigs[k_] = {"score": None, "detail": "needs chart history", "ok": False}
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

    C = cfg()
    try:
        lr = load(os.path.join(DIR, "learn_report.json"), None) or {}
        C["trust"] = {k: v.get("verdict") for k, v in (lr.get("signals") or {}).items()}
    except Exception:
        C["trust"] = {}
    try:
        import exit_learn as _xl
        xr = _xl.current(DIR, now)
        raw_ = load(os.path.join(DIR, "config.json"), {})          # settings you saved yourself win over the learned ones
        pr_ = load(os.path.join(DIR, "practice.json"), {}).get("mode")
        C["practice"] = pr_ if isinstance(pr_, str) else "auto"
        C["exit_on"] = int(raw_["exit_on"]) if "exit_on" in raw_ else (1 if xr["on"] else 0)
        C["exit_peak"] = float(raw_["exit_peak"]) if "exit_peak" in raw_ else xr["peak"]
        C["exit_drop"] = float(raw_["exit_drop"]) if "exit_drop" in raw_ else xr["drop"]
        C["exit_src"] = "you set it" if ("exit_peak" in raw_ or "exit_on" in raw_) else xr["source"]
    except Exception as e:
        print("exit rules failed:", e, flush=True)
    try:
        pj = load(os.path.join(DIR, "patterns.json"), {}) or {}
        C["pattern_bad"] = pj.get("bad") or []
    except Exception:
        C["pattern_bad"] = []
    try:
        import evidence as _ev
        st_ = _ev.update(DIR, now)
        C["entry_block"] = st_.get("block", [])
        C["blackout"] = _ev.blackout(_ev.calendar(DIR, now), now)
    except Exception as e:
        print("evidence failed:", e, flush=True)
    w = C["weights"]
    avail = {k: v for k, v in sigs.items() if v["ok"]}
    tw = sum(w[k] for k in avail)
    score = round(100 * sum(w[k] * v["score"] for k, v in avail.items()) / tw, 1) if tw else 0.0
    conf = round(tw / sum(w.values()), 2)
    lean = "UP" if score >= C["threshold"] else "DOWN" if score <= -C["threshold"] else "NONE"
    if conf < 0.4:
        lean = "NONE"  # too little data to lean on

    for o in S.get("open", []):
        o["hi"] = max(o.get("hi", o["price0"]), price)
        o["lo"] = min(o.get("lo", o["price0"]), price)

    # ---- 15-minute windows ----
    win = now // WINDOW * WINDOW
    kk_ = cache.get("kalshi") or {}
    sync = bool(kk_ and kk_.get("close_ep") and abs(kk_["close_ep"] - (win + WINDOW)) <= 5 and now - cache.get("kalshi_t", 0) <= 40
                and (cache.get("xc") or {}).get("ok", True))
    if S.get("score_ver") != 2:                      # older calls were scored against our own price, not Kalshi's result
        for nm in ("calls", "reviews"):
            try:
                os.replace(os.path.join(DIR, nm + ".jsonl"), os.path.join(DIR, nm + ".v1.jsonl"))
            except OSError:
                pass
        S["score_ver"] = 2; S["open"] = []
    audit(S, now, win, sync, kk_, hist)
    done = S.setdefault("done", [])
    for o in list(S.get("open", [])):
        end = o["start"] + WINDOW
        if now >= end:
            o.setdefault("price1", price)
            res = get_result(o["ticker"]) if o.get("ticker") else None
            src = "kalshi"
            if res is None:
                if o.get("ticker") and now - end < 540:
                    continue                          # Kalshi has not posted the result yet; try again next cycle
                S["open"].remove(o)
                if now - end > 600:
                    continue                          # too old to score fairly
                tgt = o.get("strike") or o["price0"]
                res, src = ("UP" if o["price1"] > tgt else "DOWN"), "estimated"
            else:
                S["open"].remove(o)
            o["outcome"] = res; o["src"] = src
            o["pnl"] = paper_pnl(o)
            rv = review(o)
            if rv:
                with open(os.path.join(DIR, "reviews.jsonl"), "a") as f:
                    f.write(json.dumps(rv) + "\n")
            with open(os.path.join(DIR, "calls.jsonl"), "a") as f:
                f.write(json.dumps(o) + "\n")
            if src == "kalshi":                           # learn from this round right away
                try:
                    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
                    import learner
                    learner.online(DIR, dict(WEIGHTS), now)
                except Exception as e:
                    print("online learning failed:", e, flush=True)
    if sync and not any(o["start"] == win for o in S.setdefault("open", [])) and win not in S.get("skipped", []) \
            and now - win <= 90 and win != S.get("last_win"):
        S["open"].append({"start": win, "price0": price, "score": score, "call": lean, "conf": conf,
                          "signals": {k: v["score"] for k, v in avail.items()}, "locked_at": now,
                          "ticker": kk_.get("ticker"), "kalshi_yes": kk_.get("yes_pct"), "strike": kk_.get("strike")})
        S["last_win"] = win
    cur = next((o for o in S["open"] if o["start"] == win), None)

    k = (cache.get("kalshi") or {}) if sync else {}      # only Kalshi data for THIS round counts
    off = (S.get("audit") or {}).get("offset", 0.0)
    price_k = round(price + off, 2)                       # our price nudged to match Kalshi's own reference price
    pm = p_up_model(price_k, k.get("strike"), win + WINDOW - now, [(t, p + off) for t, p in hist], now)
    P = S.setdefault("path", {"win": None, "pts": [], "ky": []})
    if P["win"] != win:
        P.update({"win": win, "pts": [], "ky": []})
    P["pts"].append([now, round(price, 2)])
    kk = k
    if kk.get("yes_pct") is not None:
        P["ky"].append([now, round(kk["yes_pct"], 1)])
    simout = None
    try:
        import sim as _sim
        live_tick(_sim)
        simout = _sim.step(S, now, win, WINDOW, price_k, k.get("strike"), pm, (cache.get("kalshi") if sync else None), sigs, score,
                           load(os.path.join(DIR, "control.json"), {"on": True}).get("on", True), DIR, C,
                           load(os.path.join(DIR, "run.json"), {}), get_result)
    except Exception as e:
        import traceback; traceback.print_exc(); simout = {"error": str(e)[:100]}
    try:
        import recorder as _rec
        ro_ = (simout or {}).get("run") if isinstance(simout, dict) else None
        _rec.SHARED.update({"sigs": {k: v["score"] for k, v in avail.items()}, "ticker": (cache.get("kalshi") or {}).get("ticker"),
                            "pos": ((ro_ or {}).get("pos") if ro_ and ro_.get("status") == "running" else None),
                            "mode": ("live" if ro_ and ro_.get("live") and ro_.get("status") == "running" else "practice"),
                            "p_model": pm, "score": score})
    except Exception:
        pass
    try:
        import alerts as _al
        _al.island((simout or {}).get("run") if isinstance(simout, dict) else None, now)
    except Exception:
        pass
    if now - S.get("snap_t", 0) >= 60:
        S["snap_t"] = now
        with open(os.path.join(DIR, "snapshots.jsonl"), "a") as f:
            f.write(json.dumps({"t": now, "price": price, "score": score, "conf": conf,
                                "sig": {k: v["score"] for k, v in avail.items()},
                                "kalshi_yes": k.get("yes_pct"),
                                "yes_bid": k.get("yes_bid"),
                                "yes_ask": k.get("yes_ask"), "qsrc": k.get("qsrc"), "list_bid": k.get("list_bid"), "list_ask": k.get("list_ask"),
                                "strike": k.get("strike"), "p_model": pm, "secs_left": win + WINDOW - now,
                                "recent_up": (cache.get("recent_markets") or []).count("UP") if cache.get("recent_markets") else None}) + "\n")
    calls = read_calls()
    sc = scorecard(calls, now)
    recent = [{"start": c["start"], "call": c["call"], "outcome": c["outcome"], "price0": c["price0"],
               "price1": c["price1"], "score": c["score"]} for c in calls[-12:]][::-1]
    order = ["book", "momentum", "whales", "bigtrades", "news", "fng", "funding"]
    return {
        "updated": now, "sample": False, "price": price_k, "price_raw": price,
        "hist": [[t, round(p + off, 2)] for t, p in hist[-800:]], "tg": [[int(w), v] for w, v in sorted((S.get("tg") or {}).items())],
        "audit": dict(audit_out(S), checks=data_checks(S, cache, now, sync, k, price)),
        "live": {"score": score, "lean": lean, "confidence": conf},
        "call": ({"start": cur["start"], "end": cur["start"] + WINDOW, "call": cur["call"], "score": cur["score"],
                  "price0": cur["price0"], "locked_at": cur["locked_at"]} if cur else None),
        "next_window": win + WINDOW,
        "signals": [dict(key=k, label=LABELS[k], weight=w[k], **sigs[k]) for k in order if k in sigs],
        "kalshi": cache.get("kalshi"), "p_model": pm, "sim": simout, "path": {"win": win, "pts": [[t, round(p + off, 2)] for t, p in P["pts"][-200:]], "ky": P["ky"][-200:]}, "config": {"now": {k: v for k, v in C.items()}, "defaults": dict(DEFAULTS, weights=dict(WEIGHTS)), "limits": LIMITS}, "headlines": cache.get("headlines", []),
        "scorecard": sc, "recent": recent, "entry_stats": load(os.path.join(DIR, "entry_stats.json"), None), "blackout": C.get("blackout"), "exit_rules": load(os.path.join(DIR, "exit_rules.json"), None), "patterns": load(os.path.join(DIR, "patterns.json"), None),
        "lessons": read_tail("reviews.jsonl", 6)[::-1], "learning": load(os.path.join(DIR, "learn_report.json"), None), "learn_health": learn_health(cache, now), "lab": lab_view(),
        "recent_markets": cache.get("recent_markets"), "weights": w,
        "note": "Paper mode: no real money. Information only, not financial advice.",
    }


class Control(BaseHTTPRequestHandler):
    """Tiny on/off switch for the simulator, reachable only on the Tailscale address."""
    def _origin_ok(self):
        """Only pages served from this same Pi may change anything (blocks other websites on your phone)."""
        o = self.headers.get("Origin")
        if not o:
            return True
        try:
            from urllib.parse import urlparse
            return urlparse(o).hostname == (self.headers.get("Host", "").split(":")[0] or None)
        except Exception:
            return False

    def _send(self, obj, code=200):
        b = json.dumps(obj).encode()
        self.send_response(code)
        hs = [("Content-Type", "application/json"), ("Access-Control-Allow-Headers", "content-type, x-crew"),
              ("Content-Length", str(len(b)))]
        if self.headers.get("Origin") and self._origin_ok():
            hs.append(("Access-Control-Allow-Origin", self.headers["Origin"]))
        for h, v in hs:
            self.send_header(h, v)
        self.end_headers(); self.wfile.write(b)

    def do_OPTIONS(self):
        self._send({})

    def do_GET(self):
        if self.path.startswith("/run"):
            return self._send(load(os.path.join(DIR, "run.json"), {}))
        if self.path.startswith("/config"):
            return self._send(cfg())
        if self.path.startswith("/live"):
            b = get_broker()
            if not b:
                return self._send({"ready": False, "why": _BROKER["err"] or "no key"})
            bal = b.balance(20)
            return self._send({"ready": bal is not None, "env": b.c.mode, "balance": bal})
        self._send(load(os.path.join(DIR, "control.json"), {"on": True}))

    def do_POST(self):
        try:
            if not self._origin_ok() or self.headers.get("X-Crew") != "1":
                return self._send({"error": "not allowed"}, 403)
            n = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(n) or b"{}")
            if self.path.startswith("/reset"):
                if body.get("confirm") is not True:
                    return self._send({"error": "needs confirm"}, 400)
                rc_ = load(os.path.join(DIR, "run.json"), {})
                if rc_.get("live") and rc_.get("active"):
                    return self._send({"error": "end the live session first"}, 400)
                if body.get("soft") is True:       # keep everything it learned; old lessons count half; fresh wallet
                    save_atomic(os.path.join(DIR, "learn_state.json"), {"soft_t": int(time.time())})
                    old = load(os.path.join(DIR, "run.json"), {})
                    save_atomic(os.path.join(DIR, "run.json"), {"active": True, "id": int(time.time()), "strategy": old.get("strategy", "auto"), "start": 1000.0})
                    return self._send({"ok": True, "soft": True})
                save_atomic(os.path.join(DIR, "reset.json"), {"id": int(time.time() * 1000)})
                return self._send({"ok": True})
            if self.path.startswith("/kill"):
                if body.get("confirm") is not True:
                    return self._send({"error": "needs confirm"}, 400)
                save_atomic(os.path.join(DIR, "run.json"), {"active": False, "halted": "kill", "detail": "Kill switch pressed", "live": True, "t": int(time.time())})
                save_atomic(os.path.join(DIR, "kill.json"), {"t": int(time.time())})
                alert("KILL SWITCH pressed. Closing the open bet and cancelling resting orders.", "Market agent: kill switch")
                return self._send({"ok": True})
            if self.path.startswith("/live"):
                if body.get("confirm") is not True:
                    return self._send({"error": "needs confirm"}, 400)
                rc_ = load(os.path.join(DIR, "run.json"), {})
                if rc_.get("live") and rc_.get("active"):
                    return self._send({"error": "a live session is already running"}, 400)
                b = get_broker()
                bal = b.balance(0) if b else None
                if bal is None or bal < 1:
                    return self._send({"error": "could not read your Kalshi balance"}, 400)
                st = str(body.get("strategy") or "auto")
                if st not in tuple(__import__("sim").STRATS) + ("auto",):
                    st = "auto"
                b.halt = None; b.fails = 0
                run = {"active": True, "live": True, "id": int(time.time()), "strategy": st, "start": round(bal, 2)}
                save_atomic(os.path.join(DIR, "run.json"), run)
                alert("LIVE session started on your Kalshi account. Balance $%.2f, strategy %s." % (bal, st), "Market agent: live started")
                return self._send(run)
            if self.path.startswith("/run"):
                rp = os.path.join(DIR, "run.json")
                cur = load(rp, {})
                if "practice" in body:                         # which practice strategy trades: one of them, or "auto" (all of them, learning)
                    pm_ = str(body.get("practice"))
                    if pm_ != "auto" and pm_ not in tuple(__import__("sim").STRATS):
                        return self._send({"error": "unknown strategy"}, 400)
                    save_atomic(os.path.join(DIR, "practice.json"), {"mode": pm_, "t": int(time.time())})
                    return self._send({"ok": True, "practice": pm_})
                if body.get("start"):
                    if cur.get("live") and cur.get("active"):
                        return self._send({"error": "end the live session first"}, 400)
                    st = str(body.get("strategy") or "auto")
                    if st not in tuple(__import__("sim").STRATS) + ("auto",):
                        st = "auto"
                    amt = min(1000.0, max(10.0, float(body.get("amount") or 1000)))
                    cur = {"active": True, "id": int(time.time()), "strategy": st, "start": amt}
                else:
                    if cur.get("live") and cur.get("active"):
                        alert("LIVE session ended by you. Closing the open bet.", "Market agent: live ended")
                    cur["active"] = False
                save_atomic(rp, cur)
                return self._send(cur)
            if self.path.startswith("/config"):
                path = os.path.join(DIR, "config.json")
                if body.get("reset"):
                    if os.path.exists(path):
                        os.remove(path)
                else:
                    cur = load(path, {})
                    new = clean_cfg(body)
                    if "weights" in new:
                        cur["weights"] = dict(cur.get("weights", {}), **new.pop("weights"))
                    cur.update(new)
                    save_atomic(path, cur)
                return self._send(cfg())
            on = bool(body.get("on"))
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
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import recorder
        recorder.start(DIR)
    except Exception as e:
        print("recorder not started:", e, flush=True)
    try:
        import exit_learn
        exit_learn.start(DIR)
        try:                                              # the pretend wallet follows Auto (the best proven strategy); a live session is never touched
            rp_ = os.path.join(DIR, "run.json"); r_ = load(rp_, {})
            if r_.get("active") and not r_.get("live") and r_.get("strategy") != "auto":
                r_["strategy"] = "auto"; save_atomic(rp_, r_)
        except Exception:
            pass
    except Exception as e:
        print("exit learning not started:", e, flush=True)
    print("market agent started (paper mode)", flush=True)
    while True:
        now = int(time.time())
        try:
            save_atomic(OUT, run_cycle(now, S))
            save_atomic(spath, S)
            if now - S.get("report_t", 0) >= 120:          # morning-report data, refreshed every 2 minutes
                S["report_t"] = now
                try:
                    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
                    import report
                    save_atomic(os.path.join(os.path.dirname(OUT), "report.json"), report.build(DIR, now))
                except Exception as e:
                    print("report failed:", e, flush=True)
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
