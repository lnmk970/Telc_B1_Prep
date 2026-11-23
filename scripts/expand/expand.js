// Usage: node expand.js <content.js> <out.js>
// Applies C.ann ([phrase, note] pairs: first unannotated occurrence becomes [[phrase::note]]),
// inserts C.extra rows before the "Prüfer-Gespräch" header and appends C.pvx rows to the speaking table.
const fs = require('fs');
const path = require('path');
const C = JSON.parse(JSON.stringify(require(path.resolve(process.argv[2]))));
const E = require(path.resolve(process.argv[3]));
C.ann = E.ann; C.extra = E.extra; C.pvx = E.pvx;
const out = process.argv[4];
const rep = [];
const noteRanges = t => { const r = []; const re = /\[\[[^\]]*?::[^\]]*?\]\]/g; let m; while ((m = re.exec(t))) r.push([m.index, m.index + m[0].length]); return r; };
let intro = C.intro;
const { findPhrase } = require(path.resolve(__dirname, 'expand_core.js'));
for (const [ph, note] of (C.ann || [])) {
  let done = false;
  for (const row of intro) {
    if (done || row[2] === '§') continue;
    const t = row[0];
    const pos = findPhrase(t, ph, noteRanges(t));
    if (pos) {
      row[0] = t.slice(0, pos[0]) + '[[' + t.slice(pos[0], pos[1]) + '::' + note.replace(/\]\]|::/g, ' ') + ']]' + t.slice(pos[1]);
      done = true; break;
    }
  }
  if (!done) rep.push('not found: ' + ph);
}
if (C.extra && C.extra.length) {
  const pIdx = intro.findIndex(r => /^Prüfer-Gespräch/.test(r[0]));
  if (pIdx < 0) throw new Error(C.id + ': no examiner header');
  intro = [...intro.slice(0, pIdx), ...C.extra, ...intro.slice(pIdx)];
}
const autoAnnotate = require(path.resolve(__dirname, 'auto_rules.js'));
intro = autoAnnotate(intro, 6);
C.intro = intro;
C.pv = [...C.pv, ...(C.pvx || [])];
delete C.ann; delete C.extra; delete C.pvx;
fs.writeFileSync(out, 'module.exports=' + JSON.stringify(C) + ';');
console.log(C.id + ': notes ' + (intro.map(r => r[0]).join(' ').match(/\[\[/g) || []).length + ', rows ' + intro.length + ', pv ' + C.pv.length + (rep.length ? ' | ' + rep.join('; ') : ''));
