"""Compile the pilot's sound plan into a v4 timeline spec for tools/audio/mix2.py.

usage: uv run tools/audio/build_pilot_mix.py [work/pilot/audio/v4/mix.json]

Reads audio/pilot/{sfx,dialogue,score_cues}.json, the mix plan's rules (mix_plan.md, transcribed below where the
plan gives numbers), the cast selection (work/pilot/audio/vo_v4/selection.json) and the generated assets (to measure
pitches and slice single hits). Everything asset-specific that a new take would change lives in the spec's
"sources" block: music (one entry per cue, with that take's edit) and dialogue (one entry per line id).
"""
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mix2  # noqa: E402
import rooms as R  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SR = 48000
DUR = 242.0
SFX = json.loads((ROOT / "audio/pilot/sfx.json").read_text())["sfx"]
DLG = json.loads((ROOT / "audio/pilot/dialogue.json").read_text())
CUES = {c["id"]: c for c in json.loads((ROOT / "audio/pilot/score_cues.json").read_text())["cues"]}
VO = ROOT / "work/pilot/audio/vo_v4"
SEL = json.loads((VO / "selection.json").read_text())
SFX_DIR = "work/pilot/audio/sfx"

BEDS = {s["id"] for s in SFX if s.get("loop")} | {"X01"}
BUS = {"BCAST": "bcast", "OPTICAL": "bcast", "OPTICAL_COLD": "bcast"}


def spec_src(sid):
    return {"sfx": sid}


def asset(sid):
    return R.mono(mix2.load_audio(mix2.sfx_path({"sources": {"sfx_dir": SFX_DIR}}, sid)))


def strongest_hz(sid, lo, hi, t0=0.0, t1=None):
    x = asset(sid)[int(t0 * SR):(int(t1 * SR) if t1 else None)]
    N = 1 << int(np.ceil(np.log2(len(x) * 4)))
    X = np.abs(np.fft.rfft(x * np.hanning(len(x)), N))
    f = np.fft.rfftfreq(N, 1 / SR)
    sel = np.where((f > lo) & (f < hi))[0]
    k = sel[np.argmax(X[sel])]
    a, b, c = np.log(X[k - 1:k + 2] + 1e-12)
    return (k + 0.5 * (a - c) / (a - 2 * b + c)) * SR / N


def strongest_hz_file(path, lo, hi, t0, t1):
    x = R.mono(mix2.load_audio(path))[int(t0 * SR):int(t1 * SR)]
    N = 1 << int(np.ceil(np.log2(len(x) * 8)))
    X = np.abs(np.fft.rfft(x * np.hanning(len(x)), N))
    f = np.fft.rfftfreq(N, 1 / SR)
    sel = np.where((f > lo) & (f < hi))[0]
    k = sel[np.argmax(X[sel])]
    a, b, c = np.log(X[k - 1:k + 2] + 1e-12)
    return (k + 0.5 * (a - c) / (a - 2 * b + c)) * SR / N


def strong_hits(sid, rel=-12, gap=0.03, length=0.08, t0=0.0, t1=None, limit=16):
    """Single hits: 5 ms frames that jump 9 dB within 20 ms and peak within `rel` dB of the asset's loudest."""
    x = asset(sid)
    k = int(0.005 * SR)
    n = len(x) // k
    e = 20 * np.log10(np.sqrt((x[:n * k].reshape(n, k) ** 2).mean(1)) + 1e-9)
    pk = e.max()
    out = []
    for i in range(4, n - 4):
        t = i * 0.005
        if t < t0 or (t1 and t > t1):
            continue
        if e[i] - e[i - 4:i].min() > 9 and e[i:i + 4].max() > pk + rel and (not out or t - out[-1] > gap + length):
            out.append(t)
    return [[round(t - 0.005, 3), round(t + length, 3)] for t in out[:limit]]


def every(p, nxt):
    """Times of an `every` placement, `to` inclusive, dropping a time the next placement of the asset starts on."""
    ts = list(np.round(np.arange(p["at"], p["to"] + 1e-6, p["every"]), 3))
    if nxt is not None and ts and abs(ts[-1] - nxt) < 1e-6:
        ts = ts[:-1]
    return [float(t) for t in ts]


def main():
    out = ROOT / (sys.argv[1] if len(sys.argv) > 1 else "work/pilot/audio/v4/mix.json")
    ev = []
    counted = {}  # sfx placement key -> how it is realised

    def pl(sid, i):
        k = f"{sid}/{i}"
        counted[k] = "event"
        return k

    by = {s["id"]: s for s in SFX}

    # ---------------------------------------------------------------- the Chime (BC04): one strike, a sampler
    f_chime = strongest_hz("BC04", 400, 4000)
    chime_rooms = {"OPTICAL": "bcast", "OPTICAL_COLD": "bcast", "DRY": "fx", "CITY_SETS": "fx", "AIR": "fx"}
    fades = {0.5: [[4.2, 0], [5.6, -60]], 1.0: [[4.2, 0], [5.6, -60]], 1.5: [[4.6, 0], [6.2, -60]],
             50.3: [[55.5, 0], [58.5, -60]], 80.0: [[82.5, 0], [84.0, -60]], 80.5: [[82.5, 0], [84.0, -60]],
             81.0: [[82.5, 0], [84.0, -60]], 233.5: [[239.6, 0], [241.6, -60]], 234.0: [[239.6, 0], [241.6, -60]]}
    for i, p in enumerate(by["BC04"]["placements"]):
        if p["at"] >= DUR:
            counted[f"BC04/{i}"] = "alt tail (after 242.0, not rendered)"
            continue
        r = mix2.note_hz(p["pitch"]) / f_chime
        e = {"id": f"BC04.{p['pitch']}@{p['at']}", "kind": "shot", "src": spec_src("BC04"), "at": p["at"], "ratio": round(r, 6),
             "room": p["room"], "lvl": p["lvl"], "bus": chime_rooms[p["room"]], "placements": [pl("BC04", i)],
             "note": f"strike {f_chime:.1f} Hz repitched to {p['pitch']}"}
        if p["at"] in fades:
            e["auto"] = fades[p["at"]]
        ev.append(e)

    # ---------------------------------------------------------------- beds
    def bed(sid, room, spans, idx, **kw):
        e = {"id": kw.pop("id", sid), "kind": "bed", "src": spec_src(sid), "room": room, "spans": spans,
             "lvl_mode": "st", "bus": kw.pop("bus", "amb"), "tile_seed": sum(map(ord, sid)),
             "placements": [pl(sid, i) for i in idx]}
        e.update(kw)
        ev.append(e)

    bed("BC01", "OPTICAL", [[0.0, 5.0, -42, "hard", "x"], [149.3, 152.0, -42, "hard", "x"]], [0, 1], bus="bcast",
        mono_src=True)
    counted["BC01/2"] = "alt tail (after 242.0, not rendered)"
    # X01 the carrier: numpy, clean hiss low-passed at 12 kHz, mono, dead centre
    ev.append({"id": "X01", "kind": "bed", "src": {"gen": "carrier"}, "room": None, "lvl_mode": "st", "bus": "bcast",
               "spans": [[5.0, 19.4, -54, "hard", "hard"], [152.0, 157.0, -54, "hard", "hard"], [163.0, 168.0, -54, "hard", "hard"],
                         [180.0, 186.0, -50, "hard", "hard"]], "placements": [pl("X01", 0), pl("X01", 1), pl("X01", 2), pl("X01", 3)],
               "note": "5.0-19.0 runs on to the tape-stop, which slows it with the bus"})
    counted["X01/4"] = "alt tail (after 242.0, not rendered)"
    counted["X02/0"] = "global tapestop on the BCAST bus"
    # H01 Hall air
    bed("H01", "HALL_BED", [[20.0, 77.0, -38, 1.0, "x"], [90.0, 94.0, -40], [99.0, 103.0, -40], [109.0, 149.0, -38, "x", "hard"],
                            [168.0, 174.0, -36], [186.0, 198.0, -44, "hard", "x"], [202.0, 205.0, -44], [210.0, 223.0, -42, "x", "hard"]],
        range(8), variants=[{"from": 186.4, "ops": [["lp", 400, 2]], "xfade": 0.6}],
        auto=[[217.0, 0], [217.1, 2], [223.0, 2]])
    counted["H01/8"] = "alt tail (after 242.0, not rendered)"
    # H02 the Engine's hum, retuned 50 -> 55 Hz series (A1/A2), with X05 strain, the sag and X03 wind-down
    f_hum = strongest_hz("H02", 125, 145) / 2  # the rumble's own series: 2nd harmonic ~134 Hz (the 100/200 Hz lines are the generator's)
    r_hum = 55.0 / f_hum
    sag = lambda t: 20 * (t - 117) / 32
    bed("H02", "HALL_FLOOR", [[20.0, 77.0, -40, 1.5, "x"], [90.0, 94.0, -42], [99.0, 103.0, -42], [109.0, 149.0, -40, "x", "hard"],
                              [168.0, 174.0, -38], [186.0, 187.8, -38, "hard", "hard"]], range(6),
        ratio=round(r_hum, 6), mono_src=True,
        pitch_auto=[[0, 0], [66.3, 0], [70.4, 100], [70.45, 0], [117.0, 0], [128.2, sag(128.2)], [128.35, sag(128.35) - 50],
                    [129.55, sag(129.55)], [149.0, 20], [149.05, 0], [186.4, 0], [187.8, 1200 * np.log2(0.36)]],
        auto=[[66.3, 0], [70.4, 6], [70.45, 0], [117.0, 0], [128.2, 8 * 11.2 / 32], [128.35, 8 * 11.35 / 32 - 6], [129.55, 8 * 12.55 / 32],
              [149.0, 8], [149.05, 0], [186.4, 0], [186.6, -1], [187.8, -50]],
        note=f"hum fundamental {f_hum:.2f} Hz (from its 2nd harmonic) -> A1 55 / A2 110 (ratio {r_hum:.4f}); X05 strain and sag, X03 wind-down 1.0 -> 0.36")
    counted["H02/6"] = "alt tail (after 242.0, not rendered)"
    for k in ("X03/0", "X05/0", "X05/1"):
        counted[k] = "automation on the H02 bed (pitch_auto / auto)"
    # H03 roof rain; the bridge swells +8 dB into the canal's rain
    bed("H03", "HALL_BED", [[22.0, 77.0, -44], [90.0, 94.0, -46], [99.0, 103.0, -46], [109.0, 149.0, -46, "x", "hard"], [168.0, 174.0, -44],
                            [186.0, 198.0, -42, "hard", "x"], [202.0, 205.0, -42], [210.0, 223.0, -42, "x", "hard"]], range(8),
        auto=[[76.0, 0], [77.0, 8], [77.1, 0]])
    # H04 the Wall's tubes, retuned so the whine's strongest partial is A6; the terminal's own tube at the desk
    f_tube = strongest_hz("H04", 1000, 3000)
    r_tube = 1760.0 / f_tube
    bed("H04", "HALL_BED", [[22.0, 30.0, -46], [66.3, 70.4, -46, 0.5, "hard"], [119.0, 149.0, -42, "x", "hard"], [168.0, 174.0, -42],
                            [186.0, 186.5, -42, "hard", "hard"], [217.0, 223.0, -52, "x", "hard"]], [0, 2, 3, 4, 5],
        ratio=round(r_tube, 6), auto=[[22.0, 0], [30.0, 4], [30.1, 0], [66.3, 0], [70.4, 8], [70.45, 0], [119.0, 0], [149.0, 6], [149.05, 0]],
        variants=[{"from": 217.0, "ops": [["lp", 1500, 2]], "xfade": 0.05}],
        note=f"whine partial {f_tube:.1f} Hz -> A6 1760 (ratio {r_tube:.4f}); 66.3-70.4 is the plan's loop rise (mix_plan.md 5)")
    bed("H04", "DESK", [[109.0, 119.0, -48]], [1], id="H04.desk", ratio=round(r_tube, 6))
    # H13 the scope's thin A: the 400 Hz partial -> A5 880
    f_sc = strongest_hz("H13", 300, 700)
    bed("H13", "DESK", [[45.9, 50.0, -36, 0.2, 0.8]], [0], ratio=round(880.0 / f_sc, 6), bus="fx",
        note=f"strongest partial {f_sc:.1f} Hz -> A5 880")
    # H20 the teleprinter (a loop) and H29 the line
    bed("H20", "DESK", [[69.0, 70.4, -24, 0.05, "hard"]], [0], pan=0.4, auto=[[69.0, -6], [70.4, 0]], bus="fx")
    ida_call = [[89.9, 90.0, -54, "hard", "x"], [90.0, 94.0, -50], [94.0, 99.0, -54], [99.0, 103.0, -50], [103.0, 109.8, -54, "x", 0.4],
                [195.0, 198.0, -50, "hard", "x"], [198.0, 202.0, -54], [202.0, 205.0, -50], [205.0, 210.0, -54], [210.0, 217.0, -48, "x", "x"]]
    bed("H29", "LINE_SPILL", ida_call, [0, 1], mono_src=True, note="-50 in Ida's shots, -54 in Nana's, -48 under D26 (PHONE_EAR's line hiss)")
    # Nana's room: N01 tone, N02 window rain, N04 the set, N05 the stove; the far room down the line in Ida's shots
    nana = [[94.0, 99.0], [103.0, 109.0], [174.0, 180.0], [198.0, 202.0], [205.0, 210.0]]
    bed("N01", "FLAT", [[83.0, 90.0, -44, 1.0, "x"], [94.0, 99.0, -44], [103.0, 109.0, -44], [174.0, 180.0, -44, "x", "hard"],
                        [198.0, 202.0, -42], [205.0, 210.0, -42]], range(6))
    bed("N02", "FLAT", [[84.0, 90.0, -40], [94.0, 99.0, -42], [103.0, 109.0, -42], [174.0, 180.0, -42, "x", "hard"],
                        [198.0, 202.0, -40], [205.0, 210.0, -40]], range(6))
    f_tv = strongest_hz("N04", 90, 115)
    bed("N04", "FLAT", [[84.0, 90.0, -46], [94.0, 99.0, -48], [103.0, 109.0, -48], [174.0, 180.0, -48, "x", "hard"]], range(4),
        ratio=round(110.0 / f_tv, 6), mono_src=True, mod={"hz": 0.25, "depth": 0.03, "spans": [[80, 110]]},
        note=f"hum {f_tv:.2f} Hz -> 110 (A2); breathes +-3 % at 0.25 Hz except on air (174-180). FLAT, not TV: the hum is the "
             "chassis in the room; the TV transfer's 180 Hz high-pass would remove the A2 the treatment asks for")
    bed("N05", "FLAT", [[84.0, 90.0, -44], [94.0, 99.0, -50], [103.0, 109.0, -50], [174.0, 180.0, -50, "x", "hard"],
                        [198.0, 202.0, -48], [205.0, 210.0, -48]], range(6))
    ida_shots = [[90.0, 94.0], [99.0, 103.0], [195.0, 198.0, "hard", "x"], [202.0, 205.0], [210.0, 217.0]]
    bed("N01", "LINE_SPILL", [[s[0], s[1], -58] + s[2:] for s in ida_shots], [], id="N01.line", mono_src=True,
        note="N01 treatment: the flat tone sent down the line in Ida's call shots")
    bed("N02", "LINE_SPILL", [[s[0], s[1], -56] + s[2:] for s in ida_shots], [], id="N02.line", mono_src=True,
        note="H29 treatment: Nana's rain carried in the line")
    bed("N05", "LINE_SPILL", [[211.0, 216.0, -58]], [6], id="N05.line", mono_src=True)
    # the city, the street, the dawn
    bed("C01", "CANAL", [[76.0, 84.0, -30, 1.0, "x"]], [0], lp_auto=[[76.0, 1500], [77.0, 16000]])
    bed("C02", "CANAL", [[77.0, 84.0, -42], [223.0, 236.0, -46, "hard", 3.0]], [0, 1],
        variants=[{"from": 223.0, "ops": [["lp", 1200, 2]], "xfade": 0.05}])
    f_tram = strongest_hz("C04", 400, 800)
    bed("C04", "STREET", [[157.0, 159.6, -32, "hard", "hard"]], [0], ratio=round(440.0 / f_tram, 6),
        pitch_auto=[[0, 0], [158.8, 0], [159.6, 1200 * np.log2(0.3)]], auto=[[158.8, 0], [159.6, -40]],
        note=f"whine partial {f_tram:.1f} Hz -> A4 440; X04 spin-down 1.0 -> 0.3 over 158.8-159.6")
    counted["X04/0"] = "automation on the C04 bed"
    bed("C05", "STREET", [[157.0, 163.0, -30, "hard", "hard"]], [0])
    bed("C06", "DAWN", [[223.0, 236.0, -40, "hard", 3.0]], [0])
    bed("C10", "CANAL", [[224.0, 236.0, -44, 1.0, 3.0]], [0], chain=[["hp", 200, 2], ["lp", 1800, 3]], auto=[[224.0, 0], [232.0, 14]],
        bus="walla", note="WINDOW for a bed: low-passed 1.8 kHz, then the canal")
    bed("C11", "DAWN", [[223.0, 236.0, -46, "hard", 3.0]], [0])

    # ---------------------------------------------------------------- one-shots and series
    def shot(sid, i, room, **kw):
        p = by[sid]["placements"][i]
        e = {"id": kw.pop("id", f"{sid}@{p['at']}"), "kind": "shot", "src": kw.pop("src", spec_src(sid)), "at": kw.pop("at", p["at"]),
             "room": room, "lvl": kw.pop("lvl", p["lvl"]), "lvl_mode": "peak", "bus": kw.pop("bus", "fx"),
             "placements": [pl(sid, i)]}
        e.update(kw)
        ev.append(e)

    def series(sid, idx, room, times, **kw):
        ps = [by[sid]["placements"][i] for i in idx]
        e = {"id": kw.pop("id", f"{sid}@{ps[0]['at']}"), "kind": "series", "src": kw.pop("src", spec_src(sid)), "times": times,
             "room": room, "lvl": kw.pop("lvl", ps[0]["lvl"]), "lvl_mode": "peak", "bus": kw.pop("bus", "fx"),
             "placements": [pl(sid, i) for i in idx]}
        e.update(kw)
        ev.append(e)

    shot("BC02", 0, "OPTICAL", bus="bcast")
    shot("BC02", 1, "OPTICAL", bus="bcast")
    counted["BC02/2"] = "alt tail (after 242.0, not rendered)"
    shot("BC03", 0, "BCAST", keep=0.12, note="the tear, 0.12 s; on FX so the tape-stop does not slow it")
    # the Air Clock: one step, every second, HALL_FAR
    acc = {75.0: 4, 76.0: 4, 117.0: 4, 118.0: 4}
    hp = by["H05"]["placements"]
    for i, p in enumerate(hp):
        nxt = hp[i + 1]["at"] if i + 1 < len(hp) else None
        ts = [[t, acc.get(t, 0)] for t in every(p, nxt)]
        series("H05", [i], "HALL_FAR", ts, id=f"H05@{p['at']}")
    shot("H06", 0, "HALL_FAR")
    shot("H06", 1, "HALL_FAR")
    ts = every(by["H07"]["placements"][0], None)
    series("H07", [0], "HALL_FLOOR", [[t, 12 * (t - ts[0]) / (ts[-1] - ts[0])] for t in ts], note="ramps -30 -> -18 peak")
    # flaps: the desk repeater as recorded; the Air Clock's big board 5 semitones down
    fp = by["H08"]["placements"]
    for i, p in enumerate(fp):
        if p["room"] == "HALL_FAR":
            shot("H08", i, "HALL_FAR", ratio=round(2 ** (-5 / 12), 6))
        elif p.get("every"):
            series("H08", [i], "DESK", every(p, None))
        else:
            shot("H08", i, "DESK")
    for i in range(len(by["H09"]["placements"])):
        shot("H09", i, "DESK")
    rng = np.random.default_rng(10)
    for i, p in enumerate(by["H10"]["placements"]):
        room = "HALL_PA_NOTAPE" if p["room"] == "HALL_PA" else p["room"]
        shot("H10", i, room, ratio=round(2 ** (rng.uniform(-1, 1) / 12), 6))
    shot("H11", 0, "DESK", fade=[1.0, 0.0], keep=4.7, mono_src=False, note="eases in over 1 s; cut by the brake at 45.6")
    shot("H12", 0, "DESK")
    shot("H14", 0, "DESK", at=49.2, align=2.72, ratio=round(1 / 1.08, 6),
         note="the clunk at 2.72 s in the take lands on 49.2; slowed 8 % (the plan's maximum) by resampling")
    shot("H15", 0, "DRY")
    shot("H16", 0, "HALL_FAR", id="H16.far", auto=[[52.4, 0], [54.9, -2], [55.35, -40]], pan_auto=[[52.4, -0.8], [55.35, 0.0]],
         lp_auto=[[52.4, 300], [55.35, 4000]])
    ev.append({**ev[-1], "id": "H16.desk", "room": "DESK", "auto": [[52.4, -40], [54.0, -8], [55.35, 0]], "placements": []})
    shot("H17", 0, "DESK", send=["HALL_FAR", -14])
    shot("H18", 0, "DESK")
    shot("H19", 0, "DESK")
    # H21 the scroll relay: single clicks
    clicks = strong_hits("H21", rel=-6, length=0.035)
    series("H21", [0], "DESK", [63.3, 65.4, 66.3], src={"sfx": "H21", "slices": clicks}, id="H21@63.3",
           note="one click per fragment the terminal appends (J07's script order)")
    t, ts = 109.0, []
    while t < 115.0:
        ts.append(round(t, 3))
        t += 1 / (22 * (2 / 22) ** ((t - 109.0) / 6.0))
    series("H21", [1], "DESK", ts, src={"sfx": "H21", "slices": clicks}, jitter={"db": 1.5}, id="H21@109.0",
           note=f"{len(ts)} clicks, 22/s thinning to 2/s")
    # H22 keys on the JS keystroke logs; H23 the heavy keys (TAB, the commit)
    strokes = strong_hits("H22", rel=-14, length=0.09)
    logs = []
    for f in ("keys_24", "keys_26"):
        logs += json.loads((ROOT / f"work/pilot/js/{f}.json").read_text())
    kp = by["H22"]["placements"]
    for i, p in enumerate(kp):
        lo, hi = p["at"] - 0.05, p.get("to", p["at"]) + 0.05
        lt = [k["abs"] for k in logs if lo <= k["abs"] <= hi and k["kind"] in ("char", "enter")]
        muff = p["lvl"] <= -38
        if muff or not lt:
            lt = every(p, None) if p.get("every") else [p["at"]]
            if muff:
                lt = [round(t + float(np.random.default_rng(int(t * 100)).uniform(-0.03, 0.03)), 3) for t in lt]
        series("H22", [i], "DESK", [round(float(t), 4) for t in lt], src={"sfx": "H22", "slices": strokes},
               jitter={"db": 2, "cents": 51, "random_slice": True}, chain=[["lp", 2500, 2]] if muff else [],
               id=f"H22@{p['at']}", note="JS log" if not muff else "spec times, irregular, muffled")
    shot("H23", 0, "DESK")
    shot("H23", 1, "DRY", keep=0.08, keep_fade=0.004, id="H23.commit")
    shot("H24", 0, "DESK")
    # H25 the Red Line: retuned to G#, each ring trimmed to 1.2 s; loudness follows her attention
    f_red = strongest_hz("H25", 800, 3000)
    r_red = mix2.note_hz("G#6") / f_red
    for i, p in enumerate(by["H25"]["placements"]):
        ts = every(p, None) if p.get("every") else [p["at"]]
        if p["at"] == 131.0:
            ts = [[t, 4 * (t - 131) / 15] for t in ts]
        elif p["at"] == 212.0:
            ts = [[212.0, 0], [215.0, -3]]
        series("H25", [i], p["room"], ts, ratio=round(r_red, 6), keep=1.2, keep_fade=0.06, id=f"H25@{p['at']}")
    # H26 the civilian bell: F, double ring 0.4 on / 0.2 off / 0.4 on
    f_hb = strongest_hz("H26", 4000, 8000)
    r_hb = mix2.note_hz("F8") / f_hb
    for i, p in enumerate(by["H26"]["placements"]):
        ts = [p["at"]] if p["at"] == 89.5 else [p["at"], round(p["at"] + 0.6, 3)]
        kw = {"until": 89.9} if p["at"] == 89.5 else {}
        series("H26", [i], p["room"], ts, src={"sfx": "H26", "slice": [0.0, 0.6]}, fade=[0.002, 0.2], ratio=round(r_hb, 6),
               id=f"H26@{p['at']}", **kw)
    shot("H27", 0, "FLAT")
    shot("H27", 1, "DESK")
    shot("H28", 0, "DESK")
    shot("H30", 0, "HALL_FAR")
    shot("H31", 0, "STREET")
    shot("H31", 1, "HALL_FAR")
    shot("H32", 0, "DESK", mono_src=False)
    shot("H33", 0, "DESK", src={"sfx": "H33", "slice": [1.40, 2.48]}, at=215.1, align=0.66, fade=[0.03, 0.05],
         note="the pop (2.06 s in the take) on 215.1")
    shot("H34", 0, "HALL_FAR")
    counted["H35/0"] = "alt tail (after 242.0, not rendered)"
    shot("H36", 0, "HALL_FAR", keep=1.5)
    # H37 the horns open: relay and amplifier hum, the hum held under the voice until the close (H10)
    for i, (op, cl) in enumerate([(74.85, 76.6), (116.85, 118.6), (144.85, 146.7)]):
        shot("H37", i, "HALL_PA_NOTAPE", hold={"loop": [0.2, 0.5], "for": round(cl - op - 0.5, 3), "release": 0.5})
    shot("N06", 0, "FLAT", mono_src=False)
    # Nana's clock: tick on even seconds, tock on odd seconds 60 ms early
    tk = strong_hits("N03", rel=-8, length=0.45, t0=4.0, t1=6.0)
    tick, tock = tk[0], tk[1]
    np3 = by["N03"]["placements"]
    for i, p in enumerate(np3):
        nxt = np3[i + 1]["at"] if i + 1 < len(np3) else None
        base = [round(p["at"] + 0.06, 3)] if p["at"] == 82.94 else every(p, nxt)
        ts = [[round(t - 0.06, 3) if int(round(t)) % 2 else t, 0, 0, int(round(t)) % 2] for t in base]
        series("N03", [i], p["room"], ts, src={"sfx": "N03", "slices": [tick, tock]}, id=f"N03@{p['at']}")
    c3 = strong_hits("C03", rel=-3, length=1.6)
    series("C03", [0], "CANAL", [79.0, 79.6], src={"sfx": "C03", "slice": [c3[-1][0], 2.48]}, fade=[0.002, 0.3],
           note="the take's last, cleanest strike, on both times")
    drips = strong_hits("C06", rel=-10, length=0.25)
    series("C06", [1], "DAWN", every(by["C06"]["placements"][1], None), src={"sfx": "C06", "slices": drips}, id="C06.drips")
    shot("C07", 0, "CANAL", keep=7.2, keep_fade=1.0, mono_src=False)
    shot("C08", 0, "CANAL")
    shot("C09", 0, "CANAL", src={"sfx": "C09", "slice": [0.30, 8.0]}, at=224.4, fade=[0.01, 0.3], mono_src=False,
         note="the first latch on 224.4")
    shot("T01", 0, "AIR")

    # ---------------------------------------------------------------- dialogue (the cast takes)
    lines = {l["id"]: l for l in DLG["lines"]}
    take = lambda t: str((VO / SEL[t]["best"]["file"]).relative_to(ROOT))
    segs = {t: mix2.take_segments(mix2.load_audio(take(t))) for t in SEL}
    expect = {"T01": 5, "T02": 2, "T03": 4, "T04": 2, "T05": 1, "T06": 3, "T07": 10, "T08": 4, "T09": 6, "T10": 3}
    for t, n in expect.items():
        if len(segs[t]) != n:
            raise SystemExit(f"{t} splits into {len(segs[t])} segments, the line map expects {n}: re-map it\n{segs[t]}")
    S = lambda t, *ix: [[round(segs[t][i][0], 3), round(segs[t][i][1], 3)] for i in ix]
    dx = {}

    def cast(lid, t, ix, chain, **kw):
        dx[lid] = {"take": take(t), "spans": S(t, *ix), "chain": chain, **kw}

    cast("D01", "T01", [0], "father")
    cast("D02", "T01", [1, 2], "father", max_gap=0.35)
    cast("D02:harvest", "T01", [1], "father")
    cast("D02:calm", "T01", [2], "father")
    cast("D03", "T01", [3], "father")
    cast("D04", "T01", [4], "father")
    cast("T02", "T02", [0, 1], "father")
    cast("D05", "T04", [0], "ida")
    cast("V01", "T04", [1], "ida")
    cast("D08", "T05", [0], "ida")
    cast("D10", "T06", [0, 1], "ida", max_gap=0.35)
    cast("D12", "T06", [2], "ida")
    cast("D11", "T08", [0, 1], "nana", max_gap=0.30)
    cast("D13", "T08", [2], "nana")
    cast("D14", "T08", [3], "nana")
    cast("D09", "T10", [0], "none")
    cast("D15", "T10", [1], "none")
    cast("D16", "T10", [2], "none")
    dx["D17"] = {"same_as": "D01"}
    cast("D18", "T03", [0], "father")
    cast("D19", "T03", [1], "father")
    cast("D20:tomorrow", "T03", [2], "father")
    cast("D20:rest", "T03", [3], "father")
    dx["D21"] = {"same_as": "D04"}
    d22 = S("T07", 0)[0]
    dx["D22"] = {"take": take("T07"), "spans": [[d22[0], round(segs["T07"][1][0] + 0.06, 3)]], "chain": "ida",
                 "note": "Nana and the first breath of I, cut with a 30 ms fade"}
    cast("D24", "T07", [3], "ida")
    cast("V02", "T07", [4], "ida")
    dx["V03"] = {"take": take("T07"), "spans": [[S("T07", 5)[0][0], S("T07", 6)[0][1]]], "chain": "ida",
                 "note": "the exhale that becomes the laugh; the laugh's voiced onset is the line's start"}
    cast("V04", "T07", [9], "ida")
    cast("D23", "T09", [0], "nana")
    cast("V05", "T09", [2], "nana")
    cast("D25", "T09", [3], "nana")
    cast("D26", "T09", [4, 5], "nana")
    for w in ("W01", "W02", "W03", "W04", "W05", "W06", "W07", "W08", "W09", "W10"):
        sg = mix2.take_segments(mix2.load_audio(take(w)))
        if len(sg) == 2:
            dx[f"{w}:1"] = {"take": take(w), "spans": [[round(sg[0][0], 3), round(sg[0][1], 3)]], "chain": "none"}
            dx[f"{w}:2"] = {"take": take(w), "spans": [[round(sg[1][0], 3), round(sg[1][1], 3)]], "chain": "none"}
        else:
            dx[w] = {"take": take(w), "spans": [[round(s[0], 3), round(s[1], 3)] for s in sg], "chain": "none"}

    LV = {"D01": -17, "D02": -17, "D03": -17, "D04": -17, "D05": -21, "V01": -26, "D08": -18, "D09": -19, "D10": -18, "D11": -17,
          "D12": -18, "D13": -17, "D14": -17, "D15": -19, "D16": -19, "D17": -17, "D18": -19, "D19": -17, "D21": -22, "D22": -18,
          "D23": -17, "D24": -18, "V05": -27, "D25": -17, "V02": -28, "D26": -16.5, "V03": -24, "V04": -26}
    ROOM = {"DESK": "DESK", "DESK_GLASS": "DESK_GLASS", "FLAT": "FLAT", "BCAST": "BCAST", "HALL_PA": "HALL_PA",
            "STREET_PR": "STREET_PR", "TV": "TV", "PHONE_EAR": "PHONE_EAR"}
    DX_TRIM = 0.0  # rebalance (mix_plan.md 2): the level table integrates to about -18.3 LUFS; the anchor moves up 0.9 dB
    LV = {k: v + DX_TRIM for k, v in LV.items()}
    for lid, l in lines.items():
        if lid.startswith("W") or lid in ("D06", "D07", "D20"):
            continue
        if l["start"] >= DUR:
            continue
        room = ROOM[l["room"]]
        e = {"id": lid, "kind": "line", "line": lid, "at": l["start"], "room": room, "lvl": LV[lid],
             "bus": "bcast" if room == "BCAST" else "dx", "dur_window": l["dur"], "end_by": l["end_by"]}
        if room == "HALL_PA":
            e["group"] = "PA"
        edits = {"D08": [[73.536, 0.015, -6.0]],  # the t release of "not"
                 "D22": [[196.616, 0.045, -5.0]], "D10": [[91.480, 0.055, -5.0], [92.018, 0.025, -6.0]]}
        if lid in edits:  # consonant clip-gain edits: transients that would make the master limiter take > 2 dB
            e["clip_gain"] = edits[lid]
        if lid.startswith("V"):
            e["keep_span"] = True
            e["onset_rel"] = -40.0  # a breath swells: its onset is where it becomes audible, not its loudest part
            e["onset_per"] = 9.0  # and it has no voicing: energy onset only
        if lid in ("V02", "V04", "V05"):
            e["fit"] = "trim"
        if lid == "V03":
            e["onset_per"], e["onset_rel"] = 0.35, -25.0
            e["keep_preroll"] = True  # the exhale leads into the laugh; the laugh's voiced onset lands on 215.15
        ev.append(e)
    # D20: the perspective cut in the comma pause; Tomorrow ends by 167.98 in the studio, the rest after 168.15 in the Hall
    l20 = lines["D20"]
    ev.append({"id": "D20a", "kind": "line", "line": "D20:tomorrow", "at": l20["start"], "room": "BCAST", "lvl": -17 + DX_TRIM, "bus": "bcast",
               "end_by": 167.95, "fit": "shift", "dur_window": None, "note": "Tomorrow, (studio)"})
    ev.append({"id": "D20b", "kind": "line", "line": "D20:rest", "at": 168.2, "room": "HALL_HORNS", "lvl": -15 + DX_TRIM, "bus": "dx",
               "end_by": l20["end_by"], "dur_window": None, "note": "you'll have to talk to each other (the Hall's horns)"})
    # the loop (D06, D07): mix_plan.md 5
    ev.append({"id": "LOOP", "kind": "gen", "gen": "loop", "bus": "dx", "from": 63.3, "to": 70.4,
               "ref": {"D01": {"line": "D01"}, "harvest": {"line": "D02:harvest"}, "calm": {"line": "D02:calm"},
                       "I_am_well": {"line": "D03"}, "T02": {"line": "T02"}},
               "phase_a": [["D01", 63.3], ["harvest", 65.4]],
               "phase_b": [["calm", 66.3], ["I_am_well", 66.7], ["T02", 67.0], ["I_am_well", 67.35], ["calm", 67.6], ["I_am_well", 67.8]],
               "phase_c": [68.0, 70.0, 70.4], "gaps": [0.33, 0.067], "send_b0": 0.1, "lvl_a": -17, "lvl_top": -9, "t_top": 70.2,
               "carrier_db": -54, "peak_ctl_dbfs": -4.0, "peak_ctl_until": 69.9, "lines": ["D06", "D07"]})
    # the walla: WINDOW, staggered (no two murmur onsets within 0.3 s)
    wins = {"W03": (-10, -0.6), "W04": (-12, 0.5), "W05": (-8, -0.2), "W06": (-13, 0.8), "W07": (-9, 0.3), "W08": (-11, -0.8),
            "W09": (-7, 0.6), "W01": (-6, -0.3), "W02": (-6, -0.3), "W10": (-6, -0.3)}
    murmur = []
    for lid in ("W03", "W04", "W05", "W06", "W07", "W08", "W09"):
        for k, st in enumerate(lines[lid]["start"]):
            murmur.append([st, lid, k + 1])
    murmur.sort()
    last = -9
    for m in murmur:
        if m[0] - last < 0.3:
            m[0] = round(last + 0.3, 3)
        last = m[0]
    for st, lid, k in murmur:
        base = -40 + 8 * np.clip((st - 224) / 8, 0, 1)  # the wave spreads: murmur -44 rising to -30 with C10
        dist, pn = wins[lid]
        ev.append({"id": f"{lid}:{k}", "kind": "line", "line": f"{lid}:{k}", "at": st, "room": "WINDOW", "bus": "walla",
                   "lvl": round(float(base + (dist + 8) * 0.5), 1),
                   "window": {"dist": dist, "pan": pn, "lpf": 1800, "phone": lid == "W07"}, "end_by": 233.0, "dur_window": None,
                   "peak_ctl": None})
    for lid, lv in (("W01", -24), ("W02", -24)):
        l = lines[lid]
        ev.append({"id": lid, "kind": "line", "line": lid, "at": l["start"], "room": "WINDOW", "bus": "walla", "lvl": lv,
                   "window": {"dist": -6, "pan": -0.3, "lpf": 3500}, "end_by": l["end_by"], "dur_window": l["dur"]})
    for k, st in ((1, lines["W10"]["start"]), (2, 234.95)):  # Stay a while waits until after the withheld note (234.3-234.9)
        ev.append({"id": f"W10:{k}", "kind": "line", "line": f"W10:{k}", "at": st, "room": "WINDOW", "bus": "walla", "lvl": -32,
                   "window": {"dist": -6, "pan": -0.3, "lpf": 1800}, "auto": [[233.0, 0], [236.0, -40]], "end_by": None, "dur_window": None,
                   "peak_ctl": None})

    # ---------------------------------------------------------------- music (score_cues.json + each take's edit)
    f_smp = strongest_hz_file("work/pilot/score/final/M2_a.mp3", 160, 190, 0.75, 1.85)
    music = {
        "M1": {"src": "work/pilot/score/bake/M1_eleven.mp3", "edit": {
            "note": "The take has no swell: it opens on the chorale's D (file 0-4 D, 4-6 G, 8-10 D, 10.5-14.2 A, then B and a "
                    "fade). Its first section goes on 5.0 so the bars land on the hits (D 5.0, G 9.0, D 13.0, A held 15.5-19.4); "
                    "1.0-5.0 is its opening bar low-passed at 500 Hz as the swell.",
            "main": {"segments": [{"src": [0.0, 4.1], "at": 0.9, "fade": [0.1, 0.25], "ops": [["lp", 500, 2]]},
                                  {"src": [0.0, 14.6], "at": 5.0, "fade": [0.15, 0.2]}]},
            "ident": {"segments": [{"src": [0.3, 2.2], "at": 149.9, "fade": [0.3, 0.6]}]}}},
        "M2": {"src": "work/pilot/score/final/M2_a.mp3",
               "sample": {"file": "work/pilot/score/final/M2_a.mp3", "span": [0.70, 1.88], "loop": [1.25, 1.80],
                          "f0": round(f_smp, 3), "decay_db_s": 7.0,
                          "note": f"the take's first note, F3 ({f_smp:.2f} Hz), the cleanest on the take (its next partial is its own "
                                  "octave; nothing else within 22 dB); every motif note is this strike resampled"},
               "edit": {
            "note": "The take plays F F A E Bb Bb D/F F A G, not A F G E (score.md 'Generating' 3): the motif is played on a sampled "
                    "note of the take's own piano (score.md's fallback) over the take slipped with its A on 110.0 and ducked 14 dB.",
            "main": {"segments": [{"src": [1.74, 9.85], "at": 108.95, "fade": [0.05, 0.005]}], "duck": [[108.95, 117.0, -14]],
                     "jitter": {"db": 1.5, "ms": 15},
                     "notes": [[109.0, "D3", -7, 2.0], [110.0, "A4", 0, 1.4, "anchor"], [111.0, "F4", 0, 1.4], [111.0, "Bb2", -7, 2.0],
                               [112.0, "G4", 0, 1.4], [113.0, "E4", 0, 4.2], [113.0, "C3", -7, 4.2]]},
            "reprise": {"segments": [{"src": [2.77, 5.8], "at": 177.48, "fade": [0.005, 0.005]}], "duck": [[177.48, 180.0, -14]],
                        "jitter": {"db": 1.5, "ms": 15},
                        "notes": [[177.5, "A4", 0, 1.4, "anchor"], [178.5, "F4", 0, 1.4], [178.5, "Bb2", -7, 2.0], [179.5, "G4", 0, 1.4]]},
            "amber": {"segments": [], "notes": [[137.7, "A4", 0, 1.5, "anchor"]]}}},
        "M3": {"src": "work/pilot/score/final/M3_e.mp3", "edit": {
            "note": "The loudest sustained region (26.0-27.1 s) ends on 148.8 (slip 121.7); 117.0-123.0 is the take's quiet opening, "
                    "crossfaded over 1 s into the slipped take; a gain ride makes the level rise continuously to its peak at 149.0.",
            "main": {"segments": [{"src": [0.0, 6.0], "at": 117.0, "fade": [0.3, 1.0]},
                                  {"src": [0.3, 27.5], "at": 122.0, "fade": [1.0, 0.005]}]}}},
        "M4": {"src": "work/pilot/score/bake/M4_eleven.mp3", "edit": {
            "note": "0.53 s of silence at the head: slip 0.53 puts the first attack on 210.0. The take never plays the motif: A F G E F D "
                    "and the high D are played on M2's sampled note, with the take's own piano ducked 12 dB to 217.4. The take's "
                    "attacks at 234.24, 234.47 and 234.75 are frozen into the sustain before them, so 234.3-234.9 has no new attack.",
            "main": {"segments": [{"src": [0.53, 32.13], "at": 210.0, "fade": [0.005, 0.3]}], "freeze": [[234.2, 234.95]],
                     "duck": [[209.9, 217.4, -12]], "jitter": {"db": 1.5, "ms": 15},
                     "notes": [[210.2, "A4", 0, 1.1], [210.2, "F2", -8, 2.4], [211.0, "F4", 0, 1.1], [211.8, "G4", 0, 1.1],
                               [212.6, "E4", 0, 1.1], [212.6, "C3", -8, 1.8], [213.4, "F4", 0, 1.3], [214.4, "D4", 0, 3.0, "anchor"],
                               [214.4, "D3", -9, 3.0, "anchor"], [215.4, "D5", -4, 2.0]]}},
               "sample_from": "M2"},
    }
    bc = [["hp", 120, 2], ["lp", 9000, 2]]
    ev += [
        {"id": "M1", "kind": "cue", "cue": "M1", "use": "main", "in": 1.0, "out": 19.4, "bus": "bcast", "mono": True, "chain": bc,
         "lvl_keys": [[1.0, -60], [4.8, -24], [5.5, -30], [19.4, -30]]},
        {"id": "M1.ident", "kind": "cue", "cue": "M1", "use": "ident", "in": 149.9, "out": 151.8, "bus": "bcast", "mono": True,
         "chain": bc + [["lp", 1000, 2]], "lvl_keys": [[150.3, -30], [151.5, -30]]},
        {"id": "M2", "kind": "cue", "cue": "M2", "use": "main", "in": 109.0, "out": 117.0, "bus": "mx", "cut": [117.0, 0.005],
         "lvl_keys": [[109.5, -24], [116.5, -24]]},
        {"id": "M2.amber", "kind": "cue", "cue": "M2", "use": "amber", "in": 137.68, "out": 139.3, "bus": "mx",
         "lvl_keys": [[137.9, -20], [138.3, -20]], "lvl_win": 0.4, "note": "the amber note: A4 from the sampled note, 1.5 s"},
        {"id": "M3", "kind": "cue", "cue": "M3", "use": "main", "in": 117.0, "out": 149.0, "bus": "mx", "cut": [149.0, 0.005],
         "ride": {"keys": [[117.0, -46], [121.0, -38], [125.0, -32], [131.0, -26], [137.0, -22], [140.0, -19], [145.0, -15], [149.0, -12]],
                  "smooth": 2.0, "min": -15, "max": 15}, "peak_ctl_dbfs": -3.5},
        {"id": "M2.reprise", "kind": "cue", "cue": "M2", "use": "reprise", "in": 177.48, "out": 180.0, "bus": "mx", "cut": [180.0, 0.003],
         "lvl_keys": [[178.0, -26], [179.8, -26]]},
        {"id": "M4", "kind": "cue", "cue": "M4", "use": "main", "in": 210.0, "out": 241.6, "bus": "mx", "fade_out": [240.6, 241.6],
         "lvl_keys": [[210.6, -24], [216.4, -24], [217.6, -30], [222.6, -30], [223.6, -20], [231.0, -14], [232.5, -14], [233.6, -28],
                      [237.5, -28], [238.6, -22], [240.4, -22]]},
    ]

    # ---------------------------------------------------------------- the v4 rebalance (mix_plan.md 6): beds +4 dB, music -2 dB
    BED_TRIM, MUSIC_TRIM = 4.0, -2.0
    for e in ev:
        if e.get("kind") == "bed" and e["bus"] in ("amb", "walla"):
            e["spans"] = [[sp[0], sp[1], sp[2] + BED_TRIM] + sp[3:] if sp[2] is not None else sp for sp in e["spans"]]
        elif e.get("kind") == "line" and e["bus"] == "walla" and e["id"] not in ("W01", "W02"):
            e["lvl"] = round(e["lvl"] + BED_TRIM, 1)
        elif e.get("kind") == "cue" and e["bus"] == "mx":
            if e.get("lvl_keys"):
                e["lvl_keys"] = [[k[0], k[1] + MUSIC_TRIM] for k in e["lvl_keys"]]
            if e.get("ride"):
                e["ride"]["keys"] = [[k[0], k[1] + MUSIC_TRIM] for k in e["ride"]["keys"]]

    # ---------------------------------------------------------------- globals
    spec = {
        "dur": DUR, "out": "work/pilot/audio/v4/mix.wav", "say_cache": "work/pilot/audio/vo",
        "sources": {"sfx_dir": SFX_DIR, "music": music, "dialogue": dx,
                    "dehum": {"base": 50, "top": 1000, "keep": ["N04", "H13"],
                              "why": "most generated assets carry 50 Hz-series lines (200/400 Hz up to 36 dB over the floor); "
                                     "notched so the only pitch in a room is the state's A. The hums that are retuned keep them."}},
        "master": {"lufs": -16, "limit_dbfs": -1.8, "tp": -1.0, "max_gr_db": 2.0, "gr_allowed": [[69.9, 70.4], [148.5, 149.08]],
                   "why": "dynamics over loudness (mix_plan.md 6): the one gain is the largest that keeps the limiter under 2 dB "
                          "outside the last 0.5 s before HALT and the commit; integrated lands where that puts it"},
        "tapestop": {"bus": "bcast", "at": 19.0, "dur": 0.4, "until": 20.0},
        "bus_fx": {"bcast": [["mono"], ["lp", 12000, 1]]},
        "mutes": [
            {"from": 19.4, "to": 20.0, "why": "signal gap"},
            {"from": 70.40, "to": 71.00, "buses": ["dx", "fx", "bcast", "mx", "walla"], "kill": True, "why": "HALT: digital black"},
            {"from": 70.40, "to": 71.00, "buses": ["amb"], "ramp_in": 0.083, "why": "beds resume at their continuing position"},
            {"from": 149.0, "to": 149.3, "except": ["H23.commit"], "kill": True, "why": "the commit: everything cut dead under the key"},
            {"from": 149.08, "to": 149.3, "why": "digital black after the key's 80 ms"},
            {"from": 180.0, "to": 186.0, "except": ["X01"], "kill": True, "why": "dead air: the carrier alone"},
            {"from": 168.0, "to": 242.0, "only": ["D20a"], "why": "perspective cut: the studio's tail is dropped"},
            {"from": 174.0, "to": 242.0, "only": ["D20b"], "why": "perspective cut: the Hall's tail is dropped at the TV"},
            {"from": 223.0, "to": 242.0, "only": ["H*"], "why": "the rain stops: the Hall is gone at dawn"},
            {"from": 241.6, "to": 242.0, "why": "end: nothing"},
        ],
        "ducks": [
            {"from": 45.6, "to": 47.1, "db": -18, "attack": 0.02, "release": 0.6, "except": ["H05*", "H13*", "H12*"],
             "why": "the held breath: only the clock, the scope's A and the brake's tail"},
            {"from": 145.2, "to": 146.6, "db": -3, "attack": 0.15, "release": 0.3, "only": ["M3"], "why": "strings duck 3 dB round Ten seconds"},
        ],
        "events": ev,
    }
    total = sum(len(s["placements"]) for s in SFX)
    missing = [f"{s['id']}/{i}" for s in SFX for i in range(len(s["placements"])) if f"{s['id']}/{i}" not in counted]
    spec["sfx_placements"] = {"total": total, "realised": counted, "unmapped": missing}
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(spec, indent=1) + "\n")
    print(f"{out.relative_to(ROOT)}: {len(ev)} events; sfx placements {total}, mapped {len(counted)}, unmapped {missing}")
    print(f"  chime {f_chime:.1f} Hz, hum {f_hum:.2f}, tubes {f_tube:.1f}, scope {f_sc:.1f}, tv {f_tv:.2f}, tram {f_tram:.1f}, "
          f"red {f_red:.1f}, house {f_hb:.1f}")


if __name__ == "__main__":
    main()
