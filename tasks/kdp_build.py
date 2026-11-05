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
import engine
F = engine.discover()
print("fonts found:", sorted(F))
TFONT = "Playfair Display" if "Playfair Display" in F else ("Liberation Serif" if "Liberation Serif" in F else "DejaVu Serif")
IFONT = "Lato" if "Lato" in F else ("Liberation Sans" if "Liberation Sans" in F else "DejaVu Sans")
print("title font:", TFONT, "| interior font:", IFONT)
NAVY, GOLD = "#16233F", "#D4AF37"
def book(slug, l1, l2):
    def t(i, panel, x, y, w, h, size, text, **k):
        d = dict(id=i, type="text", panel=panel, x=x, y=y, w=w, h=h, size=size, text=text, bold=True, align="center", font=TFONT, color=GOLD, lh=1.2, foil="", img="", zoom=1, fx=50, fy=50, tint="", tint_amt=100)
        d.update(k); return d
    els = [
        dict(id="tx1", type="image", panel="full", x=0, y=0, w=100, h=100, size=24, text="", bold=False, align="left", font="", color="", lh=1.2, foil="", img="linen01.jpg", zoom=1, fx=50, fy=50, tint=NAVY, tint_amt=88),
        t("t1", "front", 0, 10, 100, 14, 64, l1, foil="gold"),
        t("t2", "front", 0, 23, 100, 14, 64, l2, foil="gold"),
        dict(id="r1", type="rect", panel="front", x=22, y=40.5, w=56, h=0.35, size=24, text="", bold=False, align="left", font="", color=GOLD, lh=1.2, foil="", img="", zoom=1, fx=50, fy=50, tint="", tint_amt=100),
        t("sp1", "spine", 0, 0, 100, 10, 17, f"{l1} {l2}", foil="gold"),
        t("b1", "back", 0, 94, 40, 4, 8, "Lovelady LLC", bold=False, align="left", font=IFONT, color=GOLD),
    ]
    return {"name": slug, "title": f"{l1} {l2}", "subtitle": "", "author": "Lovelady LLC", "paper": "cream", "pages": 120,
        "cover": {"bg": NAVY, "pattern": "none", "pattern_color": "#999999", "frame": True, "frame_color": GOLD, "font": TFONT, "text": GOLD, "barcode_box": True, "elements": els},
        "inside": {"font": IFONT, "color": "#222222", "page_bg": "#ffffff", "style": "lines", "line_color": "#8f8f8f", "line_width": 0.5, "spacing": 0.3125, "dash": False,
                   "top": 0.7, "bottom": 0.85, "inner": 0.5, "outer": 0.4, "header": "none", "header_text": "", "num_pos": "center", "num_style": "plain", "num_size": 9},
        "front": {"title_page": False, "owner_page": True, "owner_heading": "This notebook belongs to", "owner_footer": "If found, please return to the owner.", "owner_fields": ["Name", "Phone", "Email", "Company"], "contacts": 0, "index": 0, "goals": False},
        "back": {"notes_pages": 0}, "labels": {}, "listing": {"description": "", "keywords": [], "categories": "", "price": ""}, "answers": {}, "chat": []}
for slug, l1, l2 in (("process-operator-a", "Process", "Operator"), ("lab-operator-a", "Lab", "Operator")):
    d = f"{STUDIO}/books/{slug}"; os.makedirs(d + "/img", exist_ok=True); os.makedirs(d + "/out", exist_ok=True)
    b = engine.clean(book(slug, l1, l2))
    cw, ch, sp = engine.cover_size(b["pages"], b["paper"])
    tex = d + "/img/linen01.jpg"
    if not os.path.exists(tex): engine.make_texture("linen", cw, ch, tex, seed=7)
    json.dump(b, open(d + "/book.json", "w"), indent=1)
    cp, gp, ip = d + "/out/cover.pdf", d + "/out/coverg.pdf", d + "/out/interior.pdf"
    engine.interior(b, ip); info = engine.cover(b, cp, imgdir=d + "/img"); engine.cover(b, gp, guides=True, imgdir=d + "/img")
    chk = engine.check(b, cp, ip, info, d + "/img")
    o = f"{OUT}/{slug}"; os.makedirs(o, exist_ok=True)
    engine.png(cp, o + "/cover", 1, 60); engine.png(gp, o + "/cover-guides", 1, 60)
    for n in (1, 2, 3): engine.png(ip, f"{o}/page{n}", n, 60)
    print("==", slug, "cover", round(cw, 3), "x", round(ch, 3), "spine", sp)
    for c in chk: print(" ", c["level"].upper(), c["text"][:160])
    print("  plan:", engine.plan(b)[:4], "...", len(engine.plan(b)), "pages")
