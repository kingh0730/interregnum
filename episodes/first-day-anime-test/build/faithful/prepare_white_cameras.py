from review_guard import require_reviewed_inputs
require_reviewed_inputs()
from pathlib import Path
from PIL import Image
import json,hashlib
R=Path(__file__).resolve().parents[4];W=R/'work/first-day-anime-test/faithful'
def bind(p):return dict(path=str(p.relative_to(R)),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
for name,shot,angle in [('leap-camera','S25',360),('helix-camera','S34',450)]:
 p=W/name;p.mkdir(exist_ok=True);kind=name.split('-')[0];im=Image.open(W/(kind+'-pair-cutout.png')).convert('RGBA');out=Image.new('RGB',(round(im.width*1.15),round(im.height*1.15)),'white');out.paste(im,((out.width-im.width)//2,(out.height-im.height)//2),im);a=p/'white.png';out.save(a)
 def write(n,d):(p/n).write_text(json.dumps(d,ensure_ascii=False,indent=2))
 write('story.json',{'shots':[{'id':shot,'asset':'pair'}]});write('assets.json',{'pair':str(a.relative_to(R))})
 write('review.json',dict(schema_version=1,status='approved',reviewer='Codex inspected full paired cutout and its source',story=bind(p/'story.json'),assets=bind(p/'assets.json'),additional_inputs=[],sources=[bind(a)],cuts=[],state_changes=[],scope='Conditioning input only: original paired action and costumes retained; full figures and source hair silhouette, blank pins. White compositing background and margin are for extraction. No motion or final-film approval implied.'))
 write('motion.json',{'continuity_review':str((p/'review.json').relative_to(R)),'jobs':[dict(id=name,shot_id=shot,image_key='pair',endpoint='camera',image=str(a.relative_to(R)),duration=5,resolution='1080P',seed=557000+angle,prompt_expansion_mode='disabled',out=str((p/(name+'.mp4')).relative_to(R)),prompt='Exact frozen anime paired figure turntable on completely WHITE seamless background. Preserve both bodies, full heads, hands, footwear, clothes, long hair and the rigid pose of the input. Camera makes the specified orbit while the figures remain frozen. White everywhere in every direction: absolutely no room, sky, floor, fixtures or additional objects. No mouth animation, no speech. Keep complete people and hair in the frame. Do not invent symbols on the blank pins. Maintain the same image scale.',params={'camera_trajectory':[dict(time=i/10,azimuth=angle*i/10,elevation=0,distance=1) for i in range(11)]})]})
 print(p/'motion.json')
