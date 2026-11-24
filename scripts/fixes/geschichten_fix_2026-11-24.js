// One-off corrections from the Geschichten review (24.11.2026). Safe to re-run.
// Usage: node scripts/fixes/geschichten_fix_2026-11-24.js
const fs = require('fs');
const path = require('path');
const F = path.join(__dirname, '..', '..', 'docs', 'Geschichten', 'stories.js');
const S = new Function(fs.readFileSync(F, 'utf8') + ';return S')();
const log = [];
const deep = (o, fn) => Array.isArray(o) ? o.map(x => deep(x, fn)) : (o && typeof o === 'object') ? Object.fromEntries(Object.entries(o).map(([k, v]) => [k, deep(v, fn)])) : typeof o === 'string' ? fn(o) : o;

// 1) Subject-verb agreement: several subjects -> gefallen (S01-S06, incl. speaking rows)
const R1 = [['Mir gefällt die Größe der Stadt, die Thermen', 'Mir gefallen die Größe der Stadt, die Thermen'], ['mir gefällt die Größe der Stadt, die Thermen', 'mir gefallen die Größe der Stadt, die Thermen']];

// 2) Exam labels: this site prepares telc Deutsch B1, not the DTZ; telc B1 Schreiben has a single task (no "Teil 1")
const R2 = [
  ['Schreiben formell (DTZ Aufgabe A/B) · ', 'Schreiben formell · '],
  ['Schreiben formell (DTZ Aufgabe B) · ', 'Schreiben formell · '],
  ['Schreiben formell (DTZ Aufgabe B: Vermieter) · ', 'Schreiben formell (an den Vermieter) · '],
  ['DTZ Sprechen Teil 2 (Bild beschreiben) · Wechselpräpositionen', 'Wechselpräpositionen · Bild beschreiben (Training, kein Teil der telc-B1-Prüfung)'],
  ['These words are asked again and again in DTZ.', 'These words come up again and again in telc letters and reading texts.'],
  ['Schreiben informell (telc Teil 1: Rat geben)', 'Schreiben informell (telc: Rat geben)'],
  ['Schreiben informell (telc Teil 1)', 'Schreiben informell (telc)'],
  ['A good introduction (telc Teil 1) has six points', 'A good introduction (telc Sprechen Teil 1) has six points'],
  ['The four Leitpunkte of telc Teil 1 usually ask for exactly these.', 'The four Leitpunkte of the telc writing task usually ask for exactly these.'],
  ['In telc Teil 1 these are your four Leitpunkte.', 'In the telc writing task these are your four Leitpunkte.'],
  ['Hören · Sprechen Teil 3 (Termin vereinbaren)', 'Hören · Sprechen Teil 3 (gemeinsam einen Termin planen)'],
];
const rep = s => { let t = s; for (const [a, b] of R1.concat(R2)) if (t.includes(a)) { t = t.split(a).join(b); log.push(a.slice(0, 50)); } return t; };
for (let i = 0; i < S.length; i++) S[i] = deep(S[i], rep);

// 3) S01-S06: the weil-sentence gave a non-reason ("I speak English ... because Telugu is my mother tongue")
for (const s of S.slice(0, 6)) {
  const r = s.s[14];
  const old = 'Ich {spreche|sprechen} Englisch, Telugu und ein {bisschen|bisschen} Deutsch, ';
  if (r && r[0].startsWith(old)) {
    r[0] = 'Ich {spreche|sprechen} Telugu, ' + r[0].slice(old.length).replace(']]== Telugu [[meine::', ']]== es [[meine::') + ' Außerdem spreche ich Englisch und ein {bisschen|bisschen} Deutsch.';
    r[1] = 'I speak Telugu because it is my mother tongue. I also speak English and a little German.';
    log.push(s.id + ' weil-Satz');
  }
}

// 4) S32: spoken German uses the Perfekt, not the Präteritum (except war, hatte, modal verbs)
const s32 = S.find(x => x.id === 'S32');
const set = (i, de, en, test) => { if (s32.s[i] && test.test(s32.s[i][0])) { s32.s[i][0] = de; s32.s[i][1] = en; log.push('S32 row ' + i); } };
set(14, 'Vor [[einem::Dative masculine or neuter article form: einem / keinem, usually after mit, bei, von or nach.]] {Jahr|jahr} [[habe::Perfekt with haben: habe … gesehen. When you speak, use the Perfekt for the past.]] ich [[einen::Masculine accusative article form: einen / keinen is used for der-nouns used as the direct object.]] {Unfall|unfall} an [[einer::Dative feminine article form: einer / keiner, after mit, bei, von or in.]] {Kreuzung|kreuzung} [[gesehen::sehen - sah - gesehen. In a newspaper text you read sah, when you speak you say habe gesehen.]]. Ich habe {sofort|sofort} [[geholfen::helfen - half - geholfen.]].', 'A year ago I saw an accident at a junction. I helped at once.', /sah::/);
set(22, 'Manoj: Ja, [[letztes::letzt-, neuter accusative: letztes Jahr = last year.]] {Jahr|jahr} habe ich [[einen::Masculine accusative article form: einen / keinen is used for der-nouns used as the direct object.]] {Unfall|unfall} am {Bahnhof|bahnhof} [[gesehen::Perfekt in speech: habe … gesehen (not: sah).]].', 'Manoj: Yes, last year I saw an accident at the station.', /sah::/);
set(23, 'Anna: Und was [[hast::Perfekt: hast … gemacht. In conversation people ask in the Perfekt, not with tatst.]] du [[gemacht::machen - machte - gemacht.]]?', 'Anna: And what did you do?', /tatst/);
set(24, 'Manoj: Ich habe {sofort|sofort} den {Notruf|notruf} [[gewählt::den Notruf wählen = to call the emergency number (112).]] und [[bin::bleiben takes sein in the Perfekt: bin geblieben.]] [[bei::Preposition with the dative: this word always takes the dative case.]] der {Person|person} geblieben.', 'Manoj: I called the emergency number at once and stayed with the person.', /rief::/);
set(25, 'Tipp: Wenn Sie sprechen, {erzählen|erzählen} [[Sie::Formal you (Sie): the verb agrees with the third person plural.]] im ==Perfekt==: ich habe gesehen, ich bin geblieben. Das Präteritum (sah, half, rief) müssen Sie in Zeitungstexten erkennen. Beim Sprechen benutzt man nur war, hatte und die Modalverben im Präteritum.', 'Tip: when you speak, tell the story in the Perfekt. You need to recognise the Präteritum (sah, half, rief) in newspaper texts. In speech only war, hatte and the modal verbs are used in the Präteritum.', /Präteritum\. Das klingt/);
const pvFix = { 1: ['vor einem Jahr habe ich einen Unfall an einer Kreuzung gesehen. Ich habe sofort geholfen.', 'Vor einem Jahr habe ich einen Unfall an einer Kreuzung gesehen. Ich habe sofort geholfen.'], 3: ['letztes Jahr habe ich einen Unfall am Bahnhof gesehen. Ich habe sofort den Notruf gewählt.', 'Letztes Jahr habe ich einen Unfall am Bahnhof gesehen. Ich habe sofort den Notruf gewählt.'] };
for (const [i, [low, up]] of Object.entries(pvFix)) {
  const r = s32.x.pv[i];
  if (r && /sah/.test(r[2])) { r[0] = 'Peter, ' + low; r[1] = 'Anna, ' + low; r[2] = up; r[3] = r[3].replace('called the emergency number', 'called the emergency number'); log.push('S32 pv ' + i); }
}

fs.writeFileSync(F, 'const S=' + JSON.stringify(S) + ';');
console.log(log.length + ' changes'); console.log([...new Set(log)].join('\n'));
