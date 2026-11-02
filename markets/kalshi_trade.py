#!/usr/bin/env python3
"""Kalshi trading client. The private key and the key id stay on the Pi (~/market-data), never in chat, notes or GitHub.
Environment is chosen in ~/market-data/env:  KALSHI_ENV=demo (fake funds) or prod (real money)."""
import base64, json, os, time, urllib.request, urllib.error, uuid

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

    def cancel(self, order_id):
        return self.call("DELETE", "/portfolio/events/orders/" + order_id)
