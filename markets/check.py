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
try:
    raw = json.load(open(os.path.expanduser("~/market-data/kalshi_raw.json")))
    print("kalshi price fields:", {k: v for k, v in raw.items() if any(w in k for w in ("bid", "ask", "price", "last", "yes", "no_", "strike"))})
except Exception:
    pass
print("kalshi last 10:", d.get("recent_markets") or "not reached")
print("news stories:", len(d.get("headlines") or []))
print("model chance up:", d.get("p_model"))
sm = d.get("sim") or {}
print("simulator:", "on" if sm.get("on") else "off/none", "| estimated prices" if sm.get("synthetic") else "| live Kalshi prices", sm.get("error", ""))
sc = d.get("scorecard", {})
for k in ("today", "all"):
    x = sc.get(k, {})
    print("scorecard %-5s calls %s, scored %s, right %s (%s%%), paper profit %s" % (k, x.get("calls"), x.get("scored"), x.get("right"), x.get("pct"), x.get("pnl")))
for r in sm.get("strategies", []):
    print("  sim %-38s balance $%-8s profit %-8s rounds %-3s won %s%% trades %-4s trading-vs-holding %s" % (r["label"], r["bal"], r["pnl"], r["windows"], r["win_pct"], r["trades"], r["mgmt"]))
print("reviews written:", len(d.get("lessons") or []), "latest:", (d.get("lessons") or [{}])[0].get("text", "none")[:140])
try:
    out = subprocess.run(["journalctl", "-u", "market-agent", "-n", "5", "--no-pager"], capture_output=True, text=True, timeout=10).stdout
    print("recent log:\n" + out)
except Exception:
    pass
