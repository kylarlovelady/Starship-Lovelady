"""Jarvis's tools: things he can look up or do for you. Used by phone_voice.py for every door (phone page, Siri Shortcut, home speaker).
 - context_for(text): quick live facts pulled in ONLY when your words ask for them (Pi status, Kalshi agent, Pi-hole, what Claude changed lately).
 - home_command(text): "turn off the kitchen light" -> Home Assistant (lights, switches and fans only; nothing that locks, unlocks or opens).
Everything reads local files or the Pi's own services. Nothing here sends data out. Never raises."""
import json, os, re, time, urllib.request

HOME = os.path.expanduser("~")
STOP = {"the", "a", "an", "my", "light", "lights", "lamp", "in", "on", "off", "please", "to", "for", "up", "down", "switch", "turn", "set", "jarvis", "hey", "all", "of"}


def _read(path, limit=3000):
    try: return open(os.path.join(HOME, path) if not path.startswith("/") else path, encoding="utf-8", errors="ignore").read()[:limit]
    except OSError: return ""


def _env():
    out = {}
    for fn in ("market-data/env", "voice-data/keys.env"):
        for l in _read(fn, 4000).splitlines():
            if "=" in l and not l.startswith("#"):
                k, v = l.split("=", 1); out.setdefault(k.strip(), v.strip().strip('"'))
    return out


def _http(url, token=None, body=None, timeout=4):
    req = urllib.request.Request(url, data=(json.dumps(body).encode() if body is not None else None), headers=({"Authorization": "Bearer " + token, "Content-Type": "application/json"} if token else {}))
    with urllib.request.urlopen(req, timeout=timeout) as r: return json.loads(r.read().decode() or "null")


# ------------------------------------------------------------- live facts
def pi_status():
    j = {}
    try: j = json.loads(_read("starship/hub-extra.json", 20000) or "{}")
    except ValueError: pass
    if not j: return "Pi status report not available yet."
    sv = j.get("services", {}); bad = [k for k, v in sv.items() if v != "active"]; pi = j.get("pi", {}); J = j.get("jarvis", {})
    age = int((time.time() - j.get("time", 0)) / 60)
    s = "Pi (report %d min old): %s, temp %s, memory %s, disk %s. " % (age, pi.get("uptime", "?"), pi.get("temp", "?"), pi.get("mem", "?"), pi.get("disk", "?"))
    s += ("NOT running: %s. " % ", ".join(bad)) if bad else "All watched services running. "
    if j.get("pihole"): s += "Pi-hole: %s. " % j["pihole"]
    s += "Jarvis last 24h: %s turns, hang-ups %s, errors %s." % (J.get("turns24", 0), J.get("hangups") or "none", J.get("errors", 0))
    al = []
    try: al = json.loads(_read("starship/hub-alerts.json", 4000) or "{}").get("active", [])
    except ValueError: pass
    if al: s += " Open alerts: " + "; ".join(al) + "."
    return s


def markets():
    prog = "\n".join(_read("market-data/progress.txt", 4000).splitlines()[:14])
    dig = "\n".join(_read("starship/memory/inbox/kalshi-digest.md", 3000).splitlines()[:16])
    if not prog and not dig: return "No Kalshi agent report on the Pi yet."
    return "Kalshi practice agent (practice money only, live mode off). Supervisor report:\n%s\n%s" % (prog, dig)


def pihole():
    for url in ("http://127.0.0.1:8089/admin/api.php?summaryRaw", "http://127.0.0.1:8089/api/stats/summary", "http://127.0.0.1/admin/api.php?summaryRaw"):
        try:
            j = _http(url, timeout=3)
            if "dns_queries_today" in j: return "Pi-hole: %s queries today, %s blocked (%s%%), %s clients, status %s." % (j.get("dns_queries_today"), j.get("ads_blocked_today"), round(float(j.get("ads_percentage_today", 0)), 1), j.get("unique_clients"), j.get("status"))
            q = j.get("queries", {}); 
            if q: return "Pi-hole: %s queries, %s blocked (%s%%), %s clients." % (q.get("total"), q.get("blocked"), round(float(q.get("percent_blocked", 0)), 1), (j.get("clients") or {}).get("active"))
        except Exception: continue
    return "Pi-hole did not answer from the Pi, or it needs a login I do not have."


def changed():
    L = _read("starship/memory/changelog.md", 6000).splitlines()
    return "Recent changes Claude recorded:\n" + "\n".join(L[:18]) if L else ""


RULES = [
    (r"\b(status|broken|wrong|healthy|working ok|how(?:'s| is) (?:the )?(?:pi|hub|house|system|network)|services|temperature|alerts?)\b", pi_status),
    (r"\b(kalshi|market agent|bitcoin|btc|practice (?:money|bets?)|trading agent|the agent|my bets?)\b", markets),
    (r"\b(pi-?hole|blocked|dns|ad ?block)", pihole),
    (r"\b(what changed|what did (?:you|claude)|what have you (?:done|built|changed)|what's new|recent changes)\b", changed),
]


def context_for(text):
    t = (text or "").lower(); out = []
    for rx, fn in RULES:
        if re.search(rx, t):
            try:
                r = fn()
                if r: out.append(r)
            except Exception: pass
    return "\n\n".join(out)[:4500]


# ------------------------------------------------------------- Home Assistant control
ALLOWED = ("light", "switch", "fan")


def _entities(base, token):
    return [(e["entity_id"], (e.get("attributes") or {}).get("friendly_name") or e["entity_id"]) for e in _http(base + "/api/states", token, timeout=6) if e["entity_id"].split(".")[0] in ALLOWED]


def home_command(text):
    """Returns a spoken confirmation, or None when this was not a device command we can match (the normal answer path then handles it)."""
    t = (text or "").strip().lower().rstrip(".!?")
    m = re.match(r"^(?:jarvis[, ]+)?(?:please[, ]+)?(?:can you |could you )?(?:turn|switch|shut)\s+(on|off)\s+(.+)$", t) or re.match(r"^(?:jarvis[, ]+)?(?:please[, ]+)?(.+?)\s+(on|off)$", t)
    dim = re.match(r"^(?:jarvis[, ]+)?(?:please[, ]+)?(?:dim|set|turn)\s+(.+?)\s+(?:to|at)\s+(\d{1,3})\s*(?:%|percent)?$", t)
    if not (m or dim): return None
    if dim: target, state, pct = dim.group(1), "on", max(1, min(100, int(dim.group(2))))
    elif m.group(1) in ("on", "off"): state, target, pct = m.group(1), m.group(2), None
    else: target, state, pct = m.group(1), m.group(2), None
    words = [w for w in re.findall(r"[a-z0-9']+", target) if w not in STOP]
    if not words or len(t.split()) > 9: return None
    e = _env(); token = e.get("HA_TOKEN"); base = (e.get("HA_URL") or "http://127.0.0.1:8123").rstrip("/")
    if not token: return None
    try: ents = _entities(base, token)
    except Exception: return None
    scored = []
    for eid, name in ents:
        nw = [w for w in re.findall(r"[a-z0-9']+", name.lower()) if w not in STOP]
        if not nw: continue
        hit = sum(1 for w in words if w in nw); 
        if hit == len(words) or (nw and all(w in words for w in nw)): scored.append((hit / max(len(nw), len(words)), eid, name))
    if not scored: return None
    scored.sort(reverse=True)
    if len(scored) > 1 and scored[0][0] == scored[1][0]: return "I found %s and %s. Which one?" % (scored[0][2], scored[1][2])
    _, eid, name = scored[0]; dom = eid.split(".")[0]
    try:
        if pct is not None and dom == "light": _http("%s/api/services/light/turn_on" % base, token, {"entity_id": eid, "brightness_pct": pct}); return "Okay. %s at %d percent." % (name, pct)
        _http("%s/api/services/%s/turn_%s" % (base, dom, state), token, {"entity_id": eid}); return "Okay. %s is %s." % (name, state)
    except Exception as ex: return "I couldn't reach Home Assistant to do that."
