"""ASR screening of non-dialogue sources; outputs probabilistic evidence, not listening claims."""
import json,math
from pathlib import Path
import mlx_whisper
w=Path('work/ep01/audio');p=w/'source_asr.json';out=json.loads(p.read_text()) if p.exists() else {}
for f in sorted(list((w/'sfx').glob('*.mp3'))+list((w/'music').glob('*.mp3'))):
 k=str(f)
 if k in out:continue
 res=mlx_whisper.transcribe(k,path_or_hf_repo='mlx-community/whisper-small-mlx',language='en',verbose=False)
 out[k]={'text':res['text'].strip(),'segments':[{a:s.get(a) for a in ['start','end','text','avg_logprob','no_speech_prob']} for s in res['segments']]}
 for seg in out[k]['segments']:
  for a,v in list(seg.items()):
   if isinstance(v,float) and not math.isfinite(v):seg[a]=None
 out[k]['confident_lexical_speech']=any(s.get('avg_logprob') is not None and s['avg_logprob']>-1.2 and any(c.isalpha() for c in s['text']) for s in out[k]['segments'])
 p.write_text(json.dumps(out,indent=2,allow_nan=False));print(k,out[k]['text'],flush=True)
