process exited, code=exited, status=1/FAILURE
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

## 2026-11-05 18:31:01 tasks/queue/047-kdp-same-yellow.sh
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
-rw-rw-r-- 1 kylarlovelady kylarlovelady 2050548 Nov  5 18:32 /home/kylarlovelady/starship/memory/inbox/kdp-preview/contact-sheet.png

/home/kylarlovelady/starship/memory/inbox/kdp-preview/lab-operator-a:
total 2704
drwxrwxr-x  2 kylarlovelady kylarlovelady    4096 Nov  5 17:49 .
drwxrwxr-x 10 kylarlovelady kylarlovelady    4096 Nov  5 17:50 ..
-rw-rw-r--  1 kylarlovelady kylarlovelady  381632 Nov  5 18:31 cover-guides.png
-rw-rw-r--  1 kylarlovelady kylarlovelady 1382931 Nov  5 18:31 cover-hi.png
-rw-rw-r--  1 kylarlovelady kylarlovelady  359835 Nov  5 18:31 cover.png
-rw-rw-r--  1 kylarlovelady kylarlovelady  613909 Nov  5 18:31 front.png
-rw-rw-r--  1 kylarlovelady kylarlovelady    7365 Nov  5 18:31 page1.png
-rw-rw-r--  1 kylarlovelady kylarlovelady    1569 Nov  5 18:31 page2.png
-rw-rw-r--  1 kylarlovelady kylarlovelady    1593 Nov  5 17:46 page3.png

/home/kylarlovelady/starship/memory/inbox/kdp-preview/lab-operator-b:
total 2660
drwxrwxr-x  2 kylarlovelady kylarlovelady    4096 Nov  5 17:50 .
drwxrwxr-x 10 kylarlovelady kylarlovelady    4096 Nov  5 17:50 ..
-rw-rw-r--  1 kylarlovelady kylarlovelady  375111 Nov  5 18:32 cover-guides.png
-rw-rw-r--  1 kylarlovelady kylarlovelady 1359593 Nov  5 18:32 cover-hi.png
-rw-rw-r--  1 kylarlovelady kylarlovelady  352917 Nov  5 18:32 cover.png
-rw-rw-r--  1 kylarlovelady kylarlovelady  608559 Nov  5 18:32 front.png
-rw-rw-r--  1 kylarlovelady kylarlovelady    7365 Nov  5 18:32 page1.png
-rw-rw-r--  1 kylarlovelady kylarlovelady    1569 Nov  5 18:32 page2.png

/home/kylarlovelady/starship/memory/inbox/kdp-preview/lab-operator-c:
total 2664
drwxrwxr-x  2 kylarlovelady kylarlovelady    4096 Nov  5 17:50 .
drwxrwxr-x 10 kylarlovelady kylarlovelady    4096 Nov  5 17:50 ..
-rw-rw-r--  1 kylarlovelady kylarlovelady  375566 Nov  5 18:32 cover-guides.png
(exit 0)
```

## 2026-11-05 18:43:01 tasks/queue/048-kdp-keyword-scan.sh
```
(exit 0)
```

## 2026-11-05 18:52:01 tasks/queue/049-kdp-keyword-scan-bg.sh
```
started pid 3293782
(exit 0)
```

## 2026-11-05 19:13:02 tasks/queue/050-kdp-no-barcode-box.sh
```
== process-operator-a FAILS: none | spine 0.489
== process-operator-b FAILS: none | spine 0.489
== process-operator-c FAILS: none | spine 0.489
== process-operator-e FAILS: none | spine 0.489
== lab-operator-a FAILS: none | spine 0.489
== lab-operator-b FAILS: none | spine 0.489
== lab-operator-c FAILS: none | spine 0.489
== lab-operator-e FAILS: none | spine 0.489
sheet done
-rw-rw-r-- 1 kylarlovelady kylarlovelady 5282832 Nov  5 19:13 /home/kylarlovelady/kdp-studio/books/lab-operator-a/out/coverg.pdf
-rw-rw-r-- 1 kylarlovelady kylarlovelady 5262157 Nov  5 19:13 /home/kylarlovelady/kdp-studio/books/lab-operator-a/out/cover.pdf
-rw-rw-r-- 1 kylarlovelady kylarlovelady  113757 Nov  5 19:13 /home/kylarlovelady/kdp-studio/books/lab-operator-a/out/interior.pdf
-rw-rw-r-- 1 kylarlovelady kylarlovelady 5282830 Nov  5 19:13 /home/kylarlovelady/kdp-studio/books/process-operator-a/out/coverg.pdf
-rw-rw-r-- 1 kylarlovelady kylarlovelady 5262158 Nov  5 19:13 /home/kylarlovelady/kdp-studio/books/process-operator-a/out/cover.pdf
-rw-rw-r-- 1 kylarlovelady kylarlovelady  113761 Nov  5 19:13 /home/kylarlovelady/kdp-studio/books/process-operator-a/out/interior.pdf
(exit 0)
```

## 2026-11-05 19:25:02 tasks/queue/051-kalshi-fresh-wallet.sh
```
reset reply: 
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import json;d=json.load(open('/tmp/live-after.json'));print({k:d.get(k) for k in list(d)[:12]})
                  ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.13/json/__init__.py", line 293, in load
    return loads(fp.read(),
        cls=cls, object_hook=object_hook,
        parse_float=parse_float, parse_int=parse_int,
        parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
  File "/usr/lib/python3.13/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/usr/lib/python3.13/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.13/json/decoder.py", line 363, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
{"active": true, "id": 1793908418, "strategy": "auto", "start": 1000.0}(exit 0)
```

## 2026-11-05 19:37:02 tasks/queue/052-snipe-study.sh
```
# Sniping study (recorded per-second data, last 5 days)

Rounds with a full recording: 362


## Part 1: seconds left on the clock at the LAST second the market was still open

| left at last recorded second | rounds | share |
|---|---|---|
| 0-2 s | 2 | 1% |
| 2-5 s | 2 | 1% |
| 5-10 s | 8 | 2% |
| 10-30 s | 36 | 10% |
| 30-120 s | 229 | 63% |
| >120 s | 85 | 23% |

Median seconds left at last open second: 70.0 (a high number means Kalshi stopped quoting before the clock ran out, or our recorder missed the last seconds).

Examples of rounds that stopped with more than 10 s left: left 90s, YES bid 1.00 / NO bid 0.00; left 183s, YES bid 0.01 / NO bid 0.99; left 32s, YES bid 0.00 / NO bid 1.00; left 62s, YES bid 0.00 / NO bid 1.00; left 198s, YES bid 0.13 / NO bid 0.86; left 115s, YES bid 0.00 / NO bid 1.00; left 128s, YES bid 0.00 / NO bid 1.00; left 144s, YES bid 1.00 / NO bid 0.00; left 17s, YES bid 1.00 / NO bid 0.00; left 75s, YES bid 0.00 / NO bid 1.00; left 18s, YES bid 1.00 / NO bid 0.00; left 38s, YES bid 0.00 / NO bid 1.00

Rounds with a real settled result in history: 267 of 362

## Part 2: buy the favourite at the last tick that still had at least B seconds left, hold to the result

### B = 3 s left

| ask bucket | rounds | win rate | avg cost/contract | profit per $ staked | median $ at best ask |
|---|---|---|---|---|---|
| 55-59c | 5 | 40.0% | 0.593 | -32.6% | $866 |
| 60-64c | 1 | 100.0% | 0.656 | +52.4% | $1392 |
| 65-69c | 1 | 100.0% | 0.666 | +50.2% | $1492 |
| 70-74c | 3 | 66.7% | 0.734 | -9.2% | $192 |
| 75-79c | 3 | 66.7% | 0.779 | -14.4% | $3112 |
| 80-84c | 7 | 85.7% | 0.836 | +2.6% | $1937 |
| 85-89c | 5 | 60.0% | 0.887 | -32.4% | $2778 |
| 90-94c | 16 | 93.8% | 0.927 | +1.1% | $231 |
| 95-99c | 40 | 97.5% | 0.982 | -0.7% | $965 |
| ALL | 81 | | | -3.0% | |

### B = 5 s left

| ask bucket | rounds | win rate | avg cost/contract | profit per $ staked | median $ at best ask |
|---|---|---|---|---|---|
| 55-59c | 5 | 40.0% | 0.593 | -32.6% | $866 |
| 60-64c | 1 | 100.0% | 0.656 | +52.4% | $1392 |
| 65-69c | 2 | 50.0% | 0.685 | -27.1% | $764 |
| 70-74c | 2 | 50.0% | 0.724 | -31.0% | $943 |
| 75-79c | 3 | 66.7% | 0.779 | -14.4% | $3112 |
| 80-84c | 7 | 85.7% | 0.836 | +2.6% | $1937 |
| 85-89c | 6 | 66.7% | 0.884 | -24.6% | $1762 |
| 90-94c | 15 | 93.3% | 0.928 | +0.6% | $241 |
| 95-99c | 41 | 97.6% | 0.982 | -0.6% | $902 |
| ALL | 82 | | | -4.2% | |

### B = 10 s left

| ask bucket | rounds | win rate | avg cost/contract | profit per $ staked | median $ at best ask |
|---|---|---|---|---|---|
| 55-59c | 6 | 33.3% | 0.594 | -43.9% | $667 |
| 60-64c | 2 | 100.0% | 0.656 | +52.4% | $786 |
... wrote /home/kylarlovelady/starship/memory/inbox/snipe-study.md
(exit 0)
```
