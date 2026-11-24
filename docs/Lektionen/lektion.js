
(function(){
const K='telc_L-'+LID;
function setL(l){document.body.dataset.l=l;document.querySelectorAll('.lang button').forEach(b=>b.classList.toggle('on',b.dataset.l===l));try{localStorage.setItem('telc_lang',l)}catch(e){}}
let l0='both';try{l0=localStorage.getItem('telc_lang')||'both'}catch(e){}if(!/^(both|de|en)$/.test(l0))l0='both';
document.querySelectorAll('.lang button').forEach(b=>b.onclick=()=>setL(b.dataset.l));setL(l0);
let voice=null;function pick(){const v=(window.speechSynthesis&&speechSynthesis.getVoices())||[];voice=v.find(x=>/^de(-|_)DE/i.test(x.lang))||v.find(x=>/^de/i.test(x.lang))||null}
if(window.speechSynthesis){pick();speechSynthesis.onvoiceschanged=pick}
const slug=t=>t.toLowerCase().replace(/ä/g,'ae').replace(/ö/g,'oe').replace(/ü/g,'ue').replace(/ß/g,'ss').replace(/[^a-z0-9]+/g,'_').replace(/^_|_$/g,'');
function browserSay(t){if(!window.speechSynthesis){alert('Dein Browser kann keine Wörter vorlesen.');return}
  speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(t);u.lang='de-DE';u.rate=.85;if(voice)u.voice=voice;speechSynthesis.speak(u)}
document.addEventListener('click',e=>{const b=e.target.closest('.say');if(!b)return;const t=b.dataset.t;let used=false;
  const fb=()=>{if(used)return;used=true;browserSay(t)};
  try{const a=new Audio('audio/'+slug(t)+'.mp3');a.onerror=fb;const p=a.play();if(p&&p.catch)p.catch(fb)}catch(x){fb()}});
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
