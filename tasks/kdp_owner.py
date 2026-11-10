#!/usr/bin/env python3
"""Refined 'owner' page for the KDP notebooks. Kylar (2026-11-05 20:51): the old page looked cheap (big, Word-like). New one: small, centred, letter-spaced small caps,
hairline rules, quiet fields. Works on the finished interior PDFs by replacing everything on page 1 above the page number (the page is otherwise empty), so the engine is not touched.
Usage: python3 kdp_owner.py [book-slug ...]   (default: all books in ~/kdp-studio/books). Keeps interior-orig.pdf as the untouched engine output and always rebuilds from it."""
import os, sys, io, glob, shutil
HOME = os.path.expanduser("~"); STUDIO = HOME + "/kdp-studio"
try:
    import engine
except Exception:
    sys.path.insert(0, STUDIO); import engine
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
INK = (0.13, 0.13, 0.13); GREY = (0.55, 0.55, 0.55)
def spaced(c, x_center, y, text, font, size, track, color=INK):
    w = sum(pdfmetrics.stringWidth(ch, font, size) for ch in text) + track * (len(text) - 1)
    c.setFillColorRGB(*color); c.setFont(font, size); x = x_center - w / 2
    for ch in text:
        c.drawString(x, y, ch); x += pdfmetrics.stringWidth(ch, font, size) + track
def overlay(pw, ph, serif, sans, heading, footer, fields):
    buf = io.BytesIO(); c = canvas.Canvas(buf, pagesize=(pw, ph))
    c.setFillColorRGB(1, 1, 1); c.setStrokeColorRGB(1, 1, 1)
    c.rect(0, 0.95 * 72, pw, ph - 0.95 * 72, stroke=0, fill=1)        # clear the old content, keep the page number at the bottom
    cx = pw / 2 + 2; bw = 2.7 * 72; x0, x1 = cx - bw / 2, cx + bw / 2
    y = ph - 1.55 * 72
    spaced(c, cx, y, "THIS NOTEBOOK", serif, 9.5, 2.6); y -= 15
    spaced(c, cx, y, "BELONGS TO", serif, 9.5, 2.6); y -= 13
    c.setStrokeColorRGB(*INK); c.setLineWidth(0.6); c.line(cx - 14, y, cx + 14, y); y -= 36
    for f in fields:
        c.setFillColorRGB(*GREY); c.setFont(sans, 7.2)
        c.drawString(x0, y + 3, f.upper() if False else f)
        c.setStrokeColorRGB(0.72, 0.72, 0.72); c.setLineWidth(0.4)
        c.line(x0 + 44, y, x1, y); y -= 27
    y -= 6
    spaced(c, cx, y, footer.upper(), sans, 5.6, 1.1, GREY)
    c.save(); buf.seek(0); return PdfReader(buf).pages[0]
def imprint(pw, ph, sans):
    """Last page (Kylar, 2026-11-09 10:34): blank white page, no lines, no page number, just a tiny grey LOVELADY LLC centred near the bottom."""
    buf = io.BytesIO(); c = canvas.Canvas(buf, pagesize=(pw, ph)); text = "LOVELADY LLC"; size, track = 5.6, 1.1
    spaced(c, pw / 2, 0.6 * 72, text, sans, size, track, GREY)
    c.save(); buf.seek(0); return PdfReader(buf).pages[0]
def run(slug):
    d = f"{STUDIO}/books/{slug}/out"; ip = d + "/interior.pdf"; orig = d + "/interior-orig.pdf"
    if not os.path.exists(ip) and not os.path.exists(orig): print("skip", slug, "no interior"); return
    if not os.path.exists(orig): shutil.copy(ip, orig)
    F = engine.discover(); TF = "Liberation Serif" if "Liberation Serif" in F else "DejaVu Serif"
    SF = "Lato" if "Lato" in F else ("Liberation Sans" if "Liberation Sans" in F else "DejaVu Sans")
    r = PdfReader(orig); w = PdfWriter()
    for i, p in enumerate(r.pages):
        if i == 0:
            pw, ph = float(p.mediabox.width), float(p.mediabox.height)
            p.merge_page(overlay(pw, ph, engine.fn(TF, False), engine.fn(SF, False), "", "If found, please return to the owner.", ["Name", "Phone", "Email", "Company"]))
        if i == len(r.pages) - 1:
            p = imprint(float(p.mediabox.width), float(p.mediabox.height), engine.fn(SF, False))  # replace the page: no hidden lines or page number underneath
        w.add_page(p)
    w.write(ip); print("owner page refined:", slug, len(r.pages), "pages")
if __name__ == "__main__":
    slugs = sys.argv[1:] or sorted(os.path.basename(p) for p in glob.glob(STUDIO + "/books/*-operator-*"))
    for s in slugs: run(s)
