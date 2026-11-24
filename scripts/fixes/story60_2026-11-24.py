#!/usr/bin/env python3
"""Link stories to days in the 60-day plan (docs/index.html): "Geschichte" chips per day.
Every story is used once; days 1-30 by grammar/topic, the rest on the review days. Idempotent."""
import re, json, subprocess, os
ROOT = os.path.join(os.path.dirname(__file__), '..', '..')
P = os.path.join(ROOT, 'docs', 'index.html')
M = {1:[1,7],2:[6],3:[8],4:[2],5:[3,4],6:[26,39],7:[60],8:[5,15],9:[9,12],10:[19,21],11:[20,28],12:[67,54],13:[40,50],14:[31,32],15:[61,70],
 16:[11,38],17:[25,47],18:[30,29],19:[59],20:[42],21:[37,51],22:[35,68],23:[22],24:[63],25:[36],26:[71,78],27:[34,77],28:[33,23,49],29:[73],30:[24,74],
 31:[10,13],32:[14,16],33:[52,53],34:[62,45],35:[69,64],36:[56,57],37:[58,66],38:[65,55],39:[41,43],40:[17,18],41:[72,27],42:[44,46],43:[75,76],44:[48]}
used = [s for v in M.values() for s in v]
assert len(used) == len(set(used)) == 78 and set(used) == set(range(1, 79)), (len(used), sorted(set(range(1, 79)) - set(used)))
titles = json.loads(subprocess.check_output(['node', '-e', "const fs=require('fs');const S=new Function(fs.readFileSync('docs/Geschichten/stories.js','utf8')+';return S')();console.log(JSON.stringify(Object.fromEntries(S.map(s=>[s.id,s.t.replace(/ \\(.*\\)$/,'')]))))"], cwd=ROOT))
story60 = {d: ['S%02d' % s for s in v] for d, v in M.items()}
t = open(P, encoding='utf-8').read()
data = 'const STORY60=' + json.dumps(story60) + ';const STT=' + json.dumps(titles, ensure_ascii=False) + ';'
if 'const STORY60=' in t:
    t = re.sub(r'const STORY60=.*?;const STT=\{.*?\};', lambda m: data, t, count=1, flags=re.S)
else:
    t = t.replace('const LESS=', data + '\nconst LESS=', 1)
old = ".join('')+'</span></div>'}});"
new = ".join('')+(STORY60[i+1]||[]).map(id=>'<a class=\"story\" href=\"Geschichten/index.html#'+id+'\">Geschichte '+(+id.slice(1))+' · '+STT[id]+'</a>').join('')+'</span></div>'}});"
if "STORY60[i+1]" not in t:
    assert t.count(old) == 1, t.count(old)
    t = t.replace(old, new, 1)
css = ".p60 .it a.story{border-style:dashed;background:transparent;color:var(--mut)}"
if css not in t:
    t = t.replace('@media (max-width:700px){.p60 .r{', css + '\n@media (max-width:700px){.p60 .r{', 1)
note = 'Pro Tag zusätzlich 30 Minuten: die Geschichte dazu laut lesen (gestrichelte Felder).'
if note not in t:
    t = t.replace('Dein Fortschritt gilt für beide Pläne.</p>', 'Dein Fortschritt gilt für beide Pläne. ' + note + '</p>', 1)
open(P, 'w', encoding='utf-8').write(t)
print('stories linked:', len(used), '| days with stories:', len(story60))
