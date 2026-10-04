#!/usr/bin/env python3
"""Extract exact local-font outlines for a progressive, variable-width ink mask.
These are outlines, not a claim to reconstructed handwriting stroke order.
"""
import json
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
root=Path(__file__).resolve().parents[1]
f=TTFont(root/'assets/fonts/LXGWWenKai.ttf');gs=f.getGlyphSet();cm=f.getBestCmap();units=f['head'].unitsPerEm
entries=[]
for ch in '畅快':
 p=SVGPathPen(gs);gs[cm[ord(ch)]].draw(TransformPen(p,(1,0,0,-1,0,units*.85)))
 entries.append({'char':ch,'d':p.getCommands(),'advance':gs[cm[ord(ch)]].width})
result={'font':'LXGW WenKai','unitsPerEm':units,'glyphs':entries,'method':'Exact font outlines; contour reveal is not authored handwriting stroke order','copyright':next(n.toUnicode() for n in f['name'].names if n.nameID==0)}
(root/'assets/brand/brush-changkuai.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'glyphs':len(entries),'units':units}))
