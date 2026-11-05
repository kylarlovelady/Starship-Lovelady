#!/bin/bash
# QUEUE-OK
# Read-only: every signal's graded accuracy, and the real stake sizes of the practice 'run' wallet (is the $50 cap holding?).
python3 - <<'PY'
import json, os, time, collections
D = os.path.expanduser("~/market-data")
d = json.load(open(os.path.join(D, "learn_report.json")))
print("signals (n, right%, 95% range, verdict, weight):")
for k, v in sorted((d.get("signals") or {}).items(), key=lambda kv: -kv[1].get("pct", 0)):
    print("  %-14s n=%-4s right=%5.1f%%  range %4.1f-%4.1f  %-18s x%.2f" % (k, v.get("n"), v.get("pct", 0), v.get("low", 0), v.get("high", 0), v.get("verdict"), v.get("mult", 1)))
print("other keys:", [k for k in d if k != "signals"])
print("\n'run' stakes by round, last 14 h (from sim_windows / trades):")
rows = []
try:
    for l in open(os.path.join(D, "trades.jsonl")):
        pass
except OSError: pass
ev = collections.OrderedDict()
try:
    for l in open(os.path.join(D, "run_log.jsonl")):
        try: r = json.loads(l)
        except ValueError: continue
        if r.get("t", 0) > time.time() - 14 * 3600 and (r.get("a") == "buy" or r.get("action") == "buy"):
            key = int(r["t"] // 900); ev[key] = ev.get(key, 0) + float(r.get("cost") or r.get("dollars") or r.get("d") or 0)
except OSError as e: print("run_log:", e)
for k, v in list(ev.items())[-14:]: print("  round %s  total bought $%.0f" % (time.strftime("%a %H:%M", time.localtime(k * 900)), v))
print("max per round: $%.0f" % max(ev.values())) if ev else print("no buy rows found with a cost field; first row keys:")
if not ev:
    try: print(list(json.loads(open(os.path.join(D, "run_log.jsonl")).readline()).keys()))
    except Exception as e: print(e)
PY
