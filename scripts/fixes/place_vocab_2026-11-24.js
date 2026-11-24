// Place vocabulary that is in no story yet (docs/Wortschatz/data.js) into the best-fitting story of S16-S78:
// its example sentence (German + English from data.js) is added to the story's "Neue Wörter in Sätzen" section
// with a tooltip, and the word is added to the story's word lists (w, rv). Story tags in data.js are updated.
// Usage: node scripts/fixes/place_vocab_2026-11-24.js   (idempotent: only words not yet covered are placed)
const fs = require('fs');
const path = require('path');
const DOCS = path.join(__dirname, '..', '..', 'docs');
const FV = path.join(DOCS, 'Wortschatz', 'data.js'), FS = path.join(DOCS, 'Geschichten', 'stories.js');
const V = new Function(fs.readFileSync(FV, 'utf8') + ';return V')();
const S = new Function(fs.readFileSync(FS, 'utf8') + ';return S')();
const CAP = 40;

const strip = t => String(t).replace(/\[\[([^\]]*?)::[^\]]*?\]\]/g, '$1').replace(/\{([^}|]*)\|[^}]*\}/g, '$1').replace(/==|\*\*/g, '');
const tok = t => (String(t).toLowerCase().match(/[a-zäöüß]{3,}/g) || []);
const norm = w => w.replace(/ä/g, 'a').replace(/ö/g, 'o').replace(/ü/g, 'u').replace(/ß/g, 'ss');
const baseOf = v => v[1].split(/ [–(\/,]/)[0].trim();

// --- uncovered words that have a German and an English example sentence
const covered = new Set(); S.forEach(s => Object.keys(s.w).forEach(k => covered.add(k.toLowerCase())));
const todo = V.map((v, i) => [v, i]).filter(([v]) => !covered.has(v[1].toLowerCase()) && v[6] && v[7]);
console.log('uncovered with example:', todo.length);

// --- tf-idf topic vectors
const storyIdx = S.map((s, i) => i).filter(i => i >= 15);            // S16-S78
const docOf = s => tok(s.s.map(r => strip(r[0]) + ' ' + strip(r[1])).join(' ') + ' ' + s.t + ' ' + s.te);
const sdocs = storyIdx.map(i => docOf(S[i]));
const df = new Map(); sdocs.forEach(d => new Set(d).forEach(w => df.set(w, (df.get(w) || 0) + 1)));
const N = sdocs.length, idf = w => (df.has(w) && df.get(w) / N <= 0.35) ? Math.log(N / df.get(w)) : (df.has(w) ? 0 : 0.8);
const vec = d => { const m = new Map(); d.forEach(w => m.set(w, (m.get(w) || 0) + 1)); const o = new Map(); let n2 = 0; m.forEach((c, w) => { const x = (1 + Math.log(c)) * idf(w); if (x > 0) { o.set(w, x); n2 += x * x; } }); return { o, n: Math.sqrt(n2) || 1 }; };
const sv = sdocs.map(vec);
const cos = (a, b) => { let s = 0; const [x, y] = a.o.size < b.o.size ? [a, b] : [b, a]; x.o.forEach((v, w) => { if (y.o.has(w)) s += v * y.o.get(w); }); return s / (a.n * b.n); };

const scored = todo.map(([v, i]) => {
  const wv = vec(tok([v[1], v[6], v[7], v[3], v[8]].join(' ')));
  const sc = sv.map(s => cos(wv, s));
  return { v, i, sc, best: Math.max(...sc) };
}).sort((a, b) => b.best - a.best);

// --- greedy assignment with a cap per story
const load = new Array(storyIdx.length).fill(0), assign = [];
scored.forEach(w => {
  const order = w.sc.map((s, k) => [s, k]).sort((a, b) => b[0] - a[0]);
  for (const [s, k] of order) if (load[k] < CAP) { load[k]++; assign.push([w, storyIdx[k]]); break; }
});

// --- surface form of the word in its example sentence
const PREF = ['zusammen', 'zurück', 'weiter', 'heraus', 'herein', 'hinaus', 'hinein', 'voraus', 'vorbei', 'durch', 'fest', 'mit', 'nach', 'weg', 'auf', 'aus', 'bei', 'ein', 'her', 'hin', 'vor', 'zu', 'ab', 'an', 'um'];
function surface(sentence, v) {
  const base = baseOf(v), bl = norm(base.toLowerCase());
  const words = [...sentence.matchAll(/[A-Za-zÄÖÜäöüß]+/g)].map(m => ({ w: m[0], i: m.index }));
  const stems = [bl];
  if (v[4] === 'v') PREF.forEach(p => { if (bl.startsWith(p) && bl.length - p.length >= 4) stems.push(bl.slice(p.length)); });
  const plural = (v[2] || '').split(/[,;]/)[0].trim().toLowerCase();
  let best = null, bs = 0;
  words.forEach(({ w, i }) => {
    const t = norm(w.toLowerCase());
    let sc = 0;
    if (w.toLowerCase() === base.toLowerCase() || (plural && w.toLowerCase() === plural)) sc = 100;
    else stems.forEach(st => { let p = 0; while (p < st.length && p < t.length && st[p] === t[p]) p++; if (p >= 4 && p >= Math.min(st.length - 2, t.length - 1) - (v[4] === 'v' ? 1 : 0) && p / st.length >= 0.6) sc = Math.max(sc, 10 + p); });
    if (sc > bs) { bs = sc; best = { w, i }; }
  });
  return best;
}

// --- apply
let added = 0, tooltips = 0, noSurface = 0;
const perStory = {};
assign.forEach(([w, si]) => {
  const v = w.v, s = S[si], key = v[1].toLowerCase();
  if (s.w[key]) return;
  let de = v[6];
  const sf = surface(de, v);
  const marks = [];
  if (sf) { marks.push([sf.i, sf.w, key]); } else noSurface++;
  // extra tooltips: other words of the sentence that already exist in this story's word list
  for (const m of de.matchAll(/[A-Za-zÄÖÜäöüß]+/g)) {
    const k = m[0].toLowerCase();
    if (k !== key && s.w[k] && !marks.some(x => x[0] === m.index) && marks.length < 4) marks.push([m.index, m[0], k]);
  }
  marks.sort((a, b) => b[0] - a[0]).forEach(([i, ww, k]) => { de = de.slice(0, i) + '{' + ww + '|' + k + '}' + de.slice(i + ww.length); tooltips++; });
  // exam phrases must be highlighted (checked by scripts/check_geschichten.js)
  de = de.replace(/(Ich finde|Meiner Meinung nach|Ein Vorteil ist|Ein Nachteil ist|Zum Beispiel)/, '==$1==');
  // insert the row at the end of the "Neue Wörter in Sätzen" section
  const h = s.s.findIndex(r => r[0] === 'Neue Wörter in Sätzen' && r[2] === '§');
  let e = h + 1; while (e < s.s.length && s.s[e][2] !== '§') e++;
  s.s.splice(e, 0, [de, v[7], '']);
  const entry = [v[0] || '', v[1], v[3], v[2] || '', v[4]];
  s.w[key] = entry; if (s.rv) s.rv[key] = entry;
  const tag = V[w.i][11];
  V[w.i][11] = tag ? (tag.split(',').includes(s.id) ? tag : tag + ',' + s.id) : s.id;
  added++; perStory[s.id] = (perStory[s.id] || 0) + 1;
});
fs.writeFileSync(FS, 'const S=' + JSON.stringify(S) + ';');
fs.writeFileSync(FV, 'const V=' + JSON.stringify(V) + ';');
const counts = Object.values(perStory);
console.log('placed', added, 'words; tooltips added', tooltips, '; sentences without a tooltip for the new word', noSurface);
console.log('per story: min', Math.min(...counts), 'max', Math.max(...counts), 'stories touched', counts.length);
