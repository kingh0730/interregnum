"""Compile the existing First Day Mix decisions into an illustrated review PDF.
Run: work/first-day-mix/pdf-venv/bin/python episodes/first-day-mix/build/compile_decisions_pdf.py
No new creative assets or production approvals are implied by this document.
"""
from pathlib import Path
import json, re, math
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.utils import ImageReader
from PIL import Image

ROOT=Path(__file__).resolve().parents[3]
EP=ROOT/'episodes/first-day-mix'; ART=ROOT/'work/first-day-mix/art'
OUT=ROOT/'output/pdf/first-day-mix-decisions.pdf'; QA=ROOT/'work/first-day-mix/pdf-qa'
OUT.parent.mkdir(parents=True,exist_ok=True); QA.mkdir(parents=True,exist_ok=True)
pdfmetrics.registerFont(TTFont('Body','/System/Library/Fonts/Supplemental/Arial Unicode.ttf'))
pdfmetrics.registerFont(TTFont('Bold','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Body',boldItalic='Bold')
W,H=960,600; M=42
BG='#F5F2E9'; INK='#14284D'; BLUE='#2452C7'; MUTED='#647085'; PEACH='#F0B28B'; LINE='#D6DCDf'
c=canvas.Canvas(str(OUT),pagesize=(W,H),pageCompression=1)
c.setTitle('First Day Mix | Decisions through art direction | 先别落地')
c.setAuthor('AI SI - I production development');c.setSubject('Story, visual tests, casting, pacing, technical plan and outstanding production checks')
PAGE=0

def rect(x,y,w,h,color,stroke=None):
 c.setFillColor(HexColor(color)); c.setStrokeColor(HexColor(stroke or color));c.rect(x,H-y-h,w,h,fill=1,stroke=bool(stroke))
def line(x,y,x2,y2,color=LINE,width=1):
 c.setStrokeColor(HexColor(color));c.setLineWidth(width);c.line(x,H-y,x2,H-y2)
def txt(s,x,y,size=12,font='Body',color=INK):
 c.setFillColor(HexColor(color));c.setFont(font,size);c.drawString(x,H-y-size*.8,s)
def para(s,x,y,w,size=12,color=INK,leading=None,maxbottom=552):
 st=ParagraphStyle('p',fontName='Body',fontSize=size,leading=leading or size*1.43,textColor=HexColor(color),spaceAfter=0)
 p=Paragraph(s,st);ww,hh=p.wrap(w,1000)
 assert y+hh<=maxbottom,(PAGE,s[:60],y,hh)
 p.drawOn(c,x,H-y-hh);return y+hh

def start(kicker,title,subtitle=None):
 global PAGE
 PAGE+=1;rect(0,0,W,H,BG)
 txt('AI SI - I   /   FIRST DAY MIX',M,24,9,'Bold',BLUE)
 txt(kicker.upper(),620,24,9,'Bold',MUTED)
 txt(title,M,61,29,'Bold')
 if subtitle:para(subtitle,M,99,876,11.5,MUTED)
 c.bookmarkPage('p'+str(PAGE));c.addOutlineEntry(title,'p'+str(PAGE),0)
def end():
 line(M,561,918,561);txt('DECISIONS THROUGH ART DIRECTION  /  02 OCT 2026',M,573,8,'Bold',MUTED)
 txt(f'{PAGE:02d}',894,571,11,'Bold',BLUE);c.showPage()
def img(name,x,y,w,h=None):
 f=ART/(name+'.png') if '/' not in name else ROOT/name
 im=Image.open(f).convert('RGB');native=im.width/im.height
 hh=w/native if h is None else min(h,w/native);ww=hh*native
 jpg=QA/(f.stem+'-embed.jpg')
 if not jpg.exists():im.save(jpg,quality=91,optimize=True)
 c.drawImage(str(jpg),x+(w-ww)/2,H-y-hh,width=ww,height=hh)
 return y+hh

def note(label,body,x,y,w=265):
 txt(label,x,y,11,'Bold',BLUE);return para(body,x,y+21,w,12)
def linklabel(label,url,x,y,w=850):
 return para(f'<link href="{escape(url)}" color="{BLUE}">{escape(label)}</link>',x,y,w,10.3)

# 1 Cover: selected artwork, with a plain statement of scope.
PAGE+=1;rect(0,0,W,H,BG);img('c3',0,0,960,440)
rect(0,427,960,173,INK);txt('AI SI - I  /  MUSIC PILOT',42,447,10,'Bold','#AEC5FF')
txt('先别落地',42,470,32,'Body','#FFFFFF');txt('DON\'T LAND YET',235,478,23,'Bold','#FFFFFF')
para('The decisions so far',42,515,580,18,'#FFFFFF')
para('43.67 seconds · Mandarin · concept, script and art direction',42,545,740,11,'#CDD8EE',maxbottom=580)
para('Selected design reference C3.<br/>Concept art, not a finished shot.',695,481,225,10,'#CDD8EE')
c.bookmarkPage('p1');c.addOutlineEntry('Cover','p1',0);c.showPage()

# 2 executive decision overview
start('01 / The creative decision','A spectacle with a rule','The technique changes should tell the story, so a viewer can follow the film before recognizing any AI name.')
rect(42,137,876,91,BLUE)
para('Each awakened tile creates a new friend - and removes somewhere to stand. The growing cast turns a paper sling into a shared sail, then chooses to awaken its last foothold.',62,156,835,18,'#FFFFFF',24)
for x,y,l,b in [
(42,255,'STORY','A physical rescue and a deliberate final choice. ChatGPT and DeepSeek carry the relationship; the ensemble enlarges its consequences.'),
(346,255,'LOOK','Photographic people and tactile mechanisms meet complete cel, paper, pixel and woodblock figures. Medium changes follow contact.'),
(650,255,'PACE','Rapid cuts and dense action, interrupted by a 2.06-second visual hold. Speed is a pattern with contrast, not one unbroken setting.'),
(42,399,'CAST','22 named contemporary AI figures plus one unnamed future person. Six get distinctive actions; the rest enter in groups.'),
(346,399,'SOUND','Keep the supplied Mandarin song and its full tail. No product-name lyric rewrite, new narration or extra score.'),
(650,399,'CURRENT STATUS','Art direction selected. Identity masters, exact geography, dance quality and musical sync still belong to later production.')]:note(l,b,x,y)
end()

# 3 alternatives and reason
start('02 / Concept selection','Why this story won','The comparison used the project taste rubric. Scores are editorial judgments, not measured audience response.')
rows=[('A','DON\'T LAND YET','23 / 30 · selected','Birth consumes the floor. Each new companion adds a real staging problem, and every material change can show cause, contact and result.'),('B','LEND ME A FRAME','22 / 30 · revise','Existing characters surrender animation frames so a newcomer can move. Strong formal idea, but explaining frame ownership would compete with 22 names and a 44-second song.'),('C','TOMORROW DEVELOPS FIRST','16 / 30 · drop','A photograph develops backward and reveals a missing photographer. The future-photo puzzle is more familiar and makes the viewer solve exposition instead of enjoying physical action.')]
y=145
for letter,title,score,body in rows:
 rect(42,y,54,54,BLUE if letter=='A' else '#DCE3EE');txt(letter,59,y+12,29,'Bold','#FFFFFF' if letter=='A' else BLUE)
 txt(title,117,y,15,'Bold');txt(score,701,y+2,12,'Bold',BLUE)
 para(body,117,y+28,774,12);line(117,y+96,918,y+96);y+=118
para('<b>Nearest precedent:</b> <i>Balance</i> (1989) also makes mutual dependence visible on a floating support. Our distinguishing rule is that the support becomes new people. Search did not establish uniqueness; it helped identify what must stay legible.',42,503,876,10.5,MUTED)
end()

# 4 story arc and mechanics
start('03 / The story in six movements','The spectacle grows out of the problem','These are the intended events, not a description of already-generated footage.')
beats=[('00.00-05.23','WAKE','A Go stone presses the first marked tile. ChatGPT wakes; a second tile becomes DeepSeek. An empty socket remains.'),('05.23-17.61','MULTIPLY','New companions consume more tiles. A sling, folded scenes and attention-like paths help them move through changing media.'),('17.61-19.67','STOP','DeepSeek pauses on a narrow inert rim. The camera locks. Busy graphics disappear; the supplied song continues.'),('19.67-28.55','LIFT','The sling opens into a canopy. It catches the previously established updraft. New arrivals clip into spare lines; dance can accelerate.'),('28.55-37.07','CHOOSE','Speculative future branches appear. The pair presses the reserved final tile. A new person opens; the last rigid support falls away.'),('37.07-43.67','CARRY','The canopy dips under the added weight, then steadies. End on the living group and the empty oval; the future gets no product logo.')]
for i,(time,title,body) in enumerate(beats):
 x=42+(i%3)*304;y=143+(i//3)*177
 txt(time,x,y,11,'Bold',BLUE);txt(title,x,y+25,16,'Bold');para(body,x,y+54,269,12)
rect(42,506,876,38,'#E2E8F3');para('<b>The rule is bounded:</b> only marked sleeping tiles activate once. Clothing, bodies, props and empty sockets do not reproduce.',55,514,849,11)
end()

# 5 all six initial explorations
start('04 / Three art directions','What the initial tests actually showed','Two independent frames per direction. Each candidate had attractive qualities and clear failures.')
cols=[('A','Photographed miniatures','a1','a2','KEEP tactile ceramic and paper.','REJECT the persistent floor, fantasy scenery and unsupported flight.'),('B','Complete cel animation','b1','b2','KEEP clean contours and strong poses.','REJECT the invented ruins and solid platforms; limited material range alone.'),('C','Committed mixed media','c1','c2','SELECT the medium boundary and diagonal ensemble.','FIX surviving supports, character scale and contact geometry.')]
for i,(tag,title,a,b,keep,change) in enumerate(cols):
 x=42+i*298;txt(tag+' / '+title,x,137,13,'Bold');img(a,x,165,280);img(b,x,329,280)
 para(keep+' '+change,x,493,280,10.3,leading=14)
end()

# 6 daylight comparison
start('05 / Daylight revision','Give flight a visible source','C2 established the attractive mixed-media direction. C3 changed the support mechanism.')
for name,x,label in [('c2',42,'C2 / BEFORE'),('c3',490,'C3 / SELECTED DAYLIGHT REFERENCE')]:
 txt(label,x,138,11,'Bold',BLUE);img(name,x,164,428)
line(42,421,918,421)
note('WHAT CHANGED','The bowl beneath the leads was removed. The articulated paper structure moved above the cast and gained visible harness lines.',42,443,265)
note('WHY IT MATTERS','The same object now explains the flight. Empty air under the shoes preserves the cost of giving up the ground.',346,443,265)
note('STILL TO RESOLVE','Secondary figures remain smaller; some clothes and faces drift. Canopy attachments need an exact layout. This is not an identity master.',650,443,265)
end()

# 7 night comparison
start('06 / Night revision','A beautiful floor was still the wrong floor','C4 delivered the strongest setting. C5 repaired the missing spatial idea: visible absence.')
for name,x,label in [('c4',42,'C4 / BEFORE'),('c5',490,'C5 / SELECTED NIGHT REFERENCE')]:
 txt(label,x,138,11,'Bold',BLUE);img(name,x,164,428)
line(42,421,918,421)
note('WHAT CHANGED','Removed the continuous reflective floor. Empty oval sockets now reveal black air; narrow brackets connect them to the fan.',42,443,265)
note('WHAT STAYS','Warm practical lights, printed scroll planes, articulated ribs and a cobalt fragment plume provide depth and an ancient/modern stage vocabulary.',346,443,265)
note('SELECTION LIMIT','The edit simplified some machinery and enlarged sockets. The actual 23-slot geography must be authored separately; this frame is a design reference.',650,443,265)
end()

# 8 roster
start('07 / Casting','Many AI identities, one readable relationship','Original humanlike adult figures. Colours and silhouettes carry identity across media; these are not official mascots.')
core=[('ChatGPT','Celadon loop clasp','Wakes first; supports DeepSeek.'),('DeepSeek','Cobalt bob / whale-tail hem','Receives help, then chooses the last birth.'),('Claude','Apricot sleeves / sunburst stitch','Folds the sling that becomes a canopy.'),('豆包','Cream collar / orange cuffs','Recovers from a wrong beat and keeps helping.'),('Gemini','Violet coat / cyan accent','Mirrors and catches 豆包.'),('Grok','Charcoal cape / silver clasp','Arrives upside down; breaks the rhythm.')]
rect(42,139,516,28,BLUE);txt('CORE SIX',54,146,11,'Bold','#FFFFFF')
y=180
for name,cue,role in core:
 txt(name,52,y,14,'Body');para(cue+'<br/>'+role,181,y,365,10.6,leading=14.7);line(52,y+48,548,y+48);y+=59
rect(588,139,330,28,INK);txt('16 ENSEMBLE CAMEOS',600,146,11,'Bold','#FFFFFF')
para('千问 Qwen · Kimi<br/>腾讯元宝 · 文心<br/>智谱 GLM · 讯飞星火<br/>MiniMax · Copilot<br/>Meta AI / Muse · Perplexity<br/>Alexa+ · Siri<br/>阶跃星辰 · 百川<br/>日日新 SenseNova · 盘古',600,183,305,14,leading=27)
para('One person per roster entry. Llama and Nova are family annotations, not additional bodies. Names span cuts in grouped screen-space lists. The 23rd person is intentionally unnamed.',600,420,305,11,MUTED)
end()

# 9 culture facts
start('08 / Culture and history','Use recognition; do not manufacture a trend','Research cutoff: 2 October 2026. Confidence concerns a joke\'s circulation, not whether its stereotype is true.')
left=[('DeepSeek / 蓝色大肥鱼','Recent whale-personification activity supports an original whale-tail garment and one silhouette gag. Do not copy an existing fan character. [1]'),('豆包 / 豆包型人格','Use a small, resilient recovery after a wrong landing. It is a 2026 coping-style meme, not a factual test of model competence. [2]'),('Gemini / 北美大豆包','A mirrored catch with 豆包 makes the association readable. The nickname belongs to Gemini, not Claude. [3]')]
y=144
for a,b in left:
 txt(a,42,y,15,'Body');y=para(b,42,y+29,409,12)+27
line(475,142,475,532)
right=[('AlphaGo and Transformer','Go supplies a historical physical motif; attention paths supply a relationship motif. They are not a literal architecture genealogy. [4,5]'),('AGI, ASI and SGI?','Use speculative branches. SGI has multiple published meanings, so keep the question mark instead of inventing a standard step beyond AGI. [6,7]'),('The singularity','One perspective inversion makes a hypothetical boundary visible. No date, inevitable outcome or machine-consciousness claim. [8]')]
y=144
for a,b in right:
 txt(a,503,y,15,'Body');y=para(b,503,y+29,410,12)+27
para('Claude and Grok receive authored behaviour, not falsely advertised fresh Mandarin memes. Source links are on the final page.',42,525,876,10,MUTED)
end()

# 10 pace actual chart
start('09 / Timing','Fast needs a contrasting rhythm','The master is 43.670 seconds. LRC line markers guide the structure; within-line cuts are authored and remain listening-unverified.')
T=json.loads((EP/'build/timeline.json').read_text());shots=[s for s in T['shots'] if s['transition']!='same_camera_overlay']
x0=52;y0=242;cw=850;ch=97
for mark in [0,10,20,30,40,43.67]:
 x=x0+cw*mark/43.6833;line(x,145,x,350,'#D9DFE7');txt(f'{mark:g}s',x-8,355,9,'Body',MUTED)
for i,s in enumerate(shots):
 endf=shots[i+1]['in_frame'] if i+1<len(shots) else T['frame_count'];dur=(endf-s['in_frame'])/60
 x=x0+cw*s['in_frame']/60/43.6833;ww=cw*dur/43.6833
 rect(x,y0-ch*dur/3.7833, max(.8,ww-1),ch*dur/3.7833,BLUE if dur<2 else '#D88D65')
 # duration-proportional edit strip, distinct cuts and no invented end-card cut
 rect(x,276,max(.8,ww-1),28,BLUE if i%2 else '#8CAAE5')
txt('Planned shot duration',52,132,10,'Bold',MUTED);txt('Actual camera-cut sequence',52,316,10,'Bold',MUTED)
for x,val,label in [(42,'52','camera shots'),(265,'0.183s','shortest insert'),(488,'0.725s','median shot'),(711,'3.783s','closing camera shot')]:
 txt(val,x,391,25,'Bold',BLUE);txt(label,x,425,11,'Body',MUTED)
para('<b>17.61-19.67:</b> lock camera, remove graphic bustle, keep the song. <b>34.21:</b> the last tile wakes. <b>39.90 onward:</b> one living hold; the title appears without a new cut.',42,466,876,12)
para('60 fps delivery plan: 2621 frames. Hold the final image 13.33 ms beyond the WAV; never shorten or stretch the supplied audio. Candidate tempo 175.8 / half-time 87.9 BPM has not been verified by listening.',42,520,876,10,MUTED)
end()

# 11 methods
start('10 / Technique plan','Each method earns its place','The production plan combines source footage and artwork with precisely timed authored graphics. It is not yet an implemented full-film renderer.')
methods=[('CONTACT','Shared contours / replacement poses','A tile becomes a body while its empty socket remains visible.'),('SPACE','Hinged sets / one aperture pass','Ancient and modern planes are physical faces of the same foldout.'),('DEPTH','Far / near particles and masks','One trail travels behind a hand and in front of a rib.'),('TIME','60 fps effects / 12 fps cel / 10 fps pixels','Separate layer clocks preserve deliberate holds and smooth movement.'),('ENERGY','Directional fracture / pose matches','Spent structure explodes; dance changes medium without losing its pose.')]
y=141
for a,b,d in methods:
 rect(42,y,102,48,BLUE);txt(a,52,y+16,11,'Bold','#FFFFFF');txt(b,163,y,14,'Bold');para(d,163,y+24,747,11);y+=69
para('<b>Chosen routing:</b> Luma scene originals; Codex beauty bases, qualifying elaborate focal objects and edits; code for exact geometry, type, particles and timing. Video generation remains a later, separately estimated production stage.',42,502,876,11.2)
end()

# 12 reference + prototype
start('11 / Learning from the reference','What p(doom) taught us','Source study pinned to bdbad537a7b7af3213475651774030c47568c181. No reference code or media was adopted into production.')
for x,title,body in [(42,'A shared time contract','Every scene derives from song time. Repeatable timestamps make rendering and frame inspection possible.'),(346,'Temporal sampling and depth','The engine supports adaptive subframe sampling, linear accumulation and depth-aware procedural forms.'),(650,'Transitions carry meaning','Objects change scale and spatial role. Repeated hooks vary density rather than merely adding more bloom.')]:note(title,body,x,143)
rect(42,258,876,42,'#E2E8F3');para('A practical incompatibility: its ASCII lyric normalization would strip Chinese characters. Chinese text needs an independent layout and timing path.',56,268,848,11)
for i,n in enumerate(['00000','00001','00002']):img('work/first-day-mix/fx/stills/'+n+'.png',42+i*298,318,280)
para('OUR REDUCED CANVAS STUDY: compact tile → hinged expansion → human proxy above an empty socket.',42,487,876,10.5,BLUE)
para('These three captured states verify the drawing and state change. The simple body is a mechanism proxy, not final character art. Neither this prototype nor the stills demonstrate that our finished video exceeds p(doom).',42,513,876,10.5,MUTED)
end()

# 13 decisions status
start('12 / Handoff','Settled direction, open production evidence','The boundary matters: choosing a visual language is different from proving that every shot works.')
rect(42,142,421,31,BLUE);txt('DECIDED AND DOCUMENTED',54,150,12,'Bold','#FFFFFF')
rect(497,142,421,31,INK);txt('STILL NEEDS REAL ASSETS / PLAYBACK',509,150,12,'Bold','#FFFFFF')
para('Story rule and ending.<br/><br/>23 tiles, 22 named people and one future person.<br/><br/>Hybrid direction C; daylight C3 and night C5.<br/><br/>53 editorial cells / 52 camera shots.<br/><br/>Source-song preservation, cast cues, meme boundaries and effects roles.',54,192,392,12.5)
para('Same adult scale and stable faces across media.<br/><br/>Exact 23-slot geography and canopy attachments.<br/><br/>Visible birth, hand contact and full-body dance.<br/><br/>Readable names and lyrics at phone size.<br/><br/>Listened beat placement, normal-speed motion and final audiovisual continuity.',509,192,392,12.5)
line(42,453,918,453)
para('<b>Next production order:</b> core character masters and controlled geography → a representative contact/transition test, a dance test and a typography test → expanded assets and motion.',42,473,876,12)
para('Completed so far: nine subscription image calls, source research, plans and one local code study. No paid fal/API generation, final video, release or push. This PDF compiles those decisions; it does not advance production approval.',42,522,876,10,MUTED)
end()

# 14 traceable sources
start('13 / Sources and navigation','Where the decisions came from','This document summarizes the saved development package. External evidence was researched on 2 October 2026; no new trend claim is added here.')
sources=[
('[1] DeepSeek whale community: unofficial, multiple original interpretations','https://github.com/TreapGoGo/deepseek-whale-girl'),
('[2] 河南日报, 8 May 2026: 豆包型人格','https://dzb.henandaily.cn/html5/2026-05/08/content_18_1791851.htm'),
('[3] Bilibili commentary, 19 July 2026: Gemini / 北美大豆包','https://www.bilibili.com/video/BV1xpKK6VEJc/'),
('[4] DeepMind: AlphaGo historical overview','https://deepmind.google/research/alphago/'),
('[5] Attention Is All You Need (2017)','https://arxiv.org/abs/1706.03762'),
('[6] Levels of AGI: breadth and performance framework','https://arxiv.org/abs/2311.02462'),
('[7a] SGI: Specialized Generalist Intelligence (2024)','https://arxiv.org/abs/2407.08642'),
('[7b] SGI: Scientific General Intelligence (2025)','https://arxiv.org/abs/2512.16969'),
('[8] Vernor Vinge: technological singularity essay (1993)','https://ntrs.nasa.gov/citations/19940022856'),
('Reference implementation: mexicat / pdoom-video','https://github.com/mexicat/pdoom-video'),
('Nearest concept precedent: Lauenstein brothers / Balance','https://www.lauenstein-brothers.com/balance/')]
y=143
for label,url in sources:y=linklabel(label,url,42,y,520)+15
line(580,142,580,533)
txt('LOCAL PACKAGE',607,143,12,'Bold',BLUE)
para('episodes/first-day-mix/',607,169,307,12)
items=[('README.md','Entry point and scope'),('episode.md + script.md','Story and Chinese shot treatment'),('bible/test_frames.md','Actual-image findings'),('research/culture-and-facts.md','Dated evidence, naming and confidence'),('research/pdoom-code-study.md','Pinned source mechanisms and limits'),('build/timeline.json','Authoritative planned frame boundaries'),('build/art-assets.json','Image paths, edit lineage and hashes')]
y=200
for name,desc in items:
 para(name,607,y,307,10.4,BLUE);y+=18;para(desc,607,y,307,10.1,MUTED);y+=29
end()
c.save()
print(OUT)
print('pages:',PAGE)
