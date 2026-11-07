#!/usr/bin/env python3
"""Run by Kylar on the Pi. Lists the phones Home Assistant can notify, and sets which ones get alerts. Never prints the token.
  python3 ~/starship/markets/ha_phones.py            -> list phones (notify service names) and the current alert_phone.txt
  python3 ~/starship/markets/ha_phones.py set NAME   -> alerts go ONLY to the notify service NAME (e.g. mobile_app_kylars_iphone)
  python3 ~/starship/markets/ha_phones.py all        -> remove the limit (alerts to every phone again)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import alerts as A
f = os.path.join(A.DIR, "alert_phone.txt")
if len(sys.argv) > 2 and sys.argv[1] == "set":
    open(f, "w").write("# alerts go only to these phones (Kylar, 2026-11-06)\n" + sys.argv[2] + "\n"); print("saved:", sys.argv[2])
elif len(sys.argv) > 1 and sys.argv[1] == "all":
    try: os.remove(f); print("limit removed")
    except OSError: print("no limit was set")
e = A._env(); tok = e.get("HA_TOKEN"); base = (e.get("HA_URL") or "http://127.0.0.1:8123").rstrip("/")
if not tok:
    print("no HA_TOKEN on this Pi"); sys.exit(0)
names = []
for d in A._call(base + "/api/services", tok):
    if d.get("domain") == "notify":
        names += [s for s in (d.get("services") or {}) if s.startswith("mobile_app_")]
print("phones Home Assistant can notify:"); [print("  ", n) for n in sorted(names)] or None
try: print("current alert_phone.txt:", open(f).read().strip().splitlines()[1:])
except OSError: print("current alert_phone.txt: none (alerts go to every phone)")
