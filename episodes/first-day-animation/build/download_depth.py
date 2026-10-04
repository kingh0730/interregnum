from huggingface_hub import hf_hub_download
from pathlib import Path
r=Path('work/first-day-animation/models');r.mkdir(parents=True,exist_ok=True)
p=hf_hub_download('onnx-community/depth-anything-v2-small','onnx/model.onnx',local_dir=r)
print(p)
