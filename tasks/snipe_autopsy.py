#!/usr/bin/env python3
"""$1K-Snipe report + loss autopsy. Reads ~/market-data/snipe_log.jsonl and snipe.json (written by markets/sniper.py). Writes memory/inbox/snipe-autopsy.md (numbers only).
Every LOST, MISSED and SKIP round gets a line with the facts needed to decide what would have prevented it."""
import json, os, time
HOME = os.path.expanduser("~"); D = HOME + "/market-data"; OUT = HOME + "/starship/memory/inbox/snipe-autopsy.md"
def jl(p):
    try:
        for l in open(p):
            try: yield json.loads(l)
            except ValueError: pass
    except OSError: return
try: s = json.load(open(D + "/snipe.json"))
except Exception: s = {}
log = list(jl(D + "/snipe_log.jsonl"))
L = ["# $1K-Snipe report (auto)", ""]
if s:
    L.append("- Wallet $%.2f (started $%.0f). Rounds %d: bought %d (won %d, lost %d), skipped %d, missed %d. Profit $%.2f on $%.2f staked. Busts %d." % (s.get("bal", 0), s.get("start", 0), s.get("rounds", 0), s.get("bets", 0), s.get("wins", 0), s.get("losses", 0), s.get("skips", 0), s.get("misses", 0), s.get("pnl", 0), s.get("staked", 0), s.get("busts", 0)))
else: L.append("- No sniper data yet.")
by = {}
for r in log:
    if r.get("ticker"): by.setdefault(r["ticker"], []).append(r)
bought = {k: [x for x in v if x["result"] == "BOUGHT"] for k, v in by.items()}
fl = [b.get("filled_of_wallet", 1) for v in bought.values() for b in v]
ms = [b.get("book_ms", 0) for v in bought.values() for b in v]
lf = [b.get("left_at_book", 0) for v in bought.values() for b in v]
if fl: L.append("- Average share of the wallet that actually filled: %.0f%%. Seconds left when the book came back: avg %.2f (min %.2f, max %.2f). Kalshi answer time avg %d ms." % (100 * sum(fl) / len(fl), sum(lf) / len(lf), min(lf), max(lf), sum(ms) / len(ms)))
L += ["", "## Problems (lost / missed / skipped), newest last", ""]
bad = [r for r in log if r["result"] in ("LOST", "MISSED", "SKIP", "UNSETTLED", "ERROR")][-25:]
if not bad: L.append("None yet.")
for r in bad:
    tk = r.get("ticker", "?"); b = (bought.get(tk) or [None])[0]
    extra = ""
    if r["result"] == "LOST" and b: extra = " | bought %d %s at avg %.3f with %.2f s left, BTC %s vs target %s, filled %.0f%% of wallet" % (b["c"], b["side"], b["avg_px"], b["left_at_book"], b.get("px"), b.get("strike"), 100 * b["filled_of_wallet"])
    L.append("- %s %s %s: %s%s" % (time.strftime("%m-%d %H:%M:%S", time.localtime(r.get("t", 0))), tk, r["result"], r.get("why", "") or ("pnl $%s" % r.get("pnl")), extra))
os.makedirs(os.path.dirname(OUT), exist_ok=True); open(OUT, "w").write("\n".join(L) + "\n")
