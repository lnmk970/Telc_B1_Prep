#!/usr/bin/env python3
"""Fill the missing English example sentences in docs/Wortschatz/data.js and add the still-uncovered words to the stories.
Usage: python3 scripts/fixes/translations_apply_2026-11-24.py && node scripts/fixes/place_vocab_2026-11-24.js"""
import re, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from translations_part1 import T1
from translations_part2 import T2
from translations_part3 import T3
from translations_part4 import T4
T = {**T1, **T2, **T3, **T4}
P = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', 'Wortschatz', 'data.js')
src = open(P, encoding='utf-8').read()
V = json.loads(src[len('const V='):-1])
missing = [i for i, v in enumerate(V) if v[6] and not v[7]]
extra = sorted(set(T) - set(missing)); lack = sorted(set(missing) - set(T))
assert not extra and not lack, ('not in list', extra[:5], 'no translation', lack[:10])
for i in missing:
    assert T[i].strip() and '"' not in T[i], i
    V[i][7] = T[i]
open(P, 'w', encoding='utf-8').write('const V=' + json.dumps(V, ensure_ascii=False, separators=(',', ':')) + ';')
print('translated', len(missing), 'example sentences')
