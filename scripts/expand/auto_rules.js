// Rule-based grammar notes applied automatically (max 2 per story per rule, first occurrences outside existing notes).
const RULES = [
  [/\b(dass|weil|wenn|ob|obwohl|damit|nachdem|bevor|während|sobald|falls)\b/, 'Subordinate clause opener: the conjugated verb goes to the end of the clause.'],
  [/\b(muss|müssen|musst|müsst|kann|können|kannst|könnt|soll|sollen|sollst|sollt|darf|dürfen|will|wollen|willst|möchte|möchten|möchtest)\b/, 'Modal verb: the main verb stays in the infinitive and goes to the end of the clause.'],
  [/\b(sollte|sollten|könnte|könnten|würde|würden|hätte|hätten|wäre|wären|würdest|könntest|solltest)\b/, 'Konjunktiv II (would / could / should): used for polite wishes, advice and hypotheses.'],
  [/\b(mit|bei|aus|von|nach|seit)\b(?= (?:de[mnr]|ein(?:em|er)|mein(?:em|er)|dein(?:em|er)|sein(?:em|er)|ihr(?:em|er)|unser(?:em|er)|[A-ZÄÖÜ]))/, 'Preposition with the dative: this word always takes the dative case.'],
  [/\b(für|ohne|durch|gegen)\b/, 'Preposition with the accusative: this word always takes the accusative case.'],
  [/\b(einen|keinen)\b/, 'Masculine accusative article form: einen / keinen is used for der-nouns used as the direct object.'],
  [/\b(einem|keinem)\b/, 'Dative masculine or neuter article form: einem / keinem, usually after mit, bei, von or nach.'],
  [/\b(einer|keiner)\b/, 'Dative feminine article form: einer / keiner, after mit, bei, von or in.'],
  [/\b(nicht)\b/, 'Nicht negates a verb or an adjective. Kein is used for nouns.'],
  [/\b(kein|keine)\b/, 'Negative article: kein / keine replaces ein / eine in the negative.'],
  [/\b(sich)\b/, 'Reflexive pronoun: it refers back to the subject (er, sie, es, man, sie).'],
  [/\b(ihm|ihnen|mir|dir)\b/, 'Dative pronoun: to me / you / him / them. Many verbs take the dative, e.g. helfen, gefallen, gehören.'],
  [/\b(mich|dich|uns|euch)\b/, 'Accusative pronoun: the object of the verb (me, you, us, you-plural).'],
  [/\b(aber)\b/, 'Aber does not change the word order: the verb stays in second place in the main clause.'],
  [/\b(denn|deshalb|deswegen|darum)\b/, 'Connector: the verb stays in second place after denn, or follows the connector directly after deshalb.'],
  [/\b(trotzdem|außerdem|danach|dann|zuerst|zuletzt|inzwischen|seitdem)\b/, 'Connector or time adverb: when placed first, the verb comes straight after it.'],
  [/\b(am besten|am meisten|am liebsten|am wichtigsten|am schönsten|am schnellsten)\b/, 'Am + superlative: used as an adverb, meaning most / best.'],
  [/\b(besser|mehr|weniger|schneller|länger|wichtiger|größer|kleiner|ruhiger)\b/, 'Comparative: -er after the adjective, used with als or after ist without an ending.'],
  [/\b(sehr|ziemlich|besonders)\b/, 'Intensifier placed before an adjective or adverb: sehr schön = very nice.'],
  [/\b(wegen|während)\b/, 'Preposition with the genitive (in writing) or dative (in speech): wegen / während.'],
  [/\b(gern|gerne)\b/, 'Gern: an adverb meaning with pleasure. Ich mache das gern = I like doing that.'],
  [/\b(bitte)\b/, 'Bitte = please, often at the end of a request or at the beginning of a polite phrase.'],
  [/(?<![.!?:]\s|^)\b(Sie)\b(?= [a-zäöü]+en\b)/, 'Formal you (Sie): the verb agrees with the third person plural.'],
  [/\b(gehabt|gewesen|gemacht|gegangen|gekommen|gesehen|gelesen)\b/, 'Participle (Partizip II): used with haben or sein in the Perfekt, placed at the end of the clause.'],
  [/\b(hat|hatte|hatten|haben|habe)\b/, 'Haben: used as the main verb or as the auxiliary in the Perfekt, with the participle at the end.'],
  [/\b(ist|war|sind|waren|bin|bist)\b/, 'Sein: the verb of being, also used with the participle for Perfekt verbs of movement or change.'],
  [/\b(werde|wirst|wird|werden)\b/, 'Werden: future with infinitive at the end (wird kommen = will come), or passive with a participle.'],
];
module.exports = function autoAnnotate(intro, max = 2) {
  const used = {};
  const noteRanges = t => { const r = []; const re = /\[\[[^\]]*?::[^\]]*?\]\]/g; let m; while ((m = re.exec(t))) r.push([m.index, m.index + m[0].length]); return r; };
  for (const [re, note] of RULES) {
    const key = re.source;
    used[key] = 0;
    for (const row of intro) {
      if (row[2] === '§' || used[key] >= max) continue;
      let t = row[0];
      const g = new RegExp(re.source, 'g');
      let m;
      while (used[key] < max && (m = g.exec(t))) {
        const a = m.index, b = m.index + m[0].length;
        const inside = noteRanges(t).some(([x, y]) => a < y && b > x) || t.slice(a, b).includes('==') || /\{|\|/.test(t.slice(Math.max(0, a - 1), a + 1));
        if (inside) continue;
        t = t.slice(0, a) + '[[' + m[0] + '::' + note + ']]' + t.slice(b);
        used[key]++;
        g.lastIndex = a + ('[[' + m[0] + '::' + note + ']]').length;
      }
      row[0] = t;
    }
  }
  return intro;
};
