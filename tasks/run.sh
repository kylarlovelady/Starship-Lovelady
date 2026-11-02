#!/bin/bash
# Read-only: shows what the two new free whale signals see right now.
cd ~/starship/markets && python3 - <<'PY'
import time, collector as c
now = int(time.time())
for name, fn in (("Whale transfers (Telegram, free)", c.sig_whales), ("Big exchange trades (Coinlobster, free)", c.sig_bigtrades)):
    try:
        s, d = fn(now)
        print("%s: score %+.2f | %s" % (name, s, d))
    except Exception as e:
        print("%s: FAILED: %s" % (name, e))
PY
