# Content of the additional lessons (docs/Lektionen/N1..N9.html).
# Each lesson: id, title (de, en), where (de, en), sections [(h_de, h_en, html_de, html_en)], ex [(q, [opts], answer_index, fb_de, fb_en)]
# HTML helpers: say("text") renders a listen button (browser voice).

def say(t):
    return '<button type="button" class="say" data-t="%s" aria-label="Anhören: %s">▶ %s</button>' % (t, t, t)

def tbl(head, rows):
    h = '<div class="scroll"><table><tr>' + ''.join('<th>%s</th>' % x for x in head) + '</tr>'
    for r in rows:
        h += '<tr>' + ''.join('<td>%s</td>' % x for x in r) + '</tr>'
    return h + '</table></div>'

L = []

# ---------------------------------------------------------------- N1
L.append(dict(
id='N1', t='Aussprache: Umlaute, ch, r, Wortakzent', te='Pronunciation: umlauts, ch, r, word stress',
where='Sprechen (alle Teile) · Hören', wen='Speaking (all parts) · Listening',
goal='Du sprichst die schwierigen deutschen Laute verständlich aus und betonst Wörter richtig. Drücke auf ▶, um ein Wort zu hören (die deutsche Stimme deines Geräts).',
goalen='You pronounce the difficult German sounds clearly and stress words correctly. Press ▶ to hear a word (your device’s German voice).',
sec=[
('A. Warum Aussprache Punkte bringt', 'A. Why pronunciation earns points',
 '<p>In der mündlichen Prüfung bewerten die Prüfer auch <b>Aussprache und Intonation</b>. Du musst nicht wie ein Deutscher klingen. Du musst <b>verständlich</b> sein. Die häufigsten Probleme sind: lange und kurze Vokale, ä/ö/ü, ch, r und der Wortakzent.</p><p class="tip"><b>Routine für jeden Tag (10 Minuten):</b> Spiele <i>sprechen_modell.mp3</i> von deinem Tag ab, stoppe nach jedem Satz und sprich ihn laut nach (Shadowing). Nimm dich einmal pro Woche mit dem Handy auf und vergleiche.</p>',
 '<p>In the oral exam the examiners also assess <b>pronunciation and intonation</b>. You do not have to sound like a German. You have to be <b>understandable</b>. The most common problems are: long and short vowels, ä/ö/ü, ch, r and word stress.</p><p class="tip"><b>Daily routine (10 minutes):</b> play <i>sprechen_modell.mp3</i> from your day, stop after each sentence and repeat it aloud (shadowing). Record yourself on your phone once a week and compare.</p>'),
('B. Lange und kurze Vokale', 'B. Long and short vowels',
 '<p>Ein Vokal ist meistens <b>lang</b>, wenn danach <b>h</b> kommt, wenn er doppelt ist oder wenn nur <b>ein</b> Konsonant folgt. <b>ie</b> ist immer ein langes i. Ein Vokal ist meistens <b>kurz</b> vor zwei Konsonanten (auch tt, ss, mm …).</p>' +
 tbl(['lang', 'kurz'], [[say('Miete'), say('Mitte')], [say('Staat'), say('Stadt')], [say('Ofen'), say('offen')], [say('wohnen'), say('kommen')], [say('Bahn'), say('Bank')]]) +
 '<p>Achtung: Die Länge kann die Bedeutung ändern. <i>Miete</i> (Geld für die Wohnung) und <i>Mitte</i> (Zentrum) sind verschiedene Wörter.</p>',
 '<p>A vowel is usually <b>long</b> when it is followed by <b>h</b>, when it is doubled, or when only <b>one</b> consonant follows. <b>ie</b> is always a long i. A vowel is usually <b>short</b> before two consonants (also tt, ss, mm …).</p><p>Careful: length can change the meaning. <i>Miete</i> (rent) and <i>Mitte</i> (middle) are different words.</p>'),
('C. Umlaute: ä, ö, ü', 'C. Umlauts: ä, ö, ü',
 tbl(['Laut', 'So geht es', 'Beispiele'], [
  ['ä', 'wie e in <i>Bett</i> (kurz) oder ein offenes langes e', say('Männer') + ' ' + say('spät')],
  ['ö', 'sag „e“ und mach die Lippen rund wie bei „o“', say('schön') + ' ' + say('können')],
  ['ü', 'sag „i“ und mach die Lippen rund wie bei „u“', say('müde') + ' ' + say('fünf')]]) +
 '<p>Übe die Paare: ' + say('schon') + ' – ' + say('schön') + ' · ' + say('Mutter') + ' – ' + say('Mütter') + ' · ' + say('vier') + ' – ' + say('für') + '</p>',
 '<p>ä: like e in “bed”. ö: say “e” and round your lips as for “o”. ü: say “i” and round your lips as for “u”. Practise the pairs: schon (already) – schön (beautiful), Mutter (mother) – Mütter (mothers), vier (four) – für (for).</p>'),
('D. Zwei Laute für ch', 'D. Two sounds for ch',
 tbl(['Laut', 'Wann?', 'Beispiele'], [
  ['ich-Laut (weich, vorne im Mund)', 'nach i, e, ä, ö, ü, ei, eu, nach l, n, r und in -chen', say('ich') + ' ' + say('Milch') + ' ' + say('Mädchen') + ' ' + say('leicht')],
  ['ach-Laut (hinten im Hals)', 'nach a, o, u, au', say('Buch') + ' ' + say('Nacht') + ' ' + say('auch') + ' ' + say('kochen')],
  ['ks', 'chs', say('sechs') + ' ' + say('wachsen')]]) +
 '<p><b>-ig</b> am Wortende spricht man im Standarddeutschen wie <i>ich</i>: ' + say('zwanzig') + ' ' + say('wichtig') + '</p>',
 '<p>The ich-sound is soft and at the front of the mouth (after i, e, ä, ö, ü, ei, eu, l, n, r and in -chen). The ach-sound is at the back of the throat (after a, o, u, au). chs is pronounced ks. Word-final -ig sounds like ich in standard German.</p>'),
('E. Weitere Regeln, die Anfänger oft falsch machen', 'E. More rules beginners often get wrong',
 tbl(['Schreibung', 'Aussprache', 'Beispiele'], [
  ['sp, st am Wortanfang', 'schp, scht', say('Sport') + ' ' + say('Straße') + ' ' + say('verstehen')],
  ['z', 'ts', say('Zeit') + ' ' + say('zehn')],
  ['v', 'meist f', say('Vater') + ' ' + say('viel')],
  ['w', 'wie englisches v', say('Wasser') + ' ' + say('wohnen')],
  ['ei / ie', 'ei = ai · ie = langes i', say('mein') + ' ' + say('Liebe')],
  ['eu / äu', 'oi', say('heute') + ' ' + say('Häuser')],
  ['s vor Vokal', 'weiches s', say('Sonne') + ' ' + say('Reise')],
  ['b, d, g am Wortende', 'p, t, k', say('ab') + ' ' + say('Hund') + ' ' + say('Tag')],
  ['-er am Wortende', 'fast wie ein kurzes a', say('Lehrer') + ' ' + say('Wasser') + ' ' + say('aber')]]),
 '<p>sp/st at the start of a word or stem = shp/sht. z = ts. v is usually f. w = English v. ei = “eye”, ie = long i. eu/äu = “oy”. s before a vowel is soft (like English z). b, d, g at the end of a word sound like p, t, k. Final -er sounds almost like a short a.</p>'),
('F. Wortakzent und Satzmelodie', 'F. Word stress and sentence melody',
 tbl(['Regel', 'Beispiele'], [
  ['Deutsche Wörter: meist die <b>erste</b> Silbe', '<b>AR</b>beit · <b>LE</b>ben · <b>FREUN</b>din'],
  ['Trennbare Verben: das <b>Präfix</b>', '<b>AN</b>rufen · <b>EIN</b>kaufen · <b>MIT</b>bringen'],
  ['Untrennbare Verben (be-, ver-, er-, ge-, ent-, zer-): der <b>Stamm</b>', 'be<b>SU</b>chen · ver<b>STE</b>hen · er<b>ZÄH</b>len'],
  ['-tion, -ität, -ei, -ieren', 'Informa<b>TION</b> · Universi<b>TÄT</b> · Bäcke<b>REI</b> · stu<b>DIE</b>ren']]) +
 tbl(['Satzart', 'Melodie am Ende', 'Beispiel'], [['Aussage', '↘ nach unten', 'Ich komme aus Indien. ↘'], ['W-Frage', '↘ nach unten', 'Woher kommst du? ↘'], ['Ja/Nein-Frage', '↗ nach oben', 'Kommst du mit? ↗']]),
 '<p>German words: usually the first syllable. Separable verbs: the prefix. Inseparable verbs: the stem. Endings -tion, -ität, -ei, -ieren carry the stress. Statements and W-questions fall at the end, yes/no questions rise.</p>')],
ex=[
('Welches Wort hat einen <b>langen</b> Vokal?', ['Bett', 'Bahn', 'Stadt'], 1, 'Nach dem a steht ein h, also ist es lang.', 'The h after the a makes it long.'),
('In welchem Wort spricht man ch wie in <i>ich</i>?', ['Buch', 'Nacht', 'Milch'], 2, 'Nach l spricht man den ich-Laut.', 'After l you use the ich-sound.'),
('In welchem Wort spricht man ch wie in <i>ach</i>?', ['leicht', 'kochen', 'Mädchen'], 1, 'Nach o spricht man den ach-Laut.', 'After o you use the ach-sound.'),
('Wie spricht man „sechs“?', ['mit k-Laut: „seks“', 'mit sch: „sesch“', 'mit ich-Laut: „sech“'], 0, 'chs spricht man wie ks.', 'chs is pronounced ks.'),
('Wo ist der Akzent in „anrufen“?', ['AN-ru-fen', 'an-RU-fen', 'an-ru-FEN'], 0, 'Bei trennbaren Verben trägt das Präfix den Akzent.', 'Separable verbs stress the prefix.'),
('Wo ist der Akzent in „besuchen“?', ['BE-su-chen', 'be-SU-chen', 'be-su-CHEN'], 1, 'be- ist untrennbar, der Stamm trägt den Akzent.', 'be- is inseparable, so the stem is stressed.'),
('Wo ist der Akzent in „Information“?', ['IN-for-ma-tion', 'in-FOR-ma-tion', 'in-for-ma-TION'], 2, '-tion trägt immer den Akzent.', '-tion is always stressed.'),
('Welches Wortpaar unterscheidet sich nur durch die Länge des Vokals?', ['Miete – Mitte', 'Mutter – Mütter', 'schon – schön'], 0, 'ie ist lang, i vor tt ist kurz.', 'ie is long, i before tt is short.'),
('Wie beginnt man „Sport“?', ['mit s + p', 'mit schp', 'mit ts'], 1, 'sp am Wortanfang = schp.', 'sp at the start of a word = shp.'),
('Das v in „Vater“ klingt wie …', ['w', 'f', 'b'], 1, 'v spricht man in deutschen Wörtern meist wie f.', 'In German words v is usually pronounced f.'),
('Wie klingt das g am Ende von „Tag“?', ['g', 'k', 'ch'], 1, 'b, d, g am Wortende klingen wie p, t, k.', 'Final b, d, g sound like p, t, k.'),
('Wie spricht man ü in „müde“?', ['wie i mit runden Lippen', 'wie u mit breitem Mund', 'wie e'], 0, 'ü = i-Zunge + o/u-Lippen.', 'ü = tongue for i + rounded lips.'),
('Ja/Nein-Frage: Was macht die Stimme am Ende?', ['Sie geht nach oben.', 'Sie geht nach unten.', 'Sie bleibt gleich.'], 0, 'Ja/Nein-Fragen steigen am Ende.', 'Yes/no questions rise at the end.'),
('eu in „heute“ klingt wie …', ['e-u', 'oi', 'ü'], 1, 'eu und äu klingen wie oi.', 'eu and äu sound like “oy”.')]))

# ---------------------------------------------------------------- N2
L.append(dict(
id='N2', t='Imperativ: du, ihr, Sie', te='The imperative: du, ihr, Sie',
where='Schreiben (du-E-Mail) · Lesen (Anleitungen, Schilder) · Sprechen Teil 3', wen='Writing (informal email) · Reading (instructions, signs) · Speaking part 3',
goal='Du bildest den Imperativ für du, ihr und Sie und machst höfliche Bitten und Vorschläge.',
goalen='You form the imperative for du, ihr and Sie and make polite requests and suggestions.',
sec=[
('A. So bildest du den Imperativ', 'A. How to form the imperative',
 tbl(['Person', 'Regel', 'Beispiele'], [
  ['du', 'du-Form ohne <i>du</i> und ohne <i>-st</i>', 'du kommst → <b>Komm!</b> · du machst → <b>Mach!</b> · du wartest → <b>Warte!</b>'],
  ['ihr', 'ihr-Form ohne <i>ihr</i>', 'ihr kommt → <b>Kommt!</b> · ihr macht → <b>Macht!</b>'],
  ['Sie', 'Verb + Sie (wie eine Frage, aber mit !)', '<b>Kommen Sie</b> bitte! · <b>Warten Sie</b> einen Moment!'],
  ['wir (Vorschlag)', 'Verb + wir', '<b>Gehen wir</b> ins Kino!']]) +
 '<p>Das Verb steht am <b>Satzanfang</b>. Trennbare Verben: Das Präfix steht am Ende: <b>Ruf</b> mich bitte <b>an</b>! · <b>Bring</b> etwas zu trinken <b>mit</b>!</p>',
 '<p>du: the du-form without du and without -st. ihr: the ihr-form without ihr. Sie: verb + Sie. wir: verb + wir (a suggestion). The verb comes first. Separable verbs put the prefix at the end.</p>'),
('B. Besondere Formen', 'B. Special forms',
 tbl(['Infinitiv', 'du', 'ihr', 'Sie'], [
  ['nehmen (e → i)', 'Nimm!', 'Nehmt!', 'Nehmen Sie!'],
  ['geben (e → i)', 'Gib!', 'Gebt!', 'Geben Sie!'],
  ['lesen (e → ie)', 'Lies!', 'Lest!', 'Lesen Sie!'],
  ['sprechen (e → i)', 'Sprich!', 'Sprecht!', 'Sprechen Sie!'],
  ['fahren (a → ä bleibt <b>nicht</b>)', 'Fahr!', 'Fahrt!', 'Fahren Sie!'],
  ['schlafen', 'Schlaf!', 'Schlaft!', 'Schlafen Sie!'],
  ['sein', '<b>Sei</b> pünktlich!', '<b>Seid</b> leise!', '<b>Seien Sie</b> vorsichtig!'],
  ['haben', 'Hab keine Angst!', 'Habt Geduld!', 'Haben Sie Geduld!']]) +
 '<p><b>Merke:</b> e → i/ie bleibt im Imperativ (nimm, gib, lies), a → ä nicht (fahr, schlaf).</p>',
 '<p>Remember: the e → i/ie change stays in the du-imperative (nimm, gib, lies), but a → ä does not (fahr, schlaf). sein is irregular: sei, seid, seien Sie.</p>'),
('C. Höflich und freundlich klingen', 'C. Sounding polite and friendly',
 '<ul class="tight"><li><b>bitte</b>, <b>doch</b>, <b>mal</b> machen den Imperativ freundlich: <i>Komm doch mal vorbei! · Schreib mir bitte bald!</i></li><li><b>Lass uns …! / Lasst uns …!</b> ist ein Vorschlag (Sprechen Teil 3): <i>Lass uns zuerst die Getränke kaufen!</i></li><li>In einer <b>formellen E-Mail</b> ist der Imperativ oft zu direkt. Besser: <i>Könnten Sie mir bitte … schicken?</i> (Konjunktiv II)</li><li>Auf Schildern und in Anleitungen steht oft der <b>Infinitiv</b>: <i>Bitte nicht rauchen. Tür schließen.</i></li></ul>',
 '<ul class="tight"><li>bitte, doch, mal make the imperative friendly.</li><li>Lass uns …! is a suggestion (speaking part 3).</li><li>In a formal email the imperative is often too direct: use Könnten Sie bitte …?</li><li>Signs and instructions often use the infinitive: Bitte nicht rauchen.</li></ul>')],
ex=[
('(du, kommen) ___ bitte pünktlich!', ['Kommst', 'Komm', 'Kommen'], 1, 'du-Imperativ: ohne du und ohne -st.', 'du-imperative: no du and no -st.'),
('(du, nehmen) ___ doch einen Regenschirm mit!', ['Nehm', 'Nimmst', 'Nimm'], 2, 'e → i bleibt: nimm.', 'e → i stays: nimm.'),
('(du, fahren) ___ vorsichtig!', ['Fahr', 'Fähr', 'Fährst'], 0, 'a → ä fällt im Imperativ weg.', 'a → ä is dropped in the imperative.'),
('(ihr, sein) ___ bitte leise, das Baby schläft.', ['Seid', 'Sind', 'Seien'], 0, 'ihr-Imperativ von sein: seid.', 'ihr-imperative of sein: seid.'),
('(Sie, warten) ___ bitte einen Moment!', ['Wartet', 'Warten Sie', 'Wartest'], 1, 'Sie-Imperativ: Verb + Sie.', 'Sie-imperative: verb + Sie.'),
('(du, anrufen) ___ mich heute Abend ___!', ['Rufst … an', 'Ruf … an', 'Anruf … –'], 1, 'Trennbar: Präfix ans Ende.', 'Separable: prefix at the end.'),
('(du, lesen) ___ den Text zweimal!', ['Les', 'Lies', 'Liest'], 1, 'e → ie bleibt: lies.', 'e → ie stays: lies.'),
('(du, sein) ___ nicht traurig!', ['Bist', 'Sei', 'Sein'], 1, 'du-Imperativ von sein: sei.', 'du-imperative of sein: sei.'),
('Ein Vorschlag im Sprechen Teil 3:', ['Lass uns am Samstag grillen!', 'Lassen uns am Samstag grillen!', 'Lass wir am Samstag grillen!'], 0, 'Lass uns + Infinitiv am Ende.', 'Lass uns + infinitive at the end.'),
('Formelle E-Mail an eine Firma: Was ist am besten?', ['Schicken Sie mir den Katalog!', 'Könnten Sie mir bitte den Katalog schicken?', 'Schick mir den Katalog!'], 1, 'Formell ist eine Bitte mit Konjunktiv II am höflichsten.', 'In formal writing a Konjunktiv II request is the most polite.'),
('(ihr, mitbringen) ___ bitte Salat ___!', ['Bringt … mit', 'Bringen … mit', 'Mitbringt … –'], 0, 'ihr-Form ohne ihr, Präfix ans Ende.', 'ihr-form without ihr, prefix at the end.'),
('Was bedeutet das Schild „Bitte nicht füttern“?', ['Man soll die Tiere füttern.', 'Man soll den Tieren kein Futter geben.', 'Die Tiere haben Hunger.'], 1, 'Infinitiv auf Schildern = Anweisung.', 'An infinitive on a sign = an instruction.')]))

# ---------------------------------------------------------------- N3
L.append(dict(
id='N3', t='Präteritum der normalen Verben', te='The simple past of ordinary verbs',
where='Lesen Teil 2 (Zeitungsartikel) · Hören (Nachrichten, Berichte)', wen='Reading part 2 (newspaper articles) · Listening (news, reports)',
goal='Du erkennst die häufigsten Präteritum-Formen in Texten und findest den Infinitiv. Selbst schreibst du in E-Mails weiter das Perfekt (außer war, hatte und Modalverben).',
goalen='You recognise the most common simple-past forms in texts and find the infinitive. In your own emails keep using the Perfekt (except war, hatte and modal verbs).',
sec=[
('A. Warum du das Präteritum brauchst', 'A. Why you need the simple past',
 '<p>Zeitungsartikel, Berichte und Nachrichten stehen fast immer im <b>Präteritum</b>: <i>Der Bürgermeister <b>eröffnete</b> gestern das neue Schwimmbad. Viele Familien <b>kamen</b> …</i> Wenn du die Formen nicht erkennst, verstehst du den Text in Lesen Teil 2 nicht. Du musst sie <b>erkennen</b>, nicht perfekt schreiben.</p>',
 '<p>Newspaper articles, reports and news are almost always in the simple past. If you do not recognise the forms, you will not understand the text in reading part 2. You need to <b>recognise</b> them, not write them perfectly.</p>'),
('B. Regelmäßige Verben: Stamm + -te', 'B. Regular verbs: stem + -te',
 tbl(['', 'machen', 'arbeiten (Stamm auf -t)'], [['ich', 'mach<b>te</b>', 'arbeit<b>ete</b>'], ['du', 'mach<b>test</b>', 'arbeit<b>etest</b>'], ['er/sie/es', 'mach<b>te</b>', 'arbeit<b>ete</b>'], ['wir', 'mach<b>ten</b>', 'arbeit<b>eten</b>'], ['ihr', 'mach<b>tet</b>', 'arbeit<b>etet</b>'], ['sie/Sie', 'mach<b>ten</b>', 'arbeit<b>eten</b>']]) +
 '<p><b>ich</b> und <b>er/sie/es</b> haben dieselbe Form (ohne -t am Ende). Trennbare Verben: <i>Der Zug <b>kam</b> pünktlich <b>an</b>. Sie <b>kaufte</b> im Supermarkt <b>ein</b>.</i></p>',
 '<p>ich and er/sie/es have the same form. Separable verbs put the prefix at the end, as in the present tense.</p>'),
('C. Die 40 wichtigsten unregelmäßigen Formen', 'C. The 40 most important irregular forms',
 '<p>Unregelmäßige Verben ändern den Stamm. ich und er/sie/es haben <b>keine Endung</b>: <i>ich ging, er ging, wir gingen</i>.</p>' +
 tbl(['Präteritum', 'Infinitiv', 'Präteritum', 'Infinitiv'], [
  ['ging', 'gehen', 'kam', 'kommen'], ['fuhr', 'fahren', 'sah', 'sehen'], ['gab', 'geben (es gab = there was)', 'nahm', 'nehmen'],
  ['fand', 'finden', 'sprach', 'sprechen'], ['las', 'lesen', 'schrieb', 'schreiben'], ['blieb', 'bleiben', 'aß', 'essen'],
  ['trank', 'trinken', 'saß', 'sitzen'], ['stand', 'stehen', 'lag', 'liegen'], ['begann', 'beginnen', 'half', 'helfen'],
  ['traf', 'treffen', 'rief … an', 'anrufen'], ['lief', 'laufen', 'schlief', 'schlafen'], ['fiel', 'fallen', 'hielt', 'halten'],
  ['trug', 'tragen', 'zog … um', 'umziehen'], ['flog', 'fliegen', 'verlor', 'verlieren'], ['gewann', 'gewinnen', 'starb', 'sterben'],
  ['wurde', 'werden', 'bot … an', 'anbieten'], ['wusste', 'wissen', 'dachte', 'denken'], ['brachte', 'bringen', 'kannte', 'kennen'],
  ['nannte', 'nennen', 'verstand', 'verstehen'], ['entschied', 'entscheiden', 'erhielt', 'erhalten']]) +
 '<p><b>Mischverben</b> (wusste, dachte, brachte, kannte, nannte): Stamm ändert sich <b>und</b> sie bekommen -te.</p>',
 '<p>Irregular verbs change the stem; ich and er/sie/es have no ending. Mixed verbs (wusste, dachte, brachte, kannte, nannte) change the stem and also take -te. Learn this list as pairs: past form → infinitive.</p>'),
('D. Trick für das Lesen', 'D. A trick for reading',
 '<ol class="tight"><li>Endet das Verb auf <b>-te / -ten</b>? Dann streiche -te und hänge -en an: <i>wohnte → wohnen</i>.</li><li>Kennst du die Form nicht? Suche ein Verb mit ähnlichen Konsonanten: <i>fand → f-nd → finden</i>, <i>trug → tr-g → tragen</i>.</li><li>Das Präteritum steht im Hauptsatz auf Position 2, im Nebensatz am Ende: <i>…, weil er krank <b>war</b>.</i></li></ol>',
 '<ol class="tight"><li>Ends in -te/-ten? Remove -te and add -en.</li><li>Unknown form? Look for a verb with similar consonants: fand → finden.</li><li>Main clause: position 2; subordinate clause: at the end.</li></ol>')],
ex=[
('„Gestern <b>ging</b> ich zum Arzt.“ Infinitiv?', ['gingen', 'gehen', 'gegangen'], 1, 'ging → gehen.', 'ging → gehen.'),
('„Der Film <b>begann</b> um acht Uhr.“ Infinitiv?', ['beginnen', 'begannen', 'begonnen'], 0, 'begann → beginnen.', 'begann → beginnen.'),
('„Es <b>gab</b> viele Besucher.“ bedeutet:', ['Es gibt viele Besucher.', 'Es waren viele Besucher da.', 'Die Besucher gaben etwas.'], 1, 'es gab = es gibt in der Vergangenheit (there was/were).', 'es gab = there was/were.'),
('Präteritum von „wohnen“ (er):', ['er wohnt', 'er wohnte', 'er wohnten'], 1, 'Regelmäßig: Stamm + -te.', 'Regular: stem + -te.'),
('Präteritum von „arbeiten“ (sie, Singular):', ['sie arbeitete', 'sie arbeitte', 'sie arbeitet'], 0, 'Stamm auf -t: -ete.', 'Stem ending in -t: -ete.'),
('„Wir ___ den ganzen Tag am Strand.“ (liegen)', ['lagen', 'liegten', 'lag'], 0, 'liegen → lag, wir lagen.', 'liegen → lag, wir lagen.'),
('„Er ___ nicht, wo der Bahnhof ist.“ (wissen)', ['wisste', 'wusste', 'weißte'], 1, 'Mischverb: wusste.', 'Mixed verb: wusste.'),
('„Der Zug ___ mit Verspätung ___.“ (ankommen)', ['kam … an', 'ankam … –', 'kommte … an'], 0, 'Trennbar: kam … an.', 'Separable: kam … an.'),
('„Sie <b>fand</b> eine neue Stelle.“ Infinitiv?', ['fanden', 'finden', 'fahren'], 1, 'fand → finden.', 'fand → finden.'),
('„Ich ___ ihn auf der Party.“ (treffen)', ['treffte', 'traf', 'trof'], 1, 'treffen → traf.', 'treffen → traf.'),
('„…, weil das Wetter so schlecht ___.“', ['war', 'wurde gewesen', 'warte'], 0, 'war am Ende des Nebensatzes.', 'war at the end of the subordinate clause.'),
('Welche Form passt in eine <b>private E-Mail</b> über deinen Urlaub?', ['Wir fuhren nach Italien.', 'Wir sind nach Italien gefahren.', 'Wir fahrten nach Italien.'], 1, 'Im Gespräch und in privaten E-Mails benutzt man meist das Perfekt.', 'In speech and personal emails you normally use the Perfekt.')]))

# ---------------------------------------------------------------- N4
L.append(dict(
id='N4', t='Futur I und die drei Bedeutungen von werden', te='Future tense and the three uses of werden',
where='Schreiben (Pläne, Versprechen) · Lesen · Sprachbausteine', wen='Writing (plans, promises) · Reading · Language elements',
goal='Du bildest das Futur I und unterscheidest werden als Vollverb, im Futur und im Passiv.',
goalen='You form the future tense and tell apart werden as a full verb, in the future tense and in the passive.',
sec=[
('A. Futur I: werden + Infinitiv', 'A. Future I: werden + infinitive',
 tbl(['', 'werden', 'Beispiel'], [['ich', 'werde', 'Ich <b>werde</b> dich morgen <b>anrufen</b>.'], ['du', 'wirst', '<b>Wirst</b> du zur Party <b>kommen</b>?'], ['er/sie/es', 'wird', 'Morgen <b>wird</b> es <b>regnen</b>.'], ['wir', 'werden', 'Wir <b>werden</b> pünktlich <b>sein</b>.'], ['ihr', 'werdet', 'Ihr <b>werdet</b> es <b>schaffen</b>!'], ['sie/Sie', 'werden', 'Sie <b>werden</b> eine Antwort <b>bekommen</b>.']]) +
 '<p>werden steht auf Position 2, der <b>Infinitiv am Ende</b>. Im Nebensatz steht werden ganz am Ende: <i>Ich verspreche dir, dass ich pünktlich kommen <b>werde</b>.</i></p>',
 '<p>werden in position 2, the infinitive at the end. In a subordinate clause werden goes to the very end.</p>'),
('B. Wann benutzt man das Futur?', 'B. When do you use the future tense?',
 tbl(['Verwendung', 'Beispiel'], [['Versprechen, fester Plan', 'Ich <b>werde</b> dir bei dem Umzug <b>helfen</b>.'], ['Vorhersage', 'Morgen <b>wird</b> es kalt <b>sein</b>.'], ['Vermutung (oft mit wohl)', 'Er ist nicht da. Er <b>wird</b> wohl krank <b>sein</b>.']]) +
 '<p class="tip">Sehr oft benutzt man für die Zukunft einfach das <b>Präsens + Zeitangabe</b>: <i>Morgen fahre ich nach Köln.</i> Beides ist richtig.</p>',
 '<p>Use it for promises and firm plans, predictions and assumptions. Very often German simply uses the present tense with a time expression for the future. Both are correct.</p>'),
('C. Drei Mal werden: erkenne den Unterschied', 'C. werden three times: spot the difference',
 tbl(['Form', 'Bedeutung', 'Beispiel'], [['werden allein (+ Nomen/Adjektiv)', 'Veränderung (become)', 'Sie <b>wird</b> Ärztin. Es <b>wird</b> dunkel. Perfekt: ist … <b>geworden</b>'], ['werden + <b>Infinitiv</b>', 'Futur', 'Ich <b>werde</b> morgen <b>arbeiten</b>.'], ['werden + <b>Partizip II</b>', 'Passiv', 'Das Haus <b>wird</b> renoviert.'], ['würde + Infinitiv', 'Konjunktiv II', 'Ich <b>würde</b> gern <b>kommen</b>.']]) +
 '<p>Schau immer auf das <b>Wort am Ende</b>: Infinitiv → Futur, Partizip II → Passiv, nichts davon → „become“.</p>',
 '<p>Always look at the word at the end: infinitive → future, past participle → passive, neither → “become”.</p>')],
ex=[
('Ich ___ dich morgen anrufen.', ['wird', 'werde', 'werden'], 1, 'ich werde.', 'ich werde.'),
('___ du am Samstag kommen?', ['Wirst', 'Wird', 'Werdest'], 0, 'du wirst.', 'du wirst.'),
('Morgen wird es sicher ___.', ['regnet', 'regnen', 'geregnet'], 1, 'Futur: Infinitiv am Ende.', 'Future: infinitive at the end.'),
('„Sie wird Lehrerin.“ Was bedeutet werden hier?', ['Futur', 'Passiv', 'Veränderung (become)'], 2, 'werden + Nomen = become.', 'werden + noun = become.'),
('„Die Straße wird repariert.“ Was ist das?', ['Futur', 'Passiv', 'Konjunktiv II'], 1, 'werden + Partizip II = Passiv.', 'werden + past participle = passive.'),
('„Wir werden euch besuchen.“ Was ist das?', ['Futur', 'Passiv', 'Präteritum'], 0, 'werden + Infinitiv = Futur.', 'werden + infinitive = future.'),
('Ich verspreche dir, dass ich ___ .', ['werde pünktlich sein', 'pünktlich sein werde', 'pünktlich werde sein'], 1, 'Im Nebensatz steht werden am Ende.', 'In a subordinate clause werden goes last.'),
('Er ist nicht im Büro. Er ___ wohl krank sein.', ['wird', 'würde', 'wurde'], 0, 'Vermutung: wird wohl.', 'Assumption: wird wohl.'),
('Perfekt von „Es wird kalt“:', ['Es ist kalt geworden.', 'Es hat kalt geworden.', 'Es ist kalt worden.'], 0, 'Vollverb werden: ist geworden.', 'Full verb werden: ist geworden.'),
('Welcher Satz ist <b>kein</b> Futur?', ['Ich werde dir helfen.', 'Ich würde dir helfen.', 'Wir werden helfen.'], 1, 'würde = Konjunktiv II.', 'würde = subjunctive II.'),
('Ihr ___ die Prüfung bestimmt schaffen!', ['werdet', 'werden', 'wird'], 0, 'ihr werdet.', 'ihr werdet.'),
('Was ist eine richtige Alternative zu „Ich werde morgen nach Köln fahren“?', ['Ich fahre morgen nach Köln.', 'Ich fuhr morgen nach Köln.', 'Ich bin morgen nach Köln gefahren.'], 0, 'Präsens + Zeitangabe = Zukunft.', 'Present tense + time expression = future.')]))

# ---------------------------------------------------------------- N5
L.append(dict(
id='N5', t='Zweck: um … zu oder damit?', te='Purpose: um … zu or damit?',
where='Sprachbausteine Teil 1 · Schreiben · Sprechen Teil 2', wen='Language elements part 1 · Writing · Speaking part 2',
goal='Du sagst, wozu du etwas machst, und wählst richtig zwischen um … zu und damit.',
goalen='You say what you do something for, and choose correctly between um … zu and damit.',
sec=[
('A. Die Regel', 'A. The rule',
 tbl(['', 'Wann?', 'Beispiel'], [['um … zu + Infinitiv', 'gleiches Subjekt in beiden Sätzen', '<b>Ich</b> lerne Deutsch, <b>um</b> in Deutschland <b>zu arbeiten</b>.'], ['damit + Verb am Ende', 'verschiedene Subjekte', '<b>Ich</b> spreche langsam, <b>damit</b> <b>mein Kollege</b> mich <b>versteht</b>.'], ['damit (auch möglich)', 'gleiches Subjekt', 'Ich lerne Deutsch, damit ich in Deutschland arbeiten kann.']]) +
 '<p>Frage: <b>Wozu?</b> oder <b>Wofür?</b> Antwort: um … zu / damit.</p>',
 '<p>um … zu + infinitive: same subject in both clauses. damit + verb at the end: different subjects (also possible with the same subject). The question is Wozu? (what for?).</p>'),
('B. Satzbau', 'B. Word order',
 '<ul class="tight"><li><b>um … zu:</b> kein Subjekt, kein konjugiertes Verb. zu + Infinitiv am Ende. Trennbare Verben: zu in der Mitte: <i>um <b>einzukaufen</b>, um früh <b>aufzustehen</b></i>.</li><li><b>damit:</b> normaler Nebensatz, Verb am Ende: <i>damit ich nicht zu spät <b>komme</b></i>.</li><li>Kein <i>wollen</i> oder <i>sollen</i> im damit-Satz: <s>damit er pünktlich sein will</s> → <i>damit er pünktlich ist</i>.</li><li>Der Zweck kann auch vorne stehen: <i><b>Um</b> fit <b>zu bleiben</b>, <b>gehe</b> ich jeden Tag spazieren.</i> (danach Verb auf Position 1)</li></ul>',
 '<ul class="tight"><li>um … zu: no subject, no conjugated verb; zu + infinitive at the end; separable verbs put zu in the middle (einzukaufen).</li><li>damit: normal subordinate clause, verb at the end.</li><li>No wollen/sollen in a damit clause.</li><li>The purpose clause can come first; then the main verb follows directly.</li></ul>'),
('C. Nicht verwechseln', 'C. Do not confuse',
 tbl(['Wort', 'Bedeutung', 'Beispiel'], [['weil', 'Grund (Warum?)', 'Ich lerne, <b>weil</b> ich die Prüfung bestehen will.'], ['damit (Nebensatz)', 'Zweck (Wozu?)', 'Ich lerne, <b>damit</b> ich die Prüfung bestehe.'], ['damit (Pronomen)', '= mit dem / mit der', 'Hier ist mein neues Handy. Was kann man <b>damit</b> machen?'], ['sodass', 'Folge (Ergebnis)', 'Es regnete stark, <b>sodass</b> wir zu Hause blieben.'], ['zum + Nomen', 'kurzer Zweck', '<b>Zum</b> Lernen brauche ich Ruhe.']]),
 '<p>weil = reason, damit = purpose, damit as a pronoun = “with it”, sodass = result, zum + noun = short purpose.</p>')],
ex=[
('Ich spare Geld, ___ ein Auto zu kaufen.', ['damit', 'um', 'weil'], 1, 'zu + Infinitiv am Ende → um … zu.', 'zu + infinitive at the end → um … zu.'),
('Ich erkläre es noch einmal, ___ du es verstehst.', ['um', 'damit', 'zu'], 1, 'Verschiedene Subjekte (ich / du) → damit.', 'Different subjects → damit.'),
('Sie geht früh ins Bett, um morgen fit ___.', ['ist', 'zu sein', 'sein zu'], 1, 'um … zu + Infinitiv.', 'um … zu + infinitive.'),
('Ich fahre in die Stadt, um ___.', ['einzukaufen', 'zu einkaufen', 'einkaufen zu'], 0, 'Trennbar: zu in der Mitte.', 'Separable: zu in the middle.'),
('Wir sprechen leise, damit das Baby nicht ___.', ['aufwacht', 'aufzuwachen', 'wacht auf'], 0, 'damit: Verb am Ende.', 'damit: verb at the end.'),
('Ich lerne viel, ___ ich die Prüfung bestehen will.', ['damit', 'um', 'weil'], 2, 'Grund (wollen) → weil.', 'Reason (want) → weil.'),
('___ fit zu bleiben, fahre ich mit dem Fahrrad.', ['Damit', 'Um', 'Weil'], 1, 'zu bleiben → um.', 'zu bleiben → um.'),
('Der Lehrer spricht laut, damit alle ihn ___.', ['hören', 'zu hören', 'hört'], 0, 'Subjekt alle (Plural), Verb am Ende.', 'Subject alle (plural), verb at the end.'),
('Es schneite stark, ___ der Zug Verspätung hatte.', ['damit', 'sodass', 'um'], 1, 'Folge → sodass.', 'Result → sodass.'),
('Das ist mein neues Fahrrad. ___ fahre ich zur Arbeit.', ['Damit', 'Um', 'Zu'], 0, 'damit = mit dem Fahrrad.', 'damit = with the bike.'),
('Welcher Satz ist richtig?', ['Ich rufe an, um einen Termin zu vereinbaren.', 'Ich rufe an, um ich einen Termin vereinbare.', 'Ich rufe an, damit einen Termin zu vereinbaren.'], 0, 'um … zu ohne Subjekt.', 'um … zu without a subject.'),
('___ Kochen brauche ich frische Kräuter.', ['Um', 'Zum', 'Damit'], 1, 'zum + Nomen.', 'zum + noun.')]))

# ---------------------------------------------------------------- N6
L.append(dict(
id='N6', t='Zweiteilige Konnektoren', te='Two-part connectors',
where='Sprachbausteine Teil 1 und 2 · Sprechen Teil 2 · Schreiben', wen='Language elements parts 1 and 2 · Speaking part 2 · Writing',
goal='Du kennst die sechs zweiteiligen Konnektoren und erkennst in einer Lücke sofort den passenden zweiten Teil.',
goalen='You know the six two-part connectors and immediately recognise the matching second part in a gap.',
sec=[
('A. Die sechs Paare', 'A. The six pairs',
 tbl(['Konnektor', 'Bedeutung', 'Beispiel'], [
  ['nicht nur … sondern auch', 'A und zusätzlich B', 'Er spricht <b>nicht nur</b> Deutsch, <b>sondern auch</b> Englisch.'],
  ['sowohl … als auch', 'A und B (beide)', '<b>Sowohl</b> meine Mutter <b>als auch</b> mein Vater arbeiten.'],
  ['weder … noch', 'nicht A und nicht B', 'Ich habe <b>weder</b> Zeit <b>noch</b> Geld.'],
  ['entweder … oder', 'A oder B (nur eins)', '<b>Entweder</b> fahren wir mit dem Bus <b>oder</b> wir nehmen ein Taxi.'],
  ['zwar … aber', 'A ist so, aber B dagegen', 'Die Wohnung ist <b>zwar</b> klein, <b>aber</b> sie ist billig.'],
  ['je … desto / umso', 'wenn A mehr, dann B mehr', '<b>Je</b> mehr ich übe, <b>desto</b> besser spreche ich.']]),
 '<p>not only … but also · both … and · neither … nor · either … or · admittedly … but · the more … the more.</p>'),
('B. Wortstellung, auf die Prüfer achten', 'B. Word order examiners check',
 '<ul class="tight"><li><b>weder … noch</b> ist schon negativ. Kein zusätzliches <i>nicht</i> oder <i>kein</i>: <s>Ich habe weder keine Zeit …</s></li><li><b>sowohl … als auch</b> mit zwei Personen als Subjekt: Verb im <b>Plural</b>.</li><li><b>je … desto:</b> Der je-Teil ist ein Nebensatz (Verb am Ende). Nach desto + Komparativ kommt sofort das Verb: <i>Je älter er <b>wird</b>, desto ruhiger <b>ist</b> er.</i></li><li><b>entweder</b> kann vor dem Verb stehen oder auf Position 0: <i>Entweder <b>kommst</b> du mit, oder … / Entweder du <b>kommst</b> mit, oder …</i> Beides ist richtig.</li><li><b>zwar</b> steht im Satz, meist nach dem Verb: <i>Das Hotel <b>war zwar</b> teuer, aber …</i></li></ul>',
 '<ul class="tight"><li>weder … noch is already negative: no extra nicht/kein.</li><li>sowohl … als auch with two subjects: plural verb.</li><li>je-clause: verb at the end; after desto + comparative the verb comes immediately.</li><li>entweder can come before the verb or in position 0; both are correct.</li><li>zwar stands inside the clause, usually after the verb.</li></ul>'),
('C. Tipp für Sprachbausteine', 'C. Tip for the language elements',
 '<p>Siehst du in der Lücke den ersten Teil (zwar, je, weder, sowohl, entweder, nicht nur), dann <b>suche den zweiten Teil</b> weiter hinten im Satz. Siehst du den zweiten Teil (desto, noch, als auch, sondern auch), dann fehlt vorne der erste. Diese Paare sind sichere Punkte.</p><p>Fürs Sprechen Teil 2: <i>Einerseits</i> ist das praktisch, <i>andererseits</i> ist es teuer. · Online-Kurse sind <i>zwar</i> flexibel, <i>aber</i> man hat wenig Kontakt.</p>',
 '<p>If the gap contains a first part, look for the second part later in the sentence, and vice versa. These pairs are safe points. For speaking part 2, also use einerseits … andererseits (on the one hand … on the other).</p>')],
ex=[
('Ich trinke ___ Kaffee noch Tee.', ['weder', 'entweder', 'sowohl'], 0, 'noch gehört zu weder.', 'noch goes with weder.'),
('Er kann sowohl kochen ___ backen.', ['oder', 'als auch', 'sondern auch'], 1, 'sowohl … als auch.', 'sowohl … als auch.'),
('Sie lernt nicht nur Deutsch, ___ Spanisch.', ['sondern auch', 'als auch', 'aber auch'], 0, 'nicht nur … sondern auch.', 'nicht nur … sondern auch.'),
('___ wir gehen ins Kino, oder wir bleiben zu Hause.', ['Weder', 'Entweder', 'Zwar'], 1, 'entweder … oder.', 'entweder … oder.'),
('Das Hotel war ___ teuer, aber sehr schön.', ['zwar', 'je', 'sowohl'], 0, 'zwar … aber.', 'zwar … aber.'),
('Je früher wir losfahren, ___ weniger Stau gibt es.', ['desto', 'als', 'dann'], 0, 'je … desto.', 'je … desto.'),
('Je mehr man liest, desto besser ___ man.', ['man schreibt', 'schreibt', 'schreibe'], 1, 'Nach desto + Komparativ: Verb sofort.', 'After desto + comparative: verb right away.'),
('Ich habe weder Hunger ___ Durst.', ['oder', 'noch', 'nicht'], 1, 'weder … noch.', 'weder … noch.'),
('Welcher Satz ist richtig?', ['Ich habe weder keine Zeit noch Geld.', 'Ich habe weder Zeit noch Geld.', 'Ich habe nicht weder Zeit noch Geld.'], 1, 'weder ist schon negativ.', 'weder is already negative.'),
('Sowohl mein Bruder als auch meine Schwester ___ in Berlin.', ['wohnt', 'wohnen', 'wohnst'], 1, 'Zwei Personen → Plural.', 'Two people → plural.'),
('Je länger ich in Deutschland ___, desto mehr verstehe ich.', ['wohne', 'wohnte ich', 'ich wohne'], 0, 'je-Teil: Verb am Ende.', 'je clause: verb at the end.'),
('___ ist die Arbeit interessant, andererseits ist sie stressig.', ['Einerseits', 'Entweder', 'Zwar'], 0, 'einerseits … andererseits.', 'einerseits … andererseits.')]))

# ---------------------------------------------------------------- N7
L.append(dict(
id='N7', t='Konjunktiv II der Vergangenheit', te='Subjunctive II in the past',
where='Schreiben (Absage, Bedauern) · Sprechen · Lesen', wen='Writing (declining, regret) · Speaking · Reading',
goal='Du drückst Bedauern über die Vergangenheit aus und verstehst unwirkliche Bedingungen in der Vergangenheit.',
goalen='You express regret about the past and understand unreal conditions in the past.',
sec=[
('A. Form: hätte / wäre + Partizip II', 'A. Form: hätte / wäre + past participle',
 '<p>Du bildest die Form wie das Perfekt, aber mit <b>hätte</b> statt <i>habe</i> und <b>wäre</b> statt <i>bin</i>. haben oder sein: dieselbe Regel wie im Perfekt.</p>' +
 tbl(['Perfekt (real)', 'Konjunktiv II Vergangenheit (nicht real)'], [['Ich habe dich angerufen.', 'Ich <b>hätte</b> dich <b>angerufen</b>. (habe es aber nicht gemacht)'], ['Ich bin gekommen.', 'Ich <b>wäre</b> gern <b>gekommen</b>. (bin aber nicht gekommen)']]) +
 tbl(['', 'hätte', 'wäre'], [['ich', 'hätte', 'wäre'], ['du', 'hättest', 'wär(e)st'], ['er/sie/es', 'hätte', 'wäre'], ['wir', 'hätten', 'wären'], ['ihr', 'hättet', 'wär(e)t'], ['sie/Sie', 'hätten', 'wären']]),
 '<p>Formed like the Perfekt, but with hätte instead of habe and wäre instead of bin. Use haben or sein as in the Perfekt.</p>'),
('B. Drei Verwendungen für die Prüfung', 'B. Three uses for the exam',
 tbl(['Verwendung', 'Beispiel'], [
  ['Bedauern (Absage-E-Mail)', 'Es tut mir leid. Ich <b>wäre</b> wirklich gern <b>gekommen</b>.'],
  ['Unwirkliche Bedingung', 'Wenn ich mehr Zeit <b>gehabt hätte</b>, <b>hätte</b> ich dich <b>besucht</b>.'],
  ['Rat im Nachhinein (erkennen)', 'Du <b>hättest</b> früher <b>anrufen sollen</b>. (Modalverb: hätte + 2 Infinitive)']]) +
 '<p class="tip">Im Wenn-Satz steht das konjugierte Verb (hätte/wäre) am Ende: <i>Wenn ich das <b>gewusst hätte</b>, …</i> Danach beginnt der Hauptsatz mit dem Verb: <i>…, <b>wäre</b> ich nicht gekommen.</i></p>',
 '<p>Regret (declining an invitation), unreal past condition, and advice in hindsight (recognise: du hättest … sollen). In the wenn-clause hätte/wäre goes to the end; the main clause then starts with the verb.</p>')],
ex=[
('Es tut mir leid. Ich ___ gern zu deiner Party gekommen.', ['hätte', 'wäre', 'würde'], 1, 'kommen → sein: wäre gekommen.', 'kommen takes sein: wäre gekommen.'),
('Ich ___ dir gern geholfen, aber ich war krank.', ['hätte', 'wäre', 'habe'], 0, 'helfen → haben: hätte geholfen.', 'helfen takes haben: hätte geholfen.'),
('Wenn ich das gewusst ___, hätte ich dich angerufen.', ['habe', 'hätte', 'wäre'], 1, 'wissen → haben: gewusst hätte.', 'wissen takes haben.'),
('Wenn der Bus pünktlich gewesen wäre, ___ ich nicht zu spät gekommen.', ['hätte', 'wäre', 'bin'], 1, 'kommen → sein.', 'kommen takes sein.'),
('Was bedeutet: „Ich hätte fast den Zug verpasst.“?', ['Ich habe den Zug verpasst.', 'Ich habe den Zug fast verpasst, aber ich habe ihn bekommen.', 'Ich werde den Zug verpassen.'], 1, 'Konjunktiv II = nicht passiert.', 'Subjunctive = it did not happen.'),
('Wenn du früher ___ wärst, hättest du ihn gesehen.', ['gekommen', 'kommen', 'kamst'], 0, 'wäre + Partizip II.', 'wäre + past participle.'),
('„Du hättest mich anrufen sollen.“ bedeutet:', ['Du hast mich angerufen.', 'Es wäre gut gewesen, wenn du mich angerufen hättest.', 'Du sollst mich morgen anrufen.'], 1, 'Rat im Nachhinein.', 'Advice in hindsight.'),
('Wir ___ gern länger geblieben.', ['wären', 'hätten', 'würden'], 0, 'bleiben → sein.', 'bleiben takes sein.'),
('Wenn ich Zeit gehabt hätte, ___ ich mitgekommen.', ['hätte', 'wäre', 'würde'], 1, 'mitkommen → sein.', 'mitkommen takes sein.'),
('Welcher Satz drückt Bedauern aus?', ['Ich habe die Prüfung bestanden.', 'Ich hätte mehr lernen sollen.', 'Ich werde mehr lernen.'], 1, 'hätte … sollen = Bedauern.', 'hätte … sollen = regret.'),
('Hättest du gestern Zeit gehabt, ___ wir ins Kino gehen können.', ['hätten', 'wären', 'haben'], 0, 'Modalverb können → hätte(n).', 'Modal verb → hätte(n).'),
('Ich ___ dir die E-Mail geschickt, aber ich hatte deine Adresse nicht.', ['wäre', 'hätte', 'würde'], 1, 'schicken → haben.', 'schicken takes haben.')]))

# ---------------------------------------------------------------- N8
L.append(dict(
id='N8', t='Passiv Präteritum und lassen', te='Passive in the past and lassen',
where='Lesen (Berichte, Geschichte, Dienstleistungen) · Sprachbausteine', wen='Reading (reports, history, services) · Language elements',
goal='Du erkennst das Passiv in der Vergangenheit und benutzt lassen für „etwas machen lassen“.',
goalen='You recognise the passive in the past and use lassen for “having something done”.',
sec=[
('A. Passiv in allen Zeiten (erkennen)', 'A. The passive in all tenses (recognise)',
 tbl(['Zeit', 'Form', 'Beispiel'], [['Präsens', 'wird + Partizip II', 'Das Haus <b>wird</b> renoviert.'], ['Präteritum', '<b>wurde</b> + Partizip II', 'Das Haus <b>wurde</b> 1900 <b>gebaut</b>.'], ['Perfekt', 'ist + Partizip II + <b>worden</b>', 'Das Haus <b>ist</b> renoviert <b>worden</b>.'], ['mit Modalverb', 'muss + Partizip II + werden', 'Das Haus <b>muss</b> renoviert <b>werden</b>.']]) +
 '<p>wurde: ich wurde, du wurdest, er/sie/es wurde, wir wurden, ihr wurdet, sie wurden. Wer es macht, steht mit <b>von + Dativ</b>: <i>Das Museum wurde <b>von</b> einem bekannten Architekten geplant.</i></p><p class="tip">Im Passiv-Perfekt heißt es <b>worden</b>, nicht <i>geworden</i>.</p>',
 '<p>Präteritum passive: wurde + past participle (very common in reading texts). Perfekt passive: ist … worden (not geworden). The doer is introduced with von + dative.</p>'),
('B. lassen: vier Bedeutungen', 'B. lassen: four meanings',
 tbl(['Bedeutung', 'Beispiel'], [
  ['Jemand anderes macht es für mich', 'Ich <b>lasse</b> mein Auto <b>reparieren</b>. (Der Mechaniker repariert es.)'],
  ['erlauben', 'Meine Eltern <b>lassen</b> mich allein <b>reisen</b>.'],
  ['nicht mitnehmen, liegen lassen', 'Ich habe meinen Schirm im Zug <b>gelassen</b>.'],
  ['Vorschlag', '<b>Lass uns</b> morgen <b>telefonieren</b>!']]) +
 tbl(['', 'lassen'], [['ich', 'lasse'], ['du', 'lässt'], ['er/sie/es', 'lässt'], ['wir', 'lassen'], ['ihr', 'lasst'], ['sie/Sie', 'lassen']]) +
 '<p>Perfekt mit Infinitiv: <i>Ich habe mir die Haare schneiden <b>lassen</b>.</i> (nicht <i>gelassen</i>). Ohne Infinitiv: <i>Ich habe das Handy zu Hause <b>gelassen</b>.</i></p>',
 '<p>lassen + infinitive = have something done; also “allow”, “leave behind” and “let’s”. In the Perfekt with another infinitive it stays lassen (Ich habe mir die Haare schneiden lassen); alone it is gelassen.</p>')],
ex=[
('Die Brücke ___ 1950 gebaut.', ['wird', 'wurde', 'war'], 1, 'Jahreszahl in der Vergangenheit → wurde.', 'Year in the past → wurde.'),
('Die Briefe ___ gestern verschickt.', ['wurde', 'wurden', 'worden'], 1, 'Plural → wurden.', 'Plural → wurden.'),
('Das Fenster ist repariert ___.', ['geworden', 'worden', 'wurde'], 1, 'Passiv-Perfekt: worden.', 'Perfekt passive: worden.'),
('Das Bild wurde ___ einem jungen Künstler gemalt.', ['von', 'durch den', 'bei'], 0, 'Person im Passiv: von + Dativ.', 'Person in the passive: von + dative.'),
('Die Wohnung muss noch geputzt ___.', ['wurden', 'werden', 'worden'], 1, 'Modalverb + Partizip II + werden.', 'Modal + past participle + werden.'),
('Ich repariere mein Fahrrad nicht selbst. Ich ___ es reparieren.', ['lasse', 'lässt', 'werde'], 0, 'ich lasse.', 'ich lasse.'),
('Er ___ sich die Haare schneiden.', ['lasst', 'lässt', 'lassen'], 1, 'er lässt.', 'er lässt.'),
('Ich habe meine Jacke im Restaurant ___.', ['lassen', 'gelassen', 'gelasst'], 1, 'Ohne Infinitiv: gelassen.', 'Without an infinitive: gelassen.'),
('Ich habe mein Auto waschen ___.', ['gelassen', 'lassen', 'gelasst'], 1, 'Mit Infinitiv: lassen.', 'With an infinitive: lassen.'),
('„Meine Chefin lässt mich früher gehen.“ bedeutet:', ['Sie erlaubt es mir.', 'Sie schickt mich weg.', 'Sie geht früher.'], 0, 'lassen = erlauben.', 'lassen = allow.'),
('___ uns am Wochenende einen Ausflug machen!', ['Lass', 'Lässt', 'Gelassen'], 0, 'Lass uns … = Vorschlag.', 'Lass uns … = suggestion.'),
('„Das Museum wurde 2010 eröffnet.“ Welche Zeit?', ['Passiv Präsens', 'Passiv Präteritum', 'Futur'], 1, 'wurde + Partizip II.', 'wurde + past participle.')]))

# ---------------------------------------------------------------- N9
L.append(dict(
id='N9', t='n-Deklination, man/jemand/niemand, Wortbildung', te='n-declension, indefinite pronouns, word formation',
where='Sprachbausteine Teil 1 und 2 · Lesen · Schreiben (Anrede)', wen='Language elements parts 1 and 2 · Reading · Writing (greeting)',
goal='Du erkennst Nomen mit n-Deklination, benutzt Indefinitpronomen richtig und errätst neue Wörter durch ihre Bausteine.',
goalen='You recognise n-declension nouns, use indefinite pronouns correctly and guess new words from their parts.',
sec=[
('A. n-Deklination: der Kollege → den Kollegen', 'A. n-declension: der Kollege → den Kollegen',
 '<p>Einige <b>maskuline</b> Nomen bekommen in allen Fällen außer dem Nominativ Singular ein <b>-(e)n</b>. Typisch: Nomen auf <b>-e</b> (der Kollege, Kunde, Junge, Name), auf <b>-ent, -ant, -ist</b> (der Student, Praktikant, Polizist) und: der Herr, Mensch, Nachbar.</p>' +
 tbl(['Fall', 'Singular', 'Beispiel'], [['Nominativ', 'der Kollege', 'Mein Kollege kommt aus Polen.'], ['Akkusativ', 'den Kolleg<b>en</b>', 'Ich frage meinen Kolleg<b>en</b>.'], ['Dativ', 'dem Kolleg<b>en</b>', 'Ich helfe dem Kolleg<b>en</b>.'], ['Genitiv', 'des Kolleg<b>en</b>', 'das Auto des Kolleg<b>en</b>']]) +
 '<p><b>Herr:</b> Singular <i>Herrn</i> (außer Nominativ), Plural <i>Herren</i>. Brief: <i>Sehr geehrter <b>Herr</b> Klein</i> (Anrede = Nominativ), aber auf dem Umschlag: <i>an <b>Herrn</b> Klein</i>.</p>',
 '<p>Some masculine nouns take -(e)n in every case except nominative singular: nouns in -e, -ent, -ant, -ist, and Herr, Mensch, Nachbar. Herr → Herrn (singular), Herren (plural). In a letter greeting: Sehr geehrter Herr Klein; on an envelope: an Herrn Klein.</p>'),
('B. Indefinitpronomen', 'B. Indefinite pronouns',
 tbl(['Wort', 'Bedeutung', 'Beispiel'], [
  ['man (Akk. einen, Dat. einem)', 'people in general; Verb wie er', 'Hier <b>darf man</b> nicht parken.'],
  ['jemand / niemand', 'somebody / nobody (Akk. jemanden, Dat. jemandem)', 'Ist <b>jemand</b> da? · Ich kenne <b>niemanden</b> hier.'],
  ['etwas / nichts', 'something / nothing', 'Möchtest du <b>etwas</b> trinken? – Nein, <b>nichts</b>, danke.'],
  ['einer / eine / eins', 'one (of them)', 'Hast du einen Stift? – Ja, ich habe <b>einen</b>.'],
  ['keiner / keine / keins', 'none', 'Nein, ich habe <b>keinen</b>.'],
  ['welche', 'some (Plural, unzählbar)', 'Brauchst du Eier? – Ja, ich brauche <b>welche</b>.'],
  ['alle / viele / einige / manche', 'all / many / some / some', '<b>Viele</b> arbeiten am Wochenende.']]),
 '<p>man takes the er-form of the verb. einer/keiner change like ein/kein. welche replaces plural or uncountable nouns.</p>'),
('C. Wortbildung: Wörter erraten', 'C. Word formation: guessing words',
 tbl(['Baustein', 'Bedeutung / Genus', 'Beispiele'], [
  ['-ung, -heit, -keit, -ion, -tät, -schaft', 'Nomen, immer <b>die</b>', 'die Wohnung, die Gesundheit, die Möglichkeit, die Information, die Universität, die Freundschaft'],
  ['-chen, -lein, -ment, -um', 'Nomen, <b>das</b>', 'das Mädchen, das Dokument, das Zentrum'],
  ['-er (Person) / -in', 'der Lehrer / die Lehrerin', 'der Fahrer, die Ärztin'],
  ['das + Infinitiv', 'die Tätigkeit', 'das Lesen, das Schwimmen'],
  ['-lich, -ig, -isch', 'Adjektiv', 'freundlich, lustig, praktisch'],
  ['-bar', 'kann man …', 'essbar = kann man essen, erreichbar'],
  ['-los / un-', 'ohne / nicht', 'arbeitslos = ohne Arbeit, unmöglich = nicht möglich'],
  ['Kompositum', 'das <b>letzte</b> Wort bestimmt Genus und Bedeutung', 'das Haus + <b>die Tür</b> → die Haustür; die Bahn + <b>der Hof</b> → der Bahnhof']]),
 '<p>Endings tell you the gender and the word type: -ung/-heit/-keit/-ion/-tät/-schaft are feminine; -chen/-ment/-um neuter. -bar = can be done, -los = without, un- = not. In compound nouns, the last word decides gender and core meaning.</p>')],
ex=[
('Ich habe gestern meinen ___ getroffen.', ['Kollege', 'Kollegen', 'Kollegem'], 1, 'n-Deklination, Akkusativ: Kollegen.', 'n-declension, accusative: Kollegen.'),
('Der Brief ist an ___ Schmidt.', ['Herr', 'Herrn', 'Herren'], 1, 'an + Akkusativ: Herrn.', 'an + accusative: Herrn.'),
('Anrede in einer formellen E-Mail:', ['Sehr geehrter Herrn Weber,', 'Sehr geehrter Herr Weber,', 'Sehr geehrte Herren Weber,'], 1, 'Anrede = Nominativ: Herr.', 'Greeting = nominative: Herr.'),
('Der Arzt spricht mit dem ___.', ['Patient', 'Patienten', 'Patiente'], 1, '-ent → n-Deklination, Dativ: Patienten.', '-ent nouns take -en in the dative.'),
('In der Bibliothek ___ man leise sprechen.', ['müssen', 'muss', 'musst'], 1, 'man + er-Form: muss.', 'man + er-form: muss.'),
('Kennst du hier ___? – Nein, ich kenne niemanden.', ['jemand', 'jemanden', 'jemandem'], 1, 'kennen + Akkusativ: jemanden.', 'kennen + accusative: jemanden.'),
('Hast du ein Fahrrad? – Nein, ich habe ___.', ['keins', 'keinen', 'nichts'], 0, 'das Fahrrad → keins.', 'das Fahrrad → keins.'),
('Wir haben keine Äpfel mehr. Kannst du ___ kaufen?', ['einen', 'welche', 'etwas'], 1, 'Plural → welche.', 'Plural → welche.'),
('Welches Genus hat „Möglichkeit“?', ['der', 'die', 'das'], 1, '-keit → die.', '-keit → die.'),
('Was bedeutet „Das Wasser ist nicht trinkbar“?', ['Man kann das Wasser nicht trinken.', 'Das Wasser ist sehr kalt.', 'Man muss das Wasser trinken.'], 0, '-bar = kann man.', '-bar = can be done.'),
('„die Kinder + der Garten“ → ___ Kindergarten', ['die', 'der', 'das'], 1, 'Das letzte Wort bestimmt: der Garten.', 'The last word decides: der Garten.'),
('„arbeitslos“ bedeutet:', ['viel Arbeit', 'ohne Arbeit', 'bei der Arbeit'], 1, '-los = ohne.', '-los = without.')]))
