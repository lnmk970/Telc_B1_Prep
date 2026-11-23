// Consistency check for docs/Geschichten/stories.js (S01-S15 exam-prep rules).
// Run: node scripts/check_geschichten.js
const fs = require('fs');
const path = require('path');
const file = path.join(__dirname, '..', 'docs', 'Geschichten', 'stories.js');
const S = (new Function(fs.readFileSync(file, 'utf8') + ';return S'))();
let problems = 0;
const fail = (id, msg) => { problems++; console.log(`✗ ${id}: ${msg}`); };
for (const s of S) {
  const raw = JSON.stringify(s);
  const k = parseInt(s.id.slice(1), 10);
  // 1. Partner names: Teil 3 partner Peter, Teil 2 partner Anna; no old names left
  if (/\bTom\b/.test(raw)) fail(s.id, 'old partner name Tom still present');
  const speakers = new Set(s.s.filter(p => p[2] !== '§').map(p => (p[1].match(/^(\w+):/) || [])[1]).filter(Boolean));
  for (const sp of ['Lena','Julia','Sophie','Marie','Felix','Nina','Clara','Paul','Jan','Laura','Max','Sara','Tim']) {
    if (speakers.has(sp)) fail(s.id, `dialogue speaker ${sp} should be Anna`);
  }
  // 2. Examiner exchange block before Schreiben
  const hasPrüfer = s.s.some(p => p[0].startsWith('Prüfer:'));
  if (!hasPrüfer) fail(s.id, 'no examiner (Prüfer:) line in the dialogue');
  // 3. Speaking table: Teil 1 only S01-S06; two three-version rows added
  if (!s.x) { fail(s.id, 'no exam-prep block (x)'); continue; }
  const rows = s.x.sp || [];
  if (rows.length < 2) fail(s.id, 'speaking table has fewer than 2 story rows');
  for (const r of rows) {
    if (r.length !== 4 || r.slice(0, 3).some(c => !c)) { fail(s.id, 'row without male/female/examiner version'); break; }
    if (!/\bPeter\b/.test(r[0]) || !/\bAnna\b/.test(r[1])) { fail(s.id, 'row names not Peter (er) / Anna (sie)'); break; }
  }
  // 4. Schreiben checklist (4 points + Anrede/Gruß) and 3 self-check questions
  if (!s.x.sc || s.x.sc.length < 5) fail(s.id, 'Schreiben checklist too short');
  if (!s.x.q || s.x.q.length !== 3) fail(s.id, 'self-check must have 3 questions');
  // 5. Exam phrases highlighted in every dialogue sentence that contains one
  const unmarked = s.s.filter(p => p[2] !== '§' && /Ich finde|Meiner Meinung nach|Ein Vorteil ist|Ein Nachteil ist|Zum Beispiel/.test(p[0].replace(/==/g, '')) && !/==/.test(p[0]));
  if (unmarked.length) fail(s.id, `${unmarked.length} sentence(s) with exam phrases not highlighted`);
}
console.log(problems ? `${problems} problem(s) found` : 'All stories passed the checks');
process.exit(problems ? 1 : 0);
