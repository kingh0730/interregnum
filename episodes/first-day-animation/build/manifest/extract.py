from pathlib import Path
import re,json,hashlib,collections
from decimal import Decimal,ROUND_HALF_UP
root=Path('episodes/first-day-animation'); src=root/'director-response.md'; text=src.read_text(); out=root/'build/manifest'
write=lambda n,v:(out/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
frame=lambda t:int((Decimal(str(t))*30).quantize(Decimal('1'),rounding=ROUND_HALF_UP))
section5=text.split('## 5. MASTER SHOT LIST')[1].split('## 6.')[0]
shots=[]
for line in section5.splitlines():
 if not re.match(r'\| S\d',line):continue
 c=[x.strip() for x in line.strip('|').split('|')]; a,b,d=re.match(r'([\d.]+)–([\d.]+) \(([\d.]+)\)',c[1]).groups()
 shots.append(dict(id=c[0],start=float(a),end=float(b),duration=float(d),start_frame=frame(a),end_frame=frame(b),frames=frame(b)-frame(a),source=c[2].replace('*',''),camera=c[3],action=c[4],fx=c[5],verbatim_row=line))
meta=dict(source=str(src),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),fps=30,total_frames=1311,frame_rounding='round-half-up(t * 30); intervals [start_frame,end_frame)')
write('shots.json',dict(**meta,shots=shots))
style=re.search(r'`STYLE:` (.*)',text).group(1); neg=re.search(r'`NEG:` (.*)',text).group(1); char=re.search(r'Always append: `(.*?)`',text).group(1)
charsec=text.split('### 3.3 Characters')[1].split('### 3.4')[0]
wu=re.search(r'\*\*五五.*?\*\*: (.*)',charsec).group(1)
sisters='\n'.join(x for x in charsec.splitlines() if x.startswith(('**Sonnet','**Haiku','**Clawd')))
sec6=text.split('### Keyframe + motion prompts')[1].split('**Depth maps')[0]
entries=[]
def item(id,kf,motion,raw,refs=None,kind='keyframe',output=None):
 refs=refs if refs is not None else ['REF_WUWU']
 clause=char.replace('[ref sheet]','assets/ref/wuwu.png')
 prompt='STYLE: '+style+'\n'+clause+'\n'+kf+'\nNEG: '+neg
 e=dict(id=id,out=output or f'assets/keyframes/{id}.png',kind=kind,prompt=prompt,source_keyframe=kf,source_motion=motion,verbatim_spec=raw,refs=refs,alpha=False,deps=refs,shots=[id.split('_')[0]],provider='codex-imagegen',motion_prompt=(('STYLE: '+style+'\n'+motion+' smooth, no cut, no morphing of face, hair stays ink-charcoal to terracotta\nNEG: '+neg+'\n'+clause) if motion else None))
 entries.append(e)
item('REF_WUWU','Full-body turnaround (front/side/back/3/4) + 6 expressions of 五五. Backgrounds plain ivory. '+wu,'','**Step 1: Character sheet.** Full-body turnaround (front/side/back/3/4) + 6 expressions of 五五; second sheet with Sonnet-chan, Haiku-chan, Clawd. Backgrounds plain ivory. Generate until hair gradient, spark ahoge and spark eye are consistent. Save as `assets/ref/`.',[],kind='reference',output='assets/ref/wuwu.png')
entries[-1]['prompt']='STYLE: '+style+'\n'+entries[-1]['source_keyframe']+'\nNEG: '+neg;entries[-1]['shots']=[]
item('REF_SUPPORT','Second character reference sheet with Sonnet-chan, Haiku-chan, Clawd. Backgrounds plain ivory. '+sisters,'',entries[0]['verbatim_spec'],[],kind='reference',output='assets/ref/support.png')
entries[-1]['prompt']='STYLE: '+style+'\n'+entries[-1]['source_keyframe']+'\nNEG: '+neg;entries[-1]['shots']=[]
for line in sec6.splitlines():
 m=re.match(r'\*\*(S\d+[a-z]?)(?: \([^)]*\))?\*\*: \*KF:\* (.*)',line)
 if not m: continue
 id,tail=m.groups(); parts=re.split(r' \*(?:Motion|Depth \+ P-camera|P-camera):\* ',tail); kf=parts[0]; motion=parts[1] if len(parts)>1 else ''
 refs=['REF_WUWU']+(['REF_SUPPORT'] if id in ['S03c','S09a','S10a','S10b','S16a'] else [])
 item(id,kf,motion,line,refs)
raw=next(l for l in sec6.splitlines() if l.startswith('**S13a–d'))
for suffix,kf,m in zip('abcd',['五五 mid-pose with orange burst','Sonnet-chan with blue light flood','Haiku-chan in a shower of green confetti glyphs','Clawd holding a sparkler'],['90° orbit','whip-orbit','handheld bounce','snap zoom']):item('S13'+suffix,kf,m,raw,['REF_WUWU'] if suffix=='a' else ['REF_SUPPORT'])
raw=next(l for l in sec6.splitlines() if l.startswith('**S09b ('))
item('S09b_color',"五五 on the other side of a glass pane, palm raised, the user's silhouette reflected. Full color base image for the pixel-aligned pencil-linework reveal wipe.",'',raw,output='assets/keyframes/S09b_color.png')
rawline=next(l for l in sec6.splitlines() if l.startswith('**S09b line-art'))
item('S09b_line','Generate a second image of S09b as clean pencil linework only (black lines on ivory) for the reveal wipe. Same composition, pixel-aligned (use img2img/edit tool with the color image as source).','',rawline,['S09b_color'],kind='edit',output='assets/keyframes/S09b_line.png')
entries[-1]['prompt']='Transform the provided S09b color image into clean pencil linework only (black lines on ivory) for the reveal wipe. Same composition, pixel-aligned. Preserve all characters, pose, camera, framing, geometry and silhouettes. No text, watermark, new elements, or color fills.\nOriginal mandated STYLE (line-art instruction takes precedence): '+style+'\nNEG: '+neg+'\n'+char.replace('[ref sheet]','assets/ref/wuwu.png')
entries.sort(key=lambda e:(e['kind']!='reference', e['id']))
write('image-manifest.json',dict(**meta,style=style,negative=neg,character_clause=char,notes=['User mandates Codex imagegen and forbids Luma.','Source prompt text retained verbatim; expansions explicitly identified.','S09b color is required by §7.10; line-art is a dependent edit.','Review qa.json before production: literal global CHAR clause is unsuitable for solo support-character shots.'],images=entries))
counts=collections.Counter(s['source'] for s in shots)
checks=dict(shot_count=len(shots),source_counts=dict(counts),frame_sum=sum(s['frames'] for s in shots),contiguous=all(a['end_frame']==b['start_frame'] for a,b in zip(shots,shots[1:])),keyframes=len(entries)-2,references=2,missing_keyframe_shots=[s['id'] for s in shots if s['source']!='H' and not any(s['id'] in e['shots'] for e in entries)])
conflicts=[
('counts','§5 states 21 V, 9 P, 7 H (37 total). Actual rows have '+str(dict(counts))+'.','Use all 37 actual rows. There are 20 V, 9 pure P, 6 pure H, and 2 hybrid shots; the printed source subtotals are inaccurate.'),
('grid_rounding','Hard title time 11.92 s is not on a 30 fps frame; round(t×30) = 358 = 11.9333 s. Other times have same quantization.','Preserve authored seconds as metadata, quantize once with round-half-up and use frame intervals.'),
('cut_grid','§9 says copy §5 verbatim, §7.9 says snap every non-lyric cut ±0.08 s to detected beats.','Keep verbatim planned times and separately record any measured-grid adjustments; never silently mutate source.'),
('char_global','§3.4 and §6 append Wuwu hair/outfit clause to every image, including solo Sonnet, Haiku, Clawd, and line-art.','Literal expansion retained. In production scope Wuwu traits to Wuwu only; solo support frames retain their §3.3 identities.'),
('line_color','§6 S09b shorthand describes pencil linework; §7.10 requires both color and line textures and §6 requests a second edited line version.','Generate color base first, then pixel-aligned line-art edit. Line-art requirements override luminous/full-color style.'),
('counter_duration','S04b lasts 1.05 s (about 3 beats), but six values 5.0 through 5.5 at one value per beat require five intervals (about 1.7425 s). §4 starts counter at 8.24; §5 starts at 9.59.','Keep S04b shot timing; director must explicitly resolve counter tick rate or carry progression over S04a.'),
('hypercuts','§8 calls S13 cuts every beat (~0.3485 s), while §5 S13a-d last ~0.66–0.70 s (about two beats).','Keep explicit shot list; beat accents can occur inside each shot.'),
('audio_codec','§7.3 sample re-encodes source MP3 to AAC, conflicting with untouched original audio and §7.11 bit-identical content.','Use source audio stream copy where container permits, check audio packet payload hash and playback timing.'),
('end_card','S16c asks last 0.3 s fade to ivory and §7.10 final stable clean card; fading whole image erases card text.','Fade animated scene/FX toward ivory while preserving stable final card lockup.'),
('crash_zoom','§7.4a scale = 1 + 5*(1-outExpo(u)) moves scale 6→1, opposite to §5 and §6 wide→close crash zoom.','Implement camera wide-to-close / scale 1→6 with eased settling.'),
('wipe_direction','§7.10 mix(line,color,smoothstep(...uv...-u)) with increasing u decreases color coverage, reversing required line→color.','Invert mask or swap mix endpoints, ensuring line at start and color at end.'),
('silence_overlay','§5 S05 says overlay nothing else; §7.7 L4 spans S05 and would render lyrics unless gated.','Suppress all lyric/UI overlays during S05, leaving contracted spark and prescribed drift.'),
('parallax_coverage','S07b macro brooch keyframe must pull back to face; narrow crop lacks face. §5 demands 90° orbit for S13a from one still.','Generate sufficient field-of-view and layered coverage; use explicit camera projection and bounded parallax, record limitations without silently dropping moves.')]
write('qa.json',dict(**meta,checks=checks,conflicts=[dict(id=i,evidence=e,resolution=r) for i,e,r in conflicts],prompt_verification=dict(ordinary_rows='shot-specific KF and motion snippets copied by regex without rewording',grouped_S13='split exact (a)-(d) text; one image per row',S09b='derived color counterpart is explicitly labeled; line-art edit retains required composition',references='expanded from §3.3 and §6 reference instructions',prohibited_source_used=False)))
assert checks['contiguous'] and checks['frame_sum']==1311 and not checks['missing_keyframe_shots']
print(json.dumps(checks,indent=2))
