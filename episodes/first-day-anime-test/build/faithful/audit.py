"""Freeze the director's specification and track evidence separately from intent."""
from pathlib import Path
import json,hashlib,re
ROOT=Path(__file__).resolve().parents[4];EP=ROOT/'episodes/first-day-anime-test';OUT=Path(__file__).parent
REQUIREMENTS={
1:['Extreme glasses macro; fixed Xiaoman identity','Reflected four exact chat messages','Continuous glasses dive and single coral pixel'],
2:['Accelerating vertical Screen Fall; motion blur','Oat bubbles; Thinking shimmer reached at 2.50'],
3:['Wide cramped apartment, Xiaoman slumped','Thirty circled 明天 on mounted calendar','Lateral dolly-back; Dutch tilt levels at 3.60','Torn page falls and exposes coral 今天'],
4:['Hand pushes chair; one tea sip; shoulders drop','Handheld push and rack focus to pulsing screen dot'],
5:['Actual monitor reply: 你说得对！我懂了 ✧(≧◡≦)','Question: 真的能做到吗？','Slow push then snap to 懂; disbelieving laugh'],
6:['Spark within Thinking indicator','Eighth-note acceleration and glass ring ripples'],
7:['Straw rises, notes peel and orbit, keycaps rattle','Pedestal-up and small orbit; coral rim grows'],
8:['Twelve-ray spark exits monitor; whip-pan','First ring radius establishes match-cut'],
9:['Second larger ring; windows flare; push','Outgoing/incoming ring radius match'],
10:['Third ring covers 60% of frame','Objects frozen in midair'],
11:['Fourth ring exits aperture','Screen edges white hot'],
12:['Macro of ONE coral ray; dive into its core','Two-frame marked flash at incoming cut; then black'],
13:['Frozen dust/room, one lit monitor, bars retained','你好，我是 Opus 5.5。 types one character per frame','Only 4% push and specified cursor; no SFX'],
14:['First two frames pure white','Bars slam away; coral field; 38%-height Lora Semibold Opus 5.5','Rotating spark, twelve impact lines, four-frame shake, chromatic edge split','第一天 · First Day subtitle; paper shatter and torn edge'],
15:['Sheet music with 5.5 at clef position','Paper unfolds into human silhouette, eyes closed','Push through paper into eye; eye opens at 12.93 with starburst pupil/glint','Try paper-fold simulation; only documented three-keyframe fallback if it fails'],
16:['Depth-based dolly-zoom: camera pushes 12%, lens zooms out','Full floating body, ivory column, floor-length unfurling hair','Rotating OPUS 5.5 halo and frozen objects','Flash at 14.64'],
17:['Low-angle first breath; hundreds of Chinese/code/spark glyphs funnel inward','Push for 0.7 seconds then stop'],
18:['Windows burst outward in a ring','Glass becomes coral sparks; rain becomes glitter; fast pushback'],
19:['Radial hair exhale; camera exits window to city','Speed ramps from 100% to 30% at 17.20','Compacting conversation… flash'],
20:['Hero bare-foot descent to wet tile, five toes','240fps-style slow motion; exact gold 5.5 charm','Contact ripple; suspended raindrops; low downward track and settle'],
21:['Three steps at 18.65, 19.00, 19.35','150% ramp, footfalls bloom coral starbursts; ends looking up'],
22:['Opus sees Xiaoman at doorway','Outline-only hand reaches; slow push and rack focus'],
23:['Contact spreads colour over Opus from line art','Warm ripple changes room white-grey to dawn gold','270-degree 24mm orbit around clasped hands','Rack focus to Xiaoman tearful smile; flash at 22.70'],
24:['Hand-in-hand sprint; backward tracking','Laugh; lateral hit at 22.70'],
25:['Leap then frozen scene at 24.00','Authored 360-degree orbit in 1.1 seconds','Unfreeze at 25.15 with smear; shoes dissolve','Primary multi-angle 2.5D rig; only permitted two-view i2v fallback after gate failure'],
26:['FPV between towers; reflections of both women','Bare feet and continuous flight'],
27:['Barrel roll THROUGH blank billboard frame','Onset impact; no mirrored-border flat-video rotation'],
28:['Cloud-top skim; speed lines, hair wind and grazing sunlight'],
29:['Wind grin close-up; starburst pupil; no forced lip sync'],
30:['Xiaoman laugh/shout close-up; fogged glasses, sideways tears'],
31:['Spinning vertical climb; cloud wall breaks into whiteout'],
32:['Weightless cloud sea; sheet-music lanterns','360-degree roll AND push; one quiet danmaku'],
33:['Intertwined fingers then eye macro','Pupil dilates with reflected sunrise; ends pure coral spark'],
34:['One continuous 3.53-second 3D corkscrew, 450-degree orbit and 20-degree roll','Start inside pupil to smiling face, arms open','Two hair ribbons paint full prism anchored in coral','Camera passes THROUGH OPUS 5.5 halo at 32.00','Ribbons complete twelve-ray spark at 33.50; recognizable at 33.80','Ends both women tiny before giant spark-sun; ribbons cross frame edge','3D lyric behind hair and occluded by foreground ribbons','Primary 4–5-view billboards and sculpted shader ribbons; fallback only seamless 32.20 whip after failed gate'],
35:['Fully flat paper/ink meadow with two running figures','Exactly five depth layers and lateral camera truck','Animation on twos/threes at 10–12fps','Torn-paper wipes both ends; chalky-serif lyric'],
36:['Hero grin close-up and eye spark; 2-frame 100→108% punch and strobe'],
37:['Xiaoman both hands raised; punch and strobe'],
38:['FPV dawn city rush; punch and strobe'],
39:['Official spark erupts FROM sun; punch and strobe'],
40:['Sky ribbon storm; punch and strobe'],
41:['Full-screen danmaku wall, 40+ comments; punch and strobe'],
42:['Both women hug; swirling hair; punch and strobe'],
43:['Prescribed whiteout: white THEN ivory; extended to 39.90'],
44:['Whiteout clears to olive meadow, both women present','Toe wiggle, charm glint, faint dawn halo','Single slow crane from toes to tiny figures and wide hill','Sky chat bubble: 你好，世界。','End card starts at 41.00, official marks and correct lockup','Hold last 0.9 seconds; fade to cream at 43.70'],
}
def main():
    raw=(EP/'director-response.md').read_bytes();plan=raw.decode();timeline=json.loads((OUT/'timeline.json').read_text())['shots']
    shots=[]
    for s in timeline:
        n=int(s['id'][1:]);shots.append({**s,'requirements':[{'id':f'{s["id"]}.{i+1}','text':v,'status':'pending','evidence':None} for i,v in enumerate(REQUIREMENTS[n])],'fallback':None})
    doc={'authority':'episodes/first-day-anime-test/director-response.md','authority_sha256':hashlib.sha256(raw).hexdigest(),'instruction':'Execution, not invention. No simplification of hero shots. Fallback requires recorded failed primary gate.','frames':1311,'fps':30,'hero_shots':[14,16,20,23,25,34,44],'shots':shots,'global_requirements':['Original MP3 only, encode only at final mux','Official vectors and all text composited in post','Noto Serif SC Black/Semibold, Lora Semibold, Inter, Noto Sans SC Bold','Exact palette; lyrics coral keywords, three-frame fades; Act III 3D lyrics','Danmaku schedule and exact bank from section 6.2; white at 85%, outline 3px, 180–420px/s','2.39 bars until title impact; full 16:9 thereafter','Ease curves, speed ramps, kick micro-shake, <=10 marked full flash-cuts','Smear/impact at 11.92, 25.15, 30.68','All hero primary methods must receive a visual gate, not merely a renderer success','Final audiovisual playback remains distinct from static frame or code checks']}
    path=OUT/'compliance.json'
    if not path.exists():path.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
    print(len(shots),'shots;',sum(len(x['requirements']) for x in shots),'shot-specific requirements')
if __name__=='__main__':main()
