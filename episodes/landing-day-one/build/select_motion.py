from pathlib import Path
import json
r=Path(__file__).resolve().parents[1];con=json.loads((r/'build/conformed.json').read_text());p=r/'assets/production-assets.json';d=json.loads(p.read_text());m={}
def add(shot,src,img,start,speed):
 z=con[src];m[shot]={'image':img,'prefix':f'/assets/frames/{src}/','fps':z['fps'],'count':z['count'],'source_start':start,'speed':speed}
for shot,src,img,start,speed in [
 ('S05','m_S05','S05',1.15,1.45),('S06','m_S06','S06',.4,2.5),('S07','m_S07','S07',.25,2),('S08','m_S08','S08',.5,2.6),('S09','m_S09r','S09r',.3,2.3),('S17','m_S17','S17',.3,1.1),('S18','m_S18','S18',1.2,2),('S21','m_P21_touch','P21_touch',0,1.6),('S22','m_S22r','S22r',.4,2),('S24','m_S24','S24',.5,1.2),('S26','m_S26r','S26r',.2,3),('S27','m_S27','S27',0,3),('S28','m_S28r','S28r',.4,2),('S29','m_S29r','S29r',.3,2.4),('S43','m_S43','S43',0,3)]:
 add(shot,src,img,start,speed)
add('S14','P2-i2v','P2_toy_start',1.60,.72)
for i,suffix in enumerate('abcdef'):add('S15'+suffix,'P2-i2v','P2_toy_start',.60+i*.16,1.25)
d['motion']=m;p.write_text(json.dumps(d,ensure_ascii=False,indent=2));print(len(m),'motion windows selected')
