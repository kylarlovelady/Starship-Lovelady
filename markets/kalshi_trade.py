#!/usr/bin/env python3
"""Kalshi trading client. The private key and the key id stay on the Pi (~/market-data), never in chat, notes or GitHub.
Environment is chosen in ~/market-data/env:  KALSHI_ENV=demo (fake funds) or prod (real money)."""
import base64, json, math, os, time, urllib.request, urllib.error, uuid

HOME = os.path.expanduser("~")
DIR = os.environ.get("MARKET_DIR", os.path.join(HOME, "market-data"))
HOSTS = {"demo": "https://external-api.demo.kalshi.co", "prod": "https://external-api.kalshi.com"}
PREFIX = "/trade-api/v2"


def env():
    out = {}
    try:
        for line in open(os.path.join(DIR, "env")):
            if "=" in line and not line.startswith("#"):
                k, v = line.strip().split("=", 1)
                out[k] = v
    except OSError:
        pass
    return out


class Kalshi:
    def __init__(self, mode=None):
        e = env()
        self.mode = mode or e.get("KALSHI_ENV", "demo")
        if self.mode not in HOSTS:
            raise SystemExit("KALSHI_ENV must be demo or prod")
        self.key_id = e.get("KALSHI_KEY_ID")
        self.key_file = e.get("KALSHI_KEY_FILE", os.path.join(DIR, "kalshi_key.pem"))
        if not self.key_id:
            raise SystemExit("No KALSHI_KEY_ID saved. Run: bash ~/starship/markets/kalshi_setup.sh")
        from cryptography.hazmat.primitives import serialization
        with open(self.key_file, "rb") as f:
            self.key = serialization.load_pem_private_key(f.read(), password=None)

    def _sign(self, ts, method, path):
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.asymmetric import padding
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
        msg = (ts + method + path.split("?")[0]).encode()
        if isinstance(self.key, Ed25519PrivateKey):
            sig = self.key.sign(msg)
        else:
            sig = self.key.sign(msg, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.DIGEST_LENGTH), hashes.SHA256())
        return base64.b64encode(sig).decode()

    def call(self, method, path, body=None, timeout=10):
        full = PREFIX + path
        ts = str(int(time.time() * 1000))
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(HOSTS[self.mode] + full, data=data, method=method, headers={
            "KALSHI-ACCESS-KEY": self.key_id, "KALSHI-ACCESS-TIMESTAMP": ts,
            "KALSHI-ACCESS-SIGNATURE": self._sign(ts, method, full), "Content-Type": "application/json", "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                txt = r.read().decode()
                return r.status, (json.loads(txt) if txt else {})
        except urllib.error.HTTPError as e:
            txt = e.read().decode()
            try:
                return e.code, json.loads(txt)
            except Exception:
                return e.code, {"raw": txt}

    def balance(self):
        return self.call("GET", "/portfolio/balance")

    def positions(self):
        return self.call("GET", "/portfolio/positions")

    def order(self, ticker, side, count, price, tif="good_till_canceled"):
        """side: 'bid' or 'ask'. count and price are fixed-point strings. Returns (status, json)."""
        return self.call("POST", "/portfolio/events/orders", {
            "ticker": ticker, "side": side, "count": "%.2f" % count, "price": "%.4f" % price,
            "time_in_force": tif, "self_trade_prevention_type": "taker_at_cross", "client_order_id": str(uuid.uuid4())})

    def cancel(self, order_id, ticker):
        """Kalshi needs the market ticker to route the cancel to the right engine."""
        return self.call("DELETE", "/portfolio/events/orders/" + order_id + "?market_ticker=" + ticker)


class Broker:
    """Turns the wallet's buy and sell decisions into real Kalshi orders and reports what actually filled.
    Every order and reply is written to live_orders.jsonl so nothing is hidden."""

    def __init__(self, client, folder=None):
        self.c = client
        self.dir = folder or DIR
        self.fails = 0
        self.halt = None
        self.slips = []
        self._bal = None
        self._bt = 0.0

    def _log(self, rec):
        try:
            with open(os.path.join(self.dir, "live_orders.jsonl"), "a") as f:
                f.write(json.dumps(rec) + "\n")
        except OSError:
            pass

    def balance(self, max_age=8.0):
        if self._bal is not None and time.time() - self._bt < max_age:
            return self._bal
        try:
            st, b = self.c.balance()
            if st == 200:
                v = b.get("balance_dollars")
                self._bal = float(v) if v is not None else float(b.get("balance", 0)) / 100.0
                self._bt = time.time()
                return self._bal
        except Exception:
            pass
        return None

    def forget_balance(self):
        self._bt = 0.0

    def trade(self, action, ticker, side, count, ask_up, bid_up):
        """action buy or sell, side UP or DOWN. Returns whole contracts filled. Orders are immediate-or-cancel, priced at the
        side of the book we are crossing, so nothing is left resting. Up is the Yes book. Down is the other side of the same book."""
        if action == "buy":
            ks, pr = ("bid", ask_up) if side == "UP" else ("ask", bid_up)
        else:
            ks, pr = ("ask", bid_up) if side == "UP" else ("bid", ask_up)
        n = int(count)
        if n < 1 or not ticker:
            return 0
        # Kalshi prices can be fractions of a cent. Round in the direction that still crosses the book: a bid up, an ask down.
        # plus 2 cents of slack so a quote a few seconds old still fills. Kalshi fills at the book price, not our limit (the test showed
        # a 55 cent limit filling at 54), so the slack costs nothing unless the market really moved.
        pr = (math.ceil(pr * 100 - 1e-9) + 2) / 100.0 if ks == "bid" else (math.floor(pr * 100 + 1e-9) - 2) / 100.0
        pr = min(0.99, max(0.01, pr))
        rec = {"t": int(time.time()), "action": action, "side": side, "ticker": ticker, "book_side": ks, "count": n, "price": pr}
        try:
            st, resp = self.c.order(ticker, ks, n, pr, tif="immediate_or_cancel")
        except Exception as e:
            st, resp = 0, {"error": str(e)[:120]}
        rec.update({"status": st, "reply": resp})
        self._log(rec)
        if st not in (200, 201):
            self.fails += 1
            if self.fails >= 3:
                self.halt = "Kalshi rejected %d orders in a row (%s)" % (self.fails, json.dumps(resp)[:120])
            return 0
        self.fails = 0
        self.forget_balance()
        try:
            n_ok = int(float(resp.get("fill_count") or 0) + 1e-9)
            if n_ok >= 1 and resp.get("average_fill_price") is not None:     # how much worse than the quote the fill was (cents per contract)
                f = float(resp["average_fill_price"])
                worse = {("buy", "UP"): f - ask_up, ("sell", "UP"): bid_up - f, ("buy", "DOWN"): bid_up - f, ("sell", "DOWN"): f - ask_up}[(action, side)]
                self.slips.append(round(worse * 100, 2)); self.slips = self.slips[-200:]
                self._log({"t": int(time.time()), "slip_cents": round(worse * 100, 2), "ticker": ticker, "action": action, "side": side})
            return n_ok
        except Exception:
            return 0

    def position(self, ticker):
        """What Kalshi itself says we hold in this market: {} for nothing, {"side","c","cost"}, or None if it could not be read."""
        try:
            st, p = self.c.call("GET", "/portfolio/positions?ticker=%s&count_filter=position" % ticker)
        except Exception:
            return None
        if st != 200:
            return None
        for m in p.get("market_positions", []):
            if m.get("ticker") == ticker:
                q = float(m.get("position_fp") or 0)
                if abs(q) < 0.005:
                    return {}
                return {"side": "UP" if q > 0 else "DOWN", "c": abs(q), "cost": abs(float(m.get("market_exposure_dollars") or 0))}
        return {}

    def exposure(self, ticker):
        """Dollars Kalshi says are at risk in this market's event, or None if unreadable. Used to double-check our own books."""
        try:
            st, p = self.c.positions()
            if st != 200:
                return None
            ev = ticker.rsplit("-", 1)[0]
            tot = 0.0
            for e in p.get("event_positions", []):
                if e.get("event_ticker") == ev:
                    tot += abs(float(e.get("event_exposure_dollars") or 0))
            return tot
        except Exception:
            return None

    def cancel_all(self):
        try:
            return self.c.call("DELETE", "/portfolio/events/orders")
        except Exception as e:
            return 0, {"error": str(e)[:100]}
