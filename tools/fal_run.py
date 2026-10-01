"""Run any fal endpoint with a JSON payload and download every media file in the response.

usage: uv run tools/fal_run.py <endpoint_id> <payload.json | '{"inline": "json"}'> <out_prefix>
Writes <out_prefix>.json (request id, payload minus data URIs, full response) and <out_prefix>[_N].<ext> per media file.
Add --resume to poll/download an existing logged request without another POST.
Batch-generated input files use --request-envelope and contain {"endpoint": ..., "payload": {...}};
the endpoint and payload are read together under the request lock before any submission.
Key from $FAL_KEY. Never re-POSTs on a network error (that would bill twice); polls with retries.
"""
import json
import hashlib
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from request_state import file_lock, read_log, save_log

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
            x.split("?")[0].lower().endswith(e) for e in (".mp3", ".wav", ".flac", ".ogg", ".m4a", ".aac", ".mp4", ".mov", ".webm", ".png", ".jpg", ".jpeg", ".webp")):
        yield x


def main():
    ep, payload, prefix = sys.argv[1], sys.argv[2], Path(sys.argv[3])
    options = sys.argv[4:]
    key = os.environ.get("FAL_KEY") or sys.exit("FAL_KEY is not set")
    prefix.parent.mkdir(parents=True, exist_ok=True)
    # The batch process can die while this child survives. Lock the request in
    # the child too, so a restarted batch cannot race its submission/download.
    with file_lock(prefix.with_suffix('.request.lock')):
        # Read mutable inputs only after locking, alongside the corresponding log.
        # Long inline JSON may exceed the filesystem name limit.
        try:
            is_file = Path(payload).is_file()
        except OSError:
            is_file = False
        if is_file and Path(payload).resolve() == prefix.with_suffix(".json").resolve():
            sys.exit("payload file would be overwritten by the log: choose a different out_prefix")
        payload = json.loads(Path(payload).read_text()) if is_file else json.loads(payload)
        if '--request-envelope' in options:
            # Batch input binds endpoint and payload in one atomic file. An older
            # child must not send a newly prepared payload to its old endpoint.
            if payload['endpoint'] != ep:
                sys.exit('request endpoint changed before startup; rerun the batch')
            payload = payload['payload']
        run_request(ep, payload, prefix, key, resume="--resume" in options)


def run_request(ep, payload, prefix, key, resume=False):
    lp = prefix.with_suffix(".json")
    clean = {k: (v if not (isinstance(v, str) and v.startswith("data:")) else "<data uri>") for k, v in payload.items()}
    payload_sha256 = hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":"),
                                               ensure_ascii=False).encode()).hexdigest()
    log = read_log(lp) if resume else {}
    if log:
        if log.get("endpoint") != ep or log.get("payload") != clean:
            sys.exit("existing request differs from payload; use a new output prefix")
        if log.get("payload_sha256"):
            if log["payload_sha256"] != payload_sha256:
                sys.exit("existing request differs from full payload; use a new output prefix")
        elif any(v == "<data uri>" for v in log.get("payload", {}).values()):
            sys.exit("legacy data URI payload has no identity hash; recover manually instead of uncertain resume")
        if not log.get("response") and not all(log.get(k) for k in ("request_id", "status_url", "response_url")):
            sys.exit("unresolved submission or legacy log: recover its request manually; refusing another POST")
    else:
        # Persist before POST: an interrupted response may still represent a paid request.
        log = {"endpoint": ep, "payload": clean, "payload_sha256": payload_sha256, "submission_pending": True}
        save_log(lp, log)
        sub = call(f"https://queue.fal.run/{ep}", key, payload)
        log.update({k: sub.get(k) for k in ("request_id", "status_url", "response_url")})
        log.pop("submission_pending", None)
        save_log(lp, log)
    t0 = time.time()
    while not log.get("response"):
        st = call(log["status_url"], key)
        if st.get("status") == "COMPLETED":
            break
        if st.get("status") not in ("IN_QUEUE", "IN_PROGRESS") or time.time() - t0 > 1200:
            sys.exit(f"failed: {st}")
        time.sleep(4)
    res = log.get("response") or call(log["response_url"], key)
    log["response"] = res
    log["seconds"] = round(time.time() - t0, 1)
    save_log(lp, log)
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
