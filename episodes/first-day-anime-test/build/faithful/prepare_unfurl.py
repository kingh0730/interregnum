from review_guard import require_reviewed_inputs
require_reviewed_inputs()
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[4];O=R/'work/first-day-anime-test/faithful/unfurl';O.mkdir(exist_ok=True)
def write(n,d):(O/n).write_text(json.dumps(d,ensure_ascii=False,indent=2))
def bind(p):
 p=Path(p);return dict(path=str(p.relative_to(R)),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
a=R/'work/first-day-anime-test/faithful/birth-coiled.png';b=a.with_name('birth-open.png')
write('assets.json',{'coiled':str(a.relative_to(R)),'open':str(b.relative_to(R))})
write('story.json',{'shots':[{'id':'S16','asset':'coiled','start_frame':0,'end_frame':150}]})
write('states.json',{'S16':[{'offset_frame':0,'asset':'coiled'},{'offset_frame':149,'asset':'open'}]})
write('review.json',dict(schema_version=1,status='approved',reviewer='Codex inspected both generated full frames',story=bind(O/'story.json'),assets=bind(O/'assets.json'),states=bind(O/'states.json'),additional_inputs=[],sources=[bind(a),bind(b)],cuts=[],state_changes=[dict(shot_id='S16',offset_frame=149,from_asset='coiled',to_asset='open',relation='continuous',status='approved',issues=[],evidence='Same front-facing barefoot Opus, white piped jacket, charcoal skirt and coral sash; same seated observer at left, desk and rainy room. Coiled hair beside hips/knees becomes extended hair to floor. Both endpoints retain open amber eyes and blank collar/hair pins.')],scope='Conditioning endpoints only; motion output, final composite and playback remain pending.'))
write('motion.json',{'continuity_review':str((O/'review.json').relative_to(R)),'jobs':[dict(id='unfurl',shot_id='S16',image_key='coiled',endpoint='i2v',image=str(a.relative_to(R)),end_image=str(b.relative_to(R)),out=str((O/'unfurl.mp4').relative_to(R)),duration=5,resolution='768P',seed=55016,prompt_expansion_mode='disabled',prompt='Locked camera, one uninterrupted 2D anime actor animation pass. The floating coral-haired woman remains in exactly the same body pose and screen position. Her two very long coiled low twin tails slowly unwind and settle all the way toward the floor, with overlapping strand follow-through. Complete the unfurl by three seconds and gently settle. Keep eyes open amber and mouth closed, not speaking. The seated black-haired woman at the left desk stays in place. Preserve the apartment geometry, illumination, clothes, hands, face and framing. No camera movement, no cuts, no added objects or text.') ]})
