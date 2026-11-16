 @ 52c  stake      5  result UP       +4.62  total  +6234.31
  Mon 09 06:30  UP    317 @ 63c  stake    200  result UP     +112.11  total  +6346.42
  Mon 09 06:45  DOWN 2760 @ 17c  stake    473  result UP     -499.95  total  +5846.47
  Mon 09 07:00  UP   2758 @ 17c  stake    473  result DOWN   -499.87  total  +5346.60
  Mon 09 07:15  DOWN    8 @ 63c  stake      5  result DOWN     +2.82  total  +5349.42
  Mon 09 07:30  UP    895 @ 54c  stake    484  result DOWN   -499.49  total  +4849.93
  Mon 09 07:45  UP     10 @ 55c  stake      6  result UP       +4.32  total  +4854.25
  Mon 09 08:00  DOWN    9 @ 59c  stake      5  result DOWN     +3.53  total  +4857.78
  Mon 09 08:15  UP    762 @ 64c  stake    488  result UP     +262.20  total  +5119.98
  Mon 09 08:30  DOWN  763 @ 64c  stake    487  result DOWN   +263.25  total  +5383.23
  Mon 09 09:00  DOWN    9 @ 58c  stake      5  result UP       -5.38  total  +5377.85
  Mon 09 19:30  DOWN    8 @ 65c  stake      5  result DOWN     +2.67  total  +5380.52
  Mon 09 19:45  UP     10 @ 51c  stake      5  result UP       +4.72  total  +5385.24

RUNNING TOTAL every 10 rounds: -502, +970, -1256, +63, +629, +517, +1303, +1506, -344, +1132, +1947, +5603, +4280, +1293, +2535, +5245, +6723, +4854

---- v_hold_s100 (same entries, 1/5 the size) ----
WALLET CURVE v_hold_s100 (pretend money, after fees): 186 settled rounds, Sat 07 10:30 to Mon 09 19:45, 1 unsettled skipped
  profit now +1050.33 | peak +1427.02 (Mon 09 03:00) | worst drop 1037.55 (Sun 08 16:30 -> Sun 08 22:16) | drop right now 376.69 from the peak
  wins 119 (64%), avg win +52.53, avg loss -77.62, avg stake 60.53, avg entry price 53.8 c
  entry price  0- 40 c:  35 rounds, won  29%, profit   +738.81
  entry price 40- 60 c:  56 rounds, won  66%, profit    +11.68
  entry price 60- 80 c:  95 rounds, won  76%, profit   +299.84
  bet UP  : 100 rounds, won  62%, profit   -475.25
  bet DOWN:  86 rounds, won  66%, profit  +1525.58
  5 best rounds: +469, +406, +406, +379, +358  (= 192% of total profit)
  5 worst rounds: -100, -100, -100, -100, -100
  longest losing streak: 4 rounds
  by hour (local): 00:-156(8)  01:+170(8)  02:+390(8)  03:+334(8)  04:-296(8)  05:+286(8)  06:-121(8)  07:-488(8)  08:+74(7)  09:-65(5)  10:-115(6)  11:+652(8)  12:-92(8)  13:+296(8)  14:+659(8)  15:-300(7)  16:+50(8)  17:-207(8)  18:+117(8)  19:+10(9)  20:-453(8)  21:-200(8)  22:+385(8)  23:+119(8)

LATEST 6 ROUNDS (time, bet, contracts, avg price c, stake, result, profit, running total)
```
(exit 0)
```

## 2026-11-09 20:07:01 tasks/queue/106-kalshi-signal-check.sh
```
wrote /home/kylarlovelady/starship/memory/inbox/kalshi-signal-check.md
# Kalshi signal check (queue 106, Mon 09 20:07, practice money only)

```
SIGNAL CHECK v_hold_s500: 186 settled rounds with a BUY
feature keys seen: [('el', 186), ('left', 186), ('pm', 186), ('score', 186)]

SIZE: 115 big rounds (stake >= $50), 71 small (< $50)
  big   won  55%, avg price 50c, profit per $ staked +9.7%
  small won  79%, avg price 60c, profit per $ staked +27.4%
  reasons logged on big rounds : [('Opening bet: it thinks UP is more likely (56% up) ', 7), ('Opening bet: it thinks UP is more likely (65% up) ', 5), ('Opening bet: it thinks UP is more likely (54% up) ', 5), ('Opening bet: it thinks UP is more likely (53% up) ', 5)]
  reasons logged on small rounds: [('Opening bet: it thinks UP is more likely (53% up) ', 5), ('Opening bet: it thinks UP is more likely (56% up) ', 5), ('Opening bet: it thinks DOWN is more likely (47% up', 5), ('Opening bet: it thinks UP is more likely (57% up) ', 4)]

SIGNAL SCORE vs the bet (score > 0 leans Up). 186 rounds have a score
  signals AGREE with the bet         108 rounds, won  66%, profit per $   +9.5%, total at the real stakes  +2977.93
  signals DISAGREE with the bet       77 rounds, won  62%, profit per $  +12.7%, total at the real stakes  +2907.30
  score exactly 0                      1 rounds, won   0%, profit per $ -100.0%, total at the real stakes   -499.99
  |score| 0-10, agree                 72 rounds, won  65%, profit per $  +12.9%, total at the real stakes  +2651.28
  |score| 0-10, disagree              57 rounds, won  63%, profit per $  +12.3%, total at the real stakes  +2204.12
  |score| 10-25, agree                29 rounds, won  69%, profit per $  +18.9%, total at the real stakes  +1704.76
  |score| 10-25, disagree             19 rounds, won  58%, profit per $  +14.1%, total at the real stakes   +701.39
  |score| 25-50, agree                 7 rounds, won  57%, profit per $  -80.1%, total at the real stakes  -1378.11
  |score| 25-50, disagree              1 rounds, won 100%, profit per $  +34.4%, total at the real stakes     +1.79

CHEAP SIDE (under 40c) by agreement:
  cheap, signals agree                19 rounds, won  32%, profit per $  +12.0%, total at the real stakes  +1002.00
  cheap, signals disagree             16 rounds, won  25%, profit per $  +41.8%, total at the real stakes  +3055.83

TIME INTO THE ROUND of the first buy: [(0, 140), (1, 29), (3, 7), (2, 5), (5, 2), (4, 2)]
```
(exit 0)
```

## 2026-11-09 20:10:02 tasks/queue/107-kalshi-size-rules.sh
```
wrote /home/kylarlovelady/starship/memory/inbox/kalshi-size-rules.md
# Kalshi size rules replay (queue 107, Mon 09 20:10, practice money only)

```
SIZE RULES REPLAY on 186 settled v_hold_s500 rounds (same entries, new stakes). Treat as hints, not proof.

rule                                                                                     profit worst drop  avg stake profit/$
A. as recorded (about $5 or $480)                                                         +5385      5307        294    +9.8%
B. flat $250 every round                                                                  +7518      1842        250   +16.2%
C. flat $100 every round                                                                  +3007       737        100   +16.2%
D. cheap side (<40c) capped at $100, rest $250                                            +6275      1635        222   +15.2%
E. KYLAR: $250 if signals agree, $100 if split, $50 if disagree                           +4749      1615        166   +15.3%
F. KYLAR strong: $400 agree and |score|>=10, $200 agree, $75 split, $25 disagree          +4768      1607        166   +15.5%
G. opposite of Kylar: $250 if signals DISAGREE, $100 if agree                             +5197      1422        162   +17.2%
H. size by price: $50 under 40c, $250 40-60c, $400 over 60c                               +7644      1866        289   +14.2%

SAME RULES, FIRST HALF vs SECOND HALF of the rounds (does the ranking hold on rounds it did not see?)
  B. flat $250 every round                                                         first    +1155   second    +6363
  C. flat $100 every round                                                         first     +462   second    +2545
  D. cheap side (<40c) capped at $100, rest $250                                   first    +1141   second    +5133
  E. KYLAR: $250 if signals agree, $100 if split, $50 if disagree                  first    +1264   second    +3485
  F. KYLAR strong: $400 agree and |score|>=10, $200 agree, $75 split, $25 disagree first     +697   second    +4071
  G. opposite of Kylar: $250 if signals DISAGREE, $100 if agree                    first     +493   second    +4704
  H. size by price: $50 under 40c, $250 40-60c, $400 over 60c                      first    +2368   second    +5276
```
(exit 0)
```

## 2026-11-09 20:25:02 tasks/queue/108-kalshi-check-restart.sh
```
agent: active
Nov 09 20:24:05 LoveladyMainAiHub python3[2080]: collector updated, restarting
0
      1 "s": "v_flow_flip"
      1 "s": "v_hold_s5"
      1 "s": "v_snipe"
      1 "s": "v_x16217721"
      1 "s": "v_x36215122"
sim.json read: [Errno 2] No such file or directory: '/home/kylarlovelady/market-data/sim.json'
(exit 0)
```

## 2026-11-09 20:31:02 tasks/queue/109-kalshi-new-wallets-check.sh
```
agent: active  now: 20:31
v_hold_s250 buys: 306
v_hold_s250_cheap100 buys: 1
v_hold_s250_agree buys: 1
{"t": 1794276364, "s": "v_hold_s250", "a": "BUY", "side": "UP", "c": 1444, "px": 0.16, "d": 231.04, "bal": 3383.21, "why": "Edge: it thinks UP is 28% likely but Kalshi asks 16\u00a2 (+11\u00a2 after fees).", "g": null, "ticker": "KXBTC15M-26NOV092115-15", "live": false, "ask": 0.16, "bid": 0.15, "v": 5, "q": "book", "f": {"el": 
{"t": 1794276929, "s": "v_hold_s250", "a": "BUY", "side": "UP", "c": 10, "px": 0.54, "d": 5.4, "bal": 3377.63, "why": "Opening bet: it thinks UP is more likely (56% up) and has to bet every round.", "g": null, "ticker": "KXBTC15M-26NOV092130-30", "live": false, "ask": 0.54, "bid": 0.53, "v": 5, "q": "book", "f": {"el": 29, "left
{"t": 1794277346, "s": "v_hold_s250", "a": "BUY", "side": "UP", "c": 1284, "px": 0.18, "d": 231.12, "bal": 3133.24, "why": "Edge: it thinks UP is 24% likely but Kalshi asks 18\u00a2 (+4\u00a2 after fees).", "g": null, "ticker": "KXBTC15M-26NOV092130-30", "live": false, "ask": 0.18, "bid": 0.17, "v": 5, "q": "book", "f": {"el": 4
{"t": 1794277845, "s": "v_hold_s250", "a": "BUY", "side": "DOWN", "c": 8, "px": 0.7, "d": 5.6, "bal": 3127.52, "why": "Opening bet: it thinks DOWN is more likely (37% up) and has to bet every round.", "g": null, "ticker": "KXBTC15M-26NOV092145-45", "live": false, "ask": 0.31, "bid": 0.3, "v": 5, "q": "book", "f": {"el": 45, "lef
{"t": 1794277845, "s": "v_hold_s250_cheap100", "a": "BUY", "side": "DOWN", "c": 8, "px": 0.7, "d": 5.6, "bal": 994.28, "why": "Opening bet: it thinks DOWN is more likely (37% up) and has to bet every round.", "g": null, "ticker": "KXBTC15M-26NOV092145-45", "live": false, "ask": 0.31, "bid": 0.3, "v": 5, "q": "book", "f": {"el": 
{"t": 1794277845, "s": "v_hold_s250_agree", "a": "BUY", "side": "DOWN", "c": 8, "px": 0.7, "d": 5.6, "bal": 994.28, "why": "Opening bet: it thinks DOWN is more likely (37% up) and has to bet every round.", "g": null, "ticker": "KXBTC15M-26NOV092145-45", "live": false, "ask": 0.31, "bid": 0.3, "v": 5, "q": "book", "f": {"el": 45,
buys with sz logged: 75
(exit 0)
```

## 2026-11-11 14:22:02 tasks/queue/110-hub-probe.sh
REFUSED: contains a command on the deny list

## 2026-11-11 14:40:02 tasks/queue/111-serve-hub2.sh
```
total 388
drwxrwxr-x 2 kylarlovelady kylarlovelady   4096 Nov 11 14:40 .
drwxr-xr-x 3 kylarlovelady kylarlovelady   4096 Nov 11 14:40 ..
-rw-rw-r-- 1 kylarlovelady kylarlovelady  28325 Nov 11 14:40 index.html
-rw-rw-r-- 1 kylarlovelady kylarlovelady 357575 Nov 11 14:40 ocean.jpg
hub2 over http 8095: 000
(exit 0)
```

## 2026-11-11 15:04:01 tasks/queue/112-hub-media-server.sh
REFUSED: contains a command on the deny list

## 2026-11-11 15:10:01 tasks/queue/113-hub-media-start.sh
```

total 404
drwxrwxr-x 2 kylarlovelady kylarlovelady   4096 Nov 11 15:03 .
drwxr-xr-x 3 kylarlovelady kylarlovelady   4096 Nov 11 15:10 ..
-rw-rw-r-- 1 kylarlovelady kylarlovelady  35051 Nov 11 15:10 index.html
-rw-rw-r-- 1 kylarlovelady kylarlovelady   6407 Nov 11 15:10 media_server.py
-rw-rw-r-- 1 kylarlovelady kylarlovelady 357575 Nov 11 15:10 ocean.jpg
free space:
200G free of 234G
(exit 0)
```

## 2026-11-11 15:13:01 tasks/queue/114-hub-media-check.sh
```
process:
state:

crew-update line:
1
(exit 0)
```

## 2026-11-11 15:16:02 tasks/queue/115-hub-media-debug.sh
```
python: Python 3.13.5
-- foreground test (3 s)
Traceback (most recent call last):
  File "/home/kylarlovelady/starship/hub2/media_server.py", line 116, in <module>
    ThreadingHTTPServer(("0.0.0.0", 8097), H).serve_forever()
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.13/socketserver.py", line 457, in __init__
    self.server_bind()
    ~~~~~~~~~~~~~~~~^^
  File "/usr/lib/python3.13/http/server.py", line 136, in server_bind
exit: 0
-- tail of crew-update.sh
cp ~/starship/markets/live.html ~/crew-web/live.html
cp ~/starship/markets/report.html ~/crew-web/report.html
mkdir -p ~/crew-web/hub2 && cp -r ~/starship/hub2/. ~/crew-web/hub2/
pgrep -f hub2/media_server.py >/dev/null || nohup python3 $HOME/starship/hub2/media_server.py >/dev/null 2>&1 &
-- after detached start

Traceback (most recent call last):
  File "/home/kylarlovelady/starship/hub2/media_server.py", line 116, in <module>
    ThreadingHTTPServer(("0.0.0.0", 8097), H).serve_forever()
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.13/socketserver.py", line 457, in __init__
(exit 0)
```

## 2026-11-11 15:19:01 tasks/queue/113-hub-media-start.sh
```
{"files": [], "settings": {"current": "ocean", "cycle": false, "minutes": 5, "dim_from": 20, "dim_to": 8}, "t": 1794431943}

total 404
drwxrwxr-x 2 kylarlovelady kylarlovelady   4096 Nov 11 15:03 .
drwxr-xr-x 3 kylarlovelady kylarlovelady   4096 Nov 11 15:18 ..
-rw-rw-r-- 1 kylarlovelady kylarlovelady  35051 Nov 11 15:19 index.html
-rw-rw-r-- 1 kylarlovelady kylarlovelady   6407 Nov 11 15:19 media_server.py
-rw-rw-r-- 1 kylarlovelady kylarlovelady 357575 Nov 11 15:19 ocean.jpg
free space:
200G free of 234G
(exit 0)
```

## 2026-11-11 15:19:03 tasks/queue/114-hub-media-check.sh
```
process:
1980217 python3 /home/kylarlovelady/starship/hub2/media_server.py
state:
{"files": [], "settings": {"current": "ocean", "cycle": false, "minutes": 5, "dim_from": 20, "dim_to": 8}, "t": 1794431943}

crew-update line:
1
(exit 0)
```

## 2026-11-11 15:19:03 tasks/queue/116-hub-media-port.sh
```
-- who holds 8097:
LISTEN 0      5                             100.105.140.126:8097       0.0.0.0:*    users:(("python3",pid=2080,fd=3))    
-- running:
1983512 python3 /home/kylarlovelady/starship/hub2/media_server.py
-- state:
{"files": [], "settings": {"current": "ocean", "cycle": false, "minutes": 5, "dim_from": 20, "dim_to": 8}, "t": 1794431947}

(exit 0)
```

## 2026-11-16 03:49:02 tasks/queue/117-forward-review.sh
```
wrote /home/kylarlovelady/starship/memory/inbox/kalshi-forward-review.md (41 lines)
# Kalshi forward review (queue 117, Mon 16 03:49, practice money only)

```
no settled rounds for 2026-11-11
FORWARD REVIEW (pretend money, after fees). Start Wed 11 00:00. Run Mon 16 03:49

A) SINCE START, every strategy on its own rounds:
  v_hold_s250            440 rounds | profit  -3106.66 | win  62% | avg/round    -7.06 | median round   +2.20 | stake/round 114
  v_hold_s250_cheap100   440 rounds | profit   -302.01 | win  62% | avg/round    -0.69 | median round   +2.20 | stake/round 103
  v_hold_s250_agree      384 rounds | profit  -1302.78 | win  63% | avg/round    -3.39 | median round   +2.20 | stake/round 100
  v_hold_s100            440 rounds | profit   -910.94 | win  62% | avg/round    -2.07 | median round   +2.20 | stake/round 49
  hold                   454 rounds | profit   +305.48 | win  61% | avg/round    +0.67 | median round   +2.59 | stake/round 10
  v_edge10_s100          161 rounds | profit   -100.43 | win  32% | avg/round    -0.62 | median round  -42.26 | stake/round 55
  v_hold_s500            440 rounds | profit  -2676.41 | win  62% | avg/round    -6.08 | median round   +2.20 | stake/round 222

B) PAIRED vs v_hold_s250 (same rounds only; positive = the test beat the baseline):
  v_hold_s250_cheap100   440 shared | total diff  +2804.65 | avg   +6.37/round | t-score +1.40 | better in 67, worse in 22, same in 351
  v_hold_s250_agree      384 shared | total diff   +954.86 | avg   +2.49/round | t-score +0.23 | better in 136, worse in 115, same in 133
  v_hold_s100            440 shared | total diff  +2195.72 | avg   +4.99/round | t-score +0.77 | better in 114, worse in 100, same in 226
  hold                   440 shared | total diff  +3485.05 | avg   +7.92/round | t-score +0.75 | better in 195, worse in 155, same in 90
  v_edge10_s100          161 shared | total diff  -3469.78 | avg  -21.55/round | t-score -0.99 | better in 64, worse in 97, same in 0
   (t-score: about 2 or more = probably real, under 1 = could easily be luck)

C) LUCK CHECK, all history:
  v_edge10_s100: 190 rounds, total +908.74
     without best 3 rounds -579.55 | without best 5 -1479.73 | without best 10% (19 rounds) -4974.54
     first half +1527.56 (Tue 10 07:55 to Thu 12 20:52) | second half -618.82 (to Mon 16 02:23)
     by day: Tue 10 +1009  Wed 11 +908  Thu 12 -596  Fri 13 +751  Sat 14 -794  Sun 15 -392  Mon 16 +22  -> 4 of 7 days positive
  v_hold_s250_cheap100: 547 rounds, total -2953.74
     without best 3 rounds -6317.06 | without best 5 -8195.85 | without best 10% (54 rounds) -23075.11
     first half -2402.86 (Mon 09 20:30 to Thu 12 21:30) | second half -550.88 (to Mon 16 03:31)
     by day: Mon 09 -645  Tue 10 -2006  Wed 11 +1070  Thu 12 -1209  Fri 13 +627  Sat 14 -1702  Sun 15 +1152  Mon 16 -239  -> 3 of 8 days positive
  v_hold_s250: 735 rounds, total -5263.10
     without best 3 rounds -9062.29 | without best 5 -11274.49 | without best 10% (73 rounds) -38420.15
     first half -3263.57 (Sat 07 10:30 to Wed 11 18:15) | second half -1999.53 (to Mon 16 03:31)
     by day: Sat 07 +885  Sun 08 +351  Mon 09 -295  Tue 10 -3097  Wed 11 +597  Thu 12 -1809  Fri 13 -245  Sat 14 -1375  Sun 15 -522  Mon 16 +248  -> 4 of 10 days positive
  v_hold_s500: 735 rounds, total -7263.95
     without best 3 rounds -15125.12 | without best 5 -19813.17 | without best 10% (73 rounds) -73790.58
     first half -6668.58 (Sat 07 10:30 to Wed 11 18:15) | second half -595.37 (to Mon 16 03:31)
     by day: Sat 07 +1311  Sun 08 +1219  Mon 09 -534  Tue 10 -6583  Wed 11 +1304  Thu 12 -3669  Fri 13 -622  Sat 14 -1907  Sun 15 +1679  Mon 16 +539  -> 5 of 10 days positive
```
(exit 0)
```

## 2026-11-16 04:31:01 tasks/queue/118-kdp-gold-pink.sh
```
KDP black-gold + pink build started in the background (log ~/kdp-build-fg.log)
(exit 0)
```

## 2026-11-16 04:31:01 tasks/queue/119-news-log.sh
```
# News feeds probe (queue 119, Mon 16 04:31)

```
feed               cat      result
coindesk           crypto   ok  25 items, newest 57 min old
cointelegraph      crypto   ok  30 items, newest 100 min old
decrypt            crypto   ok  40 items, newest 6 min old
bitcoinmagazine    crypto   ok  10 items, newest 1171 min old
cryptoslate        crypto   ok  10 items, newest 6 min old
bitcoinist         crypto   ok   8 items, newest 46 min old
gnews-bitcoin      crypto   ok 100 items, newest 17 min old
cnbc-top           finance  ok  30 items, newest 31 min old
cnbc-markets       finance  ok  30 items, newest 680 min old
marketwatch        finance  ok  10 items, newest 11 min old
yahoo-finance      finance  FAIL HTTPError: HTTP Error 404: Not Found
fed                finance  ok  20 items, newest 3676 min old
gnews-fed-rates    finance  ok  76 items, newest 7 min old
theverge           tech     ok  10 items, newest 374 min old
techcrunch         tech     ok  20 items, newest 211 min old
arstechnica        tech     ok  20 items, newest 679 min old
hackernews         tech     ok  20 items, newest 280 min old
bleepingcomputer   tech     ok  15 items, newest 61 min old
gnews-outage       tech     ok 100 items, newest 13 min old
bbc-world          general  ok  23 items, newest 70 min old
bbc-business       general  ok  57 items, newest 32 min old
npr                general  ok  10 items, newest 31 min old
gnews-breaking     general  ok  61 items, newest 10 min old

news_log: 722 new headlines, 1 feeds failed, file now 722 lines
```
(exit 0)
```

## 2026-11-16 04:34:01 tasks/queue/120-regime-and-schema.sh
```
# Kalshi regime days (queue 120, Mon 16 04:34, practice money only)

```
WALLET CURVE v_hold_s500 (pretend money, after fees): 750 settled rounds, Sat 07 10:30 to Mon 16 04:15, 0 unsettled skipped
  profit now -8313.75 | peak +7352.57 (Mon 09 03:00) | worst drop 18877.85 (Mon 09 03:00 -> Sun 15 19:46) | drop right now 15666.32 from the peak
  wins 462 (62%), avg win +191.42, avg loss -335.94, avg stake 238.53, avg entry price 54.7 c
  entry price  0- 40 c: 153 rounds, won  20%, profit  -4622.26
  entry price 40- 60 c: 225 rounds, won  64%, profit   -787.39
  entry price 60- 80 c: 368 rounds, won  77%, profit  -2902.38
  entry price 80-100 c:   4 rounds, won  75%, profit     -1.72
  bet UP  : 364 rounds, won  58%, profit  -8433.81
  bet DOWN: 386 rounds, won  65%, profit   +120.06
  5 best rounds: +2621, +2620, +2620, +2430, +2258  (= -151% of total profit)
  5 worst rounds: -500, -500, -500, -500, -500
  longest losing streak: 6 rounds
  by hour (local): 00:-1593(35)  01:-237(33)  02:+387(31)  03:+1839(31)  04:-1278(33)  05:+861(31)  06:-2591(31)  07:-4341(29)  08:+55(29)  09:-1953(29)  10:-676(29)  11:+1805(32)  12:-1726(30)  13:+1835(31)  14:-1058(31)  15:+1008(27)  16:-4058(30)  17:-2349(

LATEST 30 ROUNDS (time, bet, contracts, avg price c, stake, result, profit, running total)
  Sun 15 20:16  DOWN    7 @ 72c  stake      5  result UP       -5.14  total -11382.81
  Sun 15 20:32  DOWN    8 @ 71c  stake      6  result DOWN     +2.20  total -11380.61
  Sun 15 20:46  UP   3120 @ 15c  stake    472  result UP    +2620.05  total  -8760.56
  Sun 15 21:06  DOWN  624 @ 79c  stake    492  result UP     -499.60  total  -9260.16
  Sun 15 21:20  DOWN    8 @ 71c  stake      6  result DOWN     +2.20  total  -9257.96
  Sun 15 21:32  DOWN  624 @ 79c  stake    492  result DOWN   +124.48  total  -9133.48
  Sun 15 21:47  DOWN  623 @ 79c  stake    492  result UP     -499.35  total  -9632.83
  Sun 15 22:30  DOWN  624 @ 79c  stake    492  result DOWN   +124.48  total  -9508.35
  Sun 15 22:46  DOWN  699 @ 70c  stake    489  result DOWN   +199.42  total  -9308.93
  Sun 15 23:00  DOWN  637 @ 77c  stake    492  result DOWN   +137.44  total  -9171.49
  Sun 15 23:30  DOWN    7 @ 75c  stake      5  result DOWN     +1.65  total  -9169.84
  Sun 15 23:47  DOWN    7 @ 72c  stake      5  result DOWN     +1.86  total  -9167.98
  Mon 16 00:00  DOWN  699 @ 70c  stake    489  result DOWN   +199.42  total  -8968.56
  Mon 16 00:16  UP      7 @ 74c  stake      5  result UP       +1.72  total  -8966.84
  Mon 16 00:32  UP      7 @ 72c  stake      5  result UP       +1.86  total  -8964.98
  Mon 16 00:45  UP      8 @ 66c  stake      5  result UP       +2.59  total  -8962.39
  Mon 16 01:00  UP   2046 @ 19c  stake    393  result DOWN   -414.82  total  -9377.21
  Mon 16 01:15  UP      8 @ 69c  stake      6  result UP       +2.36  total  -9374.85
  Mon 16 01:30  DOWN    8 @ 70c  stake      6  result UP       -5.72  total  -9380.57
  Mon 16 01:45  DOWN 2350 @ 20c  stake    474  result UP     -499.98  total  -9880.55
  Mon 16 02:00  DOWN    7 @ 77c  stake      5  result DOWN     +1.52  total  -9879.03
  Mon 16 02:17  DOWN  625 @ 79c  stake    493  result DOWN   +125.07  total  -9753.96
  Mon 16 02:31  UP      9 @ 60c  stake      5  result UP       +3.44  total  -9750.52
  Mon 16 02:46  UP   2927 @ 16c  stake    472  result DOWN   -499.98  total -10250.50
  Mon 16 03:00  UP    797 @ 61c  stake    487  result DOWN   -499.92  total -10750.42
  Mon 16 03:15  DOWN 2350 @ 20c  stake    474  result UP     -499.89  total -11250.31
  Mon 16 03:31  UP   3121 @ 15c  stake    472  result UP    +2621.01  total  -8629.30
  Mon 16 03:45  DOWN  810 @ 60c  stake    486  result DOWN   +310.21  total  -8319.09
  Mon 16 04:00  UP      8 @ 66c  stake      5  result UP       +2.59  total  -8316.50
  Mon 16 04:15  UP      8 @ 64c  stake      5  result UP       +2.75  total  -8313.75

RUNNING TOTAL every 10 rounds: -502, +970, -1256, +63, +629, +517, +1303, +1506, -344, +1132, +1947, +5603, +4280, +1293, +2535, +5245, +6723, +4854, +4529, +2030, +1031, +1019, -308, -529, -2492, -4489, -4875, -2437, -4078, -4510, -7006, -7773, -8725, -6354, 
REGIME DAYS (pretend money, fees in). Run Mon 16 04:34
label rule: wild = day range 4%+ or hourly vol 0.45%+; trending = range 2.2%+ and mostly one direction; else calm

day         label       move%  range%  vol/h  s250 pnl   news(n/bad/shock)
2026-10-06  wild        -2.50    3.50   2.77        +0   0/0/0
2026-10-07  wild        -1.77    2.48   2.64        +0   1/0/0
2026-10-08  wild        -0.54    3.42   3.47        +0   2/0/0
2026-10-09  wild        +0.53    1.55   2.30        +0   1/0/0
2026-10-10  wild        +0.40    0.63   0.99        +0   0/0/0
2026-10-11  wild        +1.32    1.44   1.83        +0   0/0/0
2026-10-12  wild        -0.80    3.84   3.00        +0   0/0/0
2026-10-13  wild        +0.44    1.43   2.65        +0   2/0/0
2026-10-14  wild        -2.56    4.45   4.13        +0   1/0/0
2026-10-15  wild        +0.61    3.35   3.56        +0   1/0/0
2026-10-16  wild        -0.96    2.53   2.90        +0   1/1/1
2026-10-17  wild        +0.31    1.47   1.65        +0   0/0/0
2026-10-18  wild        +1.23    2.60   2.31        +0   0/0/0
2026-10-19  wild        -0.71    2.32   2.81        +0   0/0/0
2026-10-20  wild        +0.91    2.46   2.98        +0   1/0/0
2026-10-21  wild        +0.11    2.76   2.99        +0   1/0/0
2026-10-22  wild        -1.64    2.43   2.75        +0   0/0/0
2026-10-23  wild        -0.91    1.84   2.65        +0   1/0/0
2026-10-24  wild        +0.05    2.17   2.21        +0   0/0/0

---- data file field names (keys only) ----
== trades.jsonl
  keys: ['a', 'ask', 'bal', 'bid', 'c', 'd', 'g', 'live', 'px', 'q', 's', 'side', 't', 'ticker', 'v', 'why']
== sim_windows.jsonl
  keys: ['hold_pnl', 'hour', 'outcome', 'pnl', 'src', 'staked', 'strat', 't', 'trades']
== calls.jsonl
  keys: ['call', 'conf', 'hi', 'kalshi_yes', 'lo', 'locked_at', 'outcome', 'pnl', 'price0', 'price1', 'score', 'signals(exit 0)
```

## 2026-11-16 04:37:01 tasks/queue/121-regime-days-fixed.sh
```
# Kalshi regime days (queue 121, Mon 16 04:37, practice money only)

```
REGIME DAYS (pretend money, fees in). Run Mon 16 04:37
label rule: wild = day range 4%+ or hourly vol 0.5%+; trending = range 2.2%+ and mostly one direction; else calm

day         label       move%  range%  vol/h  s250 pnl   news(n/bad/shock)
2026-10-06  trending    -2.56    3.26   0.40        +0   0/0/0
2026-10-07  calm        -1.76    2.18   0.32        +0   1/0/0
2026-10-08  calm        -0.50    3.23   0.42        +0   2/0/0
2026-10-09  calm        +0.43    1.23   0.26        +0   1/0/0
2026-10-10  calm        +0.40    0.62   0.12        +0   0/0/0
2026-10-11  calm        +1.29    1.37   0.23        +0   0/0/0
2026-10-12  calm        -0.94    3.62   0.37        +0   0/0/0
2026-10-13  calm        +0.42    1.39   0.35        +0   2/0/0
2026-10-14  wild        -2.47    4.05   0.55        +0   1/0/0
2026-10-15  calm        +0.63    3.31   0.46        +0   1/0/0
2026-10-16  calm        -1.06    2.45   0.37        +0   1/1/1
2026-10-17  calm        +0.25    1.22   0.20        +0   0/0/0
2026-10-18  calm        +1.24    2.53   0.29        +0   0/0/0
2026-10-19  calm        -0.57    2.26   0.34        +0   0/0/0
2026-10-20  calm        +0.90    2.35   0.38        +0   1/0/0
2026-10-21  calm        +0.01    2.73   0.39        +0   1/0/0
2026-10-22  trending    -1.60    2.36   0.33        +0   0/0/0
2026-10-23  calm        -0.96    1.71   0.33        +0   1/0/0
2026-10-24  calm        +0.10    2.17   0.29        +0   0/0/0
2026-10-25  calm        -1.01    1.81   0.34        +0   0/0/0
2026-10-26  calm        -0.51    1.43   0.35        +0   0/0/0
2026-10-27  calm        +1.44    2.15   0.31        +0   1/0/0
2026-10-28  calm        -0.82    2.45   0.35        +0   1/1/0
2026-10-29  wild        -2.67    6.70   0.60        +0   2/0/1
2026-10-30  trending    -1.57    2.97   0.43        +0   1/0/0
2026-10-31  calm        +0.77    0.84   0.16        +0   0/0/0
2026-11-01  calm        +0.69    1.32   0.23        +0   0/0/0
2026-11-02  trending    -2.13    2.28   0.38        +0   0/0/0
2026-11-03  trending    +1.52    2.92   0.43        +0   1/0/0
2026-11-04  wild        +3.26    4.12   0.51        +0   0/0/0
2026-11-05  wild        -5.90    6.69   0.61        +0   2/1/0
2026-11-06  calm        +0.53    1.42   0.39        +0   0/0/0
2026-11-07  calm        -0.31    0.78   0.12      +885   0/0/0
2026-11-08  trending    -1.74    2.74   0.47      +351   0/0/0
2026-11-09  calm        +0.39    2.32   0.44      -295   1/0/0
2026-11-10  calm        -1.12    2.84   0.47     -3097   6/1/0
2026-11-11  calm        -0.39    1.73   0.42      +597   8/0/0
2026-11-12  wild        -7.38    7.54   0.55     -1809   39/5/2
2026-11-13  wild        -1.50    5.01   0.62      -245   93/21/10
2026-11-14  wild        -3.99    7.95   0.82     -1375   50/10/4
2026-11-15  wild        +0.23    3.19   0.66      -956   308/111/69

STRATEGY BY KIND OF DAY: total profit (rounds) | profit per round
 CALM (27 days)
   v_hold_s250                -1911 ( 291) |  -6.57 per round
   v_hold_s250_cheap100       -1582 ( 198) |  -7.99 per round
   v_hold_s250_agree          -2251 ( 176) | -12.79 per round
   v_hold_s100                 -963 ( 291) |  -3.31 per round
   hold                        -126 ( 436) |  -0.29 per round
   v_edge10_s100              +1917 (  70) | +27.38 per round
   v_hold_s500                -4502 ( 291) | -15.47 per round
 TRENDING (6 days)
   v_hold_s250                 +351 (  95) |  +3.69 per round
   v_hold_s100                  +17 (  95) |  +0.17 per round
   hold                        -228 ( 188) |  -1.21 per round
   v_hold_s500                +1219 (  95) | +12.83 per round
 WILD (8 days)
   v_hold_s250                -4385 ( 346) | -12.67 per round
   v_hold_s250_cheap100       -1810 ( 346) |  -5.23 per round
   v_hold_s250_agree          -2514 ( 304) |  -8.27 per round
   v_hold_s100                -1307 ( 346) |  -3.78 per round
   hold                         -47 ( 533) |  -0.09 per round
   v_edge10_s100              -1080 ( 123) |  -8.78 per round
   v_hold_s500                -5885 ( 346) | -17.01 per round

(few days per kind means this is a first look only; judge by unseen days.)

---- data file field names (keys only) ----
== calls.jsonl
  keys: ['call', 'conf', 'hi', 'kalshi_yes', 'lo', 'locked_at', 'outcome', 'pnl', 'price0', 'price1', 'score', 'signals', 'src', 'start', 'strike', 'ticker']
   signals -> ['bigtrades', 'book', 'fng', 'funding', 'levels', 'momentum', 'news', 'trend_1h', 'trend_24h', 'trend_4h', 'trend_7d', 'trend_h', 'trend_w', 'whales']
```
(exit 0)
```
