arket-data, last 3 days)

entry at about 1 min in: 138 orders per method
  TAKER  profit per contract -0.022  per $ staked -4.1%   (win rate 50%)
  MAKER  filled 128 of 138 (93%); avg price 1.0 cents better than the ask; win rate when filled 52% (taker on the same orders 52%)
         profit per FILLED contract +0.017 (assumed 1.75% fee) / +0.021 (0 fee);  taker on those same orders -0.006
         per $ staked: maker +3.4% vs taker -4.1%;  per ATTEMPT (unfilled = 0): maker +0.016 vs taker -0.022

entry at about 2 min in: 138 orders per method
  TAKER  profit per contract -0.021  per $ staked -4.0%   (win rate 50%)
  MAKER  filled 128 of 138 (93%); avg price 1.0 cents better than the ask; win rate when filled 49% (taker on the same orders 49%)
         profit per FILLED contract -0.001 (assumed 1.75% fee) / +0.003 (0 fee);  taker on those same orders -0.023
         per $ staked: maker -0.3% vs taker -4.0%;  per ATTEMPT (unfilled = 0): maker -0.001 vs taker -0.021

entry at about 3 min in: 138 orders per method
  TAKER  profit per contract -0.020  per $ staked -3.9%   (win rate 50%)
  MAKER  filled 125 of 138 (91%); avg price 1.0 cents better than the ask; win rate when filled 50% (taker on the same orders 50%)
         profit per FILLED contract -0.004 (assumed 1.75% fee) / -0.000 (0 fee);  taker on those same orders -0.026
         per $ staked: maker -0.8% vs taker -3.9%;  per ATTEMPT (unfilled = 0): maker -0.004 vs taker -0.020

Reading it: the maker only helps if per-$ profit beats the taker's AFTER filling only on dips (adverse selection shows up as a lower win rate when filled). Fee for maker is assumed; confirm on a first real fill.

=== review 24h (tail)
TRADE REVIEW, last 24 hours: 2363 (strategy, round) results from 65 rounds with full recordings.

EVERY STRATEGY (pretend money): rounds | profit | win%% | profit per $ staked
  v_hold          54    +990.35   70%  +63.3%
  v_cut_loose     54    +577.86   61%  +26.9%
  v_late          35    +571.24   60%  +33.6%
  v_x96220861     28    +561.71   68%  +31.3%
  v_x88221261     25    +508.59   60%  +41.9%
  v_flow_flip     60    +458.14   48%   +9.6%
  v_no_cut        54    +399.06   67%  +25.4%
  v_x60222031     27    +397.62   67%  +31.2%
  v_x64216771     50    +388.75   56%   +9.8%
  v_x16217721     38    +361.06   42%  +11.2%
  v_x32221881     28    +357.28   57%  +12.7%
  mood            58    +354.37   50%  +14.5%
  v_x52220781     25    +266.30   52%  +21.8%
  v_x219211       47    +233.55   45%   +9.2%
  v_x72222451     44    +224.51   45%   +9.5%
  v_one_shot      54    +203.17   70%  +46.6%
  v_x28219981     52    +201.35   52%   +4.9%
  v_x80218931     40    +195.57   45%   +9.0%
  swing           65    +176.90   43%   +5.2%
  v_x80218932     40    +158.30   62%  +21.7%
  flow            57    +148.58   49%  +10.0%
  v_x28219982     52    +144.01   52%   +7.5%
  v_x219212       47    +141.38   47%   +3.8%
  v_x96220872     28    +128.96   39%   +8.9%
  v_x36215122     26    +125.39   50%  +12.0%
  v_x32221882     28    +122.96   54%   +5.1%
  v_x52220782     24    +110.21   42%   +9.5%
  v_x64216772     50    +108.55   64%  +17.3%
  v_x36215121     45    +106.19   42%   +4.6%
  signals         55    +102.32   51%   +5.6%
  v_x24220781     31    +101.88   61%  +17.5%
  v_x60222032     28     +92.04   71%  +29.8%
  hold            65     +83.95   57%  +11.5%
  v_x68220542     25     +81.14   48%   +8.3%
  v_x76218991     15     +74.22   60%  +26.3%
  v_x76218992     15     +74.22   60%  +26.3%
  v_x40223631     19     +55.28   58%  +22.5%
  v_x68220541     25     +54.52   48%   +2.6%
  v_x44219232     43     +47.69   44%   +1.4%
  trend           57     +35.07   44%   +2.8%
  v_adds          54     +29.39   50%   +1.9%
  distance        54     +10.12   54%   +1.1%
  v_x8220762      43      -6.37   47%   -0.3%
  v_x12229262     12     -15.60   42%   -3.6%
  v_x40223632     20     -22.69   35%   -6.2%
  v_x44219231     43     -38.94   40%   -1.2%
  v_x8220761      44     -47.37   43%   -1.3%
  v_mood_flip     60     -54.37   52%   -1.4%
  v_x72222452     44     -57.10   39%   -1.7%
  v_x12229261     12     -70.61   33%  -16.3%
  v_x88221262     34     -95.57   41%   -3.7%
  v_cut_tight     54     -95.89   41%   -8.1%
  v_x16217722     39    -103.03   38%   -6.7%
  v_x24220782     31    -142.99   35%   -6.0%
  v_trail         54    -148.31   48%  -10.6%
  v_trail_wide    54    -148.31   48%  -10.6%
  v_x4227191      22    -202.60   32%  -11.5%
  v_x4227192      22    -204.69   32%  -10.5%
  run             54    -291.88   46%  -12.8%

=== 'run': 54 rounds. Total profit -291.88 ===
1) SIDE: first bet on the winning side in 33 of 54 rounds (61%). Money-weighted: 52% of dollars staked were on the winning side (coin flip = 50%).
2) TIMING: it makes its first bet a median 1:32 into the round. The cheapest price on the winning side came a median 3:58 in. Median paid 21 cents above that cheapest point when it was on the right side.
   first bet time -> rounds, profit, side right:  0-1 min: 24, -214, 14 right  |  1-3 min: 17, -14, 13 right  |  10+ min: 2, -17, 1 right  |  3-6 min: 6, -32, 2 right  |  6-10 min: 5, -16, 3 right
3) SELLING (money made or lost by selling versus just holding those contracts to the end):
   cut a loss                  15 sells    -325.01  selling HURT (holding would have been better)
   other                        1 sells      +6.75  selling HELPED
   its own odds said sell      28 sells     +33.85  selling HELPED
4) BET SIZE -> rounds, profit, wins:  $100-250: 6, -167, 1  |  $25-100: 23, -161, 8  |  under $25: 25, +36, 16
5) HOUR OF DAY -> rounds, profit:  00h: 3, +11  |  01h: 4, +85  |  04h: 2, -1  |  05h: 4, +17  |  06h: 2, -10  |  07h: 4, -68  |  08h: 2, -8  |  09h: 4, -77  |  10h: 4, -26  |  11h: 2, -73  |  12h: 3, -28  |  13h: 3, +19  |  14h: 2, -23  |  15h: 3, -3  |  16h: 2, +1  |  17h: 1, -6  |  20h: 3, +5  |  21h: 2, -32  |  22h(exit 0)
```

## 2026-11-05 12:43:01 tasks/queue/020-kalshi-more.sh
```
=== key strategies, last 72 h
  v_hold          95    +296.88   60%   +8.5%
  v_late          60    +125.62   48%   +2.9%
  v_one_shot      95     -58.77   60%   -5.7%
  v_cut_loose     95     -83.26   52%   -1.8%
  v_no_cut        95    -269.14   57%   -6.5%
  hold           188    -274.35   51%   -5.3%
  v_adds          95    -483.14   43%   -9.1%
  v_trail         95    -535.18   42%  -11.5%
  v_cut_tight     95    -562.70   35%  -14.3%
  swing          186    -767.42   34%   -7.5%
  signals        162    -798.12   44%   -7.3%
  distance       148   -1125.74   45%   -9.6%
  flow           156   -1151.33   39%   -8.0%
  trend          169   -1250.37   34%   -8.1%
  run            158   -1748.43   39%  -15.6%
  mood           159   -1825.53   42%  -18.1%
=== key strategies, last 12 h
  v_hold          32    +738.53   78%  +82.7%
  v_late          25    +505.31   56%  +42.0%
  mood            33    +419.86   58%  +31.5%
  v_cut_loose     32    +399.14   62%  +27.8%
  v_no_cut        32    +274.79   69%  +27.1%
  swing           34    +248.03   47%  +13.8%
  trend           33    +146.83   58%  +22.6%
  v_adds          32    +143.80   56%  +15.9%
  flow            33    +139.75   55%  +16.6%
  v_one_shot      32    +124.47   78%  +51.1%
  distance        32     +79.12   62%  +15.7%
  hold            34     +77.25   68%  +18.7%
  signals         32     +48.60   59%   +4.7%
  v_cut_tight     32      +5.29   50%   +0.8%
  v_trail         32     -30.53   56%   -4.4%
  run             31    -186.85   52%  -10.0%

=== run, recent rounds (is the cap working?)
{'strategy': 'auto', 'bal': 827.72, 'pnl': -172.28, 'windows': 42, 'active': None, 'live': False}
Thu 09:00 {'staked': 49.24, 'pnl': 15.76}
Thu 09:15 {'staked': 49.8, 'pnl': -29.65}
Thu 09:30 {'staked': 50.0, 'pnl': -27.79}
Thu 09:45 {'staked': 49.96, 'pnl': -34.89}
Thu 10:00 {'staked': 49.95, 'pnl': -37.19}
Thu 10:15 {'staked': 20.48, 'pnl': 21.52}
Thu 10:30 {'staked': 49.93, 'pnl': -32.33}
Thu 10:45 {'staked': 49.64, 'pnl': 22.02}
Thu 11:00 {'staked': 0.0, 'pnl': 0.0}
Thu 11:15 {'staked': 49.96, 'pnl': -41.19}
Thu 11:30 {'staked': 49.9, 'pnl': -31.85}
Thu 11:45 {'staked': 0.0, 'pnl': 0.0}
Thu 12:00 {'staked': 49.77, 'pnl': -22.12}
Thu 12:15 {'staked': 20.73, 'pnl': -11.13}

=== collector restart / version
ActiveEnterTimestamp=Mon 2026-11-02 22:27:17 CST
# v8.2 restart: cap 25, Auto wallet needs 40+ rounds and a positive record (else holds to the end); nothing is retired (

=== real live orders
61 rows; keys: ['action', 'book_side', 'count', 'price', 'reply', 'side', 'status', 't', 'ticker']
{('buy', 'UP'): 22, ('sell', 'UP'): 27, ('buy', 'DOWN'): 7, ('sell', 'DOWN'): 5}
{"t": 1793652359, "action": "buy", "side": "UP", "ticker": "KXBTC15M-26NOV021600-00", "book_side": "bid", "count": 1, "price": 0.55, "status": 201, "reply": {"average_fee_paid": "0.0174", "average_fill_price": "0.5400", "client_order_id": "1ab386c5-dfb6-42c2-a759-a0b764994f79", "fill_count": "1.00", "order_id": "01a19e02-ff58-7c
{"t": 1793652361, "action": "sell", "side": "UP", "ticker": "KXBTC15M-26NOV021600-00", "book_side": "ask", "count": 1, "price": 0.54, "status": 201, "reply": {"average_fee_paid": "0.0174", "average_fill_price": "0.5500", "client_order_id": "d174effe-9f14-4d4e-87ef-78e666d416c1", "fill_count": "1.00", "order_id": "01a19e03-0728-7
{"t": 1793683924, "kind": "order", "action": "sell", "side": "DOWN", "ticker": "KXBTC15M-26NOV030045-45", "book_side": "bid", "count": 18, "price": 0.38, "quote_ask": 0.35, "quote_bid": 0.34, "status": 201, "reply": {"average_fee_paid": "0.0159", "average_fill_price": "0.3500", "client_order_id": "3036302b-8f89-4e26-b607-b0c9294
{"t": 1793683924, "kind": "slip", "slip_cents": 0.0, "ticker": "KXBTC15M-26NOV030045-45", "action": "sell", "side": "DOWN"}

=== my real trades
fills downloaded: 439
fills that were YOUR own: 429, fills from the agent's live sessions: 10
rounds traded: 107   won: 49 (46%)   total after fees: -2201.25   fees: 423.82
avg stake per round: $106.34   avg win: +93.25   avg loss: -116.73
first buy in the first 2 minutes: 70 of 107 rounds   avg first buy 145s into the round
avg buy price: 47 cents
took profit early (sold before close): 38 rounds, avg -47.90, won 61%
held to the end: 69 rounds, avg -5.52, won 38%
avg time of first sale: 387s into the round
date range: 10-31 00:30 to 11-05 01:00
sold early at a profit: 23 rounds, avg +100.21   sold early at a loss (cut loser): 15 rounds, avg -275.00
stake under $10  14 rounds  won  50%  total    +26.00
stake $10-50     53 rounds  won  42%  total   -343.91
stake $50-150    21 rounds  won  52%  total   -179.99
stake over $150  19 rounds  won  47%  total  -1703.35
first buy first minute   55 rounds  won  51%  total  -1736.64
first buy minutes 2-3    21 rounds  won  29%  total   -687.50
first buy after minute 3 29 rounds  won  45%  total   +213.53
last 5 rounds:
  11-04 23:45  yes  staked 48.4    pnl  -50.00 (held)
  11-05 00:00  yes  staked 96.29   pnl +131.41 (sold early)
  11-05 00:15  no   staked 47.47   pnl  -50.00 (held)
  11-05 00:30  no   staked 19.4    pnl  +25.20 (sold early)
  11-05 01:00  no   staked 18.95   pnl  -20.00 (held)
THE AGENT'S live rounds (not yours): 4 rounds, -2.58 after fees
saved to ~/market-data/my_trades.json
(exit 0)
```

## 2026-11-05 12:49:01 tasks/queue/021-kalshi-state.sh
```
== collector process
 710034 Mon Nov  2 22:27:17 2026 /usr/bin/python3 /home/kylarlovelady/starship/markets/collector.py
== repo head on Pi
367c7df 3 minutes ago queue 021: is the new Kalshi code running
== config files (numbers only)
-- config.json
{'weights': {'book': 0.25, 'momentum': 0.2, 'whales': 0.2, 'bigtrades': 0.15, 'news': 0.1, 'fng': 0.05, 'funding': 0.05}, 'threshold': 12.0, 'min_bet': 5.0, 'cap': 0, 'edge_min': 0.03, 'max_trades': 6.0, 'slice': 0.1, 'min_price': 0.08, 'max_price': 0.92, 'aggression': 50.0, 'floor': 0, 'entry_max': 0.8, 'entry_min': 0.15}
== auto log and pick
auto_pick: None
cap shown: None None None
run keys: ['added', 'autolog', 'bal', 'curve', 'equity', 'events', 'halt', 'id', 'in_round', 'inflight', 'k_age', 'label', 'live', 'now', 'pnl', 'pos', 'refills', 'round_cash', 'rounds', 'slip_avg', 'start', 'started', 'status', 'stopped', 'strategy', 'trades', 'using', 'warn', 'windows', 'wins']
(exit 0)
```

## 2026-11-05 12:52:01 tasks/queue/022-run-state.sh
```
strategy: auto | using: v_x88221261 | status: running | halt: None
autolog {'t': 1793892614, 'from': 'v_x8220761', 'to': 'v_x44219232', 'why': 'Best positive record so far per round after fees (40+ rounds each).'}
autolog {'t': 1793893513, 'from': 'v_x44219232', 'to': 'v_x72222451', 'why': 'Best positive record so far per round after fees (40+ rounds each).'}
autolog {'t': 1793894413, 'from': 'v_x72222451', 'to': 'v_x44219232', 'why': 'Best positive record so far per round after fees (40+ rounds each).'}
autolog {'t': 1793895312, 'from': 'v_x44219232', 'to': 'v_x64216771', 'why': 'Best positive record so far per round after fees (40+ rounds each).'}
autolog {'t': 1793899823, 'from': 'v_x64216771', 'to': 'v_x52220781', 'why': 'Best positive record so far per round after fees (40+ rounds each).'}
autolog {'t': 1793902514, 'from': 'v_x52220781', 'to': 'v_x88221261', 'why': 'Best positive record so far per round after fees (40+ rounds each).'}
cap in config shown: None
11:15 49.96 -41.19
11:30 49.9 -31.85
11:45 0.0 0.0
12:00 49.77 -22.12
12:15 20.73 -11.13
12:30 49.83 -14.72
Mon Nov  2 22:27:17 2026 /usr/bin/python3 /home/kylarlovelady/starship/markets/collector.py
(exit 0)
```

## 2026-11-05 13:22:01 tasks/queue/023-verify-kalshi.sh
```
# v8.4 restart: unproven cap really 25 (saved default 50 ove
Pi repo: fefb480 2 minutes ago
using: v_hold | status: running
autolog 11:30 v_x52220781 - Best positive record so far per round after fees (40+ rounds each).
autolog 12:15 v_x88221261 - Best positive record so far per round after fees (40+ rounds each).
autolog 12:54 v_hold - No strategy has a proven positive record over 80+ rounds yet, so it holds to the end (leas
12:00 staked 49.77 pnl -22.12
12:15 staked 20.73 pnl -11.13
12:30 staked 49.83 pnl -14.72
12:45 staked 24.91 pnl -24.91
13:00 staked 0.0 pnl 0.0
(exit 0)
```

## 2026-11-05 13:52:01 tasks/queue/024-kdp-look.sh
```
== top
total 120
drwxrwxr-x  8 kylarlovelady kylarlovelady  4096 Oct 26 00:54 .
drwx------ 36 kylarlovelady kylarlovelady  4096 Nov  5 04:28 ..
-rw-r--r--  1 kylarlovelady kylarlovelady 25292 Oct 26 00:54 app.py
drwxrwxr-x  2 kylarlovelady kylarlovelady  4096 Oct 26 00:08 backup-1026-0008
drwxrwxr-x  2 kylarlovelady kylarlovelady  4096 Oct 26 00:54 backup-v2-1026-0054
drwxrwxr-x  3 kylarlovelady kylarlovelady  4096 Oct 26 00:12 books
drwxrwxr-x  4 kylarlovelady kylarlovelady  4096 Oct 25 23:46 books-old-1026-0008
-rw-r--r--  1 kylarlovelady kylarlovelady 33061 Oct 26 00:54 engine.py
-rw-r--r--  1 kylarlovelady kylarlovelady 15534 Oct 26 00:54 index.html
-rw-------  1 kylarlovelady kylarlovelady     5 Oct 25 23:44 pin.txt
drwxr-xr-x  2 kylarlovelady kylarlovelady  4096 Oct 26 00:54 __pycache__
-rw-------  1 kylarlovelady kylarlovelady   182 Oct 26 00:18 settings.json
drwxrwxr-x  5 kylarlovelady kylarlovelady  4096 Oct 25 23:44 .venv
== tree (depth 3, no venv)
.
./books
./books/new-book-e841
./books/new-book-e841/history
./books/new-book-e841/out
./books/new-book-e841/book.json
./books/new-book-e841/img
./pin.txt
./books-old-1026-0008
./books-old-1026-0008/process-operator-5079
./books-old-1026-0008/process-operator-5079/out
./books-old-1026-0008/process-operator-5079/book.json
./books-old-1026-0008/new-journal-fcd0
./books-old-1026-0008/new-journal-fcd0/out
./books-old-1026-0008/new-journal-fcd0/book.json
./app.py
./engine.py
./__pycache__
./backup-v2-1026-0054
./backup-v2-1026-0054/app.py
./backup-v2-1026-0054/engine.py
./backup-v2-1026-0054/index.html
./settings.json
./backup-1026-0008
./backup-1026-0008/app.py
./backup-1026-0008/engine.py
./backup-1026-0008/index.html
./index.html
== sizes
27M	.
== README / notes
== app routes
(exit 0)
```

## 2026-11-05 13:55:01 tasks/queue/025-kdp-engine.sh
```
== engine.py head
"""KDP Studio engine: 6x9 hardcover spec, fonts, cover + interior renderer, checks."""
import os, re, copy, subprocess, hashlib, json, io, random
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit
from reportlab.lib.colors import HexColor, Color
IN = 72.0
# ---- KDP 6x9 hardcover spec (VERIFY with KDP cover calculator before first upload) ----
SPEC = dict(trim_w=6.0, trim_h=9.0, wrap=0.591, wrap_v=0.709, hinge=0.197, board=0.189,
            rate={"white": 0.002252, "cream": 0.0025}, min_pages=75, max_pages=550,
            safe_edge=0.635, hinge_keep=0.4, bc_w=2.0, bc_h=1.2, bc_bottom=0.76, bc_side=0.25,
            verified=False)
def spine(pages, paper): return round(pages * SPEC["rate"][paper] + SPEC["board"], 4)
def gutter(p): return 0.375 if p <= 150 else 0.5 if p <= 300 else 0.625 if p <= 500 else 0.75
def cover_size(pages, paper):
    s = spine(pages, paper)
    return (2 * SPEC["wrap"] + 2 * SPEC["trim_w"] + 2 * SPEC["hinge"] + s, SPEC["trim_h"] + 2 * SPEC["wrap_v"], s)
# ---- fonts ----
_F = {}
def discover():
    if _F: return _F
    import reportlab
    vd = os.path.join(os.path.dirname(reportlab.__file__), "fonts")
    _F["Bitstream Vera"] = {k: os.path.join(vd, f) for k, f in
        (("r", "Vera.ttf"), ("b", "VeraBd.ttf"), ("i", "VeraIt.ttf"))}
    cands = ["DejaVu Sans", "DejaVu Serif", "Liberation Sans", "Liberation Serif", "Liberation Mono", "Inter",
             "Carlito", "Caladea", "Lato", "Roboto", "Open Sans", "Montserrat", "Oswald", "Bitstream Charter",
             "FreeSerif", "FreeSans", "Noto Sans", "Noto Serif", "Playfair Display", "Merriweather", "Source Sans 3"]
    def fc(fam, st):
== engine functions
14:def spine(pages, paper): return round(pages * SPEC["rate"][paper] + SPEC["board"], 4)
15:def gutter(p): return 0.375 if p <= 150 else 0.5 if p <= 300 else 0.625 if p <= 500 else 0.75
16:def cover_size(pages, paper):
21:def discover():
30:    def fc(fam, st):
41:def fn(fam, bold=False):
77:def merge(base, patch):
82:def _num(v, lo, hi, d):
85:def clean_el(e, F):
98:def clean(b):
102:    def walk(x, dflt):
133:def plan(b):
141:def lum(h):
145:def contrast(a, b2):
148:def interior(b, path):
223:def geometry(b):
239:def region(g, panel):
243:def crop_box(iw, ih, rw, rh, zoom, fx, fy):
250:def _rgb(h): return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))
251:def tint_image(im, tint, amt):
259:def to_srgb(im):
268:def prep_image(src, cache, rw_in, rh_in, zoom, fx, fy, tint, tint_amt):
288:def make_texture(kind, w_in, h_in, path, seed=None):
294:    def noise(cell, sigma=64):
330:def draw_text(c, x, y, s, f, size, col, foil):
339:def image_report(b, imgdir):
352:def _lines(text, font, size, width):
357:def cover(b, path, guides=False, imgdir=None):
436:def overflow(b, info):
453:def png(pdf, out, page=1, dpi=70):
456:def check(b, cpdf, ipdf, info, imgdir=None):
== app routes
== book.json shape (newest book)
books-old-1026-0008/process-operator-5079/book.json
   name : "Process Operator"
   title : "Process Operator"
   subtitle : "Lined Journal & Logbook"
   tagline : "Notes. Shifts. Ideas."
   author : ""
   paper : "cream"
   pages : 120
   cover : {"bg": "#26313d", "accent": "#ff7a2f", "text": "#ffffff", "title_font": "DejaVu Sans", "body_font": "DejaVu Sa
   inside : {"font": "DejaVu Sans", "color": "#444444", "page_bg": "#ffffff", "style": "lines", "line_color": "#b9bec6", "
   front : {"title_page": false, "owner_page": true, "owner_fields": ["Name", "Company", "Phone", "Email"], "contacts": 0
   back : {"notes_pages": 0}
   listing : {"description": "", "keywords": [], "categories": "", "price": ""}
   answers : {"author": false}
books/new-book-e841/book.json
   name : "New book"
   title : "Process Operator Notebook Journal"
   subtitle : ""
   author : "K.J.Lovelady"
   paper : "white"
   pages : 120
   cover : {"bg": "#000000", "pattern": "none", "pattern_color": "#999999", "frame": false, "frame_color": "#000000", "fo
   inside : {"font": "DejaVu Sans", "color": "#444444", "page_bg": "#ffffff", "style": "lines", "line_color": "#b9bec6", "
   front : {"title_page": false, "owner_page": false, "owner_heading": "", "owner_footer": "", "owner_fields": [], "conta
   back : {"notes_pages": 0}
   labels : {"contacts": "Contacts", "index": "Index", "goals": "Goals", "notes": "Notes"}
   listing : {"description": "A hardcover Process Operator Notebook Journal with 120 numbered, lined pages (6 x 9 inches). 
   answers : {"spine_text": true, "owner_page": true, "goals": true, "contacts": true, "date_header": true, "index": true, 
   chat : [{"role": "user", "text": "Ok on the front cover i want \u201cProcess Operator\u201d in yellow gold letters an
== outputs
books/new-book-e841/out:
total 260
drwxr-xr-x 2 kylarlovelady kylarlovelady   4096 Oct 26 01:21 .
drwxr-xr-x 5 kylarlovelady kylarlovelady   4096 Oct 26 00:55 ..
-rw-r--r-- 1 kylarlovelady kylarlovelady  30148 Oct 26 01:21 061c1c5034_cover_90.png
-rw-r--r-- 1 kylarlovelady kylarlovelady  44959 Oct 26 01:21 061c1c5034_coverg_90.png
-rw-r--r-- 1 kylarlovelady kylarlovelady  45669 Oct 26 01:21 061c1c5034_coverg.pdf
-rw-r--r-- 1 kylarlovelady kylarlovelady  24982 Oct 26 01:21 061c1c5034_cover.pdf
-rw-r--r-- 1 kylarlovelady kylarlovelady 101233 Oct 26 01:21 061c1c5034_interior.pdf

books-old-1026-0008/new-journal-fcd0/out:
total 268
drwxr-xr-x 2 kylarlovelady kylarlovelady   4096 Oct 25 23:46 .
drwxr-xr-x 3 kylarlovelady kylarlovelady   4096 Oct 25 23:46 ..
-rw-r--r-- 1 kylarlovelady kylarlovelady  51221 Oct 25 23:46 3d06037250_coverg_80.png
-rw-r--r-- 1 kylarlovelady kylarlovelady  44357 Oct 25 23:46 3d06037250_coverg.pdf
-rw-r--r-- 1 kylarlovelady kylarlovelady  44143 Oct 25 23:46 3d06037250_cover.pdf
-rw-r--r-- 1 kylarlovelady kylarlovelady 121995 Oct 25 23:46 3d06037250_interior.pdf

books-old-1026-0008/process-operator-5079/out:
total 268
drwxr-xr-x 2 kylarlovelady kylarlovelad(exit 0)
```

## 2026-11-05 14:28:02 tasks/queue/026-kdp-interior.sh
```
== book.json (current book) keys and sample
books/new-book-e841/book.json
name: "New book"
title: "Process Operator Notebook Journal"
subtitle: ""
author: "K.J.Lovelady"
paper: "white"
pages: 120
cover:
  bg: "#000000"
  pattern: "none"
  pattern_color: "#999999"
  frame: false
  frame_color: "#000000"
  font: "DejaVu Sans"
  text: "#FFD700"
  barcode_box: false
  elements:
    [list of 1]
      id: "e1"
      type: "text"
      panel: "front"
      x: 0
      y: 30.0
      w: 100
      h: 40.0
      size: 58.0
      text: "Process Operator"
      bold: true
      align: "center"
      font: "DejaVu Sans"
      color: "#FFD700"
      lh: 1.2
inside:
  font: "DejaVu Sans"
  color: "#444444"
  page_bg: "#ffffff"
  style: "lines"
  line_color: "#b9bec6"
  line_width: 0.5
  spacing: 0.3125
  dash: false
  top: 0.7
  bottom: 0.85
  inner: 0.5
  outer: 0.4
  header: "none"
  header_text: ""
front:
  title_page: false
  owner_page: false
  owner_heading: ""
  owner_footer: ""
  owner_fields:
    [list of 0]
  contacts: 0
  index: 0
  goals: false
back:
  notes_pages: 0
labels:
  contacts: "Contacts"
  index: "Index"
  goals: "Goals"
  notes: "Notes"
listing:
  description: "A hardcover Process Operator Notebook Journal with 120 numbered, lined pages (6 x 9 inche
  keywords:
    [list of 7]
  categories: ""
  price: "17.99"
answers:
  spine_text: true
  owner_page: true
  goals: true
  contacts: true
  date_header: true
  index: true
  notes_back: true
  title_page: true
  listing: true
chat:
  [list of 37]
    role: "user"
    text: "Ok on the front cover i want \u201cProcess Operator\u201d in yellow gold letters and i wa
    changes:
      [list of 0]
== clean() element types
def clean(b):
    d = merge(copy.deepcopy(DEFAULT), {k: v for k, v in b.items() if k not in ("cover",)})
    d["cover"] = merge(copy.deepcopy(DEFAULT["cover"]), {k: v for k, v in (b.get("cover") or {}).items() if k != "elements"}) if isinstance(b.get("cover"), dict) else copy.deepcopy(DEFAULT["cover"])
    F = discover()
    def walk(x, dflt):
        for k in list(x):
            if k not in dflt: del x[k]; continue
            v, dv = x[k], dflt[k]
            if k in ("answers", "chat", "elements"): continue
            if isinstance(dv, dict): x[k] = v if isinstance(v, dict) else {}; walk(x[k], dv); continue
            if k in ENUM and v not in ENUM[k]: x[k] = dv
            elif k in NUM: x[k] = type(dv)(_num(v, NUM[k][0], NUM[k][1], dv))
            elif k in ("bg", "text", "color", "page_bg", "line_color", "pattern_color", "frame_color") and not (isinstance(v, str) and HEX.match(v)): x[k] = dv
            elif k in ("font",) and v not in F: x[k] = dv if dv in F else "Bitstream Vera"
            elif isinstance(dv, bool): x[k] = bool(v)
            elif isinstance(dv, str): x[k] = str(v)[:2000 if k == "description" else 300]
            elif isinstance(dv, list): x[k] = [str(i)[:120] for i in (v if isinstance(v, list) else [])][:12]
    walk(d, DEFAULT)
    d["pages"] = int(d["pages"]); d["pages"] += d["pages"] % 2
    els = []
    for e in ((b.get("cover") or {}).get("elements", []) if isinstance(b.get("cover"), dict) else [])[:40]:
        o = clean_el(e, F)
        if o: els.append(o)
    used = set(); n = 1
    for o in els:
        if not o["id"] or o["id"] in used:
            while f"e{n}" in used or any(f"e{n}" == q["id"] for q in els): n += 1
            o["id"] = f"e{n}"
        used.add(o["id"])
    d["cover"]["elements"] = els
    an = b.get("answers"); an = an if isinstance(an, dict) else {}
    d["answers"] = {str(k)[:40]: bool(v) for k, v in list(an.items())[:80]}
    d["chat"] = [{"role": "assistant" if m.get("role") == "assistant" else "user", "text": str(m.get("text", ""))[:3000], "changes": [str(c)[:200] for c in (m.get("changes") if isinstance(m.get("chang
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
