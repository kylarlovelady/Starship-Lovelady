#!/bin/bash
# Read-only checks: (1) learning numbers, (2) big-trades feed probe, (3) what the voice assistant is running. Changes nothing.
cd ~/starship/markets 2>/dev/null || cd "$(dirname "$0")/../markets"
echo "################ 1. LEARNING ################"
python3 - <<'PY'
import json, os, time
D = os.path.expanduser("~/market-data")
try:
    d = json.load(open(os.path.expanduser("~/crew-web/market.json")))
except Exception as e:
    print("cannot read market.json:", e); d = {}
print("learn health:", d.get("learn_health"))
L = d.get("learning") or {}
print("rounds scored:", L.get("scored"))
for k, g in (L.get("signals") or {}).items():
    print("  %-10s n=%-3s right=%-5s trust=%-5s %s" % (k, g.get("n"), g.get("pct"), g.get("trust"), g.get("verdict")))
r = (d.get("sim") or {}).get("run") or {}
print("wallet:", {k: r.get(k) for k in ("status", "bal", "pnl", "added", "refills", "windows", "wins")})
for x in (d.get("sim") or {}).get("strategies") or []:
    print("  %-34s rounds %-3s win%% %-5s pnl %+8.2f trust %s" % (x.get("label"), x.get("windows"), x.get("win_pct"), x.get("pnl", 0), x.get("trust")))
PY
echo
echo "################ 2. BIG TRADES FEED ################"
python3 - <<'PY'
import sys, time, json, collections
sys.path.insert(0, ".")
import collector as C
now = time.time()
try:
    d = json.loads(C.fetch("https://coinlobster.com/api/public/crypto-whales", 10, C.BROWSER_UA))
    w = d.get("whales", [])
    print("feed ok, trades returned:", len(w))
    btc = [t for t in w if str(t.get("pair", "")).upper().startswith("BTC/")]
    print("BTC trades:", len(btc))
    if w:
        ages = [(now - t.get("timestamp", 0) / 1000.0) / 60 for t in w]
        print("newest trade age (min): %.1f   oldest: %.1f" % (min(ages), max(ages)))
        print("pairs seen:", dict(collections.Counter(str(t.get("pair")) for t in w).most_common(5)))
        print("sample:", json.dumps(w[0])[:300])
    print("signal now:", C.sig_bigtrades(now))
except Exception as e:
    print("FEED FAILED:", repr(e)[:300])
PY
echo
echo "################ 3. VOICE ASSISTANT SETUP ################"
echo "-- running voice-related services"
systemctl list-units --type=service --state=running 2>/dev/null | grep -i -E "wyoming|wake|porcupine|openwake|voice|assist|whisper|piper|satellite|homeassistant|hass" | cut -c1-120
echo "-- docker containers"
(docker ps --format '{{.Names}}  {{.Image}}' 2>/dev/null || sudo -n docker ps --format '{{.Names}}  {{.Image}}' 2>/dev/null) | head -15
echo "-- microphones / speakers"
arecord -l 2>/dev/null | grep -E "^card" | cut -c1-110
aplay -l 2>/dev/null | grep -E "^card" | cut -c1-110
echo "-- wake word and voice processes"
ps aux 2>/dev/null | grep -i -E "wyoming|openwakeword|porcupine|wakeword|satellite|whisper|piper" | grep -v grep | awk '{print $11, $12, $13, $14, $15, $16}' | cut -c1-140 | head -10
echo "-- voice folders in home"
ls -d ~/*voice* ~/*wyoming* ~/*wake* ~/*jarvis* ~/*satellite* 2>/dev/null | head
