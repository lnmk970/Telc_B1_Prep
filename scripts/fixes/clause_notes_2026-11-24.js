// Context-specific notes for S16-S78:
//  1) subordinate clauses (weil, dass, wenn, ob, obwohl, damit, bevor, nachdem, falls, sobald): names the verb that ends the clause
//  2) sein-Perfekt: why movement/change verbs take sein (ist gefahren, bin angekommen ...)
//  3) "während" as a preposition (während der Arbeit) is no longer explained as a conjunction
// Replaces the generic automatic notes for these words. Only clear cases are annotated. Usage: node scripts/fixes/clause_notes_2026-11-24.js (idempotent)
const fs = require('fs'), path = require('path');
const FS = path.join(__dirname, '..', '..', 'docs', 'Geschichten', 'stories.js');
const S = new Function(fs.readFileSync(FS, 'utf8') + ';return S')();

const CONJ = new Set(['weil', 'dass', 'wenn', 'ob', 'obwohl', 'damit', 'bevor', 'nachdem', 'falls', 'sobald', 'während']);
const GENERIC_CONJ = /^Subordinate clause opener/;
const GENERIC_PART = /^(Participle \(Partizip II\)|Past participle \(Partizip II\))/;
const SUBJ = new Set(['ich', 'du', 'er', 'sie', 'es', 'wir', 'ihr', 'man', 'alle', 'jeder', 'jemand', 'niemand', 'der', 'die', 'das', 'ein', 'eine', 'mein', 'meine', 'dein', 'deine', 'sein', 'seine', 'ihre', 'unser', 'unsere', 'dieser', 'diese', 'viele', 'wenige', 'beide']);
const DET = new Set(['der', 'die', 'das', 'dem', 'den', 'des', 'ein', 'einem', 'einer', 'einen', 'eines', 'meiner', 'meinem', 'meinen', 'seiner', 'seinem', 'ihrer', 'ihrem', 'dieser', 'diesem', 'jeder', 'jedem', 'unserer', 'unserem']);
const STOP = new Set(['und', 'oder', 'aber', 'dann', 'auch', 'noch', 'schon', 'nicht', 'immer', 'sehr', 'mehr', 'wieder', 'hier', 'dort', 'jetzt', 'heute', 'morgen', 'gern', 'gerne', 'bitte', 'ja', 'nein', 'so', 'denn', 'doch']);
const SEIN = { gefahren: 'fahren', gegangen: 'gehen', gekommen: 'kommen', geflogen: 'fliegen', geblieben: 'bleiben', gelaufen: 'laufen', gereist: 'reisen', gewesen: 'sein', geworden: 'werden', aufgestanden: 'aufstehen', angekommen: 'ankommen', passiert: 'passieren', umgezogen: 'umziehen', abgereist: 'abreisen', eingeschlafen: 'einschlafen', ausgestiegen: 'aussteigen', eingestiegen: 'einsteigen', gestürzt: 'stürzen', gelungen: 'gelingen', gewachsen: 'wachsen', gestorben: 'sterben', abgefahren: 'abfahren', zurückgekommen: 'zurückkommen', vorbeigekommen: 'vorbeikommen', mitgekommen: 'mitkommen', ausgezogen: 'ausziehen', eingezogen: 'einziehen', abgebogen: 'abbiegen', gesprungen: 'springen', gestiegen: 'steigen', gesunken: 'sinken' };
const AUXS = new Set(['bin', 'bist', 'ist', 'sind', 'seid', 'war', 'waren']);
const SEG = /\[\[(.+?)::(.+?)\]\]|\{([^{}|]+)(?:\|([^{}]+))?\}|==/g;
const isW = t => /^[A-Za-zÄÖÜäöüß]+$/.test(t);
const clean = n => n.replace(/\]\]|::/g, ' ');

function tokenize(raw) {
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
  return toks;
}
const wordOf = tk => (tk.kind === 'n' ? tk.t.split(/\s+/).pop() : tk.t);
const endsClause = tk => tk.kind === 'p' && /[,.!?;:“”„)]/.test(tk.t);

function processRow(raw) {
  const toks = tokenize(raw), edits = [];
  for (let k = 0; k < toks.length; k++) {
    const a = toks[k];
    const word = (a.kind === 'p' || a.kind === 'n') && isW(a.t) ? a.t.toLowerCase() : null;
    // ---- 1) subordinate clauses
    if (word && CONJ.has(word) && (a.kind === 'p' || (a.kind === 'n' && GENERIC_CONJ.test(a.note)))) {
      const n1 = toks[k + 1], n2 = toks[k + 2];
      if (word === 'während' && n1 && n1.t === ' ' && n2 && DET.has(wordOf(n2).toLowerCase())) {
        edits.push({ s: a.s, e: a.e, text: '[[' + a.t + '::während is a preposition here (with the genitive, in speech often the dative): während der Arbeit = during work. It is not the conjunction während (= while) and does not send the verb to the end.]]' });
        continue;
      }
      if (word === 'damit' && !(n1 && n1.t === ' ' && n2 && SUBJ.has(wordOf(n2).toLowerCase()))) continue;   // damit = pronoun here
      if (!(n1 && n1.t === ' ')) continue;
      // find the end of the clause
      let j = k + 1, words = [];
      while (j < toks.length && !endsClause(toks[j]) && toks[j].kind !== 'm') { if (toks[j].kind !== 'p' || isW(toks[j].t)) words.push(toks[j]); j++; }
      if (words.length < 3) continue;
      const last = words[words.length - 1], lw = wordOf(last);
      if (!/^[a-zäöüß]{3,}$/.test(lw) || STOP.has(lw) || /^[A-ZÄÖÜ]/.test(lw) || DET.has(lw) || SUBJ.has(lw)) continue;
      const kindNote = { dass: 'dass links a clause to the main sentence', weil: 'weil gives a reason', wenn: 'wenn introduces a condition or a repeated event', ob: 'ob introduces an indirect yes/no question', obwohl: 'obwohl = although', damit: 'damit = so that (purpose)', bevor: 'bevor = before', nachdem: 'nachdem = after', falls: 'falls = in case', sobald: 'sobald = as soon as', während: 'während = while' }[word];
      const hint = word === 'ob' || word === 'dass' ? ' A comma comes before ' + word + '.' : '';
      edits.push({ s: a.s, e: a.e, text: '[[' + a.t + '::' + clean(kindNote + ' and sends the conjugated verb to the end of the clause. Here the verb at the end is ' + lw + '.' + hint) + ']]' });
      continue;
    }
    // ---- 2) sein-Perfekt
    if (word && SEIN[word] !== undefined && (a.kind === 'p' || (a.kind === 'n' && GENERIC_PART.test(a.note)))) {
      let back = 0, found = false;
      for (let b = k - 1; b >= 0 && back < 10; b--) { const t = toks[b]; if (endsClause(t)) break; if ((t.kind === 'p' || t.kind === 'n') && isW(t.t)) { back++; if (AUXS.has(t.t.toLowerCase())) { found = true; break; } } }
      if (!found) continue;
      const inf = SEIN[word];
      edits.push({ s: a.s, e: a.e, text: '[[' + a.t + '::' + clean(a.t + ' is the participle of ' + inf + '. Verbs of movement or change of state form the Perfekt with sein, not haben: ich bin ' + word + '. The participle stands at the end of the clause.') + ']]' });
    }
  }
  edits.sort((x, y) => y.s - x.s).forEach(ed => { raw = raw.slice(0, ed.s) + ed.text + raw.slice(ed.e); });
  return [raw, edits.length];
}

let total = 0;
S.forEach((s, idx) => { if (idx < 15) return; s.s.forEach(r => { if (r[2] === '§') return; const [n, c] = processRow(r[0]); r[0] = n; total += c; }); });
fs.writeFileSync(FS, 'const S=' + JSON.stringify(S) + ';');
console.log('notes written/replaced:', total);
