// Context-specific case notes for S16-S78: article + noun where the noun's gender is known from the word list
// (docs/Wortschatz/data.js) and the case follows from the preposition or from the article form.
// A note is only written when gender, article form and case are consistent; unclear cases are skipped.
// Replaces the generic automatic article notes (einen / einem / einer ...). Usage: node scripts/fixes/case_notes_2026-11-24.js (idempotent)
const fs = require('fs'), path = require('path');
const DOCS = path.join(__dirname, '..', '..', 'docs');
const V = new Function(fs.readFileSync(path.join(DOCS, 'Wortschatz', 'data.js'), 'utf8') + ';return V')();
const FS = path.join(DOCS, 'Geschichten', 'stories.js');
const S = new Function(fs.readFileSync(FS, 'utf8') + ';return S')();

// --- noun -> gender (only unambiguous single words)
const nounG = new Map(), bad = new Set();
V.forEach(v => { if (!/^(der|die|das)$/.test(v[0]) || !/^[A-ZÄÖÜ][a-zäöüß]+$/.test(v[1])) return;
  const k = v[1].toLowerCase(); if (nounG.has(k) && nounG.get(k) !== v[0]) bad.add(k); nounG.set(k, v[0]); });
bad.forEach(k => nounG.delete(k));
const GN = { der: 'masculine', die: 'feminine', das: 'neuter' };

// --- article forms by case and gender
const BASES = ['ein', 'kein', 'mein', 'dein', 'sein', 'ihr', 'unser', 'euer'];
const FORMS = { nom: { der: ['der', 'ein', 'kein', 'mein', 'dein', 'sein', 'ihr', 'unser', 'euer'], die: ['die', 'eine', 'keine', 'meine', 'deine', 'seine', 'ihre', 'unsere', 'eure'], das: ['das', 'ein', 'kein', 'mein', 'dein', 'sein', 'ihr', 'unser', 'euer'] },
  acc: { der: ['den', 'einen', 'keinen', 'meinen', 'deinen', 'seinen', 'ihren', 'unseren', 'euren'], die: ['die', 'eine', 'keine', 'meine', 'deine', 'seine', 'ihre', 'unsere', 'eure'], das: ['das', 'ein', 'kein', 'mein', 'dein', 'sein', 'ihr', 'unser', 'euer'] },
  dat: { der: ['dem', 'einem', 'keinem', 'meinem', 'deinem', 'seinem', 'ihrem', 'unserem', 'eurem'], die: ['der', 'einer', 'keiner', 'meiner', 'deiner', 'seiner', 'ihrer', 'unserer', 'eurer'], das: ['dem', 'einem', 'keinem', 'meinem', 'deinem', 'seinem', 'ihrem', 'unserem', 'eurem'] } };
const DAT = new Set(['mit', 'bei', 'nach', 'von', 'zu', 'aus', 'seit', 'gegenüber', 'außer']);
const ACC = new Set(['für', 'durch', 'ohne', 'gegen', 'um', 'bis']);
const WECH = new Set(['in', 'an', 'auf', 'über', 'unter', 'vor', 'hinter', 'neben', 'zwischen']);
const ALLART = new Set([].concat(...['nom', 'acc', 'dat'].map(c => [].concat(...Object.values(FORMS[c])))));
const TABLE = 'Forms (nominative / accusative / dative): der-nouns {a} · die-nouns {b} · das-nouns {c}.';
const tableFor = a => {
  const base = a.toLowerCase();
  const stem = BASES.find(b => base.startsWith(b) && ALLART.has(base)) || null;
  if (['der', 'die', 'das', 'den', 'dem'].includes(base)) return TABLE.replace('{a}', 'der / den / dem').replace('{b}', 'die / die / der').replace('{c}', 'das / das / dem');
  const st = (base.startsWith('ein') && base !== 'eine' && base.length <= 6) ? 'ein' : (stem || 'ein');
  return TABLE.replace('{a}', st + ' / ' + st + 'en / ' + st + 'em').replace('{b}', st + 'e / ' + st + 'e / ' + st + 'er').replace('{c}', st + ' / ' + st + ' / ' + st + 'em');
};

function decide(art, noun, prep) {
  const g = nounG.get(noun.toLowerCase()); if (!g) return null;
  const a = art.toLowerCase(), N = noun, gn = GN[g];
  const fits = c => FORMS[c][g].includes(a);
  const tab = tableFor(art);
  if (prep && DAT.has(prep)) return fits('dat') ? `${N} is ${gn} (${g} ${N}) and it follows ${prep}, which always takes the dative, so the word is ${art}. ${tab}` : null;
  if (prep && ACC.has(prep)) return fits('acc') ? `${N} is ${gn} (${g} ${N}) and it follows ${prep}, which always takes the accusative, so the word is ${art}.` + (g === 'der' ? ' Only masculine nouns change here: ein becomes einen, der becomes den.' : ' Feminine and neuter nouns look the same in the nominative and the accusative.') + ' ' + tab : null;
  if (prep && WECH.has(prep)) {
    const acc = fits('acc'), dat = fits('dat');
    if (dat && !acc) return `${N} is ${gn} (${g} ${N}); ${prep} is a two-way preposition. Here the form ${art} is dative: it answers wo? (a place) or gives a point in time (an einem Montag, in der Nacht).`;
    if (acc && !dat) return `${N} is ${gn} (${g} ${N}); ${prep} is a two-way preposition. Here the form ${art} is accusative: it answers wohin? (movement) or is required by a fixed pattern (über das Thema sprechen, an das Team schreiben, auf die Nachricht antworten).`;
    return null;
  }
  if (prep) return null;
  if (g === 'der' && FORMS.acc.der.includes(a) && !FORMS.nom.der.includes(a)) return `${N} is masculine (der ${N}) and it is the direct object (accusative), so the word is ${art}. Only masculine nouns change here: ein becomes einen, der becomes den. ${tab}`;
  if ((g === 'der' || g === 'das') && FORMS.dat.der.includes(a)) return `${N} is ${gn} (${g} ${N}) and it is in the dative (indirect object or after a dative verb), so the word is ${art}. ${tab}`;
  return null;
}

const GENERIC = /^(Masculine accusative article form|Dative masculine or neuter article form|Dative feminine article form)/;
const SEG = /\[\[(.+?)::(.+?)\]\]|\{([^{}|]+)(?:\|([^{}]+))?\}|==/g;
const isW = t => /^[A-Za-zÄÖÜäöüß]+$/.test(t);

function processRow(raw) {
  // tokenise: words with their raw ranges and kind
  const toks = []; let i = 0, m; SEG.lastIndex = 0;
  const plain = (a, b) => { const x = raw.slice(a, b); const re = /[A-Za-zÄÖÜäöüß]+|[^A-Za-zÄÖÜäöüß]+/g; let k; while ((k = re.exec(x))) toks.push({ s: a + k.index, e: a + k.index + k[0].length, t: k[0], kind: 'p' }); };
  while ((m = SEG.exec(raw))) {
    plain(i, m.index);
    if (m[1] !== undefined) toks.push({ s: m.index, e: m.index + m[0].length, t: m[1], kind: 'n', note: m[2] });
    else if (m[3] !== undefined) toks.push({ s: m.index, e: m.index + m[0].length, t: m[3], kind: 't' });
    else toks.push({ s: m.index, e: m.index + 2, t: '==', kind: 'm' });
    i = m.index + m[0].length;
  }
  plain(i, raw.length);
  const edits = [];
  for (let k = 0; k < toks.length; k++) {
    const a = toks[k];
    if (!(a.kind === 'p' || a.kind === 'n') || !ALLART.has(a.t.toLowerCase())) continue;
    if (a.kind === 'n' && !GENERIC.test(a.note)) continue;          // keep hand-written notes
    const sp = toks[k + 1], nn = toks[k + 2];
    if (!sp || sp.kind !== 'p' || sp.t !== ' ' || !nn || !(nn.kind === 'p' || nn.kind === 't') || !isW(nn.t) || !/^[A-ZÄÖÜ]/.test(nn.t)) continue;
    // previous word (one space before the article)
    let prep = null; const b = toks[k - 1], c = toks[k - 2];
    if (b && b.kind === 'p' && b.t === ' ' && c && (c.kind === 'p' || c.kind === 'n' || c.kind === 't') && isW(c.t)) prep = c.t.toLowerCase();
    const note = decide(a.t, nn.t, prep);
    if (!note) continue;
    edits.push({ s: a.s, e: a.e, text: '[[' + a.t + '::' + note.replace(/\]\]|::/g, ' ') + ']]' });
  }
  edits.sort((x, y) => y.s - x.s).forEach(ed => { raw = raw.slice(0, ed.s) + ed.text + raw.slice(ed.e); });
  return [raw, edits.length];
}

let total = 0, replaced = 0, stories = 0;
S.forEach((s, idx) => { if (idx < 15) return; stories++;
  s.s.forEach(r => { if (r[2] === '§') return; const had = (r[0].match(/::(?:Masculine accusative article form|Dative masculine or neuter article form|Dative feminine article form)/g) || []).length; const [n, c] = processRow(r[0]); const left = (n.match(/::(?:Masculine accusative article form|Dative masculine or neuter article form|Dative feminine article form)/g) || []).length; r[0] = n; total += c; replaced += had - left; }); });
fs.writeFileSync(FS, 'const S=' + JSON.stringify(S) + ';');
console.log('stories', stories, '| context notes written', total, '(of which replacing generic notes ~' + replaced + ')');
