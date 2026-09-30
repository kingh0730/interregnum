"""Run a MiniMax H3 Max (or any fal video endpoint) motion manifest: parallel, resumable, never billing twice.

usage: uv run tools/video/h3_batch.py <motion_plan.json> [--root DIR] [--jobs 4] [--only id1,id2] [--redo id1,id2]
                                     [--dry-run] [--timeout 900]

Manifest: a JSON list of jobs, or {"defaults": {...}, "jobs": [...]}. Defaults are merged under every job.
A job:
  id          unique name
  endpoint    fal endpoint; aliases: "i2v" (minimax/h3-max/image-to-video), "lipsync"
              (minimax/h3-max/lip-sync/image-to-video), "ray" (luma/agent/ray/v3.2/image-to-video)
  image       start frame: an http URL, a local path (sent as a data URI), or {"job": id} for the LAST frame of
              another job's output, or {"job": id, "t": seconds} for the frame at t (chained takes; that job becomes a
              dependency)
  end_image   optional end frame, same forms
  audio       optional local audio file; sent as an MP3 data URI, as "audio_url" (lipsync) or "target_audio_url"
              (i2v). Nothing else is uploaded.
  prompt, duration, resolution, prompt_expansion_mode, seed, params (extra payload keys, passed through)
  out         output mp4, relative to --root (default: the manifest's directory's parent)
  deps        optional extra dependencies (job ids)
Price per second comes from the fal pricing API (lipsync bills the audio's length).

Money safety:
- The request id, status and response URLs are written to <manifest dir>/h3_log/<id>.json the moment fal accepts the
  POST, before any polling. A re-run polls that request instead of POSTing again.
- A request still IN_QUEUE/IN_PROGRESS after --timeout seconds is cancelled (best effort) and resubmitted once per
  attempt; a COMPLETED request is only ever fetched, never re-POSTed.
- --redo moves the old output to <out>.takeN.mp4 (so earlier takes stay comparable) and starts a new request.
Every submitted request is appended to <manifest dir>/h3_log/ledger.jsonl with its billable seconds and price.
"""
import argparse
import base64
import json
import os
import subprocess
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ALIAS = {"i2v": "minimax/h3-max/image-to-video", "lipsync": "minimax/h3-max/lip-sync/image-to-video",
         "ray": "luma/agent/ray/v3.2/image-to-video", "camera": "minimax/h3-max/camera-controls"}
PRICE_FALLBACK = {"minimax/h3-max/image-to-video": 0.025, "minimax/h3-max/lip-sync/image-to-video": 0.05,
                  "luma/agent/ray/v3.2/image-to-video": 0.03}
LOCK = threading.Lock()


def http(url, key, payload=None, method=None, tries=6):
    for i in range(tries):
        req = urllib.request.Request(url, data=json.dumps(payload).encode() if payload is not None else None,
                                     headers={"Authorization": f"Key {key}", "Content-Type": "application/json"},
                                     method=method or ("POST" if payload is not None else "GET"))
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read() or b"{}")
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors="replace")[:500]
            if payload is not None or e.code < 500 or i == tries - 1:
                raise RuntimeError(f"HTTP {e.code} {url}: {body}")
        except (urllib.error.URLError, ConnectionError, TimeoutError):
            if payload is not None or i == tries - 1:  # never retry a POST: it may have been accepted
                raise
        time.sleep(5 * (i + 1))


def price(ep, key, cache={}):
    if ep not in cache:
        try:
            r = http(f"https://api.fal.ai/v1/models/pricing?endpoint_id={ep}", key)
            cache[ep] = float(r["prices"][0]["unit_price"])
        except Exception:
            cache[ep] = PRICE_FALLBACK.get(ep, 0.05)
    return cache[ep]


def probe_dur(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                       capture_output=True, text=True)
    return float(r.stdout.strip() or 0)


def data_uri_image(p):
    p = Path(p)
    with tempfile.TemporaryDirectory() as td:
        j = Path(td) / "i.jpg"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(p), "-q:v", "2", str(j)], check=True)
        return "data:image/jpeg;base64," + base64.b64encode(j.read_bytes()).decode()


def data_uri_audio(p):
    with tempfile.TemporaryDirectory() as td:
        m = Path(td) / "a.mp3"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(p), "-ac", "1", "-ar", "44100", "-b:a", "192k",
                        str(m)], check=True)
        return "data:audio/mpeg;base64," + base64.b64encode(m.read_bytes()).decode()


def last_frame(mp4, dst):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-sseof", "-0.1", "-i", str(mp4), "-frames:v", "1", "-update", "1",
                    str(dst)], check=True)
    return dst


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest")
    ap.add_argument("--root")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--only", default="")
    ap.add_argument("--redo", default="")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--timeout", type=int, default=900)
    a = ap.parse_args()
    man_path = Path(a.manifest).resolve()
    root = Path(a.root).resolve() if a.root else man_path.parent.parent
    doc = json.loads(man_path.read_text())
    defaults = doc.get("defaults", {}) if isinstance(doc, dict) else {}
    jobs = [dict(defaults, **j) for j in (doc["jobs"] if isinstance(doc, dict) else doc)]
    by_id = {j["id"]: j for j in jobs}
    logdir = man_path.parent / "h3_log"
    logdir.mkdir(parents=True, exist_ok=True)
    ledger = logdir / "ledger.jsonl"
    only = set(filter(None, a.only.split(",")))
    redo = set(filter(None, a.redo.split(",")))
    key = os.environ.get("FAL_KEY") or sys.exit("FAL_KEY is not set")

    def ep_of(j):
        return ALIAS.get(j.get("endpoint", "i2v"), j.get("endpoint", "i2v"))

    def out_of(j):
        return root / j["out"]

    def deps_of(j):
        d = set(j.get("deps", []))
        for k in ("image", "end_image"):
            if isinstance(j.get(k), dict):
                d.add(j[k]["job"])
        return d

    def billable(j):
        if ep_of(j).endswith("lip-sync/image-to-video"):
            return max(5.0, probe_dur(root / j["audio"]))
        d = j.get("duration", 5)
        return float(str(d).rstrip("s"))

    sel = [j for j in jobs if not only or j["id"] in only]
    todo = [j for j in sel if j["id"] in redo or not out_of(j).exists()]
    est = sum(billable(j) * price(ep_of(j), key) for j in todo)
    for j in todo:
        print(f"plan {j['id']:<14} {ep_of(j):<42} {billable(j):5.1f} s  ${billable(j) * price(ep_of(j), key):.3f}")
    print(f"{len(todo)} jobs, estimated ${est:.2f}", flush=True)
    if a.dry_run:
        return

    def media(v, j):
        if isinstance(v, dict):
            src = out_of(by_id[v["job"]])
            dst = logdir / f"{j['id']}.from_{v['job']}.png"
            if v.get("t") is not None:  # a chosen frame (the join point of a chain), not the last one
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{v['t']:.3f}", "-i", str(src), "-frames:v", "1",
                                str(dst)], check=True)
                return data_uri_image(dst)
            return data_uri_image(last_frame(src, dst))
        if isinstance(v, str) and v.startswith("http"):
            return v
        return data_uri_image(root / v)

    def build(j):
        ep = ep_of(j)
        p = dict(j.get("params", {}))
        if ep.endswith("lip-sync/image-to-video"):
            p.update(image_url=media(j["image"], j), audio_url=data_uri_audio(root / j["audio"]))
            p.setdefault("resolution", j.get("resolution", "768P"))
        else:
            p["prompt"] = j["prompt"]
            if j.get("image"):
                p["image_url"] = media(j["image"], j)
            if j.get("end_image"):
                p["end_image_url"] = media(j["end_image"], j)
            if ep.startswith("minimax/"):
                p["duration"] = int(j.get("duration", 5))
                p["resolution"] = j.get("resolution", "768P")
                p["prompt_expansion_mode"] = j.get("prompt_expansion_mode", "disabled")
                if j.get("audio"):
                    p["target_audio_url"] = data_uri_audio(root / j["audio"])
            else:
                p.setdefault("duration", f"{int(j.get('duration', 5))}s")
                p.setdefault("resolution", j.get("resolution", "720p"))
                p.setdefault("aspect_ratio", "16:9")
        if j.get("seed") is not None:
            p["seed"] = j["seed"]
        return ep, p

    def clean(p):
        return {k: ("<data uri>" if isinstance(v, str) and v.startswith("data:") else v) for k, v in p.items()}

    def fetch(log, j):
        res = http(log["response_url"], key)
        log["response"] = res
        url = (res.get("video") or {}).get("url")
        if not url:
            raise RuntimeError(f"no video in response: {json.dumps(res)[:300]}")
        out = out_of(j)
        out.parent.mkdir(parents=True, exist_ok=True)
        tmp = out.with_suffix(".part.mp4")
        urllib.request.urlretrieve(url, tmp)
        tmp.replace(out)
        log["done"] = time.time()
        return out

    def run(j):
        i = j["id"]
        lp = logdir / f"{i}.json"
        log = json.loads(lp.read_text()) if lp.exists() else {}
        if i in redo and log.get("request_id"):
            hist = logdir / f"{i}.history.jsonl"
            with open(hist, "a") as f:
                f.write(json.dumps(log) + "\n")
            o = out_of(j)
            if o.exists():
                n = 1
                while o.with_name(f"{o.stem}.take{n}.mp4").exists():
                    n += 1
                o.rename(o.with_name(f"{o.stem}.take{n}.mp4"))
            log = {}
        for attempt in range(3):
            try:
                if not log.get("request_id"):
                    ep, p = build(j)
                    sub = http(f"https://queue.fal.run/{ep}", key, p)
                    log = {"id": i, "endpoint": ep, "request_id": sub["request_id"], "status_url": sub["status_url"],
                           "response_url": sub["response_url"], "cancel_url": sub.get("cancel_url"),
                           "submitted": time.time(), "payload": clean(p), "billable_s": billable(j),
                           "price": round(billable(j) * price(ep, key), 4)}
                    lp.write_text(json.dumps(log, indent=1, ensure_ascii=False))
                    with LOCK, open(ledger, "a") as f:
                        f.write(json.dumps({k: log[k] for k in ("id", "endpoint", "request_id", "submitted",
                                                                "billable_s", "price")}) + "\n")
                    print(f"sub  {i} {log['request_id']}", flush=True)
                while True:
                    st = http(log["status_url"], key)
                    s = st.get("status")
                    if s == "COMPLETED":
                        out = fetch(log, j)
                        lp.write_text(json.dumps(log, indent=1, ensure_ascii=False))
                        print(f"ok   {i} -> {out.relative_to(root)} ({time.time() - log['submitted']:.0f} s)",
                              flush=True)
                        return True
                    if s not in ("IN_QUEUE", "IN_PROGRESS"):
                        raise RuntimeError(f"status {st}")
                    if time.time() - log["submitted"] > a.timeout:
                        print(f"stuck {i} ({s} after {a.timeout} s); cancelling and resubmitting", flush=True)
                        if log.get("cancel_url"):
                            try:
                                http(log["cancel_url"], key, method="PUT")
                            except Exception:
                                pass
                        with open(logdir / f"{i}.history.jsonl", "a") as f:
                            f.write(json.dumps(dict(log, abandoned=time.time())) + "\n")
                        log = {}
                        break
                    time.sleep(6)
            except Exception as e:  # noqa: BLE001 (a bad input must fail this job, not the batch)
                msg = f"{type(e).__name__}: {e}"
                print(f"err  {i} (attempt {attempt + 1}): {msg[:400]}", flush=True)
                failed_request = log.get("response_url", "\0") in msg and "HTTP 4" in msg
                if log.get("request_id") and not failed_request:
                    # a COMPLETED request whose result we failed to read is retried by fetching, never by POSTing
                    try:
                        if http(log["status_url"], key).get("status") == "COMPLETED":
                            continue
                    except Exception:
                        pass
                # (a request that completed with an error, e.g. 422 on its result, is archived: fal does not bill it)
                    with open(logdir / f"{i}.history.jsonl", "a") as f:
                        f.write(json.dumps(dict(log, error=msg[:1000])) + "\n")
                    log = {}
                    lp.unlink(missing_ok=True)
                if "HTTP 4" in msg and "HTTP 429" not in msg:
                    break  # a validation or safety refusal will not change on retry
        print(f"FAIL {i}", flush=True)
        return False

    done = {j["id"] for j in jobs if out_of(j).exists() and j["id"] not in redo}
    failed = set()
    pending = {}
    with ThreadPoolExecutor(a.jobs) as ex:
        while todo or pending:
            for j in list(todo):
                d = deps_of(j)
                if d & failed:
                    todo.remove(j); failed.add(j["id"]); print(f"skip {j['id']} (dependency failed)", flush=True)
                elif d <= done and len(pending) < a.jobs:
                    todo.remove(j); pending[j["id"]] = ex.submit(run, j)
            if not pending:
                if todo:
                    print(f"STUCK: unresolved deps for {[j['id'] for j in todo]}", flush=True)
                break
            fin = [k for k, f in pending.items() if f.done()]
            if not fin:
                time.sleep(1)
                continue
            for k in fin:
                ok = pending.pop(k).result()
                (done if ok else failed).add(k)
    print(f"done {len(done)}  failed {len(failed)}", flush=True)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
