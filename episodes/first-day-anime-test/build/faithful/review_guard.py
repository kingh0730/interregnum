"""Prevent historical source-review recipes from approving changed media."""
from pathlib import Path
import json,hashlib

def require_reviewed_inputs():
    src=Path(__file__).resolve().parent;root=src.parents[3]
    for row in json.loads((src/'reviewed-inputs.json').read_text()):
        p=root/row['path']
        if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=row['sha256']:
            raise RuntimeError('Historical review no longer applies: '+row['path']+'. Inspect new sources and create a new review; do not copy the prior approval.')
