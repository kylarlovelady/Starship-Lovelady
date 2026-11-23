# Kalshi update (queue 126, Mon 23 12:58, practice money only)

```
== wild variant rows in trades.jsonl: 14213
== agent: active; markets repo: e0277e0 Queue 126: Kalshi update

######## FORWARD REVIEW since Mon 16 (after the wild-day test was added)
FORWARD REVIEW (pretend money, after fees). Start Mon 16 00:00. Run Mon 23 12:58

A) SINCE START, every strategy on its own rounds:
  v_hold_s250            550 rounds | profit  -4131.25 | win  61% | avg/round    -7.51 | median round   +1.69 | stake/round 134
  v_hold_s250_cheap100   550 rounds | profit  -5961.63 | win  61% | avg/round   -10.84 | median round   +1.69 | stake/round 127
  v_hold_s250_agree      469 rounds | profit  -2723.77 | win  61% | avg/round    -5.81 | median round   +1.86 | stake/round 117
  v_hold_s100            550 rounds | profit  -1390.09 | win  61% | avg/round    -2.53 | median round   +1.69 | stake/round 56
  hold                   596 rounds | profit   +152.47 | win  61% | avg/round    +0.26 | median round   +2.59 | stake/round 13
  v_edge10_s100          245 rounds | profit  -1266.65 | win  33% | avg/round    -5.17 | median round  -42.24 | stake/round 68
  v_hold_s500            550 rounds | profit  -7427.17 | win  61% | avg/round   -13.50 | median round   +1.69 | stake/round 263

B) PAIRED vs v_hold_s250 (same rounds only; positive = the test beat the baseline):
  v_hold_s250_cheap100   550 shared | total diff  -1830.38 | avg   -3.33/round | t-score -0.97 | better in 60, worse in 53, same in 437
  v_hold_s250_agree      469 shared | total diff   +402.55 | avg   +0.86/round | t-score +0.09 | better in 153, worse in 146, same in 170
  v_hold_s100            550 shared | total diff  +2741.16 | avg   +4.98/round | t-score +0.88 | better in 170, worse in 161, same in 219
  hold                   550 shared | total diff  +4154.35 | avg   +7.55/round | t-score +0.81 | better in 291, worse in 214, same in 45
  v_edge10_s100          235 shared | total diff  +2539.81 | avg  +10.81/round | t-score +0.66 | better in 116, worse in 119, same in 0
   (t-score: about 2 or more = probably real, under 1 = could easily be luck)

C) LUCK CHECK, all history:
  v_edge10_s100: 438 rounds, total -429.70
     without best 3 rounds -1945.95 | without best 5 -2922.14 | without best 10% (43 rounds) -13317.95
     first half +474.85 (Tue 10 07:55 to Mon 16 21:53) | second half -904.55 (to Mon 23 11:40)
     by day: Tue 10 +1009  Wed 11 +908  Thu 12 -596  Fri 13 +751  Sat 14 -794  Sun 15 -441  Mon 16 -145  Tue 17 +416  Wed 18 +206  Thu 19 -195  Fri 20 -1313  Sat 21 +87  Sun 22 -206  Mon 23 -119  -> 6 of 14 days positive
  v_hold_s250_cheap100: 1094 rounds, total -9353.34
     without best 3 rounds -12716.66 | without best 5 -14673.51 | without best 10% (109 rounds) -49274.73
     first half -3288.57 (Mon 09 20:30 to Mon 16 00:32) | second half -6064.77 (to Mon 23 12:25)
     by day: Mon 09 -645  Tue 10 -2006  Wed 11 +1070  Thu 12 -1209  Fri 13 +627  Sat 14 -1702  Sun 15 +475  Mon 16 +1111  Tue 17 -439  Wed 18 -1748  Thu 19 -1014  Fri 20 -2015  Sat 21 -1263  Sun 22 -609  Mon 23 +16  -> 5 of 15 days positive
  v_hold_s250: 1282 rounds, total -10076.04
     without best 3 rounds -13967.14 | without best 5 -16371.29 | without best 10% (128 rounds) -67180.38
     first half -4681.41 (Sat 07 10:30 to Sat 14 20:50) | second half -5394.63 (to Mon 23 12:25)
     by day: Sat 07 +885  Sun 08 +351  Mon 09 -295  Tue 10 -3097  Wed 11 +597  Thu 12 -1809  Fri 13 -245  Sat 14 -1375  Sun 15 -956  Mon 16 +3325  Tue 17 -578  Wed 18 -1280  Thu 19 -1130  Fri 20 -2241  Sat 21 -2019  Sun 22 -378  Mon 23 +169  -> 5 of 17 days positive
  v_hold_s500: 1282 rounds, total -16595.15
     without best 3 rounds -24456.32 | without best 5 -29368.27 | without best 10% (128 rounds) -130988.60
     first half -8867.22 (Sat 07 10:30 to Sat 14 20:50) | second half -7727.93 (to Mon 23 12:25)
     by day: Sat 07 +1311  Sun 08 +1219  Mon 09 -534  Tue 10 -6583  Wed 11 +1304  Thu 12 -3669  Fri 13 -622  Sat 14 -1907  Sun 15 +313  Mon 16 +6622  Tue 17 -1210  Wed 18 -2553  Thu 19 -2281  Fri 20 -4404  Sat 21 -2999  Sun 22 -964  Mon 23 +364  -> 6 of 17 days positive

######## FORWARD REVIEW since Wed 11
FORWARD REVIEW (pretend money, after fees). Start Wed 11 00:00. Run Mon 23 12:58

A) SINCE START, every strategy on its own rounds:
  v_hold_s250            987 rounds | profit  -7919.60 | win  62% | avg/round    -8.02 | median round   +1.86 | stake/round 125
  v_hold_s250_cheap100   987 rounds | profit  -6701.61 | win  62% | avg/round    -6.79 | median round   +1.86 | stake/round 116
  v_hold_s250_agree      852 rounds | profit  -4221.14 | win  62% | avg/round    -4.95 | median round   +2.20 | stake/round 108
  v_hold_s100            987 rounds | profit  -2643.69 | win  62% | avg/round    -2.68 | median round   +1.86 | stake/round 53
  hold                   1047 rounds | profit   +532.05 | win  61% | avg/round    +0.51 | median round   +2.59 | stake/round 12
  v_edge10_s100          409 rounds | profit  -1438.87 | win  32% | avg/round    -3.52 | median round  -42.26 | stake/round 63
  v_hold_s500            987 rounds | profit -12007.61 | win  62% | avg/round   -12.17 | median round   +1.86 | stake/round 244

B) PAIRED vs v_hold_s250 (same rounds only; positive = the test beat the baseline):
  v_hold_s250_cheap100   987 shared | total diff  +1217.99 | avg   +1.23/round | t-score +0.46 | better in 124, worse in 74, same in 789
  v_hold_s250_agree      852 shared | total diff  +1838.70 | avg   +2.16/round | t-score +0.32 | better in 287, worse in 260, same in 305
  v_hold_s100            987 shared | total diff  +5275.91 | avg   +5.35/round | t-score +1.27 | better in 281, worse in 260, same in 446
  hold                   987 shared | total diff  +8395.19 | avg   +8.51/round | t-score +1.24 | better in 487, worse in 366, same in 134
  v_edge10_s100          399 shared | total diff   -694.88 | avg   -1.74/round | t-score -0.13 | better in 182, worse in 217, same in 0
   (t-score: about 2 or more = probably real, under 1 = could easily be luck)

C) LUCK CHECK, all history:
  v_edge10_s100: 438 rounds, total -429.70
     without best 3 rounds -1945.95 | without best 5 -2922.14 | without best 10% (43 rounds) -13317.95
     first half +474.85 (Tue 10 07:55 to Mon 16 21:53) | second half -904.55 (to Mon 23 11:40)
     by day: Tue 10 +1009  Wed 11 +908  Thu 12 -596  Fri 13 +751  Sat 14 -794  Sun 15 -441  Mon 16 -145  Tue 17 +416  Wed 18 +206  Thu 19 -195  Fri 20 -1313  Sat 21 +87  Sun 22 -206  Mon 23 -119  -> 6 of 14 days positive
  v_hold_s250_cheap100: 1094 rounds, total -9353.34
     without best 3 rounds -12716.66 | without best 5 -14673.51 | without best 10% (109 rounds) -49274.73
     first half -3288.57 (Mon 09 20:30 to Mon 16 00:32) | second half -6064.77 (to Mon 23 12:25)
     by day: Mon 09 -645  Tue 10 -2006  Wed 11 +1070  Thu 12 -1209  Fri 13 +627  Sat 14 -1702  Sun 15 +475  Mon 16 +1111  Tue 17 -439  Wed 18 -1748  Thu 19 -1014  Fri 20 -2015  Sat 21 -1263  Sun 22 -609  Mon 23 +16  -> 5 of 15 days positive
  v_hold_s250: 1282 rounds, total -10076.04
     without best 3 rounds -13967.14 | without best 5 -16371.29 | without best 10% (128 rounds) -67180.38
     first half -4681.41 (Sat 07 10:30 to Sat 14 20:50) | second half -5394.63 (to Mon 23 12:25)
     by day: Sat 07 +885  Sun 08 +351  Mon 09 -295  Tue 10 -3097  Wed 11 +597  Thu 12 -1809  Fri 13 -245  Sat 14 -1375  Sun 15 -956  Mon 16 +3325  Tue 17 -578  Wed 18 -1280  Thu 19 -1130  Fri 20 -2241  Sat 21 -2019  Sun 22 -378  Mon 23 +169  -> 5 of 17 days positive
  v_hold_s500: 1282 rounds, total -16595.15
     without best 3 rounds -24456.32 | without best 5 -29368.27 | without best 10% (128 rounds) -130988.60
     first half -8867.22 (Sat 07 10:30 to Sat 14 20:50) | second half -7727.93 (to Mon 23 12:25)
     by day: Sat 07 +1311  Sun 08 +1219  Mon 09 -534  Tue 10 -6583  Wed 11 +1304  Thu 12 -3669  Fri 13 -622  Sat 14 -1907  Sun 15 +313  Mon 16 +6622  Tue 17 -1210  Wed 18 -2553  Thu 19 -2281  Fri 20 -4404  Sat 21 -2999  Sun 22 -964  Mon 23 +364  -> 6 of 17 days positive

######## WALLET CURVE v_hold_s250 (last 10 days)
WALLET CURVE v_hold_s250 (pretend money, after fees): 1282 settled rounds, Sat 07 10:30 to Mon 23 12:25, 3 unsettled skipped
  profit now -10076.04 | peak +3635.46 (Mon 09 03:00) | worst drop 15464.03 (Mon 09 03:00 -> Sun 22 09:02) | drop right now 13711.50 from the peak
  wins 788 (61%), avg win +99.50, avg loss -179.11, avg stake 127.75, avg entry price 56.2 c
  entry price  0- 40 c: 241 rounds, won  22%, profit  -5406.70
  entry price 40- 60 c: 351 rounds, won  59%, profit  -2365.82
  entry price 60- 80 c: 620 rounds, won  76%, profit  -1800.58
  entry price 80-100 c:  70 rounds, won  83%, profit   -502.94
  bet UP  : 620 rounds, won  58%, profit  -8921.02
  bet DOWN: 662 rounds, won  65%, profit  -1155.02
  5 best rounds: +1298, +1297, +1296, +1204, +1200  (= -62% of total profit)
  5 worst rounds: -250, -250, -250, -250, -250
  longest losing streak: 6 rounds
  by hour (local): 00:-2147(60)  01:-497(56)  02:-250(47)  03:+347(51)  04:-1492(54)  05:+925(55)  06:-2150(59)  07:-1195(53)  08:+1226(57)  09:+425(53)  10:-762(56)  11:+713(54)  12:-1880(51)  13:-757(49)  14:+964(53)  15:-383(47)  16:-1916(54)  17:-546(54)  18:+1878(53)  19:+235(50)  20:-1107(51)  21:-127(57)  22:-1189(54)  23:-391(54)

LATEST 10 ROUNDS (time, bet, contracts, avg price c, stake, result, profit, running total)
  Mon 23 08:30  DOWN  308 @ 80c  stake    246  result DOWN    +58.14  total  -9433.85
  Mon 23 08:45  DOWN  204 @ 49c  stake    100  result DOWN   +100.47  total  -9333.38
  Mon 23 09:17  DOWN  583 @ 41c  stake    240  result UP     -249.69  total  -9583.07
  Mon 23 09:46  DOWN    7 @ 80c  stake      6  result DOWN     +1.32  total  -9581.75
  Mon 23 10:20  UP    517 @ 47c  stake    241  result DOWN   -249.81  total  -9831.56
  Mon 23 10:31  UP    627 @ 38c  stake    239  result DOWN   -249.83  total -10081.39
  Mon 23 10:50  UP    502 @ 48c  stake    241  result UP     +252.15  total  -9829.24
  Mon 23 11:37  UP    537 @ 45c  stake    241  result DOWN   -249.92  total -10079.16
  Mon 23 11:48  UP    208 @ 48c  stake    100  result UP     +104.52  total  -9974.64
  Mon 23 12:25  UP    125 @ 80c  stake    100  result DOWN   -101.40  total -10076.04

######## WALLET CURVE v_hold_s250_wild (last 10 days)
WALLET CURVE v_hold_s250_wild (pretend money, after fees): 532 settled rounds, Mon 16 04:47 to Mon 23 12:25, 3 unsettled skipped
  profit now -2182.13 | peak +3228.55 (Mon 16 19:15) | worst drop 7539.10 (Mon 16 19:15 -> Sun 22 09:02) | drop right now 5410.68 from the peak
  wins 326 (61%), avg win +94.58, avg loss -160.27, avg stake 118.75, avg entry price 57.9 c
  entry price  0- 40 c: 100 rounds, won  25%, profit    -25.23
  entry price 40- 60 c: 115 rounds, won  52%, profit   -723.30
  entry price 60- 80 c: 251 rounds, won  74%, profit  -1031.64
  entry price 80-100 c:  66 rounds, won  83%, profit   -401.96
  bet UP  : 256 rounds, won  58%, profit  -2616.04
  bet DOWN: 276 rounds, won  64%, profit   +433.91
  5 best rounds: +1296, +1200, +1042, +1042, +976  (= -255% of total profit)
  5 worst rounds: -250, -250, -250, -250, -250
  longest losing streak: 6 rounds
  by hour (local): 00:-1601(25)  01:-83(23)  02:-192(16)  03:-857(20)  04:-509(21)  05:+175(24)  06:-744(28)  07:+579(24)  08:+1242(28)  09:+2414(24)  10:-298(27)  11:+284(22)  12:-1000(21)  13:-1754(18)  14:+1503(22)  15:-440(20)  16:+200(24)  17:+837(23)  18:-163(22)  19:-741(19)  20:-168(17)  21:+93(23)  22:-716(21)  23:-245(20)

LATEST 10 ROUNDS (time, bet, contracts, avg price c, stake, result, profit, running total)
  Mon 23 08:30  DOWN   38 @ 80c  stake     30  result DOWN     +7.17  total  -1876.13
  Mon 23 08:45  DOWN   51 @ 49c  stake     25  result DOWN    +25.11  total  -1851.02
  Mon 23 09:17  DOWN   71 @ 42c  stake     30  result UP      -31.10  total  -1882.12
  Mon 23 09:46  DOWN    7 @ 80c  stake      6  result DOWN     +1.32  total  -1880.80
  Mon 23 10:20  UP    371 @ 38c  stake    142  result DOWN   -147.86  total  -2028.66
  Mon 23 10:31  UP    198 @ 40c  stake     80  result DOWN    -82.97  total  -2111.63
  Mon 23 10:50  UP     63 @ 48c  stake     30  result UP      +31.54  total  -2080.09
  Mon 23 11:37  UP    222 @ 45c  stake     99  result DOWN   -103.02  total  -2183.11
  Mon 23 11:48  UP     52 @ 48c  stake     25  result UP      +26.13  total  -2156.98
  Mon 23 12:25  UP     31 @ 80c  stake     25  result DOWN    -25.15  total  -2182.13

######## WALLET CURVE hold (last 10 days)
WALLET CURVE hold (pretend money, after fees): 1753 settled rounds, Mon 02 22:00 to Mon 23 12:15, 4 unsettled skipped
  profit now -248.39 | peak +567.90 (Tue 03 18:30) | worst drop 1405.92 (Tue 03 18:30 -> Wed 11 21:30) | drop right now 816.29 from the peak
  wins 1021 (58%), avg win +9.69, avg loss -13.85, avg stake 13.04, avg entry price 58.0 c
  entry price  0- 40 c:  27 rounds, won  37%, profit   +391.06
  entry price 40- 60 c: 1033 rounds, won  52%, profit  -1265.08
  entry price 60- 80 c: 657 rounds, won  68%, profit   +676.62
  entry price 80-100 c:  36 rounds, won  83%, profit    -50.99
  bet UP  : 751 rounds, won  56%, profit   -657.01
  bet DOWN: 1002 rounds, won  60%, profit   +408.63
  5 best rounds: +486, +171, +154, +151, +141  (= -444% of total profit)
  5 worst rounds: -401, -233, -205, -197, -172
  longest losing streak: 8 rounds
  by hour (local): 00:-90(81)  01:-135(77)  02:-58(63)  03:-56(64)  04:+200(74)  05:+22(78)  06:-33(80)  07:+41(77)  08:-50(79)  09:+135(77)  10:-366(74)  11:+143(74)  12:+1(70)  13:-228(71)  14:-37(69)  15:-110(67)  16:-82(70)  17:-43(72)  18:+643(67)  19:-364(67)  20:-21(74)  21:+389(74)  22:+44(77)  23:-195(77)

LATEST 10 ROUNDS (time, bet, contracts, avg price c, stake, result, profit, running total)
  Mon 23 08:45  DOWN   11 @ 49c  stake      5  result DOWN     +5.41  total   -263.51
  Mon 23 09:15  UP     59 @ 40c  stake     24  result UP      +34.40  total   -229.11
  Mon 23 09:45  DOWN    8 @ 65c  stake      5  result DOWN     +2.67  total   -226.44
  Mon 23 10:15  UP     39 @ 48c  stake     19  result DOWN    -19.41  total   -245.85
  Mon 23 10:30  UP      9 @ 62c  stake      6  result DOWN     -5.73  total   -251.58
  Mon 23 10:45  DOWN   10 @ 55c  stake      6  result UP       -5.68  total   -257.26
  Mon 23 11:00  DOWN    9 @ 57c  stake      5  result DOWN     +3.71  total   -253.55
  Mon 23 11:30  DOWN   43 @ 56c  stake     24  result DOWN    +18.17  total   -235.38
  Mon 23 11:45  DOWN   35 @ 69c  stake     24  result UP      -24.68  total   -260.06
  Mon 23 12:15  DOWN   36 @ 66c  stake     24  result DOWN    +11.67  total   -248.39
```
