// Finds phrase in row text ignoring "==" markers; returns [start,end) in the original text or null.
// Skips matches inside existing [[...]] notes and matches that would straddle a "==" marker.
function findPhrase(t, ph, ranges) {
  const map = []; let s2 = '';
  for (let i = 0; i < t.length; ) {
    if (t[i] === '=' && t[i + 1] === '=') { i += 2; continue; }
    map.push(i); s2 += t[i]; i++;
  }
  let from = 0;
  while (true) {
    const k = s2.indexOf(ph, from);
    if (k < 0) return null;
    const a = map[k], b = map[k + ph.length - 1] + 1;
    const inside = ranges.some(([x, y]) => a < y && b > x);
    const straddle = t.slice(a, b).includes('==');
    if (!inside && !straddle) return [a, b];
    from = k + 1;
  }
}
module.exports = { findPhrase };
