// Builds docs/Tag60/T01.html ... T60.html (one page per day of the 60-day plan) from the data in docs/index.html.
// Also links "Tag N" in the plan to its page and adds the pages to the offline list. Safe to re-run.
const fs=require('fs'),path=require('path');
const root=path.join(__dirname,'..','..','docs');
let idx=fs.readFileSync(path.join(root,'index.html'),'utf8');
const get=(re)=>{const m=idx.match(re);if(!m)throw new Error('not found '+re);return m[1]};
const PLAN60=eval(get(/const PLAN60=(\[\[.*?\]\]);/s));
const STORY60=eval('('+get(/const STORY60=(\{.*?\});/s)+')');
const STT=eval('('+get(/const STT=(\{.*?\});/s)+')');
const LESS=eval('('+get(/const LESS=(\{.*?\});/s)+')');
const DAYS=eval(get(/const DAYS=(\[.*?\]);\n/s));
const PH=[[0,30,'Phase 1 · Lernen'],[30,45,'Phase 2 · Wiederholen und verbessern'],[45,60,'Phase 3 · Probeprüfungen']];
const css=fs.readFileSync(path.join(root,'D05_2026-11-16_Mon_W1-Praesens','day.html'),'utf8').match(/<style>([\s\S]*?)<\/style>/)[1].split('\n').slice(0,6).join('\n');
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
const pad=n=>String(n).padStart(2,'0');
function item(x){
  if(x.startsWith('L:'))return{k:'Neue Lektion',t:LESS[x.slice(2)],h:'../Lektionen/'+x.slice(2)+'.html',d:'Lektion mit Übungen'};
  if(x.startsWith('M:')){const n=+x.slice(2);return{k:'Modelltest',t:'Modelltest '+n,h:'../Modelltests/mock-test-0'+n+'/',d:'Komplette Probeprüfung: Lesen, Sprachbausteine, Hören, Schreiben. Zeit stoppen.'}}
  if(x.startsWith('X:'))return{k:'Fehlertag',t:'Fehlerheft durchgehen',h:'../index.html#g-ueberblick',d:'Schwache Teile aus den Lösungen wiederholen, Schreibvorlagen und Sprechen-Gerüst auswendig lernen.'};
  const d=DAYS.find(y=>y.id===x);return{k:'Lektionstag',t:d.title,h:'../'+d.folder+'/day.html',d:d.focus,a:'../'+d.folder+'/answers.html'}}
fs.mkdirSync(path.join(root,'Tag60'),{recursive:true});
const tpl=(n,body)=>{const ph=PH.find(([a,b])=>n-1>=a&&n-1<b)[2];
const prev=n>1?`<a href="T${pad(n-1)}.html">← Tag ${n-1}</a>`:'<a href="../index.html#plan">← Übersicht</a>';
const next=n<60?`<a href="T${pad(n+1)}.html">Tag ${n+1} →</a>`:'<a href="../index.html#plan">Übersicht →</a>';
const opts=Array.from({length:60},(_,i)=>`<option value="T${pad(i+1)}.html"${i+1===n?' selected':''}>Tag ${i+1}</option>`).join('');
return `<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#14262b"><link rel="manifest" href="../manifest.webmanifest"><link rel="icon" type="image/png" href="../icon-192.png"><title>Tag ${n} von 60 · telc B1</title><style>
${css}
.wrap{max-width:860px;margin:0 auto;padding:28px 20px 60px}.hd2{background:var(--ink);color:#fff;border-bottom:8px solid var(--gelb)}.hd2 .wrap{padding-bottom:22px}.hd2 h1{margin:0;font:600 2rem/1.1 var(--disp)}.hd2 p{margin:6px 0 0;color:#cfdcdc}
.nav{display:flex;justify-content:space-between;align-items:center;gap:10px;margin:18px 0}.nav a,.nav select{font:600 1rem var(--disp);padding:9px 16px;border-radius:4px;background:var(--white);box-shadow:inset 0 0 0 1.5px #a9b6b4;color:var(--ink);text-decoration:none;border:0}
.it{background:var(--white);border:1.5px solid var(--line);border-left:8px solid var(--petrol);border-radius:4px;padding:14px 18px;margin:14px 0}.it.new{border-left-color:var(--gelb)}.it.mock{border-left-color:var(--ink)}.it.story{border-left-style:dashed;border-left-color:#a9b6b4}
.it .k{font:600 .8rem var(--disp);color:var(--mut)}.it h2{margin:2px 0 4px;font:600 1.3rem/1.25 var(--disp)}.it p{margin:4px 0 10px;color:var(--mut)}.it .go a{display:inline-block;margin:0 8px 6px 0;padding:8px 16px;background:var(--petrol);color:#fff;border-radius:4px;text-decoration:none;font:600 .95rem var(--disp)}.it .go a.s{background:var(--white);color:var(--petrol);box-shadow:inset 0 0 0 1.5px var(--petrol)}
.it label{display:inline-flex;gap:8px;align-items:center;font-weight:600;cursor:pointer;margin-left:6px}.it.done{background:var(--okbg);border-left-color:var(--ok)}
</style></head><body><div class="hd2"><div class="wrap"><p>${ph}</p><h1>Tag ${n} von 60</h1><p id="dt"></p></div></div><div class="wrap">
<div class="nav">${prev}<select onchange="location.href=this.value" aria-label="Tag wählen">${opts}</select>${next}</div>
<p class="mut">Heute: ${n===60?'Prüfungsvorabend. Ruhe, kurze Wiederholung, früh schlafen.':'öffne jedes Feld, arbeite es ganz durch und hake es ab.'}</p>
${body}
<div class="nav">${prev}<a href="../index.html#plan">Plan</a>${next}</div></div>
<script>(function(){const N=${n};let ed='2027-02-25';try{const v=localStorage.getItem('telc_examdate');if(/^\\d{4}-\\d{2}-\\d{2}$/.test(v))ed=v}catch(e){}
const d=new Date(new Date(ed+'T12:00:00').getTime()-(60-(N-1))*864e5);document.getElementById('dt').textContent=['So','Mo','Di','Mi','Do','Fr','Sa'][d.getDay()]+' '+d.toLocaleDateString('de-DE')+' · Prüfung am '+new Date(ed+'T12:00:00').toLocaleDateString('de-DE');
document.querySelectorAll('.it input').forEach(c=>{const k='telc60:'+c.dataset.k;try{c.checked=localStorage.getItem(k)==='1'}catch(e){}c.closest('.it').classList.toggle('done',c.checked);
c.onchange=()=>{try{localStorage.setItem(k,c.checked?'1':'0')}catch(e){}c.closest('.it').classList.toggle('done',c.checked)}});
document.addEventListener('keydown',e=>{if(e.target.tagName==='SELECT')return;if(e.key==='ArrowRight'&&${n<60})location.href='T${pad(n+1)}.html';if(e.key==='ArrowLeft'&&${n>1})location.href='T${pad(n-1)}.html'})})()</script></body></html>`};
PLAN60.forEach((its,i)=>{const n=i+1;let b='';
 its.map(item).forEach((z,j)=>{const cls=z.k==='Neue Lektion'?'new':z.k==='Modelltest'?'mock':'';
  b+=`<div class="it ${cls}"><div class="k">${z.k}</div><h2>${esc(z.t)}</h2><p>${esc(z.d||'')}</p><div class="go"><a href="${z.h}">Öffnen</a>${z.a?`<a class="s" href="${z.a}">Lösungen</a>`:''}<label><input type="checkbox" data-k="${n}-${j}"> erledigt</label></div></div>\n`});
 (STORY60[n]||[]).forEach(id=>{b+=`<div class="it story"><div class="k">Geschichte · 30 Minuten laut lesen</div><h2>Geschichte ${+id.slice(1)} · ${esc(STT[id])}</h2><p>Sprechen Teil 2 und 3 und Schreiben zum selben Thema.</p><div class="go"><a href="../Geschichten/index.html#${id}">Öffnen</a><label><input type="checkbox" data-k="${n}-${id}"> erledigt</label></div></div>\n`});
 fs.writeFileSync(path.join(root,'Tag60','T'+pad(n)+'.html'),tpl(n,b))});
// link "Tag N" in the plan and add pages to the offline list
if(!idx.includes("Tag60/T")){
 idx=idx.replace("<span class=\"d\">Tag '+(i+1)+(all?' ✓':'')+'<small>","<span class=\"d\"><a href=\"Tag60/T'+String(i+1).padStart(2,'0')+'.html\">Tag '+(i+1)+'</a>'+(all?' ✓':'')+'<small>");
 idx=idx.replace('"pages": ["index.html",','"pages": ["index.html", '+Array.from({length:60},(_,i)=>'"Tag60/T'+pad(i+1)+'.html"').join(', ')+',');
 fs.writeFileSync(path.join(root,'index.html'),idx)}
console.log('built 60 pages');
