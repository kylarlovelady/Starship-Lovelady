#!/usr/bin/env python3
"""READ-ONLY. Catalogue every Kalshi 15-minute crypto series and measure which are more PREDICTABLE than BTC, from Kalshi's own history (settled rounds + 1-minute candles).
Places no orders. Reuses the parsing in backfill.py. Polite: ~8 requests per second, time budget, partial output after every series.
For each Up/Down series (BTC, ETH, SOL, XRP, DOGE, BNB, ...): rounds, volume per round, spread at 5 and 2 minutes before the close, and at 7/5/3/2 minutes before the close
  - favourite-right rate: how often the side the market favoured (mid above 50c) really won. Higher EARLIER = the round is decided earlier = more predictable.
  - Brier score of the market's mid vs the outcome (0 = perfect, 0.25 = coin flip): lower = more predictable.
  - the market's own calibration at 5 minutes out (price bucket vs how often YES won).
  - memory in the results: P(UP | previous round UP) vs P(UP | previous round DOWN).
  - lead/lag: does BTC's price 5 minutes out tell us something about this coin's outcome that the coin's own price does not?
Multi-outcome series (Coin Race, Crypto Comparison) are listed but not analysed.
Run: python3 series_catalog.py [days=3] [budget_minutes=40]. Output: ~/starship/memory/inbox/market-catalog.md"""
import collections, json, math, os, statistics, sys, time, urllib.error
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import backfill as B
BASE = B.BASE
OUT = os.environ.get("OUTF", os.path.expanduser("~/starship/memory/inbox/market-catalog.md"))
CHECK = (7, 5, 3, 2)            # minutes before the close
SKIP = ("CRYPTOLEAD", "CRYPTOCOMP")


def epoch(s):
    return B._epoch(s)


def list_series():
    d = B._get(BASE + "/series?category=Crypto")
    out = []
    for x in d.get("series", []):
        t = x.get("ticker", "")
        if t.endswith("15M"):
            out.append(x)
    out.sort(key=lambda x: (x["ticker"] != "KXBTC15M", x["ticker"]))
    return out


def open_market(series):
    try:
        d = B._get(BASE + "/markets?series_ticker=%s&status=open&limit=1" % series)
        ms = d.get("markets", [])
        return ms[0] if ms else None
    except Exception:
        return None


def settled(series, days, cap):
    cutoff = int(time.time() - days * 86400)
    out, cur = [], None
    while len(out) < cap * 3:
        d = B._get(BASE + "/markets?series_ticker=%s&status=settled&limit=1000&min_close_ts=%d" % (series, cutoff) + ("&cursor=" + cur if cur else ""))
        for m in d.get("markets", []):
            if m.get("result") in ("yes", "no"):
                try:
                    out.append((epoch(m["close_time"]), m["ticker"], 1 if m["result"] == "yes" else 0, m.get("floor_strike") or m.get("cap_strike")))
                except Exception:
                    pass
        cur = d.get("cursor")
        if not cur or not d.get("markets"):
            break
        time.sleep(0.12)
    out.sort(reverse=True)
    return out[:cap]


def candles(series, tk, close):
    for path in ("/series/%s/markets/%s/candlesticks" % (series, tk), "/historical/markets/%s/candlesticks" % tk):
        try:
            d = B._get(BASE + path + "?start_ts=%d&end_ts=%d&period_interval=1" % (close - 900 - 60, close + 60))
            rows = [x for x in (B.parse_candle(c) for c in d.get("candlesticks", [])) if x]
            if rows:
                return rows
        except Exception:
            pass
    return []


def mid_at(rows, close, mins):
    """mid, spread and minute volume of the last candle that ended at or before close - mins*60 (within 90 s)"""
    tgt = close - mins * 60
    best = None
    for r in rows:
        if r[0] <= tgt and tgt - r[0] <= 90:
            best = r
    return ((best[1] + best[2]) / 2.0, best[2] - best[1]) if best else None


def analyse(rounds):
    """rounds: [(close, result, rows)] -> dict of metrics"""
    m = {"n": len(rounds)}
    vols = [sum(r[4] for r in rows) for c, res, rows in rounds if rows]
    m["vol"] = statistics.median(vols) if vols else 0
    for k in CHECK:
        pts = []
        for c, res, rows in rounds:
            x = mid_at(rows, c, k)
            if x:
                pts.append((x[0], res, x[1]))
        m[k] = pts
    m["up"] = sum(r[1] for r in rounds) / len(rounds) if rounds else None
    seq = [r[1] for r in sorted(rounds, key=lambda r: r[0])]
    a = [(seq[i - 1], seq[i]) for i in range(1, len(seq))]
    up_after_up = [y for x, y in a if x == 1]; up_after_dn = [y for x, y in a if x == 0]
    m["mem"] = (len(up_after_up), sum(up_after_up) / len(up_after_up) if up_after_up else None, len(up_after_dn), sum(up_after_dn) / len(up_after_dn) if up_after_dn else None)
    return m


def fav_right(pts):
    v = [(1 if (mid > 0.5) == (res == 1) else 0) for mid, res, sp in pts if abs(mid - 0.5) > 0.02]
    return (len(v), sum(v) / len(v)) if v else (0, None)


def brier(pts):
    return sum((mid - res) ** 2 for mid, res, sp in pts) / len(pts) if pts else None


def fmt(x, f="%.2f"):
    return "-" if x is None else f % x


def main():
    days = float(sys.argv[1]) if len(sys.argv) > 1 else 3
    budget = float(sys.argv[2]) * 60 if len(sys.argv) > 2 else 2400
    t_end = time.time() + budget
    ser = list_series()
    L = ["# Kalshi 15-minute crypto series: catalogue and predictability (last %g days)" % days, "", "Generated %s. Read-only; from Kalshi's settled rounds and 1-minute candles." % time.strftime("%Y-%m-%d %H:%M"), "",
         "## Catalogue (what exists right now)", "", "| series | title | open round volume | bid / ask now | strike | resolves on |", "|---|---|---|---|---|---|"]
    cat = {}
    for s in ser:
        t = s["ticker"]; mk = open_market(t); time.sleep(0.12)
        src = ", ".join(x.get("name", "") for x in (s.get("settlement_sources") or []))[:40]
        cat[t] = mk
        L.append("| %s | %s | %s | %s / %s | %s | %s |" % (t, (s.get("title") or "")[:34], mk.get("volume_fp") if mk else "-", mk.get("yes_bid_dollars") if mk else "-", mk.get("yes_ask_dollars") if mk else "-",
                 (mk.get("floor_strike") or mk.get("cap_strike") or "-") if mk else "-", src or "-"))
    first = next((cat[t] for t in cat if cat[t] and "BTC" in t), None)
    if first and first.get("rules_primary"):
        L += ["", "Rule text on a BTC round (Kalshi): " + first["rules_primary"][:400].replace("\n", " "), ""]
    L += ["Multi-outcome series (%s) are listed but not analysed here." % ", ".join(s["ticker"] for s in ser if any(k in s["ticker"] for k in SKIP)), ""]
    open(OUT, "w").write("\n".join(L) + "\n")
    per = {}; btc = {}
    for s in ser:
        t = s["ticker"]
        if any(k in t for k in SKIP):
            continue
        if time.time() > t_end:
            L.append("(out of time before %s)" % t); break
        try:
            st = settled(t, days, 290)
        except Exception as e:
            L.append("(%s: could not list settled rounds: %s)" % (t, str(e)[:60])); continue
        rr = []
        for close, tk, res, strike in st:
            if time.time() > t_end:
                break
            rows = candles(t, tk, close); time.sleep(0.12)
            if rows:
                rr.append((close, res, rows))
        per[t] = analyse(rr)
        per[t]["rounds"] = rr
        if t == "KXBTC15M":
            btc = {c: mid_at(rows, c, 5) for c, res, rows in rr}
        print("%s: %d rounds" % (t, len(rr)), flush=True)
    # ---------------- results ----------------
    L += ["## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)", "",
          "| series | rounds | median volume per round | UP share | spread at 5 min | spread at 2 min | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for t, m in per.items():
        sp5 = statistics.median([x[2] for x in m[5]]) if m[5] else None; sp2 = statistics.median([x[2] for x in m[2]]) if m[2] else None
        L.append("| %s | %d | %.0f | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (t, m["n"], m["vol"], fmt(m["up"] * 100 if m["up"] is not None else None, "%.0f%%"),
                 fmt(sp5 * 100 if sp5 is not None else None, "%.1fc"), fmt(sp2 * 100 if sp2 is not None else None, "%.1fc"),
                 *[("%s (%d)" % (fmt(fav_right(m[k])[1] * 100 if fav_right(m[k])[1] is not None else None, "%.0f%%"), fav_right(m[k])[0])) for k in CHECK], fmt(brier(m[5]), "%.3f"), fmt(brier(m[3]), "%.3f")))
    L += ["", "## Memory: does the previous round's result tell us anything? (P(UP) after an UP round vs after a DOWN round)", "", "| series | after UP (n) | after DOWN (n) |", "|---|---|---|"]
    for t, m in per.items():
        a, pa, b, pb = m["mem"]
        L.append("| %s | %s (%d) | %s (%d) |" % (t, fmt(pa * 100 if pa is not None else None, "%.0f%%"), a, fmt(pb * 100 if pb is not None else None, "%.0f%%"), b))
    L += ["", "## Calibration at 5 minutes out (did the favourite win as often as its price said?)", "", "| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |", "|---|---|---|---|---|---|"]
    for t, m in per.items():
        bk = collections.defaultdict(list)
        for mid, res, sp in m[5]:
            bk[min(int(mid * 5), 4)].append((mid, res))
        for k in sorted(bk):
            v = bk[k]
            if len(v) >= 8:
                w = sum(x[1] for x in v) / len(v); am = sum(x[0] for x in v) / len(v)
                L.append("| %s | %d-%dc | %d | %.0f%% | %.0fc | %+.0fc |" % (t, k * 20, k * 20 + 20, len(v), 100 * w, 100 * am, 100 * (w - am)))
    # lead/lag: BTC's mid 5 minutes out vs the other coin's outcome beyond its own price
    L += ["", "## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (rounds where the coin's own mid was 20-80c)", "",
          "| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) |", "|---|---|---|---|"]
    for t, m in per.items():
        if t == "KXBTC15M" or not btc:
            continue
        hi, lo = [], []
        for c, res, rows in m["rounds"]:
            x = mid_at(rows, c, 5); b = None
            for bc in (c, c + 1, c - 1):
                if bc in btc and btc[bc]:
                    b = btc[bc][0]; break
            if x is None or b is None or not (0.2 <= x[0] <= 0.8):
                continue
            (hi if b >= 0.7 else lo if b <= 0.3 else []).append(res - x[0])
        L.append("| %s | %d | %s (%d) | %s (%d) |" % (t, len(hi) + len(lo), fmt(100 * sum(hi) / len(hi) if hi else None, "%+.0fc"), len(hi), fmt(100 * sum(lo) / len(lo) if lo else None, "%+.0fc"), len(lo)))
    L += ["", "## How to read this", "",
          "- 'More predictable' has two meanings: (1) the round is decided earlier (high favourite-right rate and low Brier early), which is good for a safe-late-bet style but the market already prices it; (2) the market mis-prices it (calibration gap, memory, lead/lag), which is the only thing that makes money.",
          "- A thin market (low volume) may look predictable only because its quotes are wide and stale, and a $1,000 bet would move it. Volume and spread are shown for that reason.",
          "- About 290 rounds per series: gaps under about 10c per bucket, or differences of a few percent, are noise. Anything that looks good gets the same older-half / newer-half and bootstrap test as the longshot idea before it is believed.",
          "- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on."]
    open(OUT, "w").write("\n".join(L) + "\n")
    print("done", OUT)


if __name__ == "__main__":
    main()
