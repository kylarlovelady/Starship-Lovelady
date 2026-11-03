"""Pulls history so the agent can learn from old rounds right away instead of waiting for new ones. Read-only: it places no orders.
  rounds.jsonl   every settled Kalshi BTC 15-minute round in the period: ticker, open/close time, target (strike), result
  candles.jsonl  Kalshi's own minute-by-minute Up bid/ask for each of those rounds
  btc1m.jsonl    Bitcoin's minute-by-minute price (Coinbase) over the same period
It saves to ~/market-data/history/ and can be stopped and restarted: it only fetches what it does not have yet.
Usage: python3 backfill.py [days=14] [budget_seconds=1500]"""
import json, os, sys, time, urllib.request, urllib.error

BASE = "https://api.elections.kalshi.com/trade-api/v2"
HOME = os.path.expanduser("~")
DIR = os.environ.get("MARKET_DIR", os.path.join(HOME, "market-data"))
H = os.path.join(DIR, "history")
ERRS = {}


def _get(url, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "starship-market-agent/1.0", "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code >= 500:
                time.sleep(2 * (i + 1)); continue
            raise
        except Exception:
            time.sleep(1 + i)
    raise OSError("failed after retries: " + url[:90])


def px(v):
    """A price as dollars, from a dollar string, a cents number, or a {open,high,low,close} object."""
    if isinstance(v, dict):
        for k in ("close", "close_dollars", "mean"):
            if v.get(k) is not None:
                return px(v[k])
        return None
    if v is None or v == "":
        return None
    try:
        x = float(v)
    except (TypeError, ValueError):
        return None
    return x / 100.0 if x > 1.0 else x


def parse_candle(c):
    """[end_time, yes_bid, yes_ask, last_trade, volume] in dollars, or None when the minute had no two-sided quote."""
    t = c.get("end_period_ts") or c.get("end_ts") or c.get("ts")
    if isinstance(t, str):
        try:
            import datetime
            t = datetime.datetime.fromisoformat(t.replace("Z", "+00:00")).timestamp()
        except ValueError:
            return None
    b = px(c.get("yes_bid", c.get("bid")))
    a = px(c.get("yes_ask", c.get("ask")))
    if t is None or b is None or a is None or a < b:
        return None
    try:
        vol = float(c.get("volume_fp", c.get("volume")) or 0)
    except (TypeError, ValueError):
        vol = 0.0
    return [int(t), round(b, 4), round(a, 4), px(c.get("price")), vol]


def _have(path, key):
    out = set()
    try:
        for ln in open(path):
            try:
                out.add(json.loads(ln)[key])
            except (ValueError, KeyError):
                pass
    except OSError:
        pass
    return out


def _iso(t):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t))


def _epoch(s):
    import calendar
    return calendar.timegm(time.strptime(s[:19], "%Y-%m-%dT%H:%M:%S"))


def rounds(days, deadline):
    path = os.path.join(H, "rounds.jsonl")
    have = _have(path, "ticker")
    cutoff = int(time.time() - days * 86400)
    cur, new = None, 0
    with open(path, "a") as f:
        while time.time() < deadline:
            q = "/markets?series_ticker=KXBTC15M&status=settled&limit=1000&min_close_ts=%d" % cutoff + ("&cursor=" + cur if cur else "")
            d = _get(BASE + q)
            for m in d.get("markets", []):
                tk = m.get("ticker")
                if not tk or tk in have or m.get("result") not in ("yes", "no"):
                    continue
                try:
                    close = _epoch(m["close_time"])
                except Exception:
                    continue
                st = m.get("floor_strike")
                f.write(json.dumps({"ticker": tk, "open": close - 900, "close": close, "strike": st, "result": "UP" if m["result"] == "yes" else "DOWN"}) + "\n")
                have.add(tk); new += 1
            cur = d.get("cursor")
            if not cur or not d.get("markets"):
                break
            time.sleep(0.2)
    return new


def candles(deadline):
    rp, cp = os.path.join(H, "rounds.jsonl"), os.path.join(H, "candles.jsonl")
    have = _have(cp, "ticker")
    todo = []
    for ln in open(rp):
        try:
            r = json.loads(ln)
        except ValueError:
            continue
        if r["ticker"] not in have:
            todo.append(r)
    todo.sort(key=lambda r: -r["close"])
    n = 0
    with open(cp, "a") as f:
        for r in todo:
            if time.time() > deadline:
                break
            rows = None
            for path in ("/series/KXBTC15M/markets/%s/candlesticks" % r["ticker"], "/historical/markets/%s/candlesticks" % r["ticker"]):
                try:
                    d = _get(BASE + path + "?start_ts=%d&end_ts=%d&period_interval=1" % (r["open"] - 60, r["close"] + 60))
                    rows = [x for x in (parse_candle(c) for c in d.get("candlesticks", [])) if x]
                    if rows:
                        break
                except urllib.error.HTTPError as e:
                    ERRS["candles %s" % e.code] = ERRS.get("candles %s" % e.code, 0) + 1
                except Exception as e:
                    ERRS["candles " + type(e).__name__] = ERRS.get("candles " + type(e).__name__, 0) + 1
            f.write(json.dumps({"ticker": r["ticker"], "c": rows or []}) + "\n")      # an empty list marks "nothing available", so it is not asked again
            n += 1
            if n % 50 == 0:
                print("  candles fetched for %d rounds, %d to go" % (n, len(todo) - n), flush=True)
            time.sleep(0.12)
    return n, max(0, len(todo) - n)


def btc(days, deadline):
    path = os.path.join(H, "btc1m.jsonl")
    have = _have(path, "b")
    end = int(time.time() // 18000 * 18000)
    n = 0
    with open(path, "a") as f:
        b = end
        while b >= time.time() - days * 86400 and time.time() < deadline:
            if b not in have:
                try:
                    d = _get("https://api.exchange.coinbase.com/products/BTC-USD/candles?granularity=60&start=%s&end=%s" % (_iso(b), _iso(b + 18000)))
                    rows = sorted([[int(x[0]), float(x[4])] for x in d])
                    f.write(json.dumps({"b": b, "r": rows}) + "\n"); n += 1
                except Exception as e:
                    ERRS["btc " + type(e).__name__] = ERRS.get("btc " + type(e).__name__, 0) + 1
                time.sleep(0.4)
            b -= 18000
    return n


def main():
    days = float(sys.argv[1]) if len(sys.argv) > 1 else 14
    budget = float(sys.argv[2]) if len(sys.argv) > 2 else 1500
    os.makedirs(H, exist_ok=True)
    dl = time.time() + budget
    print("1/3 listing settled rounds for the last %d days ..." % days, flush=True)
    try:
        print("   new rounds:", rounds(days, dl), flush=True)
    except Exception as e:
        print("   could not list rounds:", e); ERRS["rounds"] = 1
    print("2/3 Kalshi minute prices for each round ...", flush=True)
    got, left = 0, 0
    try:
        got, left = candles(dl)
    except Exception as e:
        print("   candles stopped:", e)
    print("   fetched %d rounds, %d still to do" % (got, left), flush=True)
    print("3/3 Bitcoin minute prices ...", flush=True)
    print("   new 5-hour blocks:", btc(days, dl), flush=True)
    full = sum(1 for ln in open(os.path.join(H, "candles.jsonl")) if json.loads(ln)["c"]) if os.path.exists(os.path.join(H, "candles.jsonl")) else 0
    st = {"t": int(time.time()), "days": days, "rounds_with_prices": full, "still_to_fetch": left, "errors": ERRS}
    json.dump(st, open(os.path.join(H, "status.json"), "w"))
    print("DONE: %d rounds with Kalshi prices saved. %s" % (full, ("Problems: %s" % ERRS) if ERRS else "No problems."))
    if left:
        print("Run it again to continue (it only fetches what is missing).")


if __name__ == "__main__":
    main()
