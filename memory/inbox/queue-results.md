"assistant" else "user", "text": str(m.get("text", ""))[:3000], "changes": [str(c)[:200] for c in (m.get("changes") if isinstance(m.get("chang
                 for m in (b.get("chat") if isinstance(b.get("chat"), list) else [])[-60:] if isinstance(m, dict)]
    return d
== interior()
def interior(b, path):
    I = b["inside"]; pages = b["pages"]; W, H = SPEC["trim_w"] * IN, SPEC["trim_h"] * IN
    c = canvas.Canvas(path, pagesize=(W, H), initialFontName=fn(I["font"])); c.setTitle(b["title"] or b["name"])
    inner = max(I["inner"], gutter(pages)); outer = I["outer"]
    kinds = plan(b); fam = I["font"]; col = HexColor(I["color"]); sp = I["spacing"] * IN
    for n, kind in enumerate(kinds, 1):
        odd = n % 2 == 1; L = (inner if odd else outer) * IN; R = W - (outer if odd else inner) * IN
        top = H - I["top"] * IN; bot = I["bottom"] * IN
        if I["page_bg"].lower() != "#ffffff":
            c.setFillColor(HexColor(I["page_bg"])); c.rect(0, 0, W, H, fill=1, stroke=0)
        c.setFillColor(col)
        def label(t, y, size=11, bold=False, x=L):
            c.setFont(fn(fam, bold), size); c.drawString(x, y, t)
        def ruled(y0, y1):
            c.setStrokeColor(HexColor(I["line_color"])); c.setFillColor(HexColor(I["line_color"])); c.setLineWidth(I["line_width"])
            if I["dash"]: c.setDash(2, 2)
            y = y0
            if I["style"] == "lines":
                while y >= y1: c.line(L, y, R, y); y -= sp
            elif I["style"] == "grid":
                while y >= y1: c.line(L, y, R, y); y -= sp
                x = L
                while x <= R + 0.1: c.line(x, y0, x, y + sp); x += sp
            elif I["style"] == "dots":
                while y >= y1:
                    x = L
                    while x <= R + 0.1: c.circle(x, y, max(.4, I["line_width"] * .8), stroke=0, fill=1); x += sp
                    y -= sp
            c.setDash()
        y0 = top
        if kind == "title":
            c.setFont(fn(fam, True), 26)
            for i, l in enumerate(simpleSplit(b["title"], fn(fam, True), 26, R - L)): c.drawCentredString((L + R) / 2, H * .62 - i * 32, l)
            c.setFont(fn(fam), 13)
            if b["subtitle"]: c.drawCentredString((L + R) / 2, H * .62 - 70, b["subtitle"])
            if b["author"]: c.drawCentredString((L + R) / 2, H *(exit 0)
```

## 2026-11-05 15:01:01 tasks/queue/027-kdp-fonts.sh
```
studio fonts (13):
Bitstream Vera, Caladea, Carlito, DejaVu Sans, DejaVu Serif, FreeSans, FreeSerif, Lato, Liberation Mono, Liberation Sans, Liberation Serif, Open Sans, Roboto
== other fonts on the system
Abril Fatface;Allerta Stencil;Allura;Audiowide;Bangers;Bebas Neue,Bebas Neue Bold;Bebas Neue,Bebas Neue Book;Bebas Neue,Bebas Neue Light;Bebas Neue,Bebas Neue Regular;Bebas Neue,Bebas Neue Thin;Black Ops One;Boogaloo;Bubblegum Sans;Bungee;Butcherman;C059;Caladea;Cantarell;Carlito;Caveat;Chelsea Market;Chewy;Cinzel;Comfortaa;Comfortaa,Comfortaa Light;Creepster;D050000L;DejaVu Math TeX Gyre;DejaVu Sans;DejaVu Sans,DejaVu Sans Condensed;DejaVu Sans,DejaVu Sans Light;DejaVu Sans Mono;DejaVu Serif;DejaVu Serif,DejaVu Serif Condensed;Droid Sans Fallback;Eater;Fira Code;Fira Code,Fira Code Light;Fira Code,Fira Code Medium;Fira Code,Fira Code Retina;Fira Code,Fira Code SemiBold;Fontdiner Swanky;FreeMono;FreeSans;FreeSerif;Frijole;GFS Didot Classic;Gochi Hand;Great Vibes;Griffy;Hack;IBM Plex Mono;IBM Plex Mono,IBM Plex Mono ExtLt;IBM Plex Mono,IBM Plex Mono Light;IBM Plex Mono,IBM Plex Mono Medm;IBM Plex Mono,IBM Plex Mono SmBld;IBM Plex Mono,IBM Plex Mono Text;IBM Plex Mono,IBM Plex Mono Thin;IBM Plex Sans;IBM Plex Sans Arabic;

== can reach GitHub raw?
200
(exit 0)
```

## 2026-11-05 15:01:02 tasks/queue/028-kdp-copy-engine.sh
```
total 88
drwxrwxr-x 2 kylarlovelady kylarlovelady  4096 Nov  5 15:01 .
drwxrwxr-x 3 kylarlovelady kylarlovelady  4096 Nov  5 15:01 ..
-rw-r--r-- 1 kylarlovelady kylarlovelady 25292 Nov  5 15:01 app.py
-rw-r--r-- 1 kylarlovelady kylarlovelady  9588 Nov  5 15:01 book-current.json
-rw-r--r-- 1 kylarlovelady kylarlovelady  1411 Nov  5 15:01 book-old.json
-rw-r--r-- 1 kylarlovelady kylarlovelady 33061 Nov  5 15:01 engine.py
(exit 0)
```

## 2026-11-05 15:04:01 tasks/queue/029-home-voice-diag.sh
```
== services
hub-satellite: active
hub-voice: active
phone-voice: active
hub-dashboard: active
hub-watchdog: active
== containers
openwakeword Up 6 days
whisper Up 6 days (healthy)
piper Up 6 days (healthy)
pihole Up 19 hours (healthy)
homeassistant Up 13 hours
== hub-satellite log (last 25)
Nov 05 14:56:55 LoveladyMainAiHub bash[2546920]: WARNING:root:Mic service disconnected
Nov 05 14:57:38 LoveladyMainAiHub bash[2546920]: INFO:root:Waiting for wake word
Nov 05 14:58:19 LoveladyMainAiHub systemd[1]: Stopping hub-satellite.service - Wyoming satellite (main hub)...
Nov 05 14:58:19 LoveladyMainAiHub systemd[1]: hub-satellite.service: Deactivated successfully.
Nov 05 14:58:19 LoveladyMainAiHub systemd[1]: Stopped hub-satellite.service - Wyoming satellite (main hub).
Nov 05 14:58:19 LoveladyMainAiHub systemd[1]: hub-satellite.service: Consumed 1h 31min 37.976s CPU time.
Nov 05 14:58:19 LoveladyMainAiHub systemd[1]: Started hub-satellite.service - Wyoming satellite (main hub).
Nov 05 14:58:19 LoveladyMainAiHub bash[2665352]: INFO:root:Ready
Nov 05 14:58:20 LoveladyMainAiHub bash[2665352]: INFO:root:Connected to services
Nov 05 14:58:32 LoveladyMainAiHub bash[2665352]: INFO:root:Connected to server
Nov 05 14:58:32 LoveladyMainAiHub bash[2665352]: INFO:root:Waiting for wake word
Nov 05 14:58:52 LoveladyMainAiHub bash[2665352]: INFO:root:Waiting for wake word
Nov 05 14:58:55 LoveladyMainAiHub bash[2666912]: Playing raw data 'stdin' : Signed 16 bit Little Endian, Rate 22050 Hz, Mono
Nov 05 15:00:18 LoveladyMainAiHub bash[2665352]: INFO:root:Waiting for wake word
Nov 05 15:00:20 LoveladyMainAiHub bash[2670871]: Playing raw data 'stdin' : Signed 16 bit Little Endian, Rate 22050 Hz, Mono
Nov 05 15:00:51 LoveladyMainAiHub bash[2665352]: INFO:root:Waiting for wake word
Nov 05 15:01:35 LoveladyMainAiHub systemd[1]: Stopping hub-satellite.service - Wyoming satellite (main hub)...
Nov 05 15:01:35 LoveladyMainAiHub systemd[1]: hub-satellite.service: Deactivated successfully.
Nov 05 15:01:35 LoveladyMainAiHub systemd[1]: Stopped hub-satellite.service - Wyoming satellite (main hub).
Nov 05 15:01:35 LoveladyMainAiHub systemd[1]: hub-satellite.service: Consumed 2.083s CPU time.
Nov 05 15:01:35 LoveladyMainAiHub systemd[1]: Started hub-satellite.service - Wyoming satellite (main hub).
Nov 05 15:01:36 LoveladyMainAiHub bash[2674286]: INFO:root:Ready
Nov 05 15:01:36 LoveladyMainAiHub bash[2674286]: INFO:root:Connected to services
Nov 05 15:01:48 LoveladyMainAiHub bash[2674286]: INFO:root:Connected to server
Nov 05 15:01:48 LoveladyMainAiHub bash[2674286]: INFO:root:Waiting for wake word
== hub-voice log (last 15)
-- No entries --
== phone-voice errors today
Nov 05 15:00:53 LoveladyMainAiHub python[692834]: Exception occurred during processing of request from ('127.0.0.1', 40060)
Nov 05 15:00:53 LoveladyMainAiHub python[692834]: Traceback (most recent call last):
Nov 05 15:00:53 LoveladyMainAiHub python[692834]: BrokenPipeError: [Errno 32] Broken pipe
Nov 05 15:00:53 LoveladyMainAiHub python[692834]: During handling of the above exception, another exception occurred:
Nov 05 15:00:53 LoveladyMainAiHub python[692834]: Traceback (most recent call last):
Nov 05 15:00:53 LoveladyMainAiHub python[692834]:     except Exception as e: return self._send(500, {"error": str(e)[:200]})
Nov 05 15:00:53 LoveladyMainAiHub python[692834]: BrokenPipeError: [Errno 32] Broken pipe
== HA log, jarvis/assist/wake lines
[36m2026-11-05 14:57:38.136 DEBUG (MainThread) [homeassistant.components.conversation.chat_log] Adding user content: UserContent(role='user', content=' What do you know about Shari?', attachments=None, created=datetime.datetime(2026, 11, 5
[36m2026-11-05 14:58:52.352 DEBUG (MainThread) [homeassistant.components.conversation.chat_log] Adding user content: UserContent(role='user', content=' What do you know about Shari?', attachments=None, created=datetime.datetime(2026, 11, 5
[36m2026-11-05 14:58:54.445 DEBUG (MainThread) [homeassistant.components.conversation.chat_log] Chat Log opened but no assistant message was added, ignoring update[0m
[36m2026-11-05 15:00:18.370 DEBUG (MainThread) [homeassistant.components.conversation.chat_log] Adding user content: UserContent(role='user', content=' What can you tell me about Shari?', attachments=None, created=datetime.datetime(2026, 1
[36m2026-11-05 15:00:19.925 DEBUG (MainThread) [homeassistant.components.conversation.chat_log] Chat Log opened but no assistant message was added, ignoring update[0m
[36m2026-11-05 15:00:51.274 DEBUG (MainThread) [homeassistant.components.conversation.chat_log] Adding user content: UserContent(role='user', content=' Do you know who I am?', attachments=None, created=datetime.datetime(2026, 11, 5, 21, 0,
== jarvis trace, last 14 events
05:54:45 sentence {'sid': 'phes14a5', 'n': 0, 'text': "Sounds good! Glad to chat, and I’ll be ready for tomorrow's fixes.", 'tts_secs': 0.43, 'since
05:54:45 state {'sid': 'phes14a5', 'frm': 'thinking', 'to': 'speaking', 'why': ''}
05:54:46 sentence {'sid': 'phes14a5', 'n': 1, 'text': 'Have a great evening!', 'tts_secs': 0.3, 'since_heard': 1.5}
05:54:46 client {'sid': 'phes14a5', 'what': 'play_start', 'info': ''}
05:54:50 client {'sid': 'phes14a5', 'what': 'play_end', 'info': ''}
05:54:50 client {'sid': 'phes14a5', 'what': 'play_start', 'info': ''}
05:54:52 client {'sid': 'phes14a5', 'what': 'play_end', 'info': ''}
05:54:52 state {'sid': 'phes14a5', 'frm': 'speaking', 'to': 'follow', 'why': 'he finished talking'}
05:54:56 hangup {'sid': 'phes14a5', 'why': 'you ended it', 'after': 3.3, 'state': 'follow'}
05:54:56 state {'sid': 'phes14a5', 'frm': 'follow', 'to': 'idle', 'why': 'hung up: you ended it'}
05:55:02 client {'sid': 'phes14a5', 'what': 'page_hidden', 'info': ''}
13:53:20 client {'sid': 'phtnri1w', 'what': 'page_hidden', 'info': ''}
13:53:49 client {'sid': 'phtnri1w', 'what': 'page_visible', 'info': ''}
13:53:51 client {'sid': 'phtnri1w', 'what': 'page_hidden', 'info': ''}
(exit 0)
```

## 2026-11-05 15:04:01 tasks/queue/030-popup-font.sh
```
== files
  
4096 11-05_14:57 .
4096 11-05_04:28 ..
4096 11-04_14:52 backgrounds
4348 10-20_20:23 crop_api.py
1147 10-26_22:14 device-names.json
138 10-26_22:11 device-names.json.bak-oct26
4096 10-20_21:15 fontcache
1841 10-25_22:21 health_api.py
3025 10-26_22:23 hub_api.py
2913 10-22_16:25 hub_api.py.bak-jh
2949 10-26_22:23 hub_api.py.bak-names
11098 11-05_03:04 hub.html
7400 10-30_14:51 hub.html.bak-cr
8936 10-30_15:25 hub.html.bak-crop
8936 10-30_15:20 hub.html.bak-dbg
8992 10-30_15:28 hub.html.bak-ha
7093 10-25_22:22 hub.html.bak-hl
7550 10-30_15:01 hub.html.bak-imm
8850 10-30_15:10 hub.html.bak-imm2
7291 10-25_23:00 hub.html.bak-ly
10776 11-02_00:51 hub.html.bak-markets
8920 10-30_15:35 hub.html.bak-merge
10449 10-30_15:43 hub.html.bak-sheet
9377 11-05_02:22 index.html
8143 11-05_02:22 index.html.bak-glass
7351 10-25_23:00 index.html.bak-ly
8072 10-25_23:19 index.html.bak-ly2
4896 10-23_11:48 janitor_api.py
7216 10-23_11:48 janitor.html
== settings (font/theme keys only)
{'font': 'Great Vibes', 'text_color': '#000000'}
== reply popup code in index.html
62:  else if(m.name==='transcript'){$('you').textContent=m.text;show('thinking','Thinking');hideLater(30000);}
== font rules in theme.html / index.html
theme.html:16:var bu=g('bubble');if(bu){if(s.glass===false){bu.style.cssText='background:none;border:0;box-shadow:none;-webkit-backdrop-filter:none;backdrop-filter:none;padding:0';}
index.html:8: font-family:"Segoe UI",system-ui,sans-serif;height:100vh;overflow:hidden;display:flex;
index.html:10:#clock{font-size:15vw;font-weight:200;letter-spacing:.02em;color:var(--cyan);
index.html:12:#date{font-size:2.6vw;color:var(--dim);letter-spacing:.2em;text-transform:uppercase;margin-bottom:4vh}
index.html:13:#wx{display:flex;gap:4vw;align-items:baseline;font-size:2.4vw;color:var(--dim)}
index.html:14:#temp{font-size:7vw;font-weight:200;color:#e8f4ff}
index.html:15:#cond{font-size:3vw;color:#e8f4ff}
index.html:18: box-shadow:0 0 40px rgba(56,232,255,.2);backdrop-filter:blur(12px);
index.html:21:#status{display:flex;align-items:center;gap:1.2vw;font-size:2vw;letter-spacing:.2em;
index.html:27:.lbl{font-size:1.7vw;color:var(--dim);text-transform:uppercase;letter-spacing:.15em}
index.html:28:#you{font-size:2.6vw;color:var(--cyan);min-height:3.4vw;margin-bottom:1.5vh}
index.html:29:#ai{font-size:3vw;line-height:1.3;min-height:4vw}
index.html:32: border:1px solid rgba(255,255,255,.6);-webkit-backdrop-filter:blur(26px) saturate(1.7);backdrop-filter:blur(26px) saturate(1.7);
index.html:121:var bu=g('bubble');if(bu){if(s.glass===false){bu.style.cssText='background:none;border:0;box-shadow:none;-webkit-backdrop-filter:none;backdrop-filter:none;padding:0';}
(exit 0)
```

## 2026-11-05 15:07:01 tasks/queue/031-home-ask-test.sh
```
== last 10 text asks (home/Siri) from the log
23:32:38 secs None | None -> None | times None
23:32:39 secs 1.2 | Hey, can you hear me? -> Yes, I can hear you. What do you need? | times None
23:33:05 secs None | None -> None | times None
23:48:28 secs None | None -> None | times None
23:48:32 secs 3.7 | What's on my to-do list? -> 1. Redo Kalshi API location verification by Nov 9.
2. Decide on ElevenLabs renewal by Nov  | times None
00:56:28 secs 1.1 | say hello -> Hello, Kylar! How's it going? | times {'llm': 1.05}
01:49:03 secs 2.1 | how is the pi doing -> The Pi is up for 1 week, 3 days, and has a temperature of 40.0°C, with 58% memory usage an | times {'llm': 2.07}
14:58:54 secs 2.1 | What do you know about Shari? -> I don't have any information on someone named Shari. Would you like to tell me who she is? | times {'llm': 2.08}
15:00:19 secs 1.5 | What can you tell me about Shari? -> I don't have any details about Shari in my records. If she's someone important, feel free  | times {'llm': 1.55}
15:00:53 secs 2.2 | Do you know who I am? -> Yes, you're Kylar Lovelady. You work nights at Dow, and you're focused on income projects  | times {'llm': 2.17}
== live timing test
What time is it -> 1.2s: {"reply": "I can't check the current time. You can look at your phone or dashboard for that.", "end": false, "followup": false}
What do you know about Sheree -> 1.0s: {"reply": "I don't have any specific information about Sheree. Could you clarify who she is?", "end": false, "followup": true}
== HA jarvis_hub warnings (6h)
== watchdog log (satellite restarts)
Nov 04 19:42:20 LoveladyMainAiHub python3[35465]: pihole dns dead, restarting
Nov 04 19:43:17 LoveladyMainAiHub python3[35465]: pihole dns dead, restarting
Nov 04 19:44:14 LoveladyMainAiHub python3[35465]: pihole dns dead, restarting
Nov 04 19:45:10 LoveladyMainAiHub python3[35465]: pihole dns dead, restarting
Nov 04 19:46:07 LoveladyMainAiHub python3[35465]: pihole dns dead, restarting
Nov 04 19:47:04 LoveladyMainAiHub python3[35465]: pihole dns dead, restarting
Nov 04 19:48:00 LoveladyMainAiHub python3[35465]: pihole dns dead, restarting
Nov 04 19:48:57 LoveladyMainAiHub python3[35465]: pihole dns dead, restarting
Nov 04 19:49:51 LoveladyMainAiHub python3[35465]: pihole dns dead, restarting
Nov 04 19:50:15 LoveladyMainAiHub python3[35465]: pihole dns dead, restarting
Nov 05 14:58:19 LoveladyMainAiHub python3[35465]: stuck in listening for 40s, restarting satellite
Nov 05 15:01:35 LoveladyMainAiHub python3[35465]: stuck in listening for 44s, restarting satellite
(exit 0)
```

## 2026-11-05 15:07:03 tasks/queue/032-home-timeline.sh
```
== satellite unit
ExecStart=/bin/bash /home/kylarlovelady/wyoming-satellite/run-hub.sh
Restart=always
RestartSec=3
== watchdog unit
ExecStart=/usr/bin/python3 /usr/local/bin/hub-watchdog.py
== HA voice pipeline events (last 90 min)
2026-11-05 14:57:38.136 DEBUG (MainThread) [homeassistant.components.conversation.chat_log] Adding user content: UserContent(role='user', content=' What do you know about Shari?', attachments=None, created=date
2026-11-05 14:58:52.352 DEBUG (MainThread) [homeassistant.components.conversation.chat_log] Adding user content: UserContent(role='user', content=' What do you know about Shari?', attachments=None, created=date
2026-11-05 14:58:54.445 DEBUG (MainThread) [homeassistant.components.conversation.chat_log] Chat Log opened but no assistant message was added, ignoring update
2026-11-05 15:00:18.370 DEBUG (MainThread) [homeassistant.components.conversation.chat_log] Adding user content: UserContent(role='user', content=' What can you tell me about Shari?', attachments=None, created=
2026-11-05 15:00:19.925 DEBUG (MainThread) [homeassistant.components.conversation.chat_log] Chat Log opened but no assistant message was added, ignoring update
2026-11-05 15:00:51.274 DEBUG (MainThread) [homeassistant.components.conversation.chat_log] Adding user content: UserContent(role='user', content=' Do you know who I am?', attachments=None, created=datetime.dat
(exit 0)
```

## 2026-11-05 15:10:01 tasks/queue/033-satellite-settings.sh
```
== run-hub.sh
#!/bin/bash
cd ~/wyoming-satellite
script/run \
--name 'main hub' \
--uri 'tcp://127.0.0.1:10700' \
--mic-command '/home/kylarlovelady/hub-mic.py plughw:3,0' \
--snd-command 'aplay -D plughw:2,0 -r 22050 -c 1 -f S16_LE -t raw' \
--wake-uri 'tcp://127.0.0.1:10400' \
--wake-word-name 'hey_jarvis' \
--detect-command 'bash -c "echo idle > /tmp/hub-state"' \
--detection-command 'bash -c "pkill -x aplay; echo listening > /tmp/hub-state; curl -s -m 2 -X POST -d wake http://127.0.0.1:8080/event/wake > /dev/null"' \
--stt-stop-command 'bash -c "echo thinking > /tmp/hub-state"' \
--transcript-command 'bash -c "curl -s -m 2 -X POST --data-binary @- http://127.0.0.1:8080/event/transcript > /dev/null"' \
--synthesize-command 'bash -c "curl -s -m 2 -X POST --data-binary @- http://127.0.0.1:8080/event/synthesize > /dev/null"' \
--tts-start-command 'bash -c "echo speaking > /tmp/hub-state"' \
--tts-stop-command 'bash -c "echo idle > /tmp/hub-state; curl -s -m 2 -X POST -d done http://127.0.0.1:8080/event/done > /dev/null"' \
--error-command 'bash -c "echo idle > /tmp/hub-state"'
== wyoming-satellite version / options
CHANGELOG.md
docker
docker-compose.yml
Dockerfile
docs
etc
examples
installer
LICENSE.md
mypy.ini
pylintrc
pyproject.toml
README.md
run-hub.sh
run-hub.sh.bak
run-hub.sh.bak2
run-hub.sh.bak-alexa
run-hub.sh.bak-lock
script
setup.cfg
  --mic-uri MIC_URI     URI of Wyoming microphone service
  --mic-command MIC_COMMAND
  --mic-command-rate MIC_COMMAND_RATE
  --mic-command-width MIC_COMMAND_WIDTH
  --mic-command-channels MIC_COMMAND_CHANNELS
  --mic-command-samples-per-chunk MIC_COMMAND_SAMPLES_PER_CHUNK
  --mic-volume-multiplier MIC_VOLUME_MULTIPLIER
  --mic-noise-suppression {0,1,2,3,4}
  --mic-auto-gain {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31}
  --mic-seconds-to-mute-after-awake-wav MIC_SECONDS_TO_MUTE_AFTER_AWAKE_WAV
  --mic-no-mute-during-awake-wav
  --mic-channel-index MIC_CHANNEL_INDEX
  --snd-uri SND_URI     URI of Wyoming sound service
  --snd-command SND_COMMAND
  --snd-command-rate SND_COMMAND_RATE
  --snd-command-width SND_COMMAND_WIDTH
  --snd-command-channels SND_COMMAND_CHANNELS
  --snd-volume-multiplier SND_VOLUME_MULTIPLIER
  --wake-uri WAKE_URI   URI of Wyoming wake word detection service
  --wake-word-name name [pipeline ...]
  --wake-command WAKE_COMMAND
  --wake-command-rate WAKE_COMMAND_RATE
  --wake-command-width WAKE_COMMAND_WIDTH
  --wake-command-channels WAKE_COMMAND_CHANNELS
  --wake-refractory-seconds WAKE_REFRACTORY_SECONDS
  --vad                 Wait for speech before streaming audio
  --vad-threshold VAD_THRESHOLD
  --vad-trigger-level VAD_TRIGGER_LEVEL
  --vad-buffer-seconds VAD_BUFFER_SECONDS
  --vad-wake-word-timeout VAD_WAKE_WORD_TIMEOUT
  --timer-started-command TIMER_STARTED_COMMAND
  --timer-updated-command TIMER_UPDATED_COMMAND
  --timer-cancelled-command, --timer-canceled-command TIMER_CANCELLED_COMMAND
  --timer-finished-command TIMER_FINISHED_COMMAND
  --awake-wav AWAKE_WAV
  --done-wav DONE_WAV   WAV file to play when voice command is done
  --timer-finished-wav TIMER_FINISHED_WAV
  --timer-finished-wav-repeat repeat delay
  --no-zeroconf         Disable discovery over zeroconf
  --debug-recording-dir DEBUG_RECORDING_DIR
== watchdog: stuck rule
4:STATE = "/tmp/hub-state"
6:LIMITS = {"listening": 40, "thinking": 60, "speaking": 120}
9:last_restart = 0
34:            log("restarting " + svc)
35:            run("systemctl", "restart", svc)
38:        r = run("docker", "inspect", "-f", "{{.State.Running}} {{if .State.Health}}{{.State.Health.Status}}{{end}}", c)
46:            log("restarting unhealthy " + c)
47:            run("docker", "restart", c)
50:        state = open(STATE).read().strip()
51:        age = now - os.stat(STATE).st_mtime
52:        if state in LIMITS and age > LIMITS[state] and now - last_restart > 60:
53:            problems.append("stuck " + state)
54:            log("stuck in %s for %ds, restarting satellite" % (state, age))
55:            run("systemctl", "restart", "hub-satellite")
56:            open(STATE, "w").write("idle")
57:            last_restart = now
62:        if run("docker", "inspect", "-f", "{{.State.Running}}", "pihole").stdout.strip() == "true":
70:                    log("pihole dns dead, restarting")
71:                    run("docker", "restart", "pihole")
88:    time.sleep(10)
== mic device and level
**** List of CAPTURE Hardware Devices ****
card 3: AC44 [MXL AC-44], device 0: USB Audio [USB Audio]
  Subdevices: 0/1
  Subdevice #0: subdevice #0
(exit 0)
```

## 2026-11-05 15:13:01 tasks/queue/034-home-mic-setup.sh
```
== options present?
                   [--mic-noise-suppression {0,1,2,3,4}]
                   [--debug-recording-dir DEBUG_RECORDING_DIR] [--debug]
  --mic-noise-suppression {0,1,2,3,4}
  --debug-recording-dir DEBUG_RECORDING_DIR
== hub-mic.py (gain/level lines)
6:def stop(*a):
added: ["--debug-recording-dir '/home/kylarlovelady/voice-data/home-mic' \\", '--mic-noise-suppression 2 \\']
syntax ok
== satellite now
activating
Nov 05 15:13:08 LoveladyMainAiHub bash[2706041]:     raise CalledProcessError(retcode, cmd)
Nov 05 15:13:08 LoveladyMainAiHub bash[2706041]: subprocess.CalledProcessError: Command '['/home/kylarlovelady/wyoming-satellite/.venv/bin/python3', '-m', 'wyom
Nov 05 15:13:08 LoveladyMainAiHub systemd[1]: hub-satellite.service: Main process exited, code=exited, status=1/FAILURE
Nov 05 15:13:08 LoveladyMainAiHub systemd[1]: hub-satellite.service: Failed with result 'exit-code'.
# Home speaker mic report (auto, stats only; audio stays on the Pi)

floor = background noise level (16-bit scale, 0 to 32767); speech% = share of the clip louder than 3x the floor; tail quiet = seconds of quiet at the end (end-of-speech needs about 1 s).

No clips yet: the satellite recording folder is empty or recording is not switched on.

## Satellite restarts by the watchdog (last 24 h)
Nov 05 14:58:19 LoveladyMainAiHub python3[35465]: stuck in listening for 40s, restarting satellite
(exit 0)
```

## 2026-11-05 15:16:01 tasks/queue/035-satellite-rollback.sh
```
== why it failed (last error lines)
Nov 05 15:15:57 LoveladyMainAiHub bash[2713529]: Extras for webrtc are not installed
Nov 05 15:15:57 LoveladyMainAiHub bash[2713529]:     import webrtc_noise_gain  # noqa: F401
Nov 05 15:15:57 LoveladyMainAiHub bash[2713529]: ModuleNotFoundError: No module named 'webrtc_noise_gain'
Nov 05 15:16:01 LoveladyMainAiHub bash[2713669]:     raise CalledProcessError(retcode, cmd)
Nov 05 15:16:01 LoveladyMainAiHub bash[2713669]: subprocess.CalledProcessError: Command '['/home/kylarlovelady/wyoming-satellite/.venv/bin/python3', '-m', 'wyoming_satellite', '--name', 'main hub', '--debug-recording-dir
Nov 05 15:16:01 LoveladyMainAiHub bash[2713670]: Extras for webrtc are not installed
Nov 05 15:16:01 LoveladyMainAiHub bash[2713670]:     import webrtc_noise_gain  # noqa: F401
Nov 05 15:16:01 LoveladyMainAiHub bash[2713670]: ModuleNotFoundError: No module named 'webrtc_noise_gain'
restored working run-hub.sh
== satellite now
active
Nov 05 15:16:04 LoveladyMainAiHub systemd[1]: Started hub-satellite.service - Wyoming satellite (main hub).
Nov 05 15:16:04 LoveladyMainAiHub bash[2713975]: INFO:root:Ready
Nov 05 15:16:04 LoveladyMainAiHub bash[2713975]: INFO:root:Connected to services
Nov 05 15:16:06 LoveladyMainAiHub bash[2713975]: INFO:root:Connected to server
Nov 05 15:16:06 LoveladyMainAiHub bash[2713975]: INFO:root:Waiting for wake word
(exit 0)
```

## 2026-11-05 15:19:01 tasks/queue/036-home-mic-record-only.sh
```
recording flag added
NOT healthy: rolled back
active
Nov 05 15:19:19 LoveladyMainAiHub systemd[1]: Started hub-satellite.service - Wyoming satellite (main hub).
Nov 05 15:19:19 LoveladyMainAiHub bash[2722919]: INFO:root:Ready
Nov 05 15:19:19 LoveladyMainAiHub bash[2722919]: INFO:root:Connected to services
(exit 0)
```

## 2026-11-05 17:04:01 tasks/queue/037-home-mic-record-only.sh
```
recording flag added
NOT healthy: rolled back
active
Nov 05 17:04:39 LoveladyMainAiHub systemd[1]: Started hub-satellite.service - Wyoming satellite (main hub).
Nov 05 17:04:39 LoveladyMainAiHub bash[3005072]: INFO:root:Ready
Nov 05 17:04:40 LoveladyMainAiHub bash[3005072]: INFO:root:Connected to services
(exit 0)
```

## 2026-11-05 17:10:01 tasks/queue/038-home-mic-record-diagnose.sh
```
4:--name 'main hub' \
#!/bin/bash
cd ~/wyoming-satellite
script/run \
--name 'main hub' \
--debug-recording-dir '/home/kylarlovelady/voice-data/home-mic' \
--uri 'tcp://127.0.0.1:10700' \
--mic-command '/home/kylarlovelady/hub-mic.py plughw:3,0' \
--snd-command 'aplay -D plughw:2,0 -r 22050 -c 1 -f S16_LE -t raw' \
--wake-uri 'tcp://127.0.0.1:10400' \
--wake-word-name 'hey_jarvis' \
--detect-command 'bash -c "echo idle > /tmp/hub-state"' \
--detection-command 'bash -c "pkill -x aplay; echo listening > /tmp/hub-state; curl -s -m 2 -X POST -d wake http://127.0.0.1:8080/event/wake > /dev/null"' \
--stt-stop-command 'bash -c "echo thinking > /tmp/hub-state"' \
--transcript-command 'bash -c "curl -s -m 2 -X POST --data-binary @- http://127.0.0.1:8080/event/transcript > /dev/null"' \
--synthesize-command 'bash -c "curl -s -m 2 -X POST --data-binary @- http://127.0.0.1:8080/event/synthesize > /dev/null"' \
--tts-start-command 'bash -c "echo speaking > /tmp/hub-state"' \
--tts-stop-command 'bash -c "echo idle > /tmp/hub-state; curl -s -m 2 -X POST -d done http://127.0.0.1:8080/event/done > /dev/null"' \
--error-command 'bash -c "echo idle > /tmp/hub-state"'
Nov 05 17:10:01 LoveladyMainAiHub bash[3005068]: Traceback (most recent call last):
Nov 05 17:10:01 LoveladyMainAiHub bash[3005068]:   File "/home/kylarlovelady/wyoming-satellite/script/run", line 12, in <module>
Nov 05 17:10:01 LoveladyMainAiHub bash[3005068]:     subprocess.check_call([context.env_exe, "-m", "wyoming_satellite"] + sys.argv[1:])
Nov 05 17:10:01 LoveladyMainAiHub bash[3005068]:     ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Nov 05 17:10:01 LoveladyMainAiHub bash[3005068]:   File "/usr/lib/python3.13/subprocess.py", line 419, in check_call
Nov 05 17:10:01 LoveladyMainAiHub bash[3005068]:     raise CalledProcessError(retcode, cmd)
Nov 05 17:10:01 LoveladyMainAiHub bash[3005068]: subprocess.CalledProcessError: Command '['/home/kylarlovelady/wyoming-satellite/.venv/bin/python3', '-m', 'wyoming_satellite', '--name', 'main hub', '-
Nov 05 17:10:01 LoveladyMainAiHub bash[3005067]: /home/kylarlovelady/wyoming-satellite/run-hub.sh: line 19: unexpected EOF while looking for matching `"'
Nov 05 17:10:01 LoveladyMainAiHub systemd[1]: hub-satellite.service: Main process exited, code=exited, status=1/FAILURE
Nov 05 17:10:01 LoveladyMainAiHub systemd[1]: hub-satellite.service: Failed with result 'exit-code'.
Nov 05 17:10:01 LoveladyMainAiHub systemd[1]: hub-satellite.service: Consumed 2.431s CPU time.
Nov 05 17:10:05 LoveladyMainAiHub systemd[1]: hub-satellite.service: Scheduled restart job, restart counter is at 5.
Nov 05 17:10:05 LoveladyMainAiHub systemd[1]: Started hub-satellite.service - Wyoming satellite (main hub).
Nov 05 17:10:05 LoveladyMainAiHub bash[3020155]: INFO:root:Recording audio to /home/kylarlovelady/voice-data/home-mic
Nov 05 17:10:05 LoveladyMainAiHub bash[3020155]: INFO:root:Ready
Nov 05 17:10:05 LoveladyMainAiHub bash[3020155]: INFO:root:Connected to services
Nov 05 17:10:14 LoveladyMainAiHub bash[3020155]: INFO:root:Connected to server
Nov 05 17:10:14 LoveladyMainAiHub bash[3020155]: INFO:root:Waiting for wake word
total 8
drwxrwxr-x 2 kylarlovelady kylarlovelady 4096 Nov  5 17:10 .
drwx------ 5 kylarlovelady kylarlovelady 4096 Nov  5 15:13 ..
-rw-r--r-- 1 kylarlovelady kylarlovelady    0 Nov  5 15:19 965988847919528-wake.wav
-rw-r--r-- 1 kylarlovelady kylarlovelady    0 Nov  5 17:04 972288312998766-wake.wav
-rw-r--r-- 1 kylarlovelady kylarlovelady    0 Nov  5 17:10 972648755382530-wake.wav
active
Nov 05 17:10:45 LoveladyMainAiHub bash[3021970]: INFO:root:Connected to services
Nov 05 17:10:54 LoveladyMainAiHub bash[3021970]: INFO:root:Connected to server
Nov 05 17:10:54 LoveladyMainAiHub bash[3021970]: INFO:root:Waiting for wake word
(exit 0)
```

## 2026-11-05 17:13:01 tasks/queue/039-home-mic-record-on.sh
REFUSED: contains a command on the deny list

## 2026-11-05 17:16:01 tasks/queue/040-home-mic-record-on.sh
```
recording flag added
HEALTHY with recording on
active
Nov 05 17:16:04 LoveladyMainAiHub bash[3036587]: INFO:root:Recording audio to /home/kylarlovelady/voice-data/home-mic
Nov 05 17:16:04 LoveladyMainAiHub bash[3036587]: INFO:root:Ready
Nov 05 17:16:05 LoveladyMainAiHub bash[3036587]: INFO:root:Connected to services
Nov 05 17:16:14 LoveladyMainAiHub bash[3036587]: INFO:root:Connected to server
Nov 05 17:16:14 LoveladyMainAiHub bash[3036587]: INFO:root:Waiting for wake word
(exit 0)
```
