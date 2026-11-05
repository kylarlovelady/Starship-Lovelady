#!/bin/bash
# QUEUE-OK
# Read-only: what can the KDP studio engine do? Function names, docstrings, routes, one book.json shape, output file names. No settings or pin.
cd ~/kdp-studio || exit 1
echo "== engine.py head"; head -30 engine.py | cut -c1-180
echo "== engine functions"; grep -n "^def \|^class \|^    def " engine.py | cut -c1-150 | head -70
echo "== app routes"; grep -n "@app\.\|@router\." app.py | cut -c1-120 | head -50
echo "== book.json shape (newest book)"; python3 - <<'PY'
import json,glob,os
for p in sorted(glob.glob(os.path.expanduser("~/kdp-studio/books*/*/book.json")),key=os.path.getmtime)[-2:]:
    d=json.load(open(p)); print(p.split("kdp-studio/")[1]); 
    for k,v in d.items(): print("  ",k,":",(json.dumps(v)[:110]))
PY
echo "== outputs"; ls -la books/*/out books-old-1026-0008/*/out 2>/dev/null | head -30
