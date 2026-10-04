"""Bind current review records to the selected immutable render, preserve older exports."""
from pathlib import Path
import json,csv,hashlib,shutil
R=Path(__file__).resolve().parents[4];E=R/'episodes/first-day-anime-test';S=Path(__file__).parent;W=R/'work/first-day-anime-test';O=R/'renders/first-day-anime-test'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    m=json.loads((W/'faithful/latest-1080.json').read_text());v=json.loads((S/'verification.json').read_text())
    assert m['source_sha256']==v['source_sha256']
    review=json.loads((S/'compliance.json').read_text());review['render_run']=m['run'];review['source_sha256']=m['source_sha256']
    for shot in review['shots']:
        for req in shot['requirements']:
            req['evidence']['render_run']=m['run'];req['evidence']['source_sha256']=m['source_sha256']
    (S/'compliance.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n')
    original=json.loads((E/'build/motion-plan-final.json').read_text())['jobs'];jobs={j['id']:j for j in original}
    for f in (W/'faithful').glob('*/motion.json'):
        for j in json.loads(f.read_text())['jobs']:jobs[j['id']]=j
    chosen={3:'room',4:'tea',5:'reply-performance',15:'mandarin-line',16:'unfurl-clean',17:'breath',18:'burst',19:'burst',20:'ankle',21:'steps-performance',22:'touch',23:'hand-camera-reverse',24:'sprint',25:'leap-camera',29:'flight',30:'flight',34:'helix-camera',35:'paper',36:'flight',37:'xiaoman-joy',40:'helix-camera',42:'hug',44:'outro'}
    fields=['shot','name','start_frame','end_frame','method','tool','seed','source','prompt','retries','implementation','review']
    with (E/'shotlog.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fields,lineterminator='\n');writer.writeheader()
        for i,s in enumerate(review['shots'],1):
            name=chosen.get(i);j=jobs.get(name,{})
            histories=list(W.glob(f'h3_log/{name}.history.jsonl'))+list((W/'faithful').glob(f'*/h3_log/{name}.history.jsonl')) if name else []
            retries=sum(len(p.read_text().splitlines()) for p in histories)
            method='B+A+C' if i in [16,20,23,25,26,27,28,31,32,34,35,38,40,44] else 'C' if i in [2,6,8,9,10,11,12,13,14,39,41,43] else 'A+C'
            writer.writerow(dict(shot=s['id'],name=s['name'],start_frame=s['start_frame'],end_frame=s['end_frame'],method=method,tool='Bun/Canvas/Three.js WebGL + Codex artwork'+(' + MiniMax H3 Max' if name else ''),seed=j.get('seed','not exposed' if name else 'deterministic code; image seed not exposed'),source=j.get('out','Prepared layers and artwork bound by the render manifest'),prompt=j.get('prompt',json.dumps(j.get('params'),ensure_ascii=False) if j.get('params') else 'Director response section5; faithful/film.js, effects.js and rigs.js'),retries=retries,implementation=s['implementation_evidence'],review='Sampled frames reviewed; normal-speed audiovisual acceptance pending'))
    archive=O/'archive';archive.mkdir(exist_ok=True)
    for suffix in ['1080p30','540p30']:
        source=O/f'first-day_opus55_faithful_{suffix}.mp4';target=O/f'first-day_opus55_{suffix}.mp4'
        assert source.exists()
        if target.exists() and sha(target)!=sha(source):
            prior=archive/f'first-day_opus55_{suffix}-{sha(target)[:12]}.mp4'
            if not prior.exists():shutil.copy2(target,prior)
        shutil.copy2(source,target)
    v['preview']={'path':str((O/'first-day_opus55_faithful_540p30.mp4').relative_to(R)),'sha256':sha(O/'first-day_opus55_faithful_540p30.mp4')}
    (S/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
    print('Packaged',m['run'])
if __name__=='__main__':main()
