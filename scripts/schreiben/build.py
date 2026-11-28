# -*- coding: utf-8 -*-
"""Builds docs/Schreiben/index.html. Run: python scripts/schreiben/build.py"""
import os, sys, re, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import STRUCT, GRAM, CSS as CSS0
from data2 import FORMAL_EMAILS, INFORMAL_EMAILS
from data3 import UNI, BANKS, SKEL
from extras import X
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'docs', 'Schreiben')
os.makedirs(OUT, exist_ok=True)
e = html.escape
def mk(s):
    s = e(s, quote=False)
    s = re.sub(r'\{\{(.+?)\}\}', r'<u class="re">\1</u>', s)
    return re.sub(r'\[\[(.+?)\]\]', r'<span class="gap">\1</span>', s)
def plain(s): return re.sub(r'\{\{|\}\}', '', s)
PAIR = {'f-ofen': 'i-ofen', 'i-ofen': 'f-ofen', 'f-termin': 'i-absage', 'i-absage': 'f-termin'}

def email(L):
    body = [list(p) for p in L['body']]
    for i, d, en in X.get(L['id'], []):
        body[i][0] += d; body[i][1] += en
    words = len(plain(' '.join(p[0] for p in body)).split())
    formal = L['id'].startswith('f-')
    paras = ''.join('<p class="de">%s</p><p class="en">%s</p>' % (mk(d), e(n)) for d, n in body)
    pts = ''.join('<li>%s</li>' % e(p) for p in L['pts'])
    pair = ''
    if L['id'] in PAIR:
        pair = '<p class="pair">Same topic in the other register: <a href="#%s">open it</a> and compare Sie / du, greeting and tone.</p>' % PAIR[L['id']]
    return '''<details class="lt" id="%(id)s"><summary><b>%(t)s</b><small>%(te)s</small><span class="wc">%(w)d Wörter</span></summary>
<div class="in"><div class="task"><b>Aufgabe</b> <small>(%(story)s)</small><p>%(task)s</p><p class="tl">Schreiben Sie etwas zu folgenden Punkten:</p><ol>%(pts)s</ol></div>
<div class="mail"><p class="meta de">Köln, den 28.11.2026<br>%(bet)s</p><p class="meta en">Cologne, 28 Nov 2026<br>%(bete)s</p>
<p class="de sal">%(anr)s</p><p class="en">%(anre)s</p>%(paras)s<p class="de sal">%(g)s</p><p class="en">%(ge)s</p><p class="de sal">%(n)s</p></div>%(pair)s</div></details>''' % dict(
        id=L['id'], t=e(L['t']), te=e(L['te']), w=words, story=e(L['story']), task=e(L['task']), pts=pts, bet=e(L['bet']), bete=e(L['bete']),
        anr=e(L['anr']), anre=e(L['anre']), paras=paras, g=e(L['gruss']), ge=e(L['gruse']), n=e(L['name']), pair=pair)

def uni(reg):
    U = UNI[reg]
    rows = ''.join('<div class="tl2"><p class="de">%s</p><p class="en">%s</p></div>' % (mk(d), e(n)) for d, n in U['lines'])
    return '<div class="uni"><h3>%s <small>%s</small></h3><p class="en">%s</p>%s</div>' % (e(U['t']), e(U['te']), e(U['note']), rows)

def banks(reg):
    out = ''
    for t, te, items in BANKS[reg]:
        li = ''.join('<li><span class="de">%s</span><span class="en">%s</span></li>' % (mk(d), e(n)) for d, n in items)
        out += '<details class="bk"><summary><b>%s</b><small>%s</small></summary><ul class="bl">%s</ul></details>' % (e(t), e(te), li)
    return out

def skels(reg):
    out = ''
    for t, te, flow, lines in SKEL[reg]:
        li = ''.join('<li class="de">%s</li>' % mk(x) for x in lines)
        out += '<div class="card"><h3>%s</h3><p class="en">%s</p><p class="flow">%s</p><ol>%s</ol></div>' % (e(t), e(te), e(flow), li)
    return '<div class="grid">%s</div>' % out

def group(reg, emails, ident, title, sub, note):
    return '''<section id="%s" class="grp %s"><h2>%s <small>%s</small></h2><p class="en note">%s</p>
<h3 class="sh">1 · Universal-Vorlage mit Lücken</h3>%s
<h3 class="sh">2 · Bausteine zum Wiederverwenden</h3><p class="en">Tap a group to open lines you can copy into any email.</p>%s
<h3 class="sh">3 · Gerüste für verschiedene Themen</h3>%s
<h3 class="sh">4 · Beispiel-E-Mails (ca. 160–180 Wörter)</h3><p class="en">Each email is built from the lines above. Underlined parts are reusable phrases.</p>%s</section>''' % (
        ident, reg, title, sub, note, uni(reg), banks(reg), skels(reg), ''.join(email(x) for x in emails))

LEG = '<div class="legend"><b>Legende</b> <u class="re">unterstrichen = wiederverwendbare Wendung</u> <span class="gap">gelb = Lücke zum Ausfüllen</span> <span class="en">grün = English</span></div>'
INTRO = '''<p class="en intro"><b>Which topics?</b> A mix of both. Two common situations are written in both registers (broken oven: Sie to the landlord and du to a friend; cancelling or postponing: Sie to an office and du to a friend), so you see exactly what changes: Sie/Ihnen vs du/dir, Sehr geehrte… vs Liebe…, Könnten Sie… vs Kannst du…. The rest are topics that really appear in the telc exam for each register: formal = complaint, inquiry, application, cancellation, return; informal = invitation, reply, apology, thanks, planning. They match the stories in Geschichten.</p>'''
CSS = CSS0 + '''
.legend{background:#fff;border:1px solid var(--line);border-radius:10px;padding:8px 12px;margin:10px 0;font-size:.92rem;display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center}
u.re{text-decoration:underline;text-decoration-color:#1fa971;text-decoration-thickness:2px;text-underline-offset:3px;background:#1fa97118;border-radius:2px}
.gap{background:#ffe066;border:1px dashed #b38600;border-radius:4px;padding:0 4px;font-weight:600;color:#5c4500}
.grp{margin-top:34px;padding-top:6px}.grp.formal h2{border-color:#1d4f7a}.grp.informal h2{border-color:#c96a00}.sh{margin:20px 0 6px;font-size:1.08rem}
.uni{background:#fff;border:2px solid var(--ink);border-radius:12px;padding:12px 14px}.uni h3{margin:0}.uni h3 small{font-weight:600;color:var(--mut);font-size:.8rem}
.tl2{padding:5px 0;border-top:1px solid #eee}.tl2 p{margin:.1em 0}.tl2 .de{font-size:1.04rem}
details.bk{background:#fff;border:1px solid var(--line);border-radius:10px;margin:6px 0}details.bk>summary{cursor:pointer;padding:9px 12px;list-style:none;display:flex;flex-wrap:wrap;gap:8px;align-items:baseline}
details.bk>summary::-webkit-details-marker{display:none}details.bk>summary small{color:var(--mut)}ul.bl{list-style:none;margin:0;padding:2px 12px 10px}ul.bl li{padding:5px 0;border-top:1px solid #eee}ul.bl .de{display:block;font-size:1.02rem}
.flow{font-weight:700;color:var(--blue);font-size:.9rem;margin:.2em 0}.card ol{padding-left:1.2em;margin:.3em 0}.card ol li{margin:.35em 0}
.note,.intro{background:#fff;border-left:4px solid #1fa971;padding:8px 12px;border-radius:8px}.pair{font-size:.9rem;margin:10px 0 0}
details.lt summary .wc{margin-left:auto;color:var(--mut);font-size:.82rem}.mail .de{font-size:1.05rem}
.bar a.f{background:#d9e8f5}.bar a.i{background:#ffe6c7}
'''
page = '''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Schreiben-Vorlagen · telc B1</title><link rel="icon" type="image/png" href="../icon-192.png"><style>%(css)s</style></head><body>
<header><div class="wrap"><a href="../index.html">← Startseite</a><h1>Schreiben-Vorlagen</h1><p class="sub">telc B1 · Vorlagen, Bausteine und Beispiel-E-Mails, formell und informell, mit englischer Hilfe</p></div></header>
<div class="bar"><div class="wrap"><a href="#grundlagen">Grundlagen</a><a class="f" href="#formell">Formell (Sie)</a><a class="i" href="#informell">Informell (du)</a><a href="#grammatik">Grammatik</a><a href="#fehler">Fehler</a><span class="sp"></span><button id="en" type="button">Englisch: an</button><button id="op" type="button">Alle öffnen</button></div></div>
<main>%(leg)s%(intro)s
<div id="grundlagen">%(struct)s</div>
%(formal)s
%(informal)s
%(gram)s
</main>
<script>
(function(){var b=document.body,en=document.getElementById('en'),op=document.getElementById('op');
try{if(localStorage.getItem('telc_schr_noen')==='1'){b.classList.add('noen');en.textContent='Englisch: aus'}}catch(e){}
en.onclick=function(){var off=b.classList.toggle('noen');en.textContent='Englisch: '+(off?'aus':'an');try{localStorage.setItem('telc_schr_noen',off?'1':'0')}catch(e){}};
var all=false;op.onclick=function(){all=!all;document.querySelectorAll('details.lt,details.bk').forEach(function(d){d.open=all});op.textContent=all?'Alle schließen':'Alle öffnen'};
function openHash(){var h=location.hash.slice(1);var d=h&&document.getElementById(h);if(d&&d.tagName==='DETAILS'){d.open=true;d.scrollIntoView()}}
addEventListener('hashchange',openHash);openHash()})();
</script></body></html>
''' % dict(css=CSS, leg=LEG, intro=INTRO, struct=STRUCT,
           formal=group('formal', FORMAL_EMAILS, 'formell', 'Formelle E-Mails und Briefe', 'Formal (Sie)', 'Use for authorities, companies, landlords, schools, employers. Always: Sie, Betreff, Sehr geehrte…, Mit freundlichen Grüßen.'),
           informal=group('informal', INFORMAL_EMAILS, 'informell', 'Informelle E-Mails', 'Informal (du)', 'Use for friends and family. Always: du, Liebe/Lieber…, Viele Grüße. Warm and personal, but still complete sentences and all four content points.'),
           gram=GRAM)
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(page)
print('built', len(FORMAL_EMAILS), 'formal +', len(INFORMAL_EMAILS), 'informal emails,', len(page), 'bytes')
