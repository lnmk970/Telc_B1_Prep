// Rewrites "Sprechen Teil 2" in 17 stories (official telc format), uses the official task wording
// in every Teil 2 section, and corrects wrong automatic grammar notes (zu, Sie, separable mit/aus).
// Usage: node scripts/fixes/teil2_rewrite.js   (idempotent for the note fixes; the rewrite replaces whole sections)
const fs = require('fs');
const path = require('path');
const F = path.join(__dirname, '..', '..', 'docs', 'Geschichten', 'stories.js');
const S = new Function(fs.readFileSync(F, 'utf8') + ';return S')();
const C = require('./teil2_content.js');
const autoAnnotate = require('../expand/auto_rules.js');
const strip = t => String(t).replace(/\[\[([^\]]*?)::[^\]]*?\]\]/g, '$1').replace(/\{([^}|]*)\|[^}]*\}/g, '$1').replace(/==/g, '');
const stats = { sections: 0, pv: 0, aufgabe: 0, zuInf: 0, zuToo: 0, sep: 0, sie: 0 };

const aufgabe = topic => [
  'Aufgabe: Sie haben in einer Zeitschrift etwas zum Thema „' + topic + '“ gelesen. Berichten Sie Ihrer Partnerin darüber. Ihre Partnerin hat eine andere Meinung gelesen. Sprechen Sie dann zusammen über das Thema: Sagen Sie Ihre Meinung und erzählen Sie von eigenen Erfahrungen.',
  'Task: you read something about “' + topic + '” in a magazine. Tell your partner about it. Your partner read a different opinion. Then talk about the topic together: give your opinion and talk about your own experiences.',
  'Aufgabe'];

// vocabulary tooltips {Word|lemma} for words in the story's word list
function tooltips(t, w) {
  const keys = new Set(Object.keys(w || {}));
  return t.replace(/(\[\[[^\]]*\]\])|([A-Za-zÄÖÜäöüß]{3,})/g, (m, note, word, off) => {
    if (note) return note;
    if (/(Herrn?|Frau) $/.test(t.slice(0, off).slice(-6))) return word; // surnames such as Keller, Schneider
    const k = word.toLowerCase();
    return keys.has(k) ? '{' + word + '|' + k + '}' : word;
  });
}

// 1) rewrite the 17 sections
for (const [id, c] of Object.entries(C)) {
  const s = S.find(x => x.id === id);
  // locate the section by its Text A row (some headers were mislabelled as Teil 1 or Teil 3)
  const a = s.s.findIndex(r => r[2] !== '§' && /^Text A/.test(strip(r[0])));
  if (a < 0) throw new Error(id + ': no Text A row');
  let h = a; while (h >= 0 && s.s[h][2] !== '§') h--;
  if (h < 0) throw new Error(id + ': no header above Text A');
  let e = h + 1; while (e < s.s.length && s.s[e][2] !== '§') e++;
  const old = new Set(s.s.slice(h + 1, e).map(r => strip(r[0]).replace(/^[A-ZÄÖÜ][a-zäöü]+: /, '')));
  const rows = [
    ['Text A – ' + c.A[0] + ': „' + c.A[1] + '“', 'Text A – ' + c.A[2], 'Text A'],
    ['Text B – ' + c.B[0] + ': „' + c.B[1] + '“', 'Text B – ' + c.B[2], 'Text B'],
    aufgabe(c.topic),
    ['Zusammenfassung: ' + c.sum[0], 'Summary: ' + c.sum[1], 'Zusammenfassung'],
    [c.thema[0], c.thema[1], 'Thema'],
    ...c.rows.map(r => [r[0], r[1], r[2]]),
    ...c.dialog.map(r => [r[0], r[1], 'Dialog']),
    [c.tipp[0], c.tipp[1], 'Tipp']];
  rows.forEach(r => { r[0] = tooltips(r[0], s.w); });
  autoAnnotate(rows, 3);
  const head = [c.header || ('Sprechen Teil 2 (telc) · ' + c.topic), 'Part 2 (telc): report on your opinion text, then discuss the topic with your partner.', '§'];
  s.s.splice(h, e - h, head, ...rows);
  stats.sections++;
  // speaking table: replace rows that quoted the old section
  let k = 0;
  s.x.pv.forEach((r, i) => {
    if (k < c.pv.length && old.has(r[2])) {
      const [de, en, qdu, qsie] = c.pv[k++];
      const low = de.charAt(0).toLowerCase() + de.slice(1);
      s.x.pv[i] = ['Peter, ' + low, 'Anna, ' + low, de, en, 'Peter, ' + qdu.charAt(0).toLowerCase() + qdu.slice(1), 'Anna, ' + qdu.charAt(0).toLowerCase() + qdu.slice(1), qsie];
      stats.pv++;
    }
  });
  while (k < c.pv.length) { // no old row matched: append
    const [de, en, qdu, qsie] = c.pv[k++];
    const low = de.charAt(0).toLowerCase() + de.slice(1);
    s.x.pv.push(['Peter, ' + low, 'Anna, ' + low, de, en, 'Peter, ' + qdu.charAt(0).toLowerCase() + qdu.slice(1), 'Anna, ' + qdu.charAt(0).toLowerCase() + qdu.slice(1), qsie]);
    stats.pv++;
  }
}

// 2) official task wording in every remaining Teil 2 section
for (const s of S) s.s.forEach((r, i) => {
  const m = strip(r[0]).match(/^Aufgabe: Sie bekommen zwei Meinungen zum Thema „([^“]+)“/);
  if (m) { s.s[i] = aufgabe(m[1]); stats.aufgabe++; }
});

// 3) correct wrong automatic notes
const ZU_INF = 'zu + infinitive: here zu is not a preposition. After expressions like Zeit haben, versuchen, es ist schwer … the verb goes to the end with zu in front of it.';
const ZU_TOO = 'zu + adjective or adverb = too: zu viel (too much), zu spät (too late), zu teuer (too expensive). Here zu is not a preposition.';
const SEP = 'Separable verb prefix (mitkommen, mitnehmen, ausrechnen …): in a main clause the prefix goes to the end of the clause. It is not a preposition here.';
const SHE = 'Sie = she here (it is written with a capital only because it starts the sentence). It refers to a woman or a feminine noun mentioned before; the verb has the er/sie/es form.';
const THEY = 'Sie = they here (it is written with a capital only because it starts the sentence). It refers to several people mentioned before; the verb has the plural form.';
const TOO = new Set('viel viele wenig wenige teuer lang lange laut spät früh kurz schwer müde langsam anstrengend groß klein hoch weit alt jung kalt heiß schnell voll eng leise dunkel schwierig stressig gefährlich'.split(' '));
const NOT_INF = new Set('den einen meinen deinen seinen ihren unseren euren allen vielen verschiedenen anderen wenigen beiden diesen jeden keinen guten neuen kleinen großen alten eigenen'.split(' '));
const nextWord = rest => { const m = rest.match(/^\s*(?:==)?\s*(?:\{([^|}]+)\||\[\[([^:\]]+)::|([A-Za-zÄÖÜäöüß]+))/); return m ? (m[1] || m[2] || m[3]) : ''; };
for (const s of S) s.s.forEach((r, ri) => {
  if (r[2] === '§') return;
  let t = r[0];
  t = t.replace(/\[\[(zu|mit|aus)::([^\]]*)\]\]/g, (all, w, note, off) => {
    const nx = nextWord(t.slice(off + all.length));
    if (w === 'zu') {
      if (TOO.has(nx)) { stats.zuToo++; return '[[zu::' + ZU_TOO + ']]'; }
      if ((/^[a-zäöüß]+(en|ern|eln)$/.test(nx) && !NOT_INF.has(nx)) || nx === 'sein' || nx === 'tun') { stats.zuInf++; return '[[zu::' + ZU_INF + ']]'; }
      return all;
    }
    if (/^(ins|herein|anpacken|und|oder)$/.test(nx)) { stats.sep++; return '[[' + w + '::' + SEP + ']]'; }
    return all;
  });
  t = t.replace(/\[\[Sie::Formal you[^\]]*\]\]/g, (all, off) => {
    const before = strip(t.slice(0, off));
    // only sentence-initial Sie in a dialogue line ("Manoj: …")
    if (!/^[A-ZÄÖÜ][a-zäöü]+( [A-ZÄÖÜ][a-zäöü]+)?: /.test(strip(t))) return all;
    if (!/(^[A-ZÄÖÜ][a-zäöü]+( [A-ZÄÖÜ][a-zäöü]+)?: |[.!?]\s)$/.test(before)) return all;
    const nx = nextWord(t.slice(off + all.length));
    // formal Sie always takes the -en verb form; a verb in -t/-e etc. proves "she".
    if (/en$/.test(nx)) {
      if (/zwei Kollegen aus der Abteilung\.\s$/.test(before) && nx === 'interessieren') { stats.sie++; return '[[Sie::' + THEY + ']]'; }
      return all;
    }
    stats.sie++;
    return '[[Sie::' + SHE + ']]';
  });
  r[0] = t;
});

fs.writeFileSync(F, 'const S=' + JSON.stringify(S) + ';');
console.log(JSON.stringify(stats));
