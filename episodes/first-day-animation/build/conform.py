from pathlib import Path
import json,subprocess
r=Path(__file__).resolve().parents[1];shots=json.load(open(r/'compositor/timeline.json'))['shots']
# Reviewed source windows in seconds. Two initial takes retained; targeted take3 repairs kept separately.
picks={'S01b':(1,0,4.6),'S02a':(1,1,3.3),'S02b':(1,0,4.8),'S03a':(1,.3,.28),'S04a':(2,0,4.8),'S06a':(1,0,3.2),'S06b':(2,0,2.7),'S07a':(3,0,5.0),'S07c':(2,1.5,3.3),'S08':(3,0,4.8),'S09a':(3,0,5.0),'S10a':(1,0,3.4),'S10b':(2,.1,3.7),'S11a':(2,0,4.8),'S11b':(1,0,4.8),'S12a':(2,0,4.7),'S12b':(2,0,4.8),'S14':(3,0,5.1),'S16a':(2,0,2.5),'S16b':(1,0,4.8)}
notes={'S08':'Takes1/2 rejected: white dress invented during upward tilt. Take3 constrained with reviewed wardrobe end frame.','S09a':'Takes1/2 replaced monitor spark with text. Take3 retains spark for match cut.','S07a':'Take3 shows upright-side-inverted-side-upright roll; preserve whole roll, prioritize compound camera over literal 50% retime.','S14':'Take3 shows front-side-back-front orbit followed by pupil approach.','S10b':'Take1 moves Clawd off head. Take2 retains correct head placement.','S06b':'Take1 introduces duplicate heroine late; choose take2 front-to-back interval.'}
records=[]
for s in shots:
 if s['source']!='V':continue
 sid=s['id'];take,ss,span=picks[sid];frames=s['frames'];D=frames/30;d=r/'plates'/sid;d.mkdir(parents=True,exist_ok=True);src=r/f'assets/clips/{sid}_take{take}.mp4'
 for p in d.glob('*.jpg'):p.unlink()
 vf=('minterpolate=fps=60:mi_mode=mci,' if sid=='S03a' else '')+f'setpts=(PTS-STARTPTS)*{D/span},fps=30,scale=1920:1080:flags=lanczos,tpad=stop_mode=clone:stop_duration=1'
 subprocess.run(['ffmpeg','-v','error','-y','-ss',str(ss),'-t',str(span),'-i',str(src),'-an','-vf',vf,'-frames:v',str(frames),'-q:v','2','-start_number','0',str(d/'%05d.jpg')],check=True)
 records.append({'id':sid,'take':take,'source':str(src.relative_to(r)),'source_start':ss,'source_duration':span,'target_duration':D,'frames':frames,'review':notes.get(sid,'Selected from five sampled timestamps per take for visible action, framing, identity and source continuity; final temporal quality requires playback.')});print(sid,frames,flush=True)
(r/'build/selected-takes.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
