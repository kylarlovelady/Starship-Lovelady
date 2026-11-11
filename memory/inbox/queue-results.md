) 
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

## 2026-11-09 04:07:01 tasks/queue/103-kalshi-wallet-curve-overnight.sh
```
wrote /home/kylarlovelady/starship/memory/inbox/kalshi-wallet-curve.md (66 lines)
# Kalshi wallet curve (queue 103, Mon 09 04:07, practice money only)

```
WALLET CURVE v_hold_s500 (pretend money, after fees): 162 settled rounds, Sat 07 10:30 to Mon 09 03:45, 3 unsettled skipped
  profit now +6435.92 | peak +7353.71 (Mon 09 03:00) | worst drop 5307.01 (Sun 08 16:30 -> Sun 08 22:16) | drop right now 917.79 from the peak
  wins 102 (63%), avg win +278.14, avg loss -365.58, avg stake 298.49, avg entry price 54.2 c
  entry price  0- 40 c:  31 rounds, won  32%, profit  +6057.53
  entry price 40- 60 c:  44 rounds, won  61%, profit   -109.43
  entry price 60- 80 c:  87 rounds, won  75%, profit   +487.82
  bet UP  :  88 rounds, won  60%, profit   -914.72
  bet DOWN:  74 rounds, won  66%, profit  +7350.64
  5 best rounds: +2430, +2108, +2107, +1971, +1852  (= 163% of total profit)
  5 worst rounds: -500, -500, -500, -500, -500
  longest losing streak: 4 rounds
  by hour (local): 00:-785(7)  01:+852(8)  02:+2046(7)  03:+1791(8)  04:-1095(4)  05:+1058(4)  06:+238(4)  07:-1146(4)  08:-208(4)  09:-304(4)  10:-570(6)  11:+2656(8)  12:-512(8)  13:+1459(8)  14:+2968(8)  15:-1263(7)  16:+292(8)  17:-863(8)  18:+543(8)  19:+33(7)  20:-2252(8)  21:-1081(8)  22:+2004(8)  23:+575(8)

LATEST 30 ROUNDS (time, bet, contracts, avg price c, stake, result, profit, running total)
  Sun 08 20:00  DOWN 3071 @ 15c  stake    472  result UP     -499.87  total  +3282.57
  Sun 08 20:15  DOWN 2758 @ 17c  stake    473  result UP     -499.99  total  +2782.58
  Sun 08 20:31  DOWN    8 @ 66c  stake      5  result DOWN     +2.59  total  +2785.17
  Sun 08 20:45  UP   2757 @ 17c  stake    473  result DOWN   -499.95  total  +2285.22
  Sun 08 21:00  DOWN   10 @ 50c  stake      5  result DOWN     +4.82  total  +2290.04
  Sun 08 21:15  DOWN  729 @ 67c  stake    488  result UP     -499.41  total  +1790.63
  Sun 08 21:30  DOWN 2351 @ 20c  stake    474  result UP     -499.90  total  +1290.73
  Sun 08 21:45  DOWN    7 @ 72c  stake      5  result DOWN     +1.86  total  +1292.59
  Sun 08 22:00  UP      9 @ 59c  stake      5  result UP       +3.53  total  +1296.12
  Sun 08 22:16  UP   2474 @ 19c  stake    473  result DOWN   -499.99  total   +796.13
  Sun 08 22:30  DOWN 2607 @ 18c  stake    473  result DOWN  +2107.13  total  +2903.26
  Sun 08 22:46  UP      9 @ 60c  stake      5  result DOWN     -5.56  total  +2897.70
  Sun 08 23:00  DOWN  634 @ 78c  stake    492  result DOWN   +134.10  total  +3031.80
  Sun 08 23:15  UP   2758 @ 17c  stake    473  result DOWN   -499.89  total  +2531.91
  Sun 08 23:30  UP      9 @ 60c  stake      5  result DOWN     -5.56  total  +2526.35
  Sun 08 23:45  UP      9 @ 58c  stake      5  result UP       +3.62  total  +2529.97
  Mon 09 00:00  UP      9 @ 56c  stake      5  result UP       +3.80  total  +2533.77
  Mon 09 00:15  DOWN    7 @ 76c  stake      5  result DOWN     +1.59  total  +2535.36
  Mon 09 00:45  DOWN  763 @ 64c  stake    487  result UP     -499.65  total  +2035.71
  Mon 09 01:00  UP   2471 @ 19c  stake    473  result DOWN   -499.95  total  +1535.76
  Mon 09 01:15  DOWN 1780 @ 27c  stake    478  result DOWN  +1280.07  total  +2815.83
  Mon 09 01:30  UP      9 @ 61c  stake      5  result UP       +3.36  total  +2819.19
  Mon 09 01:45  DOWN  947 @ 51c  stake    483  result DOWN   +447.15  total  +3266.34
  Mon 09 02:00  UP   2471 @ 19c  stake    473  result UP    +1971.08  total  +5237.42
  Mon 09 02:16  UP      9 @ 60c  stake      5  result UP       +3.44  total  +5240.86
  Mon 09 02:30  UP     10 @ 50c  stake      5  result UP       +4.82  total  +5245.68
  Mon 09 03:00  DOWN 2608 @ 18c  stake    473  result DOWN  +2108.03  total  +7353.71
  Mon 09 03:15  UP   2196 @ 18c  stake    399  result DOWN   -421.55  total  +6932.16
  Mon 09 03:30  DOWN    9 @ 57c  stake      5  result DOWN     +3.71  total  +6935.87
  Mon 09 03:45  DOWN 2373 @ 20c  stake    473  result UP     -499.95  total  +6435.92

RUNNING TOTAL every 10 rounds: -502, +970, -1256, +63, +629, +517, +1303, +1506, -344, +1132, +1947, +5603, +4280, +1293, +2535, +6932

---- v_hold_s100 (same entries, 1/5 the size) ----
WALLET CURVE v_hold_s100 (pretend money, after fees): 162 settled rounds, Sat 07 10:30 to Mon 09 03:45, 3 unsettled skipped
  profit now +1232.04 | peak +1428.16 (Mon 09 03:00) | worst drop 1037.55 (Sun 08 16:30 -> Sun 08 22:16) | drop right now 196.12 from the peak
  wins 102 (63%), avg win +58.06, avg loss -78.17, avg stake 63.47, avg entry price 54.2 c
  entry price  0- 40 c:  31 rounds, won  32%, profit  +1138.55
  entry price 40- 60 c:  44 rounds, won  61%, profit    -71.95
  entry price 60- 80 c:  87 rounds, won  75%, profit   +165.44
  bet UP  :  88 rounds, won  60%, profit   -367.87
  bet DOWN:  74 rounds, won  66%, profit  +1599.91
  5 best rounds: +469, +406, +406, +379, +358  (= 164% of total profit)
  5 worst rounds: -100, -100, -100, -100, -100
  longest losing streak: 4 rounds
  by hour (local): 00:-161(7)  01:+170(8)  02:+396(7)  03:+334(8)  04:-295(4)  05:+212(4)  06:+52(4)  07:-295(4)  08:-36(4)  09:-60(4)  10:-115(6)  11:+652(8)  12:-92(8)  13:+296(8)  14:+659(8)  15:-300(7)  16:+50(8)  17:-207(8)  18:+117(8)  19:+3(7)  20:-453(8)  21:-200(8)  22:+385(8)  23:+119(8)

LATEST 6 ROUNDS (time, bet, contracts, avg price c, stake, result, profit, running total)
```
(exit 0)
```

## 2026-11-09 19:31:01 tasks/queue/104-kdp-llc-last-page.sh
```
KDP rebuild started in the background
(exit 0)
```

## 2026-11-09 20:04:02 tasks/queue/105-kalshi-wallet-curve-evening.sh
```
wrote /home/kylarlovelady/starship/memory/inbox/kalshi-wallet-curve.md (66 lines)
# Kalshi wallet curve (queue 105, Mon 09 20:04, practice money only)

```
WALLET CURVE v_hold_s500 (pretend money, after fees): 186 settled rounds, Sat 07 10:30 to Mon 09 19:45, 1 unsettled skipped
  profit now +5385.24 | peak +7352.57 (Mon 09 03:00) | worst drop 5307.01 (Sun 08 16:30 -> Sun 08 22:16) | drop right now 1967.33 from the peak
  wins 119 (64%), avg win +250.67, avg loss -364.85, avg stake 284.65, avg entry price 53.8 c
  entry price  0- 40 c:  35 rounds, won  29%, profit  +4057.83
  entry price 40- 60 c:  56 rounds, won  66%, profit   +195.84
  entry price 60- 80 c:  95 rounds, won  76%, profit  +1131.57
  bet UP  : 100 rounds, won  62%, profit  -1549.08
  bet DOWN:  86 rounds, won  66%, profit  +6934.32
  5 best rounds: +2430, +2108, +2107, +1971, +1852  (= 194% of total profit)
  5 worst rounds: -500, -500, -500, -500, -500
  longest losing streak: 4 rounds
  by hour (local): 00:-781(8)  01:+852(8)  02:+2040(8)  03:+1791(8)  04:-1123(8)  05:+1381(8)  06:-645(8)  07:-2138(8)  08:+321(7)  09:-310(5)  10:-570(6)  11:+2656(8)  12:-512(8)  13:+1459(8)  14:+2968(8)  15:-1263(7)  16:+292(8)  17:-863(8)  18:+543(8)  19:+40(9)  20:-2252(8)  21:-1081(8)  22:+2004(8)  23:+575(8)

LATEST 30 ROUNDS (time, bet, contracts, avg price c, stake, result, profit, running total)
  Mon 09 02:00  UP   2471 @ 19c  stake    473  result UP    +1971.08  total  +5241.84
  Mon 09 02:16  UP      9 @ 60c  stake      5  result UP       +3.44  total  +5245.28
  Mon 09 02:30  UP     10 @ 50c  stake      5  result UP       +4.82  total  +5250.10
  Mon 09 02:46  DOWN    9 @ 60c  stake      5  result UP       -5.56  total  +5244.54
  Mon 09 03:00  DOWN 2608 @ 18c  stake    473  result DOWN  +2108.03  total  +7352.57
  Mon 09 03:15  UP   2196 @ 18c  stake    399  result DOWN   -421.55  total  +6931.02
  Mon 09 03:30  DOWN    9 @ 57c  stake      5  result DOWN     +3.71  total  +6934.73
  Mon 09 03:45  DOWN 2373 @ 20c  stake    473  result UP     -499.95  total  +6434.78
  Mon 09 04:00  UP   3122 @ 15c  stake    472  result DOWN   -499.94  total  +5934.84
  Mon 09 04:15  UP    964 @ 50c  stake    483  result UP     +464.22  total  +6399.06
  Mon 09 04:30  DOWN    9 @ 60c  stake      5  result DOWN     +3.44  total  +6402.50
  Mon 09 04:45  UP     10 @ 54c  stake      5  result UP       +4.42  total  +6406.92
  Mon 09 05:00  DOWN  811 @ 60c  stake    486  result DOWN   +311.56  total  +6718.48
  Mon 09 05:15  UP     10 @ 52c  stake      5  result UP       +4.62  total  +6723.10
  Mon 09 05:30  UP      9 @ 57c  stake      5  result UP       +3.71  total  +6726.81
  Mon 09 05:45  DOWN    8 @ 63c  stake      5  result DOWN     +2.82  total  +6729.63
  Mon 09 06:00  DOWN 3122 @ 15c  stake    472  result UP     -499.94  total  +6229.69
  Mon 09 06:15  UP     10 @ 52c  stake      5  result UP       +4.62  total  +6234.31
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
