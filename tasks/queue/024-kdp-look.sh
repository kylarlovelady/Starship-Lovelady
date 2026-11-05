#!/bin/bash
# QUEUE-OK
# Read-only: what is in the KDP studio (templates, books, outputs)? No file contents beyond names and short heads.
cd ~/kdp-studio 2>/dev/null || { echo "no kdp-studio"; exit 0; }
echo "== top"; ls -la | head -40
echo "== tree (depth 3, no venv)"; find . -maxdepth 3 -not -path "./.venv*" -not -path "./.git*" -not -name "*.pyc" | head -120
echo "== sizes"; du -sh . --exclude=.venv 2>/dev/null
echo "== README / notes"; for f in README* NOTES* *.md; do [ -f "$f" ] && { echo "-- $f"; head -40 "$f" | cut -c1-200; }; done
echo "== app routes"; grep -n "@app\.\(get\|post\)" app.py 2>/dev/null | head -40
