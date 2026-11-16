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
