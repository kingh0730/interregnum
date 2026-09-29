"""Design voices with ElevenLabs Voice Design and pick a preview by measurement (Claude can't listen).

usage: uv run tools/audio/voice_design.py <spec.json> <outdir> [--save]
spec: {"<role>": {"description": "...", "text": "<100+ chars preview line>", "target": {"f0": [lo, hi], "age": true|false}}}
For each role: generates previews (3 per call; --rounds N for more), transcribes them (mlx-whisper), and measures:
  f0 median (Hz), f0 spread (semitones, lower = flatter delivery), jitter (%, higher = older-sounding),
  level spread (dB, lower = even).
Scores: transcript must match; then flatness first, age cues next when target.age. With --save, the best preview is
saved as a permanent voice in the account and its voice_id is written to <outdir>/voices.json.
Key: $ELEVENLABS_API_KEY_STARTER (King's paid account; required for anything that goes in the film).
"""
import argparse
import base64
import difflib
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

import numpy as np

API = "https://api.elevenlabs.io/v1"


def post(path, body, key):
    req = urllib.request.Request(API + path, data=json.dumps(body).encode(), method="POST",
                                 headers={"xi-api-key": key, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read())


def analyse(path):
    x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                                     capture_output=True).stdout, np.float32)
    n, hop = 640, 160
    f0, lv = [], []
    for i in range(0, len(x) - n, hop):
        s = x[i:i + n]
        r = np.sqrt((s ** 2).mean())
        if r < 0.01:
            continue
        s = s - s.mean()
        ac = np.correlate(s, s, "full")[n - 1:]
        lo, hi = 16000 // 450, 16000 // 65
        k = lo + np.argmax(ac[lo:hi])
        if ac[k] > 0.45 * ac[0]:
            f0.append(16000 / k)
            lv.append(20 * np.log10(r))
    f0 = np.array(f0)
    if len(f0) < 20:
        return None
    semis = 12 * np.log2(f0 / np.median(f0))
    d = np.abs(np.diff(f0)) / f0[1:]
    jitter = 100 * np.median(d[d < 0.1]) if (d < 0.1).any() else 0
    return {"f0": round(float(np.median(f0)), 1), "f0_spread_st": round(float(np.percentile(semis, 90) - np.percentile(semis, 10)), 2),
            "jitter_pct": round(float(jitter), 2), "level_spread_db": round(float(np.percentile(lv, 90) - np.percentile(lv, 10)), 1)}


def transcript(path):
    out = Path("/tmp/claude-501/vd_wh")
    subprocess.run(["uvx", "--from", "mlx-whisper", "mlx_whisper", str(path), "--model", "mlx-community/whisper-small-mlx",
                    "--language", "en", "--output-dir", str(out), "--output-format", "txt"], capture_output=True)
    f = out / (Path(path).stem + ".txt")
    return f.read_text().strip() if f.exists() else ""


def words(t):
    return re.sub(r"[^a-z' ]", " ", re.sub(r"\[[^\]]*\]", " ", t.lower())).split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("outdir")
    ap.add_argument("--rounds", type=int, default=1)
    ap.add_argument("--save", action="store_true")
    a = ap.parse_args()
    key = os.environ.get("ELEVENLABS_API_KEY_STARTER") or sys.exit("ELEVENLABS_API_KEY_STARTER not set")
    spec = json.loads(Path(a.spec).read_text())
    out = Path(a.outdir)
    out.mkdir(parents=True, exist_ok=True)
    vpath = out / "voices.json"
    voices = json.loads(vpath.read_text()) if vpath.exists() else {}
    for role, s in spec.items():
        cands = []
        for rnd in range(a.rounds):
            res = post("/text-to-voice/design", {"voice_description": s["description"], "model_id": s.get("model", "eleven_ttv_v3"),
                                                 "text": s["text"]}, key)
            for i, p in enumerate(res["previews"]):
                f = out / f"{role}_r{rnd}_{i}.mp3"
                f.write_bytes(base64.b64decode(p["audio_base_64"]))
                m = analyse(f) or {}
                tr = transcript(f)
                acc = difflib.SequenceMatcher(None, words(s["text"]), words(tr)).ratio()
                cands.append({"file": str(f), "generated_voice_id": p["generated_voice_id"], "text_match": round(acc, 3),
                              "transcript": tr, **m})
        t = s.get("target", {})
        def score(c):
            if c["text_match"] < 0.9 or "f0" not in c:
                return -1e9
            sc = -c["f0_spread_st"] - 0.3 * c["level_spread_db"]  # flatness: the anti-over-acting criterion
            lo, hi = t.get("f0", [0, 1e9])
            if not lo <= c["f0"] <= hi:
                sc -= 5 + abs(c["f0"] - (lo if c["f0"] < lo else hi)) / 10
            if t.get("age"):
                sc += 2.0 * c["jitter_pct"]  # older voices wobble more
            return sc
        for c in cands:
            c["score"] = round(score(c), 2)
        cands.sort(key=lambda c: -c["score"])
        (out / f"{role}_candidates.json").write_text(json.dumps(cands, indent=1))
        best = cands[0]
        print(f"== {role}: best {Path(best['file']).name} score {best['score']}  f0 {best.get('f0')}  spread {best.get('f0_spread_st')} st  "
              f"jitter {best.get('jitter_pct')}%  level {best.get('level_spread_db')} dB  match {best['text_match']}")
        for c in cands[1:]:
            print(f"   {Path(c['file']).name}: score {c['score']} f0 {c.get('f0')} spread {c.get('f0_spread_st')} jitter {c.get('jitter_pct')} match {c['text_match']}")
        if a.save and best["score"] > -1e8:
            saved = post("/text-to-voice", {"voice_name": f"INTERREGNUM {role}", "voice_description": s["description"],
                                             "generated_voice_id": best["generated_voice_id"]}, key)
            voices[role] = {"voice_id": saved["voice_id"], "from": Path(best["file"]).name, "metrics": {k: best.get(k) for k in
                            ("f0", "f0_spread_st", "jitter_pct", "level_spread_db")}}
            vpath.write_text(json.dumps(voices, indent=1))
            print("   saved as", saved["voice_id"])


if __name__ == "__main__":
    main()
