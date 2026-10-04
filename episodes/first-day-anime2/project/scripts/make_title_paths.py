#!/usr/bin/env python3
"""Produce actual Newsreader weight-800 outlines, never raster faux-depth.
Requires an existing fontTools installation; no downloads. Outputs title*.svg only.
"""
import argparse
import hashlib
import html
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

ROOT = Path(__file__).resolve().parents[1]

def make(font_path, output):
    source = TTFont(font_path)
    notices = {i: next((n.toUnicode() for n in source['name'].names if n.nameID == i), '') for i in (0,13,14)}
    font = instantiateVariableFont(source, {'wght': 800, 'opsz': 72}, inplace=False)
    glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
    cap = font['OS/2'].sCapHeight
    if cap <= 0:
        raise ValueError('Font does not provide positive cap height')
    output.mkdir(parents=True, exist_ok=True)
    results = []
    for suffix, text in [('left', 'OPUS 5'), ('right', '5')]:
        x, paths = 0, []
        for char in text:
            name = cmap.get(ord(char))
            if name is None:
                raise ValueError(f'Missing outline {char!r}')
            pen = SVGPathPen(glyphs)
            glyphs[name].draw(TransformPen(pen, (1,0,0,-1,x,cap)))
            d = pen.getCommands()
            if d:
                paths.append(f'<path d="{d}"/>')
            x += glyphs[name].width
        metadata = f'Source SHA256 {hashlib.sha256(font_path.read_bytes()).hexdigest()}; Newsreader variable instance wght=800 opsz=72. {notices[0]} {notices[13]} {notices[14]}'
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {x} {cap}" data-cap-height="{cap}" data-advance="{x}" data-text="{html.escape(text)}"><metadata>{html.escape(metadata)}</metadata><g fill="#FAF9F5">'+''.join(paths)+'</g></svg>\n'
        path = output / f'title-{suffix}.svg'
        path.write_text(svg)
        results.append({'path':str(path),'text':text,'advance':x,'capHeight':cap,'paths':len(paths)})
    return results

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--font',type=Path,default=ROOT/'assets/fonts/Newsreader.ttf')
    parser.add_argument('--out',type=Path,default=ROOT/'assets/brand')
    args = parser.parse_args()
    import json
    print(json.dumps(make(args.font,args.out),indent=2))
