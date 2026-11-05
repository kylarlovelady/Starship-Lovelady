import os, re, json, uuid, hmac, glob, zipfile, hashlib, shutil, urllib.request, urllib.error, io
from pathlib import Path
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from starlette.exceptions import HTTPException
from starlette.responses import HTMLResponse, FileResponse, JSONResponse, Response
from starlette.concurrency import run_in_threadpool
import engine
from engine import DEFAULT, clean, merge, SPEC
ROOT = Path(os.environ.get("KDP_HOME", Path.home() / "kdp-studio")); BOOKS = ROOT / "books"; BOOKS.mkdir(parents=True, exist_ok=True)
import threading
LOCK = threading.RLock()
ROUTES = []
def route(path, methods=("GET",), auth=True, raw=False):
    def deco(f):
        async def h(request):
            if auth: pin_ok(request)
            body = {}
            if request.method in ("POST", "PUT"):
                rawb = await request.body()
                if raw: body = rawb
                elif rawb:
                    try: body = json.loads(rawb)
                    except Exception: raise HTTPException(400, "bad json")
            r = await run_in_threadpool(f, request, body, **request.path_params)
            return r if isinstance(r, Response) else JSONResponse(r)
        ROUTES.append(Route(path, h, methods=list(methods))); return f
    return deco
def pin_ok(request):
    try: want = (ROOT / "pin.txt").read_text().strip()
    except Exception: raise HTTPException(503, "No PIN set")
    if not hmac.compare_digest(request.headers.get("x-pin", ""), want): raise HTTPException(401, "Wrong PIN")
def bdir(i):
    if not re.fullmatch(r"[a-z0-9-]{3,60}", i): raise HTTPException(404)
    d = BOOKS / i
    if not d.is_dir(): raise HTTPException(404)
    return d
def load(i): return clean(json.loads((bdir(i) / "book.json").read_text()))
def save(i, b): (BOOKS / i / "book.json").write_text(json.dumps(b, indent=1))
def sets():
    try: return json.loads((ROOT / "settings.json").read_text())
    except Exception: return {}
def render(i, guides=False):
    with LOCK: return _render(i)
def _render(i):
    b = load(i); d = bdir(i) / "out"; d.mkdir(exist_ok=True)
    h = hashlib.sha1(json.dumps({k: v for k, v in b.items() if k not in ("name", "listing", "answers")}, sort_keys=True).encode()).hexdigest()[:10]
    cp, gp, ip = d / f"{h}_cover.pdf", d / f"{h}_coverg.pdf", d / f"{h}_interior.pdf"
    if not ip.exists():
        for f in d.glob("*"):
            if not f.name.startswith(h): f.unlink()
        engine.interior(b, str(ip)); idir = str(bdir(i) / "img"); engine.cover(b, str(cp), imgdir=idir); engine.cover(b, str(gp), guides=True, imgdir=idir)
    info = engine.cover(b, "/dev/null") if False else None
    return b, cp, gp, ip, h
@route("/health", auth=False)
def health(request, body): return {"ok": True}
@route("/", auth=False)
def home(request, body): return HTMLResponse((Path(__file__).parent / "index.html").read_text())
@route("/api/books", methods=("GET",))
def books(request, body):
    out = []
    for d in sorted(BOOKS.iterdir(), key=lambda p: -p.stat().st_mtime):
        try:
            b = json.loads((d / "book.json").read_text()); out.append({"id": d.name, "name": b.get("name") or b.get("title"), "title": b.get("title")})
        except Exception: pass
    return out
@route("/api/books", methods=("POST",))
def new_book(request, body):
    src = body.get("copy"); b = load(src) if src else clean({}); b["chat"] = []
    if body.get("name"): b["name"] = str(body["name"])[:60]
    elif src: b["name"] = b["name"] + " copy"
    i = re.sub(r"[^a-z0-9]+", "-", b["name"].lower()).strip("-")[:30] or "book"; i = f"{i}-{uuid.uuid4().hex[:4]}"
    (BOOKS / i).mkdir(); save(i, b); return {"id": i, "book": b}
@route("/api/books/{i}", methods=("GET",))
def get_book(request, body, i): return load(i)
@route("/api/books/{i}", methods=("PUT",))
def put_book(request, body, i):
    bdir(i); b = clean(body); save(i, b); return b
@route("/api/books/{i}", methods=("DELETE",))
def del_book(request, body, i): shutil.rmtree(bdir(i)); return {"ok": True}
@route("/api/books/{i}/cover.png", methods=("GET",))
def cover_png(request, body, i):
    guides = int(request.query_params.get("guides", 1)); dpi = int(request.query_params.get("dpi", 70)); b, cp, gp, ip, h = render(i); pdf = gp if guides else cp
    out = str(pdf)[:-4] + f"_{dpi}"; p = out + ".png"
    with LOCK:
        b, cp, gp, ip, h = _render(i); pdf = gp if guides else cp; out = str(pdf)[:-4] + f"_{dpi}"; p = out + ".png"
        if not os.path.exists(p): engine.png(str(pdf), out, 1, max(30, min(dpi, 150)))
        data = open(p, "rb").read()
    return Response(data, media_type="image/png")
@route("/api/books/{i}/page/{n:int}.png", methods=("GET",))
def page_png(request, body, i, n):
    dpi = int(request.query_params.get("dpi", 70)); b, cp, gp, ip, h = render(i); n = max(1, min(n, b["pages"])); out = str(ip)[:-4] + f"_{n}_{dpi}"
    with LOCK:
        b, cp, gp, ip, h = _render(i); out = str(ip)[:-4] + f"_{n}_{dpi}"
        if not os.path.exists(out + ".png"): engine.png(str(ip), out, n, max(30, min(dpi, 150)))
        data = open(out + ".png", "rb").read()
    return Response(data, media_type="image/png")
@route("/api/books/{i}/check", methods=("GET",))
def do_check(request, body, i):
    b, cp, gp, ip, h = render(i); info = engine.cover(b, "/dev/null")
    return {"checks": engine.check(b, str(cp), str(ip), info, str(bdir(i) / "img")), "pages_plan": engine.plan(b)}
@route("/api/books/{i}/export.zip", methods=("GET",))
def export(request, body, i):
    b, cp, gp, ip, h = render(i); L = b["listing"]
    txt = (f"TITLE: {b['title']}\nSUBTITLE: {b['subtitle']}\nAUTHOR: {b['author']}\n\nDESCRIPTION:\n{L['description']}\n\nKEYWORDS:\n" + "\n".join(L["keywords"]) +
           f"\n\nCATEGORIES: {L['categories']}\nPRICE: {L['price']}\nFORMAT: Hardcover, 6 x 9 in, {b['paper']} paper, {b['pages']} pages, black and white interior\n")
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.write(cp, "cover.pdf"); z.write(ip, "interior.pdf"); z.writestr("listing.txt", txt)
    return Response(buf.getvalue(), media_type="application/zip", headers={"Content-Disposition": f'attachment; filename="{i}.zip"'})
# ---- chat ----
def snapshot(i, b):
    h = BOOKS / i / "history"; h.mkdir(exist_ok=True)
    n = len(list(h.glob("*.json"))) + 1
    (h / f"{n:04d}.json").write_text(json.dumps({k: v for k, v in b.items() if k != "chat"}))
    for old in sorted(h.glob("*.json"))[:-25]: old.unlink()
def ai_json(system, user):
    key = sets().get("openai_key") or os.environ.get("OPENAI_API_KEY")
    if not key: return {"nokey": True}
    fake = os.environ.get("KDP_FAKE_AI")
    if fake and os.path.exists(fake):
        q = json.load(open(fake)); r = q.pop(0); json.dump(q, open(fake, "w")); return r
    req = urllib.request.Request("https://api.openai.com/v1/chat/completions", method="POST",
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
        data=json.dumps({"model": sets().get("model", "gpt-4o-mini"), "response_format": {"type": "json_object"}, "temperature": 0.2,
                         "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}]}).encode())
    try: return json.loads(json.loads(urllib.request.urlopen(req, timeout=90).read())["choices"][0]["message"]["content"])
    except urllib.error.HTTPError as e:
        return {"error": "OpenAI said " + str(e.code) + (" (the key looks wrong or has no access)" if e.code in (401, 403) else "")}
    except Exception as e: return {"error": str(e)[:160]}
SYS = """You are the assistant inside KDP Studio, a tool that builds a 6x9 inch HARDCOVER lined journal for Amazon KDP. The user talks to you in plain words; you change the book by returning operations.
Reply ONLY with JSON: {"ops":[...],"reply":"short friendly message","asked":["idea_id"]}
RULES
1. Do exactly what the user asks and nothing more. NEVER invent or add content (titles, taglines, slogans, descriptions, bullets, colors, extra pages, decorations) the user did not ask for. Text the user dictates must be copied exactly (their spelling, capitals, punctuation) unless they ask you to change it.
2. If a request is unclear (which side? what words? what color?), return "ops":[] and ask ONE short question.
3. Plain, short, friendly language. No jargon. Do not list what you changed (the app shows the changes itself).
4. After doing what was asked you MAY ask at most ONE follow-up from ideas_not_yet_asked, only if clearly relevant to what they are making, phrased naturally in your reply, and put its id in "asked". Never ask an id in already_asked. Do not ask a follow-up when the request was unclear or the user is just chatting.
5. If the user answers yes to a question you asked, apply it with ops. If no, do nothing.
5a. HONESTY: only say you did something that your ops actually did. If you cannot do what was asked (for example make a texture or picture, print foil, or a setting that does not exist), say so plainly and return "ops":[]. Never say "done" or "I have updated" when ops is empty.
5b. COLORS: when the user says "more X", "darker", "lighter", "brighter" or similar, change the color by a CLEARLY VISIBLE amount (at least 15 points of lightness), never a tiny shift. Reference colors: maroon #5A0F1E, mahogany #6B1A12, burgundy #6D0F26, gold #D4AF37, yellow gold #F2C230, steel gray #3A4048, navy #14233F, forest green #17402B. If the result would look nearly the same as before, push it further. If the user names a color, use that named color's reference value.
OPS
{"op":"set","path":"cover.bg","value":"#112233"}  set any value in the book JSON by dotted path (not chat, answers, cover.elements)
{"op":"add","el":{...}}  add a cover element (an id is assigned)
{"op":"update","id":"e3","set":{"x":10}}  change fields of an element
{"op":"remove","id":"e3"}   {"op":"clear_elements","panel":"front"}  (panel optional = all)
COVER ELEMENTS: {"type":"text"|"rect","panel":"front"|"back"|"spine"|"full","x","y","w","h","size","text","bold","align":"left"|"center"|"right","font","color","lh","foil":""|"gold"|"antique_gold"|"silver"|"copper"}
 - foil makes TEXT shiny metallic (gradient shine). When the user asks for gold / shiny / metallic / foil lettering use "foil":"gold" (or antique_gold, silver, copper). A flat yellow or orange color is NOT gold. Use foil only when asked or when they asked for gold or silver lettering.
 - PICTURES: elements with "type":"image" already exist only if the user added a photo or a built-in texture with the picture button. You can change them with "update" using: tint ("#rrggbb" re-colours the picture and keeps its texture; "" = original colours), tint_amt (0-100), zoom (1-8), fx and fy (0-100, which part of the picture is centred). You cannot create pictures or textures yourself. If the user asks for a texture, leather, linen, a photo or a picture, do NOT change colours to fake it: reply that they should tap the picture button (next to the message box) to add a photo or a leather/linen texture, and return "ops":[]. To recolour a picture or texture the user already added (for example "make the leather burgundy"), update its tint (use the reference colors).
 - front and back are each a 6x9 inch cover panel; x,y,w,h are PERCENT (0-100) of that panel's safe area, y measured from the TOP (0 top, 50 middle, 100 bottom). Text starts at x,y (top-left of the text block), wraps inside width w, aligned inside that block. To centre across the panel use x=0,w=100,align=center.
 - size is points: big title 40-60, subtitle 16-24, normal text 11-16. Long titles wrap onto lines; pick a size that fits (the app warns when it does not fit).
 - "rect" is a solid colour box (x,y,w,h in percent) with colour in "color". panel "full" = the whole cover file (back+spine+front) for bands that run across everything.
 - spine: text reads downward. align left = near the top, center = middle, right = near the bottom, y = percent offset from that end. size must be small enough for spine_inches (max about spine_inches*50 points).
 - color is #rrggbb (empty = cover.text); font is one of the fonts list (empty = cover.font); bold true/false.
 - NEVER place anything in the bottom-right of the back cover: that is reserved for the barcode (about 2x1.2 inches, 0.76 in above the bottom edge).
 - Keep text readable: no dark text on a dark background.
BOOK PATHS: title, subtitle, author (used for listing and page headers, NOT drawn on the cover automatically), pages (even number 75-550), paper (white|cream), cover.bg, cover.text (default text colour), cover.font, cover.pattern (none|lines|dots|grid|diagonal), cover.pattern_color, cover.frame (bool), cover.frame_color, cover.barcode_box (true draws a white box where KDP puts its barcode),
 inside.font, inside.color, inside.page_bg, inside.style (lines|dots|grid|blank), inside.line_color, inside.line_width (0.1-2), inside.spacing (inches 0.2-0.6), inside.dash, inside.header (none|date|title|date_title|custom), inside.header_text, inside.num_pos (center|outer|none), inside.num_style (plain|dash|of), inside.num_size, inside.inner/outer/top/bottom (margins, inches),
 front.title_page (bool), front.owner_page (bool), front.owner_heading (text), front.owner_fields (list of line labels), front.owner_footer (text), front.contacts (number of pages), front.index (pages), front.goals (bool), back.notes_pages (number), labels.contacts / labels.index / labels.goals / labels.notes (page headings),
 listing.description, listing.keywords (list of up to 7), listing.categories, listing.price. Only fill listing fields when the user asks you to.
Inside pages are fixed to the KDP-safe template (6x9 in, correct gutter); change only the settings above."""
IDEAS = [
 ("owner_page", "an owner page (name, company, phone, email, 'if found return to')", lambda b: not b["front"]["owner_page"]),
 ("contacts", "contact pages near the front", lambda b: b["front"]["contacts"] == 0),
 ("index", "an index (page / topic / date) at the front", lambda b: b["front"]["index"] == 0),
 ("goals", "a goals / checklist page", lambda b: not b["front"]["goals"]),
 ("date_header", "a Date line at the top of every writing page", lambda b: b["inside"]["header"] == "none"),
 ("notes_back", "extra notes pages at the back", lambda b: b["back"]["notes_pages"] == 0),
 ("title_page", "a title page at the front", lambda b: not b["front"]["title_page"]),
 ("spine_text", "text on the spine", lambda b: not any(e["panel"] == "spine" for e in b["cover"]["elements"])),
 ("back_text", "text on the back cover", lambda b: not any(e["panel"] == "back" for e in b["cover"]["elements"])),
 ("author", "the author / pen name", lambda b: not b["author"]),
 ("listing", "the Amazon listing (description, keywords, price)", lambda b: not b["listing"]["description"]),
]
def apply_ops(b, ops):
    done = 0; F = engine.discover()
    for o in ops if isinstance(ops, list) else []:
        if not isinstance(o, dict): continue
        k = o.get("op"); els = b["cover"]["elements"]
        if k == "set" and isinstance(o.get("path"), str):
            p = o["path"].split("."); 
            if p[0] in ("chat", "answers") or p[:2] == ["cover", "elements"] or p[0] not in engine.DEFAULT: continue
            t = b
            for q in p[:-1]:
                if not isinstance(t, dict) or q not in t: t = None; break
                t = t[q]
            if isinstance(t, dict) and p[-1] in t: t[p[-1]] = o.get("value"); done += 1
        elif k == "add" and isinstance(o.get("el"), dict) and o["el"].get("type") != "image": els.append(o["el"]); b["cover"]["elements"] = engine.clean({"cover": {"elements": els}})["cover"]["elements"]; done += 1
        elif k == "update" and isinstance(o.get("set"), dict):
            for e in els:
                if e["id"] == o.get("id"): e.update({kk: vv for kk, vv in o["set"].items() if kk != "id"}); done += 1
        elif k == "remove": n = len(els); b["cover"]["elements"] = [e for e in els if e["id"] != o.get("id")]; done += n - len(b["cover"]["elements"])
        elif k == "clear_elements": n = len(els); b["cover"]["elements"] = [e for e in els if o.get("panel") and e["panel"] != o["panel"]]; done += n - len(b["cover"]["elements"])
    return done
def flat(d, pre=""):
    out = {}
    for k, v in d.items():
        if k in ("chat", "answers", "elements"): continue
        if isinstance(v, dict): out.update(flat(v, pre + k + "."))
        else: out[pre + k] = v
    return out
def describe(before, after):
    ch = []; fb, fa = flat(before), flat(after)
    for k in fa:
        if fb.get(k) != fa[k]: ch.append(f"{k}: {fb.get(k) if fb.get(k) not in ('', None) else '(empty)'} → {fa[k] if fa[k] != '' else '(empty)'}")
    be = {e["id"]: e for e in before["cover"]["elements"]}; ae = {e["id"]: e for e in after["cover"]["elements"]}
    for i, e in ae.items():
        what = f"“{e['text'][:40]}”" if e["type"] == "text" else ("a picture" if e["type"] == "image" else "a colour box")
        if i not in be: ch.append(f"added {what} on the {e['panel']} (size {e['size']:g}, {e['align']}{', ' + e['foil'] + ' foil' if e['foil'] else ''})" if e["type"] == "text" else f"added {what} on the {e['panel']}")
        elif be[i] != e:
            g = lambda v: format(v, "g") if isinstance(v, float) else v
            diff = ", ".join(f"{k} {g(be[i][k]) or '(none)'} → {g(e[k]) or '(none)'}" for k in e if be[i].get(k) != e[k])
            ch.append(f"changed {what} on the {e['panel']}: {diff}")
    for i, e in be.items():
        if i not in ae: ch.append(f"removed {'a picture' if e['type'] == 'image' else '“' + e['text'][:40] + '”'} from the {e['panel']}")
    return ch[:14]
KEYRE = re.compile(r"^sk-[A-Za-z0-9_\-]{20,300}$")
GREETING = ("This is a blank 6x9 hardcover journal: 120 pages, lined, with page numbers. Nothing is filled in. "
            "Tell me what goes on the cover and where, for example: “put RUN-PLANT ENGINEER in big gold letters at the top of the front, centered.” "
            "Tap the picture button next to the message box to add a photo or a leather or linen texture.")
@route("/api/books/{i}/chat", methods=("POST",))
def chat(request, body, i):
    b = load(i); text = str(body.get("text", "")).strip()[:2000]
    if not text: return {"book": b, "reply": "", "changes": []}
    def say(reply, changes=None, usertext=text):
        b["chat"] += [{"role": "user", "text": usertext}, {"role": "assistant", "text": reply, "changes": changes or []}]; b2 = engine.clean(b); save(i, b2)
        return {"book": b2, "reply": reply, "changes": changes or []}
    if KEYRE.match(text):
        s = sets(); s["openai_key"] = text; p = ROOT / "settings.json"; p.write_text(json.dumps(s)); os.chmod(p, 0o600)
        return say("Key saved. Now tell me what you want on the book.", usertext="(OpenAI key saved)")
    if not (sets().get("openai_key") or os.environ.get("OPENAI_API_KEY")):
        return say("I need an OpenAI key before I can understand you. Paste it here as a message (it starts with sk-). It stays on your Pi.")
    asked = b["answers"]; ideas = [{"id": k, "about": q} for k, q, c in IDEAS if k not in asked and c(b)]
    sp = engine.spine(b["pages"], b["paper"])
    ctx = {"request": text, "spine_inches": sp, "fonts": list(engine.discover()), "ideas_not_yet_asked": ideas, "already_asked": list(asked),
           "recent_chat": [{"role": m["role"], "text": m["text"]} for m in b["chat"][-8:]],
           "book": {k: v for k, v in b.items() if k not in ("chat", "answers")}}
    r = ai_json(SYS, json.dumps(ctx))
    if not isinstance(r, dict) or r.get("error") or r.get("nokey"):
        return say("I could not reach the AI just now. " + str((r or {}).get("error", "")) + " Nothing was changed.")
    before = json.loads(json.dumps(b)); snapshot(i, b); n = apply_ops(b, r.get("ops"))
    b = engine.clean(b); changes = describe(engine.clean(before), b) if n else []
    for a in r.get("asked", []) if isinstance(r.get("asked"), list) else []:
        if isinstance(a, str) and a in [k for k, q, c in IDEAS]: b["answers"][a] = True
    info = engine.cover(b, "/dev/null"); prob = engine.overflow(b, info)
    reply = str(r.get("reply", "")).strip() or ("Done." if n else "I did not change anything.")
    if not n and not reply.rstrip().endswith("?"):
        if re.search(r"\b(I've|I have|done|updated|added|changed|made|applied|set)\b", reply, re.I): reply = "I did not actually change anything, sorry. Tell me again exactly what you want. For photos or textures, tap the picture button next to the message box."
        else: reply += "\n\n(Nothing was changed.)"
    if prob: reply += "\n\nHeads up: " + "; ".join(prob) + ". Tell me how you want to fix it."
    return say(reply, changes)

# ---- pictures ----
def _imgs(i):
    d = bdir(i) / "img"; d.mkdir(exist_ok=True); return d
def _add_pic(i, panel, name, tint="", tint_amt=100, zoom=1, fx=50, fy=50, note=""):
    from PIL import Image
    b = load(i); snapshot(i, b); before = json.loads(json.dumps(b)); els = b["cover"]["elements"]
    els[:] = [e for e in els if not (e["type"] == "image" and (panel == "full" or e["panel"] == panel))]
    els.insert(0, {"type": "image", "panel": panel, "img": name, "zoom": zoom, "fx": fx, "fy": fy, "tint": tint, "tint_amt": tint_amt})
    b = engine.clean(b); ch = describe(engine.clean(before), b)
    reply = note or "Added your picture."
    b["chat"] += [{"role": "assistant", "text": reply, "changes": ch}]; b = engine.clean(b); save(i, b)
    return {"book": b, "reply": reply, "changes": ch}
@route("/api/books/{i}/regions", methods=("GET",))
def regions(request, body, i):
    b = load(i); g = engine.geometry(b)
    return {p: [round((r[2] - r[0]) / engine.IN, 3), round((r[3] - r[1]) / engine.IN, 3)] for p in ("full", "front", "back") for r in [engine.region(g, p)]}
@route("/api/books/{i}/upload", methods=("POST",), raw=True)
def upload(request, body, i):
    from PIL import Image, ImageOps
    if not body or len(body) > 40_000_000: raise HTTPException(413, "Picture is empty or too big")
    try:
        im = Image.open(io.BytesIO(body)); im.load()
    except Exception: raise HTTPException(400, "That file is not a picture I can read")
    if im.width * im.height > 120_000_000: raise HTTPException(413, "Picture is too big")
    im = engine.to_srgb(ImageOps.exif_transpose(im)); name = uuid.uuid4().hex[:12] + ".jpg"
    im.save(_imgs(i) / name, "JPEG", quality=95, subsampling=0, optimize=True)
    return {"img": name, "w": im.width, "h": im.height}
@route("/api/books/{i}/place", methods=("POST",))
def place(request, body, i):
    name = str(body.get("img", "")); panel = body.get("panel") if body.get("panel") in ("front", "back", "full") else "full"
    if not engine.IMGRE.match(name) or not (_imgs(i) / name).exists(): raise HTTPException(400, "Unknown picture")
    num = lambda k, lo, hi, d: engine._num(body.get(k), lo, hi, d)
    names = {"front": "the front cover", "back": "the back cover", "full": "the whole cover"}
    return _add_pic(i, panel, name, "", 100, num("zoom", 1, 8, 1), num("fx", 0, 100, 50), num("fy", 0, 100, 50), f"Put your picture on {names[panel]}. You can tell me to change its color or zoom.")
@route("/api/books/{i}/texture", methods=("POST",))
def texture(request, body, i):
    kind = body.get("kind") if body.get("kind") in ("leather", "linen") else "leather"; panel = body.get("panel") if body.get("panel") in ("front", "back", "full") else "full"
    b = load(i); g = engine.geometry(b); r = engine.region(g, panel); name = uuid.uuid4().hex[:12] + ".jpg"
    with LOCK: engine.make_texture(kind, (r[2] - r[0]) / engine.IN, (r[3] - r[1]) / engine.IN, str(_imgs(i) / name))
    tint = b["cover"]["bg"] if b["cover"]["bg"].lower() != "#ffffff" else "#6B1A12"
    names = {"front": "the front cover", "back": "the back cover", "full": "the whole cover"}
    return _add_pic(i, panel, name, tint, 100, 1, 50, 50, f"Added a {kind} texture to {names[panel]}, colored {tint}. Tell me a different color or say if you want it lighter or darker.")
@route("/api/books/{i}/undo", methods=("POST",))
def undo(request, body, i):
    h = BOOKS / i / "history"; fs = sorted(h.glob("*.json")) if h.exists() else []
    if not fs: return {"book": load(i), "reply": "Nothing to undo."}
    b = load(i); old = json.loads(fs[-1].read_text()); fs[-1].unlink(); old["chat"] = b["chat"] + [{"role": "assistant", "text": "Undone. Back to how it was before your last change.", "changes": []}]
    old = engine.clean(old); save(i, old); return {"book": old, "reply": "Undone."}
@route("/api/meta", methods=("GET",))
def meta(request, body): return {"ai": bool(sets().get("openai_key") or os.environ.get("OPENAI_API_KEY")), "greeting": GREETING, "spec": SPEC}
@route("/api/settings", methods=("POST",))
def set_settings(request, body):
    s = sets()
    if "openai_key" in body:
        k = str(body["openai_key"]).strip()
        if k and not re.fullmatch(r"[A-Za-z0-9_\-]{20,300}", k): raise HTTPException(400, "That does not look like a key")
        s["openai_key"] = k
    p = ROOT / "settings.json"; p.write_text(json.dumps(s)); os.chmod(p, 0o600); return {"ok": True, "ai": bool(s.get("openai_key"))}

app = Starlette(routes=ROUTES)
