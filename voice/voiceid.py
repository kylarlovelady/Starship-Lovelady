"""Voice recognition for Jarvis. Basic numpy-only voiceprint (MFCC statistics + pitch).

Honest limits: this tells apart different kinds of voices (adult vs child, many male vs female) reasonably and similar voices poorly.
It is meant for 'who is probably talking' labels and for the Lab accuracy test, NOT for security. The embed() function is the one
place to swap in a stronger speaker model later (everything else only uses the vectors it returns)."""
import json, os, time
import numpy as np

SR = 16000
NMEL, NCEP = 40, 20
_FB = {}


def _mel(f): return 2595.0 * np.log10(1.0 + f / 700.0)
def _imel(m): return 700.0 * (10 ** (m / 2595.0) - 1.0)


def _fbank(nfft):
    if nfft in _FB: return _FB[nfft]
    pts = _imel(np.linspace(_mel(60), _mel(7600), NMEL + 2)); bins = np.floor((nfft + 1) * pts / SR).astype(int)
    fb = np.zeros((NMEL, nfft // 2 + 1))
    for i in range(1, NMEL + 1):
        l, c, r = bins[i - 1], bins[i], bins[i + 1]
        for k in range(l, c): fb[i - 1, k] = (k - l) / max(1, c - l)
        for k in range(c, r): fb[i - 1, k] = (r - k) / max(1, r - c)
    _FB[nfft] = fb; return fb


def _dct(n_in, n_out):
    n = np.arange(n_in); return np.array([np.cos(np.pi * k * (2 * n + 1) / (2 * n_in)) for k in range(1, n_out + 1)])


def _pitch(x, flo=70, fhi=400):
    """Median pitch (Hz) of voiced frames by autocorrelation. Returns (median_log_f0, std_log_f0) or None."""
    fl, hop = 640, 320; lo, hi = int(SR / fhi), int(SR / flo); f0s = []
    for i in range(0, len(x) - fl, hop):
        fr = x[i:i + fl]; fr = fr - fr.mean(); e = float(np.dot(fr, fr))
        if e < 1e-3: continue
        ac = np.correlate(fr, fr, "full")[fl - 1:]
        seg = ac[lo:hi]; k = int(np.argmax(seg)) + lo
        if ac[k] / ac[0] > 0.45: f0s.append(SR / k)
    if len(f0s) < 5: return None
    l = np.log(np.array(f0s)); return float(np.median(l)), float(l.std())


def embed(pcm):
    """int16 16 kHz samples -> feature vector (None if there is not enough speech)."""
    x = pcm.astype(np.float64) / 32768.0
    if len(x) < SR: return None
    x = np.append(x[0], x[1:] - 0.97 * x[:-1])
    fl, hop, nfft = 400, 160, 512
    n = 1 + (len(x) - fl) // hop
    idx = np.arange(fl)[None, :] + hop * np.arange(n)[:, None]
    fr = x[idx] * np.hamming(fl)
    en = np.log(np.sum(fr ** 2, axis=1) + 1e-10)
    keep = en > np.percentile(en, 45)
    if keep.sum() < 40: return None
    pw = np.abs(np.fft.rfft(fr[keep], nfft)) ** 2
    mf = np.log(pw @ _fbank(nfft).T + 1e-10) @ _dct(NMEL, NCEP).T
    mf = mf - 0.0
    p = _pitch(pcm.astype(np.float64) / 32768.0)
    f0m, f0s = p if p else (np.log(150.0), 0.2)
    return np.concatenate([mf.mean(0), mf.std(0), [f0m * 6.0, f0s * 6.0]])


class VoiceBook:
    def __init__(self, path):
        self.path = path; self.v = {}
        try: self.v = json.load(open(path))
        except Exception: self.v = {}

    def save(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True); json.dump(self.v, open(self.path, "w"))

    def enroll(self, name, pcm, level="guest"):
        """Add a recording (>= 8 s of speech). The spread between 3-second pieces is used as the voice's natural variation."""
        pieces = [embed(pcm[i:i + 3 * SR]) for i in range(0, len(pcm) - 2 * SR, 3 * SR)]
        pieces = [p for p in pieces if p is not None]
        if len(pieces) < 2: return False, "Not enough speech. Talk for about 15-20 seconds."
        a = np.array(pieces); cur = self.v.get(name)
        if cur:
            old = np.array(cur["samples"]); a = np.vstack([old, a])[-40:]
        self.v[name] = {"level": (cur or {}).get("level", level), "samples": a.tolist(), "n": int((cur or {}).get("n", 0)) + 1, "updated": time.time()}
        self.save(); return True, "Saved %d pieces for %s." % (len(a), name)

    def _stats(self, name):
        a = np.array(self.v[name]["samples"]); c = a.mean(0); s = np.maximum(a.std(0), 0.35 * np.maximum(np.abs(c).mean(), 1.0) * 0.1 + 0.15)
        return c, s

    def identify(self, pcm):
        """Returns (best_name, distance, ranked list). Smaller distance = closer. None if no voices or not enough speech."""
        if not self.v: return None, None, []
        e = embed(pcm)
        if e is None: return None, None, []
        rank = []
        for n in self.v:
            c, s = self._stats(n); rank.append((n, float(np.sqrt(np.mean(((e - c) / s) ** 2)))))
        rank.sort(key=lambda t: t[1]); return rank[0][0], rank[0][1], rank

    def delete(self, name):
        self.v.pop(name, None); self.save()

    def set_level(self, name, level):
        if name in self.v and level in ("owner", "family", "guest"): self.v[name]["level"] = level; self.save()

    def listing(self):
        return [{"name": n, "level": d["level"], "pieces": len(d["samples"]), "enrollments": d.get("n", 1)} for n, d in self.v.items()]
