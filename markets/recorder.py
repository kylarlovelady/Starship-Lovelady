"""Black-box recorder for the market agent. Runs in its own thread, once a second, and never touches trading.
It writes one line per second to ~/market-data/ticks-YYYYMMDD.jsonl so the agent (and Claude) can later see exactly what
Kalshi and Bitcoin were doing around every decision:
  - Kalshi best bid/ask and the size sitting at each, plus the top of the order book on both sides
  - Bitcoin price on Coinbase every second, other exchanges and recent trade flow every few seconds
  - the agent's signal readings and the position it holds at that moment
Every feed can fail on its own: a failed feed just records null and backs off, the rest keeps going."""
import gzip, json, os, shutil, threading, time, urllib.request

SHARED = {}          # filled by the collector each cycle: {"sigs": {...}, "pos": {...}, "mode": "practice"|"live", "ticker": ...}
KEEP_DAYS = 60


def _get(url, timeout=4):
    req = urllib.request.Request(url, headers={"User-Agent": "starship-market-agent/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


class Feed:
    """One data source with its own refresh rate and back-off after failures."""
    def __init__(self, name, every, fn):
        self.name, self.every, self.fn = name, every, fn
        self.next = 0.0
        self.fails = 0
        self.val = None
        self.err = None

    def poll(self, now):
        if now < self.next:
            return
        try:
            self.val = self.fn()
            self.fails = 0
            self.err = None
            self.next = now + self.every
        except Exception as e:
            self.fails += 1
            self.val = None
            self.err = (type(e).__name__ + ": " + str(e))[:140]
            self.next = now + min(300, self.every * (2 ** min(self.fails, 6)))


# ---------- feeds ----------
def f_coinbase():
    return float(_get("https://api.exchange.coinbase.com/products/BTC-USD/ticker")["price"])


def f_kraken():
    d = _get("https://api.kraken.com/0/public/Ticker?pair=XBTUSD")["result"]
    return float(list(d.values())[0]["c"][0])


def f_binanceus():
    return float(_get("https://api.binance.us/api/v3/ticker/price?symbol=BTCUSD")["price"])


def f_flow():
    """Coinbase trades of the last few seconds: dollars bought vs sold and trade count."""
    rows = _get("https://api.exchange.coinbase.com/products/BTC-USD/trades?limit=100")
    now = time.time()
    buy = sell = 0.0
    n = 0
    for r in rows:
        try:
            t = time.mktime(time.strptime(r["time"][:19], "%Y-%m-%dT%H:%M:%S")) - time.timezone
        except Exception:
            continue
        if now - t > 10:
            continue
        usd = float(r["size"]) * float(r["price"])
        n += 1
        if r.get("side") == "buy":      # coinbase reports the taker side of the maker's order, so "buy" here is a sell by the taker
            sell += usd
        else:
            buy += usd
    return {"n": n, "buy_usd": round(buy), "sell_usd": round(sell)}


def f_oi():
    """Open interest on a big futures venue (OKX). Forced liquidations are not public everywhere, so only OI for now."""
    d = _get("https://www.okx.com/api/v5/public/open-interest?instType=SWAP&instId=BTC-USD-SWAP")["data"][0]
    return {"oi": float(d["oi"]), "oi_usd": float(d.get("oiUsd") or 0)}


def f_cbbook():
    """Bitcoin order book on Coinbase: dollars waiting to buy vs to sell within 0.1% of the middle. Pressure shows up here before the price moves."""
    d = _get("https://api.exchange.coinbase.com/products/BTC-USD/book?level=2")
    bids = [(float(x[0]), float(x[1])) for x in d["bids"]]
    asks = [(float(x[0]), float(x[1])) for x in d["asks"]]
    mid = (bids[0][0] + asks[0][0]) / 2.0
    b = sum(p * q for p, q in bids if p >= mid * 0.999)
    a = sum(p * q for p, q in asks if p <= mid * 1.001)
    return {"bid_usd": round(b), "ask_usd": round(a)}


def f_funding():
    """OKX perpetual funding rate: how crowded the long or short side is."""
    d = _get("https://www.okx.com/api/v5/public/funding-rate?instId=BTC-USD-SWAP")["data"][0]
    return {"rate": float(d["fundingRate"]), "next": float(d.get("nextFundingRate") or 0)}


def f_liq():
    """Forced liquidations on OKX in the last minute: dollars of longs wiped out vs shorts wiped out. Often the end of a fast move."""
    d = _get("https://www.okx.com/api/v5/public/liquidation-orders?instType=SWAP&uly=BTC-USD&state=filled")["data"]
    now = time.time() * 1000
    lng = sht = 0.0
    for blk in d:
        for x in blk.get("details", []):
            if now - float(x["ts"]) > 60000:
                continue
            usd = float(x["sz"]) * 100.0           # BTC-USD swap: one contract is 100 dollars
            if x.get("posSide") == "long" or (x.get("side") == "sell" and x.get("posSide") in (None, "net", "")):
                lng += usd
            else:
                sht += usd
    return {"long_usd": round(lng), "short_usd": round(sht)}


def f_bybit():
    return float(_get("https://api.bybit.com/v5/market/tickers?category=linear&symbol=BTCUSDT")["result"]["list"][0]["lastPrice"])


def f_kalshi(ticker_fn):
    """Best prices and the top of the order book for the market that is open now."""
    def go():
        d = _get("https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXBTC15M&status=open&limit=3", 4)
        ms = sorted(d.get("markets", []), key=lambda m: m.get("close_time", ""))
        if not ms:
            raise ValueError("no open market")
        m = ms[0]
        out = {k: m.get(k) for k in ("ticker", "close_time", "floor_strike", "yes_bid", "yes_ask", "yes_bid_dollars", "yes_ask_dollars",
                                     "yes_bid_size_fp", "yes_ask_size_fp", "last_price", "last_price_dollars", "volume", "volume_fp", "open_interest")
               if m.get(k) is not None}
        return out
    return go


def f_book(get_ticker):
    def go():
        tk = get_ticker()
        if not tk:
            raise ValueError("no ticker")
        d = _get("https://api.elections.kalshi.com/trade-api/v2/markets/%s/orderbook?depth=5" % tk, 4)
        ob = d.get("orderbook") or d.get("orderbook_fp") or d
        out = {}
        for side in ("yes", "no", "yes_dollars", "no_dollars"):
            v = ob.get(side)
            if v:
                out[side] = v[-5:]          # best prices are last
        if not out:
            raise ValueError("empty book")
        return out
    return go


# ---------- file handling ----------
def _path(d, day):
    return os.path.join(d, "ticks-%s.jsonl" % day)


def tidy(d, today):
    """Compress finished days, delete old ones."""
    try:
        for fn in os.listdir(d):
            if not fn.startswith("ticks-"):
                continue
            full = os.path.join(d, fn)
            day = fn[6:14]
            if fn.endswith(".jsonl") and day != today:
                with open(full, "rb") as src, gzip.open(full + ".gz", "wb") as dst:
                    shutil.copyfileobj(src, dst)
                os.remove(full)
            elif fn.endswith(".gz") and time.time() - os.path.getmtime(full) > KEEP_DAYS * 86400:
                os.remove(full)
    except OSError:
        pass


def build_row(now, feeds, shared):
    kal = feeds["kalshi"].val or {}
    row = {"t": round(now, 1), "px": feeds["coinbase"].val}
    if kal:
        row["k"] = kal
        try:
            from calendar import timegm
            ce = timegm(time.strptime(kal.get("close_time", "")[:19], "%Y-%m-%dT%H:%M:%S"))
            row["left"] = int(ce - now)
        except Exception:
            pass
    if feeds["book"].val:
        row["ob"] = feeds["book"].val
    x = {n: feeds[n].val for n in ("kraken", "bybit") if feeds[n].val is not None}
    if x:
        row["x"] = x
    if feeds["flow"].val:
        row["flow"] = feeds["flow"].val
    if feeds["oi"].val:
        row["oi"] = feeds["oi"].val
    for n in ("cbbook", "funding", "liq"):
        if feeds[n].val:
            row[n] = feeds[n].val
    sg = shared.get("sigs")
    if sg:
        row["sig"] = sg
    for k in ("pos", "mode", "p_model", "score"):
        if shared.get(k) is not None:
            row[k] = shared[k]
    bad = {n: f.err for n, f in feeds.items() if f.err}
    if bad:
        row["err"] = bad
    return row


def run(d, stop=None):
    os.makedirs(d, exist_ok=True)
    holder = {"ticker": None}
    feeds = {
        "coinbase": Feed("coinbase", 1, f_coinbase),
        "kalshi": Feed("kalshi", 1, None),
        "book": Feed("book", 1, None),
        "kraken": Feed("kraken", 5, f_kraken),
        "bybit": Feed("bybit", 5, f_bybit),
        "cbbook": Feed("cbbook", 3, f_cbbook),
        "funding": Feed("funding", 60, f_funding),
        "liq": Feed("liq", 5, f_liq),
        "flow": Feed("flow", 3, f_flow),
        "oi": Feed("oi", 30, f_oi),
    }
    feeds["kalshi"].fn = f_kalshi(None)
    feeds["book"].fn = f_book(lambda: holder["ticker"])
    tidy_t = 0
    while not (stop and stop.is_set()):
        t0 = time.time()
        # fetch the slow feeds in worker threads so one slow site cannot stall the second
        ths = [threading.Thread(target=f.poll, args=(t0,), daemon=True) for f in feeds.values() if f.name != "book"]
        for th in ths:
            th.start()
        for th in ths:
            th.join(5)
        kv = feeds["kalshi"].val or {}
        holder["ticker"] = kv.get("ticker") or SHARED.get("ticker")
        feeds["book"].poll(t0)
        try:
            row = build_row(t0, feeds, SHARED)
            day = time.strftime("%Y%m%d", time.localtime(t0))
            with open(_path(d, day), "a") as fh:
                fh.write(json.dumps(row, separators=(",", ":")) + "\n")
            if t0 - tidy_t > 3600:
                tidy_t = t0
                tidy(d, day)
        except Exception:
            pass
        time.sleep(max(0.05, 1.0 - (time.time() - t0)))


def start(d):
    th = threading.Thread(target=run, args=(d,), daemon=True, name="recorder")
    th.start()
    return th
