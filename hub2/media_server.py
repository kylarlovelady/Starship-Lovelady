#!/usr/bin/env python3
"""Hub media library: a folder of background photos/videos plus the Hub's shared settings.
Runs on the main Pi, port 8110, only answers private/tailnet addresses. Files live in ~/hub-media (NOT in the repo).
  GET /api/state  -> {files:[{name,type,size}], settings:{...}}
  GET /media/<n>  -> the file (range requests ok, so videos seek)
  POST /api/upload?name=x   (raw body)   POST /api/settings (json)   POST /api/delete (json {name})"""
import json, os, re, ipaddress, mimetypes, time
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs, unquote

ROOT = os.path.expanduser("~/hub-media"); os.makedirs(ROOT, exist_ok=True)
SET = os.path.join(ROOT, "settings.json")
EXT = {".jpg": "image", ".jpeg": "image", ".png": "image", ".webp": "image", ".gif": "image", ".mp4": "video", ".webm": "video", ".mov": "video", ".m4v": "video"}
MAX = 150 * 1024 * 1024
DEFAULT = {"current": "ocean", "cycle": False, "minutes": 5, "dim_from": 20, "dim_to": 8}

def settings():
    try: s = json.load(open(SET))
    except Exception: s = {}
    d = dict(DEFAULT); d.update({k: v for k, v in s.items() if k in DEFAULT}); return d

def save(upd):
    s = settings()
    for k, v in upd.items():
        if k not in DEFAULT: continue
        if k == "current" and isinstance(v, str): s[k] = v[:200]
        elif k == "cycle": s[k] = bool(v)
        elif k in ("minutes", "dim_from", "dim_to"):
            try: s[k] = max(1, min(720, int(v))) if k == "minutes" else max(0, min(23, int(v)))
            except Exception: pass
    json.dump(s, open(SET, "w")); return s

def files():
    out = []
    for n in sorted(os.listdir(ROOT), key=lambda n: os.path.getmtime(os.path.join(ROOT, n)), reverse=True):
        e = os.path.splitext(n)[1].lower()
        if e in EXT: out.append({"name": n, "type": EXT[e], "size": os.path.getsize(os.path.join(ROOT, n))})
    return out

def safe(name):
    name = os.path.basename(unquote(name or "")); name = re.sub(r"[^A-Za-z0-9._ -]", "_", name).strip(". ")
    return name if os.path.splitext(name)[1].lower() in EXT else ""

class H(BaseHTTPRequestHandler):
    server_version = "HubMedia"
    def log_message(self, *a): pass
    def ok_ip(self):
        try:
            ip = ipaddress.ip_address(self.client_address[0].replace("::ffff:", ""))
            return ip.is_private or ip.is_loopback or ip in ipaddress.ip_network("100.64.0.0/10")
        except Exception: return False
    def send(self, code, body=b"", ctype="application/json", extra=None):
        self.send_response(code); self.send_header("Content-Type", ctype); self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*"); self.send_header("Access-Control-Allow-Headers", "*"); self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        for k, v in (extra or {}).items(): self.send_header(k, v)
        self.end_headers()
        if body and self.command != "HEAD": self.wfile.write(body)
    def do_OPTIONS(self): self.send(204)
    def js(self, o, code=200): self.send(code, json.dumps(o).encode())
    def do_GET(self):
        if not self.ok_ip(): return self.js({"error": "private network only"}, 403)
        u = urlparse(self.path)
        if u.path == "/api/state": return self.js({"files": files(), "settings": settings(), "t": int(time.time())})
        if u.path.startswith("/media/"):
            n = safe(u.path[7:]); p = os.path.join(ROOT, n)
            if not n or not os.path.isfile(p): return self.js({"error": "not found"}, 404)
            size = os.path.getsize(p); ct = mimetypes.guess_type(p)[0] or "application/octet-stream"; a, b = 0, size - 1; code = 200
            m = re.match(r"bytes=(\d*)-(\d*)", self.headers.get("Range", ""))
            if m and (m.group(1) or m.group(2)):
                if m.group(1): a = int(m.group(1))
                if m.group(2): b = min(int(m.group(2)), size - 1)
                if not m.group(1): a = max(0, size - int(m.group(2))); b = size - 1
                code = 206
            if a > b: return self.send(416)
            self.send_response(code); self.send_header("Content-Type", ct); self.send_header("Accept-Ranges", "bytes"); self.send_header("Content-Length", str(b - a + 1))
            self.send_header("Cache-Control", "max-age=86400"); self.send_header("Access-Control-Allow-Origin", "*")
            if code == 206: self.send_header("Content-Range", "bytes %d-%d/%d" % (a, b, size))
            self.end_headers()
            if self.command == "HEAD": return
            with open(p, "rb") as f:
                f.seek(a); left = b - a + 1
                while left > 0:
                    c = f.read(min(1 << 16, left))
                    if not c: break
                    try: self.wfile.write(c)
                    except Exception: break
                    left -= len(c)
            return
        self.js({"error": "no such route"}, 404)
    def body(self, limit):
        n = int(self.headers.get("Content-Length", 0) or 0)
        if n > limit: return None
        return self.rfile.read(n)
    def do_POST(self):
        if not self.ok_ip(): return self.js({"error": "private network only"}, 403)
        u = urlparse(self.path)
        if u.path == "/api/upload":
            name = safe(parse_qs(u.query).get("name", [""])[0])
            if not name: return self.js({"error": "unsupported file type"}, 400)
            data = self.body(MAX)
            if data is None: return self.js({"error": "file too big (150 MB max)"}, 413)
            base, ext = os.path.splitext(name); p = os.path.join(ROOT, name); i = 1
            while os.path.exists(p): p = os.path.join(ROOT, "%s-%d%s" % (base, i, ext)); i += 1
            open(p, "wb").write(data); return self.js({"ok": True, "name": os.path.basename(p)})
        data = self.body(20000)
        try: obj = json.loads(data or b"{}")
        except Exception: return self.js({"error": "bad json"}, 400)
        if u.path == "/api/settings": return self.js({"settings": save(obj)})
        if u.path == "/api/delete":
            n = safe(obj.get("name")); p = os.path.join(ROOT, n)
            if n and os.path.isfile(p): os.remove(p)
            return self.js({"ok": True})
        self.js({"error": "no such route"}, 404)

if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 8110), H).serve_forever()
