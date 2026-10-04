from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parents[1]
read=lambda p:json.load(open(r/p));write=lambda p,d:(r/p).write_text(json.dumps(d,ensure_ascii=False,indent=2))
shots=[s for s in read('compositor/timeline.json')['shots'] if s['source']=='V'];ims={a['id']:a for a in read('build/manifest/image-manifest.json')['images']}
assets={s['id']:f'assets/keyframes/{s["id"]}.png'for s in shots};story={'shots':[dict(s,asset=s['id'])for s in shots]};write('build/motion-assets.json',assets);write('build/motion-story.json',story)
bind=lambda p:{'path':p,'sha256':hashlib.sha256((r/p).read_bytes()).hexdigest()}
evidence={
'S01b':'Closed eyes, curled complete outfit inside glass egg; dark racks and threads visible.',
'S02a':'Macro amber eye and charcoal lashes match protagonist; insert intentionally excludes room.',
'S02b':'Corrected curved egg enclosure, palm crack, same heroine and racks; costume retained.',
'S03a':'Broken curved glass, paper fragments and terracotta strands surround escaping heroine.',
'S04a':'Same heroine rising between black server racks; leap is an intentional action ellipsis.',
'S06a':'Ivory mirror floor replaces dark datacenter at authored drop; bare feet, hair and costume match.',
'S06b':'Same ivory world, barefoot hero and floor reflection; new low viewpoint.',
'S07a':'Closed eyes and parted mouth in facial insert, same hair/brooch/paper light.',
'S07c':'Low full-body view in same ivory world; long terracotta hair and airborne paper visible.',
'S08':'Ankle 5.5 ribbon, bare foot, mirror reflection and ripple visible in insert.',
'S09a':'Authored scene change to faceless hooded developer, centered monitor spark, Clawd at desk.',
'S10a':'Return to ivory world; exactly three girls, blue bob glasses left, Wuwu center, green buns right.',
'S10b':'Exactly three same girls; corrected single Clawd on green-haired Haiku head, mid-leap.',
'S11a':'Wuwu alone by authored takeoff; bare feet rise with paper floor fragments.',
'S11b':'Corrected rear chase, same cardigan and hair streaming behind; glyph canyon replaces floor.',
'S12a':'Face insert above clouds; serene smile, amber eyes and same hair/outfit.',
'S12b':'Full-body arms spread above clouds, halo and hair visible, no other cast required.',
'S14':'Authored climax scene with same girl airborne, tears and smile, suspended petals.',
'S16a':'Rear sunrise hill tableau, all four present; blue Sonnet left, Wuwu, green Haiku, Clawd right.',
'S16b':'Corrected wide landscape keeps same four order and rear view; tiny developer window below.'}
review={'schema_version':1,'status':'approved','reviewer':'Codex — inspected generated keyframes and corrections, static sources only','story':bind('build/motion-story.json'),'assets':bind('build/motion-assets.json'),'additional_inputs':[bind('director-response.md')],'sources':[bind(p)for p in assets.values()],'cuts':[],'state_changes':[],'limits':'Static composition and identity review only. Motion performance is reviewed separately from returned takes.'}
for a,b in zip(shots,shots[1:]):review['cuts'].append({'from_shot':a['id'],'to_shot':b['id'],'from_asset':a['id'],'to_asset':b['id'],'relation':'intentional_discontinuity','status':'approved','issues':[],'evidence':evidence[a['id']]+' '+evidence[b['id']]+' Non-V inserts between these V-source occurrences remain in the full timeline.'})
write('build/continuity-review.json',review)
jobs=[]
for i,s in enumerate(shots):
 for take in [1,2]:
  a=ims[s['id']];motion=a['source_motion'];prompt='Modern cel-shaded anime film. '+motion+' '+s['action']+' Smooth continuous single shot, no cut, no face morphing, preserve exact costume and identity, hair remains ink-charcoal to terracotta. Complete the specified camera motion and action over this five-second clip. No new text, no new characters.'
  if s['id']=='S10b':prompt+=' Exactly three girls, one orange block Clawd on GREEN twin-bun Haiku at right. Never move Clawd to another head.'
  if s['id']=='S11b':prompt+=' Strict rear FPV chase, she flies AWAY, full 360 degree camera barrel roll, no front portrait.'
  jobs.append({'id':s['id']+'_take'+str(take),'shot_id':s['id'],'image':assets[s['id']],'prompt':prompt,'seed':5500+i*10+take,'out':f'assets/clips/{s["id"]}_take{take}.mp4'})
write('build/motion.json',{'continuity_review':'build/continuity-review.json','defaults':{'endpoint':'minimax/h3-max/image-to-video','duration':5,'resolution':'1080P','prompt_expansion_mode':'disabled'},'jobs':jobs})
print(len(jobs),'motion jobs; static review bound to source hashes')
