"""Import verified external reference URLs into an idle episode Luma catalog.

Only new external IDs are added. Existing request logs and original ref IDs
remain untouched. Run after register_refs.py; do not run during a Luma batch.
"""
import json,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; b=ROOT/'episodes/ep01/build'
a=json.loads((b/'images.json').read_text()); urls=json.loads((b/'images.urls.json').read_text())
t=json.loads((ROOT/'work/ep01/ref_transport_urls.json').read_text()); assert t['complete']
byid={x['id']:x for x in a}
for id,r in t['references'].items():
 assert r['remote_sha256_verified'] and (ROOT/r['out']).is_file()
 if id not in byid:a.append({'id':id,'out':r['out'],'mode':'external_reference','prompt':'Deterministic same-resolution Q90 transport of '+r['source']+'; never generate this entry. Run register_refs.py to restore.','refs':[],'deps':[],'aspect':'16:9','source':r['source']})
 urls[id]=t['urls'][id]
# The terminal k01 input failure keeps its complete request journal. Replacement
# receives a distinct ID and path; only transport URLs differ.
if 'k01_v2' not in byid:
 x=copy.deepcopy(byid['k01']);x['id']='k01_v2';x['out']='work/ep01/keys/k01_v2.png';a.append(x)
for x in a:
 if x['id'].startswith('k') and x['id'] not in ('k01','k05'):
  x['refs']=[r+'_q90' if r+'_q90' in t['references'] else r for r in x.get('refs',[])]
  x['deps']=[r+'_q90' if r+'_q90' in t['references'] else r for r in x.get('deps',[])]
(b/'images.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
(b/'images.urls.json').write_text(json.dumps(urls,indent=2)+'\n')
