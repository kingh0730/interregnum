"""Prepare the episode-only motion handoff and silence-padded audio. NO network or video generation.
Uses final approved assets.json paths when available; canonical paths are bootstrap placeholders only.
"""
import hashlib,json,math,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];E=ROOT/'episodes/ep01';W=ROOT/'work/ep01';B=E/'build'
story=json.loads((B/'story.json').read_text());lipdata=json.loads((W/'audio/lipsync_manifest.json').read_text());lips={x['shot_id']:x for x in lipdata};prices=json.loads((W/'prices.json').read_text())
assets_path=B/'assets.json';assets=json.loads(assets_path.read_text()) if assets_path.exists() else {}
def source_image(key):
 value=assets.get(key,f'work/ep01/keys/{key}.png')
 return value.get('path') if isinstance(value,dict) else value
rates={alias:float(prices[ep]['prices'][0]['unit_price']) for alias,ep in [('i2v','minimax/h3-max/image-to-video'),('lipsync','minimax/h3-max/lip-sync/image-to-video')]}
common=' Preserve the supplied identities, clothes, materials, object counts and room geometry. Maintain the full original frame and a locked camera with no reframing. Mouths remain closed. Keep the two doorways and their different destinations fixed wherever visible. Retain existing object markings. No new lettering or objects. Natural small movements only.'
silent={
 '01':('D','Eda withdraws her fingertips a few centimetres from the single blue-edged slip already beside her folded houseletter, then her hands rest. Sen stays beside the one marked blue bowl containing one cherry. The left doorway continues to show the packed old room without a planetary ring.'),
 '23':('D','Use the already stopped result pose. Both adults remain beside the floor-standing compact kitchen units and regard the clear full-size rear worktop. Their hands stay down and the placed tray, lid and bowl stay fixed. Hold the uninterrupted tableau with ordinary subtle breathing for ten seconds.'),
 '30':('C','Eda takes one ordinary onward step into the visible safe hall route, carrying the same secured folded houseletter and cloth roll, then settles. Keep her complete body and both feet visible. She continues to face onward and keeps the carried objects in the same hands.'),
 '31':('D','Hold this vast postal-hall composition. A very slight natural daylight change moves across the distant masonry. All piers, supported apartment sections, rails and visible physical structures remain rigid and in their original locations.'),
 '32':('C','The cloth roll is already on Eda\'s private cutting table. Eda straightens one nearby cloth edge a few centimetres, once, then leaves her hands at the table. Keep the real private-room floor and the distant red ring beyond the window unchanged.'),
 '33':('C','Only Sen changes location: one small step from the right entrance toward his clear right hob while holding the same pan. He settles before reaching any cloth. Eda stays at her left-hand paper pattern. Keep every textile on the left or centre counter and the right hob clear.'),
 '39':('D','The final arrangement is already complete: the spare cup weights Eda\'s pattern, the salt stays by Sen, and the marked blue bowl is on his clear preparation surface. Eda slides a hand a few centimetres along her paper edge; Sen makes one small working-hand adjustment beside his pan. They attend to their separate tasks throughout. No shared look or change of position.'),
}
# Dialogue endpoints have no behaviour prompt. Essential changed states are separate approved plates or paper edits.
state_notes={
 '03':'k03 already shows the new room beyond the fixed threshold. Keep Eda planted for the line; k04 separately supplies her reached-hand result. No traversal or room morph is demanded from lip sync.',
 '05':'Complaint reads from the empty-bowl context and her existing gaze; no required hand movement.',
 '06':'Keep the existing screen-left/down eyeline. A doorway glance is optional only if actually present and usable.',
 '07':'The line establishes divorce. Existing table pose is sufficient; do not require a bowl move or emotional reaction.',
 '09':'The existing table/plan context carries the bicycle-fit exchange. No required finger relocation.',
 '10':'Keep the existing down/right eyeline; no emphatic reaction or large gesture is needed.',
 '11':'The empty table location plus the line carries the missing-measure joke. A pat is optional, not guaranteed by the endpoint. Do not claim it occurred from its sound alone.',
 '12':'Remain in the established speaking pose. The returned measure is a separate completed-state insert k08; no doorway walk is required here.',
 '14':'Use Eda with the already visible order/module arrangement. Do not require simultaneous slip placement.',
 '15':'k10 already shows the pan resting safely on the compact hob. Sen holds the completed fit state during his question; keep the pan on the hob. The following k11 insert reveals the missing resting space without another placement.',
 '17':'k12 already holds the wet tray offered inward over the small basin, while the pan remains on the compact hob. Hold this pose throughout the request. No timed tray handoff, outward reach or pan movement is required.',
 '18':'k13 already establishes occupied hands. Keep all objects in those hands throughout.',
 '20':'Reuse the occupied-hands state from k13. Keep all props fixed; only the short supplied utterance belongs here.',
 '21':"k28 is a distinct approved result: tray already down, small spill present, and Eda's hand resting on the module. Keep those contacts. No lowering, pointing or spill simulation is required from lip sync.",
 '24':'The clear counter was established by k16. Existing gaze and voice make the proposal; no mechanical discovery.',
 '25':'The line states the use cost. Keep the existing table pose; no required palm placement.',
 '26':"k31 is the reviewed result with the pan already raised in both of Sen's hands. Keep both hands supporting the same pan. No lift is required, and neutral empty-hands k06 cannot replace this plate.",
 '27':'Existing attention to the worktop suffices; a measured gaze sweep is optional, never asserted without evidence.',
 '28':"k17 already shows the full-height floor carton CLOSED and taped, with Sen's hands resting on top. Hold that contact during his line. No open flap, fold, closing action or shrinking module is required. Packing sounds refer to off-screen completion, not a visible closure in this plate.",
 '34':"k23 already shows the pan on the main hob with Sen's hand on its handle. Keep that completed arrangement during his vegetable line. No pointing, carrying or pan placement is required; the following chair insert proves the bowl's relocation.",
 '35':'k24 already establishes Eda and the cloth/pattern. Existing eyeline and the later chair insert carry the indication; no pointing action is promised.',
 '37':'k29 is the separate result with the bowl retrieved to the cooking surface. No retrieval animation is required.',
 '38':'k30 already shows the salt pot weighting the RIGHT pattern corner, Eda indicating the opposite LEFT corner, and the spare cup still behind. Hold these exact contacts during her request. k26 separately completes the exchange with the cup weighting the pattern and salt by Sen; no handover is required here.',
}
held={'04':'Exact one-bowl/one-cherry missed-handover result. Hold the approved material insert; no object duplication or a reach invented by audio.',
      '13':'Tape measure is already back on the table. Deliberate result insert with a contact at the cut.',
      '16':'Pan already sits safely on the miniature hob; the missing preparation space is the visible fact.',
      '19':'Updated k14 is the narrow remaining strip beside the pan and Eda\'s indicating hand only. Off-screen Eda audio; no drawer, device or visible speaker.',
      '22':'Hold the completed water trail reaching the empty bowl; the folded cream rag lies beside the water. Sen stays off screen. No cloth touch-down, wiping hand or leak defect is required.',
      '36':'Marked bowl already sits on the chair. The following k29 is a separate retrieved-bowl result. Do not pretend the held image performed the lift.'}
bench=['m07','m23','m30'];jobs=[];triage=[];audio_derivatives=[]
for sh in story['shots']:
 sid=sh['id'];dur=(sh['end_frame']-sh['start_frame'])/24;category=None
 row={'shot_id':sid,'image_key':sh['asset'],'edit_frames':[sh['start_frame'],sh['end_frame']],'edit_seconds':dur,'input_state':sh['action'],'essential_story_check':sh['critical_action'],'source_shot_document':f'episodes/ep01/shots/{sid}/shot.md','motion_generated':False,'actual_action_onset':None,'actual_action_completion':None,'full_take_review':'not generated','final_cut_review':'not generated'}
 if sid in lips and lips[sid]['use_for_lipsync']:
  ln=lips[sid];source=ROOT/ln['path'];audio=source;request_dur=max(5,math.ceil(dur))
  if dur<5:
   out=W/'audio/motion_inputs'/f'shot_{sid}_{ln["speaker"]}_5s.wav';out.parent.mkdir(parents=True,exist_ok=True)
   subprocess.run(['ffmpeg','-v','error','-y','-i',str(source),'-af',f'atrim=end={dur},asetpts=PTS-STARTPTS,apad=whole_dur=5','-t','5','-ar','48000','-ac','2','-c:a','pcm_s24le',str(out)],check=True)
   audio=out;audio_derivatives.append({'shot_id':sid,'source':ln['path'],'derived':str(out.relative_to(ROOT)),'source_duration':dur,'output_duration':5,'transformation':'Exact original isolated shot audio, bounded first; silence-only tail appended. Keep source[0:shot duration] in final edit.','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'derived_sha256':hashlib.sha256(out.read_bytes()).hexdigest()})
  job={'id':'m'+sid,'endpoint':'lipsync','image':source_image(sh['asset']),'image_key':sh['asset'],'audio':str(audio.relative_to(ROOT)),'input_audio_source':ln['path'],'duration':request_dur,'params':{'enable_transcription':False},'out':f'work/ep01/motion/m{sid}.mp4','deps':[],'category':'B','shot_id':sid,'line_id':ln['line_id'],'speaker':ln['speaker'],'source_edit':[0,dur],'final_edit_frames':sh['end_frame']-sh['start_frame'],'planned_takes':1,'benchmark':('m'+sid) in bench,'behaviour_constraint':state_notes[sid],'submission_status':'NOT SUBMITTED; stage7 is outside current authorization'}
  row.update(method='lipsync',category='B',job_id=job['id'],action_policy=state_notes[sid],audio_is_on_screen=True,request_seconds=request_dur,estimated_first_take_usd=round(request_dur*rates['lipsync'],3));jobs.append(job)
 elif sid in silent:
  cat,action=silent[sid];request_dur=max(5,math.ceil(dur));prompt=action+common
  job={'id':'m'+sid,'endpoint':'i2v','image':source_image(sh['asset']),'image_key':sh['asset'],'prompt':prompt,'duration':request_dur,'out':f'work/ep01/motion/m{sid}.mp4','deps':[],'category':cat,'shot_id':sid,'source_edit':[0,dur],'final_edit_frames':sh['end_frame']-sh['start_frame'],'planned_takes':1,'benchmark':('m'+sid) in bench,'action_qa':{'required_visible_result':action,'source_onset_seconds':None,'source_completion_seconds':None,'full_take_verified':False,'final_cut_verified':False},'submission_status':'NOT SUBMITTED; stage7 is outside current authorization'}
  row.update(method='i2v',category=cat,job_id=job['id'],action_policy=action,request_seconds=request_dur,estimated_first_take_usd=round(request_dur*rates['i2v'],3));jobs.append(job)
 elif sh['kind']=='graphic':
  row.update(method='authored_state_edit',category='CONTROLLED',job_id=None,action_policy='Retain exact paper layers and state switch from build/paper_states.json. No video-generation request and no generated lettering.',audio_is_on_screen=False,estimated_first_take_usd=0)
 elif sh['kind']=='title':row.update(method='authored_typography',category='CONTROLLED',job_id=None,action_policy='Exact vector/raster typography in post; no motion-model request.',estimated_first_take_usd=0)
 else:
  assert sid in held,sid;row.update(method='held_result_insert',category='CONTROLLED',job_id=None,action_policy=held[sid],audio_is_on_screen=False,estimated_first_take_usd=0)
 triage.append(row)
first=sum(x['duration']*rates[x['endpoint']] for x in jobs);test=sum(x['duration']*rates[x['endpoint']] for x in jobs if x['benchmark'])
plan={'defaults':{'resolution':'768P','prompt_expansion_mode':'disabled'},'stage':'PREPARED ONLY; no video requests authorized or submitted','repository_root_required':True,'runner':'tools/video/h3_batch.py','fps':24,'planned_edit_frames':story['total_frames'],'benchmark_ids':bench,'input_assets_map':'episodes/ep01/build/assets.json','source_audio_manifest':'work/ep01/audio/lipsync_manifest.json','audio_submission_derivatives':audio_derivatives,'price_source':'work/ep01/prices.json','price_observed_date':'2026-10-02','rates_usd_per_second':rates,'budget':{'lipsync_jobs':23,'lipsync_billable_seconds':sum(x['duration'] for x in jobs if x['endpoint']=='lipsync'),'i2v_jobs':len(silent),'i2v_billable_seconds':sum(x['duration'] for x in jobs if x['endpoint']=='i2v'),'first_three_tests_usd':round(test,2),'all_pass_first_takes_usd':round(first,2),'retake_reserve_cap_usd':4.0,'proposed_maximum_usd':round(first+4,2),'test_cost_included_in_first_pass':True,'paid_motion_spend_so_far_usd':0,'authorization':'Stage7 not authorized; estimate is a proposed future envelope, not permission to spend.'},'endpoint_constraints':{'lipsync':'Image + supplied audio only, >=5 seconds. No prompt, end frame, or separately requested duration is sent by the runner. params.enable_transcription=false follows audio directly. duration is planning metadata; actual audio controls output and billing.','i2v':'Integer5–15seconds,768P,prompt_expansion_mode disabled. No target_audio_url: current docs describe soundtrack replacement, not demonstrated action+lip-sync.','short_audio':'Shots17,18,20 use5s silence-padded submission derivatives. Other20 dialogue jobs use the exact original shot-padded isolated WAV.','retakes':'Explicit per-job only; review accepted test takes before the remaining27jobs. Never automatically resubmit an unresolved request.','returned_media':'Discard all returned model audio. Probe decoded video duration/frame count; use planned source[0:shot duration] only after actual action and sync review.'},'jobs':jobs}
(B/'motion_plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2))
(B/'motion_triage.json').write_text(json.dumps({'stage':'Prepared only; all motion evidence remains pending','shot_count':40,'submitted_job_count':0,'planned_generation_jobs':len(jobs),'authored_or_held_shots':len(triage)-len(jobs),'benchmarks':bench,'critical_state_transitions':[{'before':'k01','after':'k03','mechanism':'Authored address-tab switch in shot02 followed by exact doorway result cut; never morph room geometry.'},{'before':'k12','after':'k28','mechanism':'Separate held-tray and tray-down/spill plates, shots17 and21; no uncontrolled lowering action required.'},{'before':'k06','after':'k31','mechanism':'Shot26 uses distinct raised-pan plate; neutral reused pose is insufficient.'},{'before':'k25','after':'k29','mechanism':'Bowl-on-chair insert then separately approved retrieved-bowl result; no invented lift.'},{'before':'k30','after':'k26','mechanism':'Salt weights pattern in request state; spare cup weights it and salt is by Sen in final state. Outcome changes across a cut, not an asserted lip-sync handoff.'}], 'shots':triage},ensure_ascii=False,indent=2))
(W/'audio/motion_inputs/manifest.json').write_text(json.dumps(audio_derivatives,indent=2));print(json.dumps(plan['budget'],indent=2));print('Prepared',len(jobs),'jobs; no video submitted.')
