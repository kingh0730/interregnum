"""QA the v4 pilot mix by metrics (mix_plan.md 9): loudness per scene against the level table, true peak, bus peaks,
dialogue levels and sync, every sfx placement present, the A, the silences, and spectrogram checks at key moments.

usage: uv run tools/audio/qa_mix.py [work/pilot/audio/v4/mix.json]   -> prints, and writes <out>.qa.json
Claude cannot listen: these are numbers, not a judgement of how it sounds.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mix2  # noqa: E402
import rooms as R  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SR = 48000

# mix_plan.md 6: scene, span, dialogue target, bed target (the scene's loudest bed, LUFS-S), music target
SCENES = [
    ("Cold open", 0.0, 19.4, "Father -17 (BCAST)", None, "M1 -30 under the voice, -24 at 4.8"),
    ("Freeze", 19.0, 22.0, None, None, None),
    ("Night desk", 22.0, 54.0, "D05 -21", -38, None),
    ("No agreement", 54.0, 77.0, "D08 -18; PA -19; loop to -9 at 70.2", -38, None),
    ("The warm window", 77.0, 109.4, "Ida -18, Nana -17", -30, None),
    ("Sign-offs", 109.0, 117.0, None, -40, "M2 -24"),
    ("Night 212", 117.0, 149.0, "PA -19", -38, "M3 -40 -> -12"),
    ("The Address", 149.3, 180.0, "Father -17 / -19 / -15 / -22", -30, "ident chord; M2 from 177.5"),
    ("Dead air", 180.0, 186.0, None, -50, None),
    ("Come home", 186.0, 217.0, "Ida -18, Nana -17, D26 -17", -42, "M4 -24 from 210"),
    ("Empty hall", 217.0, 223.0, None, -40, "M4 -30"),
    ("First light", 223.0, 233.0, "walla -44 -> -30; W01/W02 -24", -40, "M4 -20 -> -14 at 231"),
    ("Titles", 233.0, 242.0, None, None, "M4 -28, last chord -22"),
]


def load(p):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(p), "-f", "f32le", "-ac", "2", "-ar", str(SR), "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).astype(np.float64)


def ebur(p):
    r = subprocess.run(["ffmpeg", "-nostats", "-i", str(p), "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    s = r[r.rfind("Summary:"):]
    g = lambda k: float(re.search(k + r":\s+(-?[\d.]+|-inf)", s).group(1))
    return {"I": g("I"), "LRA": g("LRA"), "TP": g("Peak")}


def seg(x, a, b):
    return x[int(a * SR):int(b * SR)]


def st_stats(x, a, b):
    st = R.st_curve(seg(x, max(0, a - 1.5), b + 1.5))
    st = st[15:-15] if len(st) > 30 else st
    st = st[st > -90]
    if not len(st):
        return None
    return {"median": round(float(np.median(st)), 1), "max": round(float(st.max()), 1), "min": round(float(st.min()), 1)}


def spec_peak(x, a, b, lo, hi, n=1 << 17):
    m = R.mono(seg(x, a, b))
    X = np.abs(np.fft.rfft(m * np.hanning(len(m)), n))
    f = np.fft.rfftfreq(n, 1 / SR)
    sel = np.where((f > lo) & (f < hi))[0]
    k = sel[np.argmax(X[sel])]
    a_, b_, c_ = np.log(X[k - 1:k + 2] + 1e-12)
    fp = (k + 0.5 * (a_ - c_) / (a_ - 2 * b_ + c_)) * SR / n
    return fp, 20 * np.log10(X[k] / (np.sqrt((X ** 2).mean()) + 1e-12))


def band_db(x, a, b, lo, hi):
    m = R.mono(seg(x, a, b))
    X = np.abs(np.fft.rfft(m)) ** 2
    f = np.fft.rfftfreq(len(m), 1 / SR)
    return 10 * np.log10(X[(f >= lo) & (f < hi)].sum() / max(1, len(m)) + 1e-20)


def flux_onsets(x, a, b, hop=0.01, win=0.04):
    """Spectral-flux onsets (positive log-magnitude change summed over 150 Hz-8 kHz) -> [(t, strength z-score)]."""
    a0 = max(0.0, a - 0.5)
    m = R.mono(seg(x, a0, b + 0.5))
    N, H = int(win * SR), int(hop * SR)
    w = np.hanning(N)
    fr = np.array([np.abs(np.fft.rfft(m[i:i + N] * w)) for i in range(0, len(m) - N, H)])
    f = np.fft.rfftfreq(N, 1 / SR)
    sel = (f > 150) & (f < 8000)
    lf = np.log(fr[:, sel] + 1e-7)
    fl = np.concatenate([[0], np.maximum(np.diff(lf, axis=0), 0).sum(1)])
    t = a0 + (np.arange(len(fl)) * H + N / 2) / SR
    z = (fl - np.median(fl)) / (np.std(fl) + 1e-9)
    return t, z


def main():
    spec_path = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "work/pilot/audio/v4/mix.json")
    spec = json.loads(spec_path.read_text())
    out = ROOT / spec["out"]
    rep = json.loads(out.with_name(out.stem + ".report.json").read_text())
    x = load(out)
    stems = {b: load(out.with_name(f"{out.stem}.{b}.wav")) for b in ("dx", "bcast", "fx", "amb", "mx", "walla")
             if out.with_name(f"{out.stem}.{b}.wav").exists()}
    q = {"file": str(out.relative_to(ROOT)), "duration_s": round(len(x) / SR, 3)}
    q["ebur128"] = ebur(out)
    q["ebur128_ok"] = {"I -16 +-0.5": abs(q["ebur128"]["I"] + 16) <= 0.5, "TP <= -1.0": q["ebur128"]["TP"] <= -1.0,
                       "LRA 12-16": 12 <= q["ebur128"]["LRA"] <= 16}
    q["master"] = rep.get("master")
    # gain reduction by time (limiter), from the float master vs the float stems' sum
    mix = sum(stems.values())
    fin = load(out.with_name(out.stem + ".f32.wav"))
    k = int(0.01 * SR)
    n = min(len(mix), len(fin)) // k
    pm = np.abs(mix[:n * k]).max(1).reshape(n, k).max(1)
    pf = np.abs(fin[:n * k]).max(1).reshape(n, k).max(1)
    gr = 20 * np.log10((pm + 1e-9) / (pf + 1e-9))
    gr[pm < 1e-5] = 0
    bad = [(round(i * 0.01, 2), round(float(gr[i]), 1)) for i in np.nonzero(gr > 2.0)[0]]
    allowed = lambda t: 69.9 <= t <= 70.4 or 148.5 <= t <= 149.08
    q["limiter"] = {"max_gr_db": round(float(gr.max()), 2), "frames_over_2db": len(bad),
                    "over_2db_outside_allowed": [b for b in bad if not allowed(b[0])][:40]}

    # scenes
    sc = []
    for name, a, b, dxt, bed, mus in SCENES:
        r = {"scene": name, "span": [a, b], "master_st": st_stats(x, a, b)}
        seg_i = R.integrated(seg(x, a, b))
        r["master_I"] = round(float(seg_i), 1)
        if "amb" in stems:
            r["beds_st"] = st_stats(stems["amb"], a, b)
            r["bed_target"] = bed
        if "mx" in stems:
            r["music_st"] = st_stats(stems["mx"], a, b)
            r["music_target"] = mus
        r["dialogue_target"] = dxt
        sc.append(r)
    q["scenes"] = sc

    # dialogue: each line's loudness over its voiced span in its stem (bcast lines include the carrier/M1 under them)
    # dialogue: each line rendered alone at the master gain, read as the plan reads it (the loudest 3 s short-term)
    plan_t = {l["id"]: l for l in json.loads((ROOT / "audio/pilot/dialogue.json").read_text())["lines"]}
    base = {"D": -17, "V": None}
    lines = []
    g_master = R.db(rep["master"]["gain_db"])
    for l in rep["lines"]:
        if l.get("missing"):
            lines.append({"id": l["id"], "missing": True})
            continue
        r = mix2.Renderer(spec)
        y = sum(b.astype(np.float64) for b in r.render([l["id"]]).values()) * g_master
        a, b = l["onset"], max(l["voiced_end"], l["onset"] + 0.3)
        S = R.st_curve(seg(y, a - 1.5, b + 1.5)).max()
        L = R.span_loudness(seg(y, a, b))
        lines.append({"id": l["id"], "target_premaster": l["target"], "st3_master": round(float(S), 1), "span_master": round(float(L), 1),
                      "onset_vs_plan_ms": round((l["onset"] - l["planned"]) * 1000), "voiced_end": l["voiced_end"],
                      "end_by": l.get("end_by"), "notes": l.get("notes")})
    q["lines"] = lines
    d25 = next((l for l in lines if l["id"] == "D25"), None)
    d26 = next((l for l in lines if l["id"] == "D26"), None)
    if d25 and d26:
        q["D26_not_quieter_than_D25"] = [d25["st3_master"], d26["st3_master"], d26["st3_master"] >= d25["st3_master"] - 0.05]
    d20a = next(l for l in rep["lines"] if l["id"] == "D20a")
    d20b = next(l for l in rep["lines"] if l["id"] == "D20b")
    q["D20_pause_straddles_168"] = {"tomorrow_ends": d20a["voiced_end"], "rest_starts": d20b["onset"],
                                    "ok": d20a["voiced_end"] <= 167.98 and d20b["onset"] >= 168.15}

    # every sfx placement present
    ev = {e["id"]: e for e in rep["events"]}
    pres, absent, other = 0, [], {}
    for key, how in spec["sfx_placements"]["realised"].items():
        if how != "event":
            other[key] = how
            continue
        es = [e for e in rep["events"] if key in e.get("placements", [])]
        if es and max(e.get("peak") or -200 for e in es) > -90:
            pres += 1
        else:
            absent.append(key)
    q["sfx_placements"] = {"total_in_sfx_json": spec["sfx_placements"]["total"], "rendered_as_events": pres,
                           "absent": absent, "realised_otherwise": other}
    q["placeholders"] = rep.get("placeholders")

    # the silences
    def zero(a, b):
        s = seg(x, a + 0.004, b - 0.004)
        return round(float(20 * np.log10(np.abs(s).max() + 1e-12)), 1)
    q["silences"] = {
        "signal gap 19.4-20.0 peak dBFS": zero(19.4, 20.0),
        "HALT black 70.40-71.00 peak dBFS": zero(70.40, 71.00),
        "commit black 149.08-149.30 peak dBFS": zero(149.08, 149.30),
        "end 241.6-242.0 peak dBFS": zero(241.6, 242.0),
        "dead air 180-186": {"st": st_stats(x, 180.2, 185.8), "LR_corr": round(float(np.corrcoef(*seg(x, 180.1, 185.9).T)[0, 1]), 4),
                             "tonal_peak_over_noise_db": round(spec_peak(x, 180.2, 185.8, 40, 12000)[1], 1),
                             "only the carrier (other buses peak dBFS)": {b: round(float(20 * np.log10(np.abs(seg(s, 180.01, 185.99)).max() + 1e-12)), 1)
                                                                          for b, s in stems.items() if b != "bcast"}},
        "held breath 45.6-47.1: ambience momentary max, 44.6-45.5 vs 45.9-46.9": [
            round(float(R.st_curve(seg(stems["amb"], 44.6, 45.5), win=0.4).max()), 1),
            round(float(R.st_curve(seg(stems["amb"], 45.9, 46.9), win=0.4).max()), 1)],
    }

    # spectrogram checks
    chk = {}
    amb = stems["amb"]

    def solo(ids):  # re-render single events (the stems mix every bed of a bus together)
        r = mix2.Renderer(spec)
        return sum(b.astype(np.float64) for b in r.render(ids).values()) * R.db(rep["master"]["gain_db"])
    hum = solo(["H02"])
    tr = []
    for t0 in np.arange(185.8, 188.0, 0.2):
        fp, _ = spec_peak(hum, t0, t0 + 0.2, 15, 130, n=1 << 16)
        tr.append([round(float(t0), 1), round(float(fp), 1), round(float(20 * np.log10(np.abs(seg(hum, t0, t0 + 0.2)).max() + 1e-12)), 1)])
    chk["1 the Engine's hum dying 186.4-187.8 (H02 solo) [t, peak Hz 15-130, peak dBFS]"] = tr
    chk["1b the Hall after 186.4: A2 band 106-114 Hz dB in the ambience stem, 168.5-173.5 vs 188-198"] = [
        round(band_db(amb, 168.5, 173.5, 106, 114), 1), round(band_db(amb, 188.0, 198.0, 106, 114), 1)]
    nb = stems["dx"] + stems["fx"] + stems["mx"] + stems["walla"] + stems["bcast"]
    t, z = flux_onsets(nb, 233.0, 238.0)
    win = (t >= 234.3) & (t <= 234.9)
    tm, zm = flux_onsets(stems["mx"], 233.0, 238.0)
    wm = (tm >= 234.3) & (tm <= 234.9)
    chk["2 the withheld E-flat 234.3-234.9 (spectral flux z-scores over 233-238)"] = {
        "non-bed buses: max z in window": round(float(z[win].max()), 2),
        "non-bed buses: z at the chime 233.5 / 234.0 / letterpress 238.0": [round(float(z[np.argmin(np.abs(t - v))]), 1) for v in (233.5, 234.0, 237.99)],
        "music stem: max z in window": round(float(zm[wm].max()), 2),
        "onsets z>3 in window (non-bed buses)": [round(float(v), 3) for v in t[win][z[win] > 3]],
        "Eb4 / Eb5 bands (305-317, 616-628 Hz) dB, 234.0-234.3 vs 234.3-234.9 (master)": [
            round(band_db(x, 234.0, 234.3, 305, 317), 1), round(band_db(x, 234.3, 234.9, 305, 317), 1),
            round(band_db(x, 234.0, 234.3, 616, 628), 1), round(band_db(x, 234.3, 234.9, 616, 628), 1)]}
    fe, _ = spec_peak(amb, 30.0, 44.0, 106, 114, n=1 << 21)
    tv = solo(["N04"])
    ft, _ = spec_peak(tv, 84.2, 89.8, 106, 114, n=1 << 21)
    fm, _ = spec_peak(stems["mx"], 131.0, 145.0, 214, 226, n=1 << 21)
    c = lambda f, ref: round(1200 * np.log2(f / ref), 1)
    cs = [c(fe, 110), c(ft, 110), c(fm, 220)]
    chk["3 the A (Hz, cents from 110 / 220 Hz)"] = {"Engine hum A2 (30-44 s)": [round(fe, 3), cs[0]],
                                                    "TV hum A2 (N04 solo, 84-90 s)": [round(ft, 3), cs[1]],
                                                    "M3 A3 (131-145 s)": [round(fm, 3), cs[2]],
                                                    "max spread cents": round(max(cs) - min(cs), 1), "ok (<= 5 c)": max(cs) - min(cs) <= 5}
    tram = solo(["C04"])
    tr = []
    for t0 in np.arange(158.2, 159.8, 0.2):
        fp, _ = spec_peak(tram, t0, t0 + 0.2, 60 if t0 >= 158.9 else 380, 700, n=1 << 16)
        tr.append([round(float(t0), 1), round(float(fp), 1), round(float(20 * np.log10(np.abs(seg(tram, t0, t0 + 0.2)).max() + 1e-12)), 1)])
    chk["4 the tram's A dying 158.8-159.6 (C04 solo) [t, whine peak Hz (380-700 before 158.9, 60-700 after), peak dBFS]"] = tr
    cen = []
    bc = stems["bcast"]
    for t0 in np.arange(18.6, 19.5, 0.1):
        m = R.mono(seg(bc, t0, t0 + 0.1))
        X = np.abs(np.fft.rfft(m))
        f = np.fft.rfftfreq(len(m), 1 / SR)
        cen.append([round(float(t0), 1), round(float((X * f).sum() / (X.sum() + 1e-12))), round(float(20 * np.log10(np.abs(m).max() + 1e-12)), 1)])
    chk["5 the tape-stop 19.0-19.4 [t, BCAST centroid Hz, peak dBFS]"] = cen
    tm, zm = flux_onsets(stems["mx"], 213.5, 215.5)
    near = (tm > 214.2) & (tm < 214.6)
    i = np.argmax(np.where(near, zm, -9))
    fd, _ = spec_peak(stems["mx"], tm[i] + 0.03, tm[i] + 0.5, 130, 700)
    chk["6 M4's D on 214.4 (+-0.1)"] = {"onset": round(float(tm[i]), 3), "z": round(float(zm[i]), 1), "peak Hz after": round(fd, 1),
                                        "ok": abs(tm[i] - 214.4) <= 0.1}
    mo = R.st_curve(bc, win=0.4)
    at = lambda t_: round(float(mo[int(t_ / 0.1)]), 1)
    chk["7 M1 in the broadcast (momentary, BCAST stem incl. carrier)"] = {"swell top 4.8": at(4.8), "between D03 and D04, 14.6-15.3": at(15.0),
                                                                          "under D02 (voice + M1) 9.5": at(9.5)}
    notes = []
    for e in spec["events"]:
        if e["id"].startswith("BC04.") and e["at"] < 242:
            st_ = stems[e["bus"]]
            want = mix2.note_hz(e["id"].split(".")[1].split("@")[0])
            fp, _ = spec_peak(st_, e["at"] + 0.02, e["at"] + 0.35, want * 2 ** (-0.6 / 12), want * 2 ** (0.6 / 12), n=1 << 18)
            tt, zz = flux_onsets(st_, e["at"] - 0.2, e["at"] + 0.2)
            near = np.abs(tt - e["at"]) <= 0.1
            notes.append([e["id"], round(float(tt[near][np.argmax(zz[near])]), 3), round(1200 * np.log2(fp / want), 1)])
    chk["8 the Chime [note, detected onset s, cents from the note]"] = notes
    NM = "A Bb B C C# D Eb E F F# G G#".split()
    nm = lambda f: f"{NM[int(round(12 * np.log2(f / 440))) % 12]}{(int(round(12 * np.log2(f / 440))) + 9) // 12 + 4}"
    mot = {}
    for cid, notes_ in rep.get("motif", {}).items():
        rows = []
        starts = sorted(set(n_[0] for n_ in notes_))
        for t_, name, gdb in notes_:
            want = mix2.note_hz(name)
            nxt = [v for v in starts if v > t_ + 0.05]
            t1 = min(t_ + 0.5, (nxt[0] - 0.05) if nxt else t_ + 0.5)
            # the strongest partial within +-3 semitones of the written note (bass notes sit an octave or more below the tune)
            fp, _ = spec_peak(stems["mx"], t_ + 0.05, t1, want * 2 ** (-3 / 12), want * 2 ** (3 / 12), n=1 << 18)
            rows.append([t_, name, nm(fp), round(1200 * np.log2(fp / want), 1)])
        mot[cid] = rows
    chk["9 Nana's motif by pitch tracking [time, written, heard, cents]"] = mot
    chk["9 all motif notes right (heard == written, within 10 c)"] = all(r_[1] == r_[2] and abs(r_[3]) <= 10 for v in mot.values() for r_ in v)
    q["spectrogram_checks"] = chk
    q["sync_onset_minus_plan_ms"] = [[l["id"], round((l["onset"] - l["planned"]) * 1000)] for l in rep["lines"] if not l.get("missing")]
    mo = R.st_curve(stems["dx"], win=3.0)
    q["loop_short_term_dx"] = {f"{t:.1f}": round(float(mo[int(t / 0.1)]), 1) for t in (64.0, 66.0, 68.0, 69.0, 69.5, 70.0, 70.2, 70.3)}

    # mono fold-down: loudness of (L+R)/2 vs the stereo reading
    fold = {}
    for name, st_, a, b in (("walla 224-233", "walla", 224, 233), ("horns D20b 168.2-171", "dx", 168.2, 171.0),
                            ("PA D16 145.3-147", "dx", 145.3, 147.0), ("CITY_SETS chime 80-83.5", "fx", 80.0, 83.5)):
        s = seg(stems[st_], a, b)
        mono = np.stack([s.mean(1)] * 2, 1)
        fold[name] = round(float(R.integrated(mono) - R.integrated(s)), 1)
    q["mono_fold_down_db"] = fold
    q["warnings"] = rep.get("warnings")
    conv = lambda o: o.item() if hasattr(o, "item") else str(o)
    out.with_name(out.stem + ".qa.json").write_text(json.dumps(q, indent=1, default=conv) + "\n")
    print(json.dumps(q, indent=1, default=conv))


if __name__ == "__main__":
    main()
