#!/bin/bash
# Sends one test alert to your phone through Home Assistant and shows what happened.
cd ~/starship/markets && python3 - <<'PY'
import alerts, os, time
ok = alerts.send("Test alert from the market agent. If you can read this on your phone, alerts work.", "Market agent: test", wait=True)
print("sent:", ok)
try: print(open(os.path.join(alerts.DIR, "alerts.log")).read().strip().splitlines()[-1])
except Exception as e: print("no log yet", e)
PY
