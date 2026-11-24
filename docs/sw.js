
const PAGES='telc-pages-20261124120000', AUDIO='telc-audio-v1';
const PRECACHE=['./','index.html','manifest.webmanifest','icon-192.png','Geschichten/index.html','Geschichten/stories.js','Wortschatz/index.html','Wortschatz/data.js'];
self.addEventListener('install',e=>{self.skipWaiting();e.waitUntil(caches.open(PAGES).then(c=>Promise.all(PRECACHE.map(u=>fetch(u,{cache:'no-cache'}).then(r=>{if(r.ok)return c.put(u,r)}).catch(()=>{})))))});
self.addEventListener('activate',e=>{e.waitUntil((async()=>{for(const k of await caches.keys()){if(k!==PAGES&&k!==AUDIO&&k.indexOf('telc-pages-')===0)await caches.delete(k)}await self.clients.claim()})())});
async function audio(req){
  const c=await caches.open(AUDIO),hit=await c.match(req.url);
  if(!hit)return fetch(req);
  const range=req.headers.get('range');if(!range)return hit;
  const buf=await hit.arrayBuffer(),m=/bytes=(\d*)-(\d*)/.exec(range);
  let s=m&&m[1]!==''?parseInt(m[1],10):0,e=m&&m[2]!==''?parseInt(m[2],10):buf.byteLength-1;
  if(m&&m[1]===''&&m[2]!==''){s=Math.max(0,buf.byteLength-parseInt(m[2],10));e=buf.byteLength-1}
  e=Math.min(e,buf.byteLength-1);
  return new Response(buf.slice(s,e+1),{status:206,statusText:'Partial Content',headers:{'Content-Type':'audio/mpeg','Accept-Ranges':'bytes','Content-Range':'bytes '+s+'-'+e+'/'+buf.byteLength,'Content-Length':String(e-s+1)}})}
async function clean(r){if(!r.redirected)return r;const b=await r.blob();return new Response(b,{status:r.status,statusText:r.statusText,headers:r.headers})}
async function page(req){
  const c=await caches.open(PAGES);
  try{
    const r=await fetch(req.mode==='navigate'?req.url:req,{cache:'no-cache'});
    if(r&&r.ok){const k=await clean(r.clone());c.put(req.url,k.clone()).catch(()=>{});return clean(r)}
    const hit=await c.match(req.url,{ignoreSearch:true});return hit||r
  }catch(e){
    const hit=await c.match(req.url,{ignoreSearch:true});
    return hit||(await c.match('index.html'))||Response.error()
  }}
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET')return;const u=new URL(r.url);if(u.origin!==location.origin)return;
  if(u.pathname.endsWith('.mp3'))e.respondWith(audio(r));
  else if(r.mode==='navigate'||/\.(html|js|css|json|webmanifest|png)$/.test(u.pathname))e.respondWith(page(r))});
