"""Exact vector artwork applied to clean generated plates before motion submission.

Coordinates are measured in each 1672x941 clean source; they are not motion tracking.
"""
import json,hashlib
from graphics import ASSET,logo,text,Image

PLACEMENTS={
    'birth': {'hairpin': [903,73,32], 'brooch': [853,178,12], 'eyes': []},
    'breath': {'hairpin': [1197,101,100], 'brooch': [1065,733,46], 'eyes': [[845,319,13],[1058,232,13]]},
    'touch': {'hairpin': [1287,76,48], 'brooch': [1193,357,17], 'eyes': [[1117,199,9],[1187,157,9]]},
    'steps': {'source': 'steps-fixed-clean', 'hairpin': [676,59,25], 'brooch': [634,182,13], 'eyes': [[605,103,5],[646,96,5]]},
    'leap': {'source': 'leap-fixed-clean', 'hairpin': [581,42,24], 'brooch': [624,178,13], 'eyes': [[647,78,5],[685,94,5]]},
    'flight': {'hairpin': [1064,196,33], 'brooch': [960,347,15], 'eyes': [[928,214,7],[989,230,7]]},
    'float': {'hairpin': [918,232,25], 'brooch': [908,333,10], 'eyes': [[848,274,4],[877,261,4]]},
    'hug': {'hairpin': [919,137,53], 'brooch': [751,393,19], 'eyes': []},
    'outro': {'source': 'outro-fixed-clean', 'hairpin': [1353,130,34], 'brooch': [1202,302,18], 'eyes': [[1191,147,6],[1252,151,6]], 'charm': [736,704,9]},
    'sprint': {'hairpin':[690,60,28], 'brooch':[649,230,16], 'eyes':[[602,128,6],[661,114,6]]},
    'helix-start': {'hairpin':[992,92,28], 'brooch':[938,236,14], 'eyes':[], 'charm':[725,793,8]},
}

def main():
    records=[]
    for name,positions in PLACEMENTS.items():
        source=ASSET/(positions.get('source',name+'-clean')+'.png')
        if not source.exists():continue
        im=Image.open(source).convert('RGB');sx=im.width/1672;sy=im.height/941
        def mark(point,kind='claude-spark',color=None):
            x,y,size=point
            logo(im,(x*sx,y*sy),size*sx,name=kind,color=color)
        mark(positions['hairpin'])
        mark(positions['brooch'],'anthropic-a','#FAF9F5')
        for eye in positions['eyes']:mark(eye,color='#141413')
        if 'charm' in positions:
            x,y,size=positions['charm'];text(im,'5.5',(x*sx,y*sy),size*sx,'#765A34','latin')
        dest=ASSET/f'{name}.png';im.save(dest)
        records.append({'asset':name,'source':str(source.relative_to(ASSET.parents[2])),
                        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                        'output_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),
                        'placements':positions})
    (ASSET.parent/'mark-placements.json').write_text(json.dumps(records,indent=2)+'\n')

if __name__=='__main__':main()
