"""Render a v4 timeline spec (recorded assets placed in numpy rooms) to a mastered stereo mix plus bus stems.

usage: uv run tools/audio/mix2.py work/pilot/audio/v4/mix.json [--only ID,ID] [--no-master]

The spec is written by tools/audio/build_pilot_mix.py from audio/pilot/{sfx,dialogue,score_cues}.json and
mix_plan.md; its top-level "sources" block is the one place to swap a take:

  "sources": {
    "sfx_dir": "work/pilot/audio/sfx",                       # <id>_<name>.wav (".take1" files ignored)
    "music":    {"M1": {"src": "...mp3", "edit": {...}}, "M2": {"src": null}},      # null -> silent placeholder
    "dialogue": {"D01": {"src": "...wav", "chain": "father"}, "D17": {"same_as": "D01"},
                 "D09": {"say": {"voice": "Karen", "rate": 165, "text": "Four minutes."}}, "V01": null}
  }

Event kinds (all times absolute timeline seconds; every event has id, bus and optional lvl / lvl_mode / gain):
  shot    one sound: src, at (where the source's align point lands; default align = its first onset), trim, ratio,
          keep, fade, hold, chain, room, wet, pan, width, auto, lp_auto, pan_auto
  series  one source on many times [[t, dB, cents], ...] (slices rotate, jitter), rendered dry then roomed once;
          lvl is resolved on one representative hit
  bed     a continuous source running in real time, gated by spans [[a, b, lvl, in, out]] (edge: "x" = 83 ms
          crossfade on the cut, "hard", or a fade length in s); pitch_auto [[t, cents]], ratio, variants
  line    a dialogue line: line id (+ phrase), at = voiced onset, chain from the dialogue source, room, lvl (LUFS over
          the voiced span); missing sources become labelled placeholders
  cue     a music cue: cue id, use (segment list in the cue's edit), lvl_keys [[t, LUFS-S], ...], cut, freeze
  gen     numpy generators: "loop" (mix_plan.md 5)
Globals: mutes [{from, to, except}], ducks [{from, to, db, attack, release, except | only}], tapestop, bus_fx, master.
"""
import fnmatch
import glob
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mix as M  # noqa: E402  (render_say, limit, write, loudness)
import rooms as R  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SR = 48000
db = R.db
NOTES = {"C": -9, "D": -7, "E": -5, "F": -4, "G": -2, "A": 0, "B": 2}


def note_hz(n):
    if isinstance(n, (int, float)):
        return float(n)
    s = NOTES[n[0].upper()]
    i = 1
    while i < len(n) and n[i] in "#b":
        s += 1 if n[i] == "#" else -1
        i += 1
    return 440.0 * 2 ** ((s + 12 * (int(n[i:]) - 4)) / 12)


# ------------------------------------------------------------------ sources
_CACHE = {}


def load_audio(path):
    p = str(ROOT / path)
    if p not in _CACHE:
        raw = M.subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-f", "f32le", "-ac", "2", "-ar", str(SR), "-"],
                               capture_output=True, check=True).stdout
        _CACHE[p] = np.frombuffer(raw, np.float32).reshape(-1, 2).astype(np.float64)
    return _CACHE[p]


def sfx_path(spec, sid):
    d = ROOT / spec["sources"]["sfx_dir"]
    c = [p for p in glob.glob(str(d / f"{sid}_*.wav")) if ".take" not in Path(p).name]
    if len(c) != 1:
        raise FileNotFoundError(f"{sid}: {c}")
    return str(Path(c[0]).relative_to(ROOT))


def say(cfg):
    txt = cfg["text"]
    parts = txt if isinstance(txt, list) else [txt]
    return [M.render_say(cfg["voice"], cfg.get("rate"), t, cfg.get("af")) for t in parts]


def onset(x, floor=-30, hop=0.005):
    """First 5 ms frame within `floor` dB of the loudest frame, minus one frame."""
    m = R.mono(x)
    k = int(hop * SR)
    n = max(1, len(m) // k)
    e = np.sqrt((m[:n * k].reshape(n, k) ** 2).mean(1)) + 1e-12
    i = int(np.argmax(20 * np.log10(e) > 20 * np.log10(e.max()) + floor))
    return max(0, i - 1) * k


def phrases(x, gap=0.12):
    """Split a (gated) line into phrases at silences of at least `gap` s -> [(a, b), ...] sample ranges."""
    m = np.abs(R.mono(x))
    k = int(0.01 * SR)
    n = len(m) // k
    e = m[:n * k].reshape(n, k).max(1)
    act = e > e.max() * db(-40)
    segs, i = [], 0
    g = int(gap / 0.01)
    while i < n:
        if act[i]:
            j = i
            while j < n and act[j:j + g].any():
                j += 1
            segs.append((i * k, min(len(m), j * k + k)))
            i = j
        else:
            i += 1
    return segs


def voice_frames(x, hop=0.01):
    """Per 10 ms frame: voice-band (100 Hz-4 kHz) energy in dB and periodicity (normalised autocorrelation peak,
    70-400 Hz lags, 40 ms window)."""
    m = R.mono(x)
    vb = R.filt(m, [["bp", 100, 4000, 2]])
    k = int(hop * SR)
    n = len(m) // k
    e = 10 * np.log10((vb[:n * k].reshape(n, k) ** 2).mean(1) + 1e-14)
    W = int(0.04 * SR)
    lo, hi = int(SR / 400), int(SR / 70)
    per = np.zeros(n)
    for i in range(n):
        w = vb[i * k:i * k + W]
        if len(w) < W or e[i] < e.max() - 45:
            continue
        w = w - w.mean()
        ac = np.fft.irfft(np.abs(np.fft.rfft(w, 2 * W)) ** 2)[:W]
        if ac[0] > 0:
            per[i] = ac[lo:hi].max() / ac[0]
    return e, per


def voiced_onset(x, rel=-25.0, per_min=0.35):
    """Sample index of the voiced onset: the first frame within `rel` dB of the clip's loudest frame that is
    periodic, or is followed by a periodic frame within 150 ms (so an aspirated h- or s- counts from its start).
    Breaths (no periodic frame at all) fall back to the energy onset."""
    e, per = voice_frames(x)
    if not len(e):
        return 0
    loud = e > e.max() + rel
    periodic = per > per_min
    for i in np.nonzero(loud)[0]:
        if periodic[i:i + 15].any():
            return i * int(0.01 * SR)
    return int(np.argmax(loud)) * int(0.01 * SR)


def voiced_end(x, rel=-35.0):
    e, _ = voice_frames(x)
    idx = np.nonzero(e > e.max() + rel)[0]
    return (int(idx[-1]) + 1) * int(0.01 * SR) if len(idx) else len(R.mono(x))


def take_segments(x, rel=-35.0, merge=0.15, min_len=0.05):
    """Split a take at its pauses: runs of frames within `rel` dB of the take's 97th-percentile voice-band level,
    joined across gaps of up to `merge` s. -> [(start_s, end_s, voiced_fraction, peak_db), ...]"""
    e, per = voice_frames(x)
    top = np.percentile(e, 97)
    act = e > top + rel
    runs, i, n = [], 0, len(e)
    while i < n:
        if act[i]:
            j = i
            while j < n and act[j]:
                j += 1
            runs.append([i, j])
            i = j
        else:
            i += 1
    out = []
    for a, b in runs:
        if out and a - out[-1][1] <= merge * 100:
            out[-1][1] = b
        else:
            out.append([a, b])
    return [(a / 100, b / 100, float((per[a:b] > 0.45).mean()), float(e[a:b].max())) for a, b in out if (b - a) / 100 >= min_len]


def assemble(x, spans, max_gap=None, pad=0.08):
    """Cut [a, b] spans (s) out of a take and join them; the pause between two spans keeps the take's own
    silence, shortened from its middle to at most max_gap s (20 ms crossfade)."""
    m = R.mono(x)
    parts = []
    for i, (a, b) in enumerate(spans):
        a0 = max(0, int((a - pad) * SR)) if i == 0 else int(a * SR)
        b0 = min(len(m), int((b + pad) * SR)) if i == len(spans) - 1 else int(b * SR)
        parts.append(m[a0:b0])
        if i < len(spans) - 1:
            g0, g1 = int(b * SR), int(spans[i + 1][0] * SR)
            gap = m[g0:g1]
            if max_gap is not None and len(gap) > max_gap * SR:
                h = int(max_gap * SR / 2)
                xf = int(0.02 * SR)
                a_, b_ = gap[:h + xf].copy(), gap[len(gap) - h - xf:].copy()
                r = np.linspace(0, 1, xf)
                a_[-xf:] *= r[::-1]
                b_[:xf] *= r
                gap = np.concatenate([a_[:-xf], a_[-xf:] + b_[:xf], b_[xf:]])
            parts.append(gap)
    return np.concatenate(parts)


class Sources:
    def __init__(self, spec):
        self.spec = spec
        self.dx = spec["sources"]["dialogue"]
        self.mu = spec["sources"]["music"]
        self._lines = {}

    def sfx(self, sid):
        """The generated asset; unless it is listed as a hum, the generator's mains-series lines are notched out."""
        x = load_audio(sfx_path(self.spec, sid))
        dh = self.spec["sources"].get("dehum")
        if dh and sid not in dh.get("keep", []):
            key = ("dehum", sid)
            if key not in _CACHE:
                _CACHE[key] = R.filt(x, [["dehum", dh.get("base", 50), dh.get("top", 1000)]], pad=int(0.05 * SR))
            return _CACHE[key]
        return x

    def line(self, lid):
        """-> (mono processed clip, chain name, provenance) or None when the line is not recorded yet."""
        if lid in self._lines:
            return self._lines[lid]
        cfg = self.dx.get(lid)
        if cfg is None:
            self._lines[lid] = None
            return None
        if cfg.get("same_as"):
            r = self.line(cfg["same_as"])
            self._lines[lid] = r if r is None else (r[0], r[1], f"= {cfg['same_as']} ({r[2]})")
            return self._lines[lid]
        chain = cfg.get("chain", "none")
        if cfg.get("say"):
            parts = say(cfg["say"])
            prov = f"say {cfg['say']['voice']} (stand-in)"
            clips = [R.CHAINS[chain](p) for p in parts]
            self._lines[lid] = (clips, chain, prov)
            return self._lines[lid]
        if cfg.get("take"):
            x = assemble(load_audio(cfg["take"]), cfg["spans"], cfg.get("max_gap"))
            x = R.CHAINS[chain](x)
            self._lines[lid] = (x, chain, f"{Path(cfg['take']).name} {cfg['spans']}")
            return self._lines[lid]
        x = R.mono(load_audio(cfg["src"]))
        if cfg.get("part"):
            a, b = cfg["part"]
            x = x[int(a * SR):int(b * SR)]
        x = R.CHAINS[chain](x)
        self._lines[lid] = (x, chain, cfg.get("standin", Path(cfg["src"]).name))
        return self._lines[lid]

    def phrase(self, lid, i=None):
        r = self.line(lid)
        if r is None:
            return None
        x, chain, prov = r
        if isinstance(x, list):  # say: one clip per phrase
            return (x[i or 0] if i is not None else np.concatenate([np.concatenate([c, np.zeros(int(0.35 * SR))]) for c in x]), chain, prov)
        if i is None:
            return x, chain, prov
        segs = phrases(x)
        if i >= len(segs):
            raise ValueError(f"{lid} has {len(segs)} phrases, asked for {i}")
        a, b = segs[i]
        a = max(0, a - int(0.04 * SR))
        return x[a:b + int(0.03 * SR)], chain, prov


# ------------------------------------------------------------------ helpers
def fade(x, fi, fo):
    n = len(x)
    e = np.ones(n)
    a, b = min(n, int(fi * SR)), min(n, int(fo * SR))
    if a:
        e[:a] = np.linspace(0, 1, a)
    if b:
        e[n - b:] *= np.linspace(1, 0, b)
    return x * (e[:, None] if x.ndim == 2 else e)


def kf(t, keys, default=0.0):
    if not keys:
        return np.full(len(t), default)
    ks = sorted(keys)
    return np.interp(t, [k[0] for k in ks], [k[1] for k in ks])


def ops_of(e, key="chain"):
    return e.get(key) or []


def measure(y, mode, a=None, b=None):
    if mode == "peak":
        return 20 * np.log10(np.abs(y).max() + 1e-12)
    if mode == "line":
        return R.span_loudness(y, a, b)
    if mode == "st3":  # the plan's reading: the loudest 3 s short-term window over the sound (alone)
        return float(R.st_curve(np.concatenate([np.zeros((SR, 2)), R.as_st(y), np.zeros((SR, 2))])).max())
    v = float(R.integrated(y))  # gated (BS.1770) loudness over the span: robust to sparse beds
    return v if v > -69 else float(R.span_loudness(y))  # below the absolute gate: ungated


def hold_source(x, h):
    """Play x to h['loop'][1], loop [a, b] with 30 ms crossfades for h['for'] s, then x from h['release']."""
    a, b = int(h["loop"][0] * SR), int(h["loop"][1] * SR)
    seg = x[a:b]
    xf = int(0.03 * SR)
    n_hold = int(h["for"] * SR)
    out = [x[:b]]
    cur = 0
    body = np.zeros((n_hold + xf,) + x.shape[1:])
    step = len(seg) - xf
    while cur < n_hold:
        s = fade(seg.copy(), 0.03, 0.03)
        m = min(len(s), len(body) - cur)
        body[cur:cur + m] += s[:m]
        cur += step
    out.append(body[:n_hold])
    out.append(fade(x[int(h["release"] * SR):], 0.03, 0))
    return np.concatenate(out)


def deplosive(x, cut=200.0, win=0.06, max_dip=12.0):
    """Duck low-frequency bursts in the first 60 ms of words: the band below `cut` only, 5 ms ramps.
    A burst is a 5 ms frame after a word onset whose LF energy exceeds the rest of the spectrum by 3 dB and the
    line's typical LF level by 6 dB. -> (processed, largest dip in dB)"""
    m = R.mono(x)
    lo = R.filt(m, [["lp", cut, 2]])
    hi = m - lo
    k = int(0.005 * SR)
    n = len(m) // k
    if n < 8:
        return x, 0.0
    E = lambda v: 10 * np.log10((v[:n * k].reshape(n, k) ** 2).mean(1) + 1e-14)
    Ea, El, Eh = E(m), E(lo), E(hi)
    act = Ea > Ea.max() - 30
    ref = np.median(El[act]) if act.any() else El.max()
    g = np.zeros(n)
    for i in range(4, n):
        if Ea[i] - Ea[i - 4:i].min() > 9 and Ea[i] > Ea.max() - 40:
            for j in range(i, min(n, i + int(win / 0.005))):
                over = min(El[j] - (Eh[j] + 3), El[j] - (ref + 6))
                if over > 0:
                    g[j] = max(g[j], min(max_dip, over))
    if not g.any():
        return x, 0.0
    gs = np.interp(np.arange(len(m)) / k - 0.5, np.arange(n), g)
    r = int(0.005 * SR)
    gs = np.convolve(gs, np.ones(r) / r, "same")
    y = lo * db(-gs) + hi
    return y, float(g.max())


def sampler_note(smp, r, dur, loop, decay_db_s=7.0, release=0.08):
    """One note from a recorded piano note: the attack as recorded, then its sustain looped (flattened, 60 ms
    crossfades) and resampled by r (pitch); the decay is applied in output time, so a held note decays like one."""
    a, b = int(loop[0] * SR), int(loop[1] * SR)
    seg = smp[a:b].copy()
    q = int(0.05 * SR)
    d0 = 20 * np.log10(np.sqrt((seg[:q] ** 2).mean()) + 1e-12)
    d1 = 20 * np.log10(np.sqrt((seg[-q:] ** 2).mean()) + 1e-12)
    ramp = db(np.linspace(0, d0 - d1, len(seg)))
    seg = seg * (ramp[:, None] if seg.ndim == 2 else ramp)
    xf = int(0.06 * SR)
    need = int((dur * r + 0.2) * SR)
    src = [smp[:a]]
    L = a
    w = np.linspace(0, 1, xf)
    w2 = w[:, None] if seg.ndim == 2 else w
    body = seg.copy()
    while L + len(body) < need + len(seg):
        nxt = seg.copy()
        body = np.concatenate([body[:-xf], body[-xf:] * (1 - w2) + nxt[:xf] * w2, nxt[xf:]])
        L = a + len(body)
    src = np.concatenate([smp[:a], body])[:need]
    y = R.resample_ratio(src, r)
    t = np.arange(len(y)) / SR
    ta = a / SR / r
    env = db(-decay_db_s * np.clip(t - ta, 0, None))
    y = y * (env[:, None] if y.ndim == 2 else env)
    y = y[:int(dur * SR)]
    return fade(y, 0.0, min(release, dur / 2))


def limit_fast(x, ceiling, look=0.002, release=0.02):
    """Per-line peak control (a de-plosive): 2 ms look-ahead, 20 ms release, on 0.5 ms frames."""
    fr = SR // 2000
    n = -(-len(x) // fr)
    pk = np.zeros(n * fr)
    pk[:len(x)] = np.abs(R.as_st(x)).max(1)
    need = np.minimum(1, ceiling / (pk.reshape(n, fr).max(1) + 1e-12))
    la = int(look * 2000)
    need = np.min(np.stack([np.roll(need, -i) for i in range(la + 1)]), 0)
    g, y = np.ones(n), 1.0
    cr = 1 - np.exp(-1 / (release * 2000))
    for i, v in enumerate(need):
        y = v if v < y else y + (v - y) * cr
        g[i] = y
    gs = np.interp(np.arange(len(x)) / fr - 0.5, np.arange(n), g)
    return x * (gs[:, None] if x.ndim == 2 else gs)


# ------------------------------------------------------------------ renderer
class Renderer:
    def __init__(self, spec):
        self.spec = spec
        self.N = int(round(spec["dur"] * SR))
        self.src = Sources(spec)
        self.buses = {}
        self.report = {"events": [], "placeholders": [], "lines": [], "warnings": []}
        self.dips = {}

    # ---- global envelopes
    def _rules_for(self, eid, rules):
        out = []
        for r in rules:
            if any(fnmatch.fnmatch(eid, p) for p in r.get("except", [])):
                continue
            if r.get("only") and not any(fnmatch.fnmatch(eid, p) for p in r["only"]):
                continue
            out.append(r)
        return out

    def env(self, eid, t, bus, kind=None):
        g = np.ones(len(t))
        for r in self._rules_for(eid, self.spec.get("mutes", [])):
            if r.get("buses") and bus not in r["buses"]:
                continue
            a, b = r["from"], r["to"]
            ri = r.get("ramp_in", 0.003)
            if r.get("kill") and kind != "bed" and t[0] < a:  # a hard event: what was sounding does not come back
                b = t[-1] + 1
            g *= np.interp(t, [a - 0.003, a, b, b + ri], [1, 0, 0, 1])
        for r in self._rules_for(eid, self.spec.get("ducks", [])):
            if r.get("buses") and bus not in r["buses"]:
                continue
            a, b, d = r["from"], r["to"], db(r["db"])
            at, rl = r.get("attack", 0.02), r.get("release", 0.3)
            g *= np.interp(t, [a - at, a, b, b + rl], [1, d, d, 1])
        return g

    def add(self, e, y, s, meta=None):
        """Place stereo y at sample s on the event's bus, through mutes/ducks and automation."""
        if y is None or not len(y):
            return
        y = R.as_st(y)
        if s < 0:
            y, s = y[-s:], 0
        y = y[:max(0, self.N - s)]
        if not len(y):
            return
        t = (s + np.arange(len(y))) / SR
        g = self.env(e["id"], t, e["bus"], e.get("kind"))
        if e.get("auto"):
            g = g * db(kf(t, e["auto"]))
        y = y * g[:, None]
        if e.get("lp_auto"):
            y = R.lp_sweep(y, t, e["lp_auto"])
        if e.get("pan_auto"):
            p = kf(t, e["pan_auto"])
            m = R.mono(y)
            y = np.stack([m * np.sqrt((1 - p) / 2) * np.sqrt(2), m * np.sqrt((1 + p) / 2) * np.sqrt(2)], 1)
        bus = self.buses.setdefault(e["bus"], np.zeros((self.N, 2), np.float32))
        bus[s:s + len(y)] += y.astype(np.float32)
        pk = float(20 * np.log10(np.abs(y).max() + 1e-12))
        rec = {"id": e["id"], "bus": e["bus"], "t0": round(s / SR, 3), "t1": round((s + len(y)) / SR, 3), "peak": round(pk, 1),
               "placements": e.get("placements", [])}
        if meta:
            rec.update(meta)
        self.report["events"].append(rec)

    def resolve(self, e, y, a=None, b=None, mode=None):
        mode = mode or e.get("lvl_mode", "peak")
        if e.get("lvl") is None:
            return db(e.get("gain", 0)), None
        m = measure(y, mode, a, b)
        return db(e["lvl"] - m + e.get("gain", 0)), round(m, 1)

    def room(self, x, e, seed=0):
        if e.get("room") == "WINDOW":
            w = e.get("window", {})
            return R.window_room(x, w.get("dist", -8), w.get("pan", 0), w.get("lpf", 1800), w.get("phone", False), seed)
        y = R.apply_room(x, e.get("room"), e.get("wet"), e.get("kind_room", "object"), seed)
        if e.get("send"):  # a second room mixed in (e.g. the capsule's 20 % to HALL_FAR)
            r2, g2 = e["send"]
            z = R.apply_room(x, r2, None, "object", seed + 1) * db(g2)
            n = max(len(y), len(z))
            out = np.zeros((n, 2))
            out[:len(y)] += y
            out[:len(z)] += z
            y = out
        if e.get("pan") is not None:
            gl, gr = R.pan_gains(e["pan"])
            y = y * np.array([gl, gr])
        if e.get("width") is not None:
            y = R.width(y, e["width"])
        if e.get("post"):
            y = R.filt(y, e["post"])
        bfx = self.spec.get("bus_fx", {}).get(e.get("bus"))
        if bfx:
            if any(o[0] == "mono" for o in bfx):
                y = np.stack([R.mono(y)] * 2, 1)
            y = R.filt(y, [o for o in bfx if o[0] != "mono"])
        return y

    # ---- kinds
    def dry_shot(self, e, seed):
        src = e["src"]
        x = self.src.sfx(src["sfx"])
        if src.get("slice"):
            a, b = src["slice"]
            x = x[int(a * SR):int(b * SR)]
        x = R.mono(x) if e.get("mono_src", True) else x
        if e.get("ratio"):
            x = R.resample_ratio(x, e["ratio"])
        al = onset(x) if e.get("align") in (None, "onset") else int(e["align"] / (e.get("ratio") or 1) * SR)
        if e.get("keep"):
            x = fade(x[:al + int(e["keep"] * SR)], 0, e.get("keep_fade", 0.01))
        if e.get("hold"):
            x = hold_source(x, e["hold"])
        if e.get("fade"):
            x = fade(x, *e["fade"])
        x = R.filt(x, ops_of(e))
        return x, al

    def do_shot(self, e, seed=0):
        x, al = self.dry_shot(e, seed)
        y = self.room(x, e, seed)
        g, m = self.resolve(e, y)
        self.add(e, y * g, int(round(e["at"] * SR)) - al, {"measured": m, "lvl": e.get("lvl")})

    def do_series(self, e, seed=0):
        rng = np.random.default_rng(seed)
        src = e["src"]
        full = R.mono(self.src.sfx(src["sfx"]))
        slices = src.get("slices") or [src.get("slice") or [0, len(full) / SR]]
        hits = []
        for sl in slices:
            h = full[int(sl[0] * SR):int(sl[1] * SR)]
            if e.get("ratio"):
                h = R.resample_ratio(h, e["ratio"])
            if e.get("keep"):
                h = fade(h[:onset(h) + int(e["keep"] * SR)], 0, e.get("keep_fade", 0.01))
            if e.get("fade"):
                h = fade(h, *e["fade"])
            h = R.filt(h, ops_of(e))
            hits.append(h / (np.abs(h).max() + 1e-12))
        times = [it if isinstance(it, list) else [it] for it in e["times"]]
        jit = e.get("jitter", {})
        t0 = times[0][0] - 0.2
        L = int((times[-1][0] - t0 + max(len(h) for h in hits) / SR / 0.9 + 0.5) * SR)
        dry = np.zeros(L)
        for i, it in enumerate(times):
            if len(it) > 3:
                h = hits[it[3]]
            else:
                h = hits[i % len(hits)] if not jit.get("random_slice") else hits[rng.integers(len(hits))]
            c = (it[2] if len(it) > 2 else 0) + rng.uniform(-1, 1) * jit.get("cents", 0)
            if c:
                h = R.resample_ratio(h, 2 ** (c / 1200))
            g = db((it[1] if len(it) > 1 else 0) + rng.uniform(-1, 1) * jit.get("db", 0))
            s = int(round((it[0] - t0) * SR)) - onset(h)
            if e.get("until"):
                h = h[:max(0, int((e["until"] - it[0]) * SR))]
                h = fade(h, 0, 0.01)
            M.place(dry, h * g, s)
        rep = hits[len(hits) // 2]
        yr = self.room(rep, e, seed)
        g, m = self.resolve(e, yr)
        y = self.room(dry, e, seed)
        self.add(e, y * g, int(round(t0 * SR)), {"measured": m, "lvl": e.get("lvl"), "hits": len(times)})

    def bed_positions(self, e, t):
        """Source read position (source samples) for timeline times t: continuous in real time, integrating pitch."""
        base = e.get("ratio", 1.0)
        if not e.get("pitch_auto"):
            return t * SR * base
        tc = np.arange(0, self.spec["dur"] + 1, 0.001)
        r = base * 2 ** (kf(tc, e["pitch_auto"]) / 1200)
        pos = np.concatenate([[0], np.cumsum(r)[:-1]]) * 0.001 * SR
        return np.interp(t, tc, pos)

    def tile(self, x, p0, p1, seed):
        """The bed's source in 'tile space' [p0, p1) samples: blocks from random offsets, 1 s equal-power seams."""
        L = len(x)
        xf = int(min(1.0 * SR, L / 4))
        step = L - xf
        rng_off = lambda i: 0 if i == 0 else int(np.random.default_rng(seed * 1000 + i).integers(0, L))
        out = np.zeros((int(p1 - p0) + 2,) + x.shape[1:])
        b0, b1 = int(p0 // step) - 1, int(p1 // step) + 1
        w = np.sin(np.linspace(0, np.pi / 2, xf)) if xf else np.ones(0)
        for i in range(max(0, b0), b1 + 1):
            off = rng_off(i)
            idx = (off + np.arange(step + xf)) % L
            blk = x[idx].copy()
            if xf:
                blk[:xf] *= (w if blk.ndim == 1 else w[:, None])
                blk[step:] *= (w[::-1] if blk.ndim == 1 else w[::-1, None])
            s = i * step - int(p0)
            a, b = max(0, s), min(len(out), s + len(blk))
            if b > a:
                out[a:b] += blk[a - s:b - s]
        return out

    def gate(self, t, spans, gains):
        g = np.zeros(len(t))
        for (sp, gv) in zip(spans, gains):
            a, b = sp[0], sp[1]
            ei = sp[3] if len(sp) > 3 else "x"
            eo = sp[4] if len(sp) > 4 else "x"

            def edge(kind, at, rising):
                if kind == "x":
                    return (at - 0.0415, at + 0.0415)
                if kind == "hard":
                    return (at, at + 0.003) if rising else (at - 0.003, at)
                d = float(kind)
                return (at, at + d) if rising else (at - d, at)
            ia, ib = edge(ei, a, True)
            oa, ob = edge(eo, b, False)
            g += gv * np.interp(t, [ia, ib, oa, ob], [0, 1, 1, 0], left=0, right=0)
        return g

    def do_bed(self, e, seed=0):
        if e["src"].get("gen") == "carrier":
            n = int(20 * SR)
            x = R.filt(np.random.default_rng(7).normal(0, 1, n), [["lp", 12000, 1]])
            x = np.stack([x, x], 1)
        else:
            x = self.src.sfx(e["src"]["sfx"])
            if e.get("mono_src"):
                x = np.stack([R.mono(x)] * 2, 1)
        spans = sorted(e["spans"], key=lambda s: s[0])
        pre = e.get("preroll", 3.0 if e.get("room") not in (None, "HALL_BED", "DRY") else 0.2)
        # render clusters of spans that are close together as one segment
        clusters, cur = [], [spans[0]]
        for sp in spans[1:]:
            if sp[0] - cur[-1][1] < pre + 1.0:
                cur.append(sp)
            else:
                clusters.append(cur)
                cur = [sp]
        clusters.append(cur)
        meas = []
        for cl in clusters:
            ta, tb = max(0.0, cl[0][0] - pre), min(self.spec["dur"], cl[-1][1] + 0.3)
            t = np.arange(int(ta * SR), int(tb * SR)) / SR
            pos = self.bed_positions(e, t)
            p0 = pos[0]
            tl = self.tile(x, np.floor(p0), pos[-1] + 2, seed)
            y = R.warp(tl, pos - np.floor(p0))
            y = R.filt(y, ops_of(e))
            for v in e.get("variants", []):  # e.g. the Hall's still air after 186.4
                if v["from"] < tb:
                    z = R.filt(y, v["ops"])
                    w = np.clip((t - v["from"]) / v.get("xfade", 0.5), 0, 1)[:, None]
                    y = y * (1 - w) + z * w
            if e.get("mod"):
                md = e["mod"]
                gm = 1 + md["depth"] * np.sin(2 * np.pi * md["hz"] * t)
                if md.get("spans"):
                    inside = np.zeros(len(t), bool)
                    for a, b in md["spans"]:
                        inside |= (t >= a) & (t < b)
                    gm = np.where(inside, gm, 1)
                y = y * gm[:, None]
            y = self.room(y, e, seed)[:len(t)]
            gains = []
            for sp in cl:
                i0, i1 = np.searchsorted(t, sp[0] + 0.1), np.searchsorted(t, sp[1] - 0.1)
                seg = y[i0:max(i1, i0 + int(0.5 * SR))]
                if sp[2] is None:
                    gains.append(db(e.get("gain", 0)))
                    continue
                m = measure(seg, "st")
                meas.append(round(m, 1))
                if m < -90:  # nothing in the span (e.g. a sparse asset): use the bed's level elsewhere
                    m = float(np.median([v for v in meas if v > -90])) if any(v > -90 for v in meas) else sp[2]
                gdb = sp[2] - m + e.get("gain", 0)
                if gdb > 45:
                    self.report["warnings"].append(f"{e['id']} span {sp[:2]} needs {gdb:+.1f} dB: capped at +45")
                    gdb = 45
                gains.append(db(gdb))
            y = y * self.gate(t, cl, gains)[:, None]
            chk = []
            for sp in cl:
                i0, i1 = np.searchsorted(t, sp[0] + 0.1), np.searchsorted(t, sp[1] - 0.1)
                if sp[2] is not None and i1 > i0 + SR // 4:
                    chk.append([sp[0], sp[1], sp[2], round(measure(y[i0:i1], "st"), 1)])
            self.add(e, y, int(round(ta * SR)), {"measured": meas, "lvl": [s[2] for s in spans], "span_check": chk})

    def line_clip(self, e):
        """-> (clip trimmed to 40 ms before its voiced onset, onset sample, voiced end sample, provenance) or None."""
        r = self.src.phrase(e["line"], e.get("phrase"))
        if r is None:
            return None
        x, chain, prov = r
        x = R.mono(x).copy()
        x = R.filt(x, [["hp", 85, 2]])  # per-line high-pass
        x, dip = deplosive(x)
        if chain != "ida":  # Ida's chain already de-esses
            x = R.de_ess(x)
        self.dips[e.get("id", e.get("line"))] = dip
        on = voiced_onset(x, e.get("onset_rel", -25.0), e.get("onset_per", 0.35))
        if not e.get("keep_preroll"):  # trim to 40 ms before the voiced onset
            a = max(0, on - int(0.04 * SR))
            x, on = x[a:], on - a
        if e.get("keep_span"):  # non-verbal lines keep their whole span (a breath has no voiced end)
            end = len(x) - int(0.08 * SR)
        else:
            end = voiced_end(x)
        x = fade(x[:min(len(x), end + int(0.12 * SR))], 0.005, 0.06)
        if e.get("ratio"):
            x = R.resample_ratio(x, e["ratio"])
            on, end = int(on / e["ratio"]), int(end / e["ratio"])
        return x, on, end, prov

    def do_line(self, e, seed=0, measure_only=False):
        r = self.line_clip(e)
        if r is None:
            if not measure_only:
                self.report["placeholders"].append({"id": e["id"], "what": f"dialogue {e['line']} has no source: silent",
                                                    "at": e["at"]})
                self.report["lines"].append({"id": e["id"], "at": e["at"], "missing": True, "lvl": e.get("lvl")})
            return None
        x, on, end, prov = r
        at = e["at"]
        voiced = (end - on) / SR
        notes = []
        if e.get("end_by") is not None and at + voiced > e["end_by"] + 1e-3:
            over = at + voiced - e["end_by"]
            if e.get("fit") == "shift":
                at = e["end_by"] - voiced
                notes.append(f"moved {-over:+.2f} s to end by {e['end_by']}")
            elif e.get("fit") == "trim":
                keep = on + int((e["end_by"] - at) * SR)
                x = fade(x[:keep + int(0.03 * SR)], 0, 0.06)
                end = keep
                notes.append(f"trimmed {over:.2f} s to end by {e['end_by']}")
            else:
                notes.append(f"MISSES end_by {e['end_by']} by {over:.2f} s")
        if e.get("not_before") is not None and at < e["not_before"]:
            at = e["not_before"]
        dw = e.get("dur_window")
        if dw and not (dw[0] - 0.05 <= voiced <= dw[1] + 0.05):
            notes.append(f"voiced {voiced:.2f} s outside dur {dw}")
        for ta_, dur_, gdb_ in e.get("clip_gain", []):  # a consonant edit: [absolute time, length, dB], 3 ms ramps
            tt = (np.arange(len(x)) - on) / SR + at
            x = x * db(np.interp(tt, [ta_ - 0.003, ta_, ta_ + dur_, ta_ + dur_ + 0.003], [0, gdb_, gdb_, 0]))
            notes.append(f"clip gain {gdb_} dB at {ta_:.3f} for {dur_ * 1000:.0f} ms")
        y = self.room(x, dict(e, kind_room="voice"), seed)
        g, m = self.resolve(e, y, on, max(end, on + int(0.3 * SR)), e.get("lvl_mode", "st3"))
        if measure_only:
            return 20 * np.log10(g)
        if e.get("group_gain") is not None:
            g = db(e["group_gain"])
        y = y * g
        gr = 0.0
        if e.get("lvl") is not None and e.get("peak_ctl", 12) is not None:  # per-line limiter, at most 4 dB of reduction
            pk0 = np.abs(y).max()
            ceil = max(db(e["lvl"] + e.get("peak_ctl", 12)), pk0 / db(e.get("max_gr", 4.0)))
            if pk0 > ceil:
                y = limit_fast(y, ceil)
                gr = 20 * np.log10(pk0 / ceil)
        notes.append(f"de-plosive max dip {self.dips.get(e['id'], 0):.1f} dB, line limiter {gr:.1f} dB")
        self.add(e, y, int(round(at * SR)) - on, {"measured": m, "lvl": e.get("lvl"), "src": prov, "line": e["line"]})
        self.report["lines"].append({"id": e["id"], "line": e["line"], "planned": e["at"], "onset": round(at, 3),
                                     "voiced_end": round(at + (end - on) / SR, 3), "voiced_s": round(voiced, 2),
                                     "dur_window": dw, "end_by": e.get("end_by"), "target": e.get("lvl"),
                                     "gain_db": round(20 * np.log10(g), 1), "src": prov, "room": e.get("room"),
                                     "bus": e["bus"], "notes": notes})

    def cue_audio(self, e):
        cfg = self.src.mu.get(e["cue"]) or {}
        if not cfg.get("src"):
            return None, cfg
        x = load_audio(cfg["src"])
        edit = (cfg.get("edit") or {}).get(e.get("use", "main"))
        if edit is None:  # the nominal edit: the file's start on the cue's in point
            edit = {"segments": [{"src": [0, len(x) / SR], "at": e["in"], "fade": [0.005, 0.005]}]}
        t0 = e["in"] - 2.0
        n = int((e["out"] - t0 + 1.0) * SR)
        out = np.zeros((n, 2))
        for sg in edit["segments"]:
            a, b = sg["src"]
            seg = x[int(a * SR):int(b * SR)].copy()
            if sg.get("ops"):
                seg = R.filt(seg, sg["ops"])
            seg = fade(seg, *sg.get("fade", [0.005, 0.005]))
            M.place(out, seg, int(round((sg["at"] - t0) * SR)))
        for a_, b_, d_ in edit.get("duck", []):  # the take's own conflicting line, ducked under the sampler
            tt = t0 + np.arange(n) / SR
            out *= db(np.interp(tt, [a_ - 0.25, a_, b_, b_ + 0.25], [0, d_, d_, 0]))[:, None]
        if edit.get("notes"):  # the motif, played on a sampled note of the take's own piano
            sp = cfg["sample"] if "sample" in cfg else self.src.mu[cfg["sample_from"]]["sample"]
            smp = load_audio(sp["file"])[int(sp["span"][0] * SR):int(sp["span"][1] * SR)]
            on_s = onset(smp) / SR
            rng = np.random.default_rng(sum(map(ord, e["id"])))
            jit = edit.get("jitter", {})
            placed = []
            for nt in edit["notes"]:
                t_, name, gdb, dur = nt[0], nt[1], nt[2], nt[3]
                anchor = len(nt) > 4 and nt[4] == "anchor"
                dt = 0.0 if anchor else rng.uniform(-1, 1) * jit.get("ms", 0) / 1000
                gj = rng.uniform(-1, 1) * jit.get("db", 0)
                r = note_hz(name) / sp["f0"]
                y = sampler_note(smp, r, dur + on_s / r, [sp["loop"][0] - sp["span"][0], sp["loop"][1] - sp["span"][0]],
                                 sp.get("decay_db_s", 7.0))
                M.place(out, R.as_st(y) * db(gdb + gj), int(round((t_ + dt - t0) * SR)) - int(on_s / r * SR))
                placed.append([round(t_ + dt, 3), name, round(gdb + gj, 1)])
            self.report.setdefault("motif", {})[e["id"]] = placed
        for fr in edit.get("freeze", []):  # hold [a, b] on the grain just before it: no new attack inside
            a, b = int((fr[0] - t0) * SR), int((fr[1] - t0) * SR)
            gl, xf, src_len = int(0.12 * SR), int(0.05 * SR), int(0.25 * SR)
            pool = out[a - src_len:a].copy()
            win = np.hanning(gl)[:, None]
            hop = gl // 3
            body = np.zeros((b - a + 2 * xf + 2 * gl, 2))
            wsum = np.zeros((len(body), 1))
            rng = np.random.default_rng(3)
            for cur in range(0, len(body) - gl, hop):
                j = int(rng.integers(0, src_len - gl))
                body[cur:cur + gl] += pool[j:j + gl] * win
                wsum[cur:cur + gl] += win
            body = (body / np.maximum(wsum, 1e-3))[gl:gl + b - a + 2 * xf]
            w = np.ones((b - a + 2 * xf, 1))
            w[:xf, 0] = np.linspace(0, 1, xf)
            w[-xf:, 0] = np.linspace(1, 0, xf)
            out[a - xf:b + xf] = out[a - xf:b + xf] * (1 - w) + body * w
        return (out, int(round(t0 * SR))), cfg

    def do_cue(self, e, seed=0):
        r, cfg = self.cue_audio(e)
        if r is None:
            self.report["placeholders"].append({"id": e["id"], "what": f"music {e['cue']} ({e.get('use', 'main')}) not generated yet: "
                                                f"silent placeholder {e['in']}-{e['out']}", "at": e["in"]})
            self.report["events"].append({"id": e["id"], "bus": e["bus"], "t0": e["in"], "t1": e["out"], "placeholder": True})
            return
        y, s = r
        if e.get("mono"):
            y = np.stack([R.mono(y)] * 2, 1)
        y = R.filt(y, ops_of(e) + [o for o in self.spec.get("bus_fx", {}).get(e["bus"], []) if o[0] != "mono"])
        t = (s + np.arange(len(y))) / SR
        if e.get("lvl_keys"):
            st = R.st_curve(y, win=e.get("lvl_win", 3.0))
            ts = np.arange(len(st)) * 0.1 + 0.05 + s / SR
            mg = e.get("lvl_win", 3.0) / 2
            lo, hi = e["in"] + mg, max(e["in"] + mg, e["out"] - mg)  # read keys away from the cue's edges
            gk = [[k[0], k[1] - float(np.interp(np.clip(k[0], lo, hi), ts, st))] for k in e["lvl_keys"]]
            y = y * db(kf(t, gk))[:, None]
        if e.get("ride"):  # a gain ride onto a target curve (the Unison's continuous crescendo)
            rd = e["ride"]
            st = R.st_curve(y, win=rd.get("win", 3.0))
            k = max(1, int(rd.get("smooth", 3.0) / 0.1))
            sts = np.convolve(st, np.ones(k) / k, "same")
            ts = np.arange(len(st)) * 0.1 + 0.05 + s / SR
            need = np.clip(kf(ts, rd["keys"]) - sts, rd.get("min", -20), rd.get("max", 20))
            need = np.convolve(need, np.ones(k) / k, "same")
            y = y * db(np.interp(t, ts, need))[:, None]
        if e.get("peak_ctl_dbfs") is not None:
            y = M.limit(y, db(e["peak_ctl_dbfs"]))
        if e.get("cut"):
            c, f = e["cut"]
            g = np.interp(t, [c - f, c], [1, 0], left=1, right=0)
            y = y * g[:, None]
        if e.get("fade_out"):
            a, b = e["fade_out"]
            y = y * np.interp(t, [a, b], [1, 0], left=1, right=0)[:, None]
        y = y * np.interp(t, [e["in"] - 0.005, e["in"]], [0, 1], left=0, right=1)[:, None] if e.get("hard_in") else y
        self.add(e, y * db(e.get("gain", 0)), s, {"src": cfg.get("src")})

    def do_gen(self, e, seed=0):
        if e["gen"] == "loop":
            return self.gen_loop(e)
        raise ValueError(e["gen"])

    def gen_loop(self, e):
        """mix_plan.md 5: the Engine splicing the cold open's own clips, collapsing onto I am well."""
        rng = np.random.default_rng(212)
        t0, t1 = e["from"], e["to"]
        n = int((t1 - t0 + 8) * SR)
        mon = np.zeros((n, 2))
        horn = np.zeros(n)
        car = np.zeros(n)
        joins = []

        def clip(ref):
            r = self.line_clip(ref)
            if r is None:
                self.report["placeholders"].append({"id": e["id"], "what": f"loop fragment {ref} missing"})
                return None
            return r[0]

        def put(x, at, send, p, cents=0.0, lpf=None, g=1.0):
            if cents:
                x = R.resample_ratio(x, 2 ** (cents / 1200))
            if lpf:
                x = R.filt(x, [["lp", lpf, 2]])
            s = int(round((at - t0) * SR)) - int(0.04 * SR * (1 / 2 ** (cents / 1200)))  # clips start 40 ms before the onset
            s = max(0, s)
            m = min(len(x), n - s)
            gl, gr = R.pan_gains(p)
            mon[s:s + m, 0] += x[:m] * (1 - send) * gl * g
            mon[s:s + m, 1] += x[:m] * (1 - send) * gr * g
            horn[s:s + m] += x[:m] * send * g
            joins.extend([s, s + m])

        ref = e["ref"]
        for f in e["phase_a"]:  # [line ref key, time]
            x = clip(ref[f[0]])
            if x is not None:
                put(x, f[1], 0.0, 0.0)
        send = e.get("send_b0", 0.1)
        for i, f in enumerate(e["phase_b"]):
            x = clip(ref[f[0]])
            if x is not None:
                put(x, f[1], min(1, send + 0.1 * i), 0.2 * (-1) ** i)
        # phase C: onsets shrinking exponentially 0.33 -> 0.067 s over c0..c1, then constant, until the HALT
        c0, c1, cend = e["phase_c"]
        g0, g1 = e.get("gaps", [0.33, 0.067])
        ts, t = [], c0
        while t < cend:
            ts.append(t)
            u = np.clip((t - c0) / (c1 - c0), 0, 1)
            t += g0 * (g1 / g0) ** u
        d03 = clip(ref["I_am_well"])
        for i, t in enumerate(ts):
            u = i / max(1, len(ts) - 1)
            put(d03, t, 0.4 + 0.6 * u, rng.uniform(-0.8, 0.8), rng.uniform(15, 40) * rng.choice([-1, 1]),
                lpf=8000 * (3000 / 8000) ** u)
        self.report["loop"] = {"phase_c_copies": len(ts), "phase_c_onsets": [round(x, 3) for x in ts]}
        # the carrier on the monitor, with one frame dropped and a two-sample step at each join (phase A)
        if e.get("carrier_db") is not None:
            cz = R.filt(np.random.default_rng(9).normal(0, 1, n), [["lp", 12000, 1]])
            cz = cz / np.sqrt(np.mean(cz ** 2)) * db(e["carrier_db"])
            fr = int(SR / 24)
            a_end = int((e["phase_b"][0][1] - t0) * SR)
            cz[a_end:] = 0
            for j in joins:
                if j < a_end:
                    cz[j:j + fr] = 0
                    if j + 2 < n:
                        cz[j:j + 2] += db(-42)
            car = cz
        ym = R.apply_room(mon, "MONITOR", None, "voice")
        yh = R.apply_room(horn, "HALL_HORNS")
        L = max(len(ym), len(yh))
        y = np.zeros((L, 2))
        y[:len(ym)] += ym
        y[:len(yh)] += yh
        # level: phases A-B at lvl_a (LUFS over the fragments), then the stack rises to lvl_top at t_top
        ta = np.arange(L) / SR + t0
        pa = (ta >= t0) & (ta < c0)
        ga = e["lvl_a"] - R.span_loudness(y[pa])
        y = y * db(ga)
        st = R.st_curve(y, win=3.0)
        tst = np.arange(len(st)) * 0.1 + 0.05 + t0
        tgt = np.interp(tst, [c0, e["t_top"]], [e["lvl_a"], e["lvl_top"]])
        need = np.where(tst >= c0, tgt - st, 0.0)
        need = np.clip(need, -3, 20)
        need = np.convolve(need, np.ones(5) / 5, "same")
        gcur = np.interp(ta, tst, need)
        gcur[ta < c0] = 0
        y = y * db(gcur)[:, None]
        if e.get("peak_ctl_dbfs") is not None:  # the loop's own peak control, released for the master limiter before HALT
            yl = M.limit(y, db(e["peak_ctl_dbfs"]))
            w = np.clip((e.get("peak_ctl_until", 1e9) - ta) / 0.05, 0, 1)[:, None]
            y = yl * w + y * (1 - w)
        m = min(len(car), len(y))
        y[:m] += np.stack([car[:m], car[:m]], 1)  # the carrier keeps its own level
        self.add(e, y, int(round(t0 * SR)), {"lvl_a": e["lvl_a"], "lvl_top": e["lvl_top"]})

    # ---- main
    def render(self, only=None):
        groups = {}
        for e in self.spec["events"]:
            if e.get("kind") == "line" and e.get("group"):
                g = self.do_line(e, 0, measure_only=True)
                if g is not None:
                    groups.setdefault(e["group"], []).append(g)
        for e in self.spec["events"]:
            if e.get("kind") == "line" and e.get("group") in groups:
                e["group_gain"] = float(np.mean(groups[e["group"]]))
        for i, e in enumerate(self.spec["events"]):
            if "kind" not in e:
                continue
            if only and not any(fnmatch.fnmatch(e["id"], p) for p in only):
                continue
            seed = int(hashlib.md5(e["id"].encode()).hexdigest()[:6], 16)
            getattr(self, "do_" + e["kind"])(e, seed)
            print(f"  {e['id']:<22} {e['kind']:6} -> {e['bus']}", flush=True)
        # the tape-stop on its bus, then the signal gap
        ts = self.spec.get("tapestop")
        if ts and ts["bus"] in self.buses:
            b = self.buses[ts["bus"]].astype(np.float64)
            a, d = int(ts["at"] * SR), ts["dur"]
            tau = np.arange(int(d * SR)) / SR
            pos = a + (tau - tau ** 3 / (3 * d * d)) * SR
            seg = R.warp(b, pos)
            b[a:a + len(seg)] = seg
            b[a + len(seg):int(ts["until"] * SR)] = 0
            self.buses[ts["bus"]] = b.astype(np.float32)
        # bus_fx are applied per event (in room()), so each level is resolved on what its bus plays
        return self.buses


def master(spec, buses, out):
    ms = spec["master"]
    mix = sum(b.astype(np.float64) for b in buses.values())
    I0 = R.integrated(mix)
    gain = ms["lufs"] - I0
    binding = []
    if ms.get("max_gr_db") is not None:  # dynamics over loudness: the gain at which the limiter never takes more than
        fr = SR // 1000                     # max_gr_db outside the allowed windows (look-ahead limiter on 1 ms frames)
        n = len(mix) // fr
        pk = 20 * np.log10(np.abs(mix[:n * fr]).max(1).reshape(n, fr).max(1) + 1e-12)
        t = np.arange(n) / 1000
        ok = np.ones(n, bool)
        for a, b in ms.get("gr_allowed", []):
            ok &= ~((t >= a) & (t <= b))
        g_pk = ms["limit_dbfs"] + ms["max_gr_db"] - pk[ok].max()
        order = np.argsort(pk[ok])[::-1]
        binding = [[round(float(t[ok][i]), 3), round(float(pk[ok][i]), 2)] for i in order[:8]]
        gain = min(gain, g_pk - 0.05)
    elif abs(gain) > ms.get("max_gain_db", 2):
        print(f"  WARNING: master gain {gain:+.2f} dB exceeds +-{ms.get('max_gain_db', 2)} dB: rebalance")
    fin = M.limit(mix * db(gain), db(ms["limit_dbfs"]))
    pre_pk = 20 * np.log10(np.abs(mix * db(gain)).max())
    gr = 20 * np.log10(np.maximum(np.abs(fin).max(1), 1e-12) / np.maximum(np.abs(mix * db(gain)).max(1), 1e-12))
    out.parent.mkdir(parents=True, exist_ok=True)
    f32 = out.with_name(out.stem + ".f32.wav")
    M.write(f32, fin, "pcm_f32le")
    M.write(out, fin, "pcm_s24le")
    for name, b in buses.items():
        M.write(out.with_name(f"{out.stem}.{name}.wav"), b.astype(np.float64) * db(gain), "pcm_f32le")
    L = M.loudness(out)
    return {"premaster_I": round(I0, 2), "gain_db": round(gain, 2), "binding_peaks_premaster [t, dBFS]": binding, "pre_limit_peak_dbfs": round(float(pre_pk), 2),
            "max_gain_reduction_db": round(float(-gr.min()), 2), **L,
            "bus_peaks_dbfs": {k: round(float(20 * np.log10(np.abs(v).max() * db(gain) + 1e-12)), 1) for k, v in buses.items()}}


def main():
    args = sys.argv[1:]
    spec_path = Path(args[0])
    spec = json.loads(spec_path.read_text())
    only = None
    if "--only" in args:
        only = args[args.index("--only") + 1].split(",")
    M.CACHE = ROOT / spec.get("say_cache", "work/pilot/audio/vo")
    r = Renderer(spec)
    buses = r.render(only)
    out = ROOT / spec["out"]
    if "--no-master" not in args:
        r.report["master"] = master(spec, buses, out)
        print("  master:", r.report["master"])
    (out.with_name(out.stem + ".report.json")).write_text(json.dumps(r.report, indent=1) + "\n")
    for p in r.report["placeholders"]:
        print("  PLACEHOLDER", p)


if __name__ == "__main__":
    main()
