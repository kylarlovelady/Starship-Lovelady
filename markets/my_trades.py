"""Read-only. Pulls YOUR real Kalshi BTC 15-minute trades (fills) and shows how you actually trade: when in the round you
buy, at what price, how often you take profit early, and what you made after fees. Places no orders.
Saves a copy to ~/market-data/my_trades.json so the agent can later learn from it."""
import json, os, sys, time, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kalshi_trade as K


def f(x, d=0.0):
    try:
        return float(x)
    except Exception:
        return d


def fills(c, max_pages=150):
    out, cur = [], None
    for _ in range(max_pages):
        q = "/portfolio/fills?limit=200" + ("&cursor=" + cur if cur else "")
        st, d = c.call("GET", q)
        if st != 200:
            print("fills request failed:", st, str(d)[:200]); break
        rows = d.get("fills") or []
        out += rows
        cur = d.get("cursor")
        if not cur or not rows:
            break
    return out


def one(r):
    """Normalise one fill, whether Kalshi sends cents or dollar strings."""
    side = r.get("side")
    px = r.get("yes_price_dollars") if side == "yes" else r.get("no_price_dollars")
    px = f(px) if px is not None else f(r.get("yes_price" if side == "yes" else "no_price")) / 100.0
    n = f(r.get("count_fp") if r.get("count_fp") is not None else r.get("count"))
    t = r.get("created_time") or r.get("ts")
    if isinstance(t, str):
        import datetime
        t = datetime.datetime.fromisoformat(t.replace("Z", "+00:00")).timestamp()
    fee = f(r.get("fee_cost") if r.get("fee_cost") is not None else 0)
    return {"ticker": r.get("ticker") or r.get("market_ticker"), "side": side, "act": r.get("action"), "n": n, "px": px, "t": f(t), "fee": fee}


def analyse(fl, result_of):
    rounds = collections.defaultdict(list)
    for r in fl:
        x = one(r)
        if x["ticker"] and x["ticker"].startswith("KXBTC15M") and x["n"] > 0:
            rounds[x["ticker"]].append(x)
    out = []
    for tk, rs in rounds.items():
        rs.sort(key=lambda x: x["t"])
        res = result_of(tk)
        if res not in ("yes", "no"):
            continue
        cash = fee = 0.0
        net = {"yes": 0.0, "no": 0.0}
        for x in rs:
            amt = x["n"] * x["px"]
            if x["act"] == "buy":
                cash -= amt; net[x["side"]] += x["n"]
            else:
                cash += amt; net[x["side"]] -= x["n"]
            fee += x["fee"]
        pnl = cash - fee + net[res]
        start = int(rs[0]["t"] // 900 * 900)
        buys = [x for x in rs if x["act"] == "buy"]
        sells = [x for x in rs if x["act"] == "sell"]
        out.append({"ticker": tk, "start": start, "pnl": round(pnl, 2), "fees": round(fee, 2), "n_fills": len(rs),
                    "staked": round(sum(x["n"] * x["px"] for x in buys), 2),
                    "first_buy_secs": int(buys[0]["t"] - start) if buys else None,
                    "avg_buy_px": round(sum(x["px"] * x["n"] for x in buys) / max(1e-9, sum(x["n"] for x in buys)), 3) if buys else None,
                    "took_profit_early": bool(sells), "first_sell_secs": int(sells[0]["t"] - start) if sells else None,
                    "first_side": buys[0]["side"] if buys else None, "result": res})
    out.sort(key=lambda r: r["start"])
    return out


def show(rows):
    if not rows:
        print("No settled BTC 15-minute rounds found in your fills."); return
    n = len(rows)
    w = [r for r in rows if r["pnl"] > 0]
    tp = [r for r in rows if r["took_profit_early"]]
    hold = [r for r in rows if not r["took_profit_early"]]
    early = [r for r in rows if r["first_buy_secs"] is not None and r["first_buy_secs"] <= 120]
    avg = lambda xs: (sum(xs) / len(xs)) if xs else 0.0
    print("rounds traded: %d   won: %d (%.0f%%)   total after fees: %+.2f   fees: %.2f" % (n, len(w), 100 * len(w) / n, sum(r["pnl"] for r in rows), sum(r["fees"] for r in rows)))
    print("avg stake per round: $%.2f   avg win: %+.2f   avg loss: %+.2f" % (avg([r["staked"] for r in rows]), avg([r["pnl"] for r in w]), avg([r["pnl"] for r in rows if r["pnl"] <= 0])))
    print("first buy in the first 2 minutes: %d of %d rounds   avg first buy %.0fs into the round" % (len(early), n, avg([r["first_buy_secs"] for r in rows if r["first_buy_secs"] is not None])))
    print("avg buy price: %.0f cents" % (100 * avg([r["avg_buy_px"] for r in rows if r["avg_buy_px"]])))
    print("took profit early (sold before close): %d rounds, avg %+.2f, won %.0f%%" % (len(tp), avg([r["pnl"] for r in tp]), 100 * len([r for r in tp if r["pnl"] > 0]) / max(1, len(tp))))
    print("held to the end: %d rounds, avg %+.2f, won %.0f%%" % (len(hold), avg([r["pnl"] for r in hold]), 100 * len([r for r in hold if r["pnl"] > 0]) / max(1, len(hold))))
    print("avg time of first sale: %.0fs into the round" % avg([r["first_sell_secs"] for r in tp if r["first_sell_secs"] is not None]))
    print("date range: %s to %s" % (time.strftime("%m-%d %H:%M", time.localtime(rows[0]["start"])), time.strftime("%m-%d %H:%M", time.localtime(rows[-1]["start"]))))
    sp = [r for r in tp if r["pnl"] > 0]; sl = [r for r in tp if r["pnl"] <= 0]
    print("sold early at a profit: %d rounds, avg %+.2f   sold early at a loss (cut loser): %d rounds, avg %+.2f" % (len(sp), avg([r["pnl"] for r in sp]), len(sl), avg([r["pnl"] for r in sl])))
    for lo, hi, nm in ((0, 10, "under $10"), (10, 50, "$10-50"), (50, 150, "$50-150"), (150, 1e9, "over $150")):
        g = [r for r in rows if lo <= r["staked"] < hi]
        if g:
            print("stake %-10s %2d rounds  won %3.0f%%  total %+9.2f" % (nm, len(g), 100 * len([r for r in g if r["pnl"] > 0]) / len(g), sum(r["pnl"] for r in g)))
    for lo, hi, nm in ((0, 60, "first minute"), (60, 180, "minutes 2-3"), (180, 900, "after minute 3")):
        g = [r for r in rows if r["first_buy_secs"] is not None and lo <= r["first_buy_secs"] < hi]
        if g:
            print("first buy %-14s %2d rounds  won %3.0f%%  total %+9.2f" % (nm, len(g), 100 * len([r for r in g if r["pnl"] > 0]) / len(g), sum(r["pnl"] for r in g)))
    print("last 5 rounds:")
    for r in rows[-5:]:
        print("  %s  %-4s staked %-7s pnl %+7.2f %s" % (time.strftime("%m-%d %H:%M", time.localtime(r["start"])), r["first_side"], r["staked"], r["pnl"], "(sold early)" if r["took_profit_early"] else "(held)"))


if __name__ == "__main__":
    c = K.Kalshi()
    fl = fills(c)
    print("fills downloaded:", len(fl))
    cache = {}
    def result_of(tk):
        if tk not in cache:
            try:
                st, d = c.call("GET", "/markets/" + tk)
                cache[tk] = (d.get("market", d) or {}).get("result") if st == 200 else None
            except Exception:
                cache[tk] = None
        return cache[tk]
    agent = []                                          # orders the agent itself sent (live sessions): they are not your trades
    try:
        for ln in open(os.path.join(K.DIR, "live_orders.jsonl")):
            o = json.loads(ln)
            if o.get("kind") == "order" and o.get("ticker"):
                agent.append((o["ticker"], o["t"]))
    except (OSError, ValueError):
        pass
    def is_agent(r):
        x = one(r)
        return any(x["ticker"] == tk and abs(x["t"] - t) <= 12 for tk, t in agent)
    mine_f = [r for r in fl if not is_agent(r)]
    agent_f = [r for r in fl if is_agent(r)]
    print("fills that were YOUR own: %d, fills from the agent's live sessions: %d" % (len(mine_f), len(agent_f)))
    rows = analyse(mine_f, result_of)
    show(rows)
    arows = analyse(agent_f, result_of)
    if arows:
        print("THE AGENT'S live rounds (not yours): %d rounds, %+.2f after fees" % (len(arows), sum(r["pnl"] for r in arows)))
    try:
        with open(os.path.join(K.DIR, "agent_trades.json"), "w") as fh:
            json.dump(arows, fh)
        with open(os.path.join(K.DIR, "my_trades.json"), "w") as fh:
            json.dump(rows, fh)
        print("saved to ~/market-data/my_trades.json")
    except OSError:
        pass
