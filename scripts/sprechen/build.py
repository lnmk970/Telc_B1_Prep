# -*- coding: utf-8 -*-
"""Builds docs/Sprechen/index.html. Run: python scripts/sprechen/build.py"""
import os, sys, re, html
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'schreiben'))
from common import CSS as CSS0
from data import *
from data_extra import T2_VORTRAG, T3_EXTRA
OUT = os.path.join(HERE, '..', '..', 'docs', 'Sprechen'); os.makedirs(OUT, exist_ok=True)
e = html.escape
def mk(s):
    s = e(s, quote=False)
    s = re.sub(r'\{\{(.+?)\}\}', r'<u class="re">\1</u>', s)
    return re.sub(r'\[\[(.+?)\]\]', r'<span class="gap">\1</span>', s)
def plain(s): return re.sub(r'\{\{|\}\}', '', s)

def tmpl(T):
    rows = ''.join('<div class="tl2"><p class="de">%s</p><p class="en">%s</p></div>' % (mk(d), e(n)) for d, n in T['lines'])
    return '<div class="uni"><h3>%s <small>%s</small></h3>%s</div>' % (e(T['t']), e(T['te']), rows)
def banks(B):
    out = ''
    for t, te, items in B:
        li = ''.join('<li><span class="de">%s</span><span class="en">%s</span></li>' % (mk(d), e(n)) for d, n in items)
        out += '<details class="bk"><summary><b>%s</b><small>%s</small></summary><ul class="bl">%s</ul></details>' % (e(t), e(te), li)
    return out
def dialog(lines):
    return ''.join('<div class="turn"><span class="sp%s">%s</span><div><p class="de">%s</p><p class="en">%s</p></div></div>' % (s, s, mk(d), e(n)) for s, d, n in lines)
def tips(T): return '<div class="tips"><b>Tips</b><ul>%s</ul></div>' % ''.join('<li>%s</li>' % e(t) for t in T)

def t2sample(S, i):
    return '''<details class="lt" id="t2-%d"><summary><span class="k %s">%s</span><b>%s</b><small>%s</small><span class="wc">%d Wörter</span></summary><div class="in">
<div class="task"><b>%s</b> <small>(%s)</small><p>%s</p></div><div class="mail"><p class="de">%s</p><p class="en">%s</p></div></div></details>''' % (
        i, 'formal' if S['kind'] == 'Grafik' else 'semi', S['kind'], e(S['t']), e(S['te']), len(plain(S['de']).split()), e(S['kind']), e(S['note']), e(S['data']), mk(S['de']), e(S['en']))
def t3dialog(D, i):
    return '''<details class="lt" id="t3-%d"><summary><b>%s</b><small>%s</small></summary><div class="in"><div class="task"><b>Notiz</b><p>%s</p></div>%s</div></details>''' % (
        i, e(D['t']), e(D['te']), e(D['pts']), dialog(D['lines']))


VT = dict(t='Vorlage: Vortrag in 5 Leitpunkten', te='Template: talk in 5 steps (with partner feedback)', lines=[
 ('1 Einleitung: {{Ich möchte über das Thema}} „[[Thema]]“ {{sprechen. Zuerst erzähle ich,}} [[erster Punkt]].', 'Introduction: I would like to talk about … First I will tell …'),
 ('2 Erfahrung: {{Meine Erfahrung ist, dass}} [[Aussage]]. {{Zum Beispiel}} [[Beispiel aus deinem Alltag]].', 'Experience: My experience is that … For example …'),
 ('3 Heimatland: {{Bei uns in}} [[Land]] [[wie ist es dort?]].', 'Home country: In our country …'),
 ('4 Vor- und Nachteile: {{Ein Vorteil ist, dass}} [[…]]. {{Ein Nachteil ist, dass}} [[…]]. {{Ein Grund dafür ist, dass}} [[…]].', 'Advantages and disadvantages, with a reason.'),
 ('5 Meinung, Schluss: {{Meiner Meinung nach}} [[…]]. {{Ich finde es gut, dass}} [[…]]. {{Vielen Dank für Ihre Aufmerksamkeit. Haben Sie Fragen?}}', 'Opinion and closing.'),
 ('Partner: {{Danke für deinen Vortrag. Mir hat gefallen, dass}} [[…]]. {{Ich habe eine Frage zu}} [[Thema]]: [[Frage]]? → {{Es kommt darauf an.}} [[Antwort]].', 'Partner feedback: Thanks for your talk. I liked that … I have a question about … → It depends. …')])
def vortrag(V):
    rows = ''.join('<div class="turn"><span class="sp%s">%s</span><div><p class="meta">%s</p><p class="de">%s</p><p class="en">%s</p></div></div>' % ('B' if n == 'Partner' else 'A', str(i + 1) if n != 'Partner' else 'P', e(n), mk(d), e(en)) for i, (n, d, en) in enumerate(V['secs']))
    return '<details class="lt" id="v%d"><summary><b>Aufgabe %d: %s</b><span class="wc">%d Wörter</span></summary><div class="in">%s</div></details>' % (V['n'], V['n'], e(V['t']), len(plain(' '.join(x[1] for x in V['secs'][:5])).split()), rows)
def t3x(D):
    return '<details class="lt" id="x%d"><summary><b>Aufgabe %d: %s</b></summary><div class="in"><div class="task"><b>Situation</b><p class="de">%s</p><p class="en">%s</p><p class="tl">Leitpunkte: %s</p></div>%s</div></details>' % (D['n'], D['n'], e(D['t']), e(D['sit']), e(D['site']), e(D['pts']), dialog(D['turns']))

ov = ''.join('<div class="card"><h3>%s</h3><p class="en">%s</p><p class="flow">%s</p><p class="en">%s</p></div>' % (e(a), e(b), e(c), e(d)) for a, b, c, d in OVERVIEW)
t1 = '''<section id="teil1" class="grp formal"><h2>Teil 1: Kontaktaufnahme <small>Getting to know each other</small></h2>
<h3 class="sh">1 · Vorlage mit Lücken</h3>%s<h3 class="sh">2 · Bausteine</h3>%s
<h3 class="sh">3 · Beispielgespräch</h3><div class="task"><b>%s</b> <small>%s</small></div>%s%s</section>''' % (tmpl(T1_TEMPLATE), banks(T1_BANK), e(T1_DIALOG['t']), e(T1_DIALOG['te']), dialog(T1_DIALOG['lines']), tips(T1_TIPS))
t2 = '''<section id="teil2" class="grp informal"><h2>Teil 2: Gespräch über ein Thema <small>Talking about a topic</small></h2>
<p class="en note">Typical topics: Internetnutzung, Online-Shopping, Fernsehen, Freizeit, Gesundheit, Umwelt. Graphics: describe the numbers. Texts: report with indirect speech. Always add your own experience and ask your partner.</p>
<h3 class="sh">1 · Vorlage mit Lücken</h3>%s<h3 class="sh">2 · Bausteine</h3>%s
<h3 class="sh">3 · Beispiel-Präsentationen (6 Themen)</h3>%s%s</section>''' % (tmpl(T2_TEMPLATE), banks(T2_BANK), ''.join(t2sample(s, i) for i, s in enumerate(T2_SAMPLES)) + '<h3 class="sh">4 · Vortrag in 5 Leitpunkten (Aufgaben 7–9)</h3><p class="en">The same topic can be given as a short talk with five points and a partner who gives feedback and asks one question.</p>' + tmpl(VT) + ''.join(vortrag(v) for v in T2_VORTRAG), tips(T2_TIPS))
P = T3_PRACTICE
t3 = '''<section id="teil3" class="grp formal"><h2>Teil 3: Gemeinsam planen <small>Planning together</small></h2>
<p class="en note">Typical scenarios: Fahrradausflug, Kindergeburtstag, Abschiedsfeier, Fest nach der Prüfung, Picknick, Museumsbesuch. The same phrases work for all of them.</p>
<h3 class="sh">1 · Vorlage mit Lücken</h3>%s<h3 class="sh">2 · Bausteine</h3>%s
<h3 class="sh">3 · Beispielgespräche (4 Themen)</h3>%s
<h3 class="sh">4 · Weitere Beispielgespräche (Aufgaben 1–9)</h3>%s<h3 class="sh">5 · %s <small class="en">%s</small></h3><p class="en">%s</p><div class="mail">%s</div><p class="de"><b>Weitere Themen:</b> %s</p>%s</section>''' % (
    tmpl(T3_TEMPLATE), banks(T3_BANK), ''.join(t3dialog(d, i) for i, d in enumerate(T3_DIALOGS)), ''.join(t3x(d) for d in T3_EXTRA), e(P['t']), e(P['te']), e(P['how']), dialog(P['de']), e(' · '.join(P['topics'])), tips(T3_TIPS))

LEG = '<div class="legend"><b>Legende</b> <u class="re">unterstrichen = wiederverwendbare Wendung</u> <span class="gap">gelb = Lücke zum Ausfüllen</span> <span class="en">grün = English</span></div>'
CSS = CSS0 + '''
.legend{background:#fff;border:1px solid var(--line);border-radius:10px;padding:8px 12px;margin:10px 0;font-size:.92rem;display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center}
u.re{text-decoration:underline;text-decoration-color:#1fa971;text-decoration-thickness:2px;text-underline-offset:3px;background:#1fa97118;border-radius:2px}
.gap{background:#ffe066;border:1px dashed #b38600;border-radius:4px;padding:0 4px;font-weight:600;color:#5c4500}
.grp{margin-top:34px;padding-top:6px}.grp.formal h2{border-color:#1d4f7a}.grp.informal h2{border-color:#c96a00}.sh{margin:20px 0 6px;font-size:1.08rem}
.uni{background:#fff;border:2px solid var(--ink);border-radius:12px;padding:12px 14px}.uni h3{margin:0}.uni h3 small{font-weight:600;color:var(--mut);font-size:.8rem}
.tl2{padding:5px 0;border-top:1px solid #eee}.tl2 p{margin:.1em 0}.tl2 .de{font-size:1.04rem}
details.bk{background:#fff;border:1px solid var(--line);border-radius:10px;margin:6px 0}details.bk>summary{cursor:pointer;padding:9px 12px;list-style:none;display:flex;flex-wrap:wrap;gap:8px;align-items:baseline}
details.bk>summary::-webkit-details-marker{display:none}details.bk>summary small{color:var(--mut)}ul.bl{list-style:none;margin:0;padding:2px 12px 10px}ul.bl li{padding:5px 0;border-top:1px solid #eee}ul.bl .de{display:block;font-size:1.02rem}
.flow{font-weight:700;color:var(--blue);font-size:.9rem;margin:.2em 0}.note,.intro{background:#fff;border-left:4px solid #1fa971;padding:8px 12px;border-radius:8px}
details.lt summary .wc{margin-left:auto;color:var(--mut);font-size:.82rem}.mail .de{font-size:1.05rem}.bar a.f{background:#d9e8f5}.bar a.i{background:#ffe6c7}
.meta{color:var(--mut);font-size:.85rem;font-weight:700;margin:0}.turn{display:flex;gap:10px;padding:7px 0;border-top:1px solid #eee}.turn p{margin:.1em 0}.turn .de{font-size:1.04rem}.turn>div{flex:1}
.turn>span{flex:none;width:28px;height:28px;border-radius:50%;display:grid;place-items:center;font:800 .8rem system-ui;color:#fff;background:#1d4f7a;margin-top:3px}.turn>span.spB{background:#c96a00}.turn>span.spC{background:#0b6b4a}
'''
page = '''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sprechen-Vorlagen · telc B1</title><link rel="icon" type="image/png" href="../icon-192.png"><style>%(css)s</style></head><body>
<header><div class="wrap"><a href="../index.html">← Startseite</a><h1>Sprechen-Vorlagen</h1><p class="sub">telc B1 mündliche Prüfung: Teil 1, 2 und 3 · Vorlagen, Bausteine und Beispielgespräche mit englischer Hilfe</p></div></header>
<div class="bar"><div class="wrap"><a href="#teil1">Teil 1</a><a href="#teil2">Teil 2</a><a href="#teil3">Teil 3</a><span class="sp"></span><button id="en" type="button">Englisch: an</button><button id="op" type="button">Alle öffnen</button></div></div>
<main>%(leg)s<section><h2>Überblick <small>The oral exam</small></h2><div class="grid">%(ov)s</div></section>
%(t1)s%(t2)s%(t3)s</main>
<script>
(function(){var b=document.body,en=document.getElementById('en'),op=document.getElementById('op');
try{if(localStorage.getItem('telc_schr_noen')==='1'){b.classList.add('noen');en.textContent='Englisch: aus'}}catch(e){}
en.onclick=function(){var off=b.classList.toggle('noen');en.textContent='Englisch: '+(off?'aus':'an');try{localStorage.setItem('telc_schr_noen',off?'1':'0')}catch(e){}};
var all=false;op.onclick=function(){all=!all;document.querySelectorAll('details.lt,details.bk').forEach(function(d){d.open=all});op.textContent=all?'Alle schließen':'Alle öffnen'};
function openHash(){var h=location.hash.slice(1);var d=h&&document.getElementById(h);if(d&&d.tagName==='DETAILS'){d.open=true;d.scrollIntoView()}}
addEventListener('hashchange',openHash);openHash()})();
</script></body></html>
''' % dict(css=CSS, leg=LEG, ov=ov, t1=t1, t2=t2, t3=t3)
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(page)
print('built', len(page), 'bytes')
