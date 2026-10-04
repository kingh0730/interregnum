#!/usr/bin/env python3
"""Fallback generator for the Claude-style spark (coral 12-ray starburst). PREFER the official SVG from
Anthropic's brand/press assets if reachable; use this when it is not. Output: spark.svg (transparent, #D97757).
usage: python make_spark_svg.py [--color #D97757] [--out spark.svg]"""
import math, argparse
ap = argparse.ArgumentParser(); ap.add_argument('--color', default='#D97757'); ap.add_argument('--out', default='spark.svg'); a = ap.parse_args()
# 12 rays, deliberately uneven lengths (hand-cut feel), angles slightly irregular
L = [1.00, .78, .92, .70, .96, .74, 1.00, .80, .90, .72, .95, .76]
J = [0, 4, -3, 5, -2, 3, 0, -4, 3, -5, 2, -3]
R = 100; cx = cy = 110; w = 17
p = []
for i, (l, j) in enumerate(zip(L, J)):
    ang = math.radians(i * 30 + j - 90)
    x, y = cx + math.cos(ang) * R * l, cy + math.sin(ang) * R * l
    p.append(f'<line x1="{cx}" y1="{cy}" x2="{x:.2f}" y2="{y:.2f}" stroke="{a.color}" stroke-width="{w}" stroke-linecap="round"/>')
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 220">{"".join(p)}<circle cx="{cx}" cy="{cy}" r="19" fill="{a.color}"/></svg>'
open(a.out, 'w').write(svg); print('wrote', a.out)
