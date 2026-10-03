"""Production timeline and asset bookkeeping, independent of image generation."""
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[3]
EP=ROOT/'episodes/first-day-anime-test'
WORK=ROOT/'work/first-day-anime-test'
def main():
    timing=json.loads((EP/'timing.json').read_text())
    times=[0,1.05,2.84,4.23,5.23,6.63,7.50,8.40,9.45,10.15,10.57,10.92,11.27,11.92,12.62,13.63,14.64,15.68,16.37,17.61,18.65,19.67,20.70,22.70,23.75,25.45,26.15,26.50,27.20,27.55,27.94,28.55,29.60,30.68,34.21]+[37.07+i*.3487 for i in range(8)]+[39.90,43.70]
    anchors={round(l['time'],2) for l in timing['lyrics']}|{11.27,11.92,30.68,37.07,39.90}
    frames=[]
    for i,t in enumerate(times):
        nearest=min(timing['onsets'],key=lambda x:abs(x-t))
        # The eighth-note montage preserves its pulse; all lyric anchors stay locked.
        if i==1: f=34
        elif t in anchors or i>=35 or t==0: f=round(t*30)
        else: f=round(nearest*30) if abs(nearest-t)<=.1 else round(t*30)
        f=max(round(t*30)-3,min(round(t*30)+3,f))
        frames.append(f)
    names=['Glasses dive','Screen fall','Waiting room','Tea exhale','You are right','Thinking spark','Levitation','Burst 1','Burst 2','Burst 3','Burst 4','Ray dive','Stop time','Title slam','Paper birth','Vertigo reveal','First breath','Window burst','Exhale pullback','Ankle landing','First steps','Reach','Hand orbit','Balcony sprint','Bullet time','Flight launch','Billboard roll','Cloud skim','Opus grin','Xiaoman joy','Vertical climb','Roll float','Hands and pupil','Helix','Paper meadow','Opus smile','Xiaoman hands','City rush','Spark sun','Ribbon storm','Danmaku wall','Hug','Whiteout','Dawn crane']
    shots=[dict(id=f'S{i+1:02}',name=names[i],target_start=times[i],start_frame=frames[i],end_frame=frames[i+1],duration=(frames[i+1]-frames[i])/30) for i in range(44)]
    assert len(shots)==44 and frames[-1]==1311 and all(b>a for a,b in zip(frames,frames[1:]))
    (EP/'build/timeline.json').write_text(json.dumps(dict(fps=30,frames=1311,shots=shots),ensure_ascii=False,indent=2)+'\n')
    print('44 shots / 1311 frames. Largest target deviation:',max(abs(s['start_frame']/30-s['target_start']) for s in shots))
if __name__=='__main__':main()
