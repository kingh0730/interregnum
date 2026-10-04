from review_guard import require_reviewed_inputs
require_reviewed_inputs()
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[4];P=R/'work/first-day-anime-test/faithful/hand-camera';P.mkdir(exist_ok=True)
def write(n,d):(P/n).write_text(json.dumps(d,ensure_ascii=False,indent=2))
def bind(p):return {'path':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
a=R/'work/first-day-anime-test/faithful/hand-pair-white.png'
write('story.json',{'shots':[{'id':'S23','asset':'pair'}]});write('assets.json',{'pair':str(a.relative_to(R))})
write('review.json',{'schema_version':1,'status':'approved','reviewer':'Codex inspected full isolated pair on white','story':bind(P/'story.json'),'assets':bind(P/'assets.json'),'additional_inputs':[],'sources':[bind(a)],'cuts':[],'state_changes':[],'scope':'Conditioning input only. Full heads, joined hands, complete bodies and feet, floor-length hair retained. Blank pins intentionally reserved for exact vectors in final browser composite. Final camera take and composite require separate review.'})
write('motion.json',{'continuity_review':str((P/'review.json').relative_to(R)),'jobs':[{'id':'hand-camera','shot_id':'S23','image_key':'pair','endpoint':'camera','image':str(a.relative_to(R)),'duration':5,'resolution':'1080P','seed':552323,'prompt_expansion_mode':'disabled','out':str((P/'hand-camera.mp4').relative_to(R)),'prompt':'Frozen character turntable of the two joined-hand anime women on a perfectly featureless WHITE BACKGROUND. Keep every body part, both faces, joined fingers, hair and feet entirely in frame. Exact same paired pose, clothes and faces. The background is flat pure white in EVERY direction, no room, no architecture, no ground texture, no shadows or objects. Only the camera orbits the rigid pair. No speech or mouth movement. Do not add text or symbols. Preserve blank pins. Keep the same framing scale for the entire orbit.','params':{'camera_trajectory':[{'time':i/8,'azimuth':270*i/8,'elevation':0,'distance':1.12} for i in range(9)]}}]})
