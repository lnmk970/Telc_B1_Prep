#!/usr/bin/env python3
"""New Hören Teil 1 (official format: moderator + five opinions, once) for 14 day pages (weeks 5-14).
Changes day.html (statements, answer key), answers.html (table + transcript) and audio.json (segments 0-7).
Usage: python3 scripts/fixes/hoeren1_days_2026-11-24.py   (idempotent; then rebuild hoeren.mp3 of these days)"""
import re, json, glob, os, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from hoeren1_days_content import DAYS
D = os.path.join(os.path.dirname(__file__), '..', '..', 'docs')
OLD = 'Hören · Teil 1: fünf kurze Texte (einmal hören)'
NEW = 'Hören · Teil 1: fünf Stellungnahmen (einmal hören)'
MUT = ('Sie hören eine kurze Einführung und dann fünf Personen, die ihre Meinung zu einem Thema sagen oder von sich erzählen. '
       'Sie hören jede Stellungnahme nur einmal. Entscheiden Sie: richtig oder falsch. Lesen Sie zuerst die Aufgaben (im Audio: 30 Sekunden).')
INSTR = ('Teil eins. Sie hören jetzt eine kurze Einführung und dann fünf Personen, die ihre Meinung zu einem Thema sagen oder von sich erzählen. '
         'Dazu lösen Sie fünf Aufgaben. Sie hören jede Stellungnahme nur einmal. Lesen Sie zuerst die Aufgaben eins bis fünf. Dafür haben Sie dreißig Sekunden.')
AM, KA, CO, KI = 'de-DE-AmalaNeural', 'de-DE-KatjaNeural', 'de-DE-ConradNeural', 'de-DE-KillianNeural'
NUM = ['eins', 'zwei', 'drei', 'vier', 'fünf']
esc = lambda s: html.escape(s, quote=False)

def voices(sp):
    f, m, out = [KA, AM], [CO, KI], []
    cf = cm = 0
    for g, *_ in sp:
        if g == 'F': out.append(f[cf % 2]); cf += 1
        else: out.append(m[cm % 2]); cm += 1
    return out

def check(n, c):
    assert len(c['sp']) == 5, n
    for g, text, st, ans, wd, we in c['sp']:
        assert ans in 'rf' and '"' not in text + st + wd + c['intro'], (n, st)
        assert ('Sprecherin' in st) if g == 'F' else ('Sprecher' in st and 'Sprecherin' not in st), (n, st)
        assert 30 <= len(text.split()) <= 80, (n, len(text.split()))

for n, c in DAYS.items():
    check(n, c)
    f = glob.glob(os.path.join(D, 'D%d_*' % n))[0]
    vs = voices(c['sp'])
    # ---- day.html
    p = os.path.join(f, 'day.html'); t = open(p, encoding='utf-8').read()
    t = t.replace(OLD, NEW)
    t, k = re.subn(r'(<h3>' + re.escape(NEW) + r'</h3>\s*)<p class="mut">[^<]*</p>', lambda m: m.group(1) + '<p class="mut">' + MUT + '</p>', t, count=1)
    assert k == 1, (n, 'mut', k)
    for i, (g, text, st, ans, wd, we) in enumerate(c['sp'], 1):
        t, k = re.subn(r'(<div class="item" id="it_hoeren_1_%d"><div class="q"><b>%d\.</b> )[^<]*(</div>)' % (i, i), lambda m: m.group(1) + esc(st) + m.group(2), t, count=1)
        assert k == 1, (n, 'item', i)
        entry = '"hoeren_1_%d": {"t": "rf", "a": "%s", "w": %s, "e": %s}' % (i, ans, json.dumps(wd, ensure_ascii=False), json.dumps(we, ensure_ascii=False))
        t, k = re.subn(r'"hoeren_1_%d": \{[^{}]*\}' % i, lambda m: entry, t, count=1)
        assert k == 1, (n, 'key', i)
    open(p, 'w', encoding='utf-8').write(t)
    # ---- answers.html
    p = os.path.join(f, 'answers.html'); a = open(p, encoding='utf-8').read()
    a = a.replace(OLD, NEW)
    rows = ''.join('<tr><td>%d</td><td class="de">%s</td><td>%s <!--EN--><br><i lang="en">%s</i><!--/EN--></td></tr>' % (
        i, 'Richtig' if s[3] == 'r' else 'Falsch', esc(s[4]), esc(s[5])) for i, s in enumerate(c['sp'], 1))
    tbl = '<table><tr><th>#</th><th>Antwort</th><th>Begründung</th></tr>%s</table>' % rows
    a, k = re.subn(r'(<h3>' + re.escape(NEW) + r'</h3>)<table>.*?</table>', lambda m: m.group(1) + tbl, a, count=1, flags=re.S)
    assert k == 1, (n, 'ans table', k)
    blk = '<div class="txt"><b>Einführung</b><br><b>Killian:</b> %s<br></div> ' % esc(c['intro'])
    for i, (s, v) in enumerate(zip(c['sp'], vs), 1):
        blk += '<div class="txt"><b>Text %d</b><br><b>%s:</b> %s<br></div> ' % (i, v[6:-6], esc(s[1]))
    a, k = re.subn(r'(<h3>Hörtext</h3>\s*)(?:<div class="txt"><b>(?:Text \d|Einführung)</b>(?:(?!</div>).)*</div>\s*){5,6}', lambda m: m.group(1) + blk, a, count=1, flags=re.S)
    assert k == 1, (n, 'transcript', k)
    open(p, 'w', encoding='utf-8').write(a)
    # ---- audio.json
    p = os.path.join(f, 'audio.json'); j = json.load(open(p, encoding='utf-8')); segs = j['hoeren.mp3']
    i2 = next(x for x, s in enumerate(segs) if re.match(r'Teil (zwei|drei)', s['t'])) if any(re.match(r'Teil (zwei|drei)', s['t']) for s in segs) else len(segs)
    seg = lambda v, tx, pp, r='+0%': {'v': v, 't': tx, 'p': pp, 'r': r}
    new = [seg(AM, INSTR, 0.5), seg(AM, '', 30), seg(KI, c['intro'], 1.5, '-8%')]
    for i, (s, v) in enumerate(zip(c['sp'], vs)):
        new += [seg(AM, 'Nummer %s.' % NUM[i], 0.4), seg(v, s[1], 7, '-8%')]
    new.append(seg(AM, 'Das ist das Ende des Teils.', 3.0))
    j['hoeren.mp3'] = new + segs[i2:]
    json.dump(j, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('D%-3d %-48s %s  (old block %d segs)' % (n, c['topic'], ''.join(s[3].upper() for s in c['sp']), i2))
