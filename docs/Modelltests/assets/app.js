(function(){
'use strict';
const meta=JSON.parse(document.getElementById('meta').textContent),N=meta.n,KEY=meta.key,EX=meta.ex,TK=meta.tk,SK='telc:mt:'+N;
const M60=60000;
const B={lesen:90*M60,hoeren:32*M60,schreiben:30*M60,vorb:20*M60,gespr:15*M60};
const SECS=['lesen','hoeren','schreiben','sprechen'];
const LAB={lesen:'Lesen und Sprachbausteine',hoeren:'Hören',schreiben:'Schreiben',sprechen:'Sprechen'};
/* telc B1 Punkte je Aufgabe: Lesen 1-5 je 5, 6-10 je 5, 11-20 je 2,5 · Sprachb. je 1,5 · Hören 1-5 je 5, 6-15 je 2,5, 16-20 je 5 */
function wt(k){const p=k[0],n=+k.slice(1);if(p==='s')return 1.5;if(p==='l')return n<=10?5:2.5;return (n<=5||n>=16)?5:2.5}
let st={};try{st=JSON.parse(localStorage.getItem(SK)||'{}')}catch(e){}
st.sel=st.sel||{};st.vis=st.vis||{};st.el=st.el||{};st.lock=st.lock||{};st.cur=st.cur||{};st.began=st.began||{};
const save=()=>{try{localStorage.setItem(SK,JSON.stringify(st))}catch(e){}};
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const now=()=>Date.now();
let cur='lesen',aud=null,graceT=null;
function toast(m){const t=$('#toast');t.textContent=m;t.hidden=false;clearTimeout(toast.i);toast.i=setTimeout(()=>t.hidden=true,2400)}
const fmt=ms=>{ms=Math.max(0,ms);const s=Math.ceil(ms/1000);return String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0')};
/* ---------- Zeit ---------- */
// Uhren: lesen, hoeren, schreiben, vorb, gespr. Aktiv ist immer höchstens eine.
function used(k){return (st.el[k]||0)+(st.act===k&&st.since?now()-st.since:0)}
function budget(k){return k==='hoeren'&&st.hb?st.hb:B[k]}
function rem(k){return st.lock[k]?0:budget(k)-used(k)}
function commit(){if(st.act&&st.since){st.el[st.act]=(st.el[st.act]||0)+now()-st.since}st.since=now()}
function setAct(k){commit();st.act=k;st.since=k?now():0;save()}
function clockOf(sec){return sec==='sprechen'?(st.talk?'gespr':'vorb'):sec}
/* ---------- Verfügbarkeit ---------- */
function avail(s){if(!st.t0)return false;if(st.fin)return true;
 if(s==='lesen')return true;
 if(s==='hoeren')return !!st.lock.lesen;
 if(s==='schreiben')return !!st.lock.hoeren;
 if(s==='sprechen')return !!st.lock.schreiben;
 return false}
function tabs(){
 $$('.sbtn').forEach(b=>{const s=b.dataset.t;b.disabled=s==='antworten'?!st.fin:!avail(s);b.classList.toggle('on',s===cur);b.classList.toggle('end',!!st.lock[s])});
 const h=$('#sidehint');
 h.textContent=st.fin?'Prüfung abgegeben.':!st.lock.lesen?'Lesen und Sprachbausteine laufen zusammen 90 Minuten. Danach folgt Hören.':!st.lock.hoeren?'Hören läuft. Schreiben und Sprechen sind danach frei.':!st.lock.schreiben?'Als Nächstes: Schreiben (30 Minuten).':'Zum Schluss: Sprechen (20 Minuten Vorbereitung, ca. 15 Minuten Gespräch).';
 const b=$('#endcur');const ok=!st.fin&&SECS.includes(cur)&&!st.lock[cur]&&st.began[cur]&&(cur!=='hoeren'||st.hend);
 b.hidden=!ok;if(ok)b.textContent=cur==='sprechen'?'Sprechen beenden':(cur==='lesen'?'Lesen beenden':LAB[cur]+' beenden');
}
/* ---------- Navigation ---------- */
function go(s,keep){
 if(!st.fin&&s!=='antworten'&&!avail(s))return;
 if(s==='antworten'&&!st.fin)return;
 if(SECS.includes(cur)&&cur!==s)leaveTask(cur);
 cur=s;st.where=s;
 $$('main > section').forEach(x=>x.classList.toggle('on',x.id===s));
 $$('#lesen,#hoeren,#schreiben,#sprechen').forEach(x=>x.classList.toggle('gated',!st.lock[x.id]&&!st.fin&&!st.began[x.id]));
 if(TK[s]){showTask(s,st.cur[s]||0)}else{pal()}
 if(!st.fin&&SECS.includes(s)&&st.began[s]&&!st.lock[s]&&s!=='hoeren'&&s!=='sprechen')setAct(clockOf(s));
 tabs();save();
 if(s==='antworten')window.scrollTo(0,0);
}
function leaveTask(sec){const i=st.cur[sec];if(i===undefined||!TK[sec])return;(TK[sec][i]||[]).forEach(k=>{st.vis[k]=1})}
function showTask(sec,i){
 if(st.cur[sec]!==undefined&&st.cur[sec]!==i)leaveTask(sec);
 st.cur[sec]=i;
 $$('#'+sec+' .task').forEach(t=>t.classList.toggle('on',+t.dataset.i===i));
 pal();save();
}
function pal(){
 const P=$('#pal');
 if(!TK[cur]){P.innerHTML='<h5>'+(cur==='antworten'?'Auswertung':LAB[cur]||'')+'</h5><p class="hint">'+(cur==='schreiben'?'Ein Brief oder eine E-Mail zu vier Leitpunkten. Etwa 80 bis 100 Wörter.':cur==='sprechen'?'Drei Teile: Kontakt aufnehmen, Thema vortragen, gemeinsam planen.':'')+'</p>';return}
 const ti=st.cur[cur]||0;let h='<h5>'+LAB[cur]+' · Aufgaben</h5><p class="hint">Klicken zum Springen</p>';
 const titles=meta.tt[cur];
 TK[cur].forEach((ks,idx)=>{
  h+='<div class="grp">'+esc(titles[idx])+'</div><div class="g">';
  ks.forEach(k=>{const e=EX[k],a=st.sel[k]!==undefined,v=st.vis[k]&&!a&&idx!==ti;
   h+='<a data-k="'+k+'" data-t="'+idx+'" class="'+(a?'ans':v?'vis':'')+(idx===ti&&false?' curT':'')+'">'+e.n+'</a>'});
  h+='</div>'});
 h+='<div class="legend"><span class="l-a">beantwortet</span><span class="l-v">nicht beantwortet (übersprungen)</span><span class="l-n">noch nicht gesehen</span></div>';
 P.innerHTML=h;
 $$('#pal a').forEach(a=>a.onclick=()=>{showTask(cur,+a.dataset.t);const it=document.getElementById('i-'+a.dataset.k);if(it)it.scrollIntoView({block:'center',behavior:'smooth'})});
}
/* ---------- Antworten markieren ---------- */
document.addEventListener('change',e=>{const t=e.target;if(t.type==='radio'&&t.name&&KEY[t.name]!==undefined&&!st.fin){st.sel[t.name]=t.value;save();pal()}});
function restore(){Object.keys(st.sel).forEach(k=>{const r=document.querySelector('input[name="'+k+'"][value="'+st.sel[k]+'"]');if(r)r.checked=true})}
/* ---------- Abschnitte beenden ---------- */
function lockSec(s){commit();st.lock[s]=true;if(st.act===clockOf(s)||st.act===s){st.act=null;st.since=0}
 const sec=$('#'+s);sec.classList.add('locked');sec.classList.remove('gated');
 sec.querySelectorAll('input,textarea,select').forEach(x=>x.disabled=true);save()}
function endSec(s,msg){
 if(st.lock[s])return;
 if(s==='hoeren'){try{aud&&aud.pause()}catch(e){}clearInterval(graceT)}
 lockSec(s);leaveTask(s);
 toast(msg||(LAB[s]+' beendet, gespeichert'));
 if(s==='sprechen'){finalize();return}
 const nx={lesen:'hoeren',hoeren:'schreiben',schreiben:'sprechen'}[s];
 st.began[nx]=st.began[nx]||0;go(nx);save()
}
/* ---------- Tick ---------- */
function tick(){
 if(!st.t0||st.fin)return;
 const a=st.act;
 let main,lab,sub,sl;
 const wr=['lesen','hoeren','schreiben'];
 if(cur==='sprechen'||st.lock.schreiben){lab='Mündliche Prüfung';main=(st.talk?rem('gespr'):rem('vorb')+B.gespr)}
 else{lab='Schriftliche Prüfung';main=rem('lesen')+rem('hoeren')+rem('schreiben')}
 const sc=clockOf(SECS.includes(cur)?cur:'lesen');
 sub=rem(sc);sl={lesen:'Lesen und Sprachbausteine',hoeren:'Hören',schreiben:'Schreiben',vorb:'Vorbereitung',gespr:'Gespräch'}[sc];
 if(cur==='antworten'){$('#tm-main').textContent='—';$('#tm-sub').textContent='—';return}
 $('#tm-l').textContent=lab;$('#tm-main').textContent=fmt(main);$('#tm-sl').textContent=sl;
 $('#tm-sub').textContent=st.began[cur]||cur==='hoeren'&&!st.began.hoeren?fmt(sub):fmt(budget(sc));
 $('.bc').classList.toggle('low',sub<=5*M60&&st.began[cur]&&!st.lock[cur]);
 if(a&&!st.lock[a==='vorb'||a==='gespr'?'sprechen':a]&&rem(a)<=0){
   if(a==='vorb'){setTalk()}else endSec(a==='gespr'?'sprechen':a,'Die Zeit ist abgelaufen. Ihre Antworten sind gespeichert.')}
 if(Math.floor(now()/1000)%5===0)save();
}
/* ---------- Hören ---------- */
function setupAudio(){
 aud=$('#aud');if(!aud)return;
 aud.addEventListener('loadedmetadata',()=>{if(isFinite(aud.duration)&&aud.duration>60&&!st.began.hoeren){st.hb=Math.ceil(aud.duration*1000)+120000;save();tick()}});
 aud.addEventListener('timeupdate',()=>{if(aud.duration){$('#aprog').style.width=(aud.currentTime/aud.duration*100)+'%'}});
 aud.addEventListener('pause',()=>{if(!aud.ended&&!holdAudio&&st.began.hoeren&&!st.lock.hoeren&&!st.hend){aud.play().catch(()=>{})}});
 aud.addEventListener('ended',()=>{st.hend=true;$('#hdone').disabled=false;aStat('Der Hörtext ist zu Ende. Ergänzen Sie jetzt Ihre Antworten. Dafür haben Sie noch zwei Minuten.');
   clearInterval(graceT);const t0=now();graceT=setInterval(()=>{if(st.lock.hoeren){clearInterval(graceT);return}if(now()-t0>120000){clearInterval(graceT);endSec('hoeren','Hören beendet, gespeichert')}},1000);tabs();save()});
 aud.addEventListener('error',()=>{$('#noaudio').style.display='block';$('#hdone').disabled=false;st.hend=true;tabs()});
}
function aStat(t){$('#astat').textContent=t}
function startHoeren(){
 if(st.lock.hoeren)return;
 st.began.hoeren=1;setAct('hoeren');$('#hoeren').classList.remove('gated');save();tabs();
 aStat('Der Hörtext läuft. Er wird nur einmal abgespielt, jeder Text je nach Aufgabe ein- oder zweimal.');
 if(aud){const p=aud.play();if(p&&p.catch)p.catch(()=>{aStat('Das Audio konnte nicht automatisch starten. Klicken Sie auf „Audio starten“.');$('#aplay').hidden=false})}
 if(st.hend){$('#hdone').disabled=false}
}
/* ---------- Sprechen ---------- */
function setTalk(){commit();st.talk=1;st.el.vorb=B.vorb;setAct('gespr');$('#spprep').hidden=true;$('#sptalk').hidden=false;$('#spstart').hidden=true;toast('Das Gespräch beginnt. Die Vorbereitungszeit ist vorbei.');tabs();save()}
/* ---------- Abgabe ---------- */
function counts(){const o={};[['l','Lesen'],['s','Sprachbausteine'],['h','Hören']].forEach(([p])=>{const ks=Object.keys(KEY).filter(k=>k[0]===p);o[p]=[ks.filter(k=>st.sel[k]!==undefined).length,ks.length]});return o}
function score(p){return Object.keys(KEY).filter(k=>k[0]===p&&String(KEY[k])===st.sel[k]).length}
function pts(p){return Object.keys(KEY).filter(k=>k[0]===p&&String(KEY[k])===st.sel[k]).reduce((a,k)=>a+wt(k),0)}
function finalize(){
 commit();st.fin=true;st.sc={l:score('l'),s:score('s'),h:score('h')};st.pt={l:pts('l'),s:pts('s'),h:pts('h')};
 SECS.forEach(s=>{if(!st.lock[s])lockSec(s)});
 st.act=null;save();render();go('antworten');
}
function openFinish(){
 const c=counts();
 const rows=[['lesen','Lesen',c.l[0]+' von '+c.l[1]],['lesen','Sprachbausteine',c.s[0]+' von '+c.s[1]],['hoeren','Hören',c.h[0]+' von '+c.h[1]],['schreiben','Schreiben',((st.brief||'').trim().match(/\S+/g)||[]).length+' Wörter geschrieben']];
 $('#chk').innerHTML=rows.map(r=>'<div class="chk"><label><b>'+r[1]+'</b><small>'+r[2]+(st.lock[r[0]]?' · beendet':'')+'</small></label></div>').join('');
 $('#modal').hidden=false;$('#submit').disabled=false;
}
/* ---------- Auswertung ---------- */
function pct(a,b){return b?Math.round(a/b*100):0}
function render(){
 const c=counts(),L=st.sc.l,S=st.sc.s,H=st.sc.h;
 const P=st.pt||{l:L*3.75,s:S*1.5,h:H*3.75},pl=P.l,ps=P.s,ph=P.h;
 $('#ans-sum').innerHTML='<div class="sum"><div><b>'+L+' / '+c.l[1]+'</b><small>Lesen · '+pl.toFixed(1).replace('.0','')+' von 75 Punkten</small></div><div><b>'+S+' / '+c.s[1]+'</b><small>Sprachbausteine · '+ps.toFixed(1).replace('.0','')+' von 30</small></div><div><b>'+H+' / '+c.h[1]+'</b><small>Hören · '+ph.toFixed(1).replace('.0','')+' von 75</small></div></div>';
 verdict();list();
 $('#schmodel').hidden=false;
}
function verdict(){
 const v=$('#verdict');if(!st.sc)return;
 const sch=parseFloat(st.ssch),spr=parseFloat(st.sspr);
 const P=st.pt||{l:st.sc.l*3.75,s:st.sc.s*1.5,h:st.sc.h*3.75},base=P.l+P.s+P.h;
 let t='<p><b>Schriftlich bisher:</b> '+base.toFixed(1).replace('.0','')+' von 180 Punkten (Lesen, Sprachbausteine, Hören). Dazu kommen höchstens 45 Punkte für Schreiben. Für „bestanden“ brauchen Sie im schriftlichen Teil 135 von 225 Punkten (60 %) und im mündlichen Teil 45 von 75 Punkten.</p>';
 if(!isNaN(sch)){const w=base+sch;t+='<p><b>Schriftlich mit Schreiben:</b> '+w.toFixed(1).replace('.0','')+' von 225 · '+(w>=135?'<span class="tag ok">60 % erreicht</span>':'<span class="tag no">unter 60 %</span>')+'</p>'}
 if(!isNaN(spr)){t+='<p><b>Mündlich:</b> '+spr+' von 75 · '+(spr>=45?'<span class="tag ok">60 % erreicht</span>':'<span class="tag no">unter 60 %</span>')+'</p>'}
 if(!isNaN(sch)&&!isNaN(spr)){const tot=base+sch+spr,ok=base+sch>=135&&spr>=45;t+='<p><b>Gesamt:</b> '+tot.toFixed(1).replace('.0','')+' von 300 · <b>'+(ok?'Bestanden':'Nicht bestanden')+'</b>'+(ok?' ('+(tot>=270?'sehr gut':tot>=240?'gut':tot>=210?'befriedigend':'ausreichend')+')':'')+'</p>'}
 v.innerHTML=t;
}
function opt(e,i){return e.ot?(e.ot[i]):''}
function card(k){
 const e=EX[k],s=st.sel[k],a=String(KEY[k]),ok=s===a,none=s===undefined;
 const cls=none?'w':ok?'r':'w';
 const show=v=>{if(v===undefined)return '<i>keine Antwort</i>';if(e.t==='mc'){const i='abc'.indexOf(v);return '<b>'+v+'</b> · '+esc(opt(e,i))}if(e.t==='rf')return '<b>'+(v==='r'?'richtig':'falsch')+'</b>';return '<b>'+esc(v)+'</b>'};
 return '<div class="a-item '+cls+'" data-ok="'+(ok?1:0)+'"><div class="a-head"><span>'+e.n+'</span><span class="tag '+(ok?'ok':'no')+'">'+(ok?'richtig':none?'offen':'falsch')+'</span><small>'+esc(e.tit)+'</small></div><div class="a-body"><p class="lab">Aufgabe</p><p>'+esc(e.q)+'</p><p><span class="lab">Ihre Antwort:</span> '+show(s)+'</p><p><span class="lab">Richtig:</span> '+show(a)+'</p><p class="mem"><span class="lab">Warum?</span> '+esc(e.why)+'</p></div></div>';
}
function list(f){
 f=f||st.filt||'wrong';st.filt=f;
 $$('.filter button').forEach(b=>b.classList.toggle('on',b.dataset.f===f));
 const ks=Object.keys(KEY).filter(k=>f==='all'||String(KEY[k])!==st.sel[k]);
 $('#ans-list').innerHTML=ks.length?ks.map(card).join(''):'<p class="hint">Alle Aufgaben waren richtig.</p>';
}
/* ---------- Schreiben ---------- */
function wc(){const n=((st.brief||'').trim().match(/\S+/g)||[]).length;const e=$('#wc');if(e)e.textContent=n+' Wörter (Ziel: 80 bis 100)'}
function copyWriting(btn){
 const tx='Bitte bewerte meinen Brief zum telc-B1-Modelltest '+N+' nach den telc-Kriterien (Inhalt, Kommunikative Gestaltung, Formale Richtigkeit, jeweils mit Punkten; maximal 45 Punkte). Zeige die Fehler, erkläre sie kurz auf Englisch und gib eine verbesserte Fassung.\n\nAufgabe:\n'+meta.wtask+'\n\nMein Text:\n'+(st.brief||'');
 const done=()=>toast('Kopiert: Aufgabe und Text. Füge ihn jetzt in Claude ein.');
 if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(tx).then(done,()=>fb(tx,done))}else fb(tx,done)
}
function fb(tx,done){const a=document.createElement('textarea');a.value=tx;a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);a.select();try{document.execCommand('copy');done()}catch(e){toast('Kopieren nicht möglich')}a.remove()}
/* ---------- Pause ---------- */
let holdAudio=false;
function pauseExam(){
 commit();st.paused=true;st.pact=st.act;st.act=null;st.since=0;
 if(aud&&st.began.hoeren&&!st.lock.hoeren){st.apos=aud.currentTime||0;holdAudio=true;try{aud.pause()}catch(e){}}
 if(st.began.hoeren&&!st.lock.hoeren&&st.hend===undefined){}
 stopRec();save();
}
function resumeExam(){
 st.paused=false;st.act=st.pact||null;st.since=st.act?now():0;st.pact=null;
 if(aud&&st.began.hoeren&&!st.lock.hoeren&&!st.hend){
  holdAudio=false;
  const go2=()=>{try{if(st.apos)aud.currentTime=st.apos}catch(e){};const p=aud.play();if(p&&p.catch)p.catch(()=>{$('#aplay').hidden=false;aStat('Klicken Sie auf „Audio starten“, um an der Stelle weiterzuhören.')})};
  if(aud.readyState>=1)go2();else aud.addEventListener('loadedmetadata',go2,{once:true});
 }
 save();
}
/* ---------- Aufnahme (Sprechen) ---------- */
const IDB='telc-mt-audio';let db=null,rec=null,recPart=null,recT0=0,recIv=null,recog=null,recChunks=[],recStream=null,recTxt='';
function idb(){return new Promise((res,rej)=>{if(db)return res(db);const r=indexedDB.open(IDB,1);r.onupgradeneeded=()=>r.result.createObjectStore('a');r.onsuccess=()=>{db=r.result;res(db)};r.onerror=()=>rej(r.error)})}
function idbPut(k,v){return idb().then(d=>new Promise((res,rej)=>{const t=d.transaction('a','readwrite');t.objectStore('a').put(v,k);t.oncomplete=res;t.onerror=()=>rej(t.error)}))}
function idbGet(k){return idb().then(d=>new Promise((res,rej)=>{const q=d.transaction('a').objectStore('a').get(k);q.onsuccess=()=>res(q.result);q.onerror=()=>rej(q.error)}))}
function recRows(){st.rc=st.rc||{};$$('.rrow').forEach(row=>{const p=row.dataset.p;const c=st.rc[p];
 const t=row.querySelector('.rtx');if(c&&c.txt!==undefined)t.value=c.txt;
 row.querySelector('.rt').textContent=c&&c.sec?fmt(c.sec*1000):'00:00';
 if(c&&c.aud)idbGet(SK+':'+p).then(b=>{if(b){const a=row.querySelector('audio');a.src=URL.createObjectURL(b);a.hidden=false}}).catch(()=>{});
 t.oninput=()=>{st.rc[p]=st.rc[p]||{};st.rc[p].txt=t.value;save()};
 row.querySelector('.rb').onclick=()=>toggleRec(row,p)})}
async function toggleRec(row,p){
 if(rec){stopRec();return}
 if(!navigator.mediaDevices||!window.MediaRecorder){toast('Aufnahme wird von diesem Browser nicht unterstützt');return}
 try{recStream=await navigator.mediaDevices.getUserMedia({audio:true})}catch(e){toast('Kein Zugriff auf das Mikrofon');return}
 recChunks=[];rec=new MediaRecorder(recStream);recPart=p;recT0=now();recTxt=(st.rc[p]&&st.rc[p].txt)||'';
 rec.ondataavailable=e=>{if(e.data.size)recChunks.push(e.data)};
 rec.onstop=()=>{const blob=new Blob(recChunks,{type:rec.mimeType||'audio/webm'});const sec=Math.round((now()-recT0)/1000);st.rc[p]=st.rc[p]||{};st.rc[p].sec=sec;st.rc[p].aud=1;
  idbPut(SK+':'+p,blob).catch(()=>{});const a=row.querySelector('audio');a.src=URL.createObjectURL(blob);a.hidden=false;row.querySelector('.rt').textContent=fmt(sec*1000);
  recStream.getTracks().forEach(t=>t.stop());rec=null;recPart=null;row.querySelector('.rb').textContent='Aufnahme starten';row.classList.remove('live');save()};
 rec.start();row.classList.add('live');row.querySelector('.rb').textContent='Aufnahme beenden';
 clearInterval(recIv);recIv=setInterval(()=>{row.querySelector('.rt').textContent=fmt(now()-recT0)},300);
 const SR=window.SpeechRecognition||window.webkitSpeechRecognition;
 if(SR){try{recog=new SR();recog.lang='de-DE';recog.continuous=true;recog.interimResults=true;
  recog.onresult=ev=>{let fin='',int='';for(let i=ev.resultIndex;i<ev.results.length;i++){const r=ev.results[i];if(r.isFinal)fin+=r[0].transcript+' ';else int+=r[0].transcript}
   if(fin)recTxt+=(recTxt&&!/\s$/.test(recTxt)?' ':'')+fin;const t=row.querySelector('.rtx');t.value=recTxt+int;st.rc[p]=st.rc[p]||{};st.rc[p].txt=t.value;save()};
  recog.onend=()=>{if(rec&&recPart===p){try{recog.start()}catch(e){}}};recog.start()}catch(e){recog=null}}
}
function stopRec(){clearInterval(recIv);try{recog&&(recog.onend=null,recog.stop())}catch(e){}recog=null;try{rec&&rec.state!=='inactive'&&rec.stop()}catch(e){}}
function copySprechen(){
 const parts=[...$$('.rrow')].map(r=>{const c=st.rc[r.dataset.p]||{};return '['+r.dataset.n+'] Dauer: '+fmt((c.sec||0)*1000)+'\nText: '+(c.txt||'(keine Eingabe)')}).join('\n\n');
 const tx='Bitte bewerte meine Antworten im telc-B1-Modelltest '+N+' (Sprechen) nach den telc-Kriterien (Aufgabenbewältigung, Interaktion, Wortschatz, Grammatik; Aussprache kann ich nicht aufnehmen). Maximal 75 Punkte. Zeige Fehler, erkläre sie kurz auf Englisch und gib eine bessere Version.\n\n'+parts+'\n\nNotizen:\n'+(st.notes||'');
 const done=()=>toast('Kopiert. Füge den Text jetzt in Claude ein.');
 if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(tx).then(done,()=>fb(tx,done));else fb(tx,done)
}
/* ---------- Start ---------- */
function showApp(){$('#start').hidden=true;$('#app').hidden=false}
function begin(){
 if(!st.t0){st.t0=now();st.began.lesen=1;st.act='lesen';st.since=now();save()}
 else if(st.paused){resumeExam()}
 else{st.since=st.act?now():0}
 showApp();
 if(st.began.sprechen&&!st.lock.sprechen){if(st.talk){$('#sptalk').hidden=false}else{$('#spprep').hidden=false}}
 if(st.began.hoeren&&!st.lock.hoeren&&st.hend){$('#hdone').disabled=false}
 const w=st.where&&(st.fin||avail(st.where))?st.where:'lesen';
 go(st.fin?'antworten':w);
 if(st.fin)render();
}
function bind(){
 $('#begin').onclick=()=>begin();
 const r=$('#reset');if(r){r.hidden=!st.t0;r.onclick=()=>{if(confirm('Alle Antworten und Zeiten dieses Tests löschen und neu beginnen?')){try{localStorage.removeItem(SK)}catch(e){}location.reload()}}}
 const b=$('#begin');if(st.t0&&!st.fin)b.textContent='Prüfung fortsetzen';if(st.fin)b.textContent='Ergebnis ansehen';
 $('#home').onclick=()=>{
  if(!st.t0||st.fin){location.href='../';return}
  if(confirm('Sie sind mitten in der Prüfung. Jetzt pausieren? Die Uhr stoppt, und Sie machen später an derselben Stelle weiter.')){pauseExam();location.href='../'}};
 $$('.sbtn').forEach(x=>x.onclick=()=>go(x.dataset.t));
 $$('[data-begin]').forEach(x=>x.onclick=()=>{const k=x.dataset.begin;st.began[k]=1;st.talk=st.talk||0;
   if(k==='hoeren'){startHoeren();go('hoeren');return}
   if(k==='sprechen'){setAct('vorb');$('#spprep').hidden=false}
   save();go(k)});
 $('#endcur').onclick=()=>{if(confirm(LAB[cur]+' jetzt beenden? Danach können Sie nichts mehr ändern.'))endSec(cur)};
 $$('[data-endsec]').forEach(x=>x.onclick=()=>{if(confirm('Jetzt beenden? Danach können Sie nichts mehr ändern.'))endSec(x.dataset.endsec)});
 $('#hdone').onclick=()=>{if(confirm('Hören jetzt beenden?'))endSec('hoeren')};
 $('#aplay').onclick=()=>{aud&&aud.play();$('#aplay').hidden=true;aStat('Der Hörtext läuft.')};
 $$('[data-next]').forEach(x=>x.onclick=()=>{const sec=x.closest('section').id;const i=(st.cur[sec]||0)+1;if(i<TK[sec].length)showTask(sec,i);else toast('Das war die letzte Aufgabe in diesem Teil.');window.scrollTo(0,0)});
 $$('[data-prev]').forEach(x=>x.onclick=()=>{const sec=x.closest('section').id;const i=(st.cur[sec]||0)-1;if(i>=0)showTask(sec,i);window.scrollTo(0,0)});
 $$('[data-save]').forEach(x=>x.onclick=()=>{save();const s=x.parentNode.querySelector('.saved');if(s){s.textContent='Gespeichert';setTimeout(()=>s.textContent='',1500)}});
 $('#finish').onclick=openFinish;$('#back').onclick=()=>$('#modal').hidden=true;
 $('#submit').onclick=()=>{$('#modal').hidden=true;finalize()};
 $$('.filter button').forEach(x=>x.onclick=()=>list(x.dataset.f));
 const br=$('#brief');if(br){br.value=st.brief||'';br.oninput=()=>{st.brief=br.value;wc();save()}}
 const cp=$('#copy');if(cp)cp.onclick=()=>copyWriting(cp);
 const ss=$('#ssch'),sp=$('#sspr');
 if(ss){ss.value=st.ssch||'';ss.oninput=()=>{st.ssch=ss.value;save();verdict()}}
 if(sp){sp.value=st.sspr||'';sp.oninput=()=>{st.sspr=sp.value;save();verdict()}}
 const t=$('#sptalkbtn');if(t)t.onclick=setTalk;
 restore();wc();setupAudio();recRows();const cs=$('#copysp');if(cs)cs.onclick=copySprechen;
 document.addEventListener('visibilitychange',()=>{if(document.hidden){commit();save()}});
 window.addEventListener('pagehide',()=>{commit();save()});
 setInterval(tick,250);
}
bind();
if(st.fin&&st.t0){/* Ergebnis wird erst nach „Ergebnis ansehen“ gezeigt */}
})();
