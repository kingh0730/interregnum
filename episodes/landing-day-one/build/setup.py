from pathlib import Path
import re,json
r=Path(__file__).resolve().parents[1]
p=r/'src/vendor/pdoom/gl.ts'
s=p.read_text().replace('export const W = 1920;', 'export const W = 2560;').replace('export const H = 1080;', 'export const H = 1440;');p.write_text(s)
p=r/'src/vendor/pdoom/scale.ts';s=p.read_text().replace("Math.round(Number(new URLSearchParams(location.search).get('scale') ?? '1'))", "Number(new URLSearchParams(location.search).get('scale') ?? '1')").replace('s >= 1','s >= 0.25');p.write_text(s)
rows=[('S01',0,56,1),('S02',56,112,1),('S03',112,170,1),('S04',170,222,2),('S05',222,270,2),('S06',270,314,2),('S07',314,364,3),('S08',364,424,3),('S09',424,494,3),('S10',494,556,4),('S11',556,622,4),('S12',622,676,4),('S13',676,715,4),('S14',715,757,5)]
def add(prefix,bounds,md):
 for i,(a,b) in enumerate(zip(bounds,bounds[1:])):rows.append((prefix+chr(97+i),a,b,md[i] if isinstance(md,list) else md))
add('S15',[757,768,779,790,801,811,821],5)
rows += [('S16',821,878,5),('S17',878,940,6),('S18',940,1000,6),('S19',1000,1057,6)]
add('S20',[1057,1077,1098,1118,1139,1160,1180],[3,2,7,6,9,11])
rows += [('S21',1180,1250,2),('S22',1250,1310,3),('S23',1310,1362,3),('S24',1362,1410,7)]
add('S25',[1410,1425,1440,1455,1470],7)
rows += [('S26',1470,1527,7),('S27',1527,1580,8),('S28',1580,1640,8),('S29',1640,1713,8),('S30',1713,1760,10),('S31',1760,1800,10),('S32',1800,1841,10)]
add('S33',[1841,1865,1885,1903,1919,1933,1947,1959,1971,1983,2013],[9,11,6,2,3,4,7,5,1,10])
rows += [('S34',2013,2053,5),('S35',2053,2095,10)]
add('S36',[2095,2112,2129,2145],10)
rows += [('S37',2145,2185,10),('S38',2185,2224,10),('S39',2224,2268,12),('S40',2268,2320,12),('S41',2320,2360,12),('S42',2360,2394,12),('S43',2394,2470,12),('S44',2470,2560,12),('S45',2560,2621,12)]
assert len(rows)==69 and all(x[2]==y[1] for x,y in zip(rows,rows[1:]))
(r/'assets/timeline.json').write_text(json.dumps([dict(id=i,start=a,end=b,medium=m) for i,a,b,m in rows],indent=2))
# Split full direction as exact sections for review, no creative rewrite.
s=(r/'production-plan.md').read_text()
for n,fn in [(2,'creative-direction.md'),(3,'music-and-edit.md'),(4,'cast-and-world.md'),(5,'shots.md'),(6,'assets-and-techniques.md'),(7,'execution-and-review.md')]:
 a=s.index(f'{n}. {fn}'); nxt=re.search(r'\n'+str(n+1)+r'\. [\w-]+\.md',s[a:]);end=a+nxt.start() if nxt else len(s)
 (r/fn).write_text(s[a:end])
print(f'{len(rows)} shot units; exact coverage [0,2621)')
