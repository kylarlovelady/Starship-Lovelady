"""Evidence from the agent's own recordings, used to veto bad entries and to report time-of-day behaviour.
For every finished round (Kalshi's official result) and every minute-sample of it (snapshots.jsonl, and the per-second ticks when
there are any), it asks: if you had bought EITHER side at that moment's real ask and held to the end, what happened after fees?
Results are grouped by the price paid. A price range that has lost money after fees over enough distinct rounds is blocked.
This does not depend on what the agent traded, so it keeps learning even from rounds where the agent sat out.
Also writes calendar blackouts (big scheduled US economic releases) so the agent does not open new bets around them."""
import glob, gzip, json, os, time, urllib.request

BUCKETS = [(1, 20), (20, 35), (35, 50), (50, 60), (60, 70), (70, 80), (80, 90), (90, 100)]
MIN_ROUNDS = 25          # distinct rounds needed before a price range can be blocked
BLOCK_BELOW = -0.02      # average result per contract after fees (dollars) that blocks a range
CAL_URL = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"


def fee(p):
    return 0.07 * p * (1 - p)


def _lines(path):
    op = gzip.open if path.endswith(".gz") else open
    try:
        with op(path, "rt") as f:
            for ln in f:
                try:
                    yield json.loads(ln)
                except ValueError:
                    pass
    except OSError:
        return


def _cents(v):
    try:
        x = float(v)
    except (TypeError, ValueError):
        return None
    return x * 100 if x <= 1.0 and isinstance(v, str) and "." in v else x


def _outcomes(d):
    out = {}
    for c in _lines(os.path.join(d, "calls.jsonl")):
        if c.get("outcome") in ("UP", "DOWN") and c.get("src") == "kalshi" and c.get("start"):
            out[int(c["start"])] = c["outcome"]
    return out


def _samples(d):
    """(round_start, seconds_left, yes_bid_cents, yes_ask_cents, time) once per minute per round."""
    seen = set()
    for r in _lines(os.path.join(d, "snapshots.jsonl")):
        b, a, left, t = r.get("yes_bid"), r.get("yes_ask"), r.get("secs_left"), r.get("t")
        if b is None or a is None or left is None or t is None or not (0 < left < 900):
            continue
        st = int(t + left) - 900
        key = (st, int(left) // 60)
        if key in seen:
            continue
        seen.add(key)
        yield st, left, float(b), float(a), t
    for p in sorted(glob.glob(os.path.join(d, "ticks-*.jsonl*"))):
        for r in _lines(p):
            k = r.get("k") or {}
            left, t = r.get("left"), r.get("t")
            b = _cents(k.get("yes_bid_dollars")) if k.get("yes_bid_dollars") is not None else _cents(k.get("yes_bid"))
            a = _cents(k.get("yes_ask_dollars")) if k.get("yes_ask_dollars") is not None else _cents(k.get("yes_ask"))
            if b is None or a is None or left is None or not (0 < left < 900):
                continue
            st = int(t + left) - 900
            key = (st, int(left) // 60)
            if key in seen:
                continue
            seen.add(key)
            yield st, left, b, a, t


def build(d):
    res = _outcomes(d)
    stat = {lo: {"n": 0, "w": 0, "p": 0.0, "rounds": set()} for lo, _ in BUCKETS}
    hours = {}
    for st, left, b, a, t in _samples(d):
        if st not in res or not (150 < left < 870):
            continue
        up = res[st] == "UP"
        for side, px in (("UP", a), ("DOWN", 100 - b)):
            p = px / 100.0
            if not (0.01 <= p <= 0.99):
                continue
            won = up if side == "UP" else not up
            prof = (1 - p - fee(p)) if won else (-p - fee(p))
            for lo, hi in BUCKETS:
                if lo <= px < hi:
                    s = stat[lo]
                    s["n"] += 1; s["w"] += int(won); s["p"] += prof; s["rounds"].add(st)
            h = time.localtime(t).tm_hour
            if 35 <= px < 80:                                   # only realistic entries count for time of day
                hh = hours.setdefault(h, [0, 0.0, set()])
                hh[0] += 1; hh[1] += prof; hh[2].add(st)
    out = {"updated": int(time.time()), "rounds": len(res), "price": {}, "hours": {}, "block": []}
    for lo, hi in BUCKETS:
        s = stat[lo]
        if s["n"]:
            avg = s["p"] / s["n"]
            nr = len(s["rounds"])
            out["price"]["%d-%d" % (lo, hi)] = {"n": s["n"], "rounds": nr, "win": round(s["w"] / s["n"], 3), "avg": round(avg, 4)}
            if nr >= MIN_ROUNDS and avg <= BLOCK_BELOW:
                out["block"].append([lo, hi])
    for h, (n, p, rs) in sorted(hours.items()):
        out["hours"][str(h)] = {"n": n, "rounds": len(rs), "avg": round(p / n, 4)}
    return out


def update(d, now=None, every=300):
    """Rebuild entry_stats.json at most every few minutes. Returns the stats dict (possibly the cached one)."""
    now = now or time.time()
    path = os.path.join(d, "entry_stats.json")
    try:
        old = json.load(open(path))
        if now - old.get("updated", 0) < every:
            return old
    except (OSError, ValueError):
        pass
    try:
        out = build(d)
        tmp = path + ".tmp"
        with open(tmp, "w") as f:
            json.dump(out, f)
        os.replace(tmp, path)
        return out
    except Exception:
        return {}


def blocked(stats, px_cents):
    for lo, hi in (stats or {}).get("block", []):
        if lo <= px_cents < hi:
            return (lo, hi)
    return None


# ---------- scheduled news ----------
def calendar(d, now=None, every=1800):
    """High-impact US events this week (cached). Returns a list of {"t": epoch, "title": str}."""
    now = now or time.time()
    path = os.path.join(d, "calendar.json")
    try:
        c = json.load(open(path))
        if now - c.get("fetched", 0) < every:
            return c.get("events", [])
    except (OSError, ValueError):
        c = {}
    evs = c.get("events", [])
    try:
        req = urllib.request.Request(CAL_URL, headers={"User-Agent": "starship-market-agent/1.0"})
        rows = json.loads(urllib.request.urlopen(req, timeout=10).read().decode("utf-8", "replace"))
        evs = []
        for r in rows:
            if r.get("country") == "USD" and str(r.get("impact")).lower() == "high":
                try:
                    ds = r["date"]                         # like 2026-11-04T08:30:00-05:00
                    tt = time.strptime(ds[:19], "%Y-%m-%dT%H:%M:%S")
                    off = ds[19:]
                    sign = -1 if off.startswith("-") else 1
                    hh, mm = (off[1:].split(":") + ["0"])[:2] if off else ("0", "0")
                    import calendar as _c
                    ep = _c.timegm(tt) - sign * (int(hh) * 3600 + int(mm) * 60)
                    evs.append({"t": ep, "title": r.get("title", "US event")})
                except Exception:
                    continue
        err = None
    except Exception as e:
        err = str(e)[:80]
    try:
        with open(path + ".tmp", "w") as f:
            json.dump({"fetched": now, "events": evs, "err": err}, f)
        os.replace(path + ".tmp", path)
    except OSError:
        pass
    return evs


def blackout(events, now, before=300, after=600):
    """Title of a big event that is within `before` seconds ahead or `after` seconds behind now, else None."""
    for e in events or []:
        if e["t"] - before <= now <= e["t"] + after:
            return e["title"]
    return None
