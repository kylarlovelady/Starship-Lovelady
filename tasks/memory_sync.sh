#!/bin/bash
# Copies Jarvis's notes (~/voice-data/memory.md) into the repo (memory/jarvis_notes.md) and pushes, so Claude can read them.
# Safe to run any time. If the Pi has no GitHub push access this prints how it failed and changes nothing else.
set -e
cd ~/starship
mkdir -p memory
[ -f ~/voice-data/memory.md ] || { echo "no notes yet"; exit 0; }
cp ~/voice-data/memory.md memory/jarvis_notes.md
git add memory/jarvis_notes.md
git diff --cached --quiet && { echo "notes unchanged"; exit 0; }
git commit -qm "Jarvis notes sync"
git pull -q --rebase 2>/dev/null || true
git push -q && echo "notes pushed to the repo" || echo "push failed (Pi has no GitHub push access yet)"
