:8080/event/wake > /dev/null"' \
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

## 2026-11-05 19:46:01 tasks/queue/053-avg-lock-study.sh
```
# Average-lock study (can we call the winning side late?)

Rounds with real results and full recordings: 19. Model: the last-minute average is partly known; remaining seconds = random walk (recent 1 s vol). Edge = model P - Kalshi ask - fee.

## 10 seconds left

| rule | bets | win rate | avg cost/contract | profit per $ | avg model P | avg ask |
|---|---|---|---|---|---|---|
| any edge > 3c | 0 | | | | | |
| edge > 8c | 0 | | | | | |
| edge > 3c AND near target (within 1 sd) | 0 | | | | | |
| always bet model favourite | 0 | | | | | |
| near target only, always bet model favourite | 0 | | | | | |

## 20 seconds left

| rule | bets | win rate | avg cost/contract | profit per $ | avg model P | avg ask |
|---|---|---|---|---|---|---|
| any edge > 3c | 0 | | | | | |
| edge > 8c | 0 | | | | | |
| edge > 3c AND near target (within 1 sd) | 0 | | | | | |
| always bet model favourite | 2 | 50.0% | 0.501 | -0.1% | 0.99 | 0.50 |
| near target only, always bet model favourite | 0 | | | | | |

## 30 seconds left

| rule | bets | win rate | avg cost/contract | profit per $ | avg model P | avg ask |
|---|---|---|---|---|---|---|
| any edge > 3c | 3 | 0.0% | 0.020 | -100.0% | 0.84 | 0.02 |
| edge > 8c | 2 | 0.0% | 0.013 | -100.0% | 0.81 | 0.01 |
| edge > 3c AND near target (within 1 sd) | 1 | 0.0% | 0.014 | -100.0% | 0.74 | 0.01 |
| always bet model favourite | 4 | 25.0% | 0.264 | -5.5% | 0.88 | 0.26 |
| near target only, always bet model favourite | 1 | 0.0% | 0.014 | -100.0% | 0.74 | 0.01 |

## 45 seconds left

| rule | bets | win rate | avg cost/contract | profit per $ | avg model P | avg ask |
|---|---|---|---|---|---|---|
| any edge > 3c | 3 | 0.0% | 0.232 | -100.0% | 0.58 | 0.22 |
| edge > 8c | 3 | 0.0% | 0.232 | -100.0% | 0.58 | 0.22 |
| edge > 3c AND near target (within 1 sd) | 3 | 0.0% | 0.232 | -100.0% | 0.58 | 0.22 |
| always bet model favourite | 6 | 16.7% | 0.301 | -44.7% | 0.76 | 0.29 |
| near target only, always bet model favourite | 3 | 0.0% | 0.232 | -100.0% | 0.58 | 0.22 |

Calibration check (does the model's P match reality?): bucket by model P of the favourite
(left=20) P~0.95: 2 rounds, 50% won
... wrote /home/kylarlovelady/starship/memory/inbox/avg-lock-study.md
(exit 0)
```

## 2026-11-05 20:16:01 tasks/queue/054-sniper-reset-check.sh
REFUSED: header must be '#!/bin/bash' then '# QUEUE-OK'

## 2026-11-05 21:10:01 tasks/queue/055-kdp-owner-page.sh
```
(exit 0)
```

## 2026-11-05 21:13:01 tasks/queue/056-liq-by-second.sh
```
# Liquidity before the close (auto): dollars buyable on the favourite at 99c or less

Rounds seen: 268. 'any' = at least $25 buyable, 'full' = at least $1,000 buyable. Seconds with no row count as nothing buyable.

| s before close | rounds with data | any | full ($1,000) | median $ buyable |
|---|---|---|---|---|
| 0 | 268 | 0% | 0% | $0 |
| 1 | 268 | 0% | 0% | $0 |
| 2 | 268 | 1% | 0% | $0 |
| 3 | 268 | 1% | 0% | $0 |
| 4 | 268 | 1% | 1% | $0 |
| 5 | 268 | 1% | 1% | $0 |
| 6 | 268 | 1% | 1% | $0 |
| 7 | 268 | 2% | 2% | $0 |
| 8 | 268 | 2% | 1% | $0 |
| 9 | 268 | 3% | 2% | $0 |
| 10 | 268 | 3% | 2% | $0 |
| 11 | 268 | 3% | 2% | $0 |
| 12 | 268 | 3% | 3% | $0 |
| 13 | 268 | 4% | 3% | $0 |
| 14 | 268 | 4% | 3% | $0 |
| 15 | 268 | 4% | 4% | $0 |
| 16 | 268 | 4% | 3% | $0 |
| 17 | 268 | 4% | 3% | $0 |
| 18 | 268 | 4% | 3% | $0 |
| 19 | 268 | 5% | 4% | $0 |
| 20 | 268 | 5% | 3% | $0 |
| 25 | 268 | 7% | 4% | $0 |
| 30 | 268 | 9% | 5% | $0 |
| 40 | 268 | 16% | 11% | $0 |
(exit 0)
```
