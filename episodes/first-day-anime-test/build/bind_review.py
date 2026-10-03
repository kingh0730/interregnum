"""Bind authored, inspected conditioning-source findings to current file bytes.

This records still-source review only. It does not approve generated movement,
performance, audio sync, or the final outgoing/incoming edit states.
"""
import hashlib,json
from pathlib import Path
from graphics import ROOT,ASSET
from render import PLATES,TIMELINE
EP=ROOT/'episodes/first-day-anime-test'
BUILD=EP/'build'

# Findings from inspection of the actual plates and the complete animatic contact
# sheet, with source images viewed at full resolution during generation.
FINDINGS=[
 ('intentional_discontinuity','The glasses reflection becomes the full-frame chat feed; this is the specified optical dive, not a room cut.'),
 ('scene_change','The full-frame feed returns to the apartment: Xiaoman remains the sole person at the left desk; screen left and rainy windows behind.'),
 ('continuous','Wide room and tea insert retain Xiaoman\'s cream sleeve, round glasses, dark bob, desk-side chair and the single tea cup.'),
 ('ellipsis','Tea insert to monitor-side face: same hoodie, face and rain-lit desk. Cup lowers offscreen between setups; no second person enters.'),
 ('intentional_discontinuity','The monitor reply gives way to an authored macro of its Thinking indicator.'),
 ('scene_change','Thinking insert returns to the same selected room plate. Xiaoman remains at the left desk; levitation is an effect/action yet to be generated.'),
 ('continuous','The burst chain retains the same apartment, seated woman and props; its source is shared with the levitation setup.'),
 ('continuous','Burst 1 to Burst 2 use the same room source; the increasing spark radius is intentional graphic continuity.'),
 ('continuous','Burst 2 to Burst 3 use the same room source and increasing ring radius.'),
 ('continuous','Burst 3 to Burst 4 preserve the room source; the ring is intended to exceed the aperture.'),
 ('intentional_discontinuity','Room burst becomes the graphic ray macro, then black; no implied physical room reset.'),
 ('intentional_discontinuity','Ray/black resolves to the authored stopped-room insert. The final hold must inherit frozen outgoing levitation objects when motion exists.'),
 ('intentional_discontinuity','The stopped screen cuts to the authored title impact on locked chorus frame 358.'),
 ('intentional_discontinuity','Title to magical birth is the planned transformation. Birth source visibly retains Xiaoman left, desk left, rear windows and right balcony door.'),
 ('continuous','Birth and reveal share the same source heroine, hovering bare feet, long hair and seated Xiaoman; generated phases must remain sequential.'),
 ('continuous','Reveal to close breath retains Opus\'s face, collar brooch, hairclip and coral hair. Tight crop excludes Xiaoman\'s established desk position.'),
 ('continuous','Breath close-up returns to the same birth-room layout, with Xiaoman present at the left desk. Window rupture is a pending generated action.'),
 ('continuous','Window burst and pullback share one requested take; their final neighboring motion frames require review after generation.'),
 ('ellipsis','Room pullback to ankle insert follows Opus toward the balcony. The insert shows one bare foot and one gold 5.5 charm against wet tile and railing.'),
 ('continuous','Ankle landing to first steps retains bare feet, wet balcony tile, metal railing and long pale hair tips. The steps source was corrected to one ankle chain.'),
 ('ellipsis','Steps to reach: Opus has turned to Xiaoman at the doorway. Both women appear; same balcony rail and left interior desk, brighter dawn is the intended progression.'),
 ('continuous','The reach source shows two approaching fingertips. The orbit source is decoded frame 73 of the accepted contact take, where the two women visibly clasp hands at the same doorway. The requested orbit continues from that observed contact state.'),
 ('ellipsis','Doorway reach to sprint: both women remain together and hold hands. Their change to shoes belongs to the planned pre-flight costume state. New front camera places Opus left and Xiaoman right.'),
 ('continuous','Sprint and leap preserve Opus left/Xiaoman right, joined inner hands, Opus loafers and black socks, Xiaoman sneakers, wet tiles and metal balcony rail.'),
 ('intentional_discontinuity','Leap to flight is the planned orbit/unfreeze and shoe-dissolution transition. Flight source deliberately shows both women barefoot; change of screen side follows the orbit.'),
 ('continuous','Launch and roll share the selected flying-pair source with held hands, streaming hair and city beneath.'),
 ('continuous','Roll to cloud skim preserves the same flying pair. The city-to-cloud movement is a required action within the requested flight take, pending review.'),
 ('continuous','Cloud skim to Opus close-up is a reframing of the same selected flight take; her partner remains outside the tight crop, not removed from the source.'),
 ('continuous','Opus to Xiaoman face uses opposite tight crops of the same two-person flight source; both retain supplied identity and costume.'),
 ('continuous','Face crop to climb returns to the same flying pair and held hands; vertical climb remains a generated-action check.'),
 ('scene_change','Climb/whiteout reaches the cloud sea. Both women remain barefoot and holding hands; tall towers give way to clouds at the higher elevation.'),
 ('intentional_discontinuity','Cloud pair to contact/eye motif is a planned detail montage. The selected flying-pair source supplies sky-lit hands and Opus\'s eye; no earlier apartment plate is used here.'),
 ('intentional_discontinuity','Pupil spark opens to the helix in the cloud world. New hero source contains both barefoot women, Opus arms wide and twin tails extended.'),
 ('intentional_discontinuity','Helix to paper meadow is the explicitly scripted medium change; both women retain distinguishing hair, glasses, clothing and joined hands.'),
 ('intentional_discontinuity','Paper meadow to payoff montage is the planned return to cel anime. The close-up is the established heroine identity.'),
 ('intentional_discontinuity','Payoff montage advances from Opus to Xiaoman; these are independent celebratory inserts, not a continuous physical cut.'),
 ('intentional_discontinuity','Xiaoman payoff to city rush is the scripted strobe montage.'),
 ('intentional_discontinuity','City rush to official spark-sun is a scripted graphic payoff.'),
 ('intentional_discontinuity','Spark-sun to ribbon storm stays in the intentionally discontinuous payoff montage.'),
 ('intentional_discontinuity','Ribbon storm becomes the full-screen authored danmaku wall.'),
 ('intentional_discontinuity','Danmaku wall to embrace uses both established faces and costumes. The chosen tight crop excludes the erroneous distant sneaker in the raw hug plate.'),
 ('intentional_discontinuity','Embrace to whiteout is the specified final montage impact.'),
 ('scene_change','Whiteout opens on the meadow with both women seated, Opus\'s bare feet and one ankle chain foreground. Xiaoman sneakers were explicitly removed in the selected edit.'),
]

def binding(path):
    return {'path':str(path.relative_to(ROOT)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}

def main():
    shots=[];assets={}
    special={1:'s01-glasses',34:'helix-start',39:'sky'}
    for item in TIMELINE:
        shot=dict(item);n=int(shot['id'][1:]);name=special.get(n,PLATES.get(n))
        if name:
            shot['asset']=name;assets[name]=f'work/first-day-anime-test/assets/{name}.png'
        else:shot.update(asset='code-'+shot['id'],kind='title')
        shots.append(shot)
    assets['s20-ankle']='work/first-day-anime-test/assets/s20-ankle.png'
    # Findings belong to the inspected bytes, never just to an asset filename.
    inspected=json.loads((BUILD/'source-inspection-hashes.json').read_text())
    for path in assets.values():
        if inspected.get(path)!=hashlib.sha256((ROOT/path).read_bytes()).hexdigest():
            raise SystemExit(f'Visual re-review required for changed/unreviewed source: {path}')
    states={'S20':[{'offset_frame':0,'asset':'s20-ankle-start'},{'offset_frame':shots[19]['end_frame']-shots[19]['start_frame']-1,'asset':'s20-ankle'}]}
    for name,data in [('story-sources',{'shots':shots}),('asset-map',assets),('conditioning-states',states)]:
        (BUILD/f'{name}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    cuts=[]
    for i,(a,b) in enumerate(zip(shots,shots[1:])):
        relation,evidence=FINDINGS[i]
        cuts.append(dict(from_shot=a['id'],to_shot=b['id'],from_asset='s20-ankle' if a['id']=='S20' else a['asset'],to_asset=b['asset'],relation=relation,evidence=evidence,status='approved',issues=[]))
    review=dict(schema_version=1,status='approved',reviewer='Codex: conditioning-source visual review, 2026-10-04',review_scope='Selected still conditioning and authored intentional transitions only; generated take/cut states, performance and audio are pending.',story=binding(BUILD/'story-sources.json'),assets=binding(BUILD/'asset-map.json'),states=binding(BUILD/'conditioning-states.json'),additional_inputs=[binding(BUILD/'render.py'),binding(BUILD/'mark_plates.py')],sources=[binding(ROOT/p) for p in sorted(set(assets.values()))],cuts=cuts,state_changes=[dict(shot_id='S20',offset_frame=states['S20'][1]['offset_frame'],from_asset='s20-ankle-start',to_asset='s20-ankle',relation='continuous',status='approved',issues=[],evidence='Viewed both full-resolution ankle plates. Start has a visible air gap under all toes; endpoint touches the wet tile. Same chain, readable 5.5, railing and light. Generation must connect these states without changing anatomy.')])
    (BUILD/'continuity-review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':main()
