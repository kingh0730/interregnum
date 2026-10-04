#!/usr/bin/env python3
"""Idempotently select and normalize real sources. Run with repository .venv/bin/python.

Never writes a source image. New or changed uninspected sources keep pending features.
Annotations live in helper/features.json as source pixel coordinates and are transformed
into the normalized 16:9 crop. No substitute or placeholder imagery is generated.
"""
from __future__ import annotations
import argparse, hashlib, json, os
from pathlib import Path
from PIL import Image, ImageDraw
PROJECT=Path(__file__).resolve().parents[1]
TARGET=(1920,1080)
PURE={'S06','S08b','S09b','S10','S29','S38','S39'}
BACKGROUND={'S02','S08c','S08d','S19','S22','S34'}
EXCEPTIONS={'S02':'assets/worlds/tomorrow.png','S05':'assets/plates/S05-face.png','S09a':'assets/plates/S05-eye.png','S11':'assets/plates/S11-subject.png','S08c':'assets/plates/S08c-researchers.png','S17':'assets/plates/S17-contact.png','S18':'assets/plates/S18-opus-cutout.png','S19':'assets/plates/S19-user.png','S22':'assets/plates/S22-solo.png','S28a':'assets/plates/S27.png','S28b':'assets/plates/S28b-pose.png','S28c':'assets/plates/S28c-clean.png','S31':'assets/plates/S31-hands.png','S36c':'assets/plates/S36c-start-v2.png','S34':'assets/plates/S34-map.png','S37':'assets/plates/S37-eye-v2.png'}
LAYERS=['sky','mid','towers-left','towers-right','character']
LAYER_SOURCES={'sky':'assets/plates/S25-sky-clean.png','mid':'assets/plates/S25-mid-far.png','towers-left':'assets/plates/S25-towers-left.png','towers-right':'assets/plates/S25-towers-right.png','character':'assets/cutouts/S25-character-refined.png'}

def digest(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
 return h.hexdigest()

def crop_transform(size):
 """Exact aspect-preserving fractional source crop, consumed by Pillow resize(box=)."""
 w,h=size;tw,th=TARGET;cw,ch=(w,w*th/tw) if w/h<tw/th else (h*tw/th,h)
 left,top=(w-cw)/2,(h-ch)/2
 return {'source_size':[w,h],'crop_box':[left,top,left+cw,top+ch],'target_size':list(TARGET),'scale':tw/cw,'method':'center_crop_lanczos_preserve_alpha'}

def transform_point(point,transform):
 """Source x,y,size-pixels -> normalized u,v,size-relative-output-width."""
 x,y,size=point;l,t,r,b=transform['crop_box']
 return [round((x-l)/(r-l),8),round((y-t)/(b-t),8),round(size/(r-l),8)]

def transform_halo(halo,transform):
 if halo is None:return None
 x,y,w,h=halo;l,t,r,b=transform['crop_box']
 return [round((x-l)/(r-l),8),round((y-t)/(b-t),8),round(w/(r-l),8),round(h/(b-t),8)]

def save_json(path,value):
 path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n');os.replace(tmp,path)

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--no-previews',action='store_true');parser.parse_args()
 shots=json.loads((PROJECT/'helper/shots.json').read_text());dance_file=PROJECT/'helper/dance-production-status.json';dance=json.loads(dance_file.read_text()).get('poses',{}) if dance_file.exists() else {};feature_file=PROJECT/'helper/features.json';features=json.loads(feature_file.read_text()) if feature_file.exists() else {'schema_version':1,'assets':{}}
 previous_path=PROJECT/'helper/asset_map.json';previous=json.loads(previous_path.read_text()) if previous_path.exists() else {};old=previous.get('assets',{});assets={};missing=[];changed=[]
 def record(source,require_features=True):
  source=str(source);ident=Path(source).stem
  if ident in assets:return assets[ident]
  out=f'assets/normalized/{ident}.png';depth=f'assets/depth/{ident}.png';mask=f'assets/masks/{ident}.png'
  entry={'id':ident,'source':source,'plate':out,'depth':depth,'mask':mask if require_features else None,'expected_mask':mask,'status':'pending_source','depth_status':'pending','mask_status':'pending','features':{'status':'pending_source' if require_features else 'not_required','eyes':[],'hairpin':None,'tie':None,'halo':None},'features_required':require_features,'mask_required':require_features,'approval':False}
  path=PROJECT/source
  if not path.exists():missing.append(source);assets[ident]=entry;return entry
  try:
   source_hash=digest(path)
   with Image.open(path) as opened:
    opened.load();im=opened.convert('RGBA') if 'A' in opened.getbands() or 'transparency' in opened.info else opened.convert('RGB');transform=crop_transform(im.size)
    alpha_range=im.getchannel('A').getextrema() if im.mode=='RGBA' else None
    prev=old.get(ident,{})
    if prev.get('source_sha256')!=source_hash or prev.get('transform')!=transform or not (PROJECT/out).exists():
     normalized=im.resize(TARGET,Image.Resampling.LANCZOS,box=transform['crop_box']);(PROJECT/out).parent.mkdir(parents=True,exist_ok=True);temp=PROJECT/(out+'.tmp');normalized.save(temp,format='PNG');os.replace(temp,PROJECT/out);changed.append(ident)
   entry.update(status='normalized_source_available',source_sha256=source_hash,output_sha256=digest(PROJECT/out),transform=transform,mode=im.mode,source_alpha_range=alpha_range)
   entry['depth_status']='available_unreviewed' if (PROJECT/depth).exists() else 'pending_inference';entry['mask_status']='available_unreviewed' if (PROJECT/mask).exists() else 'pending_inference'
   if alpha_range and alpha_range[0]<255:
    with Image.open(PROJECT/out) as normalized:
     channel=normalized.getchannel('A');hist=channel.histogram();transparent_fraction=hist[0]/(TARGET[0]*TARGET[1])
     if transparent_fraction>.01:
      target_mask=PROJECT/mask;target_mask.parent.mkdir(parents=True,exist_ok=True)
      alpha_hash=hashlib.sha256(channel.tobytes()).hexdigest();prior_alpha=prev.get('mask_provenance',{}).get('alpha_sha256')
      if prior_alpha!=alpha_hash or not target_mask.exists():
       temp_mask=target_mask.with_suffix('.png.tmp');channel.save(temp_mask,format='PNG');os.replace(temp_mask,target_mask)
      depth_input=f'assets/depth-inputs/{ident}.png';entry['depth_input']=depth_input;entry['depth_preprocess']='Exact RGBA composited over ivory #FAF9F5 for inference only; original/normalized RGBA unchanged.'
      if prior_alpha!=alpha_hash or not (PROJECT/depth_input).exists() or ident in changed:
       rgb=Image.new('RGBA',TARGET,'#FAF9F5');rgb.alpha_composite(normalized.convert('RGBA'));(PROJECT/depth_input).parent.mkdir(parents=True,exist_ok=True);temp_rgb=PROJECT/(depth_input+'.tmp');rgb.convert('RGB').save(temp_rgb,format='PNG');os.replace(temp_rgb,PROJECT/depth_input)
      entry['mask_status']='exact_source_alpha';entry['mask_provenance']={'method':'normalized_source_alpha_channel','source_sha256':source_hash,'alpha_sha256':alpha_hash,'fully_transparent_pixel_fraction':transparent_fraction,'approval':False}
   if not require_features:entry['mask_status']='not_required'
   annotation=features['assets'].get(ident)
   if annotation and annotation.get('source_sha256')==source_hash:
    a=annotation['source_pixels'];f={'status':annotation.get('status','anchors_located_pending_composite_review'),'eyes':[transform_point(p,transform) for p in a.get('eyes',[])],'hairpin':transform_point(a['hairpin'],transform) if a.get('hairpin') else None,'tie':transform_point(a['tie'],transform) if a.get('tie') else None,'halo':transform_halo(a.get('halo'),transform),'eyes_state':a.get('eyes_state','open'),'review_evidence':annotation.get('review_evidence'),'halo_requires_subject_occlusion':a.get('halo') is not None,'only_character':a.get('only_character','Opus')}
    for key in ['mouth','contact','touch','tip','surface','palm','punch','heart','cloud','wrist','cross','point']:
     if a.get(key):f[key]=transform_point([*a[key][:2],0],transform)[:2]
    for key in ['iris','sun']:
     if a.get(key):f[key]=transform_point(a[key],transform)
    if a.get('reflection'):
     ref=a['reflection'];f['reflection']={'eyes':[transform_point(pt,transform) for pt in ref.get('eyes',[])],'hairpin':transform_point(ref['hairpin'],transform) if ref.get('hairpin') else None,'tie':transform_point(ref['tie'],transform) if ref.get('tie') else None}
     if ref.get('halo'):f['reflection']['halo']=transform_halo(ref['halo'],transform)
    for key in ['screenQuad','screenVisiblePolygon']:
     if a.get(key):f[key]=[transform_point([*pt,0],transform)[:2] for pt in a[key]]
    if a.get('screenVisiblePolygon'):
     screen_path=f'assets/masks/{ident}-screen.png';screen=Image.new('L',TARGET,0);ImageDraw.Draw(screen).polygon([(round(u*TARGET[0]),round(v*TARGET[1])) for u,v in f['screenVisiblePolygon']],fill=255);(PROJECT/screen_path).parent.mkdir(parents=True,exist_ok=True);
     if not (PROJECT/screen_path).exists() or Image.open(PROJECT/screen_path).tobytes()!=screen.tobytes():screen.save(PROJECT/screen_path)
     f['screenMask']=screen_path;f['screenOcclusion']='Lower-left physical screen corner is hidden behind ivory user; screenMask includes only observed visible display.'
    if a.get('screenQuadInferredCorners'):f['screenQuadInferredCorners']=a['screenQuadInferredCorners']
    entry['features']=f;annotation['normalized']=f;annotation['transform']=transform
   else:
    entry['features']['status']=('pending_visual_annotation' if require_features else 'not_required') if not annotation else 'source_changed_reannotation_required'
    if annotation:annotation['stale']=True
  except Exception as exc:entry['status']='pending_source_readable';entry['error']=str(exc);missing.append(source)
  assets[ident]=entry;return entry
 mapped={}
 for shot in shots:
  sid=shot['id'];item={'plate':None,'depth':None,'mask':None,'layers':[],'poses':[],'support':{},'features':{'status':'not_required','eyes':[],'hairpin':None,'tie':None,'halo':None},'status':'code_only' if sid in PURE else 'pending','approval':False}
  if sid=='S25':
   for layer,z in zip(LAYERS,[-4,-1,.6,.6,1.2]):
    a=record(LAYER_SOURCES[layer],layer=='character');item['layers'].append({**a,'asset_id':a['id'],'id':layer,'path':a['plate'],'z':z,'rgba':True})
   item['plate']=item['layers'][0]['path'];item['depth']=None;item['features']=item['layers'][-1]['features'];item['featureLayerId']='character';item['features']['layerId']='character'
   item['status']='layers_available' if all(a['status']=='normalized_source_available' for a in item['layers']) else 'pending_layers'
  elif sid not in PURE:
   source=dance.get(sid,{}).get('selected') or EXCEPTIONS.get(sid,f'assets/plates/{sid}-start.png' if sid.startswith('S36') else f'assets/plates/{sid}.png');a=record(source,sid not in BACKGROUND);item.update({k:a[k] for k in ['plate','depth','mask','features','status','mask_required','mask_status','depth_status']});item['asset_id']=a['id'];item['depth_input']=a.get('depth_input',a['plate'])
   if sid=='S11':
    item['support']['subject']={**a,'path':a['plate']};bg=record('assets/plates/S11-background.png',False);item['support']['background']={**bg,'path':bg['plate']}
   if sid=='S18':item['support']['hand']=record('assets/plates/S18-hand.png',False);item['support']['hand']={**item['support']['hand'],'path':item['support']['hand']['plate']}
   if sid=='S37':
    for pose in ['bust','wide']:
     a=record(f'assets/plates/S37-{pose}.png');item['support'][pose]={**a,'path':a['plate']}
   if sid=='S05':item['support']['eye']=record('assets/plates/S05-eye.png');item['support']['eye']={**item['support']['eye'],'path':item['support']['eye']['plate']}
  for support in item['support'].values():
   for key in ['tip','iris']:
    if support['features'].get(key):support[key]=support['features'][key]
  mapped[sid]=item
 map_data={'schema_version':1,'path_base':'project','target_size':list(TARGET),'shots':mapped,'assets':assets,'silhouette':'assets/cutouts/opus-silhouette.png','silhouette_provenance':'qa/silhouette-provenance.json','shell':'assets/worlds/shell.png','reflectionAtlas':'assets/mosaic/reflection-atlas.png','mosaicAtlas':'assets/mosaic/atlas.png','mosaicHero':'assets/mosaic/hero.png','special_assets':{'shell_status':'available_unreviewed' if (PROJECT/'assets/worlds/shell.png').exists() else 'pending','mosaicAtlas_status':'available_unreviewed' if (PROJECT/'assets/mosaic/atlas.png').exists() else 'pending'},'notes':['All52 shot boundaries unchanged. Missing source paths remain pending; no placeholder images.','S09a intentionally reuses the eye motif from S05-eye with a distinct4x camera move.','S28a intentionally reuses suspended S27 pose under authored stamp animation.','S36a–h use the eight authorized still-pose fallbacks; first/end clips are not claimed.','Depth/mask existence is not visual approval or proof it matches current source; renderer QA must verify.']}
 shell_path=PROJECT/'assets/worlds/shell.png'
 if shell_path.exists():
  with Image.open(shell_path) as shell:
   if 'A' in shell.getbands():
    alpha=shell.getchannel('A');hist=alpha.histogram();fraction=hist[0]/(shell.width*shell.height);map_data['special_assets']['shell_alpha']={'extrema':list(alpha.getextrema()),'fully_transparent_pixel_fraction':fraction,'source_sha256':digest(shell_path)};map_data['special_assets']['shell_status']='alpha_verified_root_reference_review' if fraction>.01 else 'alpha_rejected_not_isolated'
   else:map_data['special_assets']['shell_status']='alpha_rejected_no_channel'
 features.update(coordinate_convention={'eyes_hairpin_tie':'[u,v,size], u=x/output_width, v=y/output_height, size=symbol_diameter/output_width','halo':'[u,v,w,h], center normalized x/y, full ellipse width/output_width and height/output_height','source_pixels':'Original source-pixel anchors retained; transformed by crop_transform(). Never infer unseen image anchors.','action_points':'mouth/contact/touch/tip/surface/palm/punch/heart/cloud/wrist/cross/point are[u,v]; iris/sun are[u,v,radius/output_width]; reflection uses observed same-image coordinates.'})
 status={'status':'partial_assets_ready','shot_count':len(mapped),'selected_unique_asset_count':len(assets),'normalized_count':sum(a['status']=='normalized_source_available' for a in assets.values()),'missing_sources':missing,'written_or_updated_normalized':changed,'pending_features':[k for k,a in assets.items() if a['features_required'] and a['features']['status'] in ['pending_source','pending_visual_annotation','source_changed_reannotation_required']],'pending_depth':[k for k,a in assets.items() if a['depth_status']!='available_unreviewed'],'pending_masks':[k for k,a in assets.items() if a['mask_required'] and a['mask_status'] not in ['available_unreviewed','exact_source_alpha','not_required']],'source_files_untouched':True,'G3_approved':False,'feature_review':'Only visually inspected source images receive anchors. Overlay alignment and halo subject occlusion require composite QA.','exact_alpha_depth_inputs':{k:a['depth_input'] for k,a in assets.items() if a.get('depth_input')},'next_batch':'Await root notification before inspecting newly generated images; script may normalize existing sources without approving or annotating them.'}
 status['source_annotations_complete']=not missing and not status['pending_features']
 status['status']='sources_normalized_annotated_final_composite_QA_pending' if status['source_annotations_complete'] else 'partial_assets_ready'
 status['reflection_status']='S30 observed reflection mapped under runtime-confirmed nested schema; no synthesized halo.' if assets.get('S30',{}).get('features',{}).get('reflection') else 'pending'
 if status['source_annotations_complete']:status['next_batch']='Source annotation phase complete; run remaining real depth/mask inference and rendered composite/motion QA.'
 save_json(PROJECT/'helper/asset_map.json',map_data);save_json(feature_file,features);save_json(PROJECT/'helper/asset-selection-status.json',status)
 print(json.dumps({k:status[k] for k in ['shot_count','selected_unique_asset_count','normalized_count','written_or_updated_normalized','pending_features']},indent=2))
if __name__=='__main__':main()
