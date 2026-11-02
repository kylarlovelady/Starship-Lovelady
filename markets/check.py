#!/usr/bin/env python3
"""Quick health check for the market agent. Run: python3 ~/starship/markets/check.py"""
import json, os, subprocess, time
p = os.path.expanduser("~/crew-web/market.json")
try:
    d = json.load(open(p))
except Exception as e:
    print("No market.json yet:", e); raise SystemExit
age = int(time.time()) - d["updated"]
print("agent: file is %d seconds old (%s)" % (age, "fresh" if age < 90 else "STALE"))
print("price: $%s  score %s  lean %s" % (d["price"], d["live"]["score"], d["live"]["lean"]))
for s in d["signals"]:
    print("  %-16s %s  %s" % (s["label"], "ok " if s["ok"] else "NO ", s["detail"]))
print("kalshi:", d.get("kalshi") or "NOT REACHED")
print("kalshi last 10:", d.get("recent_markets") or "not reached")
print("news stories:", len(d.get("headlines") or []))
print("model chance up:", d.get("p_model"))
sm = d.get("sim") or {}
print("simulator:", "on" if sm.get("on") else "off/none", "| estimated prices" if sm.get("synthetic") else "| live Kalshi prices", sm.get("error", ""))
try:
    out = subprocess.run(["journalctl", "-u", "market-agent", "-n", "5", "--no-pager"], capture_output=True, text=True, timeout=10).stdout
    print("recent log:\n" + out)
except Exception:
    pass
