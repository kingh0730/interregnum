from pathlib import Path
import subprocess,json,concurrent.futures
r=Path(__file__).resolve().parents[1];ids=[p.stem for p in (r/'assets').glob('m_*.mp4')]+['P2-i2v']
def run(i):
 src=r/f'assets/{i}.mp4';out=r/f'assets/frames/{i}';out.mkdir(parents=True,exist_ok=True)
 fps=12 if i in ['m_S17','m_S18'] else 20 if i in ['m_S05','m_S06'] else 60 if i in ['m_S27','m_S28r','m_S29r'] else 24
 vf='scale=1344:756:flags=lanczos,'
 if fps==60:vf+='minterpolate=fps=60:mi_mode=mci:mc_mode=obmc:me_mode=bilat:me=hexbs:search_param=16'
 else:vf+=f'fps={fps}'
 stamp=out/'done.json'
 if not stamp.exists():
  subprocess.run(['ffmpeg','-y','-v','error','-threads','2','-i',str(src),'-an','-vf',vf,'-q:v','3','-start_number','0',str(out/'%04d.jpg')],check=True)
  stamp.write_text(json.dumps({'fps':fps,'count':len(list(out.glob('*.jpg'))),'source':str(src.relative_to(r))}))
 return i,json.loads(stamp.read_text())
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 results=dict(pool.map(run,ids))
(r/'build/conformed.json').write_text(json.dumps(results,indent=2));print('conformed',len(results),'clips')
