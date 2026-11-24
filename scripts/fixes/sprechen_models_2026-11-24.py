#!/usr/bin/env python3
"""Rewrite the Sprechen Teil 2 model answers of single-topic days in the telc format
(day.html task + table, answers.html model dialogue, audio.json for sprechen_modell.mp3).
Usage: python3 scripts/fixes/sprechen_models_2026-11-24.py   (idempotent; then record audio with docs/gen_audio.py)"""
import re, json, glob, os, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from sprechen_models_content import DAYS

D = os.path.join(os.path.dirname(__file__), '..', '..', 'docs')
VOICE = {'K': 'de-DE-KatjaNeural', 'C': 'de-DE-ConradNeural'}
esc = lambda s: html.escape(s, quote=False)

def folder(d):
    g = glob.glob(os.path.join(D, d + '_*'))
    assert len(g) == 1, d
    return g[0]

def day_block(c):
    A, B = c['A'], c['B']
    rows = ''.join('<tr><td class=de>%s</td><td>%s</td></tr>' % (esc(t), esc(l)) for s, t, l in c['turns'] if s == 'K')
    return ('<h3>Teil 2 – Über ein Thema sprechen: %s</h3>'
            '<div class="txt"><b>Teil 2 (ca. 6 Min.):</b> Sie haben in einer Zeitschrift etwas zum Thema „%s“ gelesen. Das ist Ihr Text:'
            '<blockquote><i>„%s“</i><br>%s</blockquote>'
            'Ihr Partner hat eine andere Meinung gelesen. Berichten Sie über Ihren Text, sagen Sie Ihre Meinung und erzählen Sie von eigenen Erfahrungen. '
            'Sprechen Sie dann mit Ihrem Partner über das Thema.</div>'
            '<ul class="tight"><li>Bericht über Ihren Text</li><li>Meinung mit Grund</li><li>Eigene Erfahrung</li><li>Frage an den Partner und Reaktion</li></ul>'
            '<table><tr><th>Modellgespräch (Ihre Beiträge)</th><th>Erklärung</th></tr>%s</table>') % (esc(c['short']), esc(c['topic']), esc(A[1]), esc(A[0]), rows)

def answer_block(c):
    A, B = c['A'], c['B']
    dl = ''.join('<p><b>%s:</b> %s</p>' % ('Sie' if s == 'K' else 'Partner', esc(t)) for s, t, l in c['turns'])
    return ('<section><h2>Sprechen, Modellantworten</h2>'
            '<div class="txt"><b>Ihr Text (Text A):</b> „%s“ (%s)<br><b>Text Ihres Partners (Text B):</b> „%s“ (%s)</div>'
            '<div class="txt"><b>Modellgespräch zu „%s“</b>%s</div></section>') % (esc(A[1]), esc(A[0]), esc(B[1]), esc(B[0]), esc(c['topic']), dl)

for d, c in DAYS.items():
    f = folder(d)
    # day page
    p = os.path.join(f, 'day.html')
    t = open(p, encoding='utf-8').read()
    t, n = re.subn(r'<h3>Teil 2 – [^<]*</h3>.*?</table>(?=<p class="mut">1\) Bereite dich)', lambda m: day_block(c), t, count=1, flags=re.S)
    assert n == 1, (d, 'day', n)
    open(p, 'w', encoding='utf-8').write(t)
    # answers page
    p = os.path.join(f, 'answers.html')
    t = open(p, encoding='utf-8').read()
    t, n = re.subn(r'<section><h2>Sprechen, Modellantworten</h2>.*?</section>', lambda m: answer_block(c), t, count=1, flags=re.S)
    assert n == 1, (d, 'answers', n)
    open(p, 'w', encoding='utf-8').write(t)
    # audio script
    p = os.path.join(f, 'audio.json')
    a = json.load(open(p, encoding='utf-8'))
    a['sprechen_modell.mp3'] = [{'v': VOICE[s], 't': tx, 'p': 1.2, 'r': '-10%'} for s, tx, l in c['turns']]
    json.dump(a, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    words = sum(len(tx.split()) for s, tx, l in c['turns'])
    print(d, '%-45s %d turns, %d words' % (c['topic'], len(c['turns']), words))
