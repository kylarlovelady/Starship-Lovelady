#!/bin/bash
# Copies Jarvis's voice notes (~/voice-data/memory/*.md) into the repo (memory/inbox/jarvis-<topic>.md) and pushes,
# so Claude can read them and file them. Safe to run any time. If the Pi has no GitHub push access it says so.
set -e
cd ~/starship
[ -d ~/voice-data/memory ] || { echo "no voice notes yet"; exit 0; }
mkdir -p memory/inbox
for f in ~/voice-data/memory/*.md; do cp "$f" "memory/inbox/jarvis-$(basename "$f")"; done
git add memory/inbox
git diff --cached --quiet && { echo "notes unchanged"; exit 0; }
git commit -qm "Jarvis voice notes sync"
git pull -q --rebase 2>/dev/null || true
git push -q && echo "notes pushed to the repo" || echo "push failed (the Pi has no GitHub push access yet)"
