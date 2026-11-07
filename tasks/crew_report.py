#!/usr/bin/env python3
"""Writes real facts for the Starship page: ~/crew-web/crew.json, and copies hub-extra.json / hub-alerts.json
next to the page (it is served from ~/crew-web, not ~/starship). No keys, no transcripts. Never raises."""
import json, os, re, shutil, time, glob
H = os.path.expanduser("~"); R = os.path.join(H, "starship"); W = os.path.join(H, "crew-web"); now = time.time()
def rd(p):
    try: return open(p, encoding="utf-8", errors="replace").read()
    except OSError: return ""
out = {"time": now}
try:
    import subprocess; subprocess.run(["python3", os.path.join(R, "tasks", "projects_board.py")], capture_output=True, timeout=20)   # adds the Projects board rows to hub-extra.json
except Exception: pass
try:
    subprocess.run(["python3", os.path.join(R, "tasks", "pihole_activity.py")], capture_output=True, timeout=90)   # private friendly Pi-hole activity page (~/crew-web/activity.html, tailnet only)
except Exception: pass
for n in ("hub-extra.json", "hub-alerts.json", "index.html"):
    try: shutil.copyfile(os.path.join(R, n), os.path.join(W, n))
    except OSError: pass
# decision log: changelog entries (newest first)
dec = []; cur = None
for l in rd(os.path.join(R, "memory", "changelog.md")).splitlines():
    if l.startswith("## "): cur = {"t": l[3:].strip(), "what": ""}; dec.append(cur)
    elif cur and l.startswith("- ") and not cur["what"]: cur["what"] = l[2:].strip()[:220]
out["log"] = [d for d in dec if d["what"]][:12]; out["changes"] = len(dec)
# usage (stands in for the budget): Jarvis chats and replies, last 30 days
chats = replies = 0
for l in rd(os.path.join(H, "voice-data", "trace.jsonl")).splitlines():
    try: r = json.loads(l)
    except ValueError: continue
    if r.get("t", 0) > now - 30 * 86400:
        if r.get("kind") == "heard": chats += 1
        if r.get("kind") == "sentence" and r.get("n") == 0: replies += 1
out["usage"] = {"heard": chats, "replies": replies}
# filing / rule book / trash
mem = glob.glob(os.path.join(R, "memory", "**", "*.md"), recursive=True)
out["files"] = {"memory_files": len(mem), "jarvis_notes": len(glob.glob(os.path.join(H, "voice-data", "memory", "*.md"))),
                "clips": len(glob.glob(os.path.join(H, "voice-data", "clips", "*")))}
arch = rd(os.path.join(R, "memory", "_archive.md")); out["dropped"] = len([l for l in arch.splitlines() if l.startswith("- ")])
todo = rd(os.path.join(R, "memory", "todo.md")); op = todo.split("## Done")[0]
out["todo_open"] = len([l for l in op.splitlines() if l.startswith("- ")]); out["todo_done"] = len([l for l in todo.split("## Done")[-1].splitlines() if l.startswith("- ")]) if "## Done" in todo else 0
# Captain's briefing: the top open items (first lines of todo.md Open), and what is waiting on Kylar
_op = [l[2:].strip() for l in op.splitlines() if l.startswith("- ")]
out["todo_top"] = [re.sub(r"`", "", x)[:120] for x in _op[:5]]
out["waiting_on_kylar"] = [re.sub(r"`", "", x)[:120] for x in _op if re.search(r"kylar (to|says|picks|reports|sends|decides)|waiting on (him|kylar)|needs (his|kylar)|tell claude", x, re.I)][:4]
out["rules"] = len(re.findall(r"^\d+\. ", rd(os.path.join(R, "CLAUDE.md")), re.M))
# wallet Jarvis/the agent can use: practice wallet from market.json, real Kalshi cash from the agent (read-only)
wl = {}
try:
    r = (json.load(open(os.path.join(W, "market.json"))).get("sim") or {}).get("run") or {}
    wl["practice"] = {"bal": r.get("bal"), "pnl": r.get("pnl"), "rounds": r.get("windows"), "strategy": r.get("strategy")}
except Exception: pass
try:
    import subprocess, urllib.request
    ip = subprocess.run("tailscale ip -4", shell=True, capture_output=True, text=True, timeout=5).stdout.split()[0]
    j = json.load(urllib.request.urlopen("http://%s:8097/live" % ip, timeout=6))
    wl["kalshi"] = {"ready": j.get("ready"), "env": j.get("env"), "balance": j.get("balance")}
except Exception: pass
try:
    import subprocess as _sp; _sp.run(["python3", os.path.join(R, "tasks", "home_mic_report.py")], timeout=60, capture_output=True)
except Exception: pass
try:
    _sp.run(["python3", os.path.join(R, "tasks", "snipe_autopsy.py")], timeout=60, capture_output=True)
except Exception: pass
out["wallet"] = wl
json.dump(out, open(os.path.join(W, "crew.json"), "w"))
print("crew.json written")
