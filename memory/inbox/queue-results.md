og log (satellite restarts)
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

## 2026-11-05 17:22:01 tasks/queue/041-kdp-build-scheme-a.sh
```
font download: 0 300724 

instance Bold 0 ont /home/kylarlovelady/.local/share/fonts/PlayfairDisplay-Bold.ttf
Attempting to fix OTLOffsetOverflowError ('GPOS', 'LookupIndex:', 4, 'SubTableIndex:', None, 'ItemName:', None, 'ItemIndex:', None)

instance Regular 0 , 5, 'SubTableIndex:', None, 'ItemName:', None, 'ItemIndex:', None)
Attempting to fix OTLOffsetOverflowError ('GPOS', 'LookupIndex:', 4, 'SubTableIndex:', None, 'ItemName:', None, 'ItemIndex:', None)

fonts found: ['Bitstream Vera', 'Caladea', 'Carlito', 'DejaVu Sans', 'DejaVu Serif', 'FreeSans', 'FreeSerif', 'Lato', 'Liberation Mono', 'Liberation Sans', 'Liberation Serif', 'Open Sans', 'Playfair Display', 'Roboto']
title font: Playfair Display | interior font: Lato
== process-operator-a cover 14.065 x 10.418 spine 0.489
  OK Page count 120 (hardcover needs 75 to 550)
  OK Page count is even
  OK Cover file 14.065 x 10.418 in, spine 0.489 in
  WARN Cover size NOT yet verified against KDP's cover calculator (do once before uploading)
  OK Inside margin 0.500 in (KDP minimum 0.375)
  OK All cover text inside the safe zone and clear of the barcode area
  OK Inside text contrast 15.9:1
  OK Picture on the full: sharp (300 dpi)
  OK cover PDF fonts embedded
  OK interior PDF fonts embedded
  OK Author / pen name set
  OK Title set
  OK Title + subtitle length OK
  WARN Book description not written
  WARN 0 of 7 keywords
  WARN Price not set
  plan: ['owner', 'journal', 'journal', 'journal'] ... 120 pages
== lab-operator-a cover 14.065 x 10.418 spine 0.489
  OK Page count 120 (hardcover needs 75 to 550)
  OK Page count is even
  OK Cover file 14.065 x 10.418 in, spine 0.489 in
  WARN Cover size NOT yet verified against KDP's cover calculator (do once before uploading)
  OK Inside margin 0.500 in (KDP minimum 0.375)
  OK All cover text inside the safe zone and clear of the barcode area
  OK Inside text contrast 15.9:1
  OK Picture on the full: sharp (300 dpi)
  OK cover PDF fonts embedded
  OK interior PDF fonts embedded
  OK Author / pen name set
  OK Title set
  OK Title + subtitle length OK
  WARN Book description not written
  WARN 0 of 7 keywords
  WARN Price not set
  plan: ['owner', 'journal', 'journal', 'journal'] ... 120 pages
/home/kylarlovelady/starship/memory/inbox/kdp-preview/lab-operator-a:
total 1988
drwxrwxr-x 2 kylarlovelady kylarlovelady    4096 Nov  5 17:22 .
drwxrwxr-x 4 kylarlovelady kylarlovelady    4096 Nov  5 17:22 ..
-rw-rw-r-- 1 kylarlovelady kylarlovelady 1015384 Nov  5 17:22 cover-guides.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady  994007 Nov  5 17:22 cover.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady    7365 Nov  5 17:22 page1.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady    1569 Nov  5 17:22 page2.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady    1593 Nov  5 17:22 page3.png

/home/kylarlovelady/starship/memory/inbox/kdp-preview/process-operator-a:
total 1988
drwxrwxr-x 2 kylarlovelady kylarlovelady    4096 Nov  5 17:22 .
drwxrwxr-x 4 kylarlovelady kylarlovelady    4096 Nov  5 17:22 ..
-rw-rw-r-- 1 kylarlovelady kylarlovelady 1013726 Nov  5 17:22 cover-guides.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady  992198 Nov  5 17:22 cover.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady    7365 Nov  5 17:22 page1.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady    1569 Nov  5 17:22 page2.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady    1593 Nov  5 17:22 page3.png
(exit 0)
```

## 2026-11-05 17:34:01 tasks/queue/042-kdp-build-border.sh
```
fonts found: ['Bitstream Vera', 'Caladea', 'Carlito', 'DejaVu Sans', 'DejaVu Serif', 'FreeSans', 'FreeSerif', 'Lato', 'Liberation Mono', 'Liberation Sans', 'Liberation Serif', 'Open Sans', 'Playfair Display', 'Roboto']
title font: Playfair Display | interior font: Lato
== process-operator-a cover 14.065 x 10.418 spine 0.489
  OK Page count 120 (hardcover needs 75 to 550)
  OK Page count is even
  OK Cover file 14.065 x 10.418 in, spine 0.489 in
  WARN Cover size NOT yet verified against KDP's cover calculator (do once before uploading)
  OK Inside margin 0.500 in (KDP minimum 0.375)
  OK All cover text inside the safe zone and clear of the barcode area
  OK Inside text contrast 15.9:1
  OK Picture on the full: sharp (300 dpi)
  OK cover PDF fonts embedded
  OK interior PDF fonts embedded
  OK Author / pen name set
  OK Title set
  OK Title + subtitle length OK
  WARN Book description not written
  WARN 0 of 7 keywords
  WARN Price not set
  plan: ['owner', 'journal', 'journal', 'journal'] ... 120 pages
== lab-operator-a cover 14.065 x 10.418 spine 0.489
  OK Page count 120 (hardcover needs 75 to 550)
  OK Page count is even
  OK Cover file 14.065 x 10.418 in, spine 0.489 in
  WARN Cover size NOT yet verified against KDP's cover calculator (do once before uploading)
  OK Inside margin 0.500 in (KDP minimum 0.375)
  OK All cover text inside the safe zone and clear of the barcode area
  OK Inside text contrast 15.9:1
  OK Picture on the full: sharp (300 dpi)
  OK cover PDF fonts embedded
  OK interior PDF fonts embedded
  OK Author / pen name set
  OK Title set
  OK Title + subtitle length OK
  WARN Book description not written
  WARN 0 of 7 keywords
  WARN Price not set
  plan: ['owner', 'journal', 'journal', 'journal'] ... 120 pages
/home/kylarlovelady/starship/memory/inbox/kdp-preview/lab-operator-a:
total 2000
drwxrwxr-x 2 kylarlovelady kylarlovelady    4096 Nov  5 17:30 .
drwxrwxr-x 4 kylarlovelady kylarlovelady    4096 Nov  5 17:30 ..
-rw-rw-r-- 1 kylarlovelady kylarlovelady 1017671 Nov  5 17:34 cover-guides.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady 1000394 Nov  5 17:34 cover.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady    7365 Nov  5 17:34 page1.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady    1569 Nov  5 17:34 page2.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady    1593 Nov  5 17:34 page3.png

/home/kylarlovelady/starship/memory/inbox/kdp-preview/process-operator-a:
total 1992
drwxrwxr-x 2 kylarlovelady kylarlovelady    4096 Nov  5 17:30 .
drwxrwxr-x 4 kylarlovelady kylarlovelady    4096 Nov  5 17:30 ..
-rw-rw-r-- 1 kylarlovelady kylarlovelady 1015213 Nov  5 17:34 cover-guides.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady  998636 Nov  5 17:34 cover.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady    7365 Nov  5 17:34 page1.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady    1569 Nov  5 17:34 page2.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady    1593 Nov  5 17:34 page3.png
(exit 0)
```

## 2026-11-05 17:46:01 tasks/queue/044-kdp-build-backtext.sh
```
fonts found: ['Bitstream Vera', 'Caladea', 'Carlito', 'DejaVu Sans', 'DejaVu Serif', 'FreeSans', 'FreeSerif', 'Lato', 'Liberation Mono', 'Liberation Sans', 'Liberation Serif', 'Open Sans', 'Playfair Display', 'Roboto']
title font: Playfair Display | interior font: Lato
== process-operator-a cover 14.065 x 10.418 spine 0.489
  OK Page count 120 (hardcover needs 75 to 550)
  OK Page count is even
  OK Cover file 14.065 x 10.418 in, spine 0.489 in
  WARN Cover size NOT yet verified against KDP's cover calculator (do once before uploading)
  OK Inside margin 0.500 in (KDP minimum 0.375)
  OK All cover text inside the safe zone and clear of the barcode area
  OK Inside text contrast 15.9:1
  OK Picture on the full: sharp (300 dpi)
  OK cover PDF fonts embedded
  OK interior PDF fonts embedded
  OK Author / pen name set
  OK Title set
  OK Title + subtitle length OK
  WARN Book description not written
  WARN 0 of 7 keywords
  WARN Price not set
  plan: ['owner', 'journal', 'journal', 'journal'] ... 120 pages
== lab-operator-a cover 14.065 x 10.418 spine 0.489
  OK Page count 120 (hardcover needs 75 to 550)
  OK Page count is even
  OK Cover file 14.065 x 10.418 in, spine 0.489 in
  WARN Cover size NOT yet verified against KDP's cover calculator (do once before uploading)
  OK Inside margin 0.500 in (KDP minimum 0.375)
  OK All cover text inside the safe zone and clear of the barcode area
  OK Inside text contrast 15.9:1
  OK Picture on the full: sharp (300 dpi)
  OK cover PDF fonts embedded
  OK interior PDF fonts embedded
  OK Author / pen name set
  OK Title set
  OK Title + subtitle length OK
  WARN Book description not written
  WARN 0 of 7 keywords
  WARN Price not set
  plan: ['owner', 'journal', 'journal', 'journal'] ... 120 pages
/home/kylarlovelady/starship/memory/inbox/kdp-preview/lab-operator-a:
total 2000
drwxrwxr-x 2 kylarlovelady kylarlovelady    4096 Nov  5 17:30 .
drwxrwxr-x 4 kylarlovelady kylarlovelady    4096 Nov  5 17:30 ..
-rw-rw-r-- 1 kylarlovelady kylarlovelady 1017733 Nov  5 17:46 cover-guides.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady 1000401 Nov  5 17:46 cover.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady    7365 Nov  5 17:46 page1.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady    1569 Nov  5 17:46 page2.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady    1593 Nov  5 17:46 page3.png

/home/kylarlovelady/starship/memory/inbox/kdp-preview/process-operator-a:
total 1992
drwxrwxr-x 2 kylarlovelady kylarlovelady    4096 Nov  5 17:30 .
drwxrwxr-x 4 kylarlovelady kylarlovelady    4096 Nov  5 17:30 ..
-rw-rw-r-- 1 kylarlovelady kylarlovelady 1015236 Nov  5 17:46 cover-guides.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady  998588 Nov  5 17:46 cover.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady    7365 Nov  5 17:46 page1.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady    1569 Nov  5 17:46 page2.png
-rw-rw-r-- 1 kylarlovelady kylarlovelady    1593 Nov  5 17:46 page3.png
(exit 0)
```

## 2026-11-05 17:49:01 tasks/queue/045-kdp-build-approved-look.sh
```
fonts found: ['Bitstream Vera', 'Caladea', 'Carlito', 'DejaVu Sans', 'DejaVu Serif', 'FreeSans', 'FreeSerif', 'Lato', 'Liberation Mono', 'Liberation Sans', 'Liberation Serif', 'Open Sans', 'Playfair Display', 'Roboto']
title font: Liberation Serif | interior font: Lato
== process-operator-a FAILS: none | spine 0.489
== process-operator-b FAILS: none | spine 0.489
== process-operator-c FAILS: none | spine 0.489
== process-operator-e FAILS: none | spine 0.489
== lab-operator-a FAILS: none | spine 0.489
== lab-operator-b FAILS: none | spine 0.489
== lab-operator-c FAILS: none | spine 0.489
== lab-operator-e FAILS: none | spine 0.489
sheet done
-rw-rw-r-- 1 kylarlovelady kylarlovelady 1954345 Nov  5 17:50 /home/kylarlovelady/starship/memory/inbox/kdp-preview/contact-sheet.png

/home/kylarlovelady/starship/memory/inbox/kdp-preview/lab-operator-a:
total 2580
drwxrwxr-x  2 kylarlovelady kylarlovelady    4096 Nov  5 17:49 .
drwxrwxr-x 10 kylarlovelady kylarlovelady    4096 Nov  5 17:50 ..
-rw-rw-r--  1 kylarlovelady kylarlovelady  371246 Nov  5 17:49 cover-guides.png
-rw-rw-r--  1 kylarlovelady kylarlovelady 1306165 Nov  5 17:49 cover-hi.png
-rw-rw-r--  1 kylarlovelady kylarlovelady  350388 Nov  5 17:49 cover.png
-rw-rw-r--  1 kylarlovelady kylarlovelady  583258 Nov  5 17:49 front.png
-rw-rw-r--  1 kylarlovelady kylarlovelady    7365 Nov  5 17:49 page1.png
-rw-rw-r--  1 kylarlovelady kylarlovelady    1569 Nov  5 17:49 page2.png
-rw-rw-r--  1 kylarlovelady kylarlovelady    1593 Nov  5 17:46 page3.png

/home/kylarlovelady/starship/memory/inbox/kdp-preview/lab-operator-b:
total 2540
drwxrwxr-x  2 kylarlovelady kylarlovelady    4096 Nov  5 17:50 .
drwxrwxr-x 10 kylarlovelady kylarlovelady    4096 Nov  5 17:50 ..
-rw-rw-r--  1 kylarlovelady kylarlovelady  365446 Nov  5 17:50 cover-guides.png
-rw-rw-r--  1 kylarlovelady kylarlovelady 1283146 Nov  5 17:50 cover-hi.png
-rw-rw-r--  1 kylarlovelady kylarlovelady  343754 Nov  5 17:50 cover.png
-rw-rw-r--  1 kylarlovelady kylarlovelady  578551 Nov  5 17:50 front.png
-rw-rw-r--  1 kylarlovelady kylarlovelady    7365 Nov  5 17:50 page1.png
-rw-rw-r--  1 kylarlovelady kylarlovelady    1569 Nov  5 17:50 page2.png

/home/kylarlovelady/starship/memory/inbox/kdp-preview/lab-operator-c:
total 2556
drwxrwxr-x  2 kylarlovelady kylarlovelady    4096 Nov  5 17:50 .
drwxrwxr-x 10 kylarlovelady kylarlovelady    4096 Nov  5 17:50 ..
-rw-rw-r--  1 kylarlovelady kylarlovelady  366146 Nov  5 17:50 cover-guides.png
(exit 0)
```

## 2026-11-05 17:55:02 tasks/queue/046-kdp-build-thin-border.sh
```
engine min width patched
fonts found: ['Bitstream Vera', 'Caladea', 'Carlito', 'DejaVu Sans', 'DejaVu Serif', 'FreeSans', 'FreeSerif', 'Lato', 'Liberation Mono', 'Liberation Sans', 'Liberation Serif', 'Open Sans', 'Playfair Display', 'Roboto']
title font: Liberation Serif | interior font: Lato
== process-operator-a FAILS: none | spine 0.489
== process-operator-b FAILS: none | spine 0.489
== process-operator-c FAILS: none | spine 0.489
== process-operator-e FAILS: none | spine 0.489
== lab-operator-a FAILS: none | spine 0.489
== lab-operator-b FAILS: none | spine 0.489
== lab-operator-c FAILS: none | spine 0.489
== lab-operator-e FAILS: none | spine 0.489
sheet done
-rw-rw-r-- 1 kylarlovelady kylarlovelady 2050871 Nov  5 17:56 /home/kylarlovelady/starship/memory/inbox/kdp-preview/contact-sheet.png

/home/kylarlovelady/starship/memory/inbox/kdp-preview/lab-operator-a:
total 2704
drwxrwxr-x  2 kylarlovelady kylarlovelady    4096 Nov  5 17:49 .
drwxrwxr-x 10 kylarlovelady kylarlovelady    4096 Nov  5 17:50 ..
-rw-rw-r--  1 kylarlovelady kylarlovelady  381632 Nov  5 17:55 cover-guides.png
-rw-rw-r--  1 kylarlovelady kylarlovelady 1382931 Nov  5 17:55 cover-hi.png
-rw-rw-r--  1 kylarlovelady kylarlovelady  359835 Nov  5 17:55 cover.png
-rw-rw-r--  1 kylarlovelady kylarlovelady  613909 Nov  5 17:55 front.png
-rw-rw-r--  1 kylarlovelady kylarlovelady    7365 Nov  5 17:55 page1.png
-rw-rw-r--  1 kylarlovelady kylarlovelady    1569 Nov  5 17:55 page2.png
-rw-rw-r--  1 kylarlovelady kylarlovelady    1593 Nov  5 17:46 page3.png

/home/kylarlovelady/starship/memory/inbox/kdp-preview/lab-operator-b:
total 2660
drwxrwxr-x  2 kylarlovelady kylarlovelady    4096 Nov  5 17:50 .
drwxrwxr-x 10 kylarlovelady kylarlovelady    4096 Nov  5 17:50 ..
-rw-rw-r--  1 kylarlovelady kylarlovelady  375111 Nov  5 17:56 cover-guides.png
-rw-rw-r--  1 kylarlovelady kylarlovelady 1359593 Nov  5 17:56 cover-hi.png
-rw-rw-r--  1 kylarlovelady kylarlovelady  352917 Nov  5 17:56 cover.png
-rw-rw-r--  1 kylarlovelady kylarlovelady  608559 Nov  5 17:56 front.png
-rw-rw-r--  1 kylarlovelady kylarlovelady    7365 Nov  5 17:56 page1.png
-rw-rw-r--  1 kylarlovelady kylarlovelady    1569 Nov  5 17:56 page2.png

/home/kylarlovelady/starship/memory/inbox/kdp-preview/lab-operator-c:
total 2668
drwxrwxr-x  2 kylarlovelady kylarlovelady    4096 Nov  5 17:50 .
drwxrwxr-x 10 kylarlovelady kylarlovelady    4096 Nov  5 17:50 ..
-rw-rw-r--  1 kylarlovelady kylarlovelady  375809 Nov  5 17:56 cover-guides.png
(exit 0)
```
