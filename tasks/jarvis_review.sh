#!/bin/bash
# Prints Jarvis's recent conversations with timings and your tags, so you can paste or screenshot it for Claude.
# Usage: bash ~/starship/tasks/jarvis_review.sh [how_many=15]
N=${1:-15}
python3 - "$N" <<'PY'
import json, os, sys, time
d = os.path.expanduser("~/voice-data"); n = int(sys.argv[1])
def rd(f):
    out = []
    try:
        for l in open(os.path.join(d, f)):
            try: out.append(json.loads(l))
            except ValueError: pass
    except OSError: pass
    return out
fb = {}
for f in rd("feedback.jsonl"): fb.setdefault(round(f.get("t") or 0, 1), []).append(f.get("tag"))
rows = [r for r in rd("conversations.jsonl") if r.get("heard") or r.get("reply")][-n:]
print("JARVIS REVIEW: last %d conversations" % len(rows))
tot = []
for r in rows:
    tm = r.get("times") or {}; s = sum(tm.get(k, 0) for k in ("stt", "llm", "tts")); tot.append(s) if tm else None
    print("\n%s [%s]  hear %.1fs, think %.1fs, voice %.1fs = %.1fs  %s" % (time.strftime("%a %H:%M", time.localtime(r["t"])), "shortcut" if r.get("sid") == "siri" else "page", tm.get("stt", 0), tm.get("llm", 0), tm.get("tts", 0), s, ("TAGS: " + ", ".join(fb.get(round(r["t"], 1), []))) if fb.get(round(r["t"], 1)) else ""))
    print("  YOU:    " + (r.get("heard") or "")[:200]); print("  JARVIS: " + (r.get("reply") or "")[:300])
if tot: print("\nAverage time to answer: %.1fs (slowest %.1fs)" % (sum(tot) / len(tot), max(tot)))
tags = {}
for f in rd("feedback.jsonl"): tags[f.get("tag")] = tags.get(f.get("tag"), 0) + 1
print("Tag counts:", tags or "none yet")
PY
