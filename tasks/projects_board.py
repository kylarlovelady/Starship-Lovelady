#!/usr/bin/env python3
"""Projects board for the Starship page (Kylar 2026-11-05 23:35: projects first; NOT the truck or the buy list).
Reads the tracker table in memory/projects.md, adds live numbers (Kalshi $1K-Snipe wallet from ~/market-data/snipe.json), and writes a 'projects' list into ~/starship/hub-extra.json
so the Mission board on the Starship page shows them. Rows: name, text, colour (g green / y yellow / b blue-grey). No keys, no transcripts. Never raises."""
import json, os, re
H = os.path.expanduser("~"); R = os.environ.get("STARSHIP_DIR", os.path.join(H, "starship")); D = os.environ.get("MARKET_DIR", os.path.join(H, "market-data"))
SKIP = ("truck", "vehicle", "buy list", "buy-list")
def short(t, n=150):
    t = re.sub(r"`", "", t).strip(); t = re.split(r"(?<=[a-z0-9)])\. (?=[A-Z])", t)[0] if len(t) > n else t
    return t if len(t) <= n else t[: n - 1].rstrip() + "..."
def main():
    rows = []
    try: lines = open(os.path.join(R, "memory", "projects.md"), encoding="utf-8").read().splitlines()
    except OSError: lines = []
    for l in lines:
        if not l.startswith("|") or l.startswith("|---") or l.startswith("| Project"): continue
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) < 3 or any(w in c[0].lower() for w in SKIP): continue
        st = c[1].lower(); col = "g" if st.startswith(("done", "built")) else ("y" if "progress" in st or "paused" in st or "waiting" in st else "b")
        rows.append({"name": c[0][:60], "text": "%s. Next: %s" % (c[1], short(c[2])), "color": col})
    try:
        s = json.load(open(os.path.join(D, "snipe.json")))
        for r in rows:
            if r["name"].startswith("Kalshi"):
                r["text"] = "$1K-Snipe practice wallet $%.2f (start $%.0f): %d rounds, %d bets, %d won, %d lost, %d skipped. Live trading OFF. Next: let the z-rule collect rounds and investigate any loss." % (s.get("bal", 0), s.get("start", 0), s.get("rounds", 0), s.get("bets", 0), s.get("wins", 0), s.get("losses", 0), s.get("skips", 0))
                r["color"] = "g" if s.get("pnl", 0) >= 0 else "y"
    except Exception: pass
    p = os.path.join(R, "hub-extra.json")
    try: x = json.load(open(p))
    except Exception: x = {}
    x["projects"] = rows[:14]
    json.dump(x, open(p + ".tmp", "w")); os.replace(p + ".tmp", p)
    return rows
if __name__ == "__main__":
    try:
        for r in main(): print(r["color"], r["name"], "|", r["text"][:120])
    except Exception as e: print("projects_board failed:", e)
