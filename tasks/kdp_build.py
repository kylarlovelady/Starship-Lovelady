"""Build the KDP notebooks (Process Operator, Lab Operator; scheme A) with the studio engine, check them, and write previews into memory/inbox/kdp-preview."""
import os, sys, json, subprocess, shutil, glob
HOME = os.path.expanduser("~"); STUDIO = HOME + "/kdp-studio"; OUT = HOME + "/starship/memory/inbox/kdp-preview"
sys.path.insert(0, STUDIO)
FD = HOME + "/.local/share/fonts"; os.makedirs(FD, exist_ok=True)
def sh(*a):
    return subprocess.run(a, capture_output=True, text=True, timeout=300)
# ---- Playfair Display (static Bold + Regular from the variable font) ----
if not os.path.exists(FD + "/PlayfairDisplay-Bold.ttf"):
    var = FD + "/PlayfairDisplay-var.ttf"
    r = sh("curl", "-sS", "-m", "60", "-L", "-o", var, "https://raw.githubusercontent.com/google/fonts/main/ofl/playfairdisplay/PlayfairDisplay%5Bwght%5D.ttf")
    print("font download:", r.returncode, os.path.getsize(var) if os.path.exists(var) else 0, r.stderr[:150])
    try:
        from fontTools.ttLib import TTFont
    except Exception:
        print(sh(STUDIO + "/.venv/bin/python", "-m", "pip", "install", "-q", "fonttools").stderr[-200:])
    for wt, nm in ((700, "Bold"), (400, "Regular")):
        r = sh(STUDIO + "/.venv/bin/python", "-m", "fontTools.varLib.instancer", var, f"wght={wt}", "--update-name-table", "-o", f"{FD}/PlayfairDisplay-{nm}.ttf")
        print("instance", nm, r.returncode, (r.stderr or r.stdout)[-200:])
    sh("fc-cache", "-f")
# thin vertical border lines need a width below the engine's old 1% minimum
_ep = STUDIO + "/engine.py"; _t = open(_ep).read()
if '_num(e.get("w"), 1, 100, 100)' in _t:
    shutil.copy(_ep, _ep + ".bak-minw"); open(_ep, "w").write(_t.replace('_num(e.get("w"), 1, 100, 100)', '_num(e.get("w"), 0.05, 100, 100)')); print("engine min width patched")
import engine
F = engine.discover()
print("fonts found:", sorted(F))
TFONT = "Liberation Serif" if "Liberation Serif" in F else "DejaVu Serif"
IFONT = "Lato" if "Lato" in F else ("Liberation Sans" if "Liberation Sans" in F else "DejaVu Sans")
print("title font:", TFONT, "| interior font:", IFONT)
from reportlab.pdfbase import pdfmetrics
from PIL import Image, ImageChops, ImageFilter
IN = 72.0
# Kylar's approved look (his reference picture, 2026-11-05): flat colour + fine grain, flat (not metallic) lettering, CAPS, thin double border, short rule.
SCHEMES = {"a": ("#18233D", "#CDB360"), "b": ("#1F372A", "#CDB360"), "c": ("#4D1E28", "#CDB360"), "e": ("#36291E", "#CDB360")}
TITLES = {"process-operator": ("PROCESS", "OPERATOR"), "lab-operator": ("LAB", "OPERATOR")}
def grain(path, w_in, h_in, bg):
    dpi = 300; w, h = int(w_in * dpi), int(h_in * dpi)
    base = Image.new("RGB", (w, h), bg)
    n = Image.effect_noise((w, h), 14).filter(ImageFilter.GaussianBlur(0.6))
    n3 = Image.merge("RGB", (n, n, n))
    out = ImageChops.add(base, n3, scale=1.0, offset=-128)
    out.save(path, "JPEG", quality=92, subsampling=0, optimize=True, dpi=(300, 300))
def book(slug, l1, l2, bg, fg):
    el = lambda **k: dict(dict(id="", type="text", panel="full", x=0, y=0, w=100, h=5, size=24, text="", bold=True, align="center", font=TFONT, color=fg, lh=1.2, foil="", img="", zoom=1, fx=50, fy=50, tint="", tint_amt=100), **k)
    b0 = engine.clean({"pages": 120, "paper": "cream"}); g = engine.geometry(b0); W, H = g["W"], g["H"]
    tw, th = engine.SPEC["trim_w"] * IN, engine.SPEC["trim_h"] * IN; wv = engine.SPEC["wrap_v"] * IN
    fn_ = engine.fn(TFONT, True)
    size = 0.78 * tw / (pdfmetrics.stringWidth("OPERATOR", fn_, 100) / 100.0)
    px = lambda v: v / W * 100; py = lambda v: v / H * 100
    els = [el(id="tx1", type="image", img="linen01.jpg", bold=False, font="", color="")]
    fx0, fw = g["fx0"], tw
    els.append(el(id="t1", x=px(fx0), w=px(fw), y=py(wv + 0.19 * th - 0.47 * size), h=py(size * 1.3), size=size, text=l1))
    els.append(el(id="t2", x=px(fx0), w=px(fw), y=py(wv + 0.313 * th - 0.47 * size), h=py(size * 1.3), size=size, text=l2))
    els.append(el(id="r1", type="rect", x=px(fx0 + 0.35 * tw), w=px(0.30 * tw), y=py(wv + 0.395 * th), h=py(1.0), bold=False, font=""))
    def frame(tag, x0):
        for k, (ins, lw) in enumerate(((0.32 * IN, 1.5), (0.40 * IN, 0.8))):
            xs, ys, ww, hh = x0 + ins, wv + ins, tw - 2 * ins, th - 2 * ins
            for j, (x, y, w, h) in enumerate(((xs, ys, ww, lw), (xs, ys + hh - lw, ww, lw), (xs, ys, lw, hh), (xs + ww - lw, ys, lw, hh))):
                els.append(el(id=f"{tag}{k}{j}", type="rect", x=px(x), y=py(y), w=px(w), h=py(h), bold=False, font=""))
    frame("f", g["fx0"]); frame("k", g["bx0"])
    els.append(el(id="sp1", panel="spine", x=0, y=0, w=100, h=10, size=15, text=f"{l1} {l2}"))
    els.append(el(id="b1", panel="back", x=2, y=96.8, w=40, h=4, size=8, text="Lovelady LLC", bold=False, align="left", font=IFONT))
    return {"name": slug, "title": f"{l1.title()} {l2.title()}", "subtitle": "", "author": "Lovelady LLC", "paper": "cream", "pages": 120,
        "cover": {"bg": bg, "pattern": "none", "pattern_color": "#999999", "frame": False, "frame_color": fg, "font": TFONT, "text": fg, "barcode_box": False, "elements": els},
        "inside": {"font": IFONT, "color": "#222222", "page_bg": "#ffffff", "style": "lines", "line_color": "#8f8f8f", "line_width": 0.5, "spacing": 0.3125, "dash": False,
                   "top": 0.7, "bottom": 0.85, "inner": 0.5, "outer": 0.4, "header": "none", "header_text": "", "num_pos": "center", "num_style": "plain", "num_size": 9},
        "front": {"title_page": False, "owner_page": True, "owner_heading": "This notebook belongs to", "owner_footer": "If found, please return to the owner.", "owner_fields": ["Name", "Phone", "Email", "Company"], "contacts": 0, "index": 0, "goals": False},
        "back": {"notes_pages": 0}, "labels": {}, "listing": {"description": "", "keywords": [], "categories": "", "price": ""}, "answers": {}, "chat": []}
fronts = {}
for tk, (l1, l2) in TITLES.items():
    for sk, (bg, fg) in SCHEMES.items():
        slug = f"{tk}-{sk}"; d = f"{STUDIO}/books/{slug}"; os.makedirs(d + "/img", exist_ok=True); os.makedirs(d + "/out", exist_ok=True)
        b = engine.clean(book(slug, l1, l2, bg, fg))
        cw, ch, sp = engine.cover_size(b["pages"], b["paper"])
        grain(d + "/img/linen01.jpg", cw, ch, bg)
        json.dump(b, open(d + "/book.json", "w"), indent=1)
        cp, gp, ip = d + "/out/cover.pdf", d + "/out/coverg.pdf", d + "/out/interior.pdf"
        engine.interior(b, ip); info = engine.cover(b, cp, imgdir=d + "/img"); engine.cover(b, gp, guides=True, imgdir=d + "/img")
        chk = engine.check(b, cp, ip, info, d + "/img")
        o = f"{OUT}/{slug}"; os.makedirs(o, exist_ok=True)
        engine.png(cp, o + "/cover", 1, 60); engine.png(gp, o + "/cover-guides", 1, 60)
        for n in (1, 2): engine.png(ip, f"{o}/page{n}", n, 60)
        engine.png(cp, o + "/cover-hi", 1, 110)
        im = Image.open(o + "/cover-hi.png"); g = info["geo"]; s = 110 / 72.0
        fronts[slug] = im.crop((int(g["fx0"] * s), int(g["H"] * s - g["ty1"] * s), int(g["fx1"] * s), int(g["H"] * s - g["ty0"] * s)))
        fronts[slug].save(o + "/front.png")
        bad = [c for c in chk if c["level"] == "fail"]
        print("==", slug, "FAILS:", [c["text"][:100] for c in bad] or "none", "| spine", sp)
sheet = Image.new("RGB", (4 * 460, 2 * 700), "#e8e8e8")
for i, slug in enumerate([f"{t}-{k}" for t in TITLES for k in SCHEMES]):
    f = fronts[slug].resize((440, 660)); sheet.paste(f, ((i % 4) * 460 + 10, (i // 4) * 700 + 20))
sheet.save(OUT + "/contact-sheet.png")
print("sheet done")
