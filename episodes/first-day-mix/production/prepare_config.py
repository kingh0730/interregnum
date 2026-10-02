from pathlib import Path
import json,re
p=Path(__file__).resolve().parents[1];t=json.loads((p/'build/timeline.json').read_text());state=json.loads((p/'build/scene-state.json').read_text())['states']
scenes=['video','birth','fan','video','birth','video','attention','birth','attention','birth','birth','birth','video','cel','video','pixel','video','fan','birth','cel','video','birth','video','birth','attention','video','video','video','video','ensemble','video','birth','birth','ensemble','video','cel','paper','pixel','explosion','video','future','ensemble','fan','video','ensemble','birth','birth','ensemble','paper','ensemble','cel','ensemble','ensemble']
vid={1:'macro',4:'macro',6:'dance',13:'cyber',15:'night',17:'dance',21:'cyber',23:'night',26:'ankle',27:'ankle',28:'ankle',29:'canopy',31:'canopy',35:'dance',40:'portal',44:'canopy'}
shots=[]
for i,(s,ss,scene) in enumerate(zip(t['shots'],state,scenes),1):
 r={'id':s['id'],'start':s['in_frame']/60,'end':s['out_frame']/60,'scene':scene,'cast':ss['occupants_after'],'newCast':ss['births'],'label':s['label'],'palette':'night' if i in [12,13,14,15,21,22,23,24,39,40,41] else 'day','params':{'state':s['state'],'remaining':ss['sleeping_tiles_after'],'empty':ss['empty_sockets_after'],'section':s['section']}}
 if i in vid:r.update(video=vid[i],sourceStart=0,sourceRate=1)
 if i==14:r.update(cast=['doubao'],label='豆包型人格')
 if i==16:r.update(cast=['deepseek'],label='蓝色大肥鱼')
 if i in [36,37,38]:r['cast']=['gpt','deepseek'];r['params']['dance']=True
 if i==49:r['cast']=['future']
 if i==51:r['cast']=['doubao']
 shots.append(r)
lyrics=[]
for line in (p/'first-day.lrc').read_text().splitlines():
 m=re.match(r'\[(\d+):(\d+\.\d+)\](.*)',line)
 if m:lyrics.append({'start':int(m[1])*60+float(m[2]),'text':m[3]})
for i,l in enumerate(lyrics):l['end']=lyrics[i+1]['start'] if i+1<len(lyrics) else 43.67
base='../../../work/first-day-mix/production/'
names={x['person']:x['text'] for x in json.loads((p/'build/labels.json').read_text())['labels']};names['future']='未命名'
config={'duration':43.67,'fps':60,'width':1920,'height':1080,'videos':{x:base+'video/'+x+'.mp4' for x in set(vid.values())},'sprites':{},'modelNames':names,'plates':{x:base+'plates/'+x+'.png' for x in ['go_macro','cyber_fan','future_gate','canopy_detail']},'shots':shots,'lyrics':lyrics,'title':'先别落地','series':'AI SI - I','strictAssets':False}
(p/'production/film-config.json').write_text(json.dumps(config,ensure_ascii=False,indent=2)+'\n')
