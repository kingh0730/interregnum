"""Check post-edit isolated utterances for dropped words; report phonetic apostrophe ambiguity separately."""
import difflib,json,re
from pathlib import Path
import mlx_whisper
w=Path('work/ep01/audio');sel=json.loads((w/'dialogue/selection.json').read_text());manifest=json.loads((w/'lipsync_manifest.json').read_text());p=w/'final_dialogue_asr.json';out={}
def words(t):return re.sub(r"[^a-z ]",' ',t.lower().replace("'",'')).split()
for ln in manifest:
 res=mlx_whisper.transcribe(ln['path'],path_or_hf_repo='mlx-community/whisper-small-mlx',language='en',verbose=False)
 tr=res['text'].strip();ref=sel[ln['line_id']]['text'];match=difflib.SequenceMatcher(None,words(ref),words(tr)).ratio()
 out[ln['line_id']]={'text':ref,'post_edit_transcript':tr,'apostrophe_insensitive_match':round(match,3)};p.write_text(json.dumps(out,indent=2));print(ln['line_id'],round(match,3),tr,flush=True)
