"""Run a Luma Uni-1 Max image manifest in dependency order (playbook §2b).

usage: uv run tools/imagegen/luma_batch.py <images.json> [--root DIR] [--jobs 6] [--only id1,id2] [--redo id1,id2]

Manifest: a JSON list of {"id", "out", "mode": "t2i"|"edit", "prompt", "base": id|null, "refs": [ids], "deps": [ids]}.
- t2i  -> luma/agent/uni-1/v1/max       {prompt, aspect_ratio: 16:9, reference_image_urls if refs}
- edit -> luma/agent/uni-1/v1/max/edit  {prompt, image_url: <base's fal URL>, reference_image_urls: [<refs' fal URLs>]}
Edits chain to the fal CDN URLs of earlier results, so no local file is ever uploaded.
Paths in "out" are relative to --root (default: the manifest's directory's parent).
Resumable: an image whose out file and fal URL both exist is skipped. URLs are kept in <manifest>.urls.json.
Each request's full log is kept in <manifest dir>/luma_log/<id>.json (per manifest, so parallel episodes never collide; (fal_run never re-POSTs, so a lost poll can be
recovered from the request id there).
"""
import argparse
import json
import shutil
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
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
    by_id = {it["id"]: it for it in items}
    urls_path = man_path.with_suffix(".urls.json")
    urls = json.loads(urls_path.read_text()) if urls_path.exists() else {}
    only = set(filter(None, a.only.split(",")))
    redo = set(filter(None, a.redo.split(",")))
    for r in redo:
        urls.pop(r, None)
    logdir = man_path.parent / "luma_log"
    logdir.mkdir(parents=True, exist_ok=True)
    lock = threading.Lock()
    failed = set()

    def needed(it):
        return (not only or it["id"] in only) and not (it["id"] in urls and (root / it["out"]).exists())

    def run(it):
        i = it["id"]
        if it["mode"] == "edit":
            payload = {"prompt": it["prompt"], "image_url": urls[it["base"]],
                       "reference_image_urls": [urls[r] for r in it.get("refs", []) if r in urls] or [urls[it["base"]]]}
        else:
            payload = {"prompt": it["prompt"], "aspect_ratio": it.get("aspect", "16:9")}
            if it.get("refs"):  # t2i with references: identity without edit mode's re-sharpening
                payload["reference_image_urls"] = [urls[r] for r in it["refs"] if r in urls]
        pfile = logdir / f"{i}.payload.json"
        pfile.write_text(json.dumps(payload, ensure_ascii=False))
        prefix = logdir / i
        for attempt in range(3):
            # Luma's queue sometimes leaves a request IN_PROGRESS for 20+ minutes while fresh ones finish in about 2,
            # so a request that takes longer than TIMEOUT is abandoned and resubmitted (costs about 0.3 cents).
            try:
                r = subprocess.run(["uv", "run", str(TOOLS / "fal_run.py"), EP[it["mode"]], str(pfile), str(prefix)],
                                   capture_output=True, text=True, timeout=TIMEOUT)
            except subprocess.TimeoutExpired:
                print(f"timeout {i} (attempt {attempt + 1}); resubmitting", flush=True)
                continue
            res = logdir / f"{i}.json"
            url = first_image_url(json.loads(res.read_text()).get("response")) if res.exists() else None
            got = [p for p in logdir.glob(f"{i}.*") if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")] + \
                  [p for p in logdir.glob(f"{i}_*") if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")]
            if r.returncode == 0 and url and got:
                out = root / it["out"]
                out.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(got[0], out)
                with lock:
                    urls[i] = url
                    urls_path.write_text(json.dumps(urls, indent=1))
                print(f"ok   {i}", flush=True)
                return True
            print(f"retry {i} (attempt {attempt + 1}): {(r.stderr or r.stdout)[-300:]}", flush=True)
        print(f"FAIL {i}", flush=True)
        return False

    todo = [it for it in items if needed(it)]
    done = {i for i in by_id if i in urls and (root / by_id[i]["out"]).exists() and i not in redo}
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
                break
            fin = next(iter(f for f in pending.values() if f.done()), None)
            if fin is None:
                import time; time.sleep(1); continue
            k = next(k for k, f in pending.items() if f is fin)
            pending.pop(k)
            (done if fin.result() else failed).add(k)
    print(f"done {len(done)}  failed {len(failed)}", flush=True)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
