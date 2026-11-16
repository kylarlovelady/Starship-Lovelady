# KDP: ready to upload (no deadline, do it whenever you have 15 minutes)

All files are already built. Each book folder is memory/inbox/kdp-preview/<book>/ and holds `cover.pdf` and `interior.pdf` (the same interior for every colour of a title). On your phone or computer, open this repo on GitHub, go to that folder and download the two files.

## What to upload

| Job | Colour | Folder | Do this |
|---|---|---|---|
| Process Operator | Navy | process-operator-a | Re-upload cover + interior (LLC moved to last page). Also fix the title to "Process Operator" (capital O) while you are in there. |
| Process Operator | Forest green | process-operator-b | Re-upload cover + interior |
| Process Operator | Burgundy | process-operator-c | Re-upload cover + interior |
| Process Operator | Purple | process-operator-e | Re-upload cover + interior (or leave; you may drop purple) |
| Process Operator | Black and gold | process-operator-f | NEW book |
| Process Operator | Rose pink | process-operator-g | NEW book |
| Lab Operator | Navy / Green / Burgundy / Purple | lab-operator-a, b, c, e | New books if not listed yet |
| Lab Operator | Black and gold / Rose pink | lab-operator-f, g | New books |

Black and gold and rose pink appear in the table once the Pi has built them (a few minutes after the build job). If a folder is not there yet, it is not done yet.

## Steps for a new book at KDP (about 10 minutes each)
1. kdp.amazon.com, Bookshelf, Create, Hardcover.
2. Title exactly as on the cover ("Process Operator"), no subtitle, author Lovelady LLC.
3. Description and keywords: from `python3 tasks/kdp_listing.py` output, or ask Claude to paste them.
4. No ISBN (KDP gives one), Cream paper, 6 x 9 in, matte, no bleed. Tick Low-content. AI-generated content: Yes (layout and design built with software).
5. Upload `interior.pdf`, then `cover.pdf`. Launch Previewer, check the cover and the last page (tiny LOVELADY LLC), Approve.
6. Price $18.99 USD. Publish.

## Steps to replace the files on a live book
Bookshelf, the book, three dots, Edit book content. Upload the new interior, then the new cover, Previewer, Approve, Publish. (Amazon reviews it again; the old book stays live meanwhile.)

## Not decided yet
- Purple: left live for now. Dropping it later means unpublishing it in KDP.
- Pink: built as a deeper rose (#C93C74) with white lettering so it reads clearly. If you want a soft blush or a hot pink instead, say so and Claude rebuilds it.
