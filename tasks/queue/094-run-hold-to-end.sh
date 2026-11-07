#!/bin/bash
# QUEUE-OK
# Kalshi PRACTICE wallet: switch the main practice run from auto to v_hold (never sell early, hold to the end). Practice money only; live stays off. Keeps its id and start.
python3 - <<'PY'
import json, os
p = os.path.expanduser("~/market-data/run.json")
r = json.load(open(p))
print("before:", {k: r.get(k) for k in ("active", "strategy", "live", "start")})
if not r.get("live"):
    r["strategy"] = "v_hold"
    tmp = p + ".tmp"; json.dump(r, open(tmp, "w")); os.replace(tmp, p)
r = json.load(open(p))
print("after:", {k: r.get(k) for k in ("active", "strategy", "live", "start")})
PY
