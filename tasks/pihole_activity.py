#!/usr/bin/env python3
"""Friendly Pi-hole activity page. Reads the Pi-hole query database (read-only), writes ONE private page: ~/crew-web/activity.html, which is served
on the Tailscale network only (http://loveladymainaihub.taild703ca.ts.net:8095/activity.html). 12-hour times; plain-English site/app names; grouped by device.
PRIVACY: never write this output into the repo (it is public). Browsing history lives only on the Pi. Never raises.
Run: python3 ~/starship/tasks/pihole_activity.py   (crew_report.py runs it every 5 minutes)"""
import datetime, html, json, os, subprocess, sys, time
H = os.path.expanduser("~"); R = os.path.join(H, "starship"); OUT = os.path.join(H, "crew-web", "activity.html")
NAMES = {}
try: NAMES = json.load(open(os.path.join(R, "tasks", "pihole_names.json")))
except Exception: pass
try: NAMES.update(json.load(open(os.path.join(H, "crew-web", "my-site-names.json"))))        # Kylar's own overrides (stay on the Pi)
except Exception: pass
BLOCKED = {1, 4, 5, 6, 7, 8, 9, 10, 11}
def sql(q):
    r = subprocess.run(["docker", "exec", "pihole", "pihole-FTL", "sqlite3", "-ni", "-separator", "\t", "/etc/pihole/pihole-FTL.db", q], capture_output=True, text=True, timeout=60)
    return [l.split("\t") for l in r.stdout.splitlines() if l.strip()]
def dev_names():
    d = {}
    try:
        r = subprocess.run(["docker", "exec", "pihole", "pihole-FTL", "--config", "dns.hosts"], capture_output=True, text=True, timeout=20).stdout.strip().strip("[]")
        for it in r.split(","):
            p = it.split()
            if len(p) >= 2: d[p[0]] = p[1]
    except Exception: pass
    return d
def reg(dom):
    p = dom.lower().rstrip(".").split(".")
    if len(p) >= 3 and p[-2] in ("co", "com", "org", "net", "gov", "ac") and len(p[-1]) == 2: return ".".join(p[-3:])
    return ".".join(p[-2:]) if len(p) >= 2 else dom
def friendly(dom, blocked):
    d = dom.lower().rstrip(".")
    for i in range(len(d.split("."))):                      # longest match first: a.b.c.com, b.c.com, c.com
        k = ".".join(d.split(".")[i:])
        if k in NAMES: return NAMES[k], True
    r = reg(d)
    if r in NAMES: return NAMES[r], True
    return ("Unknown ad/tracker: " if blocked else "Other site: ") + r, False
def t12(ts): return datetime.datetime.fromtimestamp(ts).strftime("%-I:%M %p")
def day12(ts): return datetime.datetime.fromtimestamp(ts).strftime("%a %-I:%M %p")
now = time.time()
rows = sql("select timestamp, client, domain, status from queries where timestamp > %d and client not in ('127.0.0.1','::1') order by timestamp;" % int(now - 86400))
dn = dev_names()
SKIP_BG = ("Wi-Fi check",)
devs = {}
unknown = {}
for ts_, cl, dom, st in rows:
    try: ts_ = float(ts_); st = int(st)
    except ValueError: continue
    if cl not in dn and ":" in cl: continue                 # skip IPv6 noise
    bl = st in BLOCKED
    app, known = friendly(dom, bl)
    if not known: unknown[reg(dom.lower())] = unknown.get(reg(dom.lower()), 0) + 1
    d = devs.setdefault(dn.get(cl, cl), {"ip": cl, "apps": {}, "visits": []})
    a = d["apps"].setdefault(app, {"n": 0, "blocked": 0, "first": ts_, "last": ts_, "sites": {}})
    a["n"] += 1; a["blocked"] += 1 if bl else 0; a["last"] = ts_; a["sites"][dom] = a["sites"].get(dom, 0) + 1
    v = d["visits"]
    if v and v[-1]["app"] == app and ts_ - v[-1]["end"] < 300: v[-1]["end"] = ts_; v[-1]["n"] += 1; v[-1]["blocked"] += 1 if bl else 0
    else: v.append({"app": app, "start": ts_, "end": ts_, "n": 1, "blocked": 1 if bl else 0})
def card(name, d):
    tot = sum(a["n"] for a in d["apps"].values()); blk = sum(a["blocked"] for a in d["apps"].values())
    top = sorted(d["apps"].items(), key=lambda kv: -kv[1]["n"])[:25]
    h = ['<section class="dev" id="dev-%s"><h2>%s <small>%s · %d lookups, %d blocked</small></h2>' % (html.escape(name), html.escape(name), html.escape(d["ip"]), tot, blk)]
    h.append("<h3>Most used (last 24 hours)</h3><table>")
    for app, a in top:
        h.append("<tr><td>%s</td><td class=r>%d</td><td class=r>%s</td><td class=r>%s</td></tr>" % (html.escape(app), a["n"], ("%d blocked" % a["blocked"]) if a["blocked"] else "", "last " + t12(a["last"])))
    h.append("</table><h3>Timeline (newest first, 12-hour time)</h3><table>")
    for v in reversed([v for v in d["visits"] if not v["app"].startswith(("Ads", "Tracker", "App tracking", "App error", "Unknown ad"))][-60:]):
        s = day12(v["start"]) if t12(v["start"]) == t12(v["end"]) else "%s to %s" % (day12(v["start"]), t12(v["end"]))
        h.append("<tr><td class=t>%s</td><td>%s</td><td class=r>%d</td></tr>" % (s, html.escape(v["app"]), v["n"]))
    h.append("</table></section>")
    return "\n".join(h)
order = sorted(devs.items(), key=lambda kv: kv[0])
page = """<!doctype html><html lang=en><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>Home activity</title><style>
:root{--bg:#0b1020;--fg:#e8eeff;--mut:#8b97b8;--card:#141b33;--line:#243056;--acc:#5ce1ff}
@media(prefers-color-scheme:light){:root{--bg:#f4f6fb;--fg:#10162b;--mut:#5a6480;--card:#fff;--line:#d5dbea;--acc:#0a6fd0}}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.4 system-ui,sans-serif;padding:16px}h1{font-size:20px;margin:0 0 4px}p.s{color:var(--mut);margin:0 0 14px;font-size:13px}
nav{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px}nav a{padding:8px 12px;border:1px solid var(--line);border-radius:10px;color:var(--acc);text-decoration:none;background:var(--card)}
section{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin-bottom:16px}h2{font-size:18px;margin:0 0 6px}h2 small{color:var(--mut);font-weight:400;font-size:12px;display:block}h3{font-size:13px;color:var(--mut);margin:12px 0 4px;text-transform:uppercase;letter-spacing:.04em}
table{width:100%%;border-collapse:collapse}td{padding:5px 4px;border-top:1px solid var(--line);vertical-align:top}.r{text-align:right;color:var(--mut);white-space:nowrap}.t{color:var(--mut);white-space:nowrap}
</style></head><body><h1>Home activity</h1><p class=s>What each device connected to, last 24 hours, updated %s. Names are plain-English guesses from the website address. Private: only visible on your Tailscale network.</p>
<nav>%s</nav>%s<section><h2>Unknown sites <small>Tell Claude what these are and they get a proper name</small></h2><table>%s</table></section></body></html>"""
nav = "".join('<a href="#dev-%s">%s</a>' % (html.escape(n), html.escape(n)) for n, _ in order)
unk = "".join("<tr><td>%s</td><td class=r>%d</td></tr>" % (html.escape(k), v) for k, v in sorted(unknown.items(), key=lambda kv: -kv[1])[:25])
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w").write(page % (datetime.datetime.now().strftime("%a %-I:%M %p"), nav, "\n".join(card(n, d) for n, d in order), unk))
print("wrote", OUT, "devices:", ", ".join(n for n, _ in order), "unknown domains:", len(unknown))
