#!/usr/bin/env python3
"""REGIME DAYS (read-only, practice money): labels each past day by what Bitcoin did (calm / trending / wild) plus how much alarming news was logged,
then shows how each strategy did on each kind of day. Tests Kylar's idea: use different strategies on different kinds of days.
  python3 regime_days.py"""
import json, os, sys, time, statistics as st
from collections import defaultdict
D = os.environ.get("MARKET_DIR", os.path.join(os.path.expanduser("~"), "market-data"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wallet_curve import outcomes
from forward_review import rounds_for
NAMES = ["v_hold_s250", "v_hold_s250_cheap100", "v_hold_s250_agree", "v_hold_s100", "hold", "v_edge10_s100", "v_hold_s500"]
day = lambda t: time.strftime("%Y-%m-%d", time.localtime(t))

def btc_days():
    px = {}
    for ln in open(os.path.join(D, "history", "btc1m.jsonl")):
        try:
            for t, c in json.loads(ln)["r"]: px[t] = c
        except Exception: pass
    by = defaultdict(list)
    for t in sorted(px): by[day(t)].append(px[t])
    out = {}
    for d, v in by.items():
        if len(v) < 600: continue                          # need most of the day
        o, c, hi, lo = v[0], v[-1], max(v), min(v)
        rets = [(v[i] - v[i - 1]) / v[i - 1] for i in range(1, len(v))]
        out[d] = {"move": 100 * (c - o) / o, "range": 100 * (hi - lo) / o, "vol": 100 * st.pstdev(rets) * 60}   # vol = per-hour %
    return out

def news_days():
    out = defaultdict(lambda: {"n": 0, "shock": 0, "bad": 0})
    try:
        for ln in open(os.path.join(D, "news.jsonl")):
            try: r = json.loads(ln)
            except Exception: continue
            x = out[day(r.get("pub") or r["seen"])]; x["n"] += 1; x["bad"] += r["score"] < 0; x["shock"] += bool({"outage", "cyber", "bank", "war"} & set(r["tags"]))
    except OSError: pass
    return out

def label(b):
    if b["range"] >= 4.0 or b["vol"] >= 0.45: return "wild"
    if b["range"] >= 2.2 and abs(b["move"]) >= 0.5 * b["range"]: return "trending"
    return "calm"

def main():
    B = btc_days(); N = news_days(); R = rounds_for(outcomes(), set(NAMES))
    print("REGIME DAYS (pretend money, fees in). Run %s" % time.strftime("%a %d %H:%M"))
    print("label rule: wild = day range 4%+ or hourly vol 0.45%+; trending = range 2.2%+ and mostly one direction; else calm\n")
    print("%-11s %-9s %7s %7s %6s %9s   news(n/bad/shock)" % ("day", "label", "move%", "range%", "vol/h", "s250 pnl"))
    lab = {}
    for d in sorted(B):
        b = B[d]; lab[d] = label(b); n = N.get(d, {"n": 0, "bad": 0, "shock": 0})
        s = sum(r["pnl"] for r in R.get("v_hold_s250", {}).values() if day(r["t"]) == d)
        print("%-11s %-9s %+7.2f %7.2f %6.2f %+9.0f   %d/%d/%d" % (d, lab[d], b["move"], b["range"], b["vol"], s, n["n"], n["bad"], n["shock"]))
    print("\nSTRATEGY BY KIND OF DAY: total profit (rounds) | profit per round")
    for kind in ("calm", "trending", "wild"):
        days = [d for d in lab if lab[d] == kind]
        print(" %s (%d days)" % (kind.upper(), len(days)))
        for n in NAMES:
            rs = [r for r in R.get(n, {}).values() if day(r["t"]) in days]
            if rs: print("   %-22s %+9.0f (%4d) | %+6.2f per round" % (n, sum(r["pnl"] for r in rs), len(rs), sum(r["pnl"] for r in rs) / len(rs)))
    print("\n(few days per kind means this is a first look only; judge by unseen days.)")
if __name__ == "__main__": main()
