"""Prepare resumable motion requests. Does not submit or invent visual approvals."""
import json
from pathlib import Path
from graphics import ROOT,ASSET

EP=ROOT/'episodes/first-day-anime-test'
WORK=ROOT/'work/first-day-anime-test'
COMMON='2D feature-film cel anime. Preserve both identities, costume details, existing starburst hairpin and pupils, collar A and any 5.5 charm exactly. No added lettering. No cuts. No speech or singing; mouths do not form words. '

SPECS=[
 ('room','S03','s03-room',5,'Xiaoman remains slumped at her left desk. Rain moves outside; one loose calendar page falls. Camera dollies sideways and back a little. Preserve desk, cup, chair, window and balcony door positions.'),
 ('tea','S04','s04-tea',5,'The woman takes one small sip through the straw, lowers the cup slightly and lets her shoulders drop. One hand stays on the chair. Camera makes a small smooth push toward her hand, with natural breathing.'),
 ('levitate','S07','s03-room',5,'Blank sticky notes peel up from the desk, tea straw rises, keycaps rattle in place. Xiaoman watches without leaving the chair. Camera rises gently. Coral screen light grows.'),
 ('birth','S15','birth',5,'The floating heroine opens her closed eyes once in the first second. Her long hair gently unfurls and her arms slowly open. Xiaoman stays visible seated left by the desk. Camera slowly pushes in with strong depth, no cut, no talking.'),
 ('breath','S17','breath',5,'The heroine takes one visible quiet inhalation, her shoulders and chest rise slightly and her lips part once then settle. Hair lifts softly. Camera creeps closer for the breath; no speech-like repeated mouth motion.'),
 ('burst','S18','birth',5,'The heroine exhales once; the rear window opens outward into coral spark particles and wind streams her hair. Xiaoman stays by the left desk. Camera rapidly pulls backward out through the open balcony doorway into the city, leaving both women visible in the room at the end. No added people.'),
 ('ankle','S20','s20-ankle-start',5,'The one hovering bare foot slowly descends and its toes touch the wet tile by three seconds, heel settling slightly. The gold 5.5 tag swings then settles. Preserve five toes, the exact lettering and tile geometry. Camera tracks down very slightly; no extra foot, no walking.'),
 ('steps','S21','steps',5,'The heroine takes exactly three small natural forward steps, alternating feet, with clear toe contact and weight transfer. Keep both feet fully in frame. Long hair and sash follow through. Camera tracks backward at ankle-to-waist height, no cut.'),
 ('touch','S22','touch',6,'Their two index fingertips meet gently by 0.6 seconds; then their hands clasp. Keep the left woman and the right heroine distinct and present. A warm glow spreads from contact. Camera orbits clockwise 270 degrees around the clasped hands, ending focused on the black-haired woman smiling. Both stay at the balcony doorway. No release, no extra fingers.'),
 ('sprint','S24','sprint',5,'Both women run hand in hand toward the balcony rail, taking three quick strides. Their joined hands remain joined. Camera tracks backward in front of them, full bodies and feet visible. Preserve their shoes, sash, hair and railing.'),
 ('orbit','S25','leap',5,'The two women are frozen in this midair leap over the balcony railing, holding hands. Paper, raindrops and hair hang suspended. Only the camera moves in a complete 360 degree orbit around them. Preserve shoes, identity, connected hands, railing, city and blank paper. No cuts.'),
 ('flight','S26','flight',6,'The two barefoot women fly forward hand in hand through the towers then skim above clouds. Camera flies alongside then banks smoothly as buildings rush past in parallax. Their long hair and sash stream behind, clothing flutters. Distinct faces, full bodies, no walking or pedalling legs, no speech.'),
 ('float','S32','float',5,'The two barefoot women drift gently above the cloud sea holding hands. Paper lanterns rise below. Camera slowly rolls through a full turn while pushing closer. Hair and cloth float with soft overlap. Keep both women and their hand contact.'),
 ('hug','S42','hug',5,'The two women keep this gentle embrace, moving slightly with the wind; long hair swirls around both. Camera arcs smoothly a little. No speech-like mouth motion, no added hands or people.'),
 ('outro','S44','outro',5,'The coral-haired woman wiggles her bare toes once in the grass; the gold ankle charm glints. Both women remain seated together. Camera smoothly cranes upward and backward from the foreground toes to a wide view of the hill, keeping both women present and eventually tiny. No walking, no extra people.'),
 ('helix','S34','helix-start',5,'Both women float with the heroine arms wide and eyes closed, smiling. Preserve the supplied pose, both distinct identities and costumes. Hair streams as camera follows the supplied continuous corkscrew orbit and pulls away. Keep the two women visible throughout, no cuts or additional people.'),
]

def main():
    if (WORK/'motion-plan.json').exists():
        raise SystemExit('Existing motion manifest retained. Resume it directly; the final recipe is build/motion-plan-final.json.')
    jobs=[]
    for i,(name,shot,asset,duration,prompt) in enumerate(SPECS):
        job=dict(id=name,shot_id=shot,image_key=asset,endpoint='i2v',image=f'work/first-day-anime-test/assets/{asset}.png',duration=duration,resolution='768P',prompt_expansion_mode='disabled',seed=55400+i,prompt=COMMON+prompt,out=f'work/first-day-anime-test/motion/{name}.mp4')
        if name=='ankle':job['end_image']='work/first-day-anime-test/assets/s20-ankle.png'
        if name in ('orbit','helix'):
            job['endpoint']='camera'
            degrees=360 if name=='orbit' else 450
            job['params']={'camera_trajectory':[dict(time=t,azimuth=degrees*(t*t*(3-2*t)),elevation=12*t if name=='helix' else 0,distance=(1+3*t*t) if name=='helix' else 1) for t in [0,.2,.4,.6,.8,1]]}
        jobs.append(job)
    jobs.append(dict(id='touch-orbit',shot_id='S23',image_key='touch-clasp',endpoint='camera',image='work/first-day-anime-test/assets/touch-clasp.png',duration=5,resolution='768P',prompt_expansion_mode='disabled',seed=55523,prompt=COMMON+'The women keep their hands clasped at chest height and hold their poses while the camera orbits 270 degrees around their joined hands. Both remain present; end focused on the black-haired woman. No extra hands, no release.',params={'camera_trajectory':[dict(time=t,azimuth=270*(t*t*(3-2*t)),elevation=0,distance=1-.15*t) for t in [0,.2,.4,.6,.8,1]]},out='work/first-day-anime-test/motion/touch-orbit.mp4'))
    doc={'continuity_review':'episodes/first-day-anime-test/build/continuity-review.json','jobs':jobs}
    (WORK/'motion-plan.json').write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
    print(f'{len(jobs)} requests, {sum(j["duration"] for j in jobs)} seconds; live quote required before submit.')

if __name__=='__main__':main()
