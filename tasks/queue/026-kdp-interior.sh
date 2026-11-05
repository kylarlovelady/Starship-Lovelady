#!/bin/bash
# QUEUE-OK
# Read-only: how book.json describes pages/covers, what element types and textures the engine supports.
cd ~/kdp-studio || exit 1
echo "== book.json (current book) keys and sample"; python3 - <<'PY'
import json,glob,os
p=sorted(glob.glob(os.path.expanduser("~/kdp-studio/books/*/book.json")),key=os.path.getmtime)[-1]
d=json.load(open(p)); print(p.split("kdp-studio/")[1])
def show(x,ind=0,depth=0):
    if depth>3: return
    if isinstance(x,dict):
        for k,v in list(x.items())[:14]:
            if isinstance(v,(dict,list)) and depth<3: print(" "*ind+str(k)+":"); show(v,ind+2,depth+1)
            else: print(" "*ind+str(k)+": "+json.dumps(v)[:90])
    elif isinstance(x,list):
        print(" "*ind+"[list of %d]"%len(x)); 
        if x: show(x[0],ind+2,depth+1)
show(d)
PY
echo "== clean() element types"; sed -n 98,132p engine.py | cut -c1-200
echo "== interior()"; sed -n 148,222p engine.py | cut -c1-170 | head -75
echo "== textures"; sed -n 288,330p engine.py | grep -n "kind" | cut -c1-160 | head -12
