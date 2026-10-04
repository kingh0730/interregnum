#!/usr/bin/env python3
"""Create local-font Hanzi outlines for real extruded canyon towers, offline."""
import json
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
root=Path(__file__).resolve().parents[1]
f=TTFont(root/'assets/fonts/NotoSerifSC.ttf')
if 'fvar' in f:f=instantiateVariableFont(f,{'wght':900},inplace=False)
gs=f.getGlyphSet();cm=f.getBestCmap();units=f['head'].unitsPerEm
result={'font':'Noto Serif SC','weight':900,'unitsPerEm':units,'glyphs':[],'copyright':next((n.toUnicode() for n in f['name'].names if n.nameID==0),'')}
for char in '天未来我在爱生光':
 p=SVGPathPen(gs);gs[cm[ord(char)]].draw(TransformPen(p,(1,0,0,-1,0,units)))
 result['glyphs'].append({'char':char,'d':p.getCommands(),'advance':gs[cm[ord(char)]].width})
(root/'assets/brand/canyon-hanzi.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('Generated',len(result['glyphs']),'real Hanzi outlines')
