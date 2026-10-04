from pathlib import Path
import sys,json,base64,subprocess
from concurrent.futures import ThreadPoolExecutor
R=Path(__file__).resolve().parents[1];repo=R.parents[1];work=repo/'work/first-day-anime1'
def run(name):
 im=R/'assets/plates'/name;target=R/'assets/mattes'/im.stem
 if target.with_suffix('.png').exists():return str(target)
 inp=work/(im.stem+'-matte-payload.json');inp.write_text(json.dumps({'image_url':'data:image/png;base64,'+base64.b64encode(im.read_bytes()).decode(),'model':'General Use (Heavy)','operating_resolution':'2048x2048','output_mask':True,'refine_foreground':False,'output_format':'png'}))
 subprocess.run([sys.executable,str(repo/'tools/fal_run.py'),'fal-ai/birefnet',str(inp),str(target),'--resume'],check=True);inp.unlink();return str(target)
with ThreadPoolExecutor(max_workers=2)as p:
 for result in p.map(run,sys.argv[1:]):print(result)
