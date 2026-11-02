#!/bin/bash
# Read-only: shows whether the market agent is learning and how the pretend wallet has done. Changes nothing.
python3 - <<'PY'
import json, os, glob, collections
D = os.path.expanduser("~/market-data")
def jl(n):
    out = []
    try:
        for l in open(os.path.join(D, n)):
            try: out.append(json.loads(l))
            except Exception: pass
    except OSError: pass
    return out
def js(n):
    try: return json.load(open(os.path.join(D, n)))
    except Exception: return None
print("=== MY WALLET ROUNDS (newest last) ===")
rl = jl("run_log.jsonl")
for r in rl[-15:]:
    print("%s pnl %+7.2f %-4s first=%-4s trades=%-2s staked=%-7s p_open=%s src=%s" % (
        __import__("time").strftime("%m-%d %H:%M", __import__("time").localtime(r.get("t", 0))), r.get("pnl", 0), r.get("outcome"), r.get("first"),
        r.get("trades"), r.get("staked"), r.get("p_open"), r.get("src")))
if rl:
    w = sum(1 for r in rl if r.get("pnl", 0) > 0)
    print("rounds %d, won %d, total pnl %+.2f, avg staked %.2f" % (len(rl), w, sum(r.get("pnl", 0) for r in rl), sum(r.get("staked", 0) for r in rl) / len(rl)))
print("\n=== PRACTICE STRATEGIES (fake $1000 each) ===")
st = js("state.json") or {}
for k, a in (st.get("accts") or st.get("strategies") or {}).items():
    if isinstance(a, dict):
        print("%-14s windows %-4s wins %-4s pnl %+.2f bal %s" % (k, a.get("windows"), a.get("wins"), a.get("pnl", 0), a.get("bal")))
print("\n=== LEARNER ===")
lr = js("learn_report.json")
print(json.dumps(lr, indent=1)[:1800] if lr else "learn_report.json: none yet (the learner waits for ~20 settled rounds per source)")
print("weights.json:", json.dumps(js("weights.json")))
ll = jl("learn_log.jsonl")
print("learn_log entries:", len(ll))
for e in ll[-5:]: print(" ", json.dumps(e)[:300])
print("calls logged:", len(jl("calls.jsonl")))
PY
