#!/usr/bin/env python3
"""SUPERVISOR for the market agent. Read-only: it never trades and never changes the agent. Run hourly by cron.
It answers one question in plain English: is the agent still learning and making progress, or has something stalled?
 - is the agent alive and recording every second
 - did it settle new rounds and turn them into lessons since the last check
 - did its learning files update (entry evidence, exit rules, patterns, nightly weights)
 - how each practice strategy is doing, and whether that moved since last check
 - has the signal scan / backtest found anything, and how many recorded rounds it has to work with
Writes ~/market-data/progress.txt (and progress.json). Sends a phone alert only when something is stuck (at most once every 6 hours).
Usage: python3 supervisor.py        (add --quiet to skip the phone alert)"""
import glob, json, os, subprocess, sys, time

HOME = os.path.expanduser("~")
D = os.environ.get("MARKET_DIR", os.path.join(HOME, "market-data"))
OUT = os.environ.get("MARKET_OUT", os.path.join(HOME, "crew-web", "market.json"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def jl(p, default=None):
    try:
        return json.load(open(p))
    except Exception:
        return default


def age(p):
    try:
        return time.time() - os.path.getmtime(p)
    except OSError:
        return None


def hrs(s):
    return "never" if s is None else ("%d min ago" % (s // 60) if s < 7200 else "%.1f h ago" % (s / 3600))


def count_lines(p):
    try:
        with open(p, "rb") as f:
            return sum(1 for _ in f)
    except OSError:
        return 0


def main():
    now = time.time()
    quiet = "--quiet" in sys.argv
    prev = jl(os.path.join(D, "supervisor_state.json"), {}) or {}
    lines, problems = [], []
    ok = lambda m: lines.append("  OK    " + m)
    bad = lambda m: (lines.append("  STUCK " + m), problems.append(m))
    note = lambda m: lines.append("        " + m)
    lines.append("MARKET AGENT PROGRESS  %s" % time.strftime("%a %d %b %H:%M"))

    lines.append("\n1. ALIVE")
    try:
        act = subprocess.run(["systemctl", "is-active", "market-agent"], capture_output=True, text=True, timeout=5).stdout.strip()
    except Exception:
        act = "unknown"
    (ok if act == "active" else bad)("service market-agent is %s" % act)
    a = age(OUT)
    (ok if a is not None and a < 120 else bad)("live file updated %s" % hrs(a))
    tk = sorted(glob.glob(os.path.join(D, "ticks-*.jsonl*")))
    a = age(tk[-1]) if tk else None
    (ok if a is not None and a < 120 else bad)("per-second recording last wrote %s" % hrs(a))

    lines.append("\n2. LEARNING (rounds turned into lessons)")
    cut = now - 86400
    calls = []
    try:
        for l in open(os.path.join(D, "calls.jsonl")):
            try:
                c = json.loads(l)
            except ValueError:
                continue
            if (c.get("start") or 0) >= cut:
                calls.append(c)
    except OSError:
        pass
    k = sum(1 for c in calls if c.get("src") == "kalshi")
    (ok if k >= 60 else bad)("%d of the last 96 rounds were settled by Kalshi and logged" % k)
    nrev = count_lines(os.path.join(D, "reviews.jsonl"))
    if "reviews" in prev:
        d = nrev - prev["reviews"]
        (ok if d > 0 else bad)("%+d new written lessons since the last check (%d total)" % (d, nrev))
    else:
        note("%d written lessons so far (first check, nothing to compare yet)" % nrev)
    for nm, lim in (("entry_stats.json", 3), ("exit_rules.json", 3), ("patterns.json", 3), ("learn_report.json", 30)):
        a = age(os.path.join(D, nm))
        (ok if a is not None and a < lim * 3600 else bad)("%s updated %s" % (nm, hrs(a)))

    lines.append("\n3. PRACTICE SCOREBOARD (fake money, after fees)")
    S = jl(os.path.join(D, "state.json"), {}) or {}
    acc = (S.get("sim") or {}).get("acc") or {}
    cur = {}
    if acc:
        for n, v in sorted(acc.items(), key=lambda kv: -kv[1].get("pnl", 0)):
            w = v.get("windows", 0)
            cur[n] = {"pnl": round(v.get("pnl", 0), 2), "windows": w}
            p = (prev.get("acc") or {}).get(n)
            ch = ("   (%+.2f over %+d rounds since last check)" % (cur[n]["pnl"] - p["pnl"], w - p["windows"])) if p else ""
            note("%-9s %+8.2f over %4d rounds, wins %s%s" % (n, v.get("pnl", 0), w, ("%.0f%%" % (100.0 * v.get("wins", 0) / w)) if w else "-", ch))
        tw = sum(v["windows"] for v in cur.values())
        if prev.get("acc"):
            (ok if tw > sum(v["windows"] for v in prev["acc"].values()) else bad)("strategies are still settling rounds")
        pos = [n for n, v in cur.items() if v["pnl"] > 0 and v["windows"] >= 50]
        note("strategies positive with 50+ rounds: %s" % (", ".join(pos) if pos else "none yet"))
    else:
        note("scoreboard not readable (state.json has no practice accounts)")

    lines.append("\n4. EVIDENCE SEARCH")
    sg = jl(os.path.join(D, "history", "signals.json"))
    if sg:
        note("signal scan ran %s on %d recorded rounds, %d ideas tried" % (hrs(now - sg["made"]), sg["rounds"], sg["ideas"]))
        w = sg.get("winners") or []
        note("winners positive in older AND newer rounds: %s" % (", ".join("%s/%s" % (x["sig"], "with" if x["dir"] > 0 else "against") for x in w[:5]) or "none"))
    else:
        note("signal scan has not produced a result yet (needs ~60 recorded rounds; run python3 signals.py)")
    rounds = 0
    try:
        import replay
        rounds = len(replay.load_ticks(14)[0]) if "--deep" in sys.argv else (sg or {}).get("rounds", 0)
    except Exception:
        pass
    if "rounds_rec" in prev and rounds:
        note("recorded second-by-second rounds: %d (%+d since last check)" % (rounds, rounds - prev["rounds_rec"]))

    lines.append("\nVERDICT: " + ("PROGRESSING. Nothing is stuck." if not problems else "NEEDS ATTENTION: %d thing(s) stuck: %s" % (len(problems), "; ".join(problems))))
    text = "\n".join(lines)
    print(text)
    try:
        open(os.path.join(D, "progress.txt"), "w").write(text + "\n")
        json.dump({"t": int(now), "problems": problems}, open(os.path.join(D, "progress.json"), "w"))
        st = {"reviews": nrev, "acc": cur, "rounds_rec": rounds or prev.get("rounds_rec", 0), "t": int(now), "alerted": prev.get("alerted", 0)}
        if problems and not quiet and now - prev.get("alerted", 0) > 6 * 3600:
            try:
                import alerts
                alerts.send("Market agent needs attention: " + "; ".join(problems)[:200], title="Agent progress check")
                st["alerted"] = int(now)
            except Exception:
                pass
        json.dump(st, open(os.path.join(D, "supervisor_state.json"), "w"))
    except OSError as e:
        print("could not save:", e)


if __name__ == "__main__":
    main()
    try:                                                   # the supervisor also keeps the experiments moving (innovate.py), not just watching
        import innovate
        sys.argv = [sys.argv[0]]
        innovate.main()
    except Exception as e:
        print("innovator failed:", e)
