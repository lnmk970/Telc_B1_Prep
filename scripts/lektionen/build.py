#!/usr/bin/env python3
"""Build docs/Lektionen/N1..N9.html and index.html from content.py.
Usage: python3 scripts/lektionen/build.py
Progress is stored in localStorage key telc_L-<id> as {res:{uebungen:{n,t}},ts} (read by the 60-day plan)."""
import os, json, html, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import L

OUT = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', 'Lektionen')
os.makedirs(OUT, exist_ok=True)

CSS = r'''
:root{--ink:#14262b;--petrol:#0e5a5a;--petrol2:#0a4444;--paper:#f2f4f3;--white:#fff;--gelb:#ffd400;--line:#d5dcda;--mut:#55656a;--ok:#12784a;--okbg:#e6f4ec;--bad:#b3312a;--badbg:#fbeceb;--tip:#fff7cf;--box:#e3eeec}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--ink:#e6eeec;--petrol:#5cc0b8;--petrol2:#7fd3cc;--paper:#111a1c;--white:#1a2629;--line:#2f3f43;--mut:#9fb4b6;--ok:#5fd39a;--okbg:#16382a;--bad:#ff8a80;--badbg:#3a1d1b;--tip:#3a3418;--box:#1d3234}}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.6 "Segoe UI",system-ui,-apple-system,Roboto,sans-serif}
a{color:var(--petrol)}header{background:#14262b;color:#fff;border-bottom:8px solid var(--gelb)}
.hd{max-width:820px;margin:0 auto;padding:28px 16px 22px}.hd a{color:#cfe5e2;font-size:.9rem}
h1{margin:8px 0 4px;font:600 clamp(1.6rem,4vw,2.3rem)/1.15 "Bahnschrift","Segoe UI",sans-serif}
.sub{color:#9fb4b6;margin:0}main{max-width:820px;margin:0 auto;padding:10px 16px 80px}
h2{font:600 1.5rem/1.2 "Bahnschrift","Segoe UI",sans-serif;margin:34px 0 10px}h3{font:600 1.15rem/1.3 "Bahnschrift","Segoe UI",sans-serif;margin:26px 0 6px}
.goal{background:var(--white);border-left:8px solid var(--gelb);padding:16px 18px;margin:20px 0}
.lang{display:flex;gap:6px;flex-wrap:wrap;margin:14px 0}.lang button{border:1px solid var(--petrol);background:var(--white);color:var(--petrol);padding:6px 12px;border-radius:6px;font:inherit;cursor:pointer}.lang button.on{background:var(--petrol);color:#fff}
body[data-l=de] .en,body[data-l=en] .de{display:none}.en{color:var(--mut)}.en p,.en li{font-size:.95rem}
.scroll{overflow-x:auto}table{border-collapse:collapse;margin:12px 0;width:100%;background:var(--white);font-size:.95rem}
th,td{border-bottom:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}th{color:var(--mut);border-bottom:2px solid var(--ink);font-weight:600}
.tip{background:var(--tip);border-left:4px solid var(--gelb);padding:10px 14px}
.say{font:inherit;font-size:.92rem;border:1px solid var(--line);background:var(--white);color:var(--ink);border-radius:4px;padding:2px 8px;margin:2px 2px;cursor:pointer}.say:hover{border-color:var(--petrol)}
.item{padding:14px 12px;border-bottom:1px solid var(--line)}.item .q{margin-bottom:8px}.item .q b.n{color:var(--petrol);margin-right:6px}
.opts{display:flex;flex-direction:column;gap:6px}.opts label{display:flex;gap:10px;align-items:center;padding:8px 12px;border:1.5px solid var(--line);background:var(--white);border-radius:4px;cursor:pointer}
.opts label:has(input:checked){border-color:var(--petrol);background:var(--box)}
.item.ok{background:var(--okbg)}.item.bad{background:var(--badbg)}.fb{display:none;margin-top:8px;font-size:.93rem}.item.ok .fb,.item.bad .fb{display:block}
.act{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:18px 0}
button.b{font:600 1rem "Bahnschrift","Segoe UI",sans-serif;background:var(--petrol);color:#fff;border:0;border-radius:4px;padding:10px 20px;cursor:pointer}button.b.s{background:transparent;color:var(--ink);box-shadow:inset 0 0 0 1.5px var(--line)}
.score{font-weight:600}.good{color:var(--ok)}.low{color:var(--bad)}
.list a{display:flex;justify-content:space-between;gap:12px;padding:14px 12px;border-bottom:1px solid var(--line);text-decoration:none;color:var(--ink);background:var(--white)}.list a:hover{background:var(--box)}
.pill{font-size:.85rem;padding:2px 8px;border-radius:10px;border:1px solid var(--line);white-space:nowrap}.pill.pass{background:var(--okbg);border-color:var(--ok)}.pill.fail{background:var(--badbg);border-color:var(--bad)}
.nav{display:flex;justify-content:space-between;margin-top:40px;padding-top:16px;border-top:2px solid var(--ink)}
@media (max-width:600px){body{font-size:16px}td,th{padding:6px 7px}}
'''

JS = r'''
(function(){
const K='telc_L-'+LID;
function setL(l){document.body.dataset.l=l;document.querySelectorAll('.lang button').forEach(b=>b.classList.toggle('on',b.dataset.l===l));try{localStorage.setItem('telc_lang',l)}catch(e){}}
let l0='both';try{l0=localStorage.getItem('telc_lang')||'both'}catch(e){}if(!/^(both|de|en)$/.test(l0))l0='both';
document.querySelectorAll('.lang button').forEach(b=>b.onclick=()=>setL(b.dataset.l));setL(l0);
let voice=null;function pick(){const v=(window.speechSynthesis&&speechSynthesis.getVoices())||[];voice=v.find(x=>/^de(-|_)DE/i.test(x.lang))||v.find(x=>/^de/i.test(x.lang))||null}
if(window.speechSynthesis){pick();speechSynthesis.onvoiceschanged=pick}
document.addEventListener('click',e=>{const b=e.target.closest('.say');if(!b)return;
  if(!window.speechSynthesis){alert('Dein Browser kann keine Wörter vorlesen.');return}
  speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(b.dataset.t);u.lang='de-DE';u.rate=.85;if(voice)u.voice=voice;speechSynthesis.speak(u)});
const box=document.getElementById('ex');
box.innerHTML=Q.map((q,i)=>'<div class="item" id="q'+i+'"><div class="q"><b class="n">'+(i+1)+'.</b>'+q[0]+'</div><div class="opts">'+q[1].map((o,j)=>'<label><input type="radio" name="r'+i+'" value="'+j+'"> '+String.fromCharCode(97+j)+') '+o+'</label>').join('')+'</div><div class="fb"><span class="de"></span><span class="en"></span></div></div>').join('');
function check(save){let n=0,t=Q.length;Q.forEach((q,i)=>{const it=document.getElementById('q'+i),s=it.querySelector('input:checked');
  it.classList.remove('ok','bad');if(!s)return;const ok=+s.value===q[2];if(ok)n++;it.classList.add(ok?'ok':'bad');
  it.querySelector('.fb .de').innerHTML=(ok?'Richtig. ':'Richtig ist <b>'+String.fromCharCode(97+q[2])+'</b>. ')+q[3];
  it.querySelector('.fb .en').innerHTML=' '+q[4]});
  const sc=document.getElementById('score');const p=Math.round(100*n/t);sc.textContent=n+' von '+t+' richtig ('+p+' %)';sc.className='score '+(p>=60?'good':'low');
  if(save){try{const st={res:{uebungen:{n:n,t:t}},ans:Q.map((q,i)=>{const s=document.querySelector('input[name=r'+i+']:checked');return s?+s.value:null}),ts:Date.now()};localStorage.setItem(K,JSON.stringify(st))}catch(e){}}}
document.getElementById('chk').onclick=()=>check(true);
document.getElementById('rst').onclick=()=>{if(!confirm('Antworten dieser Lektion löschen?'))return;try{localStorage.removeItem(K)}catch(e){}location.reload()};
try{const st=JSON.parse(localStorage.getItem(K)||'null');if(st&&st.ans){st.ans.forEach((a,i)=>{if(a!==null){const r=document.querySelector('input[name=r'+i+'][value="'+a+'"]');if(r)r.checked=true}});check(false)}}catch(e){}
})();
'''

def page(les, prev, nxt):
    secs = ''
    for h, he, d, e in les['sec']:
        secs += '<h2><span class="de">%s</span><span class="en">%s</span></h2><div class="de">%s</div><div class="en">%s</div>' % (h, he, d, e)
    q = [[x[0], x[1], x[2], x[3], x[4]] for x in les['ex']]
    nav = '<div class="nav"><span>%s</span><a href="index.html">Alle Zusatzlektionen</a><span>%s</span></div>' % (
        ('<a href="%s.html">← %s</a>' % (prev['id'], prev['id'])) if prev else '',
        ('<a href="%s.html">%s →</a>' % (nxt['id'], nxt['id'])) if nxt else '')
    return '''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(id)s · %(t)s</title><link rel="icon" type="image/png" href="../icon-192.png"><link rel="stylesheet" href="lektion.css"></head>
<body data-l="both"><header><div class="hd"><a href="../index.html">← Übersicht</a> · <a href="index.html">Zusatzlektionen</a>
<h1>%(id)s · %(t)s</h1><p class="sub">%(te)s · Prüfungsteil: %(where)s</p></div></header><main>
<div class="lang" role="group" aria-label="Sprache"><button data-l="both">Deutsch + English</button><button data-l="de">Nur Deutsch</button><button data-l="en">English only</button></div>
<div class="goal"><b class="de">Ziel: </b><span class="de">%(goal)s</span><b class="en">Goal: </b><span class="en">%(goalen)s</span></div>
%(secs)s
<h2><span class="de">Übungen</span><span class="en">Exercises</span></h2><p class="de">Wähle a, b oder c und drücke „Prüfen“. Ab 60 %% gilt die Lektion im 60-Tage-Plan als bestanden.</p><p class="en">Choose a, b or c and press “Prüfen” (check). 60 %% or more counts as passed in the 60-day plan.</p>
<div id="ex"></div><div class="act"><button class="b" id="chk" type="button">Prüfen</button><button class="b s" id="rst" type="button">Zurücksetzen</button><span id="score" class="score"></span></div>
%(nav)s</main>
<script>const LID=%(lid)s;const Q=%(q)s;</script><script src="lektion.js"></script></body></html>
''' % dict(id=les['id'], t=les['t'], te=les['te'], where=les['where'], goal=les['goal'], goalen=les['goalen'], secs=secs, nav=nav,
           lid=json.dumps(les['id']), q=json.dumps(q, ensure_ascii=False))

for i, les in enumerate(L):
    open(os.path.join(OUT, les['id'] + '.html'), 'w', encoding='utf-8').write(page(les, L[i-1] if i else None, L[i+1] if i+1 < len(L) else None))
open(os.path.join(OUT, 'lektion.css'), 'w', encoding='utf-8').write(CSS)
open(os.path.join(OUT, 'lektion.js'), 'w', encoding='utf-8').write(JS)

items = ''.join('<a href="%s.html"><span><b>%s · %s</b><br><small>%s</small></span><span class="pill" data-id="%s">offen</span></a>' % (x['id'], x['id'], x['t'], html.escape(x['where']), x['id']) for x in L)
idx = '''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Zusatzlektionen</title><link rel="icon" type="image/png" href="../icon-192.png"><link rel="stylesheet" href="lektion.css"></head>
<body><header><div class="hd"><a href="../index.html">← Übersicht</a><h1>Zusatzlektionen</h1><p class="sub">Neun B1-Themen, die im Tagesplan keine eigene Lektion hatten. Im 60-Tage-Plan sind sie in Phase 1 eingeplant.</p></div></header>
<main><div class="list">%s</div></main>
<script>document.querySelectorAll('.pill[data-id]').forEach(p=>{try{const st=JSON.parse(localStorage.getItem('telc_L-'+p.dataset.id)||'null');const r=st&&st.res&&st.res.uebungen;if(r&&r.t){const v=Math.round(100*r.n/r.t);p.textContent=v+' %%';p.className='pill '+(v>=60?'pass':'fail')}}catch(e){}})</script></body></html>
''' % items
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(idx)
print('built', len(L), 'lessons into', os.path.abspath(OUT))
