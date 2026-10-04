from pathlib import Path
import json,subprocess
R=Path(__file__).resolve().parents[1]
choices={'S01':(1,1.3),'S03':(2,2.5),'S04':(2,2.5),'S05':(2,2.5),'S16':(1,2.7),'S17':(1,1.9),'S18':(2,2.5),'S21':(3,3.0),'S22':(2,2.4),'S23':(1,2.7),'S24':(1,1.6),'S25':(1,4.3),'S29':(1,1.0),'S30':(1,1.0),'S42':(2,1.0),'S44':(2,1.8)}
media={}
for sid,(take,end) in choices.items():
 f=R/f'assets/motion/{sid}_take{take}.mp4'
 assert f.exists(),f
 media[sid]={'source_id':sid,'file':str(f.relative_to(R)),'fps':30,'source_end':end,'frames':round(end*30),'take':take,'kind':'video'}
media['S20']={'source_id':'S20','file':'assets/motion/S20-test.mp4','fps':120,'source_end':1.6,'frames':192,'take':'test','kind':'interpolated'}
media['S19']={**media['S16'],'source_id':'S16','source_start':1.0,'source_end':2.7}
media['S36']={**media['S29'],'source_id':'S29','source_end':.6}
media['S34']={'source_id':'S34','file':'assets/motion/lip-test.mp4','fps':30,'source_end':1.2,'frames':36,'kind':'lip_composite','premultiply':True}
for owner,file,end,ratio in [('FLIGHT','assets/motion/flight_take1.mp4',2.0,2/3),('FLOAT','assets/motion/float_take2.mp4',2.0,16/9)]:
 media[owner]={'source_id':owner,'file':file,'fps':30,'source_end':end,'frames':round(end*30),'kind':'chroma','aspect':ratio,'mirror':owner=='FLIGHT'}
for sid in ['S26','S27','S28','S31','S38']:media[sid]=dict(media['FLIGHT'])
media['S32']=dict(media['FLOAT'])
(R/'render_kit/text/media.json').write_text(json.dumps(media,indent=2)+'\n')
(R/'production/selected-media.json').write_text(json.dumps(media,indent=2)+'\n')
