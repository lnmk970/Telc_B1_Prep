#!/usr/bin/env python3
"""Rewrite the complete speaking models (Teil 1+2+3) of the six full-exam days in the telc format.
Usage: python3 scripts/fixes/sprechen_full_2026-11-24.py   (idempotent; then record audio with docs/gen_audio.py)"""
import re, json, glob, os, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from sprechen_full_content import DAYS
D = os.path.join(os.path.dirname(__file__), '..', '..', 'docs')
VOICE = {'K': 'de-DE-KatjaNeural', 'C': 'de-DE-ConradNeural'}
esc = lambda s: html.escape(s, quote=False)

def table(c):
    part, rows = '', ''
    for turn in c['turns']:
        if turn[0] == 'H':
            part = turn[1].split(' – ')[0]
        elif turn[0] == 'K':
            rows += '<tr><td class=de>%s</td><td>%s: %s</td></tr>' % (esc(turn[1]), part, esc(turn[2]))
    return '<table><tr><th>Modellgespräch (Ihre Beiträge)</th><th>Erklärung</th></tr>%s</table>' % rows

def answers(c):
    A, B = c['A'], c['B']
    body = ''
    for turn in c['turns']:
        if turn[0] == 'H': body += '<p><b>%s</b></p>' % esc(turn[1])
        else: body += '<p><b>%s:</b> %s</p>' % ('Sie' if turn[0] == 'K' else 'Partner', esc(turn[1]))
    return ('<section><h2>Sprechen, Modellantworten</h2>'
            '<div class="txt"><b>Teil 2, Ihr Text (Text A):</b> „%s“ (%s)<br><b>Text Ihres Partners (Text B):</b> „%s“ (%s)</div>'
            '<div class="txt">%s</div></section>') % (esc(A[1]), esc(A[0]), esc(B[1]), esc(B[0]), body)

for d, c in DAYS.items():
    f = glob.glob(os.path.join(D, d + '_*'))[0]
    p = os.path.join(f, 'day.html'); t = open(p, encoding='utf-8').read()
    # learner's opinion text inside the Teil 2 line of the task
    quote = '<blockquote><i>„%s“</i><br>%s</blockquote>' % (esc(c['A'][1]), esc(c['A'][0]))
    m = re.search(r'(<b>Teil 2[^<]*</b>(?:(?!<br><b>Teil 3).)*?)(<br><b>Teil 3)', t, flags=re.S)
    assert m, (d, 'teil2')
    if '<blockquote>' not in m.group(1):
        t = t[:m.end(1)] + quote + t[m.start(2):]
    t, n = re.subn(r'<table><tr><th>(?:Redemittel|Modellgespräch[^<]*)</th>.*?</table>(?=<p class="mut">1\) Bereite dich)', lambda mm: table(c), t, count=1, flags=re.S)
    assert n == 1, (d, 'table', n)
    open(p, 'w', encoding='utf-8').write(t)
    p = os.path.join(f, 'answers.html'); t = open(p, encoding='utf-8').read()
    t, n = re.subn(r'<section><h2>Sprechen, Modellantworten</h2>.*?</section>', lambda mm: answers(c), t, count=1, flags=re.S)
    assert n == 1, (d, 'answers', n)
    open(p, 'w', encoding='utf-8').write(t)
    p = os.path.join(f, 'audio.json'); a = json.load(open(p, encoding='utf-8'))
    a['sprechen_modell.mp3'] = [{'v': VOICE[x[0]], 't': x[1], 'p': 1.2, 'r': '-10%'} for x in c['turns'] if x[0] != 'H']
    json.dump(a, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(d, c['topic'], sum(1 for x in c['turns'] if x[0] != 'H'), 'turns,', sum(len(x[1].split()) for x in c['turns'] if x[0] != 'H'), 'words')
