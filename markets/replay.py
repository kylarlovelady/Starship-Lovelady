"""Replays old Kalshi BTC 15-minute rounds (from backfill.py) through the agent's strategies, in a private sandbox, to see what each
would have made after fees, when the best moments to buy and sell were, and how your own trades compare.
Nothing here touches the live agent, its wallets or Kalshi. Run it as its own program (never inside the collector).
Honest limits: the old history has one price per MINUTE and the replay only uses the last minute quote it would have known (no peeking ahead),
so it is too coarse for swing: swing is tested only on the agent's own second-by-second recordings. Strategies that need the order book, whale moves or news (signals, trend, flow, mood) cannot be replayed:
that old data does not exist. The replayed strategies are: swing (your strategy, at several aggression levels), distance, hold.
Usage: python3 replay.py [days=14] [aggression]   |   python3 replay.py --show"""
import bisect, json, math, os, shutil, sys, tempfile, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

HOME = os.path.expanduser("~")
DIR = os.environ.get("MARKET_DIR", os.path.join(HOME, "market-data"))
H = os.path.join(DIR, "history")


def fee(p):
    return 0.07 * p * (1 - p)


def load(days):
    rounds, cand = {}, {}
    cut = time.time() - days * 86400
    for ln in open(os.path.join(H, "rounds.jsonl")):
        r = json.loads(ln)
        if r["close"] >= cut and r.get("strike"):
            rounds[r["ticker"]] = r
    for ln in open(os.path.join(H, "candles.jsonl")):
        r = json.loads(ln)
        if r["ticker"] in rounds and len(r["c"]) >= 8:
            cand[r["ticker"]] = sorted(r["c"])
    bt = {}
    for ln in open(os.path.join(H, "btc1m.jsonl")):
        for t, c in json.loads(ln)["r"]:
            bt[t + 60] = c                                   # a Coinbase candle is labelled by its start; its close is a minute later
    ts = sorted(bt)
    use = sorted([r for r in rounds.values() if r["ticker"] in cand], key=lambda r: r["open"])
    return use, cand, ts, [bt[t] for t in ts]


class Series:
    """A price series where at(t) is the LAST value known at time t (never a value from the future)."""
    def __init__(self, ts, vs):
        self.ts, self.vs = ts, vs

    def at(self, t):
        i = bisect.bisect_right(self.ts, t)
        if i == 0 or t - self.ts[i - 1] > 120:
            return None
        return self.vs[i - 1]


def quote_at(c, t):
    """Up bid/ask known at time t: the last quote at or before t. None before the first one."""
    ts = [x[0] for x in c]
    i = bisect.bisect_right(ts, t)
    if i == 0 or t - c[i - 1][0] > 120:
        return None
    return c[i - 1][1], c[i - 1][2]


def load_ticks(days):
    """Rounds the agent recorded second by second (real order-book prices): the exact data, no filling in."""
    import calendar, glob
    import exit_learn as X
    res = X.outcomes(DIR)
    try:
        for ln in open(os.path.join(H, "rounds.jsonl")):
            r = json.loads(ln); res.setdefault(r["ticker"], r["result"])
    except OSError:
        pass
    cut = time.time() - days * 86400
    rows, meta, px = {}, {}, []
    for p in sorted(glob.glob(os.path.join(DIR, "ticks-*.jsonl*"))):
        last_keep = {}
        for r in X._lines(p):
            t = r.get("t")
            if not t or t < cut:
                continue
            if r.get("px"):
                if not px or t - px[-1][0] >= 1.0:
                    px.append((t, float(r["px"])))
            k = r.get("k") or {}
            tk, bk = k.get("ticker"), X._book(r)
            if not tk or not bk or bk[1] < bk[0]:
                continue
            if tk not in meta:
                try:
                    cl = calendar.timegm(time.strptime(k["close_time"][:19], "%Y-%m-%dT%H:%M:%S"))
                    meta[tk] = {"ticker": tk, "open": cl - 900, "close": cl, "strike": float(k["floor_strike"]), "result": res.get(tk)}
                except Exception:
                    continue
            if t - last_keep.get(tk, 0) >= 4.5:
                last_keep[tk] = t
                rows.setdefault(tk, []).append([t, bk[0], bk[1]])
    use, cand = [], {}
    for tk, m in meta.items():
        rs = rows.get(tk) or []
        if m["result"] and len(rs) >= 120 and rs[0][0] <= m["open"] + 120 and rs[-1][0] >= m["close"] - 120:
            use.append(m); cand[tk] = rs
    use.sort(key=lambda r: r["open"])
    return use, cand, Series([x[0] for x in px], [x[1] for x in px])


def run_one(label, pname, ag, use, cand, btc, cfg, ovr=None):
    import sim
    sim.SW_OVR = dict(ovr or {})
    D = tempfile.mkdtemp(prefix="replay_")
    C = {"min_bet": cfg.get("min_bet", 0.0), "max_trades": 6, "cap": cfg.get("cap", 25.0), "aggression": ag, "practice": pname}
    S, last_end, n = {}, None, 0
    RES = {r["ticker"]: r["result"] for r in use}
    rf = lambda t_: RES.get(t_)
    try:
        for r in use:
            tk, o, cl, strike = r["ticker"], r["open"], r["close"], float(r["strike"])
            if btc.at(o) is None or btc.at(cl - 10) is None:
                continue
            if last_end is None or o - last_end > 60 or "sim" not in S:           # a gap: rebuild the 11 minutes before the open
                tape = []
                for t in range(o - 660, o, 5):
                    p = btc.at(t)
                    if p is not None:
                        tape.append([float(t), p, 0.5])
                S.setdefault("sim", {"acc": {}, "win": None, "strike": None, "hours": {}, "mood": 0.0, "synth": False, "joined": False})["tape"] = tape
            # volatility from 30-second steps over the half hour before each moment
            g0 = o - 1800
            grid = [btc.at(g0 + 30 * k) for k in range(0, (cl - g0) // 30 + 2)]
            r2 = [0.0] + [((math.log(grid[k] / grid[k - 1]) ** 2) / 30.0 if grid[k] and grid[k - 1] else 0.0) for k in range(1, len(grid))]
            pre = [0.0]
            for x in r2:
                pre.append(pre[-1] + x)
            c = cand[tk]
            for now in range(o + 5, cl - 2, 5):
                price = btc.at(now)
                if price is None:
                    continue
                k = int((now - g0) // 30)
                lo = max(1, k - 59)
                pm = None
                if k - lo >= 10:
                    var = (pre[k + 1] - pre[lo]) / (k + 1 - lo)
                    sig = math.sqrt(var) * math.sqrt(max(1, cl - now))
                    if sig > 0:
                        pm = 0.5 * (1 + math.erf(math.log(price / strike) / sig / math.sqrt(2)))
                q = quote_at(c, now)
                if q is None:
                    continue
                b, a = q
                kal = {"ticker": tk, "yes_pct": (b + a) * 50.0, "yes_bid": b * 100, "yes_ask": a * 100, "close_ep": cl, "strike": strike, "qsrc": "book"}
                sim.step(S, float(now), o, 900, price, strike, pm, kal, {}, 0.0, True, D, C, {}, rf)
            sim.step(S, float(cl + 5), cl, 900, btc.at(cl) or 0.0, None, None, None, {}, 0.0, True, D, C, {}, rf)
            last_end = cl; n += 1
        sim.step(S, float(last_end + 905), last_end + 900, 900, 0.0, None, None, None, {}, 0.0, True, D, C, {}, rf)
        rows = []
        try:
            for ln in open(os.path.join(D, "sim_windows.jsonl")):
                x = json.loads(ln)
                if x["strat"] == pname:
                    rows.append(x)
        except OSError:
            pass
        return rows
    finally:
        shutil.rmtree(D, ignore_errors=True)


def summarize(rows):
    n = len(rows)
    if not n:
        return {"n": 0}
    pnl = sum(x["pnl"] for x in rows)
    hrs = {}
    for x in rows:
        h = hrs.setdefault(str(x["hour"]), {"n": 0, "pnl": 0.0}); h["n"] += 1; h["pnl"] = round(h["pnl"] + x["pnl"], 2)
    traded = [x for x in rows if x["trades"]]
    return {"n": n, "traded": len(traded), "pnl": round(pnl, 2), "per_round": round(pnl / n, 3), "win_pct": round(100 * sum(1 for x in rows if x["pnl"] > 0) / max(1, len(traded)), 1),
            "trades_per_round": round(sum(x["trades"] for x in rows) / n, 1), "by_hour": hrs}


def spots(use, cand):
    """Best buy and sell moments in hindsight (minute resolution), per side, after fees."""
    import hindsight
    out = {"UP": [], "DOWN": []}
    for r in use:
        c = cand[r["ticker"]]
        rows = [(x[0], x[1], x[2], r["close"] - x[0], None) for x in c if r["open"] <= x[0] <= r["close"]]
        if len(rows) < 8:
            continue
        for side in ("UP", "DOWN"):
            pr, i, j = hindsight.best_trade(rows, side)
            if pr > -9 and j > i:
                px = rows[i][2] if side == "UP" else 1 - rows[i][1]
                out[side].append((pr, (rows[i][0] - r["open"]) / 60.0, (rows[j][0] - r["open"]) / 60.0, px))
    res = {}
    for side, xs in out.items():
        if not xs:
            continue
        med = lambda v: sorted(v)[len(v) // 2]
        hb, hs = [0] * 15, [0] * 15
        for _, b, s, _ in xs:
            hb[min(14, max(0, int(b)))] += 1; hs[min(14, max(0, int(s)))] += 1
        res[side] = {"rounds": len(xs), "avg_best_profit": round(sum(x[0] for x in xs) / len(xs), 3), "median_buy_minute": round(med([x[1] for x in xs]), 1),
                     "median_sell_minute": round(med([x[2] for x in xs]), 1), "median_buy_price": round(med([x[3] for x in xs]), 2), "buy_minute_hist": hb, "sell_minute_hist": hs}
    return res


def yours(use, cand, per_round):
    """Compare your own settled trades with the history: what you made, what was available, and what each strategy would have made."""
    try:
        mine = json.load(open(os.path.join(DIR, "my_trades.json")))
    except (OSError, ValueError):
        return None
    byo = {r["open"]: r for r in use}
    rows = []
    for m in mine:
        r = byo.get(m["start"])
        if not r or m.get("first_side") not in ("yes", "no") or m.get("avg_buy_px") is None:
            continue
        c = cand[r["ticker"]]
        up = m["first_side"] == "yes"
        won = (r["result"] == "UP") == up
        cost = m["avg_buy_px"] + fee(m["avg_buy_px"])
        t0 = m["start"] + (m["first_buy_secs"] or 0)
        after = [x for x in c if x[0] >= t0]
        sale = [((x[1] if up else 1 - x[2]) - fee(x[1] if up else 1 - x[2])) for x in after]
        best = max(sale) - cost if sale else None
        rows.append({"pnl": m["pnl"], "early": bool(m["took_profit_early"]), "won_side": won, "best_exit_pc": best, "hold_pc": (1.0 if won else 0.0) - cost,
                     "buy_min": (m["first_buy_secs"] or 0) / 60.0, "px": m["avg_buy_px"], "staked": m["staked"], "start": m["start"]})
    if not rows:
        return None
    n = len(rows)
    lost_held = [x for x in rows if not x["early"] and x["pnl"] <= 0 and (x["best_exit_pc"] or -1) >= 0.05]
    sold_win = [x for x in rows if x["early"] and x["won_side"]]
    cmp = {}
    for lab, pr in per_round.items():
        got = [pr[x["start"]] for x in rows if x["start"] in pr]
        if got:
            cmp[lab] = {"rounds": len(got), "avg": round(sum(got) / len(got), 3), "win_pct": round(100 * sum(1 for g in got if g > 0) / len(got), 1)}
    return {"rounds": n, "your_total": round(sum(x["pnl"] for x in rows), 2), "your_avg": round(sum(x["pnl"] for x in rows) / n, 3),
            "your_win_pct": round(100 * sum(1 for x in rows if x["pnl"] > 0) / n, 1), "avg_stake": round(sum(x["staked"] for x in rows) / n, 2),
            "lost_while_a_profitable_exit_existed": {"rounds": len(lost_held), "avg_missed_per_contract": round(sum(x["best_exit_pc"] for x in lost_held) / max(1, len(lost_held)), 3)},
            "sold_early_but_that_side_won": {"rounds": len(sold_win)},
            "avg_best_exit_per_contract": round(sum(x["best_exit_pc"] for x in rows if x["best_exit_pc"] is not None) / n, 3),
            "avg_first_buy_minute": round(sum(x["buy_min"] for x in rows) / n, 1), "strategies_on_the_same_rounds": cmp}


def show(bt):
    if not bt:
        print("No replay results yet. Run: bash ~/starship/tasks/history.sh"); return
    print("REPLAY of %d old rounds (%s to %s), %s" % (bt["rounds"], time.strftime("%m-%d", time.localtime(bt["first"])), time.strftime("%m-%d", time.localtime(bt["last"])), bt["resolution"]))
    print("  strategy        rounds  traded   total $   per round   win%   trades/round")
    for lab, s in bt["strategies"].items():
        if s.get("n"):
            print("  %-14s %6d %7d %9.2f %10.3f %6.1f %8.1f" % (lab, s["n"], s["traded"], s["pnl"], s["per_round"], s["win_pct"], s["trades_per_round"]))
    if bt.get("strategies_ticks"):
        print("  EXACT second-by-second recordings: %d rounds" % bt.get("ticks_rounds", 0))
        print("  strategy        rounds  traded   total $   per round   win%   trades/round")
        for lab, s in bt["strategies_ticks"].items():
            if s.get("n"):
                print("  %-14s %6d %7d %9.2f %10.3f %6.1f %8.1f" % (lab, s["n"], s["traded"], s["pnl"], s["per_round"], s["win_pct"], s["trades_per_round"]))
    for side, s in (bt.get("spots") or {}).items():
        print("  best %s trade in hindsight: avg +%.0f c per contract after fees; usually buys around minute %.1f at %.0f c and sells around minute %.1f" % (side, 100 * s["avg_best_profit"], s["median_buy_minute"], 100 * s["median_buy_price"], s["median_sell_minute"]))
    y = bt.get("yours")
    if y:
        print("  YOUR trades matched to history: %d rounds, %+.2f total, %+.3f per round, won %.0f%%, avg stake $%.2f, first buy ~minute %.1f" % (y["rounds"], y["your_total"], y["your_avg"], y["your_win_pct"], y["avg_stake"], y["avg_first_buy_minute"]))
        print("    held a loser to the end although a profitable exit existed: %d rounds (avg %.0f c per contract left on the table)" % (y["lost_while_a_profitable_exit_existed"]["rounds"], 100 * y["lost_while_a_profitable_exit_existed"]["avg_missed_per_contract"]))
        print("    sold early on a side that went on to win: %d rounds   avg best exit available: %+.0f c per contract" % (y["sold_early_but_that_side_won"]["rounds"], 100 * y["avg_best_exit_per_contract"]))
        for lab, s in y["strategies_on_the_same_rounds"].items():
            print("    strategy %-12s on your rounds: avg %+.3f per round (fixed $20 bets), won %.0f%%" % (lab, s["avg"], s["win_pct"]))


def sweep(days, ag, cfg):
    """Try swing variants on the exact recordings. Pick on the older 70 percent of rounds, then check on the newer 30 percent."""
    import itertools
    tuse, tcand, tbtc = load_ticks(days)
    if len(tuse) < 20:
        print("Only %d fully recorded rounds so far; a sweep needs at least 20." % len(tuse)); return
    cut = int(len(tuse) * 0.7)
    tr, te = tuse[:cut], tuse[cut:]
    out = []
    grid = list(itertools.product((0.0, 10.0, 20.0, 30.0), (0.55, 0.80), (4.0, 6.0), (0.25, 0.35)))
    print("Sweeping %d swing variants on %d training rounds and %d later test rounds ..." % (len(grid), len(tr), len(te)), flush=True)
    for stop, cap, move, slow in grid:
        o = {"stop": stop, "entry_cap": cap, "move": move, "slow": slow}
        a = summarize(run_one("s", "swing", ag, tr, tcand, tbtc, cfg, o))
        b = summarize(run_one("s", "swing", ag, te, tcand, tbtc, cfg, o))
        out.append({"stop": stop, "cap": cap, "move": move, "slow": slow, "train": a.get("per_round"), "test": b.get("per_round"), "test_win": b.get("win_pct")})
    base = summarize(run_one("d", "distance", ag, tr, tcand, tbtc, cfg)).get("per_round"), summarize(run_one("d", "distance", ag, te, tcand, tbtc, cfg)).get("per_round")
    out.sort(key=lambda x: -(x["train"] or -99))
    json.dump({"made": int(time.time()), "train_rounds": len(tr), "test_rounds": len(te), "variants": out, "distance": base}, open(os.path.join(H, "sweep.json"), "w"))
    print("  best on training rounds (per round, $20 bets), then the same settings on later rounds they never saw:")
    for x in out[:6]:
        print("   cut loss at %2.0fc  price limit %.2f  move %.0fc  slow %.2f : train %+.2f   test %+.2f (won %s%%)" % (x["stop"], x["cap"], x["move"], x["slow"], x["train"] or 0, x["test"] or 0, x["test_win"]))
    print("  for comparison, distance-only: train %+.2f  test %+.2f" % (base[0] or 0, base[1] or 0))
    print("  worst on training:", ["%+.2f/%+.2f" % (x["train"] or 0, x["test"] or 0) for x in out[-3:]])


def main():
    if "--sweep" in sys.argv:
        try:
            cfg = json.load(open(os.path.join(DIR, "config.json")))
        except (OSError, ValueError):
            cfg = {}
        sweep(float(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[1] == "--sweep" else 14, float(cfg.get("aggression", 30)), cfg)
        return
    if "--show" in sys.argv:
        try:
            show(json.load(open(os.path.join(H, "backtest.json"))))
        except (OSError, ValueError):
            show(None)
        return
    days = float(sys.argv[1]) if len(sys.argv) > 1 else 14
    try:
        cfg = json.load(open(os.path.join(DIR, "config.json")))
    except (OSError, ValueError):
        cfg = {}
    ag = float(sys.argv[2]) if len(sys.argv) > 2 else float(cfg.get("aggression", 30))
    use, cand, ts, vs = load(days)
    if len(use) < 10:
        print("Only %d rounds with prices. Run backfill.py first." % len(use)); return
    btc = Series(ts, vs)
    print("Replaying %d rounds of minute history (distance and hold only: minute prices are too coarse for swing) ..." % len(use), flush=True)
    strategies, per_round = {}, {}
    for lab, pn, a in (("distance", "distance", ag), ("hold", "hold", ag)):
        t0 = time.time()
        rows = run_one(lab, pn, a, use, cand, btc, cfg)
        strategies[lab] = summarize(rows)
        per_round[lab] = {x["t"]: x["pnl"] for x in rows}
        print("  %-10s done in %.0fs: %d rounds, %+.2f total" % (lab, time.time() - t0, strategies[lab].get("n", 0), strategies[lab].get("pnl", 0)), flush=True)
    tick_s, tuse = {}, []
    try:
        tuse, tcand, tbtc = load_ticks(days)
    except Exception as e:
        print("  could not read the second-by-second recordings:", e)
    if len(tuse) >= 5:
        print("Replaying %d rounds the agent recorded second by second (exact prices) ..." % len(tuse), flush=True)
        for lab, pn, a in (("swing@10", "swing", 10), ("swing@30", "swing", 30), ("swing@60", "swing", 60), ("swing@90", "swing", 90), ("distance", "distance", ag), ("hold", "hold", ag)):
            t0 = time.time()
            rows = run_one(lab, pn, a, tuse, tcand, tbtc, cfg)
            tick_s[lab] = summarize(rows)
            print("  %-10s done in %.0fs: %d rounds, %+.2f total" % (lab, time.time() - t0, tick_s[lab].get("n", 0), tick_s[lab].get("pnl", 0)), flush=True)
    bt = {"made": int(time.time()), "rounds": len(use), "first": use[0]["open"], "last": use[-1]["close"], "days": days,
          "resolution": "last known 1-minute quote (no peeking ahead), $20 bets, your Settings for cap and minimum", "strategies": strategies,
          "ticks_rounds": len(tuse), "strategies_ticks": tick_s,
          "spots": spots(use, cand), "yours": yours(use, cand, per_round)}
    json.dump(bt, open(os.path.join(H, "backtest.json"), "w"))
    show(bt)


if __name__ == "__main__":
    main()
