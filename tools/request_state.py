"""Durable local state helpers for paid request runners (POSIX filesystems)."""
import fcntl
import json
import os
from pathlib import Path
import tempfile
import threading
from contextlib import contextmanager

LOCK = threading.Lock()


def atomic_text(path, text):
    """Publish a complete, durable file; a killed writer cannot truncate the ledger."""
    path = Path(path)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=f'.{path.name}.')
    try:
        with os.fdopen(fd, 'w') as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
        sync_dir(path.parent)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def sync_dir(path):
    fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def save_log(path, log):
    atomic_text(path, json.dumps(log, indent=1, ensure_ascii=False))


def read_log(path):
    if not path.exists():
        return {}
    log = json.loads(path.read_text())
    if not isinstance(log, dict) or not log:
        raise ValueError(f"invalid request log: {path}; recover manually")
    return log


def record_once(path, record, key=None):
    """Idempotent history/ledger update, including recovery after interrupted writes."""
    with LOCK:
        entries = [json.loads(line) for line in path.read_text().splitlines() if line.strip()] if path.exists() else []
        if any((old.get(key) == record.get(key)) if key else old == record for old in entries):
            return
        entries.append(record)
        atomic_text(path, ''.join(json.dumps(entry, ensure_ascii=False) + '\n' for entry in entries))


@contextmanager
def file_lock(path):
    with open(path, 'a') as f:
        try:
            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError(f"another process is using {path}") from None
        try:
            yield
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)


@contextmanager
def batch_lock(logdir):
    # Hold through planning as well as execution: another invocation must not skip
    # an old output while this invocation is replacing it.
    with file_lock(logdir / '.lock'):
        yield
