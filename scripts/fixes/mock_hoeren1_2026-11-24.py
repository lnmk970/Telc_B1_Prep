#!/usr/bin/env python3
"""Replace Hören Teil 1 in the 7 mock tests with the official telc format (moderator + five opinions, heard once).
Changes per mock: docs/Modelltests/mock-test-0N/index.html (statements, answer key, explanations, transcript, wording)
and audio.json (segments 0-7 = old Teil 1). The MP3 must be rebuilt afterwards with docs/gen_audio.py.
Usage: python3 scripts/fixes/mock_hoeren1_2026-11-24.py   (idempotent)"""
import re, json, os, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from mock_hoeren1_content import MOCKS, AM, KI, KA

D = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', 'Modelltests')
NUM = ['eins', 'zwei', 'drei', 'vier', 'fünf']
OLD_TIT = 'Hören · Teil 1: fünf kurze Texte (einmal hören)'
NEW_TIT = 'Hören · Teil 1: fünf Stellungnahmen (einmal hören)'
BAND = ('Sie hören eine kurze Einführung und dann fünf Personen, die ihre Meinung zu einem Thema sagen oder von sich erzählen. '
        'Sie hören jede Stellungnahme nur einmal. Entscheiden Sie: richtig oder falsch. Lesen Sie zuerst die Aufgaben (im Audio: 30 Sekunden).')
INSTR = ('Teil eins. Sie hören jetzt eine kurze Einführung und dann fünf Personen, die ihre Meinung zu einem Thema sagen oder von sich erzählen. '
         'Dazu lösen Sie fünf Aufgaben. Sie hören jede Stellungnahme nur einmal. Lesen Sie zuerst die Aufgaben eins bis fünf. Dafür haben Sie dreißig Sekunden.')
FEM = {AM, KA}

def check(n, m):
    assert len(m['sp']) == 5, n
    for i, (v, text, st, ans, why) in enumerate(m['sp'], 1):
        assert ans in 'rf', (n, i)
        assert '"' not in text + st + why + m['intro'], (n, i, 'ASCII quote')
        fem = v in FEM
        assert st.startswith('Die Sprecherin') if fem else st.startswith(('Der Sprecher', 'Dem Sprecher')), (n, i, 'gender', st)
        assert 35 <= len(text.split()) <= 80, (n, i, len(text.split()))

def patch_html(n, m):
    p = os.path.join(D, 'mock-test-%02d' % n, 'index.html')
    t = open(p, encoding='utf-8').read()
    # 1 band (title + instruction) and every other occurrence of the old title
    t, c = re.subn(r'<b>Hören · Teil 1: [^<]*</b><span>[^<]*</span>', '<b>' + NEW_TIT + '</b><span>' + BAND + '</span>', t)
    assert c == 1, ('band', n, c)
    t = t.replace(OLD_TIT, NEW_TIT)
    # 2 the five statements
    for i, (v, text, st, ans, why) in enumerate(m['sp'], 1):
        pat = r'(<div class="item" id="i-h%d"><div class="qn">%d</div><div class="qb"><p class="q">)[^<]*(</p>)' % (i, 40 + i)
        t, c = re.subn(pat, lambda mm: mm.group(1) + html.escape(st, quote=False) + mm.group(2), t)
        assert c == 1, ('item', n, i, c)
    # 3 answer key
    key = ', '.join('"h%d": "%s"' % (i, m['sp'][i - 1][3]) for i in range(1, 6))
    t, c = re.subn(r'"h1": "[rf]", "h2": "[rf]", "h3": "[rf]", "h4": "[rf]", "h5": "[rf]"', key, t)
    assert c == 1, ('key', n, c)
    # 4 explanation dictionary
    for i, (v, text, st, ans, why) in enumerate(m['sp'], 1):
        pat = (r'"h%d": \{"n": %d, "t": "rf", "q": "(?:[^"\\]|\\.)*", "why": "(?:[^"\\]|\\.)*", "tit": "%s"\}'
               % (i, 40 + i, re.escape(NEW_TIT)))
        rep = '"h%d": {"n": %d, "t": "rf", "q": %s, "why": %s, "tit": "%s"}' % (
            i, 40 + i, json.dumps(st, ensure_ascii=False), json.dumps(why, ensure_ascii=False), NEW_TIT)
        t, c = re.subn(pat, lambda mm: rep, t)
        assert c == 1, ('why', n, i, c)
    # 5 transcript ("Hörtexte zum Nachlesen")
    blk = '<h4>Hören Teil 1</h4><div class="text"><p>' + html.escape(m['intro'], quote=False) + '</p></div>'
    for i, sp in enumerate(m['sp'], 1):
        blk += '<details><summary>Text %d</summary><div class="text"><p>%s</p></div></details>' % (i, html.escape(sp[1], quote=False))
    t, c = re.subn(r'<h4>Hören Teil 1</h4>(?:<div class="text">.*?</div>)?(?:<details>.*?</details>){5}(?=<h4>Hören Teil 2)', lambda mm: blk, t, flags=re.S)
    assert c == 1, ('transcript', n, c)
    open(p, 'w', encoding='utf-8').write(t)

def patch_audio(n, m):
    p = os.path.join(D, 'mock-test-%02d' % n, 'audio.json')
    a = json.load(open(p, encoding='utf-8'))
    segs = a['hoeren.mp3']
    i2 = next(k for k, s in enumerate(segs) if s['t'].startswith('Teil zwei'))
    seg = lambda v, t, p_, r='+0%': {'v': v, 't': t, 'p': p_, 'r': r}
    new = [seg(AM, INSTR, 0.5), seg(AM, '', 30), seg(KI, m['intro'], 1.5, '-8%')]
    for i, sp in enumerate(m['sp']):
        new += [seg(AM, 'Nummer %s.' % NUM[i], 0.4), seg(sp[0], sp[1], 7, '-8%')]
    new.append(seg(AM, 'Das ist das Ende des Teils.', 3.0))
    a['hoeren.mp3'] = new + segs[i2:]
    json.dump(a, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return len(a['hoeren.mp3'])

for n, m in MOCKS.items():
    check(n, m)
    patch_html(n, m)
    k = patch_audio(n, m)
    print('mock %d: %-40s answers %s  (%d audio segments)' % (n, m['topic'], ''.join(s[3].upper() for s in m['sp']), k))
