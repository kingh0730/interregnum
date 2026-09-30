"""Perform a dialogue.json with registers (v2 of perform.py): designed or stock voices, per-register settings,
take-level overrides, Mandarin support, and inverted selection for deliberately over-performed takes.

usage: uv run tools/audio/perform2.py <dialogue.json> <voices.json> <outdir> [--seeds 3] [--only SPEAKER|TAKE,...] [--lang zh]
- Settings: speaker defaults < register < take["settings"]. The voice: voices.json[speaker]["voice_id"] (designed) or
  a stock voice named in dialogue.json voices[speaker]["voice"].
- Selection (Claude can't listen): the transcript must match (tags dropped; digits and 幺 normalised), then the
  flattest take (lowest pitch plus level spread) wins, except takes marked over-performed (note contains "inverted",
  or take["select"] == "widest"), where the widest spread wins.
- Key: $ELEVENLABS_API_KEY_STARTER (the commercial licence). Writes <outdir>/<take>_<seed>.mp3 and selection.json.
"""
import argparse
import difflib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import voice_design  # noqa: E402
from voice_design import analyse, transcript  # noqa: E402

STOCK = {"Sarah": "EXAVITQu4vr4xnSDxMaL", "Matilda": "XrExE9yKIg1WjnnlVkGX", "Jessica": "cgSgspJ2msm6clMCkdW9",
         "Roger": "CwhRBWXzGAHq8TQ4Fs17", "Eric": "cjVigY5qzO86Huf0OWal", "Chris": "iP95p4xoKVk53GoZ742B",
         "Will": "bIHbv24MWmeRgasZH58o", "Liam": "TX3LPaxmHKxFdv7VOQHJ", "Laura": "FGY2WhTYpPnrIDTdsKH5",
         "Brian": "nPczCjzI2devNBz1zQrb", "Bill": "pqHfZKP75CvOlQylNhV4", "River": "SAz9YHcvj6GT2YYXdXww",
         "Callum": "N2lVS1w4EtoT3dr4eOWO", "Bella": "hpp4J3VqNfWAUOO0d1Us", "Alice": "Xb7hH8MSUJpSbSDYk0k2",
         "Lily": "pFZP5JQG7iQjIQuC4Bku", "George": "JBFqnCBsd6RMkjVDRZzb", "Daniel": "onwK4e9ZLuTAKqWW03F9",
         "Charlie": "IKne3meq5aSn9XLyUdCD", "Adam": "pNInz6obpgDQGcFmaJgB"}
DIG = str.maketrans({"0": "零", "1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七", "8": "八", "9": "九",
                     "幺": "一", "〇": "零", "两": "二"})


def norm_chars(t):
    t = re.sub(r"\[[^\]]*\]", " ", t).translate(DIG)
    return re.findall(r"[一-鿿]", t) if voice_design.LANG == "zh" else re.sub(r"[^a-z' ]", " ", t.lower()).split()


def tts(text, voice_id, settings, seed, out, key, prev=None, nxt=None):
    body = {"text": text, "model_id": "eleven_v4", "seed": seed, "voice_settings": settings}
    # request stitching: neighbouring lines as context keep one train of thought and a steady accent (v4 accepts them)
    if prev:
        body["previous_text"] = prev
    if nxt:
        body["next_text"] = nxt
    for attempt in range(6):
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
        except (urllib.error.URLError, ConnectionError, TimeoutError):
            time.sleep(5 * (attempt + 1))
    return False


def settings_for(d, take):
    v = d["voices"][take["speaker"]]
    s = {k: v[k] for k in ("stability", "similarity_boost", "speed") if k in v}
    reg = v.get("registers", {}).get(take.get("register"), {})
    s.update({k: reg[k] for k in ("stability", "similarity_boost", "speed") if k in reg})
    s.update({k: val for k, val in take.get("settings", {}).items() if k in ("stability", "similarity_boost", "speed")})
    return s, int(take.get("seed", reg.get("seed", v.get("seed", 1000))))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dialogue")
    ap.add_argument("voices")
    ap.add_argument("outdir")
    ap.add_argument("--seeds", type=int, default=3)
    ap.add_argument("--only")
    ap.add_argument("--lang", default="en")
    a = ap.parse_args()
    voice_design.LANG = a.lang
    key = os.environ.get("ELEVENLABS_API_KEY_STARTER") or sys.exit("ELEVENLABS_API_KEY_STARTER not set")
    d = json.loads(Path(a.dialogue).read_text())
    cast = json.loads(Path(a.voices).read_text()) if Path(a.voices).exists() else {}
    out = Path(a.outdir)
    out.mkdir(parents=True, exist_ok=True)
    selp = out / "selection.json"
    sel = json.loads(selp.read_text()) if selp.exists() else {}
    only = set(a.only.split(",")) if a.only else None
    plain = [re.sub(r"\[[^\]]*\]", "", x["text"]).strip() for x in d["takes"]]
    for ti, t in enumerate(d["takes"]):
        prev = t.get("previous_text", plain[ti - 1] if ti > 0 else None)
        nxt = t.get("next_text", plain[ti + 1] if ti + 1 < len(plain) else None)
        if only and t["id"] not in only and t["speaker"] not in only:
            continue
        spk = t["speaker"]
        stock = d["voices"][spk].get("voice")
        vid = cast.get(spk, {}).get("voice_id") or STOCK.get(stock)
        if not vid:
            print(f"{t['id']}: no voice for {spk} (designed voice not in voices.json, stock '{stock}' unknown); skipped")
            continue
        text = t["text"]
        if not re.search(r"[一-鿿A-Za-z]", re.sub(r"\[[^\]]*\]", "", text)):  # breath or laugh only: no transcript check
            ref = []
        else:
            ref = norm_chars(text)
        settings, seed0 = settings_for(d, t)
        widest = t.get("select") == "widest" or "inverted" in t.get("note", "").lower()
        cands = []
        for k in range(a.seeds):
            seed = seed0 + k
            f = out / f"{t['id']}_{seed}.mp3"
            if not f.exists() and not tts(text, vid, settings, seed, f, key, prev or None, nxt or None):
                continue
            m = analyse(f) or {}
            tr = transcript(f) if ref else ""
            acc = difflib.SequenceMatcher(None, ref, norm_chars(tr)).ratio() if ref else 1.0
            spread = m.get("f0_spread_st", 0 if not ref else 99) + 0.3 * m.get("level_spread_db", 0 if not ref else 99)
            score = (spread if widest else -spread) - (0 if acc >= 0.85 else 1000)
            cands.append({"file": f.name, "seed": seed, "text_match": round(acc, 3), "transcript": tr, **m, "score": round(score, 2)})
        passing = [c for c in cands if c["text_match"] >= 0.85]
        # if no take passes the transcript check, the best match wins first (then flatness): mumbled registers
        # can fail everywhere on one misheard word, and a wrong word matters more than a flat read
        cands.sort(key=lambda c: -c["score"]) if passing else cands.sort(key=lambda c: (-c["text_match"], -c["score"]))
        sel[t["id"]] = {"speaker": spk, "register": t.get("register"), "voice_id": vid, "settings": settings,
                        "select": "widest" if widest else "flattest", "best": cands[0] if cands else None, "candidates": cands}
        selp.write_text(json.dumps(sel, indent=1, ensure_ascii=False))
        b = cands[0] if cands else {}
        print(f"{t['id']:4s} {spk:6s} {str(t.get('register')):12s} best seed {b.get('seed')} match {b.get('text_match')} "
              f"spread {b.get('f0_spread_st')} st | {b.get('transcript', '')[:40]}")


if __name__ == "__main__":
    main()
