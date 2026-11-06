#!/bin/bash
# Copies Jarvis's voice notes and a privacy-safe feedback summary (no transcripts) into the repo's memory/inbox and pushes,
# so Claude can read them. Safe to run any time. If the Pi cannot push yet, run tasks/pi_push_setup.sh.
set -e
cd ~/starship
mkdir -p memory/inbox
if [ -d ~/voice-data/memory ]; then for f in ~/voice-data/memory/*.md; do [ -f "$f" ] && cp "$f" "memory/inbox/jarvis-$(basename "$f")"; done; fi
python3 - <<'PY'
import json, os, time
d = os.path.expanduser("~/voice-data")
def rd(f):
    out = []
    try:
        for l in open(os.path.join(d, f)):
            try: out.append(json.loads(l))
            except ValueError: pass
    except OSError: pass
    return out
conv = [r for r in rd("conversations.jsonl") if r.get("reply") and r.get("times")]
fb = {}
for f in rd("feedback.jsonl"): fb[f.get("tag")] = fb.get(f.get("tag"), 0) + 1
try: st = json.load(open(os.path.join(d, "settings.json")))
except Exception: st = {}
tot = [(r["times"].get("first_audio") if r["times"].get("first_audio") is not None else sum(r["times"].get(k, 0) for k in ("stt", "llm", "tts"))) for r in conv[-40:]]
lines = ["# Jarvis feedback summary (auto, no transcripts)","",
 "- Conversations logged (last 40 with timings): %d" % len(tot),
 "- Average time to first words: %s" % ("%.1fs (slowest %.1fs)" % (sum(tot) / len(tot), max(tot)) if tot else "n/a"),
 "- Tags tapped in the Lab: %s" % (", ".join("%s x%d" % kv for kv in sorted(fb.items())) or "none"),
 "- Settings: " + ", ".join("%s=%s" % (k, st.get(k)) for k in ("speech_speed", "max_tokens", "tts_model", "silence_end", "follow_quiet", "follow_question", "barge_in", "threshold", "voice_threshold", "ask_unknown")),
 "- Voices enrolled: %d" % len(json.load(open(os.path.join(d, "voiceid", "voices.json")))) if os.path.exists(os.path.join(d, "voiceid", "voices.json")) else "- Voices enrolled: 0"]
open(os.path.expanduser("~/starship/memory/inbox/jarvis-feedback-summary.md"), "w").write("\n".join(lines) + "\n")
PY
bash "$HOME/starship/tasks/status_report.sh" >/dev/null 2>&1 || true
git add memory/inbox
git diff --cached --quiet && { echo "notes unchanged"; exit 0; }
git commit -qm "Jarvis notes and feedback summary sync"
git pull -q --rebase --autostash 2>/dev/null || true
git push -q && echo "notes pushed to the repo" || echo "push failed (run tasks/pi_push_setup.sh)"
