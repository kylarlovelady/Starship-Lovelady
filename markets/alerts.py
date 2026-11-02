#!/usr/bin/env python3
"""Phone alerts through Home Assistant's phone app. The token stays on the Pi (HA_TOKEN in ~/market-data/env, set with setkey.sh).
Never raises: an alert that cannot be sent must not stop the agent. Everything sent is also written to alerts.log."""
import json, os, threading, time, urllib.request

HOME = os.path.expanduser("~")
DIR = os.environ.get("MARKET_DIR", os.path.join(HOME, "market-data"))
_last = {}
_svc = {"t": 0, "names": []}


def _env():
    out = {}
    try:
        for line in open(os.path.join(DIR, "env")):
            if "=" in line and not line.startswith("#"):
                k, v = line.strip().split("=", 1)
                out[k] = v
    except OSError:
        pass
    return out


def _log(msg):
    try:
        with open(os.path.join(DIR, "alerts.log"), "a") as f:
            f.write("%s %s\n" % (time.strftime("%Y-%m-%d %H:%M:%S"), msg))
    except OSError:
        pass


def _call(url, token, body=None, timeout=8):
    req = urllib.request.Request(url, data=(json.dumps(body).encode() if body is not None else None),
                                 headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode() or "null")


def _targets(base, token):
    if time.time() - _svc["t"] < 600 and _svc["names"]:
        return _svc["names"]
    names = []
    for d in _call(base + "/api/services", token):
        if d.get("domain") == "notify":
            names += [s for s in (d.get("services") or {}) if s.startswith("mobile_app_")]
    _svc.update({"t": time.time(), "names": names})
    return names


def _send(title, msg):
    e = _env(); token = e.get("HA_TOKEN"); base = (e.get("HA_URL") or "http://127.0.0.1:8123").rstrip("/")
    if not token:
        _log("NOT SENT (no HA_TOKEN): %s | %s" % (title, msg)); return False
    try:
        names = _targets(base, token)
        if not names:
            _log("NOT SENT (no phone found in Home Assistant): %s | %s" % (title, msg)); return False
        for n in names:
            _call("%s/api/services/notify/%s" % (base, n), token, {"title": title, "message": msg, "data": {"push": {"interruption-level": "time-sensitive"}}})
        _log("SENT to %d phone(s): %s | %s" % (len(names), title, msg)); return True
    except Exception as ex:
        _log("NOT SENT (%s): %s | %s" % (str(ex)[:80], title, msg)); return False


def send(msg, title="Market agent", wait=False):
    """Send a phone alert in the background. The same message is not repeated within 60 seconds."""
    now = time.time()
    if now - _last.get(msg, 0) < 60:
        return
    _last[msg] = now
    if wait:
        return _send(title, msg)
    threading.Thread(target=_send, args=(title, msg), daemon=True).start()
