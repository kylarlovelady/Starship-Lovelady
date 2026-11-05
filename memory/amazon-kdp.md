# Amazon KDP
- KDP identity verification: DONE (Kylar confirmed Nov 1).
- Priority #2 income project after the Kalshi agent. A Pi service `hub-kdp` exists (details not recorded here).
- Printable/template digital products could share the KDP pipeline.
- (Add what is being published, schedule and results here.)

## Plan (Kylar, 2026-11-05)
- Account is ready. Templates and ideas exist; nothing published yet.
- Product idea: journals by job role for plant workers (operator, mechanic, electrician, etc.).
- Needs: (1) a repeatable process: one template, one script, one checklist from idea to uploaded files; (2) pen name decision; (3) where it sits under Lovelady LLC.
- Next steps for Claude: look at the existing templates on the Pi (hub-kdp / KDP studio on :8090), list KDP's template rules, and propose the streamlined process. Questions for Kylar: pen name ideas, page size, paperback or also hardcover, price range.

## KDP studio on the Pi (read 2026-11-05, queue 024/025)
- ~/kdp-studio (uvicorn on :8090, Python + reportlab, PIN-protected, files app.py, engine.py, index.html, books/<name>/book.json + out/ + img/ + history/). Three projects: process-operator, new-journal (old, in books-old), new-book (current). Last changed Oct 26.
- engine.py renders cover + interior PDFs for a 6x9 HARDCOVER (case laminate) with wrap, hinge, board and spine calculations (75 to 550 pages), 7 pt checks, fonts, textures, image prep, overflow and contrast checks. The spec in the file says verified=False: it must be checked against KDP's cover calculator before the first upload.
- Goal tonight (Kylar): 2 books into review by about 4:30 am after work. Paperback is faster to review and simpler than hardcover; decide which.
- Open questions: hardcover or paperback? which two job roles first? page count? Is there a book.json already filled in for a first title?
- Rules to remember (KDP help): tick the Low-content box if it qualifies; title must match the cover; no generic keywords like journal or notebook stuffed into the title; keep the barcode area (about 2 x 1.2 in) clear; gutter margin grows with page count; bleed adds 0.125 in on top, bottom and outside edges; disclose AI-generated content in KDP's setup questions.

## Hardcover spec check (Claude, 2026-11-05 14:20)
- Kylar: books must be HARDCOVER. Wants help with design (colors, fonts, wording) and is open to Canva.
- Studio numbers vs published: trim 6x9, wrap 0.591, hinge 0.197, cover height 10.418 (9 + 2 x 0.709), safe margin 0.635, hinge keep-out 0.4, barcode box 2 x 1.2 in at 0.76 from bottom and 0.25 from hinge, 75 to 550 pages, 300 dpi, PDF with fonts embedded: all match KDP's help page and third-party tables. Spine width is the one value that sources disagree on (about 0.002252 in per page for white plus 0.189 base). KDP's own cover calculator is the authority: after entering the page count in KDP, download the template and compare its size to the studio's cover PDF before uploading.
- Hardcover has no Standard Color (Premium Color only); a hardcover over about 120 pages gets headbands.
- Canva: fine for cover artwork or icons; export as PNG at 300 dpi and import into the studio so the spine, wrap and safe zones stay exact. Do not build the whole cover in Canva unless it matches the KDP template size.
- Sources: kdp.amazon.com help GDTKFJPNQCBTMRV6; kdpprintcover.com 6x9 hardcover guide.

## Design brief (Kylar, 2026-11-05 14:24)
- HARDCOVER notebooks (not logbooks): lined pages, every page numbered. Page 1: "This notebook belongs to" with lines for Name, Phone, Email, Company.
- First two titles: Process Operator, then Lab Operator. Published under Lovelady LLC. Goal: both in review by the time he gets off work (about 4:30 am Fri 2026-11-06).
- Look: official, professional, durable, for blue-collar workers. NO pictures or illustrations. A textured look over the whole book is fine, nothing else decorative.
- Title: bold, large, near the top of the front cover with real presence, like the lettering on a Bible cover (name front and center toward the top).
- Draft colours: Process Operator deep navy with brushed silver; Lab Operator dark forest green with gold or cream. Fonts: condensed industrial title (Oswald if installed), clean sans for small print. Check with Kylar before final.

## Done
(Finished items go here with the date, newest first. Never delete.)
