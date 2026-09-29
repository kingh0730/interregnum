"""Image-to-video through fal.ai (Seedance 2.5). Key from $FAL_KEY only.

usage: uv run tools/video/i2v.py <start.png> <out.mp4> "<prompt>" [--dur 6] [--res 720p] [--end end.png]
                                 [--seed N] [--no-audio] [--aspect 16:9] [--model bytedance/seedance-2.5/image-to-video]
       --ref-audio voice.wav  switches to reference-to-video: the start image becomes [Image1] and the audio [Audio1]
                              (write the prompt to use them, e.g. "[Image1] is the exact first frame ... voice of [Audio1]").
Writes <out>.json next to the take (model, prompt, seed, cost estimate, request id).
Cost: $0.0214 per 1000 tokens, tokens = h*w*dur*24/1024 (~$0.47/s at 720p 16:9, ~$0.22/s at 480p).
"""
import argparse
import base64
import io
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

from PIL import Image

RES = {"480p": (854, 480), "720p": (1280, 720)}


def data_uri(path):
    im = Image.open(path).convert("RGB")
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=93)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def audio_uri(path):
    return "data:audio/wav;base64," + base64.b64encode(Path(path).read_bytes()).decode()


def call(url, key, payload=None):
    req = urllib.request.Request(url, data=json.dumps(payload).encode() if payload is not None else None,
                                 headers={"Authorization": f"Key {key}", "Content-Type": "application/json"},
                                 method="POST" if payload is not None else "GET")
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("start")
    ap.add_argument("out")
    ap.add_argument("prompt")
    ap.add_argument("--dur", type=int, default=6)
    ap.add_argument("--res", default="720p")
    ap.add_argument("--end")
    ap.add_argument("--seed", type=int)
    ap.add_argument("--no-audio", action="store_true")
    ap.add_argument("--aspect", default="16:9")
    ap.add_argument("--model", default="bytedance/seedance-2.5/image-to-video")
    ap.add_argument("--ref-audio")
    a = ap.parse_args()
    key = os.environ.get("FAL_KEY")
    if not key:
        sys.exit("FAL_KEY is not set")
    w, h = RES[a.res]
    est = h * w * a.dur * 24 / 1024 / 1000 * 0.0214
    payload = {"image_url": data_uri(a.start), "prompt": a.prompt, "duration": str(a.dur), "resolution": a.res,
               "aspect_ratio": a.aspect, "generate_audio": not a.no_audio}
    if a.ref_audio:
        a.model = "bytedance/seedance-2.5/reference-to-video"
        payload["image_urls"] = [payload.pop("image_url")]
        payload["audio_urls"] = [audio_uri(a.ref_audio)]
    if a.end:
        payload["end_image_url"] = data_uri(a.end)
    if a.seed is not None:
        payload["seed"] = a.seed
    print(f"submitting {a.model} {a.res} {a.dur}s  est ${est:.2f}", flush=True)
    sub = call(f"https://queue.fal.run/{a.model}", key, payload)
    t0 = time.time()
    while True:
        st = call(sub["status_url"], key)
        if st.get("status") == "COMPLETED":
            break
        if st.get("status") not in ("IN_QUEUE", "IN_PROGRESS"):
            sys.exit(f"failed: {st}")
        if time.time() - t0 > 1800:
            sys.exit(f"timeout; request {sub.get('request_id')}")
        time.sleep(10)
    res = call(sub["response_url"], key)
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(res["video"]["url"], out)
    log = {k: v for k, v in payload.items() if not k.endswith(("image_url", "image_urls", "audio_urls"))}
    log.update(model=a.model, start=a.start, end=a.end, ref_audio=a.ref_audio, seed=res.get("seed"), request_id=sub.get("request_id"),
               est_usd=round(est, 2), seconds=round(time.time() - t0))
    out.with_suffix(".json").write_text(json.dumps(log, indent=1))
    print(out, f"seed={res.get('seed')}", f"{log['seconds']}s", flush=True)


if __name__ == "__main__":
    main()
