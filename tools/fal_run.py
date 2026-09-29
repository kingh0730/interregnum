"""Run any fal endpoint with a JSON payload and download every media file in the response.

usage: uv run tools/fal_run.py <endpoint_id> <payload.json | '{"inline": "json"}'> <out_prefix>
Writes <out_prefix>.json (request id, payload minus data URIs, full response) and <out_prefix>[_N].<ext> per media file.
Key from $FAL_KEY. Never re-POSTs on a network error (that would bill twice); polls with retries.
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


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
            if payload is not None or i == tries - 1:
                raise
            time.sleep(5 * (i + 1))


def media_urls(x):
    if isinstance(x, dict):
        for v in x.values():
            yield from media_urls(v)
    elif isinstance(x, list):
        for v in x:
            yield from media_urls(v)
    elif isinstance(x, str) and x.startswith("http") and any(
            x.split("?")[0].lower().endswith(e) for e in (".mp3", ".wav", ".flac", ".ogg", ".m4a", ".aac", ".mp4", ".mov", ".webm")):
        yield x


def main():
    ep, payload, prefix = sys.argv[1], sys.argv[2], Path(sys.argv[3])
    if Path(payload).is_file() and Path(payload).resolve() == prefix.with_suffix(".json").resolve():
        sys.exit("payload file would be overwritten by the log: choose a different out_prefix")
    payload = json.loads(Path(payload).read_text()) if Path(payload).is_file() else json.loads(payload)
    key = os.environ.get("FAL_KEY") or sys.exit("FAL_KEY is not set")
    prefix.parent.mkdir(parents=True, exist_ok=True)
    sub = call(f"https://queue.fal.run/{ep}", key, payload)
    clean = {k: (v if not (isinstance(v, str) and v.startswith("data:")) else "<data uri>") for k, v in payload.items()}
    log = {"endpoint": ep, "request_id": sub.get("request_id"), "payload": clean}
    prefix.with_suffix(".json").write_text(json.dumps(log, indent=1))
    t0 = time.time()
    while True:
        st = call(sub["status_url"], key)
        if st.get("status") == "COMPLETED":
            break
        if st.get("status") not in ("IN_QUEUE", "IN_PROGRESS") or time.time() - t0 > 1200:
            sys.exit(f"failed: {st}")
        time.sleep(4)
    res = call(sub["response_url"], key)
    log["response"] = res
    log["seconds"] = round(time.time() - t0, 1)
    prefix.with_suffix(".json").write_text(json.dumps(log, indent=1))
    urls = list(dict.fromkeys(media_urls(res)))
    for i, u in enumerate(urls):
        ext = Path(u.split("?")[0]).suffix
        dst = prefix.parent / f"{prefix.name}{'' if i == 0 else f'_{i}'}{ext}"
        urllib.request.urlretrieve(u, dst)
        print(dst)
    if not urls:
        print("no media in response:", json.dumps(res)[:300])


if __name__ == "__main__":
    main()
