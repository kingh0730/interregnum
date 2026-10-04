"""Create resumable depth maps for explicitly selected local plates; no image generation."""
from pathlib import Path
import sys,json,base64,subprocess
from concurrent.futures import ThreadPoolExecutor
R=Path(__file__).resolve().parents[1];repo=R.parents[1];work=repo/'work/first-day-anime1';work.mkdir(parents=True,exist_ok=True)
def run(name):
 im=R/'assets/plates'/name
 if not im.is_file():raise FileNotFoundError(im)
 target=R/'assets/depth'/im.stem
 if target.with_suffix('.png').exists():return str(target)
 inp=work/(im.stem+'-depth-payload.json');inp.write_text(json.dumps({'image_url':'data:image/png;base64,'+base64.b64encode(im.read_bytes()).decode()}))
 subprocess.run([sys.executable,str(repo/'tools/fal_run.py'),'fal-ai/image-preprocessors/depth-anything/v2',str(inp),str(target),'--resume'],check=True)
 inp.unlink();return str(target)
with ThreadPoolExecutor(max_workers=2) as pool:
 for result in pool.map(run,sys.argv[1:]):print(result)
