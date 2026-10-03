from pathlib import Path
from fontTools.ttLib import TTFont
import json
r=Path(__file__).resolve().parents[1]
a=json.loads((r/'assets/audio-analysis.json').read_text());txt=''.join(l['text'] for l in a['lyrics'])+'落地第一天AI SI - IChatGPTClaudeGrokDeepSeek豆包Gemini通义千问文心元宝智谱星火奇点思考中好问题蓝色大肥鱼豆包型人格北美大豆包这是真的吗'
result={}
for file in ['MaShanZheng.ttf','ZCOOLKuaiLe.ttf']:
 font=TTFont(r/'assets/fonts'/file);cmap=font.getBestCmap();result[file]={'missing':sorted(set(c for c in txt if not c.isspace() and ord(c) not in cmap)),'glyphs':len(cmap)}
(r/'build/font-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False))
