#!/bin/bash
# QUEUE-OK
# practice wallet was following v_snipe; Kylar (2026-11-06) wants every strategy experimenting again: set the practice run back to Auto (keeps wallet, id and everything learned; practice only, live untouched)
python3 - <<'PY'
import json, os, time
p = os.path.expanduser("~/market-data/run.json")
r = json.load(open(p))
print("before:", {k: r.get(k) for k in ("active", "live", "strategy", "start")})
if r.get("live"):
    print("LIVE session present: not touching it"); raise SystemExit
bk = p + ".bak-%d" % int(time.time())
open(bk, "w").write(json.dumps(r))
r["strategy"] = "auto"
tmp = p + ".tmp"
open(tmp, "w").write(json.dumps(r)); os.replace(tmp, p)
print("after:", {k: r.get(k) for k in ("active", "live", "strategy", "start")}, "backup", os.path.basename(bk))
PY
