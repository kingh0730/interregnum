"""Perform the dialogue takes with the cast voices and keep the flattest correct take (Claude can't listen).

usage: uv run tools/audio/perform.py <dialogue.json> <voices.json> <outdir> [--seeds 3] [--only T01,T05]
- Voices: designed voice ids from voices.json (FATHER, IDA, NANA); stock voices by id for the rest (STOCK below).
- Model eleven_v4 on King's Starter account ($ELEVENLABS_API_KEY_STARTER): the only account with a commercial licence.
- Selection: the transcript must match the script (tags removed), then the lowest pitch spread + level spread wins:
  the anti-over-acting rule (behaviour, not emotion; the context carries the feeling).
Writes <outdir>/<take>_<seed>.mp3, <outdir>/selection.json.
"""
import argparse
import difflib
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from voice_design import analyse, transcript, words  # noqa: E402

STOCK = {"Sarah": "EXAVITQu4vr4xnSDxMaL", "Matilda": "XrExE9yKIg1WjnnlVkGX", "Jessica": "cgSgspJ2msm6clMCkdW9",
         "Roger": "CwhRBWXzGAHq8TQ4Fs17", "Eric": "cjVigY5qzO86Huf0OWal", "Chris": "iP95p4xoKVk53GoZ742B",
         "Will": "bIHbv24MWmeRgasZH58o", "Liam": "TX3LPaxmHKxFdv7VOQHJ", "Laura": "FGY2WhTYpPnrIDTdsKH5",
         "Aria": "9BWtsMINqrJLrRacOk9x", "Brian": "nPczCjzI2devNBz1zQrb", "Bill": "pqHfZKP75CvOlQylNhV4",
         "River": "SAz9YHcvj6GT2YYXdXww", "Callum": "N2lVS1w4EtoT3dr4eOWO", "Bella": "hpp4J3VqNfWAUOO0d1Us"}
# stability raised above the plan for the living characters: flatter reads (King's over-acting note)
STABILITY = {"FATHER": 0.85, "IDA": 0.65, "NANA": 0.6, "PA": 0.9, "CITY": 0.55}


def tts(text, voice_id, settings, seed, out, key):
    body = {"text": text, "model_id": "eleven_v4", "seed": seed, "voice_settings": settings}
    for attempt in range(5):
        req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}?output_format=mp3_44100_128",
                                     data=json.dumps(body).encode(), method="POST",
                                     headers={"xi-api-key": key, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                Path(out).write_bytes(r.read())
            return True
        except urllib.error.HTTPError as e:
            msg = e.read().decode()[:300]
            if e.code == 429:
                time.sleep(4 * (attempt + 1))
                continue
            print("  HTTP", e.code, msg)
            return False
    return False


def spoken(text):
    return re.sub(r"/[^/]+/", "nana", text)  # IPA spans are read as the word they spell (here only Nana)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dialogue")
    ap.add_argument("voices")
    ap.add_argument("outdir")
    ap.add_argument("--seeds", type=int, default=3)
    ap.add_argument("--only")
    a = ap.parse_args()
    key = os.environ.get("ELEVENLABS_API_KEY_STARTER") or sys.exit("ELEVENLABS_API_KEY_STARTER not set")
    d = json.loads(Path(a.dialogue).read_text())
    cast = json.loads(Path(a.voices).read_text())
    out = Path(a.outdir)
    out.mkdir(parents=True, exist_ok=True)
    selp = out / "selection.json"
    sel = json.loads(selp.read_text()) if selp.exists() else {}
    only = set(a.only.split(",")) if a.only else None
    jobs = []
    for t in d["takes"]:
        if only and t["id"] not in only:
            continue
        v = d["voices"][t["speaker"]]
        if t["speaker"] == "CITY":  # one request per W line, each in its own stock voice
            for ln in d["lines"]:
                if ln.get("take") == t["id"]:
                    name = next((n for n in STOCK if n.lower() in json.dumps(ln).lower()), "Chris")
                    jobs.append((ln["id"], "CITY", ln["text"], STOCK[name], v))
            continue
        vid = cast[t["speaker"]]["voice_id"] if t["speaker"] in cast else STOCK[v["voice"]]
        jobs.append((t["id"], t["speaker"], t["text"], vid, v))
    for tid, spk, text, vid, v in jobs:
        settings = {"stability": STABILITY[spk], "similarity_boost": v.get("similarity_boost", 0.8), "speed": v.get("speed", 1.0)}
        cands = []
        for k in range(a.seeds):
            seed = int(v.get("seed", 1000)) + k
            f = out / f"{tid}_{seed}.mp3"
            if not f.exists() and not tts(text, vid, settings, seed, f, key):
                continue
            m = analyse(f) or {}
            tr = transcript(f)
            ref = words(spoken(text))
            acc = difflib.SequenceMatcher(None, ref, words(tr)).ratio() if ref else 1.0
            flat = -(m.get("f0_spread_st", 99) + 0.3 * m.get("level_spread_db", 99))
            cands.append({"file": f.name, "seed": seed, "text_match": round(acc, 3), "transcript": tr, **m,
                          "score": round(flat if acc >= 0.85 else flat - 1000, 2)})
        cands.sort(key=lambda c: -c["score"])
        sel[tid] = {"speaker": spk, "voice_id": vid, "settings": settings, "best": cands[0] if cands else None, "candidates": cands}
        selp.write_text(json.dumps(sel, indent=1))
        b = cands[0] if cands else {}
        print(f"{tid:4s} {spk:6s} best seed {b.get('seed')} match {b.get('text_match')} spread {b.get('f0_spread_st')} st  "
              f"level {b.get('level_spread_db')} dB  | {b.get('transcript', '')[:70]}")


if __name__ == "__main__":
    main()
