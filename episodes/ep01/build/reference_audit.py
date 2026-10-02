"""Record reviewed reference dimensions and hashes; no generation calls."""
import hashlib,json
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[3]
names=['ref_eda','ref_sen','eda_sheet','sen_sheet','ref_kitchen','ref_props','ref_modules','ref_paper']
notes={
'ref_eda':'Approved full frame and native1024px face crop. Ordinary middle-aged East Asian woman; retain exact compact bob, face and ink-blue/bone costume. Tiny natural skin details are part of this master, not permission to add weathering.',
'ref_sen':'Approved full frame and native1024px face crop. Ordinary middle-aged Black man with cropped curls, clean-shaven silhouette; preserve clay shirt and face.',
'eda_sheet':'Approved Codex derived three-view sheet; identity review reference. Luma scene jobs use base only for this adult face.',
'sen_sheet':'Approved Codex derived three-view sheet; identity review reference. Luma scene jobs use base only for this adult face.',
'ref_kitchen':'Approved empty location: left packed room, right rain landing; sinkleft/hobright, onecounter, twoashshelves, oneforegroundtable and paleyellowpendant. Geometry authority.',
'ref_props':'Approved recurring prop designs: bluebowl/onecrookedwhitestripe, carbonsteelpan/lid, mustardtapemeasure, stonewaresaltpot. Shot-specific count/content may change only as script records.',
'ref_modules':'Approved separate floorstanding compact sink and hob units; plainfronts, no invented drawer. Must remain practical furniture scale, unplugged during trial.',
'ref_paper':'Approved plain overhead ash substrate for exact authored in-world letterlocking inserts.'}
rows=[]
for n in names:
 p=ROOT/f'work/ep01/refs/{n}.png'
 rows.append({'id':n,'path':str(p.relative_to(ROOT)),'size':list(Image.open(p).size),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'review':notes[n]})
(ROOT/'episodes/ep01/build/reference_audit.json').write_text(json.dumps({'reviewed_by':'Codex director','review_scope':'Actual full frames; face masters also native-size crop; sheets inspected in returned tool images. No motion or audio perceptual claim.','references':rows},indent=2)+'\n')
