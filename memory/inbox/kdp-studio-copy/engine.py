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
        try:
            o = subprocess.run(["fc-match", "-f", "%{family}|%{file}", f"{fam}:style={st}"], capture_output=True, text=True, timeout=5).stdout
            f, p = o.split("|", 1)
            if fam.lower() in [x.strip().lower() for x in f.split(",")] and p.lower().endswith(".ttf") and os.path.exists(p): return p
        except Exception: pass
    for fam in cands:
        r = fc(fam, "Regular")
        if r: _F[fam] = {"r": r, "b": fc(fam, "Bold") or r, "i": fc(fam, "Italic") or r}
    return _F
_reg = set()
def fn(fam, bold=False):
    F = discover(); fam = fam if fam in F else "Bitstream Vera"
    k = "b" if bold else "r"; name = f"{fam}|{k}"
    if name not in _reg:
        pdfmetrics.registerFont(TTFont(name, F[fam][k])); _reg.add(name)
    return name
# ---- book model ----
DEFAULT = {
 "name": "New book", "title": "", "subtitle": "", "author": "", "paper": "white", "pages": 120,
 "cover": {"bg": "#ffffff", "pattern": "none", "pattern_color": "#999999", "frame": False, "frame_color": "#000000",
           "font": "DejaVu Sans", "text": "#000000", "barcode_box": False, "elements": []},
 "inside": {"font": "DejaVu Sans", "color": "#444444", "page_bg": "#ffffff", "style": "lines", "line_color": "#b9bec6",
            "line_width": 0.5, "spacing": 0.3125, "dash": False, "top": 0.7, "bottom": 0.85, "inner": 0.5, "outer": 0.4,
            "header": "none", "header_text": "", "num_pos": "center", "num_style": "plain", "num_size": 9},
 "front": {"title_page": False, "owner_page": False, "owner_heading": "", "owner_footer": "", "owner_fields": [], "contacts": 0, "index": 0, "goals": False},
 "back": {"notes_pages": 0},
 "labels": {"contacts": "Contacts", "index": "Index", "goals": "Goals", "notes": "Notes"},
 "listing": {"description": "", "keywords": [], "categories": "", "price": ""},
 "answers": {}, "chat": [],
}
ENUM = {"paper": ("white", "cream"), "pattern": ("none", "lines", "dots", "grid", "diagonal"),
        "style": ("lines", "dots", "grid", "blank"), "header": ("none", "date", "title", "date_title", "custom"),
        "num_pos": ("center", "outer", "none"), "num_style": ("plain", "dash", "of")}
NUM = {"pages": (SPEC["min_pages"], SPEC["max_pages"]), "line_width": (0.1, 2.0), "spacing": (0.2, 0.6),
       "top": (0.4, 2.0), "bottom": (0.5, 2.0), "inner": (0.375, 1.5), "outer": (0.25, 1.5), "num_size": (6, 14),
       "contacts": (0, 10), "index": (0, 10), "notes_pages": (0, 60)}
HEX = re.compile(r"^#[0-9a-fA-F]{6}$")
PANELS = ("front", "back", "spine", "full")
IMGRE = re.compile(r"^[a-z0-9]{6,32}\.jpg$")
# metallic foil looks: gradient stops (position, colour), outline colour, "mid" colour used for contrast checks
FOILS = {
 "gold": ([(0, "#7A5412"), (.16, "#D9A62E"), (.30, "#FFF0A0"), (.42, "#E3B53C"), (.55, "#9C6B17"), (.70, "#E8C04D"), (.84, "#FFF4B8"), (1, "#B8821F")], "#5E3F08", "#E3B53C"),
 "antique_gold": ([(0, "#5A3E10"), (.16, "#B08A2E"), (.30, "#E6CF86"), (.42, "#B8933A"), (.55, "#6E4C14"), (.70, "#C9A64A"), (.84, "#EAD99A"), (1, "#8B6A20")], "#3F2B07", "#B8933A"),
 "silver": ([(0, "#6E7480"), (.16, "#C7CCD4"), (.30, "#FFFFFF"), (.42, "#AEB4BF"), (.55, "#6A707B"), (.70, "#D5DAE1"), (.84, "#FFFFFF"), (1, "#9298A3")], "#3C414A", "#AEB4BF"),
 "copper": ([(0, "#6B2E14"), (.16, "#C8693A"), (.30, "#FFC39A"), (.42, "#D7794A"), (.55, "#8A3F1E"), (.70, "#E58E5B"), (.84, "#FFD2B0"), (1, "#A24F28")], "#4A1E0A", "#D7794A"),
}
def merge(base, patch):
    for k, v in (patch or {}).items():
        if isinstance(v, dict) and isinstance(base.get(k), dict): merge(base[k], v)
        else: base[k] = v
    return base
def _num(v, lo, hi, d):
    try: return max(lo, min(hi, float(v)))
    except Exception: return d
def clean_el(e, F):
    if not isinstance(e, dict): return None
    t = e.get("type") if e.get("type") in ("text", "rect", "image") else "text"
    return {"id": str(e.get("id", ""))[:8], "type": t, "panel": e.get("panel") if e.get("panel") in PANELS else "front",
         "x": _num(e.get("x"), 0, 100, 0), "y": _num(e.get("y"), 0, 100, 0), "w": _num(e.get("w"), 1, 100, 100), "h": _num(e.get("h"), 0.2, 100, 5),
         "size": _num(e.get("size"), 5, 220, 24), "text": str(e.get("text") or "")[:400], "bold": bool(e.get("bold", False)),
         "align": e.get("align") if e.get("align") in ("left", "center", "right") else "left",
         "font": e.get("font") if e.get("font") in F else "", "color": e.get("color") if isinstance(e.get("color"), str) and HEX.match(e.get("color")) else "",
         "lh": _num(e.get("lh"), 0.9, 2.0, 1.2),
         "foil": e.get("foil") if isinstance(e.get("foil"), str) and e.get("foil") in FOILS else "",
         "img": e.get("img") if isinstance(e.get("img"), str) and IMGRE.match(e.get("img")) else "",
         "zoom": _num(e.get("zoom"), 1, 8, 1), "fx": _num(e.get("fx"), 0, 100, 50), "fy": _num(e.get("fy"), 0, 100, 50),
         "tint": e.get("tint") if isinstance(e.get("tint"), str) and HEX.match(e.get("tint")) else "", "tint_amt": _num(e.get("tint_amt"), 0, 100, 100)}
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
    d["chat"] = [{"role": "assistant" if m.get("role") == "assistant" else "user", "text": str(m.get("text", ""))[:3000], "changes": [str(c)[:200] for c in (m.get("changes") if isinstance(m.get("changes"), list) else [])][:30]}
                 for m in (b.get("chat") if isinstance(b.get("chat"), list) else [])[-60:] if isinstance(m, dict)]
    return d
def plan(b):
    f, bk = b["front"], b["back"]; pg = []
    if f["title_page"]: pg.append("title")
    if f["owner_page"]: pg.append("owner")
    pg += ["contacts"] * f["contacts"] + ["index"] * f["index"] + (["goals"] if f["goals"] else [])
    tail = ["notes"] * bk["notes_pages"]
    main = max(1, b["pages"] - len(pg) - len(tail))
    return (pg + ["journal"] * main + tail)[: b["pages"]] if len(pg) + len(tail) < b["pages"] else (pg + tail)[: b["pages"]]
def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def contrast(a, b2):
    la, lb = sorted((lum(a), lum(b2)), reverse=True); return (la + .05) / (lb + .05)
# ---- interior ----
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
            if b["author"]: c.drawCentredString((L + R) / 2, H * .25, b["author"])
        elif kind == "owner":
            F_ = b["front"]
            if F_["owner_heading"]: label(F_["owner_heading"], top - 14, 16, True)
            y = top - 70
            for fld in b["front"]["owner_fields"]:
                label(fld + ":", y + 4, 11); c.setStrokeColor(HexColor(I["line_color"])); c.setLineWidth(.8)
                c.line(L + 80, y, R, y); y -= 40
            if F_["owner_footer"]: label(F_["owner_footer"], y - 10, 10)
        elif kind == "contacts":
            label(b["labels"]["contacts"], top - 14, 16, True); y = top - 40; c.setStrokeColor(HexColor(I["line_color"])); c.setLineWidth(.6)
            label("Name", y + 2, 9, True); label("Phone / Email", y + 2, 9, True, L + (R - L) * .42); label("Notes", y + 2, 9, True, L + (R - L) * .75)
            while y - 26 >= bot: y -= 26; c.line(L, y, R, y)
            for fx in (.42, .75): c.line(L + (R - L) * fx - 4, top - 38, L + (R - L) * fx - 4, y)
        elif kind == "index":
            label(b["labels"]["index"], top - 14, 16, True); y = top - 40; c.setStrokeColor(HexColor(I["line_color"])); c.setLineWidth(.6)
            label("Page", y + 2, 9, True); label("Topic", y + 2, 9, True, L + 50); label("Date", y + 2, 9, True, R - 60)
            while y - 24 >= bot: y -= 24; c.line(L, y, R, y)
            c.line(L + 44, top - 38, L + 44, y); c.line(R - 66, top - 38, R - 66, y)
        elif kind == "goals":
            label(b["labels"]["goals"], top - 14, 16, True); y = top - 50
            while y >= bot + 10:
                c.rect(L, y - 3, 9, 9, stroke=1, fill=0); c.setStrokeColor(HexColor(I["line_color"])); c.line(L + 18, y - 3, R, y - 3); y -= 30
        else:
            hdr = I["header"]
            if kind == "notes": label(b["labels"]["notes"], top - 14, 14, True); y0 = top - 36
            elif hdr != "none":
                t = {"date": "Date: ____ / ____ / ________", "title": b["title"], "date_title": b["title"] + "     Date: ____ / ____ / ____",
                     "custom": I["header_text"]}[hdr]
                label(t, top - 12, 10); y0 = top - 30
            if I["style"] != "blank": ruled(y0, bot + 8)
        if I["num_pos"] != "none" and kind != "title":
            t = {"plain": str(n), "dash": f"- {n} -", "of": f"{n} / {len(kinds)}"}[I["num_style"]]
            c.setFillColor(col); c.setFont(fn(fam), I["num_size"])
            if I["num_pos"] == "center": c.drawCentredString((L + R) / 2, .45 * IN, t)
            elif odd: c.drawRightString(R, .45 * IN, t)
            else: c.drawString(L, .45 * IN, t)
        c.showPage()
    c.save(); return kinds
# ---- cover ----
def geometry(b):
    """All cover positions in points, origin bottom-left of the cover PDF."""
    cw, ch, sp = cover_size(b["pages"], b["paper"])
    wr, wv, hg, tw, th = [SPEC[k] * IN for k in ("wrap", "wrap_v", "hinge", "trim_w", "trim_h")]
    sw = sp * IN; g = dict(W=cw * IN, H=ch * IN, sw=sw, sp=sp)
    g["bx0"], g["bx1"] = wr, wr + tw; g["sx0"] = g["bx1"] + hg; g["sx1"] = g["sx0"] + sw
    g["fx0"] = g["sx1"] + hg; g["fx1"] = g["fx0"] + tw; g["ty0"], g["ty1"] = wv, wv + th
    se, hk = SPEC["safe_edge"] * IN, SPEC["hinge_keep"] * IN
    g["safe"] = {"front": (g["fx0"] + hk, g["ty0"] + se, g["fx1"] - se, g["ty1"] - se),
                 "back": (g["bx0"] + se, g["ty0"] + se, g["bx1"] - hk, g["ty1"] - se)}
    bcr = g["bx1"] - hk - SPEC["bc_side"] * IN
    g["barcode"] = (bcr - SPEC["bc_w"] * IN, g["ty0"] + SPEC["bc_bottom"] * IN, bcr, g["ty0"] + SPEC["bc_bottom"] * IN + SPEC["bc_h"] * IN)
    g["spine_len"] = (g["ty0"] + 0.75 * IN, g["ty1"] - 0.75 * IN)
    return g

# ---- pictures, textures, foil ----
def region(g, panel):
    """Rectangle (x0, y0, x1, y1) in points that a picture on this panel fills (runs out to the bleed edge)."""
    W, H = g["W"], g["H"]
    return {"full": (0, 0, W, H), "front": (g["sx1"], 0, W, H), "back": (0, 0, g["sx0"], H), "spine": (g["sx0"], 0, g["sx1"], H)}.get(panel, (0, 0, W, H))
def crop_box(iw, ih, rw, rh, zoom, fx, fy):
    """Source-pixel crop box for a region of size rw x rh: largest box of that shape, shrunk by zoom, centred on (fx%, fy%) and kept inside the picture."""
    a = rw / rh
    bw = min(iw, ih * a); bh = bw / a
    bw /= max(1.0, zoom); bh /= max(1.0, zoom)
    cx = min(max(fx / 100 * iw, bw / 2), iw - bw / 2); cy = min(max(fy / 100 * ih, bh / 2), ih - bh / 2)
    return (cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2)
def _rgb(h): return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))
def tint_image(im, tint, amt):
    """Re-colour a picture to `tint` while keeping its texture (light and dark detail stays)."""
    from PIL import ImageOps, Image
    t = _rgb(tint); g = ImageOps.autocontrast(ImageOps.grayscale(im), cutoff=2)
    g = g.point(lambda v: int(128 + (v - 128) * .6))
    dark = tuple(int(v * .42) for v in t); light = tuple(min(255, int(v + (255 - v) * .30)) for v in t)
    col = ImageOps.colorize(g, dark, light, mid=t, blackpoint=0, whitepoint=255, midpoint=118)
    return Image.blend(im, col, max(0.0, min(1.0, amt / 100)))
def to_srgb(im):
    from PIL import ImageCms
    try:
        icc = im.info.get("icc_profile")
        if icc and im.mode in ("RGB", "RGBA", "CMYK", "L"):
            src = ImageCms.ImageCmsProfile(io.BytesIO(icc)); dst = ImageCms.createProfile("sRGB")
            im = ImageCms.profileToProfile(im, src, dst, outputMode="RGB")
    except Exception: pass
    return im.convert("RGB")
def prep_image(src, cache, rw_in, rh_in, zoom, fx, fy, tint, tint_amt):
    """Crop, colour-manage, tint and size a picture for the print file. Returns (jpeg path, effective dpi). Never upscales."""
    from PIL import Image, ImageOps
    st = os.stat(src); key = hashlib.sha1(json.dumps([os.path.basename(src), st.st_size, round(rw_in, 3), round(rh_in, 3), round(zoom, 3), round(fx, 2), round(fy, 2), tint, round(tint_amt)]).encode()).hexdigest()[:16]
    os.makedirs(cache, exist_ok=True); out = os.path.join(cache, key + ".jpg"); meta = out + ".dpi"
    if os.path.exists(out) and os.path.exists(meta): return out, float(open(meta).read())
    im = Image.open(src); im = ImageOps.exif_transpose(im); im = to_srgb(im)
    box = crop_box(im.width, im.height, rw_in, rh_in, zoom, fx, fy)
    l, t, r, b = [int(round(v)) for v in box]; r = max(r, l + 1); b = max(b, t + 1)
    im = im.crop((l, t, r, b)); dpi = im.width / rw_in
    tw = int(round(rw_in * 300))
    if im.width > tw: im = im.resize((tw, max(1, int(round(tw * rh_in / rw_in)))), Image.LANCZOS)
    if tint: im = tint_image(im, tint, tint_amt)
    im.save(out, "JPEG", quality=92, subsampling=0, optimize=True, dpi=(300, 300)); open(meta, "w").write(str(dpi))
    old = sorted([os.path.join(cache, f) for f in os.listdir(cache) if f.endswith(".jpg")], key=os.path.getmtime)
    for f in old[:-24]:
        for q in (f, f + ".dpi"):
            try: os.remove(q)
            except Exception: pass
    return out, dpi
def make_texture(kind, w_in, h_in, path, seed=None):
    """Draw a seamless-looking grey texture (leather or linen) at 300 dpi (capped) and save it as a JPEG. Colour comes later from the tint."""
    from PIL import Image, ImageChops, ImageFilter, ImageDraw, ImageOps
    rnd = random.Random(seed); dpi = 300
    w, h = int(w_in * dpi), int(h_in * dpi)
    while w * h > 14_000_000: dpi -= 20; w, h = int(w_in * dpi), int(h_in * dpi)
    def noise(cell, sigma=64):
        n = Image.effect_noise((max(2, w // cell + 2), max(2, h // cell + 2)), sigma)
        return n.resize((w, h), Image.BICUBIC)
    if kind == "linen":
        tile = Image.new("L", (24, 24), 128); d = ImageDraw.Draw(tile)
        for i in range(0, 24, 6):
            for j in range(0, 24, 6):
                over = ((i // 6) + (j // 6)) % 2 == 0
                d.rectangle([i, j, i + 5, j + 5], fill=150 if over else 100)
                d.line([i, j, i + 5, j], fill=185 if over else 130); d.line([i, j + 5, i + 5, j + 5], fill=70)
        base = Image.new("L", (w, h))
        for x in range(0, w, 24):
            for y in range(0, h, 24): base.paste(tile, (x, y))
        hs = Image.effect_noise((max(2, w // 60 + 2), h), 40).resize((w, h), Image.BICUBIC)
        vs = Image.effect_noise((w, max(2, h // 60 + 2)), 40).resize((w, h), Image.BICUBIC)
        streak = ImageChops.add(ImageChops.multiply(hs, Image.new("L", (w, h), 255)), vs, scale=2)
        im = ImageChops.add(base, streak, scale=1.6, offset=-40)
    else:
        hmap = None
        for cell, wt in ((22, .5), (11, .32), (5, .18)):
            n = noise(cell, 60)
            ridged = n.point(lambda v: 255 - min(255, abs(v - 128) * 1.6))
            ridged = ridged.point(lambda v, wt=wt: int(v * wt))
            hmap = ridged if hmap is None else ImageChops.add(hmap, ridged)
        hmap = hmap.filter(ImageFilter.GaussianBlur(1.8))
        light = hmap.filter(ImageFilter.EMBOSS)
        light = light.point(lambda v: min(255, max(0, int((v - 128) * 1.1 + 128))))
        fine = noise(2, 40).point(lambda v: int(v * .4 + 76))
        mott = noise(260, 60).point(lambda v: int(v * .5 + 64))
        im = ImageChops.blend(light, hmap, .5)
        im = ImageChops.blend(im, fine, .12); im = ImageChops.blend(im, mott, .12)
        flat = Image.new("L", im.size, 128); im = ImageChops.blend(ImageOps.autocontrast(im, cutoff=.5), flat, .25)
    from PIL import ImageOps
    im = ImageOps.autocontrast(im, cutoff=.5).convert("RGB")
    im.save(path, "JPEG", quality=92, subsampling=0, optimize=True)
    return im.size
def draw_text(c, x, y, s, f, size, col, foil):
    """Draw one line of text. foil = '' for flat colour, or a FOILS key for shiny metallic lettering."""
    if not foil or not s.strip():
        c.setFillColor(col); c.setFont(f, size); c.drawString(x, y, s); return
    stops, edge, _ = FOILS[foil]; w = pdfmetrics.stringWidth(s, f, size)
    c.saveState(); c.setFillColor(HexColor("#000000")); c.setFillAlpha(.40); c.setFont(f, size); c.drawString(x + size * .028, y - size * .04, s); c.restoreState()
    c.saveState(); t = c.beginText(); t.setTextOrigin(x, y); t.setFont(f, size); t.setTextRenderMode(7); t.textOut(s); c.drawText(t)
    c.linearGradient(x, y - size * .24, x + size * .45, y + size * .82, [HexColor(h) for _, h in stops], [p for p, _ in stops], extend=True); c.restoreState()
    c.saveState(); c.setStrokeColor(HexColor(edge)); c.setLineWidth(max(.35, size * .014)); t = c.beginText(); t.setTextOrigin(x, y); t.setFont(f, size); t.setTextRenderMode(1); t.textOut(s); c.drawText(t); c.restoreState()
def image_report(b, imgdir):
    """[(element id, panel, effective dpi or None if the picture file is missing)] for every picture on the cover."""
    g = geometry(b); out = []
    for e in b["cover"]["elements"]:
        if e["type"] != "image": continue
        p = os.path.join(imgdir, e["img"]) if (imgdir and e["img"]) else ""
        if not p or not os.path.exists(p): out.append((e["id"], e["panel"], None)); continue
        from PIL import Image
        x0, y0, x1, y1 = region(g, e["panel"]); rw, rh = (x1 - x0) / IN, (y1 - y0) / IN
        with Image.open(p) as im:
            bx = crop_box(im.width, im.height, rw, rh, e["zoom"], e["fx"], e["fy"])
        out.append((e["id"], e["panel"], (bx[2] - bx[0]) / rw))
    return out
def _lines(text, font, size, width):
    out = []
    for para in text.split("\n"):
        out += simpleSplit(para, font, size, width) if para.strip() else [""]
    return out
def cover(b, path, guides=False, imgdir=None):
    C = b["cover"]; g = geometry(b); W, H = g["W"], g["H"]
    c = canvas.Canvas(path, pagesize=(W, H), initialFontName=fn(C["font"])); c.setTitle(b["title"] or b["name"])
    c.setFillColor(HexColor(C["bg"])); c.rect(0, 0, W, H, fill=1, stroke=0)
    pcol = HexColor(C["pattern_color"]); c.setStrokeColor(pcol); c.setFillColor(pcol); c.setLineWidth(1)
    if C["pattern"] == "lines":
        y = 0.5 * IN
        while y < H: c.line(0, y, W, y); y += .32 * IN
    elif C["pattern"] == "grid":
        y = 0
        while y < H: c.line(0, y, W, y); y += .4 * IN
        x = 0
        while x < W: c.line(x, 0, x, H); x += .4 * IN
    elif C["pattern"] == "dots":
        y = .2 * IN
        while y < H:
            x = .2 * IN
            while x < W: c.circle(x, y, 1.3, stroke=0, fill=1); x += .3 * IN
            y += .3 * IN
    elif C["pattern"] == "diagonal":
        x = -H
        while x < W: c.line(x, 0, x + H, H); x += .45 * IN
    if C["frame"]:
        c.setStrokeColor(HexColor(C["frame_color"])); c.setLineWidth(2.5)
        for k in ("front", "back"):
            x0, y0, x1, y1 = g["safe"][k]; c.rect(x0 - 8, y0 - 8, x1 - x0 + 16, y1 - y0 + 16, stroke=1, fill=0)
    boxes = []
    for e in sorted(C["elements"], key=lambda q: {"full": 0, "spine": 1}.get(q["panel"], 2)):
        if e["type"] != "image" or not imgdir or not e["img"]: continue
        sp_ = os.path.join(imgdir, e["img"])
        if not os.path.exists(sp_): continue
        x0, y0, x1, y1 = region(g, e["panel"])
        pth, _d = prep_image(sp_, os.path.join(imgdir, "cache"), (x1 - x0) / IN, (y1 - y0) / IN, e["zoom"], e["fx"], e["fy"], e["tint"], e["tint_amt"])
        c.drawImage(pth, x0, y0, x1 - x0, y1 - y0)
    for e in C["elements"]:
        if e["type"] == "image": continue
        fam = e["font"] or C["font"]; col = HexColor(e["color"] or C["text"]); f = fn(fam, e["bold"])
        if e["panel"] == "full": x0, y0, x1, y1 = 0, 0, W, H
        elif e["panel"] == "spine": x0, y0, x1, y1 = g["sx0"], g["spine_len"][0], g["sx1"], g["spine_len"][1]
        else: x0, y0, x1, y1 = g["safe"][e["panel"]]
        sw_, sh_ = x1 - x0, y1 - y0
        if e["type"] == "rect":
            rx = x0 + e["x"] / 100 * sw_; rw = e["w"] / 100 * sw_; rh = e["h"] / 100 * sh_; ry = y1 - e["y"] / 100 * sh_ - rh
            c.setFillColor(col); c.rect(rx, ry, rw, rh, fill=1, stroke=0); continue
        if e["panel"] == "spine":
            lines = _lines(e["text"], f, e["size"], 10 ** 6); L = y1 - y0
            tw_ = max([pdfmetrics.stringWidth(l, f, e["size"]) for l in lines] or [0])
            start = {"left": y1 - e["y"] / 100 * L, "center": (y0 + y1) / 2 + tw_ / 2, "right": y0 + e["y"] / 100 * L + tw_}[e["align"]]
            cx = (g["sx0"] + g["sx1"]) / 2; n = len(lines)
            c.saveState(); c.setFillColor(col); c.setFont(f, e["size"]); c.translate(cx, start); c.rotate(-90)
            for i, l in enumerate(lines): draw_text(c, 0, -(e["size"] * .3) + (n - 1) * e["size"] * e["lh"] / 2 - i * e["size"] * e["lh"], l, f, e["size"], col, e["foil"])
            c.restoreState()
            boxes.append(("spine", e["id"], cx - e["size"] * .55 * n, start - tw_, cx + e["size"] * .55 * n, start, e["size"]))
            continue
        width = e["w"] / 100 * sw_; lines = _lines(e["text"], f, e["size"], width)
        top = y1 - e["y"] / 100 * sh_; left = x0 + e["x"] / 100 * sw_; c.setFillColor(col); c.setFont(f, e["size"])
        yy = top - e["size"] * .8
        for l in lines:
            lw = pdfmetrics.stringWidth(l, f, e["size"])
            xx = {"left": left, "center": left + (width - lw) / 2, "right": left + width - lw}[e["align"]]
            draw_text(c, xx, yy, l, f, e["size"], col, e["foil"])
            if l.strip(): boxes.append((e["panel"], e["id"], xx, yy - e["size"] * .22, xx + lw, yy + e["size"] * .78, e["size"]))
            yy -= e["size"] * e["lh"]
    if C["barcode_box"]:
        c.setFillColor(HexColor("#ffffff")); bx = g["barcode"]; c.rect(bx[0], bx[1], bx[2] - bx[0], bx[3] - bx[1], fill=1, stroke=0)
    if guides:
        lab = lambda t, x, y, col: (c.setFillColor(HexColor(col)), c.setFont(fn("Bitstream Vera"), 8), c.drawString(x, y, t))
        c.setLineWidth(1); c.setDash(4, 3); c.setStrokeColor(HexColor("#ff3b3b"))
        c.rect(g["bx0"], g["ty0"], g["fx1"] - g["bx0"], g["ty1"] - g["ty0"], fill=0); lab("TRIM EDGE", g["bx0"] + 3, g["ty0"] + 3, "#ff3b3b")
        c.setStrokeColor(HexColor("#2bd96b"))
        for k in ("back", "front"):
            x0, y0, x1, y1 = g["safe"][k]; c.rect(x0, y0, x1 - x0, y1 - y0, fill=0); lab("SAFE ZONE", x0 + 3, y1 - 10, "#2bd96b")
        c.setStrokeColor(HexColor("#4da3ff"))
        for x in (g["bx1"], g["sx0"], g["sx1"], g["fx0"]): c.line(x, 0, x, H)
        lab("SPINE %.3f in" % g["sp"], g["sx0"] - 20, g["ty1"] + 12, "#4da3ff")
        c.setStrokeColor(HexColor("#ffd34d")); bx = g["barcode"]; c.rect(bx[0], bx[1], bx[2] - bx[0], bx[3] - bx[1], fill=0)
        lab("BARCODE AREA (keep clear)", bx[0] + 4, bx[1] + 4, "#ffd34d"); c.setDash()
    c.save()
    return dict(w=g["W"] / IN, h=g["H"] / IN, spine=g["sp"], boxes=boxes, geo=g)
def overflow(b, info):
    """Plain-English problems in the cover layout (used after every chat change and in the check)."""
    g = info["geo"]; out = []; seen = set()
    for panel, eid, x0, y0, x1, y1, size in info["boxes"]:
        if panel == "spine":
            if size > (g["sw"] - 8) * .8 and ("sp", eid) not in seen: seen.add(("sp", eid)); out.append(f"spine text {eid} is too big for the spine ({g['sp']:.2f} in wide)")
            if (y0 < g["spine_len"][0] - 1 or y1 > g["spine_len"][1] + 1) and ("sl", eid) not in seen: seen.add(("sl", eid)); out.append(f"spine text {eid} is too long for the spine")
            continue
        if panel == "full": continue
        s = g["safe"][panel]
        if (x0 < s[0] - .5 or x1 > s[2] + .5 or y0 < s[1] - .5 or y1 > s[3] + .5) and (eid, "s") not in seen:
            seen.add((eid, "s")); out.append(f"text {eid} on the {panel} goes outside the safe zone")
        bc = g["barcode"]
        if panel == "back" and x0 < bc[2] and x1 > bc[0] and y0 < bc[3] and y1 > bc[1] and (eid, "b") not in seen:
            seen.add((eid, "b")); out.append(f"text {eid} overlaps the barcode area")
    return out
# ---- rendering helpers ----
def png(pdf, out, page=1, dpi=70):
    subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi), "-png", "-singlefile", pdf, out], check=True, timeout=60)
    return out + ".png"
def check(b, cpdf, ipdf, info, imgdir=None):
    r = []; add = lambda lvl, t: r.append({"level": lvl, "text": t}); p = b["pages"]
    add("ok" if SPEC["min_pages"] <= p <= SPEC["max_pages"] else "fail", f"Page count {p} (hardcover needs {SPEC['min_pages']} to {SPEC['max_pages']})")
    add("ok" if p % 2 == 0 else "fail", "Page count is even")
    cw, ch, sp = cover_size(p, b["paper"]); add("ok", f"Cover file {cw:.3f} x {ch:.3f} in, spine {sp:.3f} in")
    add("ok" if SPEC["verified"] else "warn", "Cover size verified against KDP's cover calculator" if SPEC["verified"] else "Cover size NOT yet verified against KDP's cover calculator (do once before uploading)")
    g = max(b["inside"]["inner"], gutter(p)); add("ok", f"Inside margin {g:.3f} in (KDP minimum {gutter(p)})")
    pr = overflow(b, info)
    add("ok" if not pr else "fail", "All cover text inside the safe zone and clear of the barcode area" if not pr else "; ".join(pr))
    if not b["cover"]["elements"]: add("warn", "The cover is empty (no text yet)")
    k = contrast(b["inside"]["color"], b["inside"]["page_bg"]); add("ok" if k >= 4.5 else "warn" if k >= 3 else "fail", f"Inside text contrast {k:.1f}:1")
    for e in b["cover"]["elements"]:
        if e["type"] == "text" and e["text"].strip() and not any(x["type"] == "image" for x in b["cover"]["elements"]):
            k = contrast(FOILS[e["foil"]][2] if e["foil"] else (e["color"] or b["cover"]["text"]), b["cover"]["bg"])
            if k < 3: add("warn", f"Cover text {e['id']} is hard to read against the background ({k:.1f}:1)")
    for iid, pan, dpi_ in (image_report(b, imgdir) if imgdir else []):
        if dpi_ is None: add("fail", f"The picture on the {pan} is missing from the Pi")
        elif dpi_ >= 290: add("ok", f"Picture on the {pan}: sharp ({dpi_:.0f} dpi)")
        elif dpi_ >= 200: add("warn", f"Picture on the {pan}: {dpi_:.0f} dpi. KDP wants 300; it will print a little soft")
        else: add("fail", f"Picture on the {pan}: only {dpi_:.0f} dpi, it will look blurry. Use a bigger photo or zoom out")
    for f, pdf in (("cover", cpdf), ("interior", ipdf)):
        try:
            o = subprocess.run(["pdffonts", pdf], capture_output=True, text=True, timeout=20).stdout.splitlines()[2:]
            ne = [l for l in o if l.strip() and (re.findall(r"\s(yes|no)\s", l) or ["no"])[0] != "yes"]
            add("ok" if not ne else "fail", f"{f} PDF fonts embedded" if not ne else f"{f} PDF has fonts that are not embedded")
        except Exception: add("warn", "Could not check embedded fonts")
    L = b["listing"]
    add("ok" if b["author"] else "warn", "Author / pen name set" if b["author"] else "Author / pen name not set")
    add("ok" if b["title"] else "warn", "Title set" if b["title"] else "Title not set")
    add("ok" if len((b["title"] + " " + b["subtitle"]).strip()) <= 200 else "fail", "Title + subtitle length OK")
    add("ok" if L["description"] else "warn", "Book description written" if L["description"] else "Book description not written")
    add("ok" if len(L["keywords"]) >= 7 else "warn", f"{len(L['keywords'])} of 7 keywords")
    add("ok" if L["price"] else "warn", "Price set" if L["price"] else "Price not set")
    return r
