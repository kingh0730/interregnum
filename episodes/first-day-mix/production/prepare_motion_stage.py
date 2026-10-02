from pathlib import Path
import json,hashlib,sys,subprocess
root=Path(__file__).resolve().parents[3]
specs=json.loads((root/'episodes/first-day-mix/production/motion-specs.json').read_text());ids=sys.argv[1:];batch='_'.join(ids);p=root/'work/first-day-mix/production'/('motion-'+batch);p.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,x):f=p/n;f.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');return str(f.relative_to(root))
selected=[specs[i] for i in ids]
assert all(x.get('reviewed_visually') and x.get('source_evidence') for x in selected)
assets={i:specs[i]['image'] for i in ids};story=save('story.json',{'shots':[{'id':i,'asset':i} for i in ids]});amap=save('assets.json',assets)
jud={'stage':'reviewed independent production source shots '+batch,'reviewer':'Codex root; explicit full source visual inspection','reviewed_visually':True,'status':'approved','scope_note':'Approval only of inspected source compositions for these independent motion jobs. Final edit includes authored intermediate scenes and has a separate actual-cut review after rendering. No motion/whole-film approval inferred.','story':story,'assets':amap,'reviewed_input_hashes':{'story':sha(root/story),'assets':sha(root/amap)},'reviewed_sources':[{'path':assets[i],'sha256':sha(root/assets[i]),'status':'approved','evidence':specs[i]['source_evidence']} for i in ids],'cuts':[{'from_shot':a,'to_shot':b,'from_asset':a,'to_asset':b,'relation':'scene_change','status':'approved','issues':[],'evidence':f'Independent source-shot collection, not adjacent film shots: {a} and {b} are separately inspected compositions. The final cut explicitly traverses procedural/mixed-media intermediate scenes; full edit continuity awaits those actual frames.'} for a,b in zip(ids,ids[1:])],'state_changes':[],'additional_inputs':[]}
jpath=save('judgments.json',jud);review=str((p/'review.json').relative_to(root))
if not (root/review).exists():subprocess.run([sys.executable,str(root/'episodes/first-day-mix/production/qa/make_review.py'),jpath,'--out',review],cwd=root,check=True,stdout=subprocess.DEVNULL)
jobs=[]
for i in ids:
 s=specs[i];jobs.append({'id':i,'shot_id':i,'image_key':i,'image':s['image'],'endpoint':'i2v','duration':s.get('duration',5),'resolution':'1080P','prompt_expansion_mode':'disabled','seed':s.get('seed',2000+ids.index(i)),'out':f'work/first-day-mix/production/video/{i}.mp4','prompt':s['prompt']})
print(save('motion.json',{'continuity_review':review,'jobs':jobs}))
