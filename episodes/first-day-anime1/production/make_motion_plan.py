import json
from pathlib import Path
r=Path(__file__).resolve().parents[1];p=r/'production/motion_plan.json';d=json.loads(p.read_text());existing={j['id'] for j in d['jobs']}
base='Cinematic modern anime feature-film cel animation, clean confident linework, soft cel shading and painterly luminous backgrounds. Preserve exact identities, anatomy, costumes, objects, composition and lighting from the source. No text, letters, numbers, logos or watermarks; screens, brooches and tags stay blank. One continuous shot, no cuts, no face morphing, no extra limbs. Camera locked for this source pass; the authored camera move is added in compositing. '
rows=[
('S01','S01-v1',3,'Extreme macro eye behind round glasses: a tiny natural shift of focus toward the reflected blank screen, quiet tired breath, no full blink obscuring the eye. Keep glasses geometry and screen reflection stable.'),
('S03','S03-v1',3,'The tired developer remains slumped at her desk, exhales, then lifts her head only slightly toward the monitor. Very underplayed acting; a small shoulder movement. Rain runs slowly down glass. Room furniture stays perfectly still.'),
('S04','S04-v1',3,'She takes one small sip through the milk-tea straw, gently pushes the chair back with the other hand and lets her shoulders relax. Keep both hands anatomically clean with five fingers. No exaggerated gesture.'),
('S05','S05-v1',3,'The developer gives one small warm laugh of disbelief at her blank computer screen, cheeks lift and eyes brighten behind glasses. Her hand stays by her cheek. Screen and hardware must stay fixed and blank.'),
('S16','S16-v3',3,'The anime girl floats in the ivory light column, shy awe on her face. Her two very long coral-to-cream twin-tails gently unfurl and drift, sash follows through. Body rises only slightly, bare feet relaxed. Floating blank papers and keycaps remain nearly frozen. Keep night outside.'),
('S17','S17-v2',3,'Her first breath: lips part softly, she inhales with a tiny natural chest rise, holds a moment, then releases a gentle breath. Hair follows with a light outward drift. Keep amber-coral eyes and face completely consistent; underplayed awe. No exaggerated singing.'),
('S18','S18-v1',3,'The already shattered window ring expands OUTWARD away from the room, glass fragments becoming delicate coral sparks, rain glitters. Keep room geometry intact, no new people or objects. Strong spatial depth and smooth particle motion.'),
('S21','S21-v1',3,'She takes exactly three natural short barefoot steps toward the camera, contacting at approximately 0, 1 and 2 seconds. Left and right feet alternate correctly. The low camera tracks her feet only through the later compositing pass. Hair and sash follow through. She looks up shyly near the end. Preserve five toes on each foot and the single gold ankle charm.'),
('S22','S22-v2',3,'The girl slowly extends her reaching hand a few centimetres toward the developer, while the developer holds her hand out warmly. Hands remain separated, no contact yet. Underplayed anticipation, subtle breath, slight hair movement. Preserve exactly five fingers per hand and night outside.'),
('S23','S23-v1',3,'Their index fingertips remain in exactly the same gentle contact at frame center, a tender shared breath and a barely perceptible tearful smile. Keep the fingertip contact point stationary and all fingers stable. Tiny natural eye and cheek movement only; no reaching or withdrawing.'),
('S24','S24-v1',3,'The two girls sprint hand-in-hand forward onto the balcony, laughing naturally, three quick alternating running steps. Their clasp remains secure and anatomically clean, very long twin-tails and coral sash stream behind with overlap. Keep the same outfits and tan shoes.'),
('S29','S29-v1',2,'Close flying portrait: fearless joyful grin, wind streams the long hair past camera, bright eyes stable, very slight head lift. Do not rotate the body or change framing. No lip-sync needed.'),
('S30','S30-v1',2,'Close flying portrait: she laughs joyfully, short black hair blows, a few tears trail sideways, round glasses remain intact and recognizable. No body flip or camera rotation; preserve the face and framing.'),
('S42','S42-v1',2,'The two girls hold a tender joyful hug while floating, shoulders breathe and the long hair swirls gently around them. Keep the existing arms, hands and bodies exactly coherent, no new limbs, no change of identity. Underplayed smiles.'),
('S44','S44-v1',3,'Quiet dawn in grass: Opus gently wiggles the toes of the near bare foot once, ankle tag catches a tiny glint, both girls breathe peacefully and smile softly. A light breeze moves grass and hair. Keep foot anatomy and all five toes clean. Camera locked; a real crane rig is added later. No large body motion.')]
for sid,src,duration,prompt in rows:
 for take in [1,2]:
  ident=f'{sid}_take{take}'
  if ident in existing:continue
  d['jobs'].append({'id':ident,'shot_id':sid,'image':f'assets/plates/{src}.png','duration':duration,'seed':2026100000+int(sid[1:])*10+take,'out':f'assets/motion/{ident}.mp4','prompt':base+prompt+(' Keep the performance especially restrained and the background stable.' if take==2 else '')})
if 'S20_take2' not in existing:
 j=dict(d['jobs'][0]);j.update(id='S20_take2',seed=2026100421,out='assets/motion/S20_take2.mp4');d['jobs'].append(j)
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
