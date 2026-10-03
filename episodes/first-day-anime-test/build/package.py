"""Package selected sources, exact submitted motion prompts and technical checks."""
from pathlib import Path
import csv,hashlib,json,subprocess
from graphics import ROOT
from render import TIMELINE,PLATES,MOTION,TAKE_RANGES
EP=ROOT/'episodes/first-day-anime-test';WORK=ROOT/'work/first-day-anime-test';OUT=ROOT/'renders/first-day-anime-test'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    motion=json.loads((WORK/'motion-plan.json').read_text())
    (EP/'build/motion-plan-final.json').write_text(json.dumps(motion,ensure_ascii=False,indent=2)+'\n')
    jobs={j['id']:j for j in motion['jobs']}
    with (EP/'shotlog.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['shot','name','start_frame','end_frame','method','tool','seed','source','take_interval_seconds','prompt','retries','review'])
        w.writeheader()
        for shot in TIMELINE:
            n=int(shot['id'][1:]);name=MOTION.get(n);j=jobs.get(name,{})
            histories=WORK/'h3_log'/f'{name}.history.jsonl'
            retries=len(histories.read_text().splitlines()) if histories.exists() else 0
            method='A+C' if name else 'C'
            if n in [16,20,23,25,34,35,44]:method='A+B+C' if name else 'B+C'
            w.writerow(dict(shot=shot['id'],name=shot['name'],start_frame=shot['start_frame'],end_frame=shot['end_frame'],method=method,tool='Codex image_gen + MiniMax H3 Max + local compositor' if name else 'Codex plates + local compositor',seed=j.get('seed','deterministic'),source=j.get('out',PLATES.get(n,'code')),take_interval_seconds=json.dumps(TAKE_RANGES.get(n)),prompt=j.get('prompt','See build/render.py and build/graphics.py'),retries=retries,review='Sampled frames reviewed; normal-speed audiovisual review pending'))
    sources=[]
    for p in sorted((WORK/'assets').glob('*')):
        if p.is_file() and p.suffix in ['.png','.svg']:
            sources.append(dict(path=str(p.relative_to(ROOT)),sha256=sha(p),bytes=p.stat().st_size))
    ledger=[json.loads(s) for s in (WORK/'h3_log/ledger.jsonl').read_text().splitlines()]
    master=OUT/'first-day_opus55_1080p30.mp4'
    probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','stream=codec_name,width,height,r_frame_rate,nb_frames,duration','-of','json',str(master)]))
    video=next(s for s in probe['streams'] if s['codec_name']=='h264')
    assert (video['width'],video['height'],video['nb_frames'],video['r_frame_rate'])==(1920,1080,'1311','30/1')
    subprocess.run(['ffmpeg','-v','error','-i',str(master),'-f','null','-'],check=True)
    lyrics=json.loads((EP/'timing.json').read_text())['lyrics']
    assert all(l['frame']==round(l['time']*30) for l in lyrics)
    assert all(abs(s['start_frame']-round(s['target_start']*30))<=3 for s in TIMELINE)
    report=dict(master=str(master.relative_to(ROOT)),master_sha256=sha(master),probe=probe,full_decode='passed',frames=1311,fps=30,planned_shots=len(TIMELINE),cut_frame_tolerance='passed, <= 3 frames from rounded target',lyric_anchor_data='passed; visual appearance reviewed separately',audio=dict(source='episodes/first-day-anime-test/first-day.mp3',sha256=sha(EP/'first-day.mp3'),processing='Original MP3 supplied directly to final AAC mux. No gain, SFX, or model audio used.'),requests=len(ledger),billable_seconds=sum(r['billable_s'] for r in ledger),estimated_motion_cost_usd=round(sum(r['price'] for r in ledger),2),image_tool='Codex built-in image_gen',luma_requests=0,playback_review='pending',sources=sources)
    (EP/'build/delivery-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    (EP/'build/take-selection.json').write_text(json.dumps({f'S{n:02}':{'take':MOTION.get(n),'seconds':r} for n,r in TAKE_RANGES.items()},indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['frames','fps','requests','billable_seconds','estimated_motion_cost_usd','full_decode']}))

if __name__=='__main__':main()
