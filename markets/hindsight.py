"""Hindsight memory and pattern learning.
After every finished round the agent replays its own per-second recording and finds, in hindsight, the best buy and the best sell on each side
(the most it could possibly have made after fees). For those two moments it stores a snapshot of everything it could see: the model's odds,
the combined signal score, how far into the round it was, the price. That memory (hindsight.jsonl) grows every round.
Then it looks for patterns: which conditions (time in the round, model edge over the price, signal agreement) went with entries that made money
when managed by the take-profit rule, and which went with entries that lost. Hindsight always looks easy, so a pattern only counts if it also holds
on LATER rounds it was not trained on (walk-forward test), after fees:
  bad pattern  = lost money in training AND in the test rounds -> the agent refuses to buy in that state (live and practice)
  good pattern = made money in training AND in the test rounds -> listed, not used to size bets until enough rounds confirm it.
Writes hindsight.jsonl, patterns.json."""
import json, math, os, time

import exit_learn as X

MIN_ROUNDS_TOTAL = 40            # rounds needed before any pattern can be judged
MIN_BUCKET_ROUNDS = 12           # distinct rounds a bucket needs in both train and test
BAD_TRAIN, BAD_TEST = -0.02, -0.005
GOOD_TRAIN, GOOD_TEST = 0.01, 0.003


def fee(p):
    return 0.07 * p * (1 - p)


def _snap(r):
    return {"p_model": r.get("p_model"), "score": r.get("score"), "sig": r.get("sig")}


def _rows(d, days=4):
    """{ticker: [ (t, yes_bid, yes_ask, left, snapshot) ... ]} from the per-second recording, book prices only."""
    import glob
    out = {}
    for p in sorted(glob.glob(os.path.join(d, "ticks-*.jsonl*")))[-days:]:
        for r in X._lines(p):
            tk = (r.get("k") or {}).get("ticker")
            b = X._book(r)
            if tk and b and r.get("t") and r.get("left") is not None:
                out.setdefault(tk, []).append((r["t"], b[0], b[1], r["left"], _snap(r)))
    return out


def best_trade(rows, side):
    """Best buy then sell in hindsight on one side: (profit, i_buy, i_sell). Sell value is net of fee, buy cost includes fee."""
    cost = [((a if side == "UP" else 1 - b)) for _, b, a, _, _ in rows]
    sell = [((b - fee(b)) if side == "UP" else ((1 - a) - fee(1 - a))) for _, b, a, _, _ in rows]
    best = (-9.0, 0, 0)
    min_i, min_c = 0, 9.0
    for j in range(len(rows)):
        c_j = cost[j] + fee(cost[j])
        if 0.15 <= cost[j] <= 0.80 and c_j < min_c:
            min_c, min_i = c_j, j
        if min_c < 9.0 and sell[j] - min_c > best[0]:
            best = (sell[j] - min_c, min_i, j)
    return best


def build_memory(d):
    """One line per finished round, appended once, with the hindsight-best trade and the signal snapshot at both moments."""
    res = X.outcomes(d)
    rows = _rows(d)
    path = os.path.join(d, "hindsight.jsonl")
    have = set()
    try:
        for ln in open(path):
            try:
                have.add(json.loads(ln)["ticker"])
            except (ValueError, KeyError):
                pass
    except OSError:
        pass
    n = 0
    with open(path, "a") as f:
        for tk, rs in rows.items():
            if tk in have or tk not in res or len(rs) < 600:
                continue
            rs = sorted(rs, key=lambda x: x[0])[::2]
            up = res[tk] == "UP"
            best = None
            for side in ("UP", "DOWN"):
                pr, i, j = best_trade(rs, side)
                won = up if side == "UP" else not up
                px = rs[i][2] if side == "UP" else 1 - rs[i][1]
                hold = (1.0 if won else 0.0) - (px + fee(px))
                if best is None or pr > best["profit"]:
                    best = {"side": side, "profit": round(pr, 4), "hold": round(hold, 4), "entry": {"t": rs[i][0], "px": round(px, 3), "left": rs[i][3], **rs[i][4]},
                            "exit": {"t": rs[j][0], "left": rs[j][3], **rs[j][4]}}
            f.write(json.dumps(dict(best, ticker=tk, outcome=res[tk], t0=rs[0][0])) + "\n")
            n += 1
    return n


def buckets(elapsed, edge, score_aligned):
    t = "t%d" % min(4, int(max(0, elapsed) // 180))
    e = "e0" if edge < 0 else "e1" if edge < 0.05 else "e2" if edge < 0.10 else "e3"
    s = "s0" if score_aligned < -10 else "s1" if score_aligned <= 10 else "s2"
    return {"time": t, "edge": e, "score": s}


def learn_patterns(d, now=None):
    now = now or time.time()
    res = X.outcomes(d)
    rows = _rows(d)
    rules = X.current(d)
    P, D = rules["peak"], rules["drop"]
    rounds = sorted([(rs[0][0], tk, sorted(rs, key=lambda x: x[0])[::2]) for tk, rs in rows.items() if tk in res and len(rs) > 600])
    out = {"updated": int(now), "rounds": len(rounds), "bad": [], "good": [], "note": None}
    if len(rounds) < MIN_ROUNDS_TOTAL:
        out["note"] = "only %d finished rounds with a full recording; patterns need %d" % (len(rounds), MIN_ROUNDS_TOTAL)
        _save(d, out)
        return out
    cut = int(len(rounds) * 0.7)
    stats = {}   # (feature, bucket) -> {"tr":[per-round means], "te":[...]}
    for idx, (t0, tk, rs) in enumerate(rounds):
        part = "tr" if idx < cut else "te"
        up = res[tk] == "UP"
        for side in ("UP", "DOWN"):
            vals = X._vals(rs, side)
            won = up if side == "UP" else not up
            hold_v = 1.0 if won else 0.0
            per = {}
            for i in range(len(rs)):
                t, yb, ya, left, snap = rs[i]
                el = 900 - left
                if el < 30 or el > 780 or (el % 60) >= 2:
                    continue
                px = ya if side == "UP" else 1 - yb
                if not (0.15 <= px <= 0.80) or snap.get("p_model") is None or snap.get("score") is None:
                    continue
                cost = px + fee(px)
                v = X._sim_rule(vals, i, cost, P, D)
                result = (v if v is not None else hold_v) - cost
                pm = snap["p_model"] if side == "UP" else 1 - snap["p_model"]
                sc = snap["score"] * (1 if side == "UP" else -1)
                per.setdefault(("all", "all"), []).append(result)
                for k, b in buckets(el, pm - px - fee(px), sc).items():
                    per.setdefault((k, b), []).append(result)
            for key, lst in per.items():
                s = stats.setdefault(key, {"tr": [], "te": []})
                s[part].append(sum(lst) / len(lst))
    base = stats.get(("all", "all"))
    if not base or not base["tr"] or not base["te"]:
        _save(d, out)
        return out
    btr, bte = sum(base["tr"]) / len(base["tr"]), sum(base["te"]) / len(base["te"])
    out["baseline"] = {"train": round(btr, 4), "test": round(bte, 4)}      # what an average entry makes after fees; fees alone make this negative
    for (k, b), s in sorted(stats.items()):
        if k == "all" or len(s["tr"]) < MIN_BUCKET_ROUNDS or len(s["te"]) < MIN_BUCKET_ROUNDS:
            continue
        mtr, mte = sum(s["tr"]) / len(s["tr"]), sum(s["te"]) / len(s["te"])
        rec = {"feature": k, "bucket": b, "train": round(mtr, 4), "test": round(mte, 4), "n_train": len(s["tr"]), "n_test": len(s["te"])}
        # bad = clearly worse than an average entry in training AND in the later test rounds (judged against the baseline, not zero)
        if mtr - btr <= BAD_TRAIN and mte - bte <= BAD_TEST and mte < 0:
            out["bad"].append(rec)
        elif mtr >= GOOD_TRAIN and mte >= GOOD_TEST:
            out["good"].append(rec)
    _save(d, out)
    return out


def _save(d, obj):
    tmp = os.path.join(d, "patterns.json.tmp")
    try:
        with open(tmp, "w") as f:
            json.dump(obj, f)
        os.replace(tmp, os.path.join(d, "patterns.json"))
    except OSError:
        pass


def run(d):
    try:
        n = build_memory(d)
    except Exception:
        n = -1
    return n, learn_patterns(d)
