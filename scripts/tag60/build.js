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
const tpl=(n,its)=>{const ph=PH.find(([a,b])=>n-1>=a&&n-1<b)[2];
const prev=n>1?`T${pad(n-1)}.html`:'../index.html#plan',next=n<60?`T${pad(n+1)}.html`:'../index.html#plan';
const opts=Array.from({length:60},(_,i)=>`<option value="T${pad(i+1)}.html"${i+1===n?' selected':''}>Tag ${i+1}</option>`).join('');
const data=JSON.stringify(its.map(z=>({k:z.k,t:z.t,d:z.d||'',h:z.h,a:z.a||''})));
return `<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#14262b"><link rel="manifest" href="../manifest.webmanifest"><link rel="icon" type="image/png" href="../icon-192.png"><title>Tag ${n} von 60 · telc B1</title><style>
${css}
html,body{height:100%}body{display:flex;flex-direction:column;overflow:hidden}
.top{background:var(--ink);color:#fff;border-bottom:6px solid var(--gelb);display:flex;align-items:center;gap:12px;padding:8px 14px;flex-wrap:wrap}
.top h1{margin:0;font:600 1.3rem/1.1 var(--disp)}.top small{color:#cfdcdc;display:block;font:400 .8rem var(--body)}
.top a,.top select{font:600 .95rem var(--disp);padding:6px 12px;border-radius:4px;background:#fff;color:var(--ink);text-decoration:none;border:0}.top .sp{flex:1}
.main{flex:1;display:flex;min-height:0}.view{flex:1;min-width:0;background:#fff}.view iframe{width:100%;height:100%;border:0;display:block}
.side{width:340px;max-width:40%;overflow:auto;background:var(--paper);border-left:2px solid var(--line);padding:10px}
.si{display:block;width:100%;text-align:left;background:#fff;border:1.5px solid var(--line);border-left:7px solid var(--petrol);border-radius:4px;padding:9px 12px;margin:0 0 8px;cursor:pointer;font:inherit;color:var(--ink)}
.si.new{border-left-color:var(--gelb)}.si.mock{border-left-color:var(--ink)}.si.story{border-left-style:dashed;border-left-color:#a9b6b4}
.si .k{display:block;font:600 .72rem var(--disp);color:var(--mut)}.si b{display:block;font:600 1rem/1.25 var(--disp)}.si i{display:block;font-style:normal;font-size:.82rem;color:var(--mut);margin-top:2px}
.si.on{box-shadow:0 0 0 3px var(--gelb);background:#fffbe0}.si.done{background:var(--okbg);border-left-color:var(--ok)}
.row2{display:flex;gap:8px;align-items:center;margin-top:6px;font-size:.85rem}.row2 button{font:600 .8rem var(--disp);padding:4px 10px;border-radius:3px;border:1.5px solid var(--petrol);background:#fff;color:var(--petrol);cursor:pointer}.row2 label{margin-left:auto;display:flex;gap:5px;align-items:center;cursor:pointer}
.nx{display:flex;gap:8px;margin-top:10px}.nx button{flex:1;font:600 .9rem var(--disp);padding:9px;border-radius:4px;border:0;background:var(--petrol);color:#fff;cursor:pointer}.nx button.g{background:#fff;color:var(--petrol);box-shadow:inset 0 0 0 1.5px var(--petrol)}
@media (max-width:820px){.main{flex-direction:column-reverse}.side{width:100%;max-width:none;max-height:38%;border-left:0;border-top:2px solid var(--line)}}
</style></head><body>
<div class="top"><div><h1>Tag ${n} von 60</h1><small>${ph} · <span id="dt"></span></small></div><span class="sp"></span><a href="${prev}">← Tag ${n-1||'Plan'}</a><select onchange="location.href=this.value" aria-label="Tag wählen">${opts}</select><a href="${next}">Tag ${n<60?n+1:'Plan'} →</a><a href="../index.html#plan">Plan</a></div>
<div class="main"><div class="view"><iframe id="fr" title="Inhalt" src="about:blank"></iframe></div><div class="side" id="side"></div></div>
<script>(function(){const N=${n},IT=${data};let ed='2027-02-25';try{const v=localStorage.getItem('telc_examdate');if(/^\\d{4}-\\d{2}-\\d{2}$/.test(v))ed=v}catch(e){}
const d=new Date(new Date(ed+'T12:00:00').getTime()-(60-(N-1))*864e5);document.getElementById('dt').textContent=['So','Mo','Di','Mi','Do','Fr','Sa'][d.getDay()]+' '+d.toLocaleDateString('de-DE')+' · Prüfung '+new Date(ed+'T12:00:00').toLocaleDateString('de-DE');
const fr=document.getElementById('fr'),side=document.getElementById('side');let cur=0,ans=false;
const dk=i=>{try{return localStorage.getItem('telc60:'+N+'-'+i)==='1'}catch(e){return false}};
function show(i,a){cur=i;ans=!!a;fr.src=(a&&IT[i].a)?IT[i].a:IT[i].h;try{history.replaceState(null,'','#'+(i+1))}catch(e){}draw()}
function draw(){let h='';IT.forEach((z,i)=>{const c=z.k==='Neue Lektion'?'new':z.k==='Modelltest'?'mock':z.k.indexOf('Geschichte')===0?'story':'';
 h+='<div class="si '+c+(i===cur?' on':'')+(dk(i)?' done':'')+'" data-i="'+i+'" role="button" tabindex="0"><span class="k">'+z.k+'</span><b>'+z.t.replace(/</g,'&lt;')+'</b><i>'+z.d.replace(/</g,'&lt;')+'</i>'+
 '<div class="row2">'+(z.a?'<button data-a="'+i+'">Lösungen</button>':'')+'<label><input type="checkbox" data-c="'+i+'"'+(dk(i)?' checked':'')+'> erledigt</label></div></div>'});
 h+='<div class="nx"><button class="g" id="pv">← zurück</button><button id="nx">weiter →</button></div>';side.innerHTML=h;
 side.querySelectorAll('.si').forEach(e=>e.onclick=ev=>{if(ev.target.closest('button,label'))return;show(+e.dataset.i,false)});
 side.querySelectorAll('[data-a]').forEach(b=>b.onclick=()=>show(+b.dataset.a,true));
 side.querySelectorAll('[data-c]').forEach(c=>c.onchange=()=>{try{localStorage.setItem('telc60:'+N+'-'+c.dataset.c,c.checked?'1':'0')}catch(e){}draw()});
 document.getElementById('pv').onclick=()=>{if(cur>0)show(cur-1,false);else location.href='${prev}'};
 document.getElementById('nx').onclick=()=>{if(cur<IT.length-1)show(cur+1,false);else location.href='${next}'}}
const st=parseInt((location.hash||'').slice(1),10);show(st>=1&&st<=IT.length?st-1:0,false)})()</script></body></html>`};
PLAN60.forEach((its,i)=>{const n=i+1;const arr=its.map(item);
 (STORY60[n]||[]).forEach(id=>arr.push({k:'Geschichte · 30 Minuten laut lesen',t:'Geschichte '+(+id.slice(1))+' · '+STT[id],d:'Sprechen Teil 2 und 3 und Schreiben zum selben Thema.',h:'../Geschichten/index.html#'+id}));
 fs.writeFileSync(path.join(root,'Tag60','T'+pad(n)+'.html'),tpl(n,arr))});
// link "Tag N" in the plan and add pages to the offline list
if(!idx.includes("Tag60/T")){
 idx=idx.replace("<span class=\"d\">Tag '+(i+1)+(all?' ✓':'')+'<small>","<span class=\"d\"><a href=\"Tag60/T'+String(i+1).padStart(2,'0')+'.html\">Tag '+(i+1)+'</a>'+(all?' ✓':'')+'<small>");
 idx=idx.replace('"pages": ["index.html",','"pages": ["index.html", '+Array.from({length:60},(_,i)=>'"Tag60/T'+pad(i+1)+'.html"').join(', ')+',');
 fs.writeFileSync(path.join(root,'index.html'),idx)}
console.log('built 60 pages');
