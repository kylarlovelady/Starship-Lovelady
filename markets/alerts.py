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


# ---------- Dynamic Island / Live Activity (real-money session only, your phone only) ----------
_isl = {"t": 0.0, "sig": None, "tag": None, "ended": False, "hb": 0.0, "t0": 0.0, "warned": False}


def _activity(token, base, dev, tag, title, msg, crit, color, progress=None, clear=False):
    if clear:
        body = {"message": "clear_notification", "data": {"tag": tag}}
    else:
        data = {"tag": tag, "live_update": True, "critical_text": crit, "notification_icon": "mdi:record-circle",
                "notification_icon_color": color, "progress_bar_color": color}
        if progress:
            data["progress"], data["progress_max"] = progress
        body = {"title": title, "message": msg, "data": data}
    try:
        _call("%s/api/services/notify/%s" % (base, dev), token, body)
        _log("ISLAND %s: %s | %s" % ("cleared" if clear else "updated", title, msg))
    except Exception as ex:
        _log("ISLAND NOT SENT (%s)" % str(ex)[:80])


def island(run, now=None):
    """Keep one Live Activity (lock screen + Dynamic Island) in step with the REAL-money session. Sends only to the phone named
    HA_LIVE_DEVICE in the env file, never to other phones. Never raises. Updates only on a real change (value moved about $2.50, round result, position opened or closed, offline), plus a heartbeat every 3 minutes, so the Island does not keep popping open."""
    try:
        now = now or time.time()
        e = _env(); token = e.get("HA_TOKEN"); dev = e.get("HA_LIVE_DEVICE"); base = (e.get("HA_URL") or "http://127.0.0.1:8123").rstrip("/")
        live = bool(run and run.get("live"))
        if not token or not dev:
            if live and not _isl["warned"]:
                _isl["warned"] = True; _log("ISLAND skipped: HA_LIVE_DEVICE is not set (run setisland.sh)")
            return
        running = live and run.get("status") == "running"
        if not live or (not running and not run.get("halt")):
            if _isl["tag"] and not _isl["ended"]:
                tag = _isl["tag"]; _isl.update({"tag": None, "sig": None, "ended": False})
                threading.Thread(target=_activity, args=(token, base, dev, tag, "", "", "", "", None, True), daemon=True).start()
            return
        rid = run.get("id")
        if _isl.get("rid") != rid:                                  # a different session: forget the old one
            if _isl["tag"] and not _isl["ended"]:
                threading.Thread(target=_activity, args=(token, base, dev, _isl["tag"], "", "", "", "", None, True), daemon=True).start()
            _isl.update({"rid": rid, "tag": None, "sig": None, "ended": False, "t0": now})
        n = int((now - _isl["t0"]) // 27000)
        tag = "kalshi_live_%s_%d" % (rid or "x", n)
        if _isl["tag"] and _isl["tag"] != tag and not _isl["ended"]:  # Apple ends an activity after about 8 hours: start a fresh one
            threading.Thread(target=_activity, args=(token, base, dev, _isl["tag"], "", "", "", "", None, True), daemon=True).start()
        halted = bool(run.get("halt")) or not running
        offline = (run.get("k_age") or 0) > 15 and not halted       # cannot read the wallet from Kalshi right now
        eq = run.get("equity") if run.get("equity") is not None else run.get("bal", 0)
        pos = run.get("pos")
        sig = (round(eq * 0.4) / 0.4, run.get("windows"), run.get("wins"), (pos or {}).get("side"), round((pos or {}).get("cost", 0)), halted, offline)
        if halted and _isl["ended"] and _isl["tag"] == tag:
            return                                                  # the HALTED notice was already sent
        if _isl["tag"] == tag and sig == _isl["sig"] and now - _isl["hb"] < 180:
            return
        if _isl["tag"] == tag and sig != _isl["sig"] and now - _isl["t"] < 30 and not halted:
            return
        _isl.update({"tag": tag, "sig": sig, "t": now, "hb": now, "ended": halted})
        pnl = run.get("pnl") or 0.0
        asof = time.strftime("%I:%M:%S %p", time.localtime(now - (run.get("k_age") or 0))).lstrip("0")
        msg = "%s%.2f this session · %s/%s rounds won" % ("+$" if pnl >= 0 else "-$", abs(pnl), run.get("wins", 0), run.get("windows", 0))
        if pos:
            msg += " · open: %s $%.2f" % (pos["side"], pos["cost"])
        msg += " · as of " + asof
        bad = halted or offline
        title = ("HALTED · $%.2f" if halted else "NO KALSHI DATA · last $%.2f" if offline else "LIVE · $%.2f") % eq
        color = "#8e8e93" if bad else "#ff4d57"
        try:
            json.dump({"tag": tag, "t": now}, open(os.path.join(DIR, "island.json"), "w"))
        except OSError:
            pass
        rs = int(now % 900)
        threading.Thread(target=_activity, args=(token, base, dev, tag, title, msg, ("HALT" if halted else "OFFLINE" if offline else "$%d" % round(eq)), color, (rs, 900)), daemon=True).start()
    except Exception:
        pass


def island_dead(run, asof_ts):
    """Called by the independent watchdog when the agent has stopped: turn the pill gray with the last known value and its age."""
    try:
        e = _env(); token = e.get("HA_TOKEN"); dev = e.get("HA_LIVE_DEVICE"); base = (e.get("HA_URL") or "http://127.0.0.1:8123").rstrip("/")
        if not (token and dev and run):
            return
        tag = json.load(open(os.path.join(DIR, "island.json")))["tag"]
        eq = run.get("equity") if run.get("equity") is not None else run.get("bal", 0)
        asof = time.strftime("%I:%M:%S %p", time.localtime(asof_ts)).lstrip("0")
        _activity(token, base, dev, tag, "AGENT STOPPED · last $%.2f" % eq, "Lost connection. Last value as of %s. Check the Kalshi app." % asof, "OFFLINE", "#8e8e93")
    except Exception:
        pass
