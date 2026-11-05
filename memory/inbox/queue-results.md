26-11-05 02:13:01 tasks/queue/004-find-theme.sh
```
== kiosk / chromium command
kylarlo+    1731  0.8  4.2 55429072 354416 ?     Sl   Oct25 129:52 /usr/lib/chromium/chromium --force-renderer-accessibility --enable-remote-extensions --show-component-extension-options --enable-gpu-rasterization --no-default-browser-check --disable-pings --m
kylarlo+    3135  0.0  0.0 54541856 2912 ?       Sl   Oct25   0:00 /usr/lib/chromium/chrome_crashpad_handler --monitor-self --monitor-self-annotation=ptype=crashpad-handler --database=/home/kylarlovelady/.config/chromium/Crash Reports --annotation=channel=buil
kylarlo+    3137  0.0  0.0 54533536 2400 ?       S    Oct25   0:00 /usr/lib/chromium/chrome_crashpad_handler --no-periodic-tasks --monitor-self-annotation=ptype=crashpad-handler --database=/home/kylarlovelady/.config/chromium/Crash Reports --annotation=channel
== ports 8080/8081
LISTEN 0      200                                   0.0.0.0:8089       0.0.0.0:*                                         
LISTEN 0      2048                                127.0.0.1:8080       0.0.0.0:*    users:(("python",pid=3765271,fd=12)) 
LISTEN 0      4096               100.105.140.126%tailscale0:8081       0.0.0.0:*                                         
LISTEN 0      4096   [fd7a:115c:a1e0::2f4c:8c7f]%tailscale0:8081          [::]:*                                         
== hub files
ls: cannot access '/usr/local/bin/hub-dashboard.py': No such file or directory
/home/kylarlovelady/hub-alerts-state.json
/home/kylarlovelady/hub-backup-2026-10-20.tar.gz
/home/kylarlovelady/hub-dashboard
/home/kylarlovelady/hub-devices.py
/home/kylarlovelady/hub-devices.py.bak-ts1026-0206
/home/kylarlovelady/hub-mic.py
/home/kylarlovelady/hub-outage.py
/home/kylarlovelady/hub-outage.py.bak-ts1026-0206
/home/kylarlovelady/hub-scripts-backup-2026-10-26.tar.gz
/home/kylarlovelady/hub-voice
== files mentioning clock+weather
/home/kylarlovelady/crew-web/index.html
/home/kylarlovelady/hub-dashboard/theme.html
/home/kylarlovelady/hub-dashboard/settings.html
/home/kylarlovelady/hub-dashboard/layout.html
/home/kylarlovelady/hub-dashboard/preview_api.py
/home/kylarlovelady/hub-dashboard/settings_api.py
/home/kylarlovelady/hub-dashboard/.venv/lib/python3.13/site-packages/watchfiles/_rust_notify.abi3.so
/home/kylarlovelady/hub-dashboard/.venv/lib/python3.13/site-packages/h11/_receivebuffer.py
/home/kylarlovelady/hub-dashboard/.venv/lib/python3.13/site-packages/PIL/Image.py
/home/kylarlovelady/hub-dashboard/.venv/lib/python3.13/site-packages/pip/_vendor/urllib3/util/timeout.py
/home/kylarlovelady/hub-dashboard/.venv/lib/python3.13/site-packages/pip/_vendor/resolvelib/providers.py
/home/kylarlovelady/hub-dashboard/.venv/lib/python3.13/site-packages/pip/_vendor/rich/progress.py
== theme words
/home/kylarlovelady/hub-dashboard/.venv/lib/python3.13/site-packages/PIL/ImageColor.py
/home/kylarlovelady/hub-dashboard/.venv/lib/python3.13/site-packages/pip/_vendor/pygments/lexers/_mapping.py
/home/kylarlovelady/hub-dashboard/.venv/lib/python3.13/site-packages/pip/_vendor/rich/_emoji_codes.py
/home/kylarlovelady/hub-dashboard/.venv/lib/python3.13/site-packages/pydantic/networks.py
/home/kylarlovelady/hub-dashboard/.venv/lib/python3.13/site-packages/pydantic/__init__.py
/home/kylarlovelady/hub-dashboard/.venv/lib/python3.13/site-packages/pydantic/color.py
/home/kylarlovelady/hub-dashboard/.venv/lib/python3.13/site-packages/pydantic/v1/color.py
/home/kylarlovelady/hub-dashboard/.venv/lib/python3.13/site-packages/uvloop/loop.cpython-313-aarch64-linux-gnu.so
== nocursor
(exit 0)
```

## 2026-11-05 02:16:01 tasks/queue/005-hubdash-map.sh
```
== files
2 ./oled-message.json
1147 ./device-names.json
1 ./muted
1416 ./theme.html
3025 ./hub_api.py
1654 ./pictures.py
2003 ./memory_api.py
7216 ./janitor.html
1942 ./network_api.py
8072 ./index.html.bak-ly2
8992 ./hub.html.bak-ha
530 ./mute_api.py
1080 ./theme.html.bak4
7400 ./hub.html.bak-cr
2949 ./hub_api.py.bak-names
138 ./device-names.json.bak-oct26
3485 ./server.py.bak-ly
7093 ./hub.html.bak-hl
4171 ./messages.py
5404 ./settings_api.py.bak-ly
3311 ./network.html
5 ./settings-pin.txt
7550 ./hub.html.bak-imm
3650 ./memory.html
4348 ./crop_api.py
6640 ./fontcache/Nunito_Sans.png
7318 ./fontcache/Open_Sans.png
7094 ./fontcache/Quicksand.png
5341 ./fontcache/Staatliches.png
6730 ./fontcache/Roboto.png
11684 ./fontcache/Great_Vibes.png
8324 ./fontcache/Gochi_Hand.png
6928 ./fontcache/Noto_Mono.png
6087 ./fontcache/Ubuntu_Condensed.png
7093 ./fontcache/FreeSerif.png
7511 ./fontcache/Fira_Code.png
7077 ./fontcache/IBM_Plex_Serif.png
6940 ./fontcache/Noto_Sans_Mono.png
7271 ./fontcache/Stardos_Stencil.png
9774 ./fontcache/Satisfy.png
10098 ./fontcache/Pacifico.png
6603 ./fontcache/League_Spartan.png
8424 ./fontcache/P052.png
5496 ./fontcache/Saira_Stencil_One.png
1185 ./fontcache/Press_Start_2P.png
11363 ./fontcache/Fontdiner_Swanky.png
6797 ./fontcache/FreeSans.png
6577 ./fontcache/Nimbus_Sans_Narrow.png
6933 ./fontcache/Hack.png
7257 ./fontcache/Allerta_Stencil.png
6848 ./fontcache/IBM_Plex_Sans_Var.png
7604 ./fontcache/Caveat.png
6032 ./fontcache/Roboto_Condensed.png
7260 ./fontcache/Nimbus_Roman.png
6861 ./fontcache/Nimbus_Mono_PS.png
7988 ./fontcache/Luckiest_Guy.png
8362 ./fontcache/Chewy.png
7125 ./fontcache/Nimbus_Sans.png
7700 ./fontcache/Montserrat.png
6427 ./fontcache/DejaVu_Sans_Mono.png
== who serves 8080
    PID COMMAND
3765271 /home/kylarlovelady/hub-dashboard/.venv/bin/python /home/kylarlovelady/hub-dashboard/server.py
== clock/weather/date in html (line:text)
index.html:10:#clock{font-size:15vw;font-weight:200;letter-spacing:.02em;color:var(--cyan);
index.html:12:#date{font-size:2.6vw;color:var(--dim);letter-spacing:.2em;text-transform:uppercase;margin-bottom:4vh}
index.html:32:<div id="clock">--:--</div><div id="date"></div>
index.html:109:col('clock',s.clock_color);if(g('clock'))g('clock').style.textShadow=s.clock_color?'0 0 30px '+rgba(s.clock_color,.35):'';
index.html:110:col('date',s.date_color);col('wx',s.weather_color);
janitor.html:67: d.trash.forEach(t=>{const r=el('div','row');const b=el('div','b');b.appendChild(el('div','p',t.path));b.appendChild(el('div','w','Moved '+t.date+' · '+t
settings.html:28:<div class="r"><span>Clock color</span><input type="color" id="clock_color"></div>
settings.html:29:<div class="r"><span>Date color</span><input type="color" id="date_color"></div>
settings.html:30:<div class="r"><span>Weather color</span><input type="color" id="weather_color"></div>
theme.html:9:col('clock',s.clock_color);if(g('clock'))g('clock').style.textShadow=s.clock_color?'0 0 30px '+rgba(s.clock_color,.35):'';
theme.html:10:col('date',s.date_color);col('wx',s.weather_color);
== theme storage
-rw-r--r-- 1 kylarlovelady kylarlovelady 1147 Oct 26 22:14 device-names.json
-rw-r--r-- 1 kylarlovelady kylarlovelady    2 Oct 19 17:33 oled-message.json
-rw-r--r-- 1 kylarlovelady kylarlovelady  495 Nov  4 15:02 settings.json
settings_api.py:14:CFG = BASE / "settings.json"
settings_api.py:80:    body = await request.json()
settings_api.py:137:    url = str((await request.json()).get("url", ""))
settings_api.py:157:    name = str((await request.json()).get("name", ""))
preview_api.py:74:    b = await request.json()
(exit 0)
```

## 2026-11-05 02:19:01 tasks/queue/006-homescreen-source.sh
```
== index.html lines 1-40 (cut 330)
<!doctype html>
<html><head><meta charset="utf-8"><title>Hub</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
:root{--bg:#05080f;--cyan:#38e8ff;--dim:#6b7f94;--red:#ff4d5e;--blue:#4d8dff;--green:#3dffa0}
*{box-sizing:border-box;margin:0}
body{background:radial-gradient(ellipse at 50% 20%,#0d1a2b 0%,var(--bg) 70%);color:#e8f4ff;
 font-family:"Segoe UI",system-ui,sans-serif;height:100vh;overflow:hidden;display:flex;
 flex-direction:column;align-items:center;justify-content:center}
#clock{font-size:15vw;font-weight:200;letter-spacing:.02em;color:var(--cyan);
 text-shadow:0 0 30px rgba(56,232,255,.35)}
#date{font-size:2.6vw;color:var(--dim);letter-spacing:.2em;text-transform:uppercase;margin-bottom:4vh}
#wx{display:flex;gap:4vw;align-items:baseline;font-size:2.4vw;color:var(--dim)}
#temp{font-size:7vw;font-weight:200;color:#e8f4ff}
#cond{font-size:3vw;color:#e8f4ff}
#panel{position:fixed;left:5vw;right:5vw;bottom:4vh;padding:2.5vh 3vw;border-radius:22px;
 background:rgba(10,20,34,.88);border:1px solid rgba(56,232,255,.4);
 box-shadow:0 0 40px rgba(56,232,255,.2);backdrop-filter:blur(12px);
 transform:translateY(130%);opacity:0;transition:transform .45s ease,opacity .45s ease}
#panel.show{transform:none;opacity:1}
#status{display:flex;align-items:center;gap:1.2vw;font-size:2vw;letter-spacing:.2em;
 text-transform:uppercase;color:var(--dim);margin-bottom:1.5vh}
#dot{width:1.6vw;height:1.6vw;border-radius:50%;background:var(--red);animation:pulse 1.2s infinite}
#panel.thinking #dot{background:var(--blue)}
#panel.speaking #dot{background:var(--green)}
@keyframes pulse{50%{opacity:.35;transform:scale(.8)}}
.lbl{font-size:1.7vw;color:var(--dim);text-transform:uppercase;letter-spacing:.15em}
#you{font-size:2.6vw;color:var(--cyan);min-height:3.4vw;margin-bottom:1.5vh}
#ai{font-size:3vw;line-height:1.3;min-height:4vw}
#pic{display:none;max-height:28vh;max-width:100%;border-radius:12px;margin-top:1.5vh;object-fit:contain}
</style></head><body>
<div id="clock">--:--</div><div id="date"></div>
<div id="wx"><span id="temp"></span><span id="cond"></span><span id="extra"></span></div>
<div id="panel"><div id="status"><div id="dot"></div><span id="stext">Listening</span></div>
<div class="lbl">You</div><div id="you"></div><div class="lbl">Alexa</div><div id="ai"></div><img id="pic" alt=""></div>
<script>
const $=id=>document.getElementById(id);
function tick(){const d=new Date();
 $('clock').textContent=d.toLocaleTimeString('en-US',{hour:'numeric',minute:'2-digit',hour12:true});
 $('date').textContent=d.toLocaleDateString('en-US',{weekday:'long',month:'long',day:'numeric'});}
== theme.html
<!--theme--><script>
(function(){var v=-1,rl=null,q=null;
try{q=new URLSearchParams(location.search).get('pv');}catch(e){}
function g(i){return document.getElementById(i);}
function rgba(h,a){var n=parseInt(h.slice(1),16);return 'rgba('+(n>>16)+','+((n>>8)&255)+','+(n&255)+','+a+')';}
function col(i,c){var e=g(i);if(e)e.style.color=c||'';}
function apply(s){var b=document.body.style;
b.fontFamily=s.font?'"'+s.font+'",system-ui,sans-serif':'';
col('clock',s.clock_color);if(g('clock'))g('clock').style.textShadow=s.clock_color?'0 0 30px '+rgba(s.clock_color,.35):'';
col('date',s.date_color);col('wx',s.weather_color);
b.color=s.text_color||'';col('temp',s.text_color);col('cond',s.text_color);
if(s.bg_mode==='image'&&s.bg_image){var d=s.dim;b.background='linear-gradient(rgba(0,0,0,'+d+'),rgba(0,0,0,'+d+')),url("/bg/'+s.bg_image+'") center/cover no-repeat';}
else if(s.bg_mode==='color'){b.background=s.bg_color;}
else{b.background='';}}
if(q){var st=document.createElement('style');st.textContent='#mutebtn{display:none!important}';document.head.appendChild(st);try{apply(JSON.parse(q));}catch(e){}return;}
function poll(){fetch('/api/settings').then(function(r){return r.json();}).then(function(s){
if(rl===null){rl=s.reload||0;}else if((s.reload||0)!==rl){location.reload();return;}
if(s.version!==v){v=s.version;apply(s);}}).catch(function(){});}
poll();setInterval(poll,3000);})();
</script><!--/theme-->
== how theme.html is used
== settings.json (colors/fonts/sizes only)
{'font': 'Great Vibes', 'clock_color': '#000000', 'date_color': '#000000', 'weather_color': '#000000', 'text_color': '#000000', 'bg_mode': 'image', 'bg_color': '#05080f', 'bg_image': 'bg-1793825570392.jpg'}
all keys: ['bg_color', 'bg_image', 'bg_mode', 'clock_color', 'date_color', 'dim', 'font', 'layout', 'reload', 'text_color', 'version', 'weather_color']
(exit 0)
```

## 2026-11-05 02:22:01 tasks/queue/007-glass-bubble.sh
```
patched: ['theme.html', 'index.html']
asked the screen to reload
== check
1
index.html:1
theme.html:1
(exit 0)
```

## 2026-11-05 02:31:01 tasks/queue/008-review-12.sh
```
TRADE REVIEW, last 12 hours: 711 (strategy, round) results from 28 rounds with full recordings.

EVERY STRATEGY (pretend money): rounds | profit | win%% | profit per $ staked
  v_x8220761      15    +253.71   67%  +21.3%
  v_x44219232     14    +239.11   64%  +25.9%
  v_x219212       18    +176.34   56%  +14.0%
  v_x44219231     14    +174.29   57%  +18.9%
  v_x72222452     15    +156.13   53%  +15.3%
  v_x28219981     22    +139.91   55%   +9.2%
  v_x88221262      5    +117.66  100%  +63.8%
  v_x80218932     11     +82.77   73%  +44.0%
  v_cut_loose     21     +80.83   62%  +14.7%
  v_late          10     +79.64   70%  +25.3%
  v_one_shot      21     +71.13   62%  +45.8%
  v_x16217722     10     +63.24   60%  +17.9%
  v_x24220782      2     +55.99  100%  +82.5%
  v_x64216771     21     +55.33   52%   +3.8%
  v_hold          21     +54.27   62%   +9.6%
  v_no_cut        21     +43.05   67%  +10.1%
  mood            23     +42.12   48%   +5.0%
  hold            27     +32.59   56%  +12.9%
  v_x24220781      2     +26.35  100%  +66.6%
  v_x36215122      7      +4.71   43%   +2.0%
  v_x88221261      2      +3.16  100%  +29.9%
  v_x64216772     21      -5.01   52%   -1.7%
  flow            22      -8.50   45%   -1.5%
  run             22     -11.61   41%   -2.0%
  trend           22     -14.71   41%   -3.3%
  signals         22     -19.50   41%   -2.8%
  distance        21     -35.65   48%  -11.6%
  v_x8220762      15     -37.95   47%   -6.7%
  v_x52220782      2     -42.40    0%  -42.4%
  v_x28219982     21     -44.61   43%   -5.2%
  v_cut_tight     21     -46.37   38%  -11.7%
  v_x52220781      3     -48.97   33%  -48.5%
  v_adds          21     -55.85   48%  -13.1%
  v_trail         21     -56.81   43%  -12.1%
  v_trail_wide    21     -56.81   43%  -12.1%
  v_x16217721     10     -71.41   40%  -10.7%
  swing           28    -123.46   36%   -8.9%
  v_x219211       18    -126.84   28%  -15.5%
  v_x72222451     15    -135.88   27%  -20.8%
  v_x36215121     16    -155.78   25%  -22.2%
  v_x80218931     11    -164.82   18%  -35.8%
  v_mood_flip     28    -316.60   43%  -14.6%
  v_flow_flip     28    -473.12   29%  -20.5%

=== 'run': 22 rounds. Total profit -11.61 ===
1) SIDE: first bet on the winning side in 10 of 22 rounds (45%). Money-weighted: 58% of dollars staked were on the winning side (coin flip = 50%).
2) TIMING: it makes its first bet a median 1:32 into the round. The cheapest price on the winning side came a median 3:06 in. Median paid 9 cents above that cheapest point when it was on the right side.
   first bet time -> rounds, profit, side right:  0-1 min: 9, +26, 5 right  |  10+ min: 1, -5, 0 right  |  1-3 min: 7, +6, 4 right  |  3-6 min: 5, -37, 1 right
3) SELLING (money made or lost by selling versus just holding those contracts to the end):
   its own odds said sell       3 sells     -52.59  selling HURT (holding would have been better)
   cut a loss                   5 sells     -12.97  selling HURT (holding would have been better)
   other                        1 sells      +6.75  selling HELPED
4) BET SIZE -> rounds, profit, wins:  $25-100: 10, -5, 4  |  under $25: 12, -7, 5
5) HOUR OF DAY -> rounds, profit:  00h: 3, +11  |  01h: 3, +95  |  14h: 1, -5  |  15h: 3, -3  |  16h: 2, +1  |  17h: 1, -6  |  20h: 3, +5  |  21h: 2, -32  |  22h: 1, -19  |  23h: 3, -59
6) HINDSIGHT: buying the winning side at its cheapest moment and holding earns an average 65 cents per contract after fees; the best swing (buy low, sell high, any side) averages 65 cents per contract. It is not achievable (nobody knows the cheapest moment); it shows how much room there is.

WORST 5 ROUNDS (when, what it did, what was best):
  Wed 21:30  -26  bet DOWN at 1:40 @49c ($47) (WRONG SIDE); result UP. best swing UP bought at 1:12 sold at 14:19, +56c/contract;  cheapest winning-side price 42c at 1:12
  Wed 23:15  -25  bet UP at 0:17 @48c ($46) (WRONG SIDE); result DOWN. best swing DOWN bought at 14:05 sold at 14:45, +85c/contract;  cheapest winning-side price 14c at 14:05
  Thu 00:00  -21  bet DOWN at 0:15 @48c ($26) (WRONG SIDE); result UP. best swing UP bought at 6:20 sold at 13:50, +62c/contract;  cheapest winning-side price 36c at 6:20
  Wed 23:30  -19  bet DOWN at 3:20 @47c ($47) (WRONG SIDE); result UP. best swing DOWN bought at 10:28 sold at 14:00, +72c/contract;  cheapest winning-side price 23c at 14:00
  Wed 22:15  -19  bet UP at 1:32 @48c ($46); result UP. best swing UP bought at 4:40 sold at 14:21, +78c/contract;  cheapest winning-side price 21c at 4:40

BEST 3 ROUNDS:
  Thu 01:15  +50  bet DOWN at 2:01 @49c ($47); result DOWN
  Thu 01:00  +30  bet UP at 0:57 @44c ($96); result UP
  Thu 00:30  +26  bet DOWN at 0:26 @48c ($48); result DOWN
(exit 0)
```

## 2026-11-05 02:31:17 tasks/queue/009-review-24.sh
```
TRADE REVIEW, last 24 hours: 1282 (strategy, round) results from 71 rounds with full recordings.

EVERY STRATEGY (pretend money): rounds | profit | win%% | profit per $ staked
  v_x8220761      15    +253.71   67%  +21.3%
  v_x44219232     14    +239.11   64%  +25.9%
  v_x219212       18    +176.34   56%  +14.0%
  v_x44219231     14    +174.29   57%  +18.9%
  v_x72222452     15    +156.13   53%  +15.3%
  v_x88221262      5    +117.66  100%  +63.8%
  v_x28219981     23     +88.49   52%   +5.5%
  v_x80218932     11     +82.77   73%  +44.0%
  v_cut_loose     53     +81.47   51%   +4.4%
  v_hold          53     +66.51   55%   +4.4%
  v_x16217722     10     +63.24   60%  +17.9%
  v_x24220782      2     +55.99  100%  +82.5%
  v_x64216771     21     +55.33   52%   +3.8%
  v_x28219982     23     +32.07   48%   +3.5%
  v_x24220781      2     +26.35  100%  +66.6%
  v_x36215122      7      +4.71   43%   +2.0%
  v_x88221261      2      +3.16  100%  +29.9%
  v_x64216772     21      -5.01   52%   -1.7%
  distance        53     -18.88   43%   -1.6%
  v_no_cut        53     -19.13   55%   -1.2%
  v_x8220762      15     -37.95   47%   -6.7%
  v_x52220782      2     -42.40    0%  -42.4%
  v_x52220781      3     -48.97   33%  -48.5%
  v_x16217721     10     -71.41   40%  -10.7%
  v_trail         53     -98.51   38%   -3.8%
  v_trail_wide    53     -98.51   38%   -3.8%
  v_x219211       18    -126.84   28%  -15.5%
  v_one_shot      52    -135.62   54%  -19.8%
  v_x72222451     15    -135.88   27%  -20.8%
  flow            56    -155.11   36%  -11.5%
  v_x36215121     16    -155.78   25%  -22.2%
  v_x80218931     11    -164.82   18%  -35.8%
  v_late          30    -165.74   47%  -10.8%
  signals         57    -194.59   33%   -9.4%
  v_cut_tight     53    -261.88   28%  -13.2%
  v_adds          53    -326.58   38%  -11.9%
  trend           60    -362.62   28%  -16.3%
  v_mood_flip     30    -365.94   40%  -15.5%
  run             54    -392.53   43%  -34.2%
  v_flow_flip     30    -394.45   30%  -15.5%
  hold            70    -536.47   37%  -47.9%
  swing           71    -584.03   31%  -16.3%
  mood            55    -599.92   35%  -17.7%

=== 'run': 54 rounds. Total profit -392.53 ===
1) SIDE: first bet on the winning side in 24 of 54 rounds (44%). Money-weighted: 38% of dollars staked were on the winning side (coin flip = 50%).
2) TIMING: it makes its first bet a median 2:08 into the round. The cheapest price on the winning side came a median 4:44 in. Median paid 15 cents above that cheapest point when it was on the right side.
   first bet time -> rounds, profit, side right:  0-1 min: 14, -48, 8 right  |  1-3 min: 18, -44, 8 right  |  10+ min: 4, -127, 1 right  |  3-6 min: 12, -120, 5 right  |  6-10 min: 6, -54, 2 right
3) SELLING (money made or lost by selling versus just holding those contracts to the end):
   its own odds said sell       3 sells     -52.59  selling HURT (holding would have been better)
   cut a loss                   5 sells     -12.97  selling HURT (holding would have been better)
   other                        1 sells      +6.75  selling HELPED
4) BET SIZE -> rounds, profit, wins:  $25-100: 19, -389, 5  |  under $25: 35, -4, 18
5) HOUR OF DAY -> rounds, profit:  00h: 3, +11  |  01h: 3, +95  |  03h: 2, -11  |  04h: 4, -29  |  05h: 4, -64  |  06h: 2, -58  |  07h: 2, -41  |  08h: 3, -182  |  09h: 3, -5  |  10h: 3, +5  |  11h: 3, +12  |  12h: 2, -10  |  13h: 3, +19  |  14h: 2, -23  |  15h: 3, -3  |  16h: 2, +1  |  17h: 1, -6  |  20h: 3, +5  |  21h: 2, -32  |  22h: 1, -19  |  23h: 3, -59
6) HINDSIGHT: buying the winning side at its cheapest moment and holding earns an average 69 cents per contract after fees; the best swing (buy low, sell high, any side) averages 68 cents per contract. It is not achievable (nobody knows the cheapest moment); it shows how much room there is.

WORST 5 ROUNDS (when, what it did, what was best):
  Wed 08:45  -84  bet UP at 0:43 @37c ($80) (WRONG SIDE); result DOWN. best swing DOWN bought at 4:50 sold at 12:27, +67c/contract;  cheapest winning-side price 31c at 4:50
  Wed 08:15  -64  bet UP at 10:14 @46c ($61) (WRONG SIDE); result DOWN. best swing DOWN bought at 11:41 sold at 14:27, +92c/contract;  cheapest winning-side price 7c at 11:41
  Wed 06:45  -63  bet DOWN at 13:05 @49c ($60) (WRONG SIDE); result UP. best swing UP bought at 9:42 sold at 14:31, +95c/contract;  cheapest winning-side price 4c at 9:42
  Wed 05:30  -56  bet UP at 3:14 @49c ($53) (WRONG SIDE); result DOWN. best swing DOWN bought at 7:58 sold at 14:54, +67c/contract;  cheapest winning-side price 31c at 7:58
  Wed 07:45  -46  bet UP at 3:02 @49c ($44) (WRONG SIDE); result DOWN. best swing DOWN bought at 11:46 sold at 14:09, +67c/contract;  cheapest winning-side price 31c at 11:46

BEST 3 ROUNDS:
  Thu 01:15  +50  bet DOWN at 2:01 @49c ($47); result DOWN
  Thu 01:00  +30  bet UP at 0:57 @44c ($96); result UP
  Wed 05:15  +27  bet UP at 6:46 @48c ($25); result UP
(exit 0)
```

## 2026-11-05 02:31:32 tasks/queue/010-learn-files.sh
```
== learn_report.json
{"time": 1793864719, "scored": 238, "adopted": false, "signals": {"book": {"n": 161, "right": 81, "pct": 50.3, "low": 39.7, "high": 60.6, "verdict": "no clear edge", "mult": 1.0, "trust": 50.1, "n_eff": 83.5}, "momentum": {"n": 193, "right": 110, "pct": 57.0, "low": 46.9, "high": 65.6, "verdict": "no clear edge", "mult": 1.16, "trust": 55.4, "n_eff": 103.7}, "whales": {"n": 94, "right": 39, "pct": 41.5, "low": 27.8, "high": 54.4, "verdict": "no clear edge", "mult": 0.8, "trust": 43.2, "n_eff": 48.6}, "bigtrades": {"n": 156, "right": 75, "pct": 48.1, "low": 41.3, "high": 61.1, "verdict": "no clear edge", "mult": 1.03, "trust": 51.0, "n_eff": 94.6}, "news": {"n": 202, "right": 97, "pct": 48.0, "low": 38.0, "high": 56.7, "verdict": "no clear edge", "mult": 0.93, "trust": 47.7, "n_eff": 105.2}, "fng": {"n": 215, "right": 110, "pct": 51.2, "low": 41.7, "high": 60.5, "verdict": "no clear edge", "mult": 1.03, "trust": 51.0, "n_eff": 104.4}, "funding": {"n": 238, "right": 122, "pct": 51.3, "low": 42.7, "high": 59.9, "verdict": "no clear edge", "mult": 1.03, "trust": 51.2, "n_eff": 126.0}, "trend_h": {"n": 196, "right": 100, "pct": 51.0, "low": 40.9, "high": 59.0, "verdict": "no clear edge", "mult": 1.0, "trust": 50.0, "n_eff": 114.2}, "trend_w": {"n": 189, "right": 91, "pct": 48.1, "low"
== exit_rules.json
{"updated": 1793867339, "rounds": 190, "source": "default", "peak": 8, "drop": 4, "enabled": false, "audit": "switched off: over 190 rounds every tested take-profit rule did worse than holding", "table": [{"peak": 20, "drop": 8, "gain": -0.0087, "se": 0.0119, "rounds": 368, "rule": -0.0291, "hold": -0.0203}, {"peak": 20, "drop": 6, "gain": -0.011, "se": 0.012, "rounds": 368, "rule": -0.0314, "hold": -0.0203}, {"peak": 15, "drop": 8, "gain": -0.0146, "se": 0.0138, "rounds": 368, "rule": -0.0349, "hold": -0.0203}, {"peak": 20, "drop": 4, "gain": -0.0146, "se": 0.0124, "rounds": 368, "rule": -0.0349, "hold": -0.0203}, {"peak": 20, "drop": 2, "gain": -0.0148, "se": 0.0123, "rounds": 368, "rule": -0.0351, "hold": -0.0203}, {"peak": 20, "drop": 3, "gain": -0.0153, "se": 0.0124, "rounds": 368, "rule": -0.0357, "hold": -0.0203}], "note": "no take-profit rule beat holding by a clear margin yet; keeping the starting guess", "exits_checked": 30, "exit_vs_hold": 0.034}
== entry_stats.json
{"updated": 1793867284, "rounds": 238, "price": {"1-20": {"n": 742, "rounds": 166, "win": 0.09, "avg": -0.0068}, "20-35": {"n": 625, "rounds": 188, "win": 0.269, "avg": -0.0179}, "35-50": {"n": 747, "rounds": 171, "win": 0.431, "avg": -0.0109}, "50-60": {"n": 538, "rounds": 154, "win": 0.53, "avg": -0.0294}, "60-70": {"n": 469, "rounds": 170, "win": 0.635, "avg": -0.0254}, "70-80": {"n": 395, "rounds": 169, "win": 0.742, "avg": -0.0153}, "80-90": {"n": 353, "rounds": 158, "win": 0.822, "avg": -0.0292}, "90-100": {"n": 465, "rounds": 138, "win": 0.946, "avg": -0.0039}}, "hours": {"0": {"n": 106, "rounds": 12, "avg": 0.0233}, "1": {"n": 105, "rounds": 11, "avg": -0.1425}, "2": {"n": 70, "rounds": 8, "avg": 0.0457}, "3": {"n": 87, "rounds": 8, "avg": -0.0401}, "4": {"n": 119, "rounds": 8, "avg": -0.0665}, "5": {"n": 113, "rounds": 8, "avg": -0.0513}, "6": {"n": 94, "rounds": 8, "avg": -0.0212}, "7": {"n": 94, "rounds": 8, "avg": 0.0209}, "8": {"n": 87, "rounds": 7, "avg": -0.0399}, "9": {"n": 111, "rounds": 8, "avg": -0.0462}, "10": {"n": 95, "rounds": 8, "avg": 0.0081}, "11": {"n": 116, "rounds": 8, "avg": -0.0162}, "12": {"n": 67, "rounds": 7, "avg": 0.0019}, "13": {"n": 88, "rounds": 8, "avg": -0.0311}, "14": {"n": 77, "rounds": 8, "avg": 0.0149}, "15": {"n": 90, "rounds": 8, "av
== patterns.json
{"updated": 1793867373, "rounds": 196, "bad": [], "good": [], "note": null, "baseline": {"train": -0.0491, "test": -0.0439}}
== config (keys with plain values only)
{'threshold': 12.0, 'min_bet': 5.0, 'cap': 0, 'edge_min': 0.03, 'max_trades': 6.0, 'slice': 0.1, 'min_price': 0.08, 'max_price': 0.92, 'aggression': 50.0, 'floor': 0, 'entry_max': 0.8, 'entry_min': 0.15}
== real (live) order slippage notes, last 8
{"t": 1793679463, "kind": "slip", "slip_cents": 0.0, "ticker": "KXBTC15M-26NOV022330-30", "action": "buy", "side": "UP"}
{"t": 1793681642, "kind": "slip", "slip_cents": 0.0, "ticker": "KXBTC15M-26NOV030000-00", "action": "buy", "side": "DOWN"}
{"t": 1793681702, "kind": "slip", "slip_cents": 0.0, "ticker": "KXBTC15M-26NOV030000-00", "action": "sell", "side": "DOWN"}
{"t": 1793681918, "kind": "slip", "slip_cents": 0.0, "ticker": "KXBTC15M-26NOV030000-00", "action": "buy", "side": "UP"}
{"t": 1793681966, "kind": "slip", "slip_cents": 0.0, "ticker": "KXBTC15M-26NOV030000-00", "action": "buy", "side": "UP"}
{"t": 1793682188, "kind": "slip", "slip_cents": 0.0, "ticker": "KXBTC15M-26NOV030015-15", "action": "buy", "side": "DOWN"}
{"t": 1793683870, "kind": "slip", "slip_cents": 0.0, "ticker": "KXBTC15M-26NOV030045-45", "action": "buy", "side": "DOWN"}
{"t": 1793683924, "kind": "slip", "slip_cents": 0.0, "ticker": "KXBTC15M-26NOV030045-45", "action": "sell", "side": "DOWN"}
(exit 0)
```

## 2026-11-05 02:34:01 tasks/queue/011-signals-and-stakes.sh
```
signals (n, right%, 95% range, verdict, weight):
  momentum       n=193  right= 57.0%  range 46.9-65.6  no clear edge      x1.16
  levels         n=159  right= 52.2%  range 42.4-63.0  no clear edge      x1.07
  trend_1h       n=108  right= 51.9%  range 40.3-62.0  no clear edge      x1.03
  funding        n=238  right= 51.3%  range 42.7-59.9  no clear edge      x1.03
  fng            n=215  right= 51.2%  range 41.7-60.5  no clear edge      x1.03
  trend_h        n=196  right= 51.0%  range 40.9-59.0  no clear edge      x1.00
  book           n=161  right= 50.3%  range 39.7-60.6  no clear edge      x1.00
  bigtrades      n=156  right= 48.1%  range 41.3-61.1  no clear edge      x1.03
  trend_w        n=189  right= 48.1%  range 38.5-57.2  no clear edge      x0.94
  news           n=202  right= 48.0%  range 38.0-56.7  no clear edge      x0.93
  trend_4h       n=98   right= 48.0%  range 35.1-58.0  no clear edge      x0.92
  trend_7d       n=94   right= 47.9%  range 36.3-59.0  no clear edge      x0.94
  trend_24h      n=110  right= 47.3%  range 37.0-58.2  no clear edge      x0.94
  whales         n=94   right= 41.5%  range 27.8-54.4  no clear edge      x0.80
other keys: ['time', 'scored', 'adopted', 'notes', 'weights']

'run' stakes by round, last 14 h (from sim_windows / trades):
no buy rows found with a cost field; first row keys:
['t', 'pnl', 'outcome', 'bal', 'src', 'hold', 'trades', 'moves', 'first', 'end', 'mix', 'sigs', 'p_open', 'staked', 'ticker', 'why', 'run', 'strat', 'hour']
(exit 0)
```

## 2026-11-05 02:37:01 tasks/queue/012-stakes.sh
```
rows: 137
Wed 20:00 staked $5.59 pnl -5.59 UP strat auto trades 1
Wed 20:15 staked $5.48 pnl 5.52 DOWN strat auto trades 1
Wed 20:30 staked $0.0 pnl 0.0 DOWN strat auto trades 0
Wed 20:45 staked $5.48 pnl 5.52 DOWN strat auto trades 1
Wed 21:00 staked $5.59 pnl -5.59 UP strat auto trades 1
Wed 21:15 staked $0.0 pnl 0.0 UP strat auto trades 0
Wed 21:30 staked $49.68 pnl -26.39 UP strat auto trades 3
Wed 21:45 staked $0.0 pnl 0.0 DOWN strat auto trades 0
Wed 22:00 staked $0.0 pnl 0.0 DOWN strat auto trades 0
Wed 22:15 staked $48.22 pnl -18.9 UP strat auto trades 4
Wed 22:30 staked $0.0 pnl 0.0 UP strat auto trades 0
Wed 22:45 staked $49.75 pnl -28.52 DOWN strat auto trades 4
Wed 23:00 staked $36.63 pnl -15.53 DOWN strat auto trades 3
Wed 23:15 staked $48.26 pnl -24.68 DOWN strat auto trades 5
Wed 23:30 staked $49.83 pnl -19.09 UP strat auto trades 5
Wed 23:45 staked $0.0 pnl 0.0 DOWN strat auto trades 0
Thu 00:00 staked $20.3 pnl -20.3 UP strat auto trades 1
Thu 00:15 staked $0.0 pnl 0.0 UP strat auto trades 0
Thu 00:30 staked $49.71 pnl 25.65 DOWN strat auto trades 3
Thu 00:45 staked $19.85 pnl 6.15 UP strat auto trades 1
Thu 01:00 staked $49.71 pnl 30.02 UP strat auto trades 5
Thu 01:15 staked $49.55 pnl 50.45 DOWN strat auto trades 2
Thu 01:30 staked $49.66 pnl 14.34 DOWN strat auto trades 2
Thu 01:45 staked $49.6 pnl -10.09 DOWN strat auto trades 6
max staked, last 14h: $49.83
(exit 0)
```
