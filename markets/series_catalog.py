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
Accumulates: every settled round it has seen is cached in ~/market-data/history/series15m.jsonl (prices 10/7/5/3/2 minutes before the close), so each run only fetches NEW rounds and the sample keeps growing. Runs nightly (tasks/series_catalog_daily.sh install).
Run: python3 series_catalog.py [days=3] [budget_minutes=40]. Output: ~/starship/memory/inbox/market-catalog.md"""
import collections, json, math, os, statistics, sys, time, urllib.error
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import backfill as B
BASE = B.BASE
OUT = os.environ.get("OUTF", os.path.expanduser("~/starship/memory/inbox/market-catalog.md"))
CHECK = (7, 5, 3, 2)            # minutes before the close
STORE = (10, 7, 5, 3, 2)
CACHE = os.environ.get("CACHE", os.path.expanduser("~/market-data/history/series15m.jsonl"))
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


def load_cache():
    C = collections.defaultdict(dict)
    try:
        for ln in open(CACHE):
            try:
                r = json.loads(ln); C[r["s"]][r["tk"]] = r
            except (ValueError, KeyError):
                pass
    except OSError:
        pass
    return C


def pts_of(recs, k):
    return [(r["m"][str(k)][0], r["r"], r["m"][str(k)][1]) for r in recs if str(k) in r["m"]]


def pair_up(recs):
    """(previous result, this result) for rounds exactly 15 minutes apart"""
    by = {r["c"]: r["r"] for r in recs}
    return [(by[c - 900], by[c], c) for c in sorted(by) if (c - 900) in by]


def main():
    days = float(sys.argv[1]) if len(sys.argv) > 1 else 3
    budget = float(sys.argv[2]) * 60 if len(sys.argv) > 2 else 2400
    t_end = time.time() + budget
    ser = list_series()
    L = ["# Kalshi 15-minute crypto series: catalogue and predictability", "", "Generated %s. Read-only; from Kalshi's settled rounds and 1-minute candles, cached and growing (each run adds the new rounds)." % time.strftime("%Y-%m-%d %H:%M"), "",
         "## Catalogue (what exists right now; volume = contracts traded so far in the open round)", "", "| series | title | open round volume | bid / ask now | strike | resolves on |", "|---|---|---|---|---|---|"]
    cat = {}
    for s_ in ser:
        t = s_["ticker"]; mk = open_market(t); time.sleep(0.12)
        src = ", ".join(x.get("name", "") for x in (s_.get("settlement_sources") or []))[:40]
        cat[t] = mk
        L.append("| %s | %s | %s | %s / %s | %s | %s |" % (t, (s_.get("title") or "")[:34], mk.get("volume_fp") if mk else "-", mk.get("yes_bid_dollars") if mk else "-", mk.get("yes_ask_dollars") if mk else "-",
                 (mk.get("floor_strike") or mk.get("cap_strike") or "-") if mk else "-", src or "-"))
    first = next((cat[t] for t in cat if cat[t] and "BTC" in t), None)
    if first and first.get("rules_primary"):
        L += ["", "Rule text on a BTC round (Kalshi): " + first["rules_primary"][:420].replace("\n", " "), ""]
    L += ["Multi-outcome series (%s) are listed but not analysed here." % ", ".join(s_["ticker"] for s_ in ser if any(k in s_["ticker"] for k in SKIP)), ""]
    open(OUT, "w").write("\n".join(L) + "\n")
    C = load_cache(); added = collections.Counter()
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    with open(CACHE, "a") as cf:
        for s_ in ser:
            t = s_["ticker"]
            if any(k in t for k in SKIP) or time.time() > t_end:
                continue
            try:
                st = settled(t, days, 1500)
            except Exception as e:
                L.append("(%s: could not list settled rounds: %s)" % (t, str(e)[:60])); continue
            for close, tk, res, strike in st:
                if time.time() > t_end:
                    break
                if tk in C[t]:
                    continue
                rows = candles(t, tk, close); time.sleep(0.12)
                m = {}
                for k in STORE:
                    x = mid_at(rows, close, k)
                    if x:
                        m[str(k)] = [round(x[0], 4), round(x[1], 4)]
                rec = {"s": t, "tk": tk, "c": close, "r": res, "m": m}
                cf.write(json.dumps(rec) + "\n"); cf.flush(); C[t][tk] = rec; added[t] += 1
            print("%s: +%d new, %d total" % (t, added[t], len(C[t])), flush=True)
    per = {t: sorted([r for r in C[t].values() if r["m"]], key=lambda r: r["c"]) for t in C if C[t]}
    per = {t: v for t, v in per.items() if v}
    L += ["## Predictability (higher favourite-right EARLIER and lower Brier = decided earlier = more predictable)", "",
          "| series | rounds cached | span (days) | UP share | fav-right 7 min | 5 min | 3 min | 2 min | Brier 5 min | Brier 3 min | open round volume now |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    for t, v in per.items():
        span = (v[-1]["c"] - v[0]["c"]) / 86400.0
        row = [fav_right(pts_of(v, k)) for k in CHECK]
        L.append("| %s | %d | %.1f | %.0f%% | %s | %s | %s | %s | %s | %s | %s |" % (t, len(v), span, 100.0 * sum(r["r"] for r in v) / len(v),
                 *["%s (%d)" % (fmt(x[1] * 100 if x[1] is not None else None, "%.0f%%"), x[0]) for x in row], fmt(brier(pts_of(v, 5)), "%.3f"), fmt(brier(pts_of(v, 3)), "%.3f"), (cat.get(t) or {}).get("volume_fp") or "-"))
    L += ["", "## Memory: P(UP) after an UP round vs after a DOWN round (rounds exactly 15 minutes apart; older half / newer half in brackets)", "", "| series | after UP (n) | after DOWN (n) | older half: up / down | newer half: up / down |", "|---|---|---|---|---|"]
    for t, v in per.items():
        pr = pair_up(v)
        def rate(x, want): 
            q = [b for a, b, c in x if a == want]; return (sum(q) / len(q) if q else None, len(q))
        mid_c = sorted(c for a, b, c in pr)[len(pr) // 2] if pr else 0
        o = [x for x in pr if x[2] < mid_c]; n_ = [x for x in pr if x[2] >= mid_c]
        a1, a0 = rate(pr, 1), rate(pr, 0)
        f = lambda r: fmt(r[0] * 100 if r[0] is not None else None, "%.0f%%")
        L.append("| %s | %s (%d) | %s (%d) | %s / %s | %s / %s |" % (t, f(a1), a1[1], f(a0), a0[1], f(rate(o, 1)), f(rate(o, 0)), f(rate(n_, 1)), f(rate(n_, 0))))
    L += ["", "## Calibration at 5 minutes out (did the price mean what it said?)", "", "| series | price bucket (YES mid) | rounds | YES won | avg mid | gap |", "|---|---|---|---|---|---|"]
    for t, v in per.items():
        bk = collections.defaultdict(list)
        for mid, res, sp in pts_of(v, 5):
            bk[min(int(mid * 5), 4)].append((mid, res))
        for k in sorted(bk):
            q = bk[k]
            if len(q) >= 8:
                w = sum(x[1] for x in q) / len(q); am = sum(x[0] for x in q) / len(q)
                L.append("| %s | %d-%dc | %d | %.0f%% | %.0fc | %+.0fc |" % (t, k * 20, k * 20 + 20, len(q), 100 * w, 100 * am, 100 * (w - am)))
    btc = {r["c"]: r["m"]["5"][0] for r in per.get("KXBTC15M", []) if "5" in r["m"]}
    L += ["", "## Lead / lag: does BTC's 5-minute price tell us about this coin beyond the coin's own price? (own mid 20-80c; older / newer half in brackets)", "",
          "| series | rounds | outcome minus own mid when BTC mid >= 70c (n) | when BTC mid <= 30c (n) | older half: high / low | newer half: high / low |", "|---|---|---|---|---|---|"]
    for t, v in per.items():
        if t == "KXBTC15M" or not btc:
            continue
        rows_ = []
        for r in v:
            if "5" not in r["m"] or r["c"] not in btc or not (0.2 <= r["m"]["5"][0] <= 0.8):
                continue
            b = btc[r["c"]]
            rows_.append((r["c"], "hi" if b >= 0.7 else "lo" if b <= 0.3 else "mid", r["r"] - r["m"]["5"][0]))
        if not rows_:
            continue
        cm = sorted(x[0] for x in rows_)[len(rows_) // 2]
        def avg(q, tag):
            z = [x[2] for x in q if x[1] == tag]; return (sum(z) / len(z) if z else None, len(z))
        g = lambda a: fmt(a[0] * 100 if a[0] is not None else None, "%+.0fc")
        h, l_ = avg(rows_, "hi"), avg(rows_, "lo")
        ro = [x for x in rows_ if x[0] < cm]; rn = [x for x in rows_ if x[0] >= cm]
        L.append("| %s | %d | %s (%d) | %s (%d) | %s / %s | %s / %s |" % (t, len(rows_), g(h), h[1], g(l_), l_[1], g(avg(ro, "hi")), g(avg(ro, "lo")), g(avg(rn, "hi")), g(avg(rn, "lo"))))
    L += ["", "## How to read this", "",
          "- 'More predictable' has two meanings: (1) decided earlier (high favourite-right rate and low Brier early); the market already prices that, so it is not money by itself; (2) mis-priced (calibration gap, memory, lead/lag), which is the only thing that makes money.",
          "- All the coins move together with BTC, so ten series agreeing is NOT ten independent confirmations: the same market-wide moves show up in every one. Judge by the older-half / newer-half columns and by sample size.",
          "- Thin markets: compare the open-round volume column; a $1,000 bet would move the thin ones.",
          "- Gaps under about 10c per bucket, or a few percent in the memory table, are noise at these sizes. Anything that holds up gets the bootstrap and older/newer test before it is believed.",
          "- Practice only. Standing rule is BTC only for real trading; this study is data, not a change to what the agent bets on."]
    open(OUT, "w").write("\n".join(L) + "\n")
    print("done", OUT)


if __name__ == "__main__":
    main()
