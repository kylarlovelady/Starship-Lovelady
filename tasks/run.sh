#!/bin/bash
# Cancels the leftover 1 cent test bid from the connection test (one specific order only; nothing else is touched).
cd ~/starship/markets && python3 - <<'PY'
import json, kalshi_trade as k
c = k.Kalshi()
s, x = c.cancel("01a19df5-3fd0-72f9-8626-ace23f46edeb", "KXBTC15M-26NOV021545-45")
print("cancel ->", s, json.dumps(x)[:300])
s, p = c.positions(); print("positions ->", s, json.dumps(p)[:200])
PY
