"""Build a stereo soundtrack from a JSON timeline: scratch dialogue (macOS `say`), synthesized score and SFX, files.

usage: uv run tools/audio/mix.py <timeline.json>   -> spec["out"] (.wav, 48 kHz 24-bit stereo, loudness-normalized)

{"dur": 242, "out": "work/pilot/audio/main.wav", "lufs": -16, "tp": -1,
 "stems": true,                                # also write <out>.<bus>.wav (float) per bus, at the mix gain
 "gain_db": null,                              # fixed output gain instead of measuring (to match another render)
 "mutes": [[70.4, 71.0]],                      # true silences: every event is cut here unless it has "nomute"
 "tapestop": {"at": 19.0, "dur": 0.4},         # events sounding across `at` slow to a stop, then go silent
 "duck": {"key": "dx", "mx": -4},              # duck bus mx by 4 dB under bus dx (40 ms attack, 300 ms release)
 "cuts": [0, 5, 12],                           # shot in-points: warns when a say line runs past its shot
 "subs": "work/pilot/subs.json",               # subtitles from the rendered say durations
 "presets": {"father": {"type": "say", "voice": "Daniel", "rate": 135}},   # merged into events with "use"
 "events": [
   {"at": 3.2, "type": "say", "voice": "Samantha", "text": "...", "rate": 170, "af": "highpass=f=80", "id": "D01"},
   {"at": 0, "type": "pad", "chords": [["F3 A3 C4", 10], ["E3 G3 C4", 8]], "cutoff": 1200, "octave": true},
   {"type": "pluck", "seq": [[110, "A4"], [111, "F4"]], "gain": -20},    # seq/times expand into copies
   {"type": "phone", "kind": "red", "times": [131, [134, -6]], "gain": -12, "reverb": 0.4, "rt60": 3.5}
 ]}

Generators: say loop walla | drone pad hymn brass chime bell pluck arp shimmer pulse hit riser | tone noise bed
clock phone clicks clank breath birds blip glitch whoosh heartbeat tick file.

Common event keys (applied in this order):
  gain (dB), wide (render twice for L/R), hpf/lpf (Hz), pan (-1..1), fade [in, out] s, slap [delay s, dB],
  reverb (0..1 wet) + rt60 (s) + predelay (s) + rcut (Hz), glide [t0, t1, semitones], auto [[t, dB], ...] gain keyframes,
  spans [[t0, t1(, dB)], ...] gate, bus, noduck, nomute, use (preset name).
  say only: id (reported and subtitled), sub (subtitle text, or false), sub_end, italic, keep (s), overrun_ok.
  file: path; af / af_post (ffmpeg chains, in that order); norm (true or target dBFS: level like a say line);
        trim (true: cut leading/trailing silence); id / text / sub / sub_start / sub_end / italic as for say lines.
  loop: text (say) or path (a file, silence-trimmed), plus af / af_post as for file.
  An event without "type" or "use" (e.g. {"//": "1M2 Night Desk"}) is a comment.
  Times in auto / glide / spans / seq / times / accent are absolute timeline seconds; "at" is the event start.
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
SR = 48000
NOTE = {"C": -9, "D": -7, "E": -5, "F": -4, "G": -2, "A": 0, "B": 2}
CACHE = ROOT / "work" / "audio_cache"


def hz(n):
    if isinstance(n, (int, float)):
        return float(n)
    s = NOTE[n[0].upper()]
    i = 1
    if n[i:i + 1] in ("#", "b"):
        s += 1 if n[i] == "#" else -1
        i += 1
    return 440.0 * 2 ** ((s + 12 * (int(n[i:]) - 4)) / 12)


def notes(v):
    return v.split() if isinstance(v, str) else list(v)


def db(g):
    return 10 ** (g / 20)


def lp(x, fc):
    """Zero-phase 4th-order-ish low-pass via FFT (works on mono or (n, 2))."""
    X = np.fft.rfft(x, axis=0)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    m = 1 / (1 + (f / fc) ** 4)
    return np.fft.irfft(X * (m[:, None] if x.ndim == 2 else m), len(x), axis=0)


def hp(x, fc):
    X = np.fft.rfft(x, axis=0)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    m = 1 / (1 + (fc / np.maximum(f, 1)) ** 4)
    return np.fft.irfft(X * (m[:, None] if x.ndim == 2 else m), len(x), axis=0)


def bp(x, lo, hi):
    return lp(hp(x, lo), hi)


def sweep_lp(x, f0, f1):
    """Time-varying low-pass from f0 to f1 (geometric), by crossfading 6 static filters."""
    cs = np.geomspace(f0, f1, 6)
    ys = [lp(x, c) for c in cs]
    pos = np.linspace(0, 5, len(x))
    out = np.zeros_like(x)
    for i, y in enumerate(ys):
        out += y * np.clip(1 - np.abs(pos - i), 0, 1)
    return out


def norm(x):
    return x / (np.abs(x).max() + 1e-9)


def env(n, a=0.005, r=0.1):
    e = np.ones(n)
    na, nr = min(n, int(a * SR)), min(n, int(r * SR))
    if na:
        e[:na] = np.linspace(0, 1, na)
    if nr:
        e[n - nr:] *= np.linspace(1, 0, nr)
    return e


def expdec(n, d):
    return np.exp(-np.arange(n) / (d * SR))


def T(n):
    return np.arange(n) / SR


RNG = np.random.default_rng(3)


def noise(n):
    return RNG.normal(0, 1, n)


def colored(n, color="white"):
    x = noise(n)
    if color == "white":
        return x
    X = np.fft.rfft(x)
    f = np.maximum(np.fft.rfftfreq(n, 1 / SR), 10)
    X /= f ** (0.5 if color == "pink" else 1.0)
    return norm(np.fft.irfft(X, n))


def place(dst, src, s):
    """Add src into dst at sample s (clipped at both ends)."""
    if s < 0:
        src, s = src[-s:], 0
    m = max(0, min(len(src), len(dst) - s))
    dst[s:s + m] += src[:m]


def stereo(x, pan=0.0):
    if x.ndim == 2:
        return x
    return np.stack([x * np.sqrt((1 - pan) / 2), x * np.sqrt((1 + pan) / 2)], 1) * np.sqrt(2)


def warp(x, pos):
    """Read x (mono or stereo) at fractional sample positions pos."""
    idx = np.arange(len(x))
    if x.ndim == 1:
        return np.interp(pos, idx, x)
    return np.stack([np.interp(pos, idx, x[:, c]) for c in range(x.shape[1])], 1)


# ------------------------------------------------------------------ voices
def render_say(voice, rate, text, af=None, trim=True):
    """macOS `say` -> 48 kHz mono float, through an optional ffmpeg -af chain; cached; silence trimmed."""
    key = hashlib.sha1(json.dumps([voice, rate, text, af, trim]).encode()).hexdigest()[:16]
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / f"{key}.f32"
    if f.exists():
        return np.fromfile(f, np.float32).astype(np.float64)
    aiff = CACHE / f"{key}.aiff"
    cmd = ["say", "-v", voice, "-o", str(aiff)] + (["-r", str(rate)] if rate else []) + [text]
    subprocess.run(cmd, check=True, stdin=subprocess.DEVNULL)
    chain = ["-af", af] if af else []
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(aiff), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    if af:  # process at 48 kHz so asetrate factors are exact
        raw = subprocess.run(["ffmpeg", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-"] + chain +
                             ["-ar", str(SR), "-ac", "1", "-f", "f32le", "-"], input=raw, capture_output=True, check=True).stdout
    aiff.unlink()
    x = np.frombuffer(raw, np.float32).astype(np.float64)
    if trim:
        loud = np.nonzero(np.abs(x) > np.abs(x).max() * db(-45))[0]
        a, b = max(0, loud[0] - int(0.005 * SR)), min(len(x), loud[-1] + int(0.03 * SR))
        x = x[a:b]
    x.astype(np.float32).tofile(f)
    return x


def speech_norm(x, target=-20.0):
    """Scale speech so its gated RMS (20 ms frames within 30 dB of the loudest) sits at `target` dBFS."""
    k = int(0.02 * SR)
    fr = np.sqrt((x[:len(x) // k * k].reshape(-1, k) ** 2).mean(1) + 1e-12)
    rms = np.sqrt((fr[fr > fr.max() * db(-30)] ** 2).mean())
    return x * db(target) / rms


def say_chain(e):
    af = ",".join(a for a in (e.get("af"), e.get("af_post")) if a)
    return render_say(e.get("voice", "Samantha"), e.get("rate"), e["text"], af or None)


def trim_silence(x, floor=-45):
    loud = np.nonzero(np.abs(x) > np.abs(x).max() * db(floor))[0]
    return x[max(0, loud[0] - int(0.005 * SR)):min(len(x), loud[-1] + int(0.03 * SR))]


def load_file(e):
    """Audio file -> 48 kHz mono float, through the event's af / af_post chain."""
    af = ",".join(a for a in (e.get("af"), e.get("af_post")) if a)
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(ROOT / e["path"])] + (["-af", af] if af else []) +
                         ["-f", "f32le", "-ac", "1", "-ar", str(SR), "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).astype(np.float64)


def g_say(e):
    x = say_chain(e)
    fx = e.get("fx", "none")  # legacy quick effects
    if fx == "radio":
        x = np.tanh(bp(x, 400, 3200) * 3) / 2
    elif fx == "phone":
        x = bp(x, 300, 3400)
    elif fx == "robot":
        x = x * (0.6 + 0.4 * np.sin(2 * np.pi * 50 * T(len(x))))
    elif fx == "whisper":
        x = bp(x, 1500, 9000) * 0.8 + bp(noise(len(x)), 2000, 8000) * np.abs(lp(np.abs(x), 30)) * 2
    elif fx == "room":
        e.setdefault("reverb", 0.25)
    if e.get("keep"):  # cut the line off (e.g. "Nana—")
        x = x[:int(e["keep"] * SR)] * env(int(e["keep"] * SR), 0, 0.03)[:len(x)]
    e["_dur"] = len(x) / SR
    return speech_norm(x)  # voices are levelled by loudness, not peak: gain 0 = -20 dBFS gated RMS


def g_loop(e):
    """The Loop choir: copies of one say line on accelerating onsets, detuned, panned, darkening, rising `rise` dB."""
    one = speech_norm(trim_silence(load_file(e)) if e.get("path") else say_chain(e))
    dur = e["to"] - e["at"]
    g0, g1 = e.get("gap", [0.33, 0.07])
    ons, t = [], 0.0
    while t <= dur:
        ons.append(t)
        t += g0 * (g1 / g0) ** (t / dur)
    lo, hi = e.get("detune", [15, 40])
    f0, f1 = e.get("lpf_ramp", [8000, 3000])
    n = int((dur + len(one) / SR * 1.05 + 0.1) * SR)
    x = np.zeros((n, 2))
    for i, o in enumerate(ons):
        u = i / max(1, len(ons) - 1)
        cents = RNG.uniform(lo, hi) * RNG.choice([-1, 1])
        r = 2 ** (cents / 1200)
        c = warp(one, np.arange(0, len(one) - 1, r))
        c = lp(c, f0 * (f1 / f0) ** u)
        place(x, stereo(c, RNG.uniform(-1, 1) * e.get("spread", 0.8)), int(o * SR))
    # auto-level: short-term RMS ramps from one voice to one voice + rise dB
    w = int(0.1 * SR)
    ms = np.convolve((x ** 2).mean(1), np.ones(w) / w, "same")
    ref = np.sqrt((one ** 2).mean())
    tgt = ref * db(np.clip(T(n) / dur, 0, 1) * e.get("rise", 6))
    g = np.clip(tgt / (np.sqrt(ms) + 1e-6), 0, 1.5)
    g = np.convolve(g, np.ones(w) / w, "same")
    return x * g[:, None]


def g_walla(e):
    """A crowd of `say` voices: `per_voice` phrases each, random onsets with density rising over `dur`."""
    dur = e["dur"]
    x = np.zeros((int((dur + 4) * SR), 2))
    lo_r, hi_r = e.get("rates", [150, 180])
    lo_g, hi_g = e.get("gains", [-36, -28])
    for v in e["voices"]:
        for _ in range(e.get("per_voice", 3)):
            ph = e["phrases"][RNG.integers(len(e["phrases"]))]
            y = norm(render_say(v, int(RNG.uniform(lo_r, hi_r)), ph)) * db(RNG.uniform(lo_g, hi_g))
            y = lp(y, e.get("voice_lpf", 2500))
            y = reverb(stereo(y, RNG.uniform(-0.9, 0.9)), 0.3, 0.8)
            place(x, y, int(dur * np.sqrt(RNG.random()) * SR))
    return x / db(-30)  # so "gain" reads as the bus level


# ------------------------------------------------------------------ tonal
def chord_track(e, voice):
    """Sequence of chords [[notes, dur], ...] (or notes + dur), each with attack/release crossfades."""
    chords = e.get("chords") or [[e["notes"], e["dur"]]]
    total = sum(d for _, d in chords)
    a, r = e.get("attack", 1.5), e.get("release", 1.5)
    n = int(total * SR)
    x = np.zeros(n)
    t0 = 0.0
    for i, (ns, d) in enumerate(chords):
        last = i == len(chords) - 1
        m = int((d + (0 if last else r)) * SR)
        seg = sum(voice(hz(f), m) for f in notes(ns)) * env(m, a if i else 0.005, r)
        place(x, seg, int(t0 * SR))
        t0 += d
    return x


def g_pad(e):
    """PAD: 3 detuned band-limited saws per note, low-passed (warm ~1200, dark ~350); octave sine if warm."""
    def voice(f, m):
        t = T(m)
        y = np.zeros(m)
        for c in (-7, 0, 7):
            ff = f * 2 ** (c / 1200)
            ph = RNG.uniform(0, 6.28)
            for k in range(1, int(min(16, 8000 // ff)) + 1):
                y += np.sin(2 * np.pi * ff * k * t + ph * k) / k
        if e.get("octave"):
            y += 0.25 * 3 * np.sin(2 * np.pi * 2 * f * t)
        return y
    x = chord_track(e, voice)
    return norm(lp(x, e.get("cutoff", 600 + 3000 * e.get("bright", 0.3))))


def g_hymn(e):
    """HYMN: organ-like additive partials 1-4 (1, .5, .25, .12), 3-voice chorus ±6 cents, LPF 3 kHz."""
    e.setdefault("attack", 0.3)
    e.setdefault("release", 1.0)

    def voice(f, m):
        t = T(m)
        return sum(a * np.sin(2 * np.pi * f * 2 ** (c / 1200) * k * t + RNG.uniform(0, 6.28))
                   for c in (-6, 0, 6) for k, a in ((1, 1), (2, .5), (3, .25), (4, .12)))
    return norm(lp(chord_track(e, voice), e.get("cutoff", 3000)))


def g_brass(e):
    """BRASS: saw stack with the low-pass opening 200 -> 1200 Hz."""
    n = int(e["dur"] * SR)
    t = T(n)
    x = sum(np.sin(2 * np.pi * hz(f) * k * t) / k for f in notes(e.get("notes", "D2 A2 D3")) for k in range(1, 25))
    return norm(sweep_lp(x, *e.get("open", [200, 1200])))


def g_drone(e):
    n = int(e["dur"] * SR)
    t = T(n)
    f = hz(e.get("freq", 55))
    x = sum(np.sin(2 * np.pi * f * k * (1 + 0.0015 * d) * t + d) / k ** 1.3 for k, d in [(1, 0), (1, 1), (2, 2), (3, 3), (4, 5)])
    x = x * (0.8 + 0.2 * np.sin(2 * np.pi * 0.07 * t))
    x += 0.15 * lp(noise(n), f * 4)
    return norm(x)


def g_shimmer(e):
    """Sines with slow tremolo (0.3-0.7 Hz), plus optional band noise [lo, hi] at noise_gain dB."""
    n = int(e["dur"] * SR)
    t = T(n)
    x = sum(np.sin(2 * np.pi * hz(f) * t) * (0.6 + 0.4 * np.sin(2 * np.pi * RNG.uniform(0.3, 0.7) * t + RNG.uniform(0, 6)))
            for f in notes(e["notes"]))
    x = norm(x)
    if e.get("noise"):
        x += norm(bp(noise(n), *e["noise"])) * db(e.get("noise_gain", -6))
    return x


def pluck_tone(f, dur, decay, bright=0.5):
    n = int(dur * SR)
    t = T(n)
    x = sum(np.sin(2 * np.pi * f * k * t) * np.exp(-t * k * (1 + 3 * (1 - bright)) / decay) / k ** 1.5 for k in range(1, 7))
    return x * env(n, 0.002, 0.05)


def g_pluck(e):
    """PLUCK. timbre piano (default): h 1..6, 1/h^1.3, decay e^-t(2.2+1.8h)/decay, inharmonic, hammer noise.
    timbre marimba: partials 1, 4, 9.2 with fast decays. timbre soft: the old pluck."""
    f, d = hz(e["note"]), e.get("decay", 1.0)
    tim = e.get("timbre", "piano")
    if tim == "soft":
        return norm(pluck_tone(f, d * 4, d, e.get("bright", 0.5)))
    n = int((1.5 + 2.5 * d) * SR)
    t = T(n)
    if tim == "marimba":
        x = sum(a * np.sin(2 * np.pi * f * r * t) * np.exp(-t / (dd * d)) for r, a, dd in ((1, 1, .5), (4, .35, .08), (9.2, .15, .03)))
        return norm(x * env(n, 0.001, 0.05))
    x = sum(np.sin(2 * np.pi * f * h * (1 + 0.0004 * h * h) * t) * np.exp(-t * (2.2 + 1.8 * h) / d) / h ** 1.3 for h in range(1, 7))
    k = int(0.005 * SR)
    x[:k] += lp(noise(k), 3000) * db(-18) * 3
    return norm(x * env(n, 0.002, 0.05))


def g_chime(e):
    """BELL (the Chime): FM, index 3.2 e^-t/0.6, ratio 1.4, amp e^-t/decay, + 2.76f partial; ±3 cents L/R (stereo)."""
    f, d = hz(e["note"]), e.get("decay", 2.2)
    n = int(d * 4 * SR)
    t = T(n)
    ch = []
    for c in (-3, 3):
        ff = f * 2 ** (c / 1200)
        idx = e.get("index", 3.2) * np.exp(-t / e.get("idecay", 0.6))
        y = np.sin(2 * np.pi * ff * t + idx * np.sin(2 * np.pi * e.get("ratio", 1.4) * ff * t)) * np.exp(-t / d)
        y += e.get("p2", 0.2) * np.sin(2 * np.pi * 2.76 * ff * t) * np.exp(-t / 0.7)
        ch.append(y * env(n, 0.002, 0.05))
    return norm(np.stack(ch, 1))


def g_bell(e):
    d = e.get("decay", 5.0)
    n = int(d * 3 * SR)
    t = T(n)
    f = hz(e.get("note", "A3"))
    x = sum(a * np.sin(2 * np.pi * f * r * t) * np.exp(-t / (d * dd)) for r, a, dd in
            [(1, 1, 1), (2.0, 0.6, 0.7), (2.76, 0.45, 0.5), (5.4, 0.25, 0.3), (8.93, 0.12, 0.15)])
    return norm(x * env(n, 0.001, 0.2))


def g_arp(e):
    n = int(e["dur"] * SR)
    x = np.zeros(n)
    step = 60 / e.get("bpm", 96) / (e.get("div", 4) / 4)  # div 4 = quarter notes, 8 = eighths
    ns = e["notes"]
    i, t0 = 0, 0.0
    while t0 < e["dur"]:
        place(x, pluck_tone(hz(ns[i % len(ns)]), e.get("decay", 0.3) * 4, e.get("decay", 0.3), e.get("bright", 0.6)), int(t0 * SR))
        i += 1
        t0 += step
    return norm(x)


def g_pulse(e):
    """PULSE: a sine thump on every beat (freq Hz, len 180 ms, e^-t/0.08) plus a soft click."""
    n = int(e["dur"] * SR)
    x = np.zeros(n)
    beat = 60 / e.get("bpm", 60)
    k = int(0.18 * SR)
    tt = T(k)
    thump = np.sin(2 * np.pi * hz(e.get("freq", 50)) * tt) * np.exp(-tt / 0.08) * env(k, 0.002, 0.02)
    thump[:int(0.002 * SR)] += lp(noise(int(0.002 * SR)), 4000) * 0.15
    t0 = 0.0
    while t0 < e["dur"] - 1e-6:
        place(x, thump, int(round(t0 * SR)))
        t0 += beat / e.get("per_beat", 1)
    return norm(x)


def g_hit(e):
    """SUB HIT: sine sweeping freq+42 -> freq Hz (e^-t/0.12), amp e^-t/0.9, 3 ms click; size scales the decay."""
    sz = e.get("size", 1.0)
    n = int(3 * sz * SR)
    t = T(n)
    f = hz(e.get("freq", 38))
    sub = np.sin(2 * np.pi * (f * t + 42 * 0.12 * (1 - np.exp(-t / 0.12)))) * np.exp(-t / (0.9 * sz))
    click = lp(noise(n), 5000) * np.exp(-t / 0.003) * e.get("click", 0.4)
    body = lp(noise(n), 300) * np.exp(-t / (0.4 * sz)) * e.get("body", 0.3)
    return norm(sub + click + body)


def g_riser(e):
    """RISER: noise band-pass sweeping 300 -> 6000 Hz, gain rising ~26 dB, plus a sine gliding D3 -> D5."""
    n = int(e["dur"] * SR)
    t = T(n)
    u = t / e["dur"]
    src = noise(n)
    cs = np.geomspace(300, 6000, 8)
    pos = u * 7
    x = sum(bp(src, c / 1.4, c * 1.4) * np.clip(1 - np.abs(pos - i), 0, 1) for i, c in enumerate(cs))
    x = norm(x) * db(-26 * (1 - u))
    f = hz("D3") * 4 ** u
    x += db(-16) * np.sin(2 * np.pi * np.cumsum(f) / SR) * db(-26 * (1 - u))
    return x * env(n, 0.01, 0.01)


def g_whoosh(e):
    n = int(e.get("dur", 0.8) * SR)
    t = T(n)
    u = t / t[-1]
    shape = np.sin(np.pi * u) ** 2
    x = np.zeros(n)
    blk = 2048
    src = noise(n)
    for s in range(0, n, blk):  # sweeping band-pass
        c = 300 + 3000 * shape[s]
        x[s:s + blk] = bp(src[s:s + blk], c * 0.5, c * 2)[:len(x[s:s + blk])]
    return norm(lp(x, 8000) * shape)


# ------------------------------------------------------------------ noise, ambience, SFX
def g_tone(e):
    """Sine or square at freq (gliding exponentially to `to`), with optional harmonics `harm` (amps for 1, 2, 3, ...)."""
    n = int(e["dur"] * SR)
    f0, f1 = hz(e.get("freq", 1000)), hz(e.get("to", e.get("freq", 1000)))
    f = f0 * (f1 / f0) ** (T(n) / e["dur"])
    ph = 2 * np.pi * np.cumsum(f) / SR
    if e.get("wave") == "square":
        x = np.sign(np.sin(ph))
    else:
        x = sum(a * np.sin(k * ph) for k, a in enumerate(e.get("harm", [1]), 1))
    return norm(x) * env(n, 0.003, 0.003)


def g_noise(e):
    """Noise: color white|pink|brown, band [lo, hi], sweep [f0, f1] (time-varying low-pass)."""
    n = int(e["dur"] * SR)
    x = colored(n, e.get("color", "white"))
    if e.get("band"):
        x = bp(x, *e["band"])
    if e.get("sweep"):
        x = sweep_lp(x, *e["sweep"])
    return norm(x)


def droplets(n, rate, lo=2000):
    x = (RNG.random(n) < rate / SR) * noise(n) * 4
    return hp(x, lo)


def g_bed(e):
    n = int(e["dur"] * SR)
    t = T(n)
    k = e.get("kind", "wind")
    nz = noise(n)
    slow = lambda hzz, seed=0: 0.5 + 0.5 * np.sin(2 * np.pi * hzz * t + seed) * np.sin(2 * np.pi * hzz * 0.37 * t + 2 * seed)
    f = hz(e.get("freq", 50))
    if k == "wind":
        x = bp(nz, 150, 1200) * (0.4 + 0.6 * slow(0.11)) + 0.3 * bp(noise(n), 900, 3000) * slow(0.23, 1)
    elif k == "rain":  # pink body + droplet transients (Poisson `drops`/s)
        x = norm(bp(colored(n, "pink"), 400, 9000)) + 0.5 * norm(droplets(n, e.get("drops", 40)))
    elif k == "room":
        x = lp(nz, 300) * 0.5 + 0.05 * np.sin(2 * np.pi * 60 * t)
    elif k == "city":
        x = lp(nz, 500) * (0.7 + 0.3 * slow(0.05)) + 0.2 * bp(noise(n), 1000, 3000) * slow(0.3, 2)
    elif k == "crowd":
        x = sum(bp(noise(n), 300, 2500) * slow(3 + i * 0.7, i) for i in range(6)) / 3
    elif k == "sea":
        x = bp(nz, 200, 4000) * (0.2 + 0.8 * (0.5 + 0.5 * np.sin(2 * np.pi * t / 7.0)) ** 3)
    elif k == "canal":  # slow lapping
        x = lp(nz, 600) * (0.3 + 0.7 * slow(0.35, 1) ** 2)
    elif k == "hum":
        x = sum(np.sin(2 * np.pi * f * h * t) / h for h in (1, 2, 3, 5)) * 0.5 + 0.1 * lp(nz, 200)
    elif k == "hall":  # the hall's mains hum and air
        x = norm(sum(np.sin(2 * np.pi * f * h * t) / h ** 1.5 for h in (1, 2, 3, 4))) + 0.7 * norm(lp(nz, 1000))
    elif k == "air":
        x = lp(nz, 1000) * (0.8 + 0.2 * slow(0.07))
    elif k == "hiss":  # broadcast / tape hiss
        x = hp(nz, 1500)
    elif k == "line":  # phone-line hiss
        x = norm(bp(nz, 300, 3400)) + 0.1 * np.sin(2 * np.pi * 50 * t)
    elif k == "tram":  # idle hum with motor whine
        x = np.sin(2 * np.pi * 100 * t) + 0.6 * np.sin(2 * np.pi * 200 * t) + 0.15 * np.sin(2 * np.pi * 1180 * t * (1 + 0.004 * np.sin(2 * np.pi * 0.8 * t)))
    elif k == "fire":
        x = lp(nz, 900) * 0.6 + (RNG.random(n) > 0.9985) * noise(n) * 4
    elif k == "static":
        x = bp(nz, 1000, 12000) * (0.7 + 0.3 * slow(1.5))
    else:
        raise ValueError(k)
    return norm(x)


def g_clock(e):
    """A clock ticking on every beat from `at`: kind hall (brass tick) or wood (900/800 Hz tick-tock).
    accent [[t, dB], ...] makes single ticks heavier."""
    n = int(e["dur"] * SR) + SR
    x = np.zeros(n)
    k = int(0.12 * SR)
    t = T(k)
    if e.get("kind", "hall") == "wood":
        ticks = [np.sin(2 * np.pi * f * t) * np.exp(-t / 0.015) + lp(noise(k), 3000) * np.exp(-t / 0.003) * 0.3 for f in (900, 800)]
    else:
        ticks = [sum(a * np.sin(2 * np.pi * f * s * t) * np.exp(-t / d) for f, a, d in ((1850, 1, .02), (3120, .6, .012), (4700, .35, .008), (420, .5, .03)))
                 + hp(noise(k), 2000) * np.exp(-t / 0.002) * 0.6 for s in (1, 0.96)]
    acc = {round(a, 2): g for a, g in e.get("accent", [])}
    beat = 60 / e.get("bpm", 60)
    i = 0
    while i * beat < e["dur"] - 1e-6:
        g = db(acc.get(round(e["at"] + i * beat, 2), 0))
        place(x, norm(ticks[i % 2]) * g * (1 if i % 2 == 0 else 0.85), int(round(i * beat * SR)))
        i += 1
    return x[:int(e["dur"] * SR) + k]


def g_phone(e):
    """One ring. kind red: 1080/1350 Hz bells (partials x1, x2.4, x3.9, decay 0.3), 20 Hz clapper, 1.2 s.
    kind nana: 800/1000 Hz, 25 Hz clapper, 0.4 on / 0.2 off / 0.4 on."""
    red = e.get("kind", "red") == "red"
    fa, fb, rate = (1080, 1350, 20) if red else (800, 1000, 25)
    on = [(0, 1.2)] if red else [(0, 0.4), (0.6, 1.0)]
    n = int((on[-1][1] + 0.8) * SR)
    ta, tb = np.zeros(n), np.zeros(n)
    for a, b in on:
        for j, s in enumerate(np.arange(a, b, 1 / rate)):
            (ta if j % 2 == 0 else tb)[int(s * SR)] = 1 + 0.15 * RNG.normal()
    k = int(0.8 * SR)
    t = T(k)
    ir = lambda f: sum(w * np.sin(2 * np.pi * f * r * t) * np.exp(-t / 0.3 / r ** 0.5) for r, w in ((1, 1), (2.4, .5), (3.9, .3)))
    conv = lambda a, b: np.fft.irfft(np.fft.rfft(a, 2 * n) * np.fft.rfft(b, 2 * n), 2 * n)[:n]
    return norm(np.tanh(norm(conv(ta, ir(fa)) + conv(tb, ir(fb))) * 1.5))


def click(kind):
    """One small mechanical sound."""
    j = RNG.uniform(0.95, 1.05)  # pitch jitter
    if kind in ("key", "tab"):
        k = int(0.12 * SR)
        t = T(k)
        f, d = (180, 0.03) if kind == "key" else (130, 0.06)
        burst = bp(noise(k), 1000, 4000) * np.exp(-t / 0.002) * (t < 0.008)
        return norm(burst * (0.6 if kind == "key" else 0.4) + np.sin(2 * np.pi * f * j * t) * np.exp(-t / d))
    if kind == "crinkle":
        L = int(RNG.uniform(0.02, 0.08) * SR)
        return norm(bp(noise(L), 2000, 6000) * np.hanning(L) * (0.5 + RNG.random(L)))
    if kind == "bubble":
        L = int(0.04 * SR)
        t = T(L)
        return norm(np.sin(2 * np.pi * RNG.uniform(250, 600) * t * (1 + 3 * t)) * np.hanning(L))
    if kind == "drip":
        L = int(0.12 * SR)
        t = T(L)
        f = RNG.uniform(2000, 4000) * j
        drip = np.sin(2 * np.pi * f * (t - 8 * t * t)) * np.exp(-t / 0.006)
        plop = np.sin(2 * np.pi * 160 * j * t) * np.exp(-t / 0.02) * 0.4
        return norm(drip + plop)
    L = int(0.06 * SR)
    t = T(L)
    ping = {"stylus": (3000, 0.004), "mouse": (1500, 0.006), "relay": (2000, 0.04), "track": (4000, 0.0005),
            "gen": (2400, 0.003), "handset": (320, 0.02)}[kind]
    burst = hp(noise(L), 1500) * np.exp(-t / 0.0007)
    body = np.sin(2 * np.pi * ping[0] * j * t) * np.exp(-t / ping[1])
    if kind == "handset":
        body += lp(noise(L), 1500) * np.exp(-t / 0.01) * 0.8
    return norm(burst * 0.7 + body)


def g_clicks(e):
    """kind key|tab|stylus|mouse|relay|track|gen|crinkle|bubble|drip|handset. One click, or `count` clicks over
    `dur`: rate0 given -> the rate changes linearly so exactly `count` land in `dur`; else random (Poisson-ish)."""
    kind = e.get("kind", "key")
    if not e.get("count"):
        return click(kind) * db(RNG.uniform(-3, 3))
    dur, c = e["dur"], e["count"]
    if e.get("rate0") is not None:  # C(t) = r0 t + b t^2
        r0 = e["rate0"]
        b = (c - r0 * dur) / dur ** 2
        ons = [((-r0 + np.sqrt(r0 * r0 + 4 * b * i)) / (2 * b)) if abs(b) > 1e-9 else i / r0 for i in range(c)]
    else:
        ons = np.sort(RNG.uniform(0, dur, c))
    x = np.zeros(int((dur + 0.2) * SR))
    for o in ons:
        place(x, click(kind) * db(RNG.uniform(-3, 3)), int(o * SR))
    return norm(x)


def g_clank(e):
    """Pneumatic capsule landing: 60 Hz whump e^-t/0.15 + metal partials 520/1370/2210/3140 Hz."""
    n = int(1.5 * SR)
    t = T(n)
    x = np.sin(2 * np.pi * 60 * t) * np.exp(-t / 0.15)
    x += sum(a * np.sin(2 * np.pi * f * t) * np.exp(-t / d) for f, a, d in ((520, .5, .6), (1370, .4, .35), (2210, .3, .2), (3140, .25, .12)))
    x += lp(noise(n), 3000) * np.exp(-t / 0.01) * 0.5
    return norm(x)


def g_breath(e):
    """Breath: noise BP 300-3000 with a soft envelope; voiced adds a shaky 150 Hz buzz (a laugh-sob)."""
    n = int(e.get("dur", 0.6) * SR)
    t = T(n)
    shape = np.sin(np.pi * t / t[-1]) ** 1.5
    x = norm(bp(noise(n), 300, 3000)) * shape
    if e.get("voiced"):
        buzz = sum(np.sin(2 * np.pi * 150 * k * t * (1 + 0.02 * np.sin(2 * np.pi * 6 * t))) / k for k in range(1, 12))
        x += 0.6 * norm(lp(buzz, 1800)) * shape * (0.5 + 0.5 * np.sin(2 * np.pi * 5 * t) ** 2)
    return norm(x)


def g_birds(e):
    """Sparse FM chirps (3-6 kHz sweeps, 60-120 ms) from 2-3 birds; stereo."""
    n = int(e["dur"] * SR)
    x = np.zeros((n + SR, 2))
    birds = [(RNG.uniform(3000, 4500), RNG.uniform(-0.7, 0.7)) for _ in range(e.get("birds", 3))]
    for _ in range(e.get("count", 20)):
        f, pan = birds[RNG.integers(len(birds))]
        s = RNG.uniform(0, e["dur"])
        for j in range(RNG.integers(1, 4)):  # a little phrase
            L = int(RNG.uniform(0.06, 0.12) * SR)
            t = T(L)
            ff = f * (1 + RNG.uniform(0.2, 0.5) * t / t[-1] * RNG.choice([-1, 1]))
            y = np.sin(2 * np.pi * np.cumsum(ff) / SR + 2 * np.sin(2 * np.pi * 40 * t)) * np.hanning(L)
            place(x, stereo(y, pan), int((s + j * 0.14) * SR))
    return norm(x)


def g_blip(e):
    one = int(0.06 * SR)
    t = T(one)
    tone = np.sin(2 * np.pi * hz(e.get("note", e.get("freq", 1800))) * t) * np.exp(-t * 60) * env(one, 0.002, 0.005)
    cnt, gap = e.get("count", 1), e.get("gap", 0.1)
    x = np.zeros(int((cnt * gap + 0.1) * SR))
    for i in range(cnt):
        place(x, tone, int(i * gap * SR))
    return norm(x)


def g_glitch(e):
    n = int(e.get("dur", 0.4) * SR)
    x = np.zeros(n)
    s = 0
    while s < n:
        L = int(RNG.uniform(0.005, 0.04) * SR)
        kind = RNG.integers(3)
        seg = noise(L) if kind == 0 else np.sign(np.sin(2 * np.pi * RNG.uniform(200, 3000) * T(L)))
        if kind == 2:
            seg *= 0
        x[s:s + L] = seg[:len(x[s:s + L])]
        s += L
    x = np.round(x * 4) / 4  # bit-crush
    return norm(bp(x, 100, 10000))


def g_heartbeat(e):
    n = int(e["dur"] * SR)
    x = np.zeros(n)
    beat = 60 / e.get("bpm", 60)
    k = int(0.25 * SR)
    tt = T(k)
    thump = np.sin(2 * np.pi * 50 * tt) * np.exp(-tt * 25)
    t0 = 0.0
    while t0 < e["dur"]:
        for off, a in ((0, 1.0), (0.28, 0.6)):
            place(x, a * thump, int((t0 + off) * SR))
        t0 += beat
    return norm(lp(x, 200))


def g_tick(e):
    n = int(e["dur"] * SR)
    x = np.zeros(n)
    k = int(0.02 * SR)
    clk = bp(noise(k), 2000, 8000) * np.exp(-T(k) * 400)
    beat = 60 / e.get("bpm", 60)
    t0, i = 0.0, 0
    while t0 < e["dur"]:
        place(x, clk * (1 if i % 2 == 0 else 0.7), int(t0 * SR))
        t0 += beat
        i += 1
    return norm(x)


def g_file(e):
    x = load_file(e)
    if e.get("trim"):
        x = trim_silence(x)
    e["_dur"] = len(x) / SR
    if e.get("norm"):  # dialogue from a file, levelled exactly like a say line
        x = speech_norm(x, -20.0 if e["norm"] is True else e["norm"])
    return x


GEN = {k[2:]: v for k, v in globals().items() if k.startswith("g_")}
MUSIC = {"drone", "pad", "hymn", "brass", "chime", "bell", "pluck", "arp", "shimmer", "pulse", "hit", "riser"}
DEFAULT_BUS = {"say": "dx", "loop": "dx", "walla": "walla", "bed": "amb", **{k: "mx" for k in MUSIC}}


def reverb(st, wet, decay=1.8, pre=0.0, cutoff=6000):
    """Stereo reverb: exponentially decaying noise IR (RT60 = decay), decorrelated L/R, predelay, low-passed."""
    n, p = int(decay * SR), int(pre * SR)
    m = len(st) + n + p
    L = 1 << (m - 1).bit_length()
    out = np.zeros((m, 2))
    out[:len(st)] = st * (1 - wet)
    for c in range(2):
        ir = lp(noise(n) * np.exp(-T(n) * 6.9 / decay), cutoff)
        ir = np.concatenate([np.zeros(p), ir / np.sqrt((ir ** 2).sum())])
        out[:, c] += np.fft.irfft(np.fft.rfft(st[:, c], L) * np.fft.rfft(ir, L), L)[:m] * wet * 1.5
    return out


# ------------------------------------------------------------------ timeline
def resolve(e, presets):
    uses = e.get("use", [])
    out = {}
    for u in [uses] if isinstance(uses, str) else uses:
        out.update(resolve(presets[u], presets))
    out.update({k: v for k, v in e.items() if k != "use"})
    return out


def expand(e):
    """seq [[t, note(, dB)], ...] / times [t | [t, dB], ...] / times_from (JS keystroke log) -> one event per item."""
    if "times_from" in e:
        log = json.loads((ROOT / e["times_from"]).read_text())
        e = {**e, "times": [k["abs"] for k in log if k.get("kind") in e.get("only", ["char"])]}
        del e["times_from"]
    items = e.get("seq") or e.get("times")
    if not items:
        return [e]
    base = {k: v for k, v in e.items() if k not in ("seq", "times")}
    out = []
    for it in items:
        it = it if isinstance(it, list) else [it]
        c = dict(base, at=it[0], gain=base.get("gain", -12) + (it[-1] if len(it) > (2 if "seq" in e else 1) else 0))
        if "seq" in e:
            c["note"] = it[1]
        out.append(c)
    return out


def keyframes(ts, kf, fn=lambda v: v):
    """Piecewise-linear automation [[t, v], ...] (absolute) sampled at absolute times ts."""
    kf = sorted(kf)
    return fn(np.interp(ts, [k[0] for k in kf], [k[1] for k in kf]))


def render(e, spec, mute_env):
    x = GEN[e["type"]](e)
    if e.get("wide") and x.ndim == 1:
        x = np.stack([x, GEN[e["type"]](e)], 1)
    if e.get("hpf"):
        x = hp(x, e["hpf"])
    if e.get("lpf"):
        x = lp(x, e["lpf"])
    x = stereo(x * db(e.get("gain", -12)), e.get("pan", 0))
    fi, fo = e.get("fade", [0, 0])
    if fi or fo:
        x = x * env(len(x), fi, fo)[:, None]
    if e.get("slap"):
        d, g = e["slap"]
        y = np.zeros((len(x) + int(d * SR), 2))
        y[:len(x)] += x
        y[int(d * SR):] += x * db(g)
        x = y
    if e.get("reverb"):
        x = reverb(x, e["reverb"], e.get("rt60", 1.8), e.get("predelay", 0.0), e.get("rcut", 6000))
    at = e["at"]
    ts = at + T(len(x))
    if e.get("glide"):
        t0, t1, semis = e["glide"]
        ratio = 2 ** (semis * np.clip((ts - t0) / (t1 - t0), 0, 1) / 12)
        x = warp(x, np.concatenate([[0], np.cumsum(ratio)[:-1]]))
    ts_ = spec.get("tapestop")
    if ts_ and at < ts_["at"] < ts[-1]:
        a, d = int((ts_["at"] - at) * SR), ts_["dur"]
        tau = T(int(d * SR))
        pos = a + (tau - tau ** 3 / (3 * d * d)) * SR
        x = np.concatenate([x[:a], warp(x, pos)])
        ts = ts[:len(x)]
    if e.get("auto"):
        x = x * keyframes(ts, e["auto"], db)[:, None]
    if e.get("spans"):
        g = np.zeros(len(x))
        for sp in e["spans"]:
            a, b = np.searchsorted(ts, sp[0]), np.searchsorted(ts, sp[1])
            g[a:b] = db(sp[2] if len(sp) > 2 else 0)
        k = int(0.003 * SR)  # ramps end on the span edges, so a tick on a cut keeps its attack
        x = x * np.convolve(g, np.ones(k) / k, "full")[k - 1:k - 1 + len(g)][:, None]
    s = int(round(at * SR))
    if not e.get("nomute"):
        m = np.ones(len(x))
        seg = mute_env[max(0, s):s + len(x)]
        m[max(0, -s):max(0, -s) + len(seg)] = seg
        x = x * m[:, None]
    return x, s


def mute_envelope(N, mutes):
    m = np.ones(N)
    r, ri = int(0.003 * SR), int(0.001 * SR)
    for a, b in mutes:
        a, b = int(a * SR), int(b * SR)
        m[a:b] = 0
        m[max(0, a - r):a] *= np.linspace(1, 0, len(m[max(0, a - r):a]))
        m[b:b + ri] *= np.linspace(0, 1, len(m[b:b + ri]))
    return m


def duck_env(key, attack=0.04, release=0.3, thr=-45):
    """Gate on the key bus at 1 kHz frames, smoothed with attack/release; returns 0..1 per sample."""
    fr = SR // 1000
    n = len(key) // fr
    lvl = np.abs(key[:n * fr]).max(1).reshape(n, fr).max(1)
    gate = (lvl > db(thr)).astype(float)
    ca, cr = 1 - np.exp(-1 / (attack * 1000)), 1 - np.exp(-1 / (release * 1000))
    out, y = np.zeros(n), 0.0
    for i, g in enumerate(gate):
        y += (g - y) * (ca if g > y else cr)
        out[i] = y
    full = np.zeros(len(key))
    full[:n * fr] = np.repeat(out, fr)
    return full


def limit(x, ceiling):
    """Look-ahead peak limiter (5 ms look-ahead, 80 ms release) on 1 ms frames."""
    fr = SR // 1000
    n = -(-len(x) // fr)
    pk = np.zeros(n * fr)
    pk[:len(x)] = np.abs(x).max(1)
    need = np.minimum(1, ceiling / (pk.reshape(n, fr).max(1) + 1e-12))
    la = 5
    need = np.min(np.stack([np.roll(need, -i) for i in range(la + 1)]), 0)
    g, y = np.ones(n), 1.0
    cr = 1 - np.exp(-1 / 80)
    for i, v in enumerate(need):
        y = v if v < y else y + (v - y) * cr
        g[i] = y
    gs = np.interp(np.arange(len(x)) / fr - 0.5, np.arange(n), g)
    return x * gs[:, None]


def write(path, a, codec="pcm_s24le"):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", codec, str(path)],
                   input=a.astype(np.float32).tobytes(), check=True)


def loudness(path):
    """Integrated loudness, LRA and true peak via ffmpeg ebur128."""
    r = subprocess.run(["ffmpeg", "-nostats", "-i", str(path), "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    summ = r[r.rfind("Summary:"):]
    get = lambda k: float(re.search(k + r":\s+(-?[\d.]+|-inf)", summ).group(1))
    return {"I": get("I"), "LRA": get("LRA"), "TP": get("Peak")}


def main():
    spec_path = Path(sys.argv[1])
    spec = json.loads(spec_path.read_text())
    global CACHE
    CACHE = ROOT / spec.get("cache", "work/audio_cache")
    presets = spec.get("presets", {})
    busmap = {**DEFAULT_BUS, **spec.get("bus_of", {})}
    N = int(spec["dur"] * SR)
    mute_env = mute_envelope(N, spec.get("mutes", []))
    buses = {}  # name -> [ducked, unducked]
    lines = []
    for raw in spec["events"]:
        if "type" not in raw and "use" not in raw:  # {"//": "comment"} section markers
            continue
        for e in expand(resolve(raw, presets)):
            if e["at"] >= spec["dur"]:
                continue
            x, s = render(e, spec, mute_env)
            bus = e.get("bus", busmap.get(e["type"], "fx"))
            pair = buses.setdefault(bus, [np.zeros((N, 2)), np.zeros((N, 2))])
            place(pair[1 if e.get("noduck") else 0], x, s)
            if e["type"] == "say" or (e["type"] == "file" and e.get("id")):
                lines.append(e)
    duck = spec.get("duck", {"key": "dx", "mx": -4})
    if duck.get("key") in buses:
        k = duck_env(sum(buses[duck["key"]]))
        for name, g in duck.items():
            if name != "key" and name in buses:
                buses[name][0] *= (1 - (1 - db(g)) * k)[:, None]
    buses = {k: v[0] + v[1] for k, v in buses.items()}
    mix = sum(buses.values())

    # loudness: measure, apply one static gain, look-ahead limit to the true-peak ceiling
    out = ROOT / spec["out"]
    out.parent.mkdir(parents=True, exist_ok=True)
    tp = spec.get("tp", -1.0)
    if spec.get("gain_db") is None:
        tmp = out.with_suffix(".tmp.wav")
        write(tmp, mix, "pcm_f32le")
        gain = spec.get("lufs", -16) - loudness(tmp)["I"]
        tmp.unlink()
    else:
        gain = spec["gain_db"]
    final = limit(mix * db(gain), db(tp - 0.8))
    write(out, final)
    if spec.get("stems"):
        for name, b in buses.items():
            write(out.with_suffix(f".{name}.wav"), b * db(gain), "pcm_f32le")  # float: stems are not limited
    L = loudness(out)
    print(f"{out.relative_to(ROOT)}  {spec['dur']:.1f} s  gain {gain:+.2f} dB  I {L['I']} LUFS  LRA {L['LRA']} LU  TP {L['TP']} dBTP")
    print("  bus peaks (dBFS after gain):", {k: float(round(20 * np.log10(np.abs(v).max() * db(gain) + 1e-12), 1)) for k, v in buses.items()})

    # dialogue report: every line against its shot
    cuts = sorted(spec.get("cuts", []))
    subs = []
    for e in sorted(lines, key=lambda e: e["at"]):
        end = e["at"] + e["_dur"]
        nxt = next((c for c in cuts if c > e["at"] + 1e-6), spec["dur"])
        flag = "" if end <= nxt else f"  OVERRUN by {end - nxt:.2f} s" + (" (cut by design)" if e.get("overrun_ok") else "")
        if e.get("id"):
            print(f"  {e['id']:4} {e['at']:7.2f} +{e['_dur']:.2f} -> {end:7.2f}  shot ends {nxt:6.1f}  "
                  f"margin {nxt - end:+.2f}{flag}  {Path(e['path']).name if e['type'] == 'file' else f"{e.get('voice')} {e.get('rate')}"}  {e['text'][:40]}")
        if e.get("sub", True) is not False and e.get("id"):
            subs.append({"start": round(e.get("sub_start", e["at"]), 2), "end": round(e.get("sub_end", end + 0.3), 2),
                         "text": e.get("sub", e["text"]), **({"italic": True} if e.get("italic") else {})})
    for a, b in zip(subs, subs[1:]):
        a["end"] = round(min(a["end"], b["start"] - 0.05), 2)
    if spec.get("subs"):
        p = ROOT / spec["subs"]
        p.write_text(json.dumps(subs, indent=1, ensure_ascii=False) + "\n")
        print(f"  {len(subs)} subtitles -> {p.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
