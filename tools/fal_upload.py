"""Upload a local file to fal's CDN and print its public URL (for endpoints that need a video_url or audio_url).

usage: uv run tools/fal_upload.py <file>
Key from $FAL_KEY only. Files on the fal CDN are publicly readable via their URL; don't upload anything private.
"""
import json
import mimetypes
import os
import sys
import urllib.request
from pathlib import Path


def upload(path):
    key = os.environ["FAL_KEY"]
    path = Path(path)
    ctype = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    req = urllib.request.Request("https://rest.alpha.fal.ai/storage/upload/initiate?storage_type=fal-cdn-v3",
                                 data=json.dumps({"content_type": ctype, "file_name": path.name}).encode(),
                                 headers={"Authorization": f"Key {key}", "Content-Type": "application/json"}, method="POST")
    init = json.loads(urllib.request.urlopen(req, timeout=60).read())
    put = urllib.request.Request(init["upload_url"], data=path.read_bytes(), headers={"Content-Type": ctype}, method="PUT")
    urllib.request.urlopen(put, timeout=600).read()
    return init["file_url"]


if __name__ == "__main__":
    print(upload(sys.argv[1]))
