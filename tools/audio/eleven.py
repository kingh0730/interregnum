"""ElevenLabs on fal: TTS (Eleven v4), sound effects, music, voice changer. Key from $FAL_KEY only.

usage:
  uv run tools/audio/eleven.py tts   <out.wav> "<text with [tags]>" --voice Bill [--stability .5] [--similarity .75] [--seed N]
  uv run tools/audio/eleven.py sfx   <out.wav> "<prompt>" [--dur 4] [--loop] [--influence .5]
  uv run tools/audio/eleven.py music <out.wav> --plan plan.json | --prompt "..." [--ms 60000] [--instrumental]
  uv run tools/audio/eleven.py vc    <out.wav> <in.wav> --voice Bill
Every output is converted to 48 kHz WAV, with a <out>.json log next to it (endpoint, request id, inputs, cost estimate).
Prices (fal, 2026-09-29): TTS $0.04 per 1k chars; SFX $0.002/s; music $0.60/min; voice changer $0.30/min.
"""
import argparse
import base64
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

EP = {"tts": "elevenlabs/tts/eleven-v4-turbo", "sfx": "fal-ai/elevenlabs/sound-effects/v2",
      "music": "fal-ai/elevenlabs/music", "vc": "fal-ai/elevenlabs/voice-changer"}


def _call(url, key, payload=None):
    req = urllib.request.Request(url, data=json.dumps(payload).encode() if payload is not None else None,
                                 headers={"Authorization": f"Key {key}", "Content-Type": "application/json"},
                                 method="POST" if payload is not None else "GET")
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())


def call(url, key, payload=None, tries=6):
    for i in range(tries):
        try:
            return _call(url, key, payload)
        except (urllib.error.URLError, ConnectionError, TimeoutError):
            if payload is not None or i == tries - 1:  # never re-submit a POST: it would bill twice
                raise
            time.sleep(5 * (i + 1))


def run(kind, payload, out, est):
    key = os.environ.get("FAL_KEY") or sys.exit("FAL_KEY is not set")
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    sub = call(f"https://queue.fal.run/{EP[kind]}", key, payload)
    log = {"endpoint": EP[kind], "request_id": sub.get("request_id"), "est_usd": round(est, 4),
           "input": {k: v for k, v in payload.items() if k != "audio_url"}}
    out.with_suffix(".json").write_text(json.dumps(log, indent=1))
    t0 = time.time()
    while True:
        st = call(sub["status_url"], key)
        if st.get("status") == "COMPLETED":
            break
        if st.get("status") not in ("IN_QUEUE", "IN_PROGRESS") or time.time() - t0 > 900:
            sys.exit(f"failed: {st}")
        time.sleep(3)
    res = call(sub["response_url"], key)
    url = (res.get("audio") or res.get("audio_file") or {}).get("url")
    if not url:
        sys.exit(f"no audio in response: {json.dumps(res)[:300]}")
    raw = out.with_suffix(".src" + Path(url.split("?")[0]).suffix)
    urllib.request.urlretrieve(url, raw)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(raw), "-ar", "48000", "-c:a", "pcm_f32le", str(out)], check=True)  # float: mp3 overshoot must not clip
    raw.unlink()
    log.update(seconds=round(time.time() - t0, 1), seed=res.get("seed"))
    out.with_suffix(".json").write_text(json.dumps(log, indent=1))
    print(out, f"~${est:.4f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=EP)
    ap.add_argument("out")
    ap.add_argument("text", nargs="?")
    ap.add_argument("--voice", default="Rachel")
    ap.add_argument("--stability", type=float)
    ap.add_argument("--similarity", type=float)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--dur", type=float)
    ap.add_argument("--loop", action="store_true")
    ap.add_argument("--influence", type=float)
    ap.add_argument("--plan")
    ap.add_argument("--prompt")
    ap.add_argument("--ms", type=int)
    ap.add_argument("--instrumental", action="store_true")
    a = ap.parse_args()
    if a.kind == "tts":
        p = {"text": a.text, "voice": a.voice, "output_format": "mp3_44100_192"}
        for k, v in (("stability", a.stability), ("similarity_boost", a.similarity), ("seed", a.seed)):
            if v is not None:
                p[k] = v
        run("tts", p, a.out, len(a.text) / 1000 * 0.04)
    elif a.kind == "sfx":
        p = {"text": a.text, "output_format": "mp3_44100_192", "loop": a.loop}
        if a.dur:
            p["duration_seconds"] = a.dur
        if a.influence is not None:
            p["prompt_influence"] = a.influence
        run("sfx", p, a.out, (a.dur or 5) * 0.002)
    elif a.kind == "music":
        p = {"output_format": "mp3_44100_192"}
        if a.plan:
            plan = json.loads(Path(a.plan).read_text())
            p["composition_plan"] = plan
            p["respect_sections_durations"] = True
            ms = sum(s["duration_ms"] for s in plan["sections"])
        else:
            p["prompt"] = a.prompt
            ms = a.ms or 60000
            p["music_length_ms"] = ms
        if a.instrumental:
            p["force_instrumental"] = True
        run("music", p, a.out, ms / 60000 * 0.6)
    elif a.kind == "vc":
        src = Path(a.text)
        p = {"audio_url": "data:audio/wav;base64," + base64.b64encode(src.read_bytes()).decode(), "voice": a.voice,
             "output_format": "mp3_44100_192"}
        dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                    str(src)], capture_output=True, text=True).stdout)
        run("vc", p, a.out, dur / 60 * 0.3)


if __name__ == "__main__":
    main()
