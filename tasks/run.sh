#!/bin/bash
# Read-only. (A) when and at what price the wallet's bets were placed, (B) what the voice assistant is set up with. Changes nothing.
echo "################ A. WHEN IT BETS (last 6 wallet rounds) ################"
python3 - <<'PY'
import json, os
D = os.path.expanduser("~/market-data")
rows = []
for l in open(os.path.join(D, "run_log.jsonl")):
    try: rows.append(json.loads(l))
    except Exception: pass
for r in rows[-6:]:
    print("round %s  pnl %+.2f  outcome %s  staked %s" % (__import__("time").strftime("%H:%M", __import__("time").localtime(r["t"])), r["pnl"], r["outcome"], r.get("staked")))
    for m in (r.get("moves") or [])[:8]:
        print("    %4ds in  %-4s %-4s $%-7s at %2d cents" % (m["t"] - r["t"], m["a"], m["side"], m["d"], round(m["px"] * 100)))
PY
echo
echo "################ B. VOICE SETUP ################"
echo "-- capture devices (microphones)"; arecord -l 2>&1 | grep -E "^card|no soundcards" | cut -c1-110
echo "-- playback devices"; aplay -l 2>&1 | grep -E "^card" | cut -c1-110
echo "-- satellite launch script"; grep -v -i -E "token|key|pass|secret" ~/wyoming-satellite/run-hub.sh 2>&1 | head -30
echo "-- wake word service"; systemctl list-units --type=service 2>/dev/null | grep -i -E "wake|wyoming" | cut -c1-100
ps aux | grep -i openwakeword | grep -v grep | sed 's/.*wyoming_openwakeword/wyoming_openwakeword/' | cut -c1-200
echo "-- wake word models and sensitivity"; ls ~/wyoming-openwakeword 2>/dev/null | head; ls ~/*/custom* ~/*/models 2>/dev/null | head
