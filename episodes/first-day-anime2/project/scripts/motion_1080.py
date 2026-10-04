"""Episode-scoped H3 runner with a verified, resolution-specific price estimate.

Uses the shared durable request/recovery implementation unchanged. Its historical
endpoint-only fallback is too low for this episode's 1080P requests. This snapshot
is scoped to 2026-10-04 and the promotion ending 2026-10-15, not a general price.
Source: https://fal.ai/models/minimax/h3-max/image-to-video
"""
from pathlib import Path
import datetime
import json
import sys

REPO=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(REPO/'tools/video'))
import h3_batch

if not datetime.date(2026,10,4)<=datetime.date.today()<datetime.date(2026,10,15):
    raise SystemExit('Refresh 1080P rate snapshot before new production requests.')
manifest=json.loads(Path(sys.argv[1]).read_text())
for job in manifest['jobs']:
    settings={**manifest.get('defaults',{}),**job}
    if settings.get('resolution')!='1080P' or settings.get('endpoint','i2v') not in ('i2v','minimax/h3-max/image-to-video'):
        raise SystemExit('This episode runner only quotes H3 Max 1080P i2v jobs.')
h3_batch.price=lambda ep,key: .096
h3_batch.main()
