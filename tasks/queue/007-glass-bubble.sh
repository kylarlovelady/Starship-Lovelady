#!/bin/bash
# QUEUE-OK
# Home screen (~/hub-dashboard): frosted-glass bubble behind the clock, date and weather (like iOS), tint adapts to dark/light text,
# plus no text cursor/caret in full screen. Makes a backup first; safe to run twice. Turn the bubble off with "glass": false in settings.json.
cd ~/hub-dashboard || { echo "no hub-dashboard"; exit 0; }
python3 - <<'PY'
import glob, os, re, shutil, json
CSS = """/*glass*/#bubble{display:flex;flex-direction:column;align-items:center;padding:2.2vh 5vw 2.4vh;border-radius:34px;background:rgba(255,255,255,.5);max-width:92vw;
 border:1px solid rgba(255,255,255,.6);-webkit-backdrop-filter:blur(26px) saturate(1.7);backdrop-filter:blur(26px) saturate(1.7);
 box-shadow:0 8px 40px rgba(0,0,0,.28),inset 0 1px 0 rgba(255,255,255,.45);text-shadow:none}
#bubble #clock{text-shadow:none!important}#bubble #date{margin-bottom:1.6vh}
html,body,*{caret-color:transparent!important;-webkit-user-select:none;user-select:none;-webkit-tap-highlight-color:transparent}*:focus{outline:none!important}body{cursor:none}/*/glass*/
"""
JS = """else{b.background='';}
try{var lum=function(h){if(!h||h.charAt(0)!=='#')return 1;var n=parseInt(h.slice(1),16);return (0.299*(n>>16)+0.587*((n>>8)&255)+0.114*(n&255))/255;};
var bu=g('bubble');if(bu){if(s.glass===false){bu.style.cssText='background:none;border:0;box-shadow:none;-webkit-backdrop-filter:none;backdrop-filter:none;padding:0';}
else{var dk=lum(s.clock_color||s.text_color||'#e8f4ff')<0.5;bu.style.cssText='';bu.style.background=dk?'rgba(255,255,255,.5)':'rgba(14,20,32,.5)';bu.style.borderColor=dk?'rgba(255,255,255,.6)':'rgba(255,255,255,.18)';}}}catch(e){}"""
OLD_JS = "else{b.background='';}"
done = []
for f in glob.glob("*.html"):
    h = open(f, encoding="utf-8").read(); o = h
    if f == "index.html" and 'id="bubble"' not in h:
        m = re.search(r'<div id="clock">.*?<div id="wx">.*?</div>', h, re.S)
        if m: h = h[:m.start()] + '<div id="bubble">' + m.group(0) + '</div>' + h[m.end():]
    if f == "index.html" and "/*glass*/" not in h: h = h.replace("</style>", CSS + "</style>", 1)
    if "/*glass js*/" not in h and OLD_JS in h and "<!--theme-->" in h:
        h = h.replace(OLD_JS, "/*glass js*/" + JS, 1)
    if h != o:
        if not os.path.exists(f + ".bak-glass"): shutil.copy(f, f + ".bak-glass")
        open(f, "w", encoding="utf-8").write(h); done.append(f)
print("patched:", done or "nothing (already done?)")
try:   # make the open screen reload itself
    d = json.load(open("settings.json")); d["reload"] = int(d.get("reload", 0)) + 1; json.dump(d, open("settings.json", "w"))
    print("asked the screen to reload")
except Exception as e: print("settings.json not touched:", e)
PY
echo "== check"; grep -c 'id="bubble"' index.html; grep -c "glass js" index.html theme.html 2>/dev/null
