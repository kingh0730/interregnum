"""Run a MiniMax H3 Max (or any fal video endpoint) motion manifest: parallel and resumable without automatic paid resubmission.

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
- Requests exceeding --timeout are retained for a later run; polling/download failures never trigger replacement.
- An ambiguous submission is retained for manual recovery rather than automatically POSTed again.
- Resuming verifies the endpoint and full payload, including inline media. Legacy logs with redacted media
  cannot establish identity and require manual recovery.
- Confirmed generation failures are recorded and can be replaced with an explicit --redo; never automatically.
- --redo moves the old output to <out>.takeN.mp4 (so earlier takes stay comparable) and starts a new request.
- Redo intent is committed before archiving. Interrupted preparation resumes from that saved plan on a normal
  rerun; an old output file cannot override a pending request. Logged completed outputs also verify input identity.
- Logs/history/ledger use atomic, fsynced writes. One process at a time may use a batch's h3_log directory.
  Use distinct output paths for independent batches; other tools must not write these files during a run.
- A crash at the POST boundary is inherently ambiguous without service-side idempotency. The saved submitting
  state blocks further POSTs until its request is manually recovered; --redo does not override that protection.
Every submitted request is appended to <manifest dir>/h3_log/ledger.jsonl with its billable seconds and price.
"""
import argparse
import base64
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from request_state import batch_lock, read_log, record_once, save_log, sync_dir

ALIAS = {"i2v": "minimax/h3-max/image-to-video", "lipsync": "minimax/h3-max/lip-sync/image-to-video",
         "ray": "luma/agent/ray/v3.2/image-to-video", "camera": "minimax/h3-max/camera-controls"}
PRICE_FALLBACK = {"minimax/h3-max/image-to-video": 0.025, "minimax/h3-max/lip-sync/image-to-video": 0.05,
                  "luma/agent/ray/v3.2/image-to-video": 0.03}


class HTTPFailure(RuntimeError):
    def __init__(self, code, url, body):
        super().__init__(f"HTTP {code} {url}: {body}")
        self.code = code


class GenerationFailure(RuntimeError):
    pass


def archive_previous(log, logdir):
    """Replay a persisted replacement plan before crossing the POST boundary."""
    replacement = log.get('replacement')
    if not replacement:
        return
    if replacement.get('previous'):
        record_once(logdir / f"{log['id']}.history.jsonl", replacement['previous'])
    if replacement.get('target'):
        source, target = Path(replacement['source']), Path(replacement['target'])
        if target.exists():
            if source.exists():
                raise RuntimeError(f"both archive and original exist: {target}; recover manually")
        elif source.exists():
            source.rename(target)
            sync_dir(source.parent)
        else:
            raise RuntimeError(f"missing original and archive: {source}; recover manually")


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
                raise HTTPFailure(e.code, url, body) from e
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
    logdir = man_path.parent / "h3_log"
    logdir.mkdir(parents=True, exist_ok=True)
    try:
        with batch_lock(logdir):
            run_batch(a, root, jobs, logdir)
    except (OSError, ValueError, RuntimeError) as e:
        sys.exit(str(e))


def run_batch(a, root, jobs, logdir):
    by_id = {j["id"]: j for j in jobs}
    if a.jobs < 1 or len(by_id) != len(jobs):
        raise ValueError("--jobs must be positive and manifest job IDs must be unique")
    if any(not isinstance(i, str) or not i or Path(i).name != i or i in ('.', '..') for i in by_id):
        raise ValueError("job IDs must be nonempty filenames")
    outputs = [(root / j['out']).resolve() for j in jobs]
    working_paths = outputs + [p.with_suffix('.part.mp4') for p in outputs]
    if len(set(working_paths)) != len(working_paths):
        raise ValueError("manifest output and temporary download paths must be distinct")
    reserved_paths = set(working_paths)
    ledger = logdir / "ledger.jsonl"
    only = set(filter(None, a.only.split(",")))
    redo = set(filter(None, a.redo.split(",")))
    if (only | redo) - by_id.keys():
        raise ValueError("--only/--redo contains unknown job IDs")
    if only and redo - only:
        raise ValueError("--redo jobs must also be selected by --only")
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
    selected_ids = {j['id'] for j in sel}
    dependency_ids = set().union(*(deps_of(j) for j in sel)) & by_id.keys()
    relevant_ids = selected_ids | dependency_ids
    # A bad log outside the selected jobs and their required inputs must not
    # prevent an independent --only recovery. Required logs still fail closed.
    logs = {i: read_log(logdir / f"{i}.json") for i in relevant_ids}
    planned = [j for j in sel if j['id'] in redo or logs[j['id']].get('phase') == 'prepared'
               or not logs[j['id']] and not out_of(j).exists()]
    todo = list(sel)
    est = sum(billable(j) * price(ep_of(j), key) for j in planned)
    for j in planned:
        print(f"plan {j['id']:<14} {ep_of(j):<42} {billable(j):5.1f} s  ${billable(j) * price(ep_of(j), key):.3f}")
    print(f"{len(sel)} selected jobs, estimated new spend ${est:.2f}", flush=True)
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

    def read_result(log):
        try:
            res = http(log["response_url"], key)
        except HTTPFailure as e:
            # Only called after COMPLETED. Authentication, missing results and service
            # outages are retrieval failures, not evidence of a failed generation.
            if e.code == 422:
                raise GenerationFailure(str(e)) from e
            raise
        if res.get("error") or res.get("error_type"):
            raise GenerationFailure(json.dumps(res))
        return res

    def fetch(log, j, lp):
        res = read_result(log)
        log["response"] = res
        url = (res.get("video") or {}).get("url")
        if not url:
            raise RuntimeError(f"no video in response: {json.dumps(res)[:300]}")
        save_log(lp, log)
        out = out_of(j)
        out.parent.mkdir(parents=True, exist_ok=True)
        tmp = out.with_suffix(".part.mp4")
        urllib.request.urlretrieve(url, tmp)
        with open(tmp, 'rb') as f:
            os.fsync(f.fileno())
        tmp.replace(out)
        sync_dir(out.parent)
        log["done"] = time.time()
        log['phase'] = 'done'
        return out

    def run(j):
        i = j["id"]
        lp = logdir / f"{i}.json"
        log = read_log(lp)

        def record_failure(detail):
            log["terminal_failure"] = {"time": time.time(), "detail": detail}
            log['phase'] = 'failed'
            save_log(lp, log)

        prepared = log.get('phase') == 'prepared'
        if i in redo and log and not prepared and not (log.get("done") or log.get("terminal_failure")):
            # Older runs did not record terminal failures. Inspect completed results
            # too, without downloading or rebuilding the original (possibly redacted) inputs.
            if log.get("request_id") and log.get("status_url") and not log.get("submission_pending"):
                try:
                    st = http(log["status_url"], key)
                    if st.get("status") == "COMPLETED":
                        if st.get("error") or st.get("error_type"):
                            record_failure(st)
                        elif log.get("response_url"):
                            read_result(log)
                except GenerationFailure as e:
                    record_failure(str(e))
                except Exception as e:
                    print(f"unable to verify {i}: {e}", flush=True)
            if not log.get("terminal_failure"):
                print(f"FAIL {i}: unresolved request; resume/recover it before requesting a redo", flush=True)
                return False
        replacing = i in redo and not prepared
        if log.get("submission_pending"):
            print(f"FAIL {i}: previous submission unresolved; recover manually before another POST", flush=True)
            return False
        if log.get("terminal_failure") and not replacing:
            print(f"FAIL {i}: generation failed; use --redo {i} to request a replacement", flush=True)
            return False
        if not log and out_of(j).exists() and not replacing:
            print(f"skip {i}: existing unlogged output (use --redo to replace)", flush=True)
            return True
        try:
            ep, p = build(j)
            fingerprint = hashlib.sha256(json.dumps(p, sort_keys=True, separators=(",", ":"),
                                                   ensure_ascii=False).encode()).hexdigest()
            if log and not replacing:
                if log.get('out') and log['out'] != str(out_of(j).resolve()):
                    raise ValueError("existing request has a different output path; restore the original path")
                if log.get("endpoint") != ep or log.get("payload") != clean(p):
                    raise ValueError("existing request differs from payload; restore original inputs or use a new job ID")
                if log.get("payload_sha256"):
                    if log["payload_sha256"] != fingerprint:
                        raise ValueError("existing request differs from full payload; restore original inputs or use a new job ID")
                elif any(v == "<data uri>" for v in log["payload"].values()):
                    raise ValueError("legacy media payload has no identity hash; recover manually")
                if not prepared and not all(log.get(k) for k in ("request_id", "status_url", "response_url")):
                    raise ValueError("incomplete request log; recover manually before another POST")
            if not replacing and log.get('done') and out_of(j).exists():
                print(f"skip {i}: completed request", flush=True)
                return True
            # Finish all potentially failing local preparation before changing state.
            seconds = billable(j) if replacing or not log or prepared else log.get('billable_s')
            cost = round(seconds * price(ep, key), 4) if replacing or not log or prepared else log.get('price')
        except Exception as e:
            print(f"FAIL {i}: {e}", flush=True)
            return False
        poll_start = time.time()
        for attempt in range(3):
            try:
                if replacing or not log:
                    old = log
                    log = {'id': i, 'endpoint': ep, 'payload': clean(p), 'payload_sha256': fingerprint,
                           'out': str(out_of(j).resolve()), 'phase': 'prepared', 'billable_s': seconds, 'price': cost}
                    if replacing:
                        o = out_of(j).resolve()
                        target = None
                        if o.exists():
                            n = 1
                            while (o.with_name(f"{o.stem}.take{n}.mp4").exists()
                                   or o.with_name(f"{o.stem}.take{n}.mp4") in reserved_paths):
                                n += 1
                            target = str(o.with_name(f"{o.stem}.take{n}.mp4"))
                        log['replacement'] = {'previous': old, 'source': str(o), 'target': target}
                    # Commit redo intent BEFORE moving the old take. A restart replays
                    # this plan even when the old output still occupies the final path.
                    save_log(lp, log)
                    replacing = False
                if not log.get("request_id"):
                    archive_previous(log, logdir)
                    log.pop('replacement', None)
                    log['phase'] = 'submitting'
                    log['submission_pending'] = True
                    save_log(lp, log)
                    sub = http(f"https://queue.fal.run/{ep}", key, p)
                    log.update({k: sub.get(k) for k in ('request_id', 'status_url', 'response_url', 'cancel_url')})
                    if not all(log.get(k) for k in ('request_id', 'status_url', 'response_url')):
                        save_log(lp, log)
                        raise RuntimeError('incomplete submission response; recover manually')
                    log.update(phase='accepted', submitted=time.time())
                    log.pop('submission_pending', None)
                    save_log(lp, log)
                    print(f"sub  {i} {log['request_id']}", flush=True)
                if log.get('submission_pending'):
                    break
                if all(k in log for k in ('submitted', 'billable_s', 'price')):
                    record_once(ledger, {k: log[k] for k in ('id', 'endpoint', 'request_id', 'submitted',
                                                           'billable_s', 'price')}, key='request_id')
                while True:
                    st = http(log["status_url"], key)
                    s = st.get("status")
                    if s == "COMPLETED":
                        if st.get("error") or st.get("error_type"):
                            record_failure(st)
                            print(f"FAIL {i}: generation failed; use --redo {i} to request a replacement", flush=True)
                            return False
                        out = fetch(log, j, lp)
                        save_log(lp, log)
                        print(f"ok   {i} -> {out} ({time.time() - log['submitted']:.0f} s)",
                              flush=True)
                        return True
                    if s not in ("IN_QUEUE", "IN_PROGRESS"):
                        raise RuntimeError(f"status {st}")
                    if time.time() - poll_start > a.timeout:
                        print(f"pending {i} ({s} after {a.timeout} s); retained for next run", flush=True)
                        return False
                    time.sleep(6)
            except Exception as e:  # noqa: BLE001 (a bad input must fail this job, not the batch)
                msg = f"{type(e).__name__}: {e}"
                print(f"err  {i} (attempt {attempt + 1}): {msg[:400]}", flush=True)
                if isinstance(e, GenerationFailure):
                    record_failure(msg)
                    break
                if not log.get("request_id") or log.get('submission_pending'):
                    # The POST may have reached the service even though its response was lost.
                    break
                if "HTTP 4" in msg and "HTTP 429" not in msg:
                    break
                # Retry only polling/fetching this same request. Keep its log even on failure.
        print(f"FAIL {i}", flush=True)
        return False

    # Selected jobs must validate their request identity before becoming dependencies.
    # Unselected jobs may supply already completed takes, never pending replacements.
    done = {j['id'] for j in jobs if j['id'] in dependency_ids - selected_ids and out_of(j).exists()
            and (not logs[j['id']] or logs[j['id']].get('done'))}
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
                    failed.update(j["id"] for j in todo)
                break
            fin = [k for k, f in pending.items() if f.done()]
            if not fin:
                wait(pending.values(), return_when=FIRST_COMPLETED)
                continue
            for k in fin:
                try:
                    ok = pending.pop(k).result()
                except Exception as e:
                    print(f"FAIL {k}: {e}", flush=True)
                    ok = False
                (done if ok else failed).add(k)
    print(f"done {len(done)}  failed {len(failed)}", flush=True)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
