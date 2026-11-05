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

## Done
(Finished items go here with the date, newest first. Never delete.)
