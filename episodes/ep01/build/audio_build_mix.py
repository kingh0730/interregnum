"""Reproducible COMMON ROOM 48k stereo mix, stems, onset subtitles and dry lipsync inputs.
Uses recorded/generated acoustic sources only; numpy implements edits, room response and mastering.
"""
import json,math,sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'tools/audio'))
import mix2 as MX
R=MX.R;M=MX.M;SR=48000;W=ROOT/'work/ep01/audio';P=W/'prepared';P.mkdir(parents=True,exist_ok=True)
R.IR_DIR=W/'ir'
story=json.loads((ROOT/'episodes/ep01/build/story.json').read_text());selection=json.loads((W/'dialogue/selection.json').read_text())
def relative(p):return str(p.relative_to(ROOT))
def wav(name,x):
 p=P/name;M.write(p,x,'pcm_f32le');return p
files={'S01':'paper_test','S02':'ceramics','S03':'cloth','S04':'door_latch','S05':'scissors','S06':'drawer','S07':'tape_measure','S08':'water_sink','S09':'footsteps','S10':'cardboard','S11':'extractor'}
source_stats={}
for sid,name in files.items():
 x=MX.load_audio(relative(W/'sfx'/f'{name}.mp3'));pk=np.max(np.abs(x));x=x*R.db(-6)/(pk+1e-12)
 wav(f'{sid}_{name}.wav',x)
 # Locate actual recorded attacks, separated by 0.6s, to make reusable close-contact edits.
 env=np.sqrt(np.mean(R.mono(x)[:len(x)//480*480].reshape(-1,480)**2,axis=1))
 active=np.flatnonzero(env>env.max()*R.db(-24));starts=[]
 for v in active:
  if not starts or v-starts[-1]>65: starts.append(int(v))
 source_stats[sid]={'name':name,'attacks_s':[round(v/100,2) for v in starts]}
# Normalize the two different recordings to a common bed level before a 1-second crossfade.
for sid,name in [('B01','kitchen_air'),('B02','rain_window'),('B03','dry_air'),('B04','hall_air')]:
 pairs=[]
 for take in (1,2):
  x=MX.load_audio(relative(W/'sfx'/f'{name}{take}_v2.mp3'));x=R.filt(x,[['hp',55,2]])
  level=R.span_loudness(x);x=x*R.db(-32-level);pairs.append(x)
 n=SR;f=np.linspace(0,1,n)[:,None]
 x=np.concatenate([pairs[0][:-n],pairs[0][-n:]*(1-f)+pairs[1][:n]*f,pairs[1][n:]])
 wav(f'{sid}_{name}_pair.wav',x)
# Fan's steady region omits its deliberately generated switch clicks.
x=MX.load_audio(relative(W/'sfx'/'extractor.mp3'))[2*SR:8*SR];wav('B05_extractor_steady.wav',x)
(W/'prepared/source_edits.json').write_text(json.dumps(source_stats,indent=2))
spec={'dur':story['total_frames']/24,'out':'work/ep01/audio/master_mix.wav','sources':{'sfx_dir':relative(P),'dialogue':{},'music':{}},'events':[],'ducks':[],'master':{'lufs':-18,'limit_dbfs':-1.8,'max_gr_db':2,'gr_allowed':[]}}
events=spec['events']
def bed(id,sid,spans,pan=0,width=1):events.append({'id':id,'kind':'bed','bus':'ambience','src':{'sfx':sid},'spans':spans,'room':'DRY','pan':pan,'width':width})
bed('AIR_KITCHEN','B01',[[0,157,-38,.3,2],[177,230,-38,1,5]])
bed('AIR_RAIN_RIGHT','B02',[[0,156,-47,.6,2],[177,229,-44,1,4]],.45,.6)
bed('AIR_DRY_LEFT','B03',[[10,156,-49,1.5,2],[170,178,-40,1.5,1],[177,229,-47,1,4]],-.45,.6)
bed('AIR_HALL','B04',[[154.5,163,-37,2,1],[162,171,-33,1,1],[170,177,-39,1,2]],0,1.1)
bed('AIR_EXTRACTOR','B05',[[180,227,-47,2,4]],.35,.5)
# Isolated useful contacts. Each occurs on its image state; broad physical motions remain modest in a still reel.
def hit(id,sid,t,level=-26,pan=0,index=0,length=.8,bus='foley',room='FLAT'):
 attacks=source_stats[sid]['attacks_s'];a=max(0,attacks[index%len(attacks)]-.025) if attacks else 0
 events.append({'id':id,'kind':'shot','bus':bus,'src':{'sfx':sid,'slice':[a,min(a+length,12 if sid!='S07' else 8)]},'at':t,'lvl':level,'lvl_mode':'peak','room':room,'wet':-26,'pan':pan,'fade':[.006,.08],'keep':length})
hit('PAPER_ADDRESS','S01',2.1,-28,-.2,length=1.1)
hit('PAPER_TAB','S01',8.0,-23,-.2,index=2,length=.65)
hit('BOWL_LAST_CHERRY','S02',16,-25,.2,length=.7)
hit('SLEEVE_REACH','S03',17.4,-34,-.2,length=.5)
hit('PAPER_ROOM','S01',40.0,-27,-.2,index=3,length=.8)
hit('HAND_TABLE','S10',61.8,-35,.15,index=2,length=.35)
hit('EDA_STEP','S09',67.5,-32,-.3,length=.6)
hit('TAPE_CASE','S07',69.2,-24,.1,index=3,length=.5)
hit('CARTON_OPEN','S10',73.25,-27,0,length=1.4)
hit('PAN_CARDBOARD','S02',83.2,-26,.2,index=1,length=.7)
# Object rhythm is acoustic recordings; unlike the room, this bus stops once at exactly frame2616.
for n,(t,sid,idx,lev,ln) in enumerate([(85.2,'S02',0,-24,.55),(86.05,'S02',3,-27,.45),(87.0,'S02',1,-23,.6),(89.7,'S08',2,-31,1),(91.1,'S02',2,-24,.45),(92.9,'S02',1,-25,.6),(94.8,'S02',3,-30,.4),(96.1,'S02',2,-24,.45),(97.2,'S08',4,-29,.6),(100.9,'S02',0,-24,.7),(103.0,'S02',4,-27,.45),(104.9,'S08',2,-26,.5),(105.9,'S02',1,-21,.45),(106.65,'S02',3,-25,.4),(107.4,'S08',4,-26,.7),(108.2,'S02',2,-20,1)]):
 hit(f'MODULE_{n:02}',''+sid,t,lev,(-.18 if n%2 else .18),idx,ln,bus='action')
hit('PAN_NEGOTIATION','S02',135.9,-30,.2,index=1,length=.8)
hit('CARTON_CLOSE','S10',147.4,-26,0,index=3,length=1.3)
hit('PAPER_TWO_TABS_A','S01',150.0,-25,-.1,index=2,length=.55)
hit('PAPER_TWO_TABS_B','S01',152.0,-25,.1,index=4,length=.55)
hit('TAPE_CARTON','S07',153.0,-32,.1,index=1,length=.9)
for n,t in enumerate([155.8,156.8,158.0,159.3]):hit(f'HALL_STEP_{n}','S09',t,-29-n*.6,-.2,n,.7,room='HALL_FAR')
hit('CLOTH_NEW_ROOM','S03',173.8,-28,-.15,index=2,length=1.4)
hit('SCISSOR_RETURN','S05',178.7,-27,-.2,length=.8)
hit('CLOTH_SPREAD','S03',181,-31,-.2,index=3,length=1.2)
hit('CLOTH_POINT','S03',193.7,-34,-.2,index=4,length=.6)
hit('BOWL_RETRIEVE','S02',196.2,-27,.2,index=0,length=.7)
hit('CLOTH_LIFT','S03',197.4,-29,-.1,index=1,length=1.1)
hit('SALT_POT','S02',210.4,-31,-.1,index=2,length=.6)
hit('PAPER_CORNER','S01',212.1,-32,-.2,index=1,length=.8)
hit('FINAL_CUP_WEIGHT','S02',216.2,-29,-.1,index=1,length=.6)
hit('FINAL_SCISSOR','S05',219,-32,-.2,index=2,length=.9)
# Original music is three performed sections; discontinuous first movement preserves uncluttered exchanges.
for cid,span,src,lv,fade in [('DIVIDE',[37,50],[0,13],-29,[.8,1.5]),('MODULES',[73,109],[14,50],-26,[.7,.003]),('HALL',[148,173],[50,75],-27,[1.1,2]),('CODA',[214,228],[75,89],-32,[1.5,4])]:
 spec['sources']['music'][cid]={'src':'work/ep01/audio/music/take1.mp3','edit':{'main':{'segments':[{'src':src,'at':span[0],'fade':fade}]}}}
 ev={'id':'MU_'+cid,'kind':'cue','bus':'music','cue':cid,'in':span[0],'out':span[1],'lvl_keys':[[span[0],lv],[span[1]-2,lv]]}
 if cid=='MODULES':ev['lvl_keys']=[[73,-29],[85,-26],[100,-24],[108,-23]];ev['cut']=[109,.003]
 events.append(ev)
spec['mutes']=[{'from':109,'to':119,'except':['AIR_*','D*']}]
# Voice onset is the actual event time. Captions use the measured report rather than guessed raw-file starts.
line_lookup={}
for sh in story['shots']:
 for ln in sh['dialogue']:
  lid=ln['id'];take=selection[lid]['best'];assert take['text_match']>=.85,(lid,take)
  spec['sources']['dialogue'][lid]={'src':relative(W/'dialogue'/take['file']),'chain':'none'}
  at=sh['start_frame']/24+ln['offset'];end=sh['end_frame']/24
  ev={'id':lid,'kind':'line','bus':'dialogue','line':lid,'at':at,'lvl':-21,'lvl_mode':'line','room':'FLAT','wet':-26,'pan':-.07 if ln['speaker']=='EDA' else .07,'end_by':end-.12,'not_before':sh['start_frame']/24+.05,'fit':'shift','peak_ctl':13,'max_gr':2}
  events.append(ev);line_lookup[lid]=(sh,ln,ev)
  dur=take['duration'];spec['ducks'].append({'from':at-.1,'to':min(at+dur,end),'db':-5,'attack':.16,'release':.4,'only':['MU_*']})
sp=ROOT/'episodes/ep01/build/audio_mix.json';sp.write_text(json.dumps(spec,indent=2))
r=MX.Renderer(spec);buses=r.render();r.report['master']=MX.master(spec,buses,W/'master_mix.wav')
assert not r.report['placeholders'],r.report['placeholders']
subs=[];lipmanifest=[];L=W/'lipsync';L.mkdir(exist_ok=True)
for rec in r.report['lines']:
 lid=rec['line'];sh,ln,ev=line_lookup[lid]
 assert not any('MISSES' in s for s in rec['notes']),rec
 assert rec['voiced_end']<=sh['end_frame']/24-.06,(lid,rec)
 subs.append({'line_id':lid,'shot_id':sh['id'],'start_frame':int(math.floor(rec['onset']*24)),'end_frame':min(sh['end_frame'],int(math.ceil((rec['voiced_end']+.15)*24))),'en':ln['text'],'zh':ln['zh']})
 x,on,end,prov=r.line_clip(ev);duration=(sh['end_frame']-sh['start_frame'])/24;out=np.zeros((round(duration*SR),2));start=round((rec['onset']-sh['start_frame']/24)*SR)-on
 # Isolated normalized voice, no ambience/music/reverb, padded to the shot's exact frame length.
 gain=R.db(-20-R.span_loudness(x,on,end));M.place(out,R.as_st(x)*gain,start)
 path=L/f"shot_{sh['id']}_{ln['speaker']}.wav";M.write(path,out,'pcm_s24le')
 lipmanifest.append({'shot_id':sh['id'],'speaker':ln['speaker'],'line_id':lid,'path':relative(path),'frames':sh['end_frame']-sh['start_frame'],'fps':24,'sample_rate':48000,'channels':2,'source':prov,'voiced_onset_seconds':round(rec['onset']-sh['start_frame']/24,3),'voiced_end_seconds':round(rec['voiced_end']-sh['start_frame']/24,3),'use_for_lipsync':sh['kind']=='scene'})
(W/'subtitles.json').write_text(json.dumps(subs,ensure_ascii=False,indent=2));(W/'lipsync_manifest.json').write_text(json.dumps(lipmanifest,indent=2));(W/'master_mix.report.json').write_text(json.dumps(r.report,indent=2))
def stamp(frame):
 ms=round(frame/24*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
(W/'subtitles.srt').write_text('\n\n'.join(f"{i+1}\n{stamp(s['start_frame'])} --> {stamp(s['end_frame'])}\n{s['en']}\n{s['zh']}" for i,s in enumerate(subs))+'\n')
print(json.dumps(r.report['master'],indent=2),flush=True)
