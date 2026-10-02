#!/usr/bin/env python3
"""Bind explicit human/agent visual judgments to stage-specific inputs; no inferred approvals."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('judgments', help='Root-authored JSON; see README.md')
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    jpath = Path(args.judgments).resolve()
    j = json.loads(jpath.read_text())
    assert j.get('stage') and j.get('reviewer'), 'Explicit stage and reviewer required'
    assert j.get('reviewed_visually') is True, 'No visual review attestation'
    assert j.get('status') in ('pending', 'blocked', 'approved')
    def bind(value):
        path = (ROOT / value).resolve()
        assert path.is_file(), f'Missing input: {path}'
        return {'path': str(path), 'sha256': digest(path)}
    story = json.loads((ROOT / j['story']).read_text())
    assets = json.loads((ROOT / j['assets']).read_text())
    assert isinstance(story.get('shots'), list) and story['shots'], 'Nonempty stage story required'
    # Hashes supplied by reviewer ensure an old judgment cannot silently bind newer media.
    observed = j['reviewed_sources']
    needed = {(ROOT / (v['path'] if isinstance(v, dict) else v)).resolve() for v in assets.values()}
    assert len(observed) == len(needed), 'One explicit observation per unique source required'
    seen = set()
    for row in observed:
        p = (ROOT / row['path']).resolve()
        assert p in needed and p not in seen, f'Extra or duplicated source: {p}'
        assert row.get('evidence', '').strip(), f'Specific visual evidence required: {p}'
        assert row.get('sha256') == digest(p), f'Reviewed source changed or hash missing: {p}'
        assert row.get('status') in ('approved', 'pending', 'blocked')
        if j['status'] == 'approved':
            assert row['status'] == 'approved', f'Unapproved source: {p}'
        seen.add(p)
    for key in ('story', 'assets', 'states'):
        if key in j:
            assert j.get('reviewed_input_hashes', {}).get(key) == digest((ROOT / j[key]).resolve()), f'{key} changed since review'
    review = {k: j[k] for k in ('status', 'reviewer', 'stage')}
    review.update(schema_version=1, story=bind(j['story']), assets=bind(j['assets']),
                  sources=[bind(str(p)) for p in sorted(needed)],
                  additional_inputs=[bind(str(jpath))] + [bind(p) for p in j.get('additional_inputs', [])],
                  cuts=j['cuts'], state_changes=j.get('state_changes', []),
                  reviewed_sources=observed, scope_note=j.get('scope_note', 'Stage-specific source review; not approval of unseen motion.'))
    if 'states' in j:
        review['states'] = bind(j['states'])
    # Never synthesize cut/state judgments. Existing gate checks complete coverage and endpoint IDs.
    out = Path(args.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        raise ValueError('Refusing to overwrite review; use a new versioned output path')
    out.write_text(json.dumps(review, ensure_ascii=False, indent=2) + '\n')
    spec = importlib.util.spec_from_file_location('continuity', ROOT / 'tools/continuity.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    result = mod.evaluate_review(out, ROOT)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['approved'] else 2

if __name__ == '__main__':
    raise SystemExit(main())
