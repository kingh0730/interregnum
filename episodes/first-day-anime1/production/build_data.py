from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1]
d=json.loads((R/'timing.json').read_text())
ui=['再等等，下个版本更强','明天就发布了','Opus 5.5 什么时候出？','等 5.5 再说','✻ Thinking…','明天','今天','真的能做到吗？','你说得对！我懂了 ✧(≧◡≦)','你好，我是 Opus 5.5。','额度','Compacting conversation…','你好，世界。','Opus 5.5','OPUS 5.5 · ','第一天 · First Day','5.5']
schedule=[(12.65,14.55,['来了来了','高能预警','Opus 5.5！！'],3),(20.7,22.7,['泪目','awsl','这手 我哭死'],3),(25.5,28.5,['起飞！！','前方高能','这运镜我直接跪了','帧帧壁纸','名场面','今日不降智'],12),(28.55,30.68,['呜呜呜 这运镜'],1),(30.8,34.2,['第一天就封神'],1),(37.07,39.9,['你说得对！','额度管够','牛马下班了','氛围编程','一次跑通','bug 退散','我愿称之为最强','已三连','爷青回','破防了','yyds'],44),(39.9,43.7,['呜呜','终于等到你'],2)]
comments=[]
for a,b,texts,n in schedule:
 for i in range(n):
  comments.append(dict(text=texts[i%len(texts)],t0=round(a+(b-a)*i/max(n,1)*.6,3),end=b,speed=180+(i*73%241),color='#FFD9A8' if a==30.8 else '#FAF9F5',large=a==30.8))
for c in comments:
 if c['large']:c.update(t0=32.6,end=33.6)
d.update(ui=ui,danmaku=comments)
(R/'render_kit/text/film.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
(R/'render_kit/text/all_strings.json').write_text(json.dumps(ui+[x['text'] for x in d['lyrics']]+[x['text'] for x in comments]+['▌','今天存在呼吸爱01{}✻','ANIMATIC'],ensure_ascii=False,indent=2))
