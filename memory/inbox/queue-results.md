t repr     : MemoryError()
lost sys.stderr
(exit 0)
```

## 2026-11-06 14:19:01 tasks/queue/081-maker-study2-light.sh
```
Mem:            8058        2626        2423          74        3168        5431
# Stricter maker study (fills need a real trade on the tape), last 3 days

Rounds with a full recording, a tape and a real result: **28**. Orders are 1 contract; post 1c above the best bid; wait 120 s; hold to the result.

| entry | possible orders | skipped (spread under 2c) | filled | fill rate | win rate (filled) | win rate (all posted) | avg maker price | maker profit/$ (1.75% fee) | maker profit/$ (0 fee) | taker profit/$ same orders | taker profit/$ filled only |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 60 s in | 0 | 56 | 0 | | | | | | | | |
| 120 s in | 0 | 56 | 0 | | | | | | | | |
| 180 s in | 0 | 56 | 0 | | | | | | | | |

## How to read it

- Fill rate: the share of resting orders a real seller actually hit. The first study assumed much higher.
- If the win rate of FILLED orders is lower than for ALL posted orders, we get filled mostly when we are wrong (adverse selection) and the maker saving is partly an illusion.
- 'taker profit/$ filled only' is the fair comparison: the same orders that filled, bought at the ask instead. Maker beats taker only if maker profit/$ is higher there.
- The 1.75% maker fee is from one article (dev.to) and should be confirmed with a real fill. Practice only; sample is a few hundred orders, so small differences are noise.
(exit 0)
```

## 2026-11-06 14:20:31 tasks/queue/082-longshot-test.sh
```
# Longshot hypothesis test (cheap side 3 to 7 minutes out), last 5 days

Rounds with a full recording and a real result: **450**.

| seconds left | price ceiling | bets | wins | avg price | profit per $ | 90% range (bootstrap) | older half | newer half | days positive |
|---|---|---|---|---|---|---|---|---|---|
| 420 | 10c | 81 | 5 | 6c | -4% | -63% to +72% | +82% (42) | -100% (39) | 1 of 5 |
| 420 | 15c | 114 | 7 | 8c | -27% | -69% to +20% | +35% (55) | -80% (59) | 1 of 5 |
| 420 | 20c | 157 | 18 | 11c | +3% | -31% to +43% | +42% (72) | -28% (85) | 1 of 5 |
| 300 | 10c | 108 | 6 | 6c | -3% | -62% to +60% | +97% (49) | -72% (59) | 1 of 5 |
| 300 | 15c | 135 | 12 | 7c | +25% | -27% to +83% | +91% (66) | -39% (69) | 4 of 5 |
| 300 | 20c | 173 | 17 | 10c | +2% | -35% to +40% | +41% (83) | -32% (90) | 3 of 5 |
| 240 | 10c | 103 | 2 | 6c | -65% | -100% to -26% | -62% (51) | -68% (52) | 1 of 5 |
| 240 | 15c | 128 | 6 | 7c | -34% | -77% to +11% | +15% (64) | -79% (64) | 3 of 5 |
| 240 | 20c | 157 | 14 | 9c | -4% | -40% to +36% | +33% (80) | -44% (77) | 3 of 5 |
| 180 | 10c | 91 | 6 | 6c | +13% | -60% to +86% | -17% (43) | +37% (48) | 2 of 5 |
| 180 | 15c | 111 | 9 | 7c | +13% | -42% to +78% | +30% (54) | -3% (57) | 3 of 5 |
| 180 | 20c | 140 | 15 | 9c | +13% | -30% to +63% | +31% (66) | -2% (74) | 3 of 5 |

## Per day for the 300 s / 15c rule (Central calendar days)

| day | bets | wins | profit per $ |
|---|---|---|---|
| 11-02 | 3 | 1 | +284% |
| 11-03 | 43 | 4 | +29% |
| 11-04 | 41 | 4 | +51% |
| 11-05 | 38 | 3 | +4% |
| 11-06 | 10 | 0 | -100% |

## Reading this

- Pays about 10 to 1 when it hits, so results swing hard: a few wins decide everything. Trust only a 90% range that stays above zero AND the same sign in both halves and on most days.
- Practice only; nothing changes in the agent. If it holds, the next step is a small forward test as its own practice strategy, small stakes.
(exit 0)
```

## 2026-11-06 15:16:01 tasks/queue/083-series-catalog.sh
```
started; progress so far:
(exit 0)
```

## 2026-11-06 15:37:02 tasks/queue/084-series-nightly-install.sh
```
installed: runs every night at 4:40 am
40 4 * * * flock -n /tmp/series_catalog.lock bash $HOME/starship/tasks/series_catalog_daily.sh >> $HOME/market-data/series_catalog.log 2>&1 # series-catalog
== BTC lag-1 check
rounds: 2936 span days: 31.0 UP share: 48.6%
all                    P(UP|prev UP)=47.6% (n=1424)  P(UP|prev DOWN)=49.4% (n=1506)  gap=-1.8 pts  +-1.8 (1 SE)  z=-1.0
older half             P(UP|prev UP)=49.5% (n=734)  P(UP|prev DOWN)=50.5% (n=731)  gap=-1.0 pts  +-2.6 (1 SE)  z=-0.4
newer half             P(UP|prev UP)=45.7% (n=690)  P(UP|prev DOWN)=48.4% (n=775)  gap=-2.7 pts  +-2.6 (1 SE)  z=-1.0
after UP,UP            P(UP)=46.7% (n=677)
after DOWN,DOWN        P(UP)=49.9% (n=759)
CT hours 00-04         P(UP|prev UP)=50.0% (n=228)  P(UP|prev DOWN)=49.3% (n=225)  gap=+0.7 pts  +-4.7 (1 SE)  z=+0.1
CT hours 04-08         P(UP|prev UP)=44.2% (n=224)  P(UP|prev DOWN)=45.7% (n=269)  gap=-1.5 pts  +-4.5 (1 SE)  z=-0.3
CT hours 08-12         P(UP|prev UP)=45.6% (n=241)  P(UP|prev DOWN)=51.4% (n=255)  gap=-5.7 pts  +-4.5 (1 SE)  z=-1.3
CT hours 12-16         P(UP|prev UP)=45.5% (n=244)  P(UP|prev DOWN)=53.2% (n=252)  gap=-7.7 pts  +-4.5 (1 SE)  z=-1.7
CT hours 16-20         P(UP|prev UP)=51.5% (n=237)  P(UP|prev DOWN)=46.7% (n=259)  gap=+4.8 pts  +-4.5 (1 SE)  z=+1.1
CT hours 20-24         P(UP|prev UP)=48.8% (n=250)  P(UP|prev DOWN)=50.4% (n=246)  gap=-1.6 pts  +-4.5 (1 SE)  z=-0.4
(exit 0)
```

## 2026-11-06 20:10:01 tasks/queue/085-pihole-clients.sh
```
== devices seen in the last 24 h (address, lookups, last seen, blocked)
OCI runtime exec failed: exec failed: unable to start container process: exec: "sqlite3": executable file not found in $PATH
== names Pi-hole knows (address, name)
OCI runtime exec failed: exec failed: unable to start container process: exec: "sqlite3": executable file not found in $PATH
== local DNS names set (dns.hosts)
[]
(exit 0)
```

## 2026-11-06 20:13:01 tasks/queue/086-pihole-clients.sh
```
== devices seen in the last 24 h (address, lookups, last seen, blocked)
127.0.0.1|9852|2026-11-06 20:12:29|0
192.168.1.142|1435|2026-11-06 20:12:16|375
192.168.1.228|1009|2026-11-06 17:00:25|246
192.168.1.240|560|2026-11-06 20:06:51|52
192.168.1.130|127|2026-11-06 20:11:37|70
== names Pi-hole knows (address, name)
127.0.0.1|localhost|virtual interface
::1|localhost|virtual interface
fe80::e197:65e6:719b:399c||Raspberry Pi (Trading) Ltd
172.17.0.1||
0.0.0.0||virtual interface
ff02::16||virtual interface
192.168.1.107||Raspberry Pi (Trading) Ltd
fe80::469:a9ff:fed0:ac9f||
fe80::1034:1fff:fe35:38b9||
fe80::a405:93ff:fefe:aa3d||
fe80::98b3:90ff:fedc:483b||
192.168.1.142||
192.168.1.130||Cloud Network Technology Singapore Pte. Ltd.
fe80::a045:3bb6:47e1:55f3||Cloud Network Technology Singapore Pte. Ltd.
192.168.1.240||
192.168.1.228||
fe80::c6e:c5ff:fe19:b9b5||
fe80::1831:65ff:fe10:4206||
fe80::8064:fff:fe79:13c4||
fe80::44aa:1cff:fe5a:a4cb||
== local DNS names set (dns.hosts)
[]
(exit 0)
```

## 2026-11-06 20:16:01 tasks/queue/087-pihole-names.sh
```
[ 192.168.1.107 pi-hub, 192.168.1.142 kylar-iphone, 192.168.1.228 sharee-iphone, 192.168.1.240 warren-ipad, 192.168.1.130 living-room-tv ]
== dns.hosts now
[ 192.168.1.107 pi-hub, 192.168.1.142 kylar-iphone, 192.168.1.228 sharee-iphone, 192.168.1.240 warren-ipad, 192.168.1.130 living-room-tv ]
== name lookups via Pi-hole
kylar-iphone -> Traceback (most recent call last):
sharee-iphone -> Traceback (most recent call last):
warren-ipad -> Traceback (most recent call last):
living-room-tv -> Traceback (most recent call last):
pi-hub -> Traceback (most recent call last):
== reverse lookup of the iPad
Traceback (most recent call last):
(exit 0)
```

## 2026-11-06 20:22:01 tasks/queue/088-pihole-names-refresh.sh
```
ALL
  networkflush        Flush information stored in Pi-hole's network tables
                        Add '--arp' to additionally flush the ARP table 
== names now (address|name)
192.168.1.106|
192.168.1.107|pi-hub
192.168.1.142|kylar-iphone
192.168.1.228|sharee-iphone
192.168.1.130|living-room-tv
192.168.1.240|warren-ipad
== DNS still answering?
  [✓] FTL is listening on port 53
     [✓] UDP (IPv4)
     [✓] TCP (IPv4)
(exit 0)
```

## 2026-11-06 20:31:01 tasks/queue/089-ha-notify-targets.sh
REFUSED: contains a command on the deny list

## 2026-11-06 20:43:01 tasks/queue/090-pihole-activity-now.sh
```
wrote /home/kylarlovelady/crew-web/activity.html devices: kylar-iphone, living-room-tv, sharee-iphone, warren-ipad unknown domains: 137
-rw-rw-r-- 1 kylarlovelady kylarlovelady 31235 Nov  6 20:43 /home/kylarlovelady/crew-web/activity.html
(exit 0)
```

## 2026-11-07 10:22:01 tasks/queue/091-kalshi-review-long.sh
```
=== review last 72 hours
TRADE REVIEW, last 72 hours: 10992 (strategy, round) results from 242 rounds with full recordings.

EVERY STRATEGY (pretend money): rounds | profit | win%% | profit per $ staked
  v_hold         198    +790.65   55%  +18.1%
  v_x60222031    167    +427.65   51%   +7.8%
  v_x96220861    175    +401.29   46%   +6.0%
  v_one_shot     197    +199.29   55%  +14.1%
  v_x88221261    131    +185.64   39%   +4.4%
  v_late         145    +185.07   39%   +3.8%
  v_x12229262    159    +175.03   50%   +4.9%
  v_x64216772    197    +163.11   55%   +9.3%
  hold           241    +151.58   56%   +6.1%
  v_x60222032    175    +146.60   55%  +10.3%
  v_x40223631    166    +109.84   52%   +8.0%
  v_x40223632    187     +84.45   45%   +4.4%
  v_no_cut       198     +14.35   51%   +0.2%
  v_snipe_all      1      +2.70  100%   +0.9%
  v_x80218932    188     -11.97   48%   -0.6%
  v_x64216771    198     -17.52   42%   -0.2%
  v_flow_flip    227     -18.27   35%   -0.1%
  v_x96220872    176     -44.22   38%   -0.9%
  v_snipe         68     -62.94   79%  -14.2%
  v_x24220781    179     -68.39   47%   -3.6%
  v_cut_loose    198     -82.66   45%   -1.4%
  v_x76218991    163     -96.05   46%   -6.0%
  v_x76218992    163     -96.05   46%   -6.0%
  v_x8220762     183    -103.57   42%   -1.8%
  v_x52220781    131    -103.59   40%   -2.6%
  v_x28219982    199    -104.77   40%   -2.1%
  trend          212    -134.06   39%   -2.6%
  v_x219211      194    -166.67   39%   -2.4%
  v_x68220542    172    -167.64   37%   -4.1%
  v_x72222451    191    -175.71   39%   -2.6%
  mood           207    -180.27   41%   -2.3%
  v_x36215122    119    -180.92   42%   -5.6%
  swing          241    -190.95   40%   -1.6%
  v_x80218931    187    -204.65   39%   -3.1%
  v_x16217721    204    -210.09   30%   -2.1%
  flow           209    -216.35   41%   -4.0%
  v_x52220782    127    -218.38   41%   -5.9%
  v_x36215121    192    -229.13   36%   -3.5%
  v_x28219981    200    -257.56   40%   -2.5%
  signals        203    -285.88   41%   -6.2%
  v_x12229261    159    -319.39   35%   -8.9%
  v_x219212      195    -328.46   38%   -3.3%
=== review last 168 hours
TRADE REVIEW, last 168 hours: 12088 (strategy, round) results from 366 rounds with full recordings.

EVERY STRATEGY (pretend money): rounds | profit | win%% | profit per $ staked
  v_x60222031    167    +427.65   51%   +7.8%
  v_x96220861    175    +401.29   46%   +6.0%
  v_x88221261    131    +185.64   39%   +4.4%
  v_x12229262    159    +175.03   50%   +4.9%
  v_x64216772    197    +163.11   55%   +9.3%
  v_x60222032    175    +146.60   55%  +10.3%
  v_hold         232    +127.74   53%   +2.1%
  v_x40223631    166    +109.84   52%   +8.0%
  v_x40223632    187     +84.45   45%   +4.4%
  v_snipe_all      1      +2.70  100%   +0.9%
  v_x80218932    188     -11.97   48%   -0.6%
  v_x64216771    198     -17.52   42%   -0.2%
  v_flow_flip    227     -18.27   35%   -0.1%
  v_x96220872    176     -44.22   38%   -0.9%
  v_one_shot     232     -61.36   53%   -3.2%
  v_snipe         68     -62.94   79%  -14.2%
  v_x24220781    179     -68.39   47%   -3.6%
  v_x76218991    163     -96.05   46%   -6.0%
  v_x76218992    163     -96.05   46%   -6.0%
  v_x8220762     183    -103.57   42%   -1.8%
  v_x52220781    131    -103.59   40%   -2.6%
  v_x28219982    199    -104.77   40%   -2.1%
  hold           356    -156.92   53%   -2.3%
  v_x219211      194    -166.67   39%   -2.4%
  v_x68220542    172    -167.64   37%   -4.1%
  v_x72222451    191    -175.71   39%   -2.6%
  v_x36215122    119    -180.92   42%   -5.6%
  v_late         166    -197.33   39%   -2.7%
  v_x80218931    187    -204.65   39%   -3.1%
  v_x16217721    204    -210.09   30%   -2.1%
  v_x52220782    127    -218.38   41%   -5.9%
  v_x36215121    192    -229.13   36%   -3.5%
  v_x28219981    200    -257.56   40%   -2.5%
  v_x12229261    159    -319.39   35%   -8.9%
  v_x219212      195    -328.46   38%   -3.3%
  v_mood_flip    223    -334.60   39%   -3.3%
  v_x32221882    176    -335.96   39%   -3.8%
  v_x68220541    173    -352.75   39%   -4.1%
  v_x44219232    191    -358.58   39%   -3.7%
  v_x32221881    176    -457.93   39%   -4.6%
  v_x16217722    187    -500.01   33%  -10.7%
  v_no_cut       232    -515.59   50%   -6.4%
=== config now
run.json {"active": true, "id": 1793935799, "strategy": "auto", "start": 1000.0}
config.json {"weights": {"book": 0.25, "momentum": 0.2, "whales": 0.2, "bigtrades": 0.15, "news": 0.1, "fng": 0.05, "funding": 0.05}, "threshold": 12.0, "min_bet": 5.0, "cap": 0, "edge_min": 0.03, "max_trades": 6.0, "slice": 0.1, "min_price": 0.08, "max_price": 0.92, "aggression": 50.0, "floor": 0, "entry_max": 0.8, "entry_min": 0.15}
(exit 0)
```

## 2026-11-07 10:25:02 tasks/queue/092-take-profit-study.sh
```

Average over every entry time and side: hold -3.9%; take +15% -8.0%; take +25% -8.0%; take +40% -7.4%.

Reading: if take-profit rows beat the 'hold' row of the same entry and side in both halves, the idea helps; if not, it is just selling winners early and paying the fee twice.
108 /home/kylarlovelady/starship/memory/inbox/take-profit-study.md
(exit 0)
```

## 2026-11-07 10:28:02 tasks/queue/093-take-profit-study-wide.sh
```

Rules positive in the whole sample, in BOTH halves, and with a 90% range above zero: **0** of 264 (with this many rules tried, a couple would pass by luck alone).

Average over every entry time and side: hold -3.9%; take +5% -8.1%; take +10% -7.9%; take +15% -8.0%; take +20% -8.1%; take +25% -8.0%; take +30% -7.9%; take +40% -7.4%; take +50% -6.8%; take +75% -6.4%; take +100% -5.9%.

Reading: if take-profit rows beat the 'hold' row of the same entry and side in both halves, the idea helps; if not, it is just selling winners early and paying the fee twice.
(exit 0)
```

## 2026-11-07 10:29:30 tasks/queue/094-run-hold-to-end.sh
```
before: {'active': True, 'strategy': 'auto', 'live': None, 'start': 1000.0}
after: {'active': True, 'strategy': 'v_hold', 'live': None, 'start': 1000.0}
(exit 0)
```

## 2026-11-07 12:28:02 tasks/queue/095-jarvis-home-survey.sh
```
== docker
openwakeword  rhasspy/wyoming-openwakeword  Up 33 hours
whisper  rhasspy/wyoming-whisper  Up 33 hours (healthy)
piper  rhasspy/wyoming-piper  Up 33 hours (healthy)
pihole  pihole/pihole:latest  Up 33 hours (healthy)
homeassistant  ghcr.io/home-assistant/home-assistant:stable  Up 33 hours
== units (ExecStart only)
-- hub-satellite: active
User=kylarlovelady
ExecStart=/bin/bash /home/kylarlovelady/wyoming-satellite/run-hub.sh
-- hub-voice: active
User=kylarlovelady
ExecStart=/home/kylarlovelady/hub-voice/.venv/bin/python /home/kylarlovelady/hub-voice/voiced.py daemon
-- hub-watchdog: active
ExecStart=/usr/bin/python3 /usr/local/bin/hub-watchdog.py
== satellite process
root        2687  1-09:13:31 .venv/bin/python3 -m wyoming_piper --uri tcp://0.0.0.0:10200 --data-dir /data --voice en_US-lessac-medium
root        2854  1-09:13:30 .venv/bin/python3 -m wyoming_faster_whisper --uri tcp://0.0.0.0:10300 --data-dir /data --device cpu --model base-int8 --language en
root        2859  1-09:13:30 .venv/bin/python3 -m wyoming_openwakeword --uri tcp://0.0.0.0:10400 --preload-model alexa --threshold 0.7
kylarlo+    2951  1-09:13:30 /bin/bash /home/kylarlovelady/wyoming-satellite/run-hub.sh
kylarlo+    3014  1-09:13:30 /home/kylarlovelady/wyoming-satellite/.venv/bin/python3 -m wyoming_satellite --name main hub --debug-recording-dir /home/kylarlovelady/voice-data/home-mic --uri tcp://127.0.0.1:10700 --mic-command /home/kylarlovelady/hub-mic.py plughw:3,0 --snd-command aplay -D plughw:2,0 -r 22050 -c 1 -f S16_LE -t raw --wake-uri tcp://127.0.0.1:10400 --wake-word-name hey_jarvis --detect-command bash -c "
== audio capture devices
**** List of CAPTURE Hardware Devices ****
card 3: AC44 [MXL AC-44], device 0: USB Audio [USB Audio]
  Subdevices: 0/1
  Subdevice #0: subdevice #0
== mixer (capture controls)
card2: Simple mixer control 'PCM',0
card3: Simple mixer control 'Mic',0
== groups
kylarlovelady adm dialout cdrom sudo audio video plugdev games users netdev lpadmin docker pironman5 gpio i2c spi render input
== voice-data
total 240
drwx------  5 kylarlovelady kylarlovelady   4096 Nov  5 15:13 .
drwx------ 36 kylarlovelady kylarlovelady   4096 Nov  6 03:14 ..
drwxr-xr-x  2 kylarlovelady kylarlovelady   4096 Nov  5 05:54 clips
-rw-r--r--  1 kylarlovelady kylarlovelady  57716 Nov  7 12:20 conversations.jsonl
-rw-r--r--  1 kylarlovelady kylarlovelady   2426 Nov  5 05:46 events.jsonl
drwxrwxr-x  2 kylarlovelady kylarlovelady   4096 Nov  7 12:20 home-mic
-rw-r--r--  1 kylarlovelady kylarlovelady    111 Nov  5 06:00 hours.jsonl
-rw-------  1 kylarlovelady kylarlovelady    292 Nov  4 22:12 keys.env
-rw-r--r--  1 kylarlovelady kylarlovelady    321 Nov  5 05:26 labels.jsonl
drwxr-xr-x  2 kylarlovelady kylarlovelady  12288 Nov  5 05:54 replies
-rw-r--r--  1 kylarlovelady kylarlovelady    440 Nov  5 05:26 settings.json
-rw-r--r--  1 kylarlovelady kylarlovelady 124749 Nov  6 20:37 trace.jsonl
115581106260969-stt.wav
115581106260969-wake.wav
115944154382670-stt.wav
115944154382670-wake.wav
119162982453665-stt.wav
== satellite log, last 24 h: count of key lines
19 /tmp/sat24.log
9
Nov 06 13:55:16 LoveladyMainAiHub bash[3014]: WARNING:root:Event(type='error', data={'text': 'No text recognized', 'code': 'stt-no-text-recognized'}, payload=None)
Nov 06 13:55:16 LoveladyMainAiHub bash[3014]: INFO:root:Waiting for wake word
Nov 06 17:25:15 LoveladyMainAiHub bash[3014]: INFO:root:Waiting for wake word
Nov 06 17:56:51 LoveladyMainAiHub bash[3014]: INFO:root:Waiting for wake word
Nov 06 17:58:02 LoveladyMainAiHub bash[3014]: INFO:root:Waiting for wake word
Nov 06 17:58:15 LoveladyMainAiHub bash[3014]: INFO:root:Waiting for wake word
Nov 07 11:20:34 LoveladyMainAiHub bash[3014]: WARNING:root:Event(type='error', data={'text': 'No text recognized', 'code': 'stt-no-text-recognized'}, payload=None)
Nov 07 11:20:34 LoveladyMainAiHub bash[3014]: INFO:root:Waiting for wake word
Nov 07 11:26:37 LoveladyMainAiHub bash[3014]: INFO:root:Waiting for wake word
Nov 07 12:20:16 LoveladyMainAiHub bash[3014]: INFO:root:Waiting for wake word
Nov 07 12:20:46 LoveladyMainAiHub bash[3014]: INFO:root:Waiting for wake word
== openwakeword container log tail
INFO:root:Ready
INFO:root:Ready
INFO:root:Ready
INFO:root:Ready
INFO:root:Ready
INFO:root:Ready
INFO:root:Ready
INFO:root:Ready
== tailscale name/ports free?
0.0.0.0:8123
127.0.0.1:10200
127.0.0.1:10300
127.0.0.1:10400
127.0.0.1:8099
100.105.140.126:8097
100.105.140.126:8095
100.105.140.126%tailscale0:8081
[::]:8123
[fd7a:115c:a1e0::2f4c:8c7f]%tailscale0:8081
(exit 0)
```

## 2026-11-07 12:31:01 tasks/queue/096-jarvis-mic-files.sh
REFUSED: sudo is not allowed in queue scripts

## 2026-11-07 12:34:01 tasks/queue/096-jarvis-mic-files.sh
```
== run-hub.sh
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
== hub-mic.py
21 /home/kylarlovelady/hub-mic.py
#!/usr/bin/env python3
import sys, os, subprocess, signal
M = "/home/kylarlovelady/hub-dashboard/muted"
p = subprocess.Popen(["arecord", "-D", sys.argv[1], "-r", "16000", "-c", "1", "-f", "S16_LE", "-t", "raw"],
                     stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
def stop(*a):
    p.terminate()
    sys.exit(0)
signal.signal(signal.SIGTERM, stop)
w = sys.stdout.buffer
try:
    while True:
        d = p.stdout.read(2048)
        if not d:
            break
        w.write(bytes(len(d)) if os.path.exists(M) else d)
        w.flush()
except BrokenPipeError:
finally:
    p.terminate()
== mute mentions
/home/kylarlovelady/hub-voice/voiced.py:210:        print("Enrolling %s. Unmute the mic. Say 'Alexa' then a sentence of 3 or more seconds, 5 times." % name)
/usr/local/bin/hub-lights.py:5:MUTE_FILE = "/home/kylarlovelady/hub-dashboard/muted"
/usr/local/bin/hub-lights.py:21:    if os.path.exists(MUTE_FILE):
/usr/local/bin/hub-oled.py:6:MUTE_FILE = "/home/kylarlovelady/hub-dashboard/muted"
/usr/local/bin/hub-oled.py:85:        if os.path.exists(MUTE_FILE):
/usr/local/bin/hub-oled.py:86:            view = ("muted", dx, dy)
/usr/local/bin/hub-oled.py:108:            elif view[0] == "muted":
/usr/local/bin/hub-oled.py:109:                oled.draw_text("MIC MUTED", view[1], view[2], size=fit_size(oled, "MIC MUTED", 20))
/home/kylarlovelady/hub-mic.py:3:M = "/home/kylarlovelady/hub-dashboard/muted"
== mixer Mic
Simple mixer control 'Mic',0
  Capabilities: cvolume cswitch cswitch-joined
  Capture channels: Front Left - Front Right
  Limits: Capture 0 - 36
  Front Left: Capture 36 [100%] [12.00dB] [on]
  Front Right: Capture 36 [100%] [12.00dB] [on]
== what listens on 8097
LISTEN 0      5                             100.105.140.126:8097       0.0.0.0:*    users:(("python3",pid=2080,fd=3)) 
== wake clips per hour (last 24 h) and conversations
11-05 15 1
11-05 17 3
11-06 02 2
11-06 03 4
11-06 11 1
11-06 13 1
11-06 17 4
11-07 11 2
11-07 12 3
total wake clips 21
== conversations.jsonl keys of last row
['t', 'sid', 'who', 'heard', 'reply', 'secs', 'times']
== trace.jsonl last 3 rows (trimmed)
{"t": 1793908429.312, "sid": "phtnri1w", "kind": "client", "what": "page_visible", "info": ""}
{"t": 1793908431.636, "sid": "phtnri1w", "kind": "client", "what": "page_hidden", "info": ""}
{"t": 1794019030.422, "sid": "phtnri1w", "kind": "client", "what": "page_hidden", "info": ""}
(exit 0)
```

## 2026-11-07 12:40:01 tasks/queue/097-jarvis-install.sh
```
{"muted": false, "unmute_at": null, "state": "idle", "now": 1794076823.6926272, "wake": {"updated": 1794076823.6450362, "threshold": 0.7, "wakes24": 10, "empty24": 3, "talk24": 1, "command24": 6, "wakes7d": 21, "false7d": 14, "by_hour": {"12": {"empty": 1, "talk": 1, "command": 1}, "17": {"empty": 3

LISTEN 0      5                                     0.0.0.0:8098       0.0.0.0:*   
--- watcher report
# Home Jarvis wake-up report (auto, audio stats only)

Updated Sat 12:40. Wake word threshold now: 0.7. Mic muted now: False.

Last 24 h: **10** wake-ups: 3 empty, 1 probably us talking, 6 real commands. Last 7 days: 21 wake-ups, 14 false.

| hour | empty | talk | command |
|---|---|---|---|
| 02:00 | 2 | 0 | 0 |
| 03:00 | 4 | 0 | 0 |
| 11:00 | 2 | 0 | 1 |
| 12:00 | 1 | 1 | 1 |
(exit 0)
```

## 2026-11-07 23:07:02 tasks/queue/098-jarvis-tune-080.sh
```
old threshold: 0.7 new: 0.8
container up with threshold 0.8
active
openwakeword Up 14 seconds
active
(exit 0)
```

## 2026-11-08 13:01:01 tasks/queue/099-cad-setup.sh
```
manifold3d ok
trimesh 5.2.0 numpy 2.5.4
boolean test volume 968.8 genus 0
openscad on this Pi: not installed
arch: aarch64; python: Python 3.13.5
(exit 0)
```

## 2026-11-08 13:13:01 tasks/queue/100-build-case-v6.sh
```
node is not installed on this Pi
(exit 0)
```

## 2026-11-08 13:46:01 tasks/queue/101-slicer-probe.sh
```
arch: aarch64  os: Debian GNU/Linux 13 (trixie)  ram: 8058 MB  disk free: 200G
flatpak: no
snap: no
orca-slicer: no
bambu-studio: no
prusa-slicer: no
slic3r: no
mosquitto_pub: no
curl: /usr/bin/curl
prusa-slicer:
  Installed: (none)
  Candidate: 2.9.2+dfsg-1
slic3r:
  Installed: (none)
  Candidate: (none)
ModuleNotFoundError: No module named 'paho'
printers seen on LAN (ssdp, 4s):
none: TimeoutError
(exit 0)
```

## 2026-11-08 20:31:01 tasks/queue/102-kalshi-wallet-curve.sh
```
wrote /home/kylarlovelady/starship/memory/inbox/kalshi-wallet-curve.md (66 lines)
# Kalshi wallet curve (queue 102, Sun 08 20:31, practice money only)

```
WALLET CURVE v_hold_s500 (pretend money, after fees): 134 settled rounds, Sat 07 10:30 to Sun 08 20:15, 0 unsettled skipped
  profit now +2782.58 | peak +6103.14 (Sun 08 16:30) | worst drop 3320.56 (Sun 08 16:30 -> Sun 08 20:15) | drop right now 3320.56 from the peak
  wins 85 (63%), avg win +238.66, avg loss -357.21, avg stake 307.48, avg entry price 56.1 c
  entry price  0- 40 c:  20 rounds, won  30%, profit  +2012.40
  entry price 40- 60 c:  37 rounds, won  54%, profit   -580.88
  entry price 60- 80 c:  77 rounds, won  77%, profit  +1351.06
  bet UP  :  74 rounds, won  62%, profit   -475.92
  bet DOWN:  60 rounds, won  65%, profit  +3258.50
  5 best rounds: +2430, +1852, +1850, +1029, +545  (= 277% of total profit)
  5 worst rounds: -500, -500, -500, -500, -500
  longest losing streak: 4 rounds
  by hour (local): 00:-291(4)  01:-379(4)  02:+66(4)  03:+601(4)  04:-1095(4)  05:+1058(4)  06:+238(4)  07:-1146(4)  08:-208(4)  09:-304(4)  10:-570(6)  11:+2656(8)  12:-512(8)  13:+1459(8)  14:+2968(8)  15:-1263(7)  16:+292(8)  17:-863(8)  18:+543(8)  19:+33(7)  20:-1754(6)  21:-89(4)  22:+399(4)  23:+943(4)

LATEST 30 ROUNDS (time, bet, contracts, avg price c, stake, result, profit, running total)
  Sun 08 12:45  DOWN   10 @ 50c  stake      5  result UP       -5.18  total  +1926.69
  Sun 08 13:00  DOWN  729 @ 67c  stake    488  result DOWN   +229.28  total  +2155.97
  Sun 08 13:15  UP      9 @ 58c  stake      5  result UP       +3.62  total  +2159.59
  Sun 08 13:30  UP      8 @ 68c  stake      5  result UP       +2.43  total  +2162.02
  Sun 08 13:45  UP    784 @ 62c  stake    487  result UP     +284.44  total  +2446.46
  Sun 08 14:00  UP    930 @ 52c  stake    483  result DOWN   -499.66  total  +1946.80
  Sun 08 14:15  UP   2930 @ 16c  stake    472  result UP    +2430.04  total  +4376.84
  Sun 08 14:30  DOWN   10 @ 50c  stake      5  result DOWN     +4.82  total  +4381.66
  Sun 08 14:45  DOWN    9 @ 57c  stake      5  result DOWN     +3.71  total  +4385.37
  Sun 08 15:00  UP   2927 @ 16c  stake    472  result DOWN   -499.84  total  +3885.53
  Sun 08 15:15  UP   1213 @ 18c  stake    222  result DOWN   -234.77  total  +3650.76
  Sun 08 15:30  DOWN  965 @ 50c  stake    483  result DOWN   +465.20  total  +4115.96
  Sun 08 16:00  UP      7 @ 73c  stake      5  result UP       +1.79  total  +4117.75
  Sun 08 16:15  DOWN 2352 @ 20c  stake    474  result DOWN  +1852.08  total  +5969.83
  Sun 08 16:30  DOWN  633 @ 78c  stake    492  result DOWN   +133.31  total  +6103.14
  Sun 08 16:45  DOWN  709 @ 69c  stake    489  result UP     -499.83  total  +5603.31
  Sun 08 17:00  UP    664 @ 74c  stake    491  result UP     +164.39  total  +5767.70
  Sun 08 17:15  UP      9 @ 59c  stake      5  result UP       +3.53  total  +5771.23
  Sun 08 17:30  UP   1939 @ 25c  stake    477  result DOWN   -499.93  total  +5271.30
  Sun 08 17:45  DOWN    9 @ 62c  stake      6  result DOWN     +3.27  total  +5274.57
  Sun 08 18:00  UP   2928 @ 16c  stake    472  result DOWN   -499.92  total  +4774.65
  Sun 08 18:18  UP      7 @ 77c  stake      5  result UP       +1.52  total  +4776.17
  Sun 08 18:30  DOWN    9 @ 58c  stake      5  result DOWN     +3.62  total  +4779.79
  Sun 08 18:45  UP     10 @ 52c  stake      5  result UP       +4.62  total  +4784.41
  Sun 08 19:00  UP    823 @ 59c  stake    485  result DOWN   -499.43  total  +4284.98
  Sun 08 19:15  UP     10 @ 50c  stake      5  result DOWN     -5.18  total  +4279.80
  Sun 08 19:30  DOWN 3121 @ 15c  stake    472  result UP     -499.87  total  +3779.93
  Sun 08 19:45  UP      8 @ 67c  stake      5  result UP       +2.51  total  +3782.44
  Sun 08 20:00  DOWN 3071 @ 15c  stake    472  result UP     -499.87  total  +3282.57
  Sun 08 20:15  DOWN 2758 @ 17c  stake    473  result UP     -499.99  total  +2782.58

RUNNING TOTAL every 10 rounds: -502, +970, -1256, +63, +629, +517, +1303, +1506, -344, +1132, +1947, +5603, +4280

---- v_hold_s100 (same entries, 1/5 the size) ----
WALLET CURVE v_hold_s100 (pretend money, after fees): 134 settled rounds, Sat 07 10:30 to Sun 08 20:15, 0 unsettled skipped
  profit now +539.46 | peak +1190.39 (Sun 08 16:30) | worst drop 650.93 (Sun 08 16:30 -> Sun 08 20:15) | drop right now 650.93 from the peak
  wins 85 (63%), avg win +50.82, avg loss -77.16, avg stake 65.55, avg entry price 56.2 c
  entry price  0- 40 c:  20 rounds, won  30%, profit   +390.39
  entry price 40- 60 c:  37 rounds, won  54%, profit   -184.77
  entry price 60- 80 c:  77 rounds, won  77%, profit   +333.84
  bet UP  :  74 rounds, won  62%, profit   -259.05
  bet DOWN:  60 rounds, won  65%, profit   +798.51
  5 best rounds: +469, +358, +356, +199, +182  (= 290% of total profit)
  5 worst rounds: -100, -100, -100, -100, -100
  longest losing streak: 4 rounds
  by hour (local): 00:-67(4)  01:-78(4)  02:+8(4)  03:+124(4)  04:-295(4)  05:+212(4)  06:+52(4)  07:-295(4)  08:-36(4)  09:-60(4)  10:-115(6)  11:+652(8)  12:-92(8)  13:+296(8)  14:+659(8)  15:-300(7)  16:+50(8)  17:-207(8)  18:+117(8)  19:+3(7)  20:-355(6)  21:-7(4)  22:+81(4)  23:+192(4)

LATEST 6 ROUNDS (time, bet, contracts, avg price c, stake, result, profit, running total)
```
(exit 0)
```
