"""v2 conform (see conform_brief.md): pre-cut Seedance segments, write comp_v2 specs, extract dialogue, build main_v2.json.

usage: uv run work/pilot/v2/conform_v2.py [video|audio|all]
"""
import copy
import json
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
FPS = 24
V2 = "work/pilot/v2"
CLIP = {k: f"{V2}/shots/{k}/takes/01.mp4" for k in
        ["02", "03", "07", "13", "17", "18", "19", "20", "23", "25", "32", "33", "38", "39", "40", "41", "42", "address"]}
CLIP["16"] = f"{V2}/16/takes/02.mp4"
CLIP["44"] = f"{V2}/44/takes/02.mp4"

# shot -> (clip, segment start s, hold last frame to fill)
SHOTS = {"02": ("02", 0), "03": ("03", 0), "07": ("07", 0), "13": ("13", 0), "16": ("16", 0), "17": ("17", 0),
         "18": ("18", 0), "19": ("19", 0), "20": ("20", 0), "23": ("23", 0), "25": ("25", 0), "29": ("address", 0.1),
         "31": ("address", 7.0), "32": ("32", 0), "33": ("33", 0), "34": ("address", 18.0), "38": ("38", 0),
         "39": ("39", 0), "40": ("40", 0), "41": ("41", 0), "42": ("42", 0), "44": ("44", 0)}
PARTICLES_KEEP = {"07", "23", "32"}   # dust in the Hall; rain is in the clips


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, **kw)


def nframes(p):
    r = run(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0", "-show_entries",
             "stream=nb_read_frames", "-of", "csv=p=0", str(ROOT / p)], capture_output=True, text=True)
    return int(r.stdout.strip())


def v1_timeline():
    edit = json.loads((ROOT / "work/pilot/edit_main.json").read_text())
    t, out = 0, {}
    for s in edit["shots"]:
        n = nframes(s)
        out[Path(s).stem] = (t, n)
        t += n
    return out, t


def seg_start_frame(sh):
    return int(round(SHOTS[sh][1] * FPS))


def video(tl):
    src_dir = ROOT / "work/pilot/comp_v2/src"
    src_dir.mkdir(parents=True, exist_ok=True)
    (ROOT / "work/pilot/shots_v2").mkdir(parents=True, exist_ok=True)
    make_sky()
    for sh, (clip, _) in SHOTS.items():
        t0f, n = tl[sh]
        a = seg_start_frame(sh)
        have = nframes(CLIP[clip]) - a
        use = min(n, have)
        vf = f"trim=start_frame={a}:end_frame={a + use},setpts=PTS-STARTPTS,scale=1920:1080:flags=lanczos"
        if use < n:
            vf += f",tpad=stop_mode=clone:stop={n - use}"
        inter = f"work/pilot/comp_v2/src/{sh}.mp4"
        run(["ffmpeg", "-y", "-v", "error", "-i", str(ROOT / CLIP[clip]), "-vf", vf, "-an", "-c:v", "libx264", "-crf", "10",
             "-preset", "fast", "-pix_fmt", "yuv420p", str(ROOT / inter)])
        v1 = json.loads((ROOT / f"work/pilot/comp/{sh}.json").read_text())
        layers = [{"src": inter}]
        layers += [L for L in v1["layers"][1:] if Path(L["src"]).name in ("scanlines.png", "j14_bug.png", "s34_bug.mov")]
        spec = {"dur": n / FPS, "fps": FPS, "out": f"work/pilot/shots_v2/{sh}.mp4", "layers": layers,
                "camera": {"from": [0.5, 0.5, 1.0], "to": [0.5, 0.5, 1.0]}, "grade": v1["grade"]}
        if v1.get("letterbox"):
            spec["letterbox"] = v1["letterbox"]
        if sh in PARTICLES_KEEP and v1.get("particles"):
            spec["particles"] = v1["particles"]
        # 44: no added sky. The Seedance take already turns rose at dawn; an extra gradient only hazed the towers.
        (ROOT / f"work/pilot/comp_v2/{sh}.json").write_text(json.dumps(spec, indent=1) + "\n")
        print(sh, "in", t0f / FPS, "frames", n, "src frames", use, "+hold", n - use, "from", CLIP[clip], "@", a)


def make_sky():
    """Rose (#E8A0A8) at the top to pale gold at 45 % of frame height; alpha falls to 0 over the lower third of that."""
    W, H = 1920, 1080
    y = np.arange(H, dtype=np.float32)[:, None] / H
    u = np.clip(y / 0.45, 0, 1)
    rose, gold = np.array([232, 160, 168], np.float32), np.array([242, 222, 170], np.float32)
    rgb = rose + (gold - rose) * u[..., None]
    a = np.clip((0.45 - y) / 0.15, 0, 1)
    a = a * a * (3 - 2 * a)
    im = np.concatenate([np.broadcast_to(rgb, (H, 1, 3)).repeat(W, 1), np.broadcast_to(a[..., None] * 255, (H, W, 1))], -1)
    cv2.imwrite(str(ROOT / "work/pilot/comp_v2/sky44.png"), im[..., [2, 1, 0, 3]].astype(np.uint8))


# ------------------------------------------------------------------ audio
# id -> (clip, line start, line end, shot | None for off-screen, preset for off-screen)
LINES = {
    "D01": ("02", 0.00, 1.72, "02"), "D02": ("02", 3.16, 6.60, "02"),
    "D03": ("03", 0.00, 1.62, "03"), "D04": ("03", 4.04, 6.36, "03"),
    "D08": ("13", 2.04, 2.70, "13"),
    "D10": ("17", 0.00, 2.30, "17"), "D11": ("18", 0.00, 3.14, "18"), "D12": ("19", 1.52, 2.98, "19"),
    "D13": ("20", 0.30, 1.05, "20"),   # Whisper missed it; bounds from the energy envelope
    "D14": ("20", 3.10, 5.56, "20"),
    "D17": ("address", 0.88, 2.40, "29"), "D19": ("address", 7.78, 9.44, "31"),
    "D22": ("38", 0.00, 1.84, "38"), "D23": ("39", 1.52, 2.90, "39"), "D24": ("40", 1.16, 2.38, "40"),
    "D25": ("41", 0.86, 3.30, "41"),
    "D18": ("address", 4.12, 5.64, None), "D20": ("address", 12.24, 14.62, None),
    "D21": ("address", 16.18, 18.02, None), "D26": ("41", 4.18, 7.34, None),
}
SPATIAL = ("af_post", "slap", "reverb", "rt60", "predelay", "rcut", "gain")
FATHER_EQ = "highpass=f=90,lowpass=f=7000,equalizer=f=2500:t=q:w=1:g=3,acompressor=threshold=-20dB:ratio=3"


def resolve(e, presets):
    uses = e.get("use", [])
    out = {}
    for u in [uses] if isinstance(uses, str) else uses:
        out.update(resolve(presets[u], presets))
    out.update({k: v for k, v in e.items() if k != "use"})
    return out


def extract(lid):
    clip, ls, le, _ = LINES[lid]
    s, e = max(0.0, ls - 0.12), le + 0.25
    out = ROOT / f"work/pilot/audio/vo_v2/{lid}.wav"
    d = e - s
    run(["ffmpeg", "-y", "-v", "error", "-i", str(ROOT / CLIP[clip]), "-af",
         f"aresample=48000,atrim=start={s}:end={e},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={d - 0.02:.4f}:d=0.02",
         "-ac", "1", "-ar", "48000", "-c:a", "pcm_s24le", str(out)])
    return s, e


def read_wav(p):
    raw = run(["ffmpeg", "-v", "error", "-i", str(p), "-f", "f32le", "-ac", "1", "-ar", "48000", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.float32)


def speech_trim(x, below=18, pre=0.06, post=0.15):
    """Trim room tone: keep from the first to the last 20 ms frame within `below` dB of the loudest, padded, 20 ms fades."""
    k = 960
    n = len(x) // k
    r = 20 * np.log10(np.sqrt((x[:n * k].reshape(n, k) ** 2).mean(1)) + 1e-9)
    on = np.nonzero(r > r.max() - below)[0]
    x = x[max(0, on[0] * k - int(pre * 48000)):min(len(x), (on[-1] + 1) * k + int(post * 48000))].copy()
    x[:k] *= np.linspace(0, 1, k)
    x[-k:] *= np.linspace(1, 0, k)
    return x


def write_wav(p, y):
    run(["ffmpeg", "-y", "-v", "error", "-f", "f32le", "-ar", "48000", "-ac", "1", "-i", "-", "-c:a", "pcm_s24le", str(p)],
        input=y.astype(np.float32).tobytes())


def make_d06():
    """The Loop's source: clip-02 lines and clip-03 'I am well.', silence-trimmed, joined with 0.3 s gaps."""
    parts = []
    for lid in ("D01", "D02", "D03"):
        x = speech_trim(read_wav(ROOT / f"work/pilot/audio/vo_v2/{lid}.wav"))
        parts += [x, np.zeros(int(0.3 * 48000), np.float32)]
        if lid == "D03":  # the loop's single "I am well."
            write_wav(ROOT / "work/pilot/audio/vo_v2/D03_loop.wav", x)
    y = np.concatenate(parts[:-1])
    write_wav(ROOT / "work/pilot/audio/vo_v2/D06.wav", y)
    return len(y) / 48000


def audio(tl):
    (ROOT / "work/pilot/audio/vo_v2").mkdir(parents=True, exist_ok=True)
    main = json.loads((ROOT / "work/pilot/audio/main.json").read_text())
    presets = main["presets"]
    v2 = copy.deepcopy(main)
    v2.update({"out": "work/pilot/audio/main_v2.wav", "subs": "work/pilot/subs_v2.json"})
    events, placed = [], {}
    for raw in main["events"]:
        lid = raw.get("id")
        if lid in LINES:
            r = resolve(raw, presets)
            clip, ls, le, shot = LINES[lid]
            s, e = extract(lid)
            if shot:  # on-screen: lip-sync to the picture actually used
                at = tl[shot][0] / FPS + (s - seg_start_frame(shot) / FPS)
                ev = {"at": round(at, 4), "type": "file", "path": f"work/pilot/audio/vo_v2/{lid}.wav", "norm": True,
                      "gain": r.get("gain", -12)}
            else:  # off-screen: v1 time and spatial treatment
                at = raw["at"] - (ls - s)
                ev = {"at": round(at, 4), "type": "file", "path": f"work/pilot/audio/vo_v2/{lid}.wav", "norm": True,
                      **{k: r[k] for k in SPATIAL if k in r}}
                if raw.get("use") == "PHONE":  # the phone band lives in PHONE's af, not af_post
                    ev["af_post"] = presets["PHONE"]["af"]
            ev.update({"bus": "dx", "id": lid, "text": raw["text"], "sub_start": round(at + ls - s, 2),
                       "sub_end": round(at + le - s + 0.3, 2)})
            for k in ("sub", "italic"):
                if k in raw:
                    ev[k] = raw[k]
            placed[lid] = ev
            events.append(ev)
        elif lid == "D06":
            continue
        elif raw.get("type") == "loop":
            continue
        else:
            events.append(raw)
    # The Loop, rebuilt from Seedance father audio (after D01-D03 exist)
    d06 = make_d06()
    main_d06 = next(e for e in main["events"] if e.get("id") == "D06")
    main_loop = next(e for e in main["events"] if e.get("type") == "loop")
    i = next(k for k, e in enumerate(events) if e.get("at", -1) > main_d06["at"])
    events[i:i] = [
        {"at": main_d06["at"], "type": "file", "path": "work/pilot/audio/vo_v2/D06.wav", "norm": True, "gain": 0,
         "af_post": FATHER_EQ, "bus": "dx", "id": "D06", "text": main_d06["text"], "sub": main_d06["sub"],
         "sub_end": main_d06["sub_end"], "italic": True, "overrun_ok": True},
        {"at": main_loop["at"], "type": "loop", "path": "work/pilot/audio/vo_v2/D03_loop.wav", "af_post": FATHER_EQ,
         "to": main_loop["to"], "gain": main_loop["gain"], "rise": main_loop["rise"], "bus": "dx"}]
    v2["events"] = events
    (ROOT / "work/pilot/audio/main_v2.json").write_text(json.dumps(v2, indent=1, ensure_ascii=False) + "\n")
    print("D06 length", round(d06, 2), "s")
    for lid, ev in sorted(placed.items()):
        print(lid, ev["at"], LINES[lid])


def match():
    """Level-match each Seedance line to its v1 say line: integrated loudness (ebur128) of each event rendered alone."""
    sys.path.insert(0, str(ROOT / "tools/audio"))
    import mix
    main = json.loads((ROOT / "work/pilot/audio/main.json").read_text())
    mix.CACHE = ROOT / main["cache"]
    spec_p = ROOT / "work/pilot/audio/main_v2.json"
    v2 = json.loads(spec_p.read_text())
    v1 = {e["id"]: mix.resolve(e, main["presets"]) for e in main["events"] if e.get("id")}
    tmp = ROOT / "work/pilot/audio/vo_v2/_tmp.wav"

    def lufs(e):
        e = dict(e, at=0.0)
        x, _ = mix.render(e, {}, np.ones(1))
        mix.write(tmp, x, "pcm_f32le")
        return mix.loudness(tmp)["I"]

    for e in v2["events"]:
        if e.get("type") == "file" and e.get("id") in v1:
            l1 = lufs(v1[e["id"]])
            g = e.get("gain", 0)
            l2 = lufs(dict(e, gain=0))
            e["gain"] = round(l1 - l2, 2)
            print(f"{e['id']} v1 {l1:6.1f} LUFS (gain {v1[e['id']].get('gain', -12)})  v2 raw {l2:6.1f}  gain {g} -> {e['gain']}")
    lp1 = lufs(mix.resolve(next(e for e in main["events"] if e.get("type") == "loop"), main["presets"]))
    for e in v2["events"]:
        if e.get("type") == "loop":
            l2 = lufs(dict(e, gain=0))
            g = e["gain"]
            e["gain"] = round(lp1 - l2, 2)
            print(f"loop v1 {lp1:6.1f} LUFS  v2 raw {l2:6.1f}  gain {g} -> {e['gain']}")
    tmp.unlink()
    spec_p.write_text(json.dumps(v2, indent=1, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    cache = ROOT / "work/pilot/comp_v2/v1_timeline.json"
    if cache.exists():
        tl, total = json.loads(cache.read_text())
    else:
        tl, total = v1_timeline()
        cache.write_text(json.dumps([tl, total]))
    print("v1 total frames", total)
    if what in ("video", "all"):
        video(tl)
    if what in ("audio", "all"):
        audio(tl)
        match()
    if what == "match":
        match()
