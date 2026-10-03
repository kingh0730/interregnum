from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parents[1];root=r.parents[1]
# Stills reviewed from scene-art-review and individual integrated frames. Generation is action-specific.
spec={
'S05':'Locked medium close-up. The sitting girl softly exhales, her shoulders lower and long sleeves settle against her crossed knees. Understated small smile, only a gentle blink. Preserve cel animation artwork, costume and scene. No camera move, no new objects.',
'S06':'Locked eye-level wide view. The peach-puffer girl passes the ONE steaming bun to the indigo-peach girl; their hands release and receive it cleanly. The cream-haired terracotta-cardigan boy gives one small nod. Other friends watch naturally with small head movements. Keep six characters, no extras. Preserve cel style.',
'S07':'Locked low-angle live-action medium shot. The man raises one eyebrow and gives a single small deadpan shrug, shoulders up then down. One unseen friend hand briefly points toward him from camera edge. Wet neon bokeh and vending-machine practical light. Real natural motion, no exaggerated face, no camera pan.',
'S08':'Side-on camera tracks a short fast lateral skid. The whale-hood young man brakes from his running pose, sneaker slides then PLANTS firmly in one shallow puddle with one small splash. Hood and headlamp bounce then settle. Finish with both feet grounded. All feet remain in frame. No forward walk, no jump.',
'S17':'Locked macro camera on the felt boy. Handmade stop-motion performance: one slow inhale, chest rises, shoulders rise slightly, then a held breath. Individual wool fibers drift subtly. Gentle tiny face, no lip speech, no camera movement, keep handmade needle-felt material.',
'S18':'Locked wide miniature view. All six wool puppets take a slow synchronized breath, chests and shoulders expand, then exhale together and a modest cloud of cotton dandelion seeds rises. Keep six distinct puppets exactly, all feet planted and visible, handmade stop motion not liquid deformation.',
'S24':'Locked floor-level wide camera. All six friends perform one forceful synchronized heel plant from crouch, then knees compress and settle. Their soles visibly contact the wet crossing, making small puddle splashes. Keep all feet and heads framed. No camera push or cut, preserve the night street and neon reflections.',
'S27':'Locked wide full-body framing, anime action. The girl bends knees slightly deeper, stamps her raised heel on the white stripe once, then springs into a strong vertical jump with arms reaching upward. Start anticipation, visible foot contact, then launch. Keep full body feet visible throughout, camera may tilt up only to follow the ascent, no walking or extra flips. Clean drawing and squash-and-stretch.',
'S29':'The two linked friends complete a slow graceful quarter-turn in zero gravity without releasing their joined hands. Hair, braid and cardigan hems float. The other four tiny friends drift around them; black-white jacket man stays deadpan. Camera gently rolls with them, preserve clear silhouettes and all fingers. No extra bodies.',
'P21_touch':'Locked 100mm macro camera. The TWO index fingertips approach horizontally, pause just before touching, then touch softly once and stay touching. Grey cuff hand left, terracotta cuff hand right. Real anatomically natural hands, no extra fingers or hands. Warm golden backlight, no camera movement.',
'S43':'Locked top-down macro. The hand gently lowers its calligraphy brush tip to the dead center of the ivory paper, deposits ONE small black ink dot, then lifts and begins to withdraw toward lower right. Only one brush and one hand, no letters, no other marks. Warm paper fiber macro, delicate precise contact.'
}
items=[]
for sid,prompt in spec.items():
 p=r/f'assets/{sid}.png'
 if not p.exists():continue
 items.append({'id':'m_'+sid,'shot_id':sid,'image_key':sid,'image':str(p.relative_to(root)),'endpoint':'i2v','duration':4,'resolution':'768P','prompt_expansion_mode':'disabled','prompt':prompt+' No dialogue, no text, no subtitles.','out':f'episodes/landing-day-one/assets/m_{sid}.mp4'})
# Each source is a separately staged cut; no action continuity is asserted across these selected proofs.
story={'shots':[{'id':j['shot_id'],'asset':j['image_key'],'start_frame':i*240,'end_frame':(i+1)*240} for i,j in enumerate(items)]}
assets={j['image_key']:j['image'] for j in items}
b=r/'build/motion';b.mkdir(exist_ok=True)
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2))
def bind(p):return {'path':str(p.relative_to(root)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
write(b/'story.json',story);write(b/'assets.json',assets)
judgments={
'S05':'Single seated ChatGPT girl, braid, emerald cuffs and knees clearly visible; open sky; MCU intentionally excludes complete feet.',
'S06':'All six lead silhouettes distinct in a sitting cluster; one bun between Doubao and Gemini hands; Claude is adjacent and visible.',
'S07':'Real human Grok incarnation in diagonal-stripe jacket with shoulder towel, low neon alley staging. Cut is an intentional medium switch.',
'S08':'Full-body real human whale-hood runner, shoes and wet floor visible. Independent lateral coverage preserves whale hood and blue costume.',
'S17':'Felt Claude is a waist-up macro with cream wool hair and terracotta knit; source is a new fully handmade material, no claim of spatial continuity with photo scene.',
'S18':'Six wool figures stand on one miniature floor. Lead palette and costume cues retained; different shot size is intentional.',
'S24':'Six lead figures crouch on a night crossing, feet within source frame. New location and medium are an intentional landing-event change.',
'S27':'ChatGPT cel action body fully visible in crouch with floor stripe beneath sneaker; costume invariant and braid retained.',
'S29':'Two lead figures linked by hands in aerial composition, others at distance; flight is intentional, not a floor continuity claim.',
'P21_touch':'Exactly two index fingertips approach centrally; grey cuff from left, terracotta cuff from right; no body or face appears.',
'S43':'A single right hand with grey cuff and one brush enters camera-side lower right over blank warm paper; central contact location is visible.'}
review={'schema_version':1,'status':'approved','reviewer':'Codex static source-frame review','story':bind(b/'story.json'),'assets':bind(b/'assets.json'),'additional_inputs':[bind(r/'shots.md'),bind(r/'src/painter.ts'),bind(r/'cast-and-world.md')],'sources':[bind(root/p) for p in assets.values()],'cuts':[],'notes':'Source-frame suitability only. Does not certify generated motion. Sequence is selected source tasks, not final edit order.'}
for j,k in zip(items,items[1:]):review['cuts'].append({'from_shot':j['shot_id'],'to_shot':k['shot_id'],'from_asset':j['image_key'],'to_asset':k['image_key'],'relation':'intentional_discontinuity','status':'approved','evidence':judgments[j['shot_id']]+' Next source: '+judgments[k['shot_id']],'issues':[]})
write(b/'continuity.json',review);write(b/'manifest.json',{'continuity_review':str((b/'continuity.json').relative_to(root)),'jobs':items});print(len(items),'clips; estimated',len(items)*4*.03)
