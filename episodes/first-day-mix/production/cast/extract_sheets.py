"""Exact crop/chroma compositing for explicitly requested green-backed generated cast sheets."""
from pathlib import Path
import json, hashlib
import numpy as np
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[4]
OUT=ROOT/'work/first-day-mix/production/cast'
GROUPS={'core':(3,2,['gpt','deepseek','claude','doubao','gemini','grok']), 'group1':(2,2,['qwen','kimi','yuanbao','wenxin']), 'group2':(2,2,['step','baichuan','glm','spark']), 'group3':(2,2,['sense','pangu','minimax','copilot']), 'group4':(2,2,['alexa','meta','perplexity','siri'])}
GROUPS['poses']=(3,2,['gpt_dance_a','gpt_dance_b','deepseek_dance_a','deepseek_dance_b','future','future_open'])
manifest={'status':'generated artwork; exact crop and chroma extraction; intended authored cutout animation','processing':'fixed grid crop; green-screen unmix alpha; no synthesized pixels; RGB despill only at partial alpha; tight bbox with 12px transparent padding','characters':{}}
for sheet,(cols,rows,ids) in GROUPS.items():
 path=OUT/f'{sheet}-sheet.png'
 if not path.exists(): continue
 im=Image.open(path).convert('RGB'); w,h=im.size
 for i,id in enumerate(ids):
  rect=(i%cols*w//cols,i//cols*h//rows,(i%cols+1)*w//cols,(i//cols+1)*h//rows)
  # The actual group1 layout places Yuanbao's forelock just above the nominal row split.
  # Rows 748-750 are clean green: a measured cut at 750 preserves both complete figures.
  if id=='qwen': rect=(0,0,w//2,750)
  if id=='yuanbao': rect=(0,750,w//2,h)
  if sheet=='group2':
   rect=(i%2*w//2,0 if i<2 else 735,(i%2+1)*w//2,735 if i<2 else h)
  if id=='sense': rect=(0,0,512,750)
  if id=='pangu': rect=(512,0,1024,740)
  if id=='minimax': rect=(0,750,550,h)
  if id=='copilot': rect=(512,740,1024,h)
  if id=='alexa': rect=(0,0,490,750)
  if id=='meta': rect=(490,0,1024,750)
  if id=='perplexity': rect=(0,750,512,h)
  if id=='siri': rect=(512,750,1024,h)
  if id=='gpt_dance_a': rect=(0,0,512,500)
  if id=='deepseek_dance_b': rect=(0,500,512,h)
  if id=='deepseek_dance_a': rect=(1024,0,1536,450)
  if id=='future_open': rect=(1024,450,1536,h)
  cell=im.crop(rect); rgb=np.asarray(cell).astype(np.float32)
  r,g,b=rgb[:,:,0],rgb[:,:,1],rgb[:,:,2]
  mx=np.maximum(r,b)
  # Reference background is saturated green. Retain subdued celadon/jade costume interiors.
  strength=np.clip((g-mx-18)/np.maximum(1,235-mx),0,1)
  strength=np.where((g>125)&(g>mx*1.30),strength,0)
  alpha=1-strength
  alpha=np.where(alpha<.06,0,alpha)
  # Disjoint bent cell boundary preserves MiniMax's reaching fingertips and Copilot's low coat.
  yy,xx=np.indices(alpha.shape); sheet_x=xx+rect[0]; sheet_y=yy+rect[1]
  if id=='minimax': alpha=np.where((sheet_y>=1050)&(sheet_x>=512),0,alpha)
  if id=='copilot': alpha=np.where((sheet_y<1050)&(sheet_x<550),0,alpha)
  # Green pixels at anti-aliased boundaries are a mixture of subject and the known screen.
  corrected=rgb.copy(); edge=(alpha>0)&(alpha<.98)
  corrected[:,:,1][edge]=np.clip((g[edge]-(1-alpha[edge])*255)/np.maximum(alpha[edge],.06),0,255)
  corrected[:,:,0][edge]=np.clip(r[edge]/np.maximum(alpha[edge],.06),0,255)
  corrected[:,:,2][edge]=np.clip(b[edge]/np.maximum(alpha[edge],.06),0,255)
  rgba=np.dstack([corrected,np.rint(alpha*255)]).astype('uint8')
  ys,xs=np.where(alpha>.08)
  box=(max(0,int(xs.min())-12),max(0,int(ys.min())-12),min(cell.width,int(xs.max())+13),min(cell.height,int(ys.max())+13))
  sprite=Image.fromarray(rgba).crop(box)
  target=OUT/f'{id}.png'; sprite.save(target)
  manifest['characters'][id]={'path':str(target.relative_to(ROOT)), 'sheet':str(path.relative_to(ROOT)), 'sheet_size':[w,h], 'cell_rect_xyxy':rect,'tight_crop_within_cell_xyxy':box,'size':list(sprite.size),'body_alpha_bbox':list(sprite.getbbox()),'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'sha256':hashlib.sha256(target.read_bytes()).hexdigest()}
allrows=dict(manifest['characters'])
manifest['variants']={k:manifest['characters'].pop(k) for k in list(manifest['characters']) if '_dance_' in k or k=='future_open'}
(ROOT/'episodes/first-day-mix/production/cast/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
# A checkerboard contact board verifies alpha and silhouette on light/dark squares.
board=Image.new('RGB',(1320,((len(allrows)+5)//6)*300),(224,227,233)); draw=ImageDraw.Draw(board)
for i,(id,row) in enumerate(allrows.items()):
 x,y=(i%6)*220,(i//6)*300
 for xx in range(x,x+220,20):
  for yy in range(y,y+280,20):
   if ((xx-x)//20+(yy-y)//20)%2:draw.rectangle((xx,yy,xx+19,yy+19),fill=(90,98,115))
 sp=Image.open(ROOT/row['path']);sp.thumbnail((210,265),Image.Resampling.LANCZOS)
 board.paste(sp,(x+(220-sp.width)//2,y+(270-sp.height)//2),sp)
 draw.text((x+8,y+282),id,fill=(15,20,30))
board.save(OUT/'cast-alpha-review.jpg',quality=93)
print(json.dumps({'count':len(manifest['characters']),'sizes':{k:v['size'] for k,v in manifest['characters'].items()}},indent=2))
