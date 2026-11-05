"status": 201, "reply": {"average_fee_paid": "0.0174", "average_fill_price": "0.5400", "client_order_id": "1ab386c5-dfb6-42c2-a759-a0b764994f79", "fill_count": "1.00", "order_id": "01a19e02-ff58-7c
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

## 2026-11-05 15:04:01 tasks/queue/029-home-voice-diag.sh
```
== services
hub-satellite: active
hub-voice: active
phone-voice: active
hub-dashboard: active
hub-watchdog: active
== containers
openwakeword Up 6 days
whisper Up 6 days (healthy)
piper Up 6 days (healthy)
pihole Up 19 hours (healthy)
homeassistant Up 13 hours
== hub-satellite log (last 25)
Nov 05 14:56:55 LoveladyMainAiHub bash[2546920]: WARNING:root:Mic service disconnected
Nov 05 14:57:38 LoveladyMainAiHub bash[2546920]: INFO:root:Waiting for wake word
Nov 05 14:58:19 LoveladyMainAiHub systemd[1]: Stopping hub-satellite.service - Wyoming satellite (main hub)...
Nov 05 14:58:19 LoveladyMainAiHub systemd[1]: hub-satellite.service: Deactivated successfully.
Nov 05 14:58:19 LoveladyMainAiHub systemd[1]: Stopped hub-satellite.service - Wyoming satellite (main hub).
Nov 05 14:58:19 LoveladyMainAiHub systemd[1]: hub-satellite.service: Consumed 1h 31min 37.976s CPU time.
Nov 05 14:58:19 LoveladyMainAiHub systemd[1]: Started hub-satellite.service - Wyoming satellite (main hub).
Nov 05 14:58:19 LoveladyMainAiHub bash[2665352]: INFO:root:Ready
Nov 05 14:58:20 LoveladyMainAiHub bash[2665352]: INFO:root:Connected to services
Nov 05 14:58:32 LoveladyMainAiHub bash[2665352]: INFO:root:Connected to server
Nov 05 14:58:32 LoveladyMainAiHub bash[2665352]: INFO:root:Waiting for wake word
Nov 05 14:58:52 LoveladyMainAiHub bash[2665352]: INFO:root:Waiting for wake word
Nov 05 14:58:55 LoveladyMainAiHub bash[2666912]: Playing raw data 'stdin' : Signed 16 bit Little Endian, Rate 22050 Hz, Mono
Nov 05 15:00:18 LoveladyMainAiHub bash[2665352]: INFO:root:Waiting for wake word
Nov 05 15:00:20 LoveladyMainAiHub bash[2670871]: Playing raw data 'stdin' : Signed 16 bit Little Endian, Rate 22050 Hz, Mono
Nov 05 15:00:51 LoveladyMainAiHub bash[2665352]: INFO:root:Waiting for wake word
Nov 05 15:01:35 LoveladyMainAiHub systemd[1]: Stopping hub-satellite.service - Wyoming satellite (main hub)...
Nov 05 15:01:35 LoveladyMainAiHub systemd[1]: hub-satellite.service: Deactivated successfully.
Nov 05 15:01:35 LoveladyMainAiHub systemd[1]: Stopped hub-satellite.service - Wyoming satellite (main hub).
Nov 05 15:01:35 LoveladyMainAiHub systemd[1]: hub-satellite.service: Consumed 2.083s CPU time.
Nov 05 15:01:35 LoveladyMainAiHub systemd[1]: Started hub-satellite.service - Wyoming satellite (main hub).
Nov 05 15:01:36 LoveladyMainAiHub bash[2674286]: INFO:root:Ready
Nov 05 15:01:36 LoveladyMainAiHub bash[2674286]: INFO:root:Connected to services
Nov 05 15:01:48 LoveladyMainAiHub bash[2674286]: INFO:root:Connected to server
Nov 05 15:01:48 LoveladyMainAiHub bash[2674286]: INFO:root:Waiting for wake word
== hub-voice log (last 15)
-- No entries --
== phone-voice errors today
Nov 05 15:00:53 LoveladyMainAiHub python[692834]: Exception occurred during processing of request from ('127.0.0.1', 40060)
Nov 05 15:00:53 LoveladyMainAiHub python[692834]: Traceback (most recent call last):
Nov 05 15:00:53 LoveladyMainAiHub python[692834]: BrokenPipeError: [Errno 32] Broken pipe
Nov 05 15:00:53 LoveladyMainAiHub python[692834]: During handling of the above exception, another exception occurred:
Nov 05 15:00:53 LoveladyMainAiHub python[692834]: Traceback (most recent call last):
Nov 05 15:00:53 LoveladyMainAiHub python[692834]:     except Exception as e: return self._send(500, {"error": str(e)[:200]})
Nov 05 15:00:53 LoveladyMainAiHub python[692834]: BrokenPipeError: [Errno 32] Broken pipe
== HA log, jarvis/assist/wake lines
[36m2026-11-05 14:57:38.136 DEBUG (MainThread) [homeassistant.components.conversation.chat_log] Adding user content: UserContent(role='user', content=' What do you know about Shari?', attachments=None, created=datetime.datetime(2026, 11, 5
[36m2026-11-05 14:58:52.352 DEBUG (MainThread) [homeassistant.components.conversation.chat_log] Adding user content: UserContent(role='user', content=' What do you know about Shari?', attachments=None, created=datetime.datetime(2026, 11, 5
[36m2026-11-05 14:58:54.445 DEBUG (MainThread) [homeassistant.components.conversation.chat_log] Chat Log opened but no assistant message was added, ignoring update[0m
[36m2026-11-05 15:00:18.370 DEBUG (MainThread) [homeassistant.components.conversation.chat_log] Adding user content: UserContent(role='user', content=' What can you tell me about Shari?', attachments=None, created=datetime.datetime(2026, 1
[36m2026-11-05 15:00:19.925 DEBUG (MainThread) [homeassistant.components.conversation.chat_log] Chat Log opened but no assistant message was added, ignoring update[0m
[36m2026-11-05 15:00:51.274 DEBUG (MainThread) [homeassistant.components.conversation.chat_log] Adding user content: UserContent(role='user', content=' Do you know who I am?', attachments=None, created=datetime.datetime(2026, 11, 5, 21, 0,
== jarvis trace, last 14 events
05:54:45 sentence {'sid': 'phes14a5', 'n': 0, 'text': "Sounds good! Glad to chat, and I’ll be ready for tomorrow's fixes.", 'tts_secs': 0.43, 'since
05:54:45 state {'sid': 'phes14a5', 'frm': 'thinking', 'to': 'speaking', 'why': ''}
05:54:46 sentence {'sid': 'phes14a5', 'n': 1, 'text': 'Have a great evening!', 'tts_secs': 0.3, 'since_heard': 1.5}
05:54:46 client {'sid': 'phes14a5', 'what': 'play_start', 'info': ''}
05:54:50 client {'sid': 'phes14a5', 'what': 'play_end', 'info': ''}
05:54:50 client {'sid': 'phes14a5', 'what': 'play_start', 'info': ''}
05:54:52 client {'sid': 'phes14a5', 'what': 'play_end', 'info': ''}
05:54:52 state {'sid': 'phes14a5', 'frm': 'speaking', 'to': 'follow', 'why': 'he finished talking'}
05:54:56 hangup {'sid': 'phes14a5', 'why': 'you ended it', 'after': 3.3, 'state': 'follow'}
05:54:56 state {'sid': 'phes14a5', 'frm': 'follow', 'to': 'idle', 'why': 'hung up: you ended it'}
05:55:02 client {'sid': 'phes14a5', 'what': 'page_hidden', 'info': ''}
13:53:20 client {'sid': 'phtnri1w', 'what': 'page_hidden', 'info': ''}
13:53:49 client {'sid': 'phtnri1w', 'what': 'page_visible', 'info': ''}
13:53:51 client {'sid': 'phtnri1w', 'what': 'page_hidden', 'info': ''}
(exit 0)
```

## 2026-11-05 15:04:01 tasks/queue/030-popup-font.sh
```
== files
  
4096 11-05_14:57 .
4096 11-05_04:28 ..
4096 11-04_14:52 backgrounds
4348 10-20_20:23 crop_api.py
1147 10-26_22:14 device-names.json
138 10-26_22:11 device-names.json.bak-oct26
4096 10-20_21:15 fontcache
1841 10-25_22:21 health_api.py
3025 10-26_22:23 hub_api.py
2913 10-22_16:25 hub_api.py.bak-jh
2949 10-26_22:23 hub_api.py.bak-names
11098 11-05_03:04 hub.html
7400 10-30_14:51 hub.html.bak-cr
8936 10-30_15:25 hub.html.bak-crop
8936 10-30_15:20 hub.html.bak-dbg
8992 10-30_15:28 hub.html.bak-ha
7093 10-25_22:22 hub.html.bak-hl
7550 10-30_15:01 hub.html.bak-imm
8850 10-30_15:10 hub.html.bak-imm2
7291 10-25_23:00 hub.html.bak-ly
10776 11-02_00:51 hub.html.bak-markets
8920 10-30_15:35 hub.html.bak-merge
10449 10-30_15:43 hub.html.bak-sheet
9377 11-05_02:22 index.html
8143 11-05_02:22 index.html.bak-glass
7351 10-25_23:00 index.html.bak-ly
8072 10-25_23:19 index.html.bak-ly2
4896 10-23_11:48 janitor_api.py
7216 10-23_11:48 janitor.html
== settings (font/theme keys only)
{'font': 'Great Vibes', 'text_color': '#000000'}
== reply popup code in index.html
62:  else if(m.name==='transcript'){$('you').textContent=m.text;show('thinking','Thinking');hideLater(30000);}
== font rules in theme.html / index.html
theme.html:16:var bu=g('bubble');if(bu){if(s.glass===false){bu.style.cssText='background:none;border:0;box-shadow:none;-webkit-backdrop-filter:none;backdrop-filter:none;padding:0';}
index.html:8: font-family:"Segoe UI",system-ui,sans-serif;height:100vh;overflow:hidden;display:flex;
index.html:10:#clock{font-size:15vw;font-weight:200;letter-spacing:.02em;color:var(--cyan);
index.html:12:#date{font-size:2.6vw;color:var(--dim);letter-spacing:.2em;text-transform:uppercase;margin-bottom:4vh}
index.html:13:#wx{display:flex;gap:4vw;align-items:baseline;font-size:2.4vw;color:var(--dim)}
index.html:14:#temp{font-size:7vw;font-weight:200;color:#e8f4ff}
index.html:15:#cond{font-size:3vw;color:#e8f4ff}
index.html:18: box-shadow:0 0 40px rgba(56,232,255,.2);backdrop-filter:blur(12px);
index.html:21:#status{display:flex;align-items:center;gap:1.2vw;font-size:2vw;letter-spacing:.2em;
index.html:27:.lbl{font-size:1.7vw;color:var(--dim);text-transform:uppercase;letter-spacing:.15em}
index.html:28:#you{font-size:2.6vw;color:var(--cyan);min-height:3.4vw;margin-bottom:1.5vh}
index.html:29:#ai{font-size:3vw;line-height:1.3;min-height:4vw}
index.html:32: border:1px solid rgba(255,255,255,.6);-webkit-backdrop-filter:blur(26px) saturate(1.7);backdrop-filter:blur(26px) saturate(1.7);
index.html:121:var bu=g('bubble');if(bu){if(s.glass===false){bu.style.cssText='background:none;border:0;box-shadow:none;-webkit-backdrop-filter:none;backdrop-filter:none;padding:0';}
(exit 0)
```
