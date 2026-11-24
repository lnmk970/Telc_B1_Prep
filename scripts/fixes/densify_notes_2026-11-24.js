// Add rule-based grammar notes (scripts/expand/auto_rules.js) to S16-S78, up to CAP per rule and story.
// Existing notes and tooltips are never touched. Usage: node scripts/fixes/densify_notes_2026-11-24.js
const fs = require('fs'), path = require('path');
const F = path.join(__dirname, '..', '..', 'docs', 'Geschichten', 'stories.js');
const S = new Function(fs.readFileSync(F, 'utf8') + ';return S')();
const annotate = require('../expand/auto_rules.js');
const CAP = 28;
const count = s => (JSON.stringify(s.s).match(/\[\[[^\]]*?::/g) || []).length;
let before = 0, after = 0, n = 0;
S.forEach((s, i) => { if (i < 15) return; before += count(s); annotate(s.s, CAP); after += count(s); n++; });
fs.writeFileSync(F, 'const S=' + JSON.stringify(S) + ';');
console.log('stories', n, '| notes before', before, '(avg ' + Math.round(before / n) + ') -> after', after, '(avg ' + Math.round(after / n) + ')');
