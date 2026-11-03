#!/usr/bin/env python3
"""COACH for the market agent. Read-only diagnosis: WHERE did the practice money go, and which simple guardrails would have kept it.
Reads every buy and sell the agent logged (trades.jsonl), settles each round with Kalshi's real result, charges real fees, and tags
every losing round with its cause:
  CHURN      sold within 30 s of buying (pays spread + fees twice for nothing)
  OVERTRADE  more than 3 buys in one round (fee drag)
  BAD PRICE  bought in a price zone that has lost money (50-90c)
  HELD LOSER held to the end and lost, never sold
  EARLY SELL sold a winner for less than it ended up paying
  WRONG SIDE ended on the wrong side with a normal hold
For each fix it computes what the money would have been without those trades, on the older and the newer half of the rounds, and writes
coach_rules.json: a rule is marked "proven" only if it would have helped in BOTH halves. Usage: python3 coach.py [hours=72] [strategy]"""
import json, math, os, sys, time

HOME = os.path.expanduser("~")
D = os.environ.get("MARKET_DIR", os.path.join(HOME, "market-data"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
CHURN_SECS, MAX_BUYS, BAD_LO, BAD_HI = 30, 3, 0.50, 0.90


def fee_total(c, p):
    return math.ceil(0.07 * c * p * (1 - p) * 100 - 1e-9) / 100.0


def load_rounds(hours, only):
    import exit_learn as X
    res = X.outcomes(D)
    cut = time.time() - hours * 86400 / 24.0
    ev = {}
    try:
        for l in open(os.path.join(D, "trades.jsonl")):
            try: r = json.loads(l)
            except ValueError: continue
            if r.get("live") or r.get("a") not in ("BUY", "SELL") or not r.get("t") or r["t"] < cut or not r.get("c") or not r.get("px"):
                continue
            if only and r.get("s") != only: continue
            ev.setdefault((r.get("s"), r.get("ticker")), []).append(r)
    except OSError:
        return [], res
    out = []
    for (s, tk), rs in ev.items():
        rr = res.get(tk)
        if rr not in ("UP", "DOWN"): continue
        rs.sort(key=lambda r: r["t"])
        pos = {}                                         # side -> [contracts, cost]
        cash = fees = 0.0; buys = 0; churn = 0.0; churn_n = 0; last_buy = {}; early = 0.0; hi_buys = []; entries = []
        for r in rs:
            side, c, p = r["side"], int(r["c"]), float(r["px"])
            f = fee_total(c, p)
            if r["a"] == "BUY":
                buys += 1; cash -= c * p + f; fees += f
                P = pos.setdefault(side, [0, 0.0]); P[0] += c; P[1] += c * p + f
                last_buy[side] = r["t"]
                entries.append({"n": buys, "px": p, "side": side, "c": c, "cost": c * p + f, "t": r["t"], "sold": 0.0, "csold": 0})
                if BAD_LO <= p < BAD_HI: hi_buys.append(len(entries) - 1)
            else:
                P = pos.get(side)
                if not P or P[0] <= 0: continue
                c = min(c, P[0]); f = fee_total(c, p); avg = P[1] / P[0]
                gain = c * p - f - c * avg
                cash += c * p - f; fees += f; P[0] -= c; P[1] -= c * avg
                for e in entries:
                    if e["side"] == side and e["csold"] < e["c"]:
                        take = min(c, e["c"] - e["csold"]); e["sold"] += take * p - f * take / max(1, c); e["csold"] += take; c -= take
                        if c <= 0: break
                if r["t"] - last_buy.get(side, 0) < CHURN_SECS:
                    churn += gain; churn_n += 1
                if p < 0.9 and side == rr:
                    early += (1.0 - p) * int(r["c"])      # money left on the table by selling a winner early
        held_loser = 0.0; settle = 0.0
        for side, P in pos.items():
            if P[0] > 0:
                pay = P[0] * (1.0 if side == rr else 0.0); settle += pay - P[1]
                if side != rr: held_loser += P[1]
        net = cash + sum(P[0] * (1.0 if sd == rr else 0.0) for sd, P in pos.items())
        extra = [e for e in entries if e["n"] > MAX_BUYS]
        extra_pnl = sum((e["c"] * (1.0 if e["side"] == rr else 0.0) - e["cost"]) for e in extra)     # hold-to-end view of the extra buys
        bad = [entries[i] for i in hi_buys]
        bad_pnl = sum((e["c"] * (1.0 if e["side"] == rr else 0.0) - e["cost"]) for e in bad)
        out.append({"s": s, "tk": tk, "t": rs[0]["t"], "net": net, "fees": fees, "buys": buys, "churn": churn, "churn_n": churn_n,
                    "extra_pnl": extra_pnl, "extra_n": len(extra), "bad_pnl": bad_pnl, "bad_n": len(bad), "held_loser": held_loser, "early": early,
                    "wrong": net < 0 and buys > 0 and churn_n == 0 and held_loser == 0})
    out.sort(key=lambda r: r["t"])
    return out, res


def main():
    hours = float(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].replace(".", "").isdigit() else 72
    only = sys.argv[2] if len(sys.argv) > 2 else None
    R, _ = load_rounds(hours, only)
    if len(R) < 10:
        print("Only %d settled practice rounds with trades in the last %d hours; need more. Let it run." % (len(R), hours)); return
    tot = sum(r["net"] for r in R); fees = sum(r["fees"] for r in R); gross = tot + fees
    print("COACH: %d settled practice rounds%s, last %d hours" % (len(R), (" (%s only)" % only) if only else "", hours))
    print("net %+.2f after fees. Before fees it would be %+.2f; fees alone cost %.2f (%.0f%% of everything staked wins and losses combined)\n" % (tot, gross, fees, 100 * fees / max(1e-9, abs(gross) + fees)))
    by = {}
    for r in R:
        a = by.setdefault(r["s"], [0, 0.0, 0.0]); a[0] += 1; a[1] += r["net"]; a[2] += r["fees"]
    print("BY STRATEGY (rounds, net, fees):")
    for s, a in sorted(by.items(), key=lambda kv: kv[1][1]): print("  %-9s %4d rounds  %+8.2f  fees %6.2f" % (s, a[0], a[1], a[2]))
    half = len(R) // 2; A, B = R[:half], R[half:]
    rules = {}
    def rule(key, label, fn):
        a, b = sum(fn(r) for r in A), sum(fn(r) for r in B)
        rules[key] = {"label": label, "older": round(a, 2), "newer": round(b, 2), "total": round(a + b, 2), "proven": (a > 0 and b > 0)}
    # money SAVED by the rule = minus what the removed trades made
    rule("min_hold", "Never sell within %d s of buying" % CHURN_SECS, lambda r: -r["churn"])
    rule("max_buys", "At most %d buys per round" % MAX_BUYS, lambda r: -r["extra_pnl"])
    rule("price_zone", "No buys at %d-%dc" % (round(100 * BAD_LO), round(100 * BAD_HI)), lambda r: -r["bad_pnl"])
    print("\nWHERE THE MONEY WENT (all strategies):")
    print("  quick flips (sold <%ds after buying): %d of them, result %+.2f" % (CHURN_SECS, sum(r["churn_n"] for r in R), sum(r["churn"] for r in R)))
    print("  extra buys beyond %d per round: %d buys in %d rounds, result if held to the end %+.2f" % (MAX_BUYS, sum(r["extra_n"] for r in R), sum(1 for r in R if r["extra_n"]), sum(r["extra_pnl"] for r in R)))
    print("  buys at %d-%dc: %d buys, result if held to the end %+.2f" % (round(100 * BAD_LO), round(100 * BAD_HI), sum(r["bad_n"] for r in R), sum(r["bad_pnl"] for r in R)))
    print("  held to the end and lost, never sold: %d rounds, %.2f staked and lost" % (sum(1 for r in R if r["held_loser"] > 0), sum(r["held_loser"] for r in R)))
    print("  winners sold early (money left on the table): %.2f" % sum(r["early"] for r in R))
    print("  losing rounds on a normal hold, just the wrong call: %d of %d" % (sum(1 for r in R if r["wrong"]), len(R)))
    print("\nGUARDRAIL TEST (money saved if the rule had been on; older rounds | newer rounds):")
    for k, v in rules.items():
        print("  %-9s %-38s %+7.2f | %+7.2f   %s" % (k, v["label"], v["older"], v["newer"], "PROVEN (helps in both halves)" if v["proven"] else "not proven"))
    worst = sorted(R, key=lambda r: r["net"])[:5]
    print("\nWORST 5 ROUNDS:")
    for r in worst: print("  %s %-8s %+7.2f  buys %d, quick flips %d, fees %.2f" % (time.strftime("%d %H:%M", time.localtime(r["t"])), r["s"], r["net"], r["buys"], r["churn_n"], r["fees"]))
    json.dump({"made": int(time.time()), "rounds": len(R), "net": round(tot, 2), "rules": rules}, open(os.path.join(D, "coach_rules.json"), "w"))
    print("\nSaved coach_rules.json. Only PROVEN rules would be switched on, and each one is re-tested every time this runs.")


if __name__ == "__main__":
    main()
