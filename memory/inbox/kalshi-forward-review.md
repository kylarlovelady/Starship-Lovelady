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
