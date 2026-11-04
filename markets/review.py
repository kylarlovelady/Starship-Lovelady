#!/usr/bin/env python3
"""TRADE REVIEW (read-only): what the agent actually did, round by round, against what hindsight says was possible, with the times of everything.
Uses the agent's own trade log and the second-by-second Kalshi book it recorded. Practice trades only. Money in dollars, prices in cents, fees included.
  python3 review.py [hours=24] [strategy=run]"""
import bisect, json, math, os, sys, time
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
D = os.environ.get("MARKET_DIR", os.path.join(os.path.expanduser("~"), "market-data"))


def fee1(p): return 0.07 * p * (1 - p)
def fee_total(c, p): return math.ceil(0.07 * c * p * (1 - p) * 100 - 1e-9) / 100.0
def hm(t): return time.strftime("%a %H:%M", time.localtime(t))


def main():
    hours = float(sys.argv[1]) if len(sys.argv) > 1 else 24
    who = sys.argv[2] if len(sys.argv) > 2 else "run"
    import replay
    use, cand, btc = replay.load_ticks(max(1, hours / 24.0 + 1))
    res = {r["ticker"]: r for r in use}
    cut = time.time() - hours * 3600
    ev = defaultdict(list)
    for l in open(os.path.join(D, "trades.jsonl")):
        try: r = json.loads(l)
        except ValueError: continue
        if r.get("live") or r.get("a") not in ("BUY", "SELL") or not r.get("c") or not r.get("px") or (r.get("t") or 0) < cut: continue
        ev[(r["s"], r.get("ticker"))].append(r)
    # ---- replay every (strategy, round) into dollars
    rounds = []
    for (s, tk), rs in ev.items():
        if tk not in res: continue
        R = res[tk]; rs.sort(key=lambda r: r["t"]); won = {"UP": R["result"] == "UP", "DOWN": R["result"] == "DOWN"}
        pos = {"UP": 0, "DOWN": 0}; cash = 0.0; stake = 0.0; buys = []; sells = []
        for r in rs:
            c, p, sd = int(r["c"]), float(r["px"]), r["side"]
            f = fee_total(c, p)
            if r["a"] == "BUY":
                cash -= c * p + f; stake += c * p; pos[sd] += c; buys.append((r["t"], sd, c, p))
            else:
                c = min(c, pos[sd]);
                if c <= 0: continue
                cash += c * p - fee_total(c, p); pos[sd] -= c
                hold_val = c * (1.0 if won[sd] else 0.0)
                sells.append({"t": r["t"], "side": sd, "c": c, "p": p, "net": c * p - fee_total(c, p), "hold": hold_val, "why": (r.get("why") or "")})
        end = sum(pos[sd] * (1.0 if won[sd] else 0.0) for sd in pos)
        pnl = cash + end
        rounds.append({"s": s, "tk": tk, "R": R, "pnl": pnl, "stake": stake, "buys": buys, "sells": sells, "end": end})
    if not rounds:
        print("No finished practice rounds with trades in the last %d hours that also have a full per-second recording." % hours); return
    print("TRADE REVIEW, last %d hours: %d (strategy, round) results from %d rounds with full recordings.\n" % (hours, len(rounds), len({r["tk"] for r in rounds})))
    # ---- scoreboard of every strategy
    by = defaultdict(lambda: [0, 0.0, 0, 0.0])
    for r in rounds:
        a = by[r["s"]]; a[0] += 1; a[1] += r["pnl"]; a[2] += 1 if r["pnl"] > 0 else 0; a[3] += r["stake"]
    print("EVERY STRATEGY (pretend money): rounds | profit | win%% | profit per $ staked")
    for k, a in sorted(by.items(), key=lambda kv: -kv[1][1]):
        print("  %-14s %3d  %+9.2f  %3.0f%%  %+5.1f%%" % (k, a[0], a[1], 100.0 * a[2] / a[0], 100.0 * a[1] / a[3] if a[3] else 0))
    mine = [r for r in rounds if r["s"] == who and r["buys"]]
    if len(mine) < 3:
        print("\nOnly %d rounds for '%s'. Not enough to review." % (len(mine), who)); return
    # ---- hindsight for each of my rounds
    def series(tk, side):
        c = cand[tk]; ts = [x[0] for x in c]
        a = [x[2] if side == "UP" else 1 - x[1] for x in c]; b = [x[1] if side == "UP" else 1 - x[2] for x in c]
        return ts, a, b
    tot_act = tot_best = tot_hold = 0.0; right = n = 0; right_stake = all_stake = 0.0
    et, bt = [], []; over = []; rows = []
    for r in mine:
        R = r["R"]; op = R["open"]; sd0 = r["buys"][0][1]; t0 = r["buys"][0][0]; p0 = r["buys"][0][3]
        rs = R["result"]; n += 1; all_stake += r["stake"]
        ok = sd0 == rs; right += ok
        right_stake += sum(c * p for t, s_, c, p in r["buys"] if s_ == rs)
        ts, a, b = series(r["tk"], rs)
        i0 = max(0, bisect.bisect_left(ts, op + 5))
        best_i = min(range(i0, len(ts) - 1), key=lambda i: a[i] + fee1(a[i]), default=None)
        if best_i is None: continue
        best_px = a[best_i]; best_t = ts[best_i] - op
        et.append(t0 - op); bt.append(best_t)
        if ok: over.append(100 * (p0 - best_px))
        # best possible: buy the right side at its cheapest and hold, per contract, vs what we earned per contract staked
        best_hold = (1.0 - best_px - fee1(best_px))
        # best swing: any side, buy low sell high later (after fees)
        bs = 0.0; bsi = None
        for side in ("UP", "DOWN"):
            tt, aa, bb = series(r["tk"], side); mn = None
            for i in range(i0, len(tt)):
                if mn is not None:
                    g = (bb[i] - fee1(bb[i])) - mn[0]
                    if g > bs: bs = g; bsi = (side, mn[1] - op, tt[i] - op)
                v = aa[i] + fee1(aa[i])
                if mn is None or v < mn[0]: mn = (v, tt[i])
        cpc = r["pnl"] / (r["stake"] / max(.01, p0)) if r["stake"] else 0.0
        rows.append({"r": r, "ok": ok, "best_hold": best_hold, "best_t": best_t, "best_px": best_px, "bs": bs, "bsi": bsi, "t0": t0 - op, "p0": p0, "sd0": sd0})
        tot_act += r["pnl"]
        tot_best += best_hold * (r["stake"] / max(.01, p0)); tot_hold += 0
    print("\n=== '%s': %d rounds. Total profit %+.2f ===" % (who, len(mine), sum(r["pnl"] for r in mine)))
    print("1) SIDE: first bet on the winning side in %d of %d rounds (%.0f%%). Money-weighted: %.0f%% of dollars staked were on the winning side (coin flip = 50%%)." % (right, n, 100.0 * right / n, 100.0 * right_stake / all_stake if all_stake else 0))
    if et:
        mid = lambda v: sorted(v)[len(v) // 2]
        print("2) TIMING: it makes its first bet a median %d:%02d into the round. The cheapest price on the winning side came a median %d:%02d in. Median paid %d cents above that cheapest point when it was on the right side." % (mid(et) // 60, mid(et) % 60, mid(bt) // 60, mid(bt) % 60, mid(over) if over else 0))
    b = defaultdict(lambda: [0, 0.0, 0])
    for x in rows:
        m = x["t0"] / 60.0; k = "0-1 min" if m < 1 else "1-3 min" if m < 3 else "3-6 min" if m < 6 else "6-10 min" if m < 10 else "10+ min"
        b[k][0] += 1; b[k][1] += x["r"]["pnl"]; b[k][2] += 1 if x["ok"] else 0
    print("   first bet time -> rounds, profit, side right:  " + "  |  ".join("%s: %d, %+.0f, %d right" % (k, v[0], v[1], v[2]) for k, v in sorted(b.items(), key=lambda kv: ("0" if kv[0][0] == "0" else kv[0][0]))))
    # exits: what each selling rule did vs just holding
    g = defaultdict(lambda: [0, 0.0])
    for r in mine:
        for s_ in r["sells"]:
            w = s_["why"]; k = "cut a loss" if w.startswith("Cutting") else "take-profit exit" if w.startswith("Take-profit") else "move slowed" if "move slowed" in w else "its own odds said sell" if w.startswith("Selling") else "other"
            g[k][0] += 1; g[k][1] += s_["net"] - s_["hold"]
    print("3) SELLING (money made or lost by selling versus just holding those contracts to the end):")
    for k, v in sorted(g.items(), key=lambda kv: kv[1][1]):
        print("   %-26s %3d sells  %+9.2f  %s" % (k, v[0], v[1], "selling HELPED" if v[1] > 0 else "selling HURT (holding would have been better)"))
    # stakes
    sb = defaultdict(lambda: [0, 0.0, 0])
    for r in mine:
        k = "under $25" if r["stake"] < 25 else "$25-100" if r["stake"] < 100 else "$100-250" if r["stake"] < 250 else "$250+"
        sb[k][0] += 1; sb[k][1] += r["pnl"]; sb[k][2] += 1 if r["pnl"] > 0 else 0
    print("4) BET SIZE -> rounds, profit, wins:  " + "  |  ".join("%s: %d, %+.0f, %d" % (k, v[0], v[1], v[2]) for k, v in sorted(sb.items())))
    hb = defaultdict(lambda: [0, 0.0])
    for r in mine:
        h = time.strftime("%H", time.localtime(r["R"]["open"])); hb[h][0] += 1; hb[h][1] += r["pnl"]
    print("5) HOUR OF DAY -> rounds, profit:  " + "  |  ".join("%sh: %d, %+.0f" % (h, v[0], v[1]) for h, v in sorted(hb.items())))
    # hindsight
    ev_ = sum(x["bs"] for x in rows) / len(rows)
    print("6) HINDSIGHT: buying the winning side at its cheapest moment and holding earns an average %d cents per contract after fees; the best swing (buy low, sell high, any side) averages %d cents per contract. It is not achievable (nobody knows the cheapest moment); it shows how much room there is." % (round(100 * sum(x["best_hold"] for x in rows) / len(rows)), round(100 * ev_)))
    print("\nWORST 5 ROUNDS (when, what it did, what was best):")
    for x in sorted(rows, key=lambda x: x["r"]["pnl"])[:5]:
        r = x["r"]; sd = "" if x["bsi"] is None else "best swing %s bought at %d:%02d sold at %d:%02d, +%dc/contract; " % (x["bsi"][0], x["bsi"][1] // 60, x["bsi"][1] % 60, x["bsi"][2] // 60, x["bsi"][2] % 60, round(100 * x["bs"]))
        print("  %s  %+.0f  bet %s at %d:%02d @%dc ($%d)%s; result %s. %s cheapest winning-side price %dc at %d:%02d" % (hm(r["R"]["open"]), r["pnl"], x["sd0"], x["t0"] // 60, x["t0"] % 60, round(100 * x["p0"]), r["stake"], "" if x["ok"] else " (WRONG SIDE)", r["R"]["result"], sd, round(100 * x["best_px"]), x["best_t"] // 60, x["best_t"] % 60))
    print("\nBEST 3 ROUNDS:")
    for x in sorted(rows, key=lambda x: -x["r"]["pnl"])[:3]:
        r = x["r"]; print("  %s  %+.0f  bet %s at %d:%02d @%dc ($%d); result %s" % (hm(r["R"]["open"]), r["pnl"], x["sd0"], x["t0"] // 60, x["t0"] % 60, round(100 * x["p0"]), r["stake"], r["R"]["result"]))
    json.dump({"made": int(time.time()), "hours": hours, "who": who, "rounds": len(mine), "profit": sum(r["pnl"] for r in mine), "side_right_pct": 100.0 * right / n}, open(os.path.join(D, "review.json"), "w"))


if __name__ == "__main__":
    main()
