#!/usr/bin/env python3
"""Home Jarvis MIC SWITCH (Kylar 2026-11-07). Tiny web service for the Starship: mute / unmute the home voice assistant's microphone, optionally for a set time.
The mute itself is the file ~/hub-dashboard/muted that hub-mic.py (the satellite's mic wrapper) already honours, so the mic sends silence while it exists (the OLED and
lights already show MIC MUTED). Port 8098. Only the tailnet, this Pi and the home Wi-Fi (192.168.1.x) may call it. Nothing is stored except a timer file.
GET /mic -> JSON status   POST /mic/mute[?minutes=N]   POST /mic/unmute   (N: unmute automatically after N minutes; 'until8' = until 8 AM Central)
Run by cron keep-alive (tasks/jarvis_install.sh). Never raises out of a request."""
import json, os, time, threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
H = os.path.expanduser("~"); M = os.path.join(H, "hub-dashboard", "muted"); T = os.path.join(H, ".mic-unmute-at"); PORT = 8098
WAKE = os.path.join(H, "crew-web", "jarvis-wake.json")


def okip(ip):
    return ip in ("127.0.0.1", "::1") or ip.startswith("192.168.1.") or ip.startswith("100.") or ip.startswith("::ffff:192.168.1.") or ip.startswith("::ffff:100.")


def muted(): return os.path.exists(M)


def until():
    try: return float(open(T).read().strip())
    except Exception: return None


def set_mute(on, minutes=None, until8=False):
    if on:
        open(M, "a").close()
        t = None
        if until8:
            lt = time.localtime(); import calendar
            tgt = time.mktime((lt.tm_year, lt.tm_mon, lt.tm_mday, 8, 0, 0, 0, 0, -1))
            if tgt <= time.time(): tgt += 86400
            t = tgt
        elif minutes: t = time.time() + 60 * float(minutes)
        if t: open(T, "w").write(str(t))
        elif os.path.exists(T): os.remove(T)
    else:
        try: os.remove(M)
        except OSError: pass
        try: os.remove(T)
        except OSError: pass


def state():
    st = "?"
    try: st = open("/tmp/hub-state").read().strip()
    except Exception: pass
    w = {}
    try: w = json.load(open(WAKE))
    except Exception: pass
    return {"muted": muted(), "unmute_at": until(), "state": st, "now": time.time(), "wake": w}


def timer_loop():
    while True:
        try:
            u = until()
            if muted() and u and time.time() >= u: set_mute(False)
        except Exception: pass
        time.sleep(10)


class Hd(BaseHTTPRequestHandler):
    def log_message(self, *a): pass

    def _send(self, code, obj):
        b = json.dumps(obj).encode()
        self.send_response(code); self.send_header("Content-Type", "application/json"); self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS"); self.send_header("Cache-Control", "no-store"); self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)

    def do_OPTIONS(self): self._send(204, {})

    def _go(self):
        try:
            if not okip(self.client_address[0]): return self._send(403, {"error": "not allowed"})
            u = urlparse(self.path); q = parse_qs(u.query); p = u.path.rstrip("/")
            if p == "/mic/mute" and self.command == "POST":
                m = (q.get("minutes") or [""])[0]
                set_mute(True, minutes=(float(m) if m and m != "until8" else None), until8=(m == "until8"))
            elif p == "/mic/unmute" and self.command == "POST": set_mute(False)
            elif p not in ("/mic", ""): return self._send(404, {"error": "no"})
            self._send(200, state())
        except Exception as e:
            self._send(500, {"error": str(e)[:100]})

    do_GET = _go; do_POST = _go


if __name__ == "__main__":
    threading.Thread(target=timer_loop, daemon=True).start()
    ThreadingHTTPServer(("0.0.0.0", PORT), Hd).serve_forever()
