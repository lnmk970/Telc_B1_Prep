
const PAGES='telc-pages-20261112112833', AUDIO='telc-audio-v1';
self.addEventListener('install',e=>{self.skipWaiting();e.waitUntil(caches.open(PAGES).then(c=>c.addAll(['./','index.html','manifest.webmanifest','icon-192.png'])).catch(()=>{}))});
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
async function page(req){
  const c=await caches.open(PAGES),hit=await c.match(req,{ignoreSearch:true});
  const net=fetch(req).then(r=>{if(r&&r.ok&&r.type==='basic')c.put(req,r.clone());return r}).catch(()=>null);
  if(hit){net.catch(()=>{});return hit}
  const r=await net;return r||(await c.match('index.html'))||Response.error()}
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET')return;const u=new URL(r.url);if(u.origin!==location.origin)return;
  if(u.pathname.endsWith('.mp3'))e.respondWith(audio(r));
  else if(r.mode==='navigate'||/\.(html|json|webmanifest|png)$/.test(u.pathname))e.respondWith(page(r))});
