"""Scan Amazon and Google search-bar suggestions for notebook keyword ideas. Writes memory/inbox/kdp-keywords.md (counts and ranks only)."""
import json, time, urllib.parse, urllib.request, os, collections, string
OUT = os.path.expanduser("~/starship/memory/inbox/kdp-keywords.md")
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}
def get(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=12) as r: return json.loads(r.read().decode("utf-8", "ignore"))
    except Exception as e: return None
def amazon(q, alias):
    d = get("https://completion.amazon.com/api/2017/suggestions?mid=ATVPDKIKX0DER&alias=%s&prefix=%s" % (alias, urllib.parse.quote(q)))
    try: return [s["value"] for s in d["suggestions"]]
    except Exception: return []
def google(q):
    d = get("https://suggestqueries.google.com/complete/search?client=firefox&q=" + urllib.parse.quote(q))
    try: return list(d[1])
    except Exception: return []
CORE = ["process operator", "plant operator", "chemical operator", "operator notebook", "refinery operator", "shift work notebook", "lab technician notebook", "laboratory notebook", "work notebook for men", "hardcover lined notebook", "numbered pages notebook", "journal for work notes"]
EXTRA = ["gifts for plant operators", "gifts for chemical operators", "gift for refinery worker", "industrial worker gift", "blue collar gift", "oil and gas notebook", "oilfield notebook", "lab operator", "lab analyst notebook", "operator log book", "shift notes notebook", "work journal for men", "tradesman notebook", "hard cover notebook for work", "notebook with numbered pages", "notebook for plant workers", "operator journal"]
score = collections.defaultdict(lambda: {"amz": 0, "amz_all": 0, "goog": 0, "seeds": set()})
raw = []
def add(kind, seed, items):
    for i, v in enumerate(items):
        v = v.strip().lower()
        if v: score[v][kind] += 11 - (i + 1); score[v]["seeds"].add(seed)
for seed in CORE + EXTRA:
    qs = [seed] + ([seed + " " + c for c in string.ascii_lowercase] if seed in CORE else [])
    for q in qs:
        a = amazon(q, "stripbooks"); b = amazon(q, "aps"); g = google(q)
        add("amz", seed, a); add("amz_all", seed, b); add("goog", seed, g)
        if q == seed: raw.append((seed, a[:10], b[:10], g[:10]))
        time.sleep(0.25)
rows = sorted(score.items(), key=lambda kv: -(kv[1]["amz"] * 1.0 + kv[1]["amz_all"] * 1.0 + kv[1]["goog"] * 0.7))
L = ["# KDP keyword scan (Amazon and Google search-bar suggestions)", "", "Score = rank points (10 for first suggestion down to 1) added up across all seeds and letter expansions; Amazon books + Amazon all + 0.7 x Google. Bigger = suggested more often and higher = people type it more. Not exact volumes.", ""]
L.append("## Raw suggestions per seed (Amazon books | Amazon all | Google)")
for seed, a, b, g in raw: L.append("- **%s**\n  - books: %s\n  - all: %s\n  - google: %s" % (seed, "; ".join(a), "; ".join(b), "; ".join(g)))
L += ["", "## Top phrases by score (relevance still to be judged by Claude)", "", "| phrase | amz books | amz all | google | seeds |", "|---|---|---|---|---|"]
for v, s in rows[:150]: L.append("| %s | %d | %d | %d | %d |" % (v, s["amz"], s["amz_all"], s["goog"], len(s["seeds"])))
open(OUT, "w").write("\n".join(L) + "\n")
print("phrases:", len(rows), "| wrote", OUT, os.path.getsize(OUT), "bytes")
print("amazon books suggestions seen:", sum(1 for v in score.values() if v["amz"]), "| google:", sum(1 for v in score.values() if v["goog"]))
