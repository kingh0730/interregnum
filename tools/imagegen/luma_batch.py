"""Run a Luma Uni-1 Max image manifest in dependency order (playbook §2b).

usage: uv run tools/imagegen/luma_batch.py <images.json> [--root DIR] [--jobs 6] [--only id1,id2] [--redo id1,id2]

Manifest: a JSON list of {"id", "out", "mode": "t2i"|"edit", "prompt", "base": id|null, "refs": [ids], "deps": [ids]}.
- t2i  -> luma/agent/uni-1/v1/max       {prompt, aspect_ratio: 16:9, reference_image_urls if refs}
- edit -> luma/agent/uni-1/v1/max/edit  {prompt, image_url: <base's fal URL>, reference_image_urls: [<refs' fal URLs>]}
Edits chain to the fal CDN URLs of earlier results, so no local file is ever uploaded.
Paths in "out" are relative to --root (default: the manifest's directory's parent).
Resumable: an image whose out file and fal URL both exist is skipped. URLs are kept in <manifest>.urls.json.
Each request's full log is kept in <manifest dir>/luma_log/<id>.json. Timeouts and download failures resume that
request without another POST. Use distinct manifest directories for batches with overlapping IDs.
Legacy logs missing polling URLs and ambiguous submissions require manual recovery.
Redo intent is journaled before retiring the old request and survives interruption. A normal rerun resumes it;
an old output or URL cannot mark a pending redo complete. Batch and request locks prevent competing writers.
Keep independent batches' output paths distinct. Only use these runners to modify active request state.
"""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import threading
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from request_state import batch_lock, file_lock, read_log, record_once, save_log, sync_dir
TIMEOUT = 420
EP = {"t2i": "luma/agent/uni-1/v1/max", "edit": "luma/agent/uni-1/v1/max/edit"}


def first_image_url(x):
    if isinstance(x, dict):
        for v in x.values():
            u = first_image_url(v)
            if u:
                return u
    elif isinstance(x, list):
        for v in x:
            u = first_image_url(v)
            if u:
                return u
    elif isinstance(x, str) and x.startswith("http") and x.split("?")[0].lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        return x
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest")
    ap.add_argument("--root")
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--only", default="")
    ap.add_argument("--redo", default="")
    a = ap.parse_args()
    man_path = Path(a.manifest).resolve()
    root = Path(a.root).resolve() if a.root else man_path.parent.parent
    items = json.loads(man_path.read_text())
    logdir = man_path.parent / "luma_log"
    logdir.mkdir(parents=True, exist_ok=True)
    try:
        with batch_lock(logdir):
            run_batch(a, man_path, root, items, logdir)
    except (OSError, ValueError, RuntimeError) as e:
        sys.exit(str(e))


def run_batch(a, man_path, root, items, logdir):
    by_id = {it["id"]: it for it in items}
    if a.jobs < 1 or len(by_id) != len(items):
        raise ValueError("--jobs must be positive and manifest IDs must be unique")
    # fal_run uses with_suffix('.json') for its log. Dotted IDs would collide
    # with other request logs or the payload/redo sidecars.
    if any(not isinstance(i, str) or not i or Path(i).name != i or '.' in i for i in by_id):
        raise ValueError("Luma job IDs must be nonempty filenames without dots")
    outputs = [(root / it['out']).resolve() for it in items]
    paths = outputs + [p.with_name(p.name + '.part') for p in outputs]
    if len(paths) != len(set(paths)):
        raise ValueError("manifest output and temporary paths must be distinct")
    urls_path = man_path.with_suffix(".urls.json")
    urls = json.loads(urls_path.read_text()) if urls_path.exists() else {}
    only = set(filter(None, a.only.split(",")))
    redo = set(filter(None, a.redo.split(",")))
    if (only | redo) - by_id.keys() or (only and redo - only):
        raise ValueError("--only/--redo must name existing, selected jobs")
    lock = threading.Lock()
    failed = set()
    recovering = {i for i in by_id if (logdir / f'{i}.redo.json').exists()}

    def needed(it):
        return (not only or it["id"] in only) and (it["id"] in redo | recovering or not (
            it["id"] in urls and (root / it["out"]).exists()))

    def run(it):
        i = it["id"]
        if it["mode"] == "edit":
            payload = {"prompt": it["prompt"], "image_url": urls[it["base"]],
                       "reference_image_urls": [urls[r] for r in it.get("refs", []) if r in urls] or [urls[it["base"]]]}
        else:
            payload = {"prompt": it["prompt"], "aspect_ratio": it.get("aspect", "16:9")}
            if it.get("refs"):  # t2i with references: identity without edit mode's re-sharpening
                payload["reference_image_urls"] = [urls[r] for r in it["refs"] if r in urls]
        # A surviving fal child owns this lock until it has finished using both
        # its payload and request log. Never retire or rewrite files under it.
        with file_lock((logdir / i).with_suffix('.request.lock')):
            pfile = logdir / f"{i}.payload.json"
            prefix = logdir / i
            lp = prefix.with_suffix('.json')
            journal_path = logdir / f'{i}.redo.json'
            journal = read_log(journal_path)
            identity = hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(',', ':'),
                                                 ensure_ascii=False).encode()).hexdigest()
            if i in redo and not journal:
                old = read_log(lp)
                if old and not old.get("response"):
                    print(f"FAIL {i}: unresolved request; recover it before requesting a redo", flush=True)
                    return False
                journal = {'previous': old, 'endpoint': EP[it['mode']], 'payload_sha256': identity,
                           'out': str((root / it['out']).resolve())}
                # Commit redo intent before touching the URL cache or old request.
                save_log(journal_path, journal)
            if journal:
                if (journal['endpoint'] != EP[it['mode']] or journal['payload_sha256'] != identity
                        or journal['out'] != str((root / it['out']).resolve())):
                    raise ValueError(f'{i}: interrupted redo inputs changed; restore the original manifest')
            # Publish only validated inputs. A rejected recovery must not change
            # the payload a surviving child will read after acquiring this lock.
            # Publish before retiring the old log, so a child cannot pair the old
            # payload with a freshly cleared request slot.
            save_log(pfile, {'endpoint': EP[it['mode']], 'payload': payload})
            if journal:
                with lock:
                    urls.pop(i, None)
                    save_log(urls_path, urls)
                old = journal['previous']
                if old:
                    record_once(logdir / f'{i}.history.jsonl', old)
                    # Replay retirement only while the active log is still the OLD
                    # request. A newly accepted request is always resumed, never removed.
                    active = read_log(lp)
                    same_request = (active.get('request_id') == old['request_id']) if old.get('request_id') else active == old
                    if active and same_request:
                        lp.unlink()
                        sync_dir(logdir)
        for attempt in range(3):
            # --resume reuses the accepted request even after timeout or download failure.
            try:
                r = subprocess.run(["uv", "run", str(TOOLS / "fal_run.py"), EP[it["mode"]], str(pfile), str(prefix),
                                    "--resume", "--request-envelope"], capture_output=True, text=True, timeout=TIMEOUT)
            except subprocess.TimeoutExpired:
                print(f"timeout {i} (attempt {attempt + 1}); retaining request for resume", flush=True)
                continue
            res = logdir / f"{i}.json"
            url = first_image_url(json.loads(res.read_text()).get("response")) if res.exists() else None
            got = prefix.parent / (prefix.name + Path(url.split("?")[0]).suffix) if url else None
            if r.returncode == 0 and url and got and got.exists():
                out = root / it["out"]
                out.parent.mkdir(parents=True, exist_ok=True)
                tmp = out.with_name(out.name + '.part')
                shutil.copyfile(got, tmp)
                with open(tmp, 'rb') as f:
                    os.fsync(f.fileno())
                tmp.replace(out)
                sync_dir(out.parent)
                with lock:
                    urls[i] = url
                    save_log(urls_path, urls)
                if journal:
                    journal_path.unlink()
                    sync_dir(logdir)
                print(f"ok   {i}", flush=True)
                return True
            print(f"resume {i} (attempt {attempt + 1}): {(r.stderr or r.stdout)[-300:]}", flush=True)
        print(f"FAIL {i}", flush=True)
        return False

    todo = [it for it in items if needed(it)]
    done = {i for i in by_id if i in urls and (root / by_id[i]["out"]).exists() and i not in redo | recovering}
    with ThreadPoolExecutor(a.jobs) as ex:
        pending = {}
        while todo or pending:
            for it in list(todo):
                deps = set(it.get("deps", [])) | ({it["base"]} if it.get("base") else set()) | set(it.get("refs", []))
                if deps & failed:
                    todo.remove(it); failed.add(it["id"]); print(f"skip {it['id']} (dependency failed)", flush=True)
                elif deps <= done and len(pending) < a.jobs:
                    todo.remove(it); pending[it["id"]] = ex.submit(run, it)
            if not pending:
                if todo:
                    missing = {d for it in todo for d in it.get("deps", []) if d not in by_id}
                    print(f"STUCK: unresolved deps {missing or '(dependency not yet generated)'}", flush=True)
                    failed.update(it['id'] for it in todo)
                break
            fin = next(iter(f for f in pending.values() if f.done()), None)
            if fin is None:
                wait(pending.values(), return_when=FIRST_COMPLETED)
                continue
            k = next(k for k, f in pending.items() if f is fin)
            pending.pop(k)
            try:
                ok = fin.result()
            except Exception as e:
                print(f'FAIL {k}: {e}', flush=True)
                ok = False
            (done if ok else failed).add(k)
    print(f"done {len(done)}  failed {len(failed)}", flush=True)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
