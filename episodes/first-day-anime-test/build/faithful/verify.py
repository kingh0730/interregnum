"""Verify the encoded artifact and authored timings; does not approve audiovisual quality."""
from pathlib import Path
import json, hashlib, subprocess
import numpy as np
from PIL import Image, ImageDraw
ROOT=Path(__file__).resolve().parents[4]
SRC=Path(__file__).parent
WORK=ROOT/'work/first-day-anime-test/faithful'
EP=ROOT/'episodes/first-day-anime-test'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def pcm(p):
    return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-ac','1','-ar','16000','-f','f32le','-']),dtype='<f4')
def main():
    manifest=json.loads((WORK/'latest-1080.json').read_text())
    movie=ROOT/manifest['output']['path'];run=ROOT/manifest['run']
    assert sha(movie)==manifest['output']['sha256']
    assert not manifest['errors']
    for row in manifest['sources']:
        assert sha(ROOT/row['path'])==row['sha256'],row['path']
    assert sha(EP/'director-response.md')=='3fe028c324e007a12ab93bff5f69f44500b4b0e50758bb0e851728ac0dd23779'
    probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','stream=codec_name,width,height,r_frame_rate,nb_frames,duration','-of','json',str(movie)]))
    v=next(x for x in probe['streams'] if x['codec_name']=='h264')
    assert (v['width'],v['height'],v['r_frame_rate'],int(v['nb_frames']))==(1920,1080,'30/1',1311)
    subprocess.run(['ffmpeg','-v','error','-i',str(movie),'-f','null','-'],check=True)
    trace=json.loads((run/'camera-trace.json').read_text());assert len(trace)==1311
    timeline=json.loads((SRC/'timeline.json').read_text())['shots']
    assert len(timeline)==44 and timeline[-1]['end_frame']==1311
    for s in timeline:
        assert abs(s['start_frame']-round(s['target_start']*30))<=3
        assert all(x['shot']==s['id'] for x in trace[s['start_frame']:s['end_frame']])
    lyrics=json.loads((EP/'timing.json').read_text())['lyrics'];lyric_checks=[]
    for i,l in enumerate(lyrics):
        first=next(x['frame'] for x in trace if x['lyric_index']==i and x['lyric_layer_requested'] and x['lyric_alpha']>0)
        delta=first-round(l['time']*30);assert abs(delta)<=2,(i,delta)
        lyric_checks.append({'text':l['text'],'anchor_frame':round(l['time']*30),'first_requested_frame':first,'delta':delta})
    assert trace[680]['orbit_degrees']==-270 and trace[680]['focal_length_mm']==24
    assert trace[753]['orbit_degrees']==360 and trace[754]['frozen'] and not trace[755]['frozen']
    assert trace[1025]['orbit_degrees']==450 and trace[1025]['roll_degrees']==20
    assert trace[960]['halo_plane_distance']==0
    cam=trace[960]['camera'];assert np.hypot(cam[0],cam[2])<trace[960]['halo_radius']
    assert trace[1005]['spark_complete']
    assert trace[559]['camera_settle_metres']==.06
    assert trace[1068]['layers']==5 and trace[1068]['animation_fps']==12
    assert min(x['danmaku_count'] for x in trace[1163:1173])>=40
    source=pcm(EP/'first-day.mp3');encoded=pcm(movie);n=min(len(source),len(encoded));a=source[:n];b=encoded[:n]
    correlation=float(np.corrcoef(a,b)[0,1]);gain=float(np.dot(a,b)/np.dot(a,a));assert correlation>.995 and abs(gain-1)<.01
    pixels={}
    for f,target in [(358,[255,255,255]),(359,[255,255,255]),(1310,[240,238,230])]:
        raw=subprocess.check_output(['ffmpeg','-v','error','-i',str(movie),'-vf',f'select=eq(n\\,{f})','-frames:v','1','-f','rawvideo','-pix_fmt','rgb24','-'])
        im=np.frombuffer(raw,np.uint8).reshape(1080,1920,3);error=int(np.abs(im.astype(int)-target).max());assert error<=4,(f,error);pixels[str(f)]={'expected_rgb':target,'max_codec_error':error}
    sheet=Image.new('RGB',(1920,1080*2),'#141413')
    available=[int(x.stem.split('-')[1]) for x in (run/'qa').glob('frame-*.jpg')]
    for i,s in enumerate(timeline):
        mid=(s['start_frame']+s['end_frame']-1)/2;f=min(available,key=lambda f:abs(f-mid));im=Image.open(run/'qa'/f'frame-{f:04}.jpg').resize((320,180));ImageDraw.Draw(im).text((8,8),s['id'],fill='white',stroke_width=1,stroke_fill='black');sheet.paste(im,((i%6)*320,(i//6)*180))
    contact=ROOT/'renders/first-day-anime-test/first-day_opus55_faithful-contact.jpg';sheet.crop((0,0,1920,1440)).save(contact,quality=94)
    report={'master':manifest['output'],'render_run':manifest['run'],'source_sha256':manifest['source_sha256'],'authority':manifest['authority'],'probe':probe,'full_decode':'passed','browser_errors':manifest['errors'],'timeline':'44 shots; 1311 contiguous frames; all cuts within three rounded target frames','lyric_checks':lyric_checks,'camera_checks':'270°/24mm hand orbit, 360° leap orbit, 450°/20° helix, halo plane crossing at 32.00, spark complete 33.50, 6cm landing settle, five paper layers at 12fps','pixel_checks':pixels,'audio':{'source_samples':len(source),'encoded_samples':len(encoded),'sample_rate':16000,'correlation':correlation,'least_squares_gain':gain,'processing':'Original MP3 to final AAC only; no SFX, gain processing or model audio'},'limits':'Trace verifies authored values, not perceived smoothness or physical truth. Lyric request timing does not measure occlusion. Normal-speed audiovisual and sung lip-sync review remain pending.'}
    (SRC/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'decode':'passed','frames':1311,'audio_correlation':correlation,'audio_gain':gain,'source_sha256':manifest['source_sha256']}))
if __name__=='__main__':main()
