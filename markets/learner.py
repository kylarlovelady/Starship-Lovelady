"""Nightly learning step for the market agent (paper mode).
Reads the scored calls, measures each signal with an honest confidence range, fits a simple model
on the older 70 percent of calls and checks it on the newest 30 percent it has never seen.
New signal weights are adopted ONLY if they clearly beat the current ones on that unseen data,
and only in small steps. Every night's result is logged. Delete weights.json to go back to defaults."""
import json, math, os, time


def wilson(k, n, z=1.96):
    if n == 0:
        return 0.0, 1.0
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return max(0.0, c - h), min(1.0, c + h)


def _acc(w, rows, keys):
    n = r = 0
    for c in rows:
        s = sum(w[k] * (c["signals"].get(k) or 0.0) for k in keys)
        if s == 0:
            continue
        n += 1
        r += (s > 0) == (c["outcome"] == "UP")
    return (r / n if n else None), n


def learn(DIR, base_w, now=None):
    now = now or int(time.time())
    calls = []
    try:
        with open(os.path.join(DIR, "calls.jsonl")) as f:
            for line in f:
                try:
                    calls.append(json.loads(line))
                except Exception:
                    pass
    except FileNotFoundError:
        pass
    sc = [c for c in calls if c.get("outcome") in ("UP", "DOWN") and c.get("signals")]
    keys = list(base_w)
    rep = {"time": now, "scored": len(sc), "adopted": False, "signals": {}, "notes": []}
    for k in keys:
        n = r = 0
        for c in sc:
            s = c["signals"].get(k)
            if s is not None and abs(s) >= 0.1:
                n += 1
                r += (s > 0) == (c["outcome"] == "UP")
        lo, hi = wilson(r, n)
        rep["signals"][k] = {"n": n, "pct": round(100 * r / n, 1) if n else None,
                             "low": round(100 * lo, 1), "high": round(100 * hi, 1),
                             "verdict": "too early" if n < 100 else "helps" if lo > 0.5 else "hurts" if hi < 0.5 else "no clear effect"}
    if len(sc) < 200:
        rep["notes"].append("Needs 200 scored calls before it changes anything. Has %d." % len(sc))
    else:
        cut = int(len(sc) * 0.7)
        train, test = sc[:cut], sc[cut:]
        beta, b0 = [0.0] * len(keys), 0.0
        for _ in range(400):                      # logistic regression, small L2 penalty
            gb, g0 = [0.0] * len(keys), 0.0
            for c in train:
                x = [(c["signals"].get(k) or 0.0) for k in keys]
                z = b0 + sum(b * v for b, v in zip(beta, x))
                p = 1 / (1 + math.exp(-max(-30, min(30, z))))
                e = p - (1.0 if c["outcome"] == "UP" else 0.0)
                g0 += e
                for i, v in enumerate(x):
                    gb[i] += e * v
            m = len(train)
            b0 -= 0.5 * g0 / m
            beta = [b - 0.5 * (g / m + 0.01 * b) for b, g in zip(beta, gb)]
        pos = [max(0.0, b) for b in beta]
        if sum(pos) == 0:
            rep["notes"].append("The model found no signal that helps, so weights stay.")
        else:
            norm = {k: p / sum(pos) for k, p in zip(keys, pos)}
            cand = {k: 0.5 * base_w[k] + 0.5 * norm[k] for k in keys}
            stepped = {k: base_w[k] + max(-0.05, min(0.05, cand[k] - base_w[k])) for k in keys}
            tot = sum(stepped.values())
            stepped = {k: round(v / tot, 4) for k, v in stepped.items()}
            old, n_old = _acc(base_w, test, keys)
            new, n_new = _acc(stepped, test, keys)
            rep["holdout"] = {"n": n_new, "old_pct": None if old is None else round(100 * old, 1),
                              "new_pct": None if new is None else round(100 * new, 1)}
            if new is not None and old is not None and n_new >= 60 and new - old >= 0.03:
                with open(os.path.join(DIR, "weights.json"), "w") as f:
                    json.dump(stepped, f)
                rep["adopted"] = True
                rep["notes"].append("Adopted new weights: better on %d calls it had never seen (%.1f%% vs %.1f%%)." % (n_new, 100 * new, 100 * old))
            else:
                rep["notes"].append("Tried new weights but they did not clearly beat the current ones on unseen calls, so nothing changed.")
    with open(os.path.join(DIR, "learn_report.json"), "w") as f:
        json.dump(rep, f)
    with open(os.path.join(DIR, "learn_log.jsonl"), "a") as f:
        f.write(json.dumps(rep) + "\n")
    return rep
