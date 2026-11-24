# -*- coding: utf-8 -*-
# Additional lessons N10-N18: gap-filling lessons for Phase 2 of the 60-day plan.
# Same structure as content.py (id, t, te, where, wen, goal, goalen, sec, ex).
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import say, tbl

L2 = []

# ---------------------------------------------------------------- N10
L2.append(dict(
 id='N10', t='Wortstellung: Satzklammer und Mittelfeld', te='Word order: the verb frame and the middle field',
 where='Sprachbausteine · Schreiben · Sprechen (richtige Sätze bauen)', wen='Language elements · Writing · Speaking (building correct sentences)',
 goal='Du baust Sätze mit der richtigen Wortstellung: Verb auf Position 2, Satzklammer, Reihenfolge im Mittelfeld und Nebensatz mit Verb am Ende.',
 goalen='You build sentences with the right word order: verb in position 2, verb frame, order in the middle field and subordinate clauses with the verb at the end.',
 sec=[
 ['A. Das Verb steht auf Position 2', 'A. The verb is in position 2',
  '<p>Im Aussagesatz steht das <b>konjugierte Verb immer auf Position 2</b>. Auf Position 1 kann fast alles stehen. Wenn nicht das Subjekt auf Position 1 steht, kommt das Subjekt direkt nach dem Verb (Inversion).</p>'
  + tbl(['Position 1', 'Position 2 (Verb)', 'Rest'], [
   ['Ich', '<b>gehe</b>', 'morgen ins Kino.'], ['Morgen', '<b>gehe</b>', 'ich ins Kino.'], ['Ins Kino', '<b>gehe</b>', 'ich morgen.'],
   ['Leider', '<b>habe</b>', 'ich keine Zeit.'], ['Deshalb', '<b>möchte</b>', 'ich Sie um Hilfe bitten.']])
  + '<p><b>Ja/Nein-Frage:</b> Verb auf Position 1: <i>Kommst du morgen?</i> · <b>W-Frage:</b> Fragewort auf Position 1, Verb auf Position 2: <i>Wann kommst du?</i></p>'
  '<p><b>Wichtig:</b> Die Konnektoren <i>und, aber, oder, denn, sondern</i> zählen nicht als Position 1: <i>Ich bin müde, aber ich komme.</i> Dagegen <i>deshalb, trotzdem, außerdem</i> stehen auf Position 1, danach kommt das Verb: <i>Ich bin müde, trotzdem komme ich.</i></p>',
  '<p>In a statement the conjugated verb is always in position 2. If the subject is not in position 1 it follows the verb. Yes/no questions: verb first. W-questions: question word first, verb second. und, aber, oder, denn, sondern do not count as position 1; deshalb, trotzdem, außerdem do.</p>'],
 ['B. Die Satzklammer', 'B. The verb frame',
  '<p>Bei zwei Verbteilen steht das <b>konjugierte Verb auf Position 2</b> und der <b>zweite Teil am Satzende</b>. Dazwischen steht alles andere. So entsteht die Satzklammer.</p>'
  + tbl(['Fall', 'Beispiel'], [
   ['Modalverb + Infinitiv', 'Ich <b>muss</b> heute lange <b>arbeiten</b>.'], ['Perfekt', 'Ich <b>habe</b> dir gestern eine E-Mail <b>geschrieben</b>.'],
   ['trennbares Verb', 'Ich <b>rufe</b> dich morgen Abend <b>an</b>.'], ['Futur', 'Wir <b>werden</b> im Sommer nach Indien <b>fliegen</b>.'],
   ['Passiv', 'Die Wohnung <b>wird</b> nächste Woche <b>renoviert</b>.'], ['Konjunktiv II', 'Könnten Sie mir bitte einen Termin <b>geben</b>?']])
  + '<p>Im Prüfungstext suchst du in einer Lücke oft das <b>Ende der Klammer</b>: Wenn vorn <i>hat/ist/muss/wird</i> steht, brauchst du hinten Partizip II oder Infinitiv.</p>',
  '<p>With two verb parts the conjugated verb is in position 2 and the second part is at the end of the sentence. Everything else sits in between. In a gap text, look for the end of the frame: after hat/ist you need a participle, after muss/wird an infinitive.</p>'],
 ['C. Reihenfolge im Mittelfeld', 'C. Order in the middle field',
  '<p>Zwischen den beiden Teilen der Klammer steht das Mittelfeld. Merke diese Reihenfolge:</p>'
  + tbl(['Regel', 'Beispiel'], [
   ['<b>Zeit – Grund – Art – Ort</b> (temporal, kausal, modal, lokal)', 'Ich fahre <b>morgen</b> <b>wegen des Wetters</b> <b>mit dem Zug</b> <b>nach Berlin</b>.'],
   ['<b>Pronomen vor Nomen</b>', 'Ich gebe <b>es</b> meinem Bruder. · Ich gebe <b>ihm</b> das Buch.'],
   ['Dativ vor Akkusativ (zwei Nomen)', 'Ich schenke <b>meiner Mutter</b> <b>einen Blumenstrauß</b>.'],
   ['zwei Pronomen: Akkusativ vor Dativ', 'Ich gebe <b>es dir</b>. · Er zeigt <b>sie uns</b>.'],
   ['<b>nicht</b> steht meist vor dem Teil, den du verneinst, oder am Ende', 'Ich komme <b>nicht</b> heute. · Ich gehe heute <b>nicht</b>. · Ich habe das Buch <b>nicht</b> gelesen.']])
  , '<p>Order in the middle field: time – reason – manner – place. Pronouns come before nouns. With two nouns: dative before accusative. With two pronouns: accusative before dative (ich gebe es dir). nicht usually comes before the part you negate, or at the end.</p>'],
 ['D. Haupt- und Nebensatz', 'D. Main clause and subordinate clause',
  '<p>Im <b>Nebensatz</b> (weil, dass, wenn, obwohl, als, nachdem, ob, damit …) steht das <b>konjugierte Verb am Ende</b>. Mit zwei Verben steht das konjugierte Verb ganz am Schluss. Mit einem Komma trennst du die Sätze.</p>'
  + tbl(['Satz', 'Beispiel'], [
   ['Hauptsatz – Nebensatz', 'Ich bleibe zu Hause, <b>weil</b> ich krank <b>bin</b>.'],
   ['Nebensatz mit Perfekt', 'Ich bin zu spät gekommen, <b>weil</b> der Bus nicht gefahren <b>ist</b>.'],
   ['Nebensatz mit Modalverb', 'Ich rufe an, <b>weil</b> ich eine Frage stellen <b>möchte</b>.'],
   ['Nebensatz zuerst: danach Verb auf Position 1', '<b>Weil</b> ich krank <b>bin</b>, <b>bleibe</b> ich zu Hause.'],
   ['trennbares Verb im Nebensatz', 'Ich weiß nicht, <b>wann</b> der Zug <b>ankommt</b>. (Im Nebensatz wird ankommen zusammengeschrieben.)'],
   ['Infinitiv mit zu', 'Ich habe keine Zeit, ins Kino <b>zu gehen</b>. · Ich fange an, Deutsch <b>zu lernen</b>.']])
  + '<p>Steht der Nebensatz <b>vor</b> dem Hauptsatz, ist der ganze Nebensatz Position 1. Darum kommt danach direkt das Verb des Hauptsatzes.</p>',
  '<p>In a subordinate clause the conjugated verb goes to the end; with two verbs the conjugated verb is last. If the subordinate clause comes first it counts as position 1, so the verb of the main clause follows directly.</p>'],
 ['E. Typische Fehler und Prüfungstipp', 'E. Typical mistakes and exam tip',
  '<ul class="tight"><li>✗ <i>Morgen ich gehe ins Kino.</i> → ✓ <i>Morgen gehe ich ins Kino.</i> (Verb auf Position 2)</li>'
  '<li>✗ <i>Ich bleibe zu Hause, weil ich bin krank.</i> → ✓ <i>… weil ich krank bin.</i></li>'
  '<li>✗ <i>Ich habe gekauft ein Buch.</i> → ✓ <i>Ich habe ein Buch gekauft.</i></li>'
  '<li>✗ <i>Ich möchte gehen nach Hause.</i> → ✓ <i>Ich möchte nach Hause gehen.</i></li>'
  '<li>✗ <i>Deshalb ich komme nicht.</i> → ✓ <i>Deshalb komme ich nicht.</i></li></ul>'
  '<div class="tip"><b>Tipp für die E-Mail im Schreiben:</b> Lies jeden Satz nach dem Schreiben noch einmal und suche das Verb. Steht es im Hauptsatz auf Position 2? Steht es im Nebensatz am Ende? Diese zwei Kontrollen bringen schon viele Punkte bei „Korrektheit“.</div>',
  '<p>Typical mistakes: the verb not in position 2 (Morgen ich gehe), the verb not at the end in weil clauses, participle or infinitive not at the end of the sentence. Tip for the email: after writing, check where the verb is in every sentence.</p>'],
 ],
 ex=[
 ['Welcher Satz ist richtig?', ['Morgen ich fahre nach Köln.', 'Morgen fahre ich nach Köln.', 'Morgen fahre nach Köln ich.'], 1, 'Verb auf Position 2, dann das Subjekt.', 'Verb in position 2, then the subject.'],
 ['Ich habe gestern meinen Freund ___.', ['besucht', 'besuchen', 'besuche'], 0, 'Perfekt: haben … + Partizip II am Satzende.', 'Perfect: haben … + participle at the end.'],
 ['Ich bleibe zu Hause, weil ich krank ___.', ['bin', 'ich bin', 'sein'], 0, 'Im weil-Satz steht das Verb am Ende: … weil ich krank bin.', 'In a weil clause the verb goes last.'],
 ['Welcher Satz ist richtig?', ['Ich rufe an dich morgen.', 'Ich rufe dich morgen an.', 'Ich anrufe dich morgen.'], 1, 'Trennbares Verb: rufe … an (Klammer).', 'Separable verb: rufe … an.'],
 ['Ich möchte ___.', ['nach Hause gehen', 'gehen nach Hause', 'nach gehen Hause'], 0, 'Modalverb auf Position 2, Infinitiv am Ende.', 'Modal verb in position 2, infinitive at the end.'],
 ['Er ist müde, ___ arbeitet er noch.', ['trotzdem', 'aber', 'weil'], 0, 'trotzdem steht auf Position 1, danach kommt das Verb: …, trotzdem arbeitet er noch.', 'trotzdem takes position 1, then the verb follows.'],
 ['Ich gebe ___.', ['es dir', 'dir es', 'dir das es'], 0, 'Zwei Pronomen: Akkusativ vor Dativ (es dir).', 'Two pronouns: accusative before dative (es dir).'],
 ['Wähle den richtigen Satz.', ['Ich schenke einen Blumenstrauß meiner Mutter.', 'Ich schenke meiner Mutter einen Blumenstrauß.', 'Ich meiner Mutter schenke einen Blumenstrauß.'], 1, 'Zwei Nomen: Dativ vor Akkusativ.', 'Two nouns: dative before accusative.'],
 ['Ich fahre ___ nach Berlin.', ['morgen mit dem Zug', 'mit dem Zug morgen', 'nach Berlin morgen mit dem Zug'], 0, 'Zeit vor Art und Weise (morgen, mit dem Zug), danach der Ort.', 'Time before manner, then place.'],
 ['Wenn es regnet, ___ ich zu Hause.', ['bleibe', 'ich bleibe', 'bleiben'], 0, 'Der Nebensatz ist Position 1, danach steht sofort das Verb des Hauptsatzes.', 'The subordinate clause counts as position 1, so the verb follows.'],
 ['Ich weiß nicht, wann der Zug ___.', ['ankommt', 'kommt an', 'an kommt'], 0, 'Im Nebensatz steht das Verb am Ende und wird zusammengeschrieben.', 'In a subordinate clause the separable verb is written as one word at the end.'],
 ['Ich habe keine Zeit, ins Kino ___ ___.', ['zu gehen', 'gehen zu', 'zu gegangen'], 0, 'Infinitiv mit zu: zu gehen.', 'Infinitive with zu: zu gehen.'],
 ['Wann ___ der Kurs?', ['beginnt', 'der Kurs beginnt', 'beginnen'], 0, 'W-Frage: Fragewort, dann Verb auf Position 2.', 'W-question: question word, then the verb.'],
 ['Welcher Satz ist richtig?', ['Ich habe das Buch nicht gelesen.', 'Ich habe nicht gelesen das Buch.', 'Ich nicht habe das Buch gelesen.'], 0, 'Das Partizip steht am Ende, nicht vor dem Partizip.', 'The participle is last, nicht comes before it.'],
 ['Welcher Nebensatz ist richtig?', ['Ich rufe an, weil ich möchte eine Frage stellen.', 'Ich rufe an, weil ich eine Frage stellen möchte.', 'Ich rufe an, weil möchte ich eine Frage stellen.'], 1, 'Im Nebensatz steht das konjugierte Verb ganz am Ende (… stellen möchte).', 'The conjugated verb is last (stellen möchte).'],
 ]))

# ---------------------------------------------------------------- N11
L2.append(dict(
 id='N11', t='Artikelwörter, Possessivartikel und Personalpronomen', te='Articles, possessive articles and personal pronouns',
 where='Sprachbausteine Teil 1 · Lesen · Schreiben (richtige Endungen)', wen='Language elements part 1 · Reading · Writing (correct endings)',
 goal='Du wählst den richtigen Artikel und das richtige Pronomen im Nominativ, Akkusativ, Dativ und Genitiv.',
 goalen='You choose the right article and the right pronoun in nominative, accusative, dative and genitive.',
 sec=[
 ['A. Der bestimmte und der unbestimmte Artikel', 'A. Definite and indefinite article',
  tbl(['Kasus', 'der-Wort', 'die-Wort', 'das-Wort', 'Plural'], [
   ['Nominativ', 'der / ein', 'die / eine', 'das / ein', 'die / –'], ['Akkusativ', '<b>den / einen</b>', 'die / eine', 'das / ein', 'die / –'],
   ['Dativ', '<b>dem / einem</b>', '<b>der / einer</b>', '<b>dem / einem</b>', '<b>den</b> + n / –'], ['Genitiv', 'des / eines + (e)s', 'der / einer', 'des / eines + (e)s', 'der / –']])
  + '<p><b>Merke:</b> Nur das <b>der-Wort</b> ändert sich im Akkusativ (der → den). <b>kein</b> und die Possessivartikel (mein, dein …) haben dieselben Endungen wie <b>ein</b>, im Plural wie <b>die</b>: <i>meine Eltern, keine Zeit</i>. Im Dativ Plural bekommt das Nomen ein <b>-n</b>: <i>mit den Kindern</i>.</p>',
  '<p>Only the masculine changes in the accusative (der → den). kein and the possessive articles have the same endings as ein (plural like die). In the dative plural the noun gets an -n: mit den Kindern.</p>'],
 ['B. Possessivartikel', 'B. Possessive articles',
  tbl(['Person', 'Possessivartikel', 'Beispiel'], [
   ['ich', 'mein-', 'mein Bruder · meine Frau'], ['du', 'dein-', 'dein Bus · deine E-Mail'], ['er / es', 'sein-', 'sein Auto · seine Mutter'], ['sie (she)', 'ihr-', 'ihr Hund · ihre Tochter'],
   ['wir', 'unser-', 'unser Haus · unsere Wohnung (Akk. m.: unseren)'], ['ihr', 'euer-', 'euer Lehrer · eure Kinder (Akk. m.: euren)'], ['sie (they) / Sie', 'ihr- / Ihr-', 'ihre Eltern · Ihre Anmeldung (Sie: großgeschrieben!)']])
  + '<p><b>Wichtig:</b> Der Possessivartikel richtet sich nach <b>dem Besitzer</b> (sein/ihr), die Endung nach <b>dem Nomen</b>: <i>Er liebt seine Frau. · Sie liebt ihren Mann.</i> In formellen E-Mails schreibst du <b>Sie, Ihnen, Ihr, Ihre</b> immer groß.</p>',
  '<p>The possessive article depends on the owner (sein/ihr), the ending on the noun. In formal emails Sie, Ihnen, Ihr, Ihre are always capitalised.</p>'],
 ['C. dieser, jeder, welcher', 'C. dieser, jeder, welcher',
  '<p>Diese Wörter haben die Endungen des bestimmten Artikels: <i>dieser Tisch, diesen Tisch, diesem Tisch · diese Frau · dieses Kind · diese Leute</i>. Genauso: <b>jeder</b> (jeden Tag, jedem Kind), <b>welcher</b> (Welchen Kurs nimmst du?), <b>mancher, solcher, alle</b>.</p>'
  '<p>Fragen: <b>Welcher</b> Kurs? (Auswahl) · <b>Was für ein</b> Kurs? (Art, Eigenschaft: <i>Was für einen Kurs suchst du?</i>)</p>',
  '<p>dieser, jeder, welcher take the endings of the definite article. Welcher asks for a choice, was für ein asks for the kind.</p>'],
 ['D. Personalpronomen', 'D. Personal pronouns',
  tbl(['Nominativ', 'Akkusativ', 'Dativ', 'Beispiel'], [
   ['ich', 'mich', 'mir', 'Er ruft mich an. · Das gefällt mir.'], ['du', 'dich', 'dir', 'Ich helfe dir. · Ich sehe dich.'], ['er', 'ihn', 'ihm', 'Ich kenne ihn. · Ich gebe ihm das Buch.'],
   ['sie', 'sie', 'ihr', 'Ich besuche sie. · Ich schreibe ihr.'], ['es', 'es', 'ihm', 'Ich kaufe es. · Wir geben ihm Zeit.'], ['wir', 'uns', 'uns', 'Er lädt uns ein. · Er hilft uns.'],
   ['ihr', 'euch', 'euch', 'Ich rufe euch an. · Ich danke euch.'], ['sie (they)', 'sie', 'ihnen', 'Ich sehe sie. · Ich glaube ihnen.'], ['Sie', 'Sie', 'Ihnen', 'Ich rufe Sie an. · Ich danke Ihnen.']])
  + '<p><b>Verben mit Dativ:</b> helfen, danken, gefallen, gehören, schmecken, passen, antworten, gratulieren, fehlen, zuhören. <i>Das Buch gehört mir. · Die Pizza schmeckt ihm.</i></p>'
  '<p><b>Reihenfolge:</b> Pronomen vor Nomen (<i>Ich gebe ihm das Buch</i>), zwei Pronomen: Akkusativ vor Dativ (<i>Ich gebe es ihm</i>).</p>',
  '<p>Many verbs take the dative: helfen, danken, gefallen, gehören, schmecken, passen, antworten, gratulieren, fehlen. Pronouns before nouns; with two pronouns accusative before dative.</p>'],
 ['E. Typische Prüfungsfehler', 'E. Typical exam mistakes',
  '<ul class="tight"><li>✗ <i>Ich habe ein Frage.</i> → ✓ <i>eine Frage</i> (die Frage).</li><li>✗ <i>Ich sehe der Mann.</i> → ✓ <i>den Mann</i> (Akkusativ).</li>'
  '<li>✗ <i>mit der Freund</i> → ✓ <i>mit dem Freund</i> (mit + Dativ).</li><li>✗ <i>Ich danke dich.</i> → ✓ <i>Ich danke dir.</i></li>'
  '<li>✗ <i>Sie hat ihr Mann gesehen.</i> → ✓ <i>ihren Mann</i> (Akkusativ maskulin).</li></ul>'
  '<div class="tip"><b>Tipp für Sprachbausteine Teil 1:</b> Frage dich bei jeder Lücke: Welches Genus hat das Nomen? Welcher Kasus kommt vom Verb oder von der Präposition? Dann erst wählst du die Form.</div>',
  '<p>Typical mistakes: wrong gender or case after a verb or preposition. Tip: ask for the gender of the noun and the case required by the verb or preposition, then choose the form.</p>'],
 ],
 ex=[
 ['Ich sehe ___ Mann.', ['der', 'den', 'dem'], 1, 'Mann ist maskulin, sehen verlangt den Akkusativ: den Mann.', 'masculine accusative: den.'],
 ['Wir fahren mit ___ Bus.', ['dem', 'den', 'der'], 0, 'mit + Dativ, Bus ist maskulin: mit dem Bus.', 'mit + dative: dem.'],
 ['Hast du ___ Frage?', ['ein', 'eine', 'einen'], 1, 'Frage ist feminin: eine Frage.', 'Frage is feminine: eine.'],
 ['Das ist ___ Tasche. (er hat eine Tasche)', ['seine', 'ihre', 'sein'], 0, 'Der Besitzer ist er: sein-; Tasche ist feminin: seine Tasche.', 'owner = er: sein-; Tasche feminine: seine.'],
 ['Sie liebt ___ Mann. (der Mann gehört zu ihr)', ['ihr', 'ihren', 'ihrem'], 1, 'Akkusativ maskulin: ihren Mann.', 'accusative masculine: ihren.'],
 ['Ich danke ___ für die Hilfe. (du)', ['dich', 'dir', 'du'], 1, 'danken + Dativ: dir.', 'danken + dative: dir.'],
 ['Das Buch gehört ___. (ich)', ['mich', 'mir', 'mein'], 1, 'gehören + Dativ: mir.', 'gehören + dative: mir.'],
 ['Ich rufe ___ morgen an. (Sie, formell)', ['Sie', 'Ihnen', 'Ihr'], 0, 'anrufen + Akkusativ: Sie.', 'anrufen + accusative: Sie.'],
 ['Ich gebe ___ das Buch. (er)', ['ihn', 'ihm', 'er'], 1, 'geben + Dativ der Person: ihm.', 'dative of the person: ihm.'],
 ['In ___ Stadt wohnst du? (Frage nach der Auswahl)', ['Welcher', 'Welchen', 'Welcher Stadt'], 0, 'Dativ feminin: in welcher Stadt. (Welcher gehört zum Nomen Stadt.)', 'dative feminine: in welcher Stadt.'],
 ['Er hilft ___ Kindern.', ['die', 'den', 'dem'], 1, 'helfen + Dativ Plural: den Kindern.', 'dative plural: den Kindern.'],
 ['Ich kaufe ___ Auto. (unser, das Auto: Akkusativ)', ['unser', 'unseren', 'unsere'], 0, 'Auto ist ein das-Wort; ohne Endung im Nominativ/Akkusativ: unser Auto.', 'neuter nominative/accusative: no ending, unser Auto.'],
 ['Wir laden ___ Eltern ein. (ihr: eure)', ['euer', 'eure', 'eurer'], 1, 'Plural Akkusativ: eure Eltern.', 'plural accusative: eure Eltern.'],
 ['Die Pizza schmeckt ___ gut. (wir)', ['uns', 'wir', 'unser'], 0, 'schmecken + Dativ: uns.', 'schmecken + dative: uns.'],
 ['Wähle die richtige Reihenfolge.', ['Ich gebe dir es.', 'Ich gebe es dir.', 'Ich es gebe dir.'], 1, 'Zwei Pronomen: Akkusativ (es) vor Dativ (dir).', 'two pronouns: accusative (es) before dative (dir).'],
 ]))

# ---------------------------------------------------------------- N12
L2.append(dict(
 id='N12', t='Reflexive Verben und Reflexivpronomen', te='Reflexive verbs and reflexive pronouns',
 where='Sprachbausteine · Schreiben (E-Mail) · Sprechen', wen='Language elements · Writing (email) · Speaking',
 goal='Du erkennst reflexive Verben und benutzt mich/mir, dich/dir, sich, uns, euch richtig, auch mit Präposition.',
 goalen='You recognise reflexive verbs and use mich/mir, dich/dir, sich, uns, euch correctly, also with prepositions.',
 sec=[
 ['A. Die Formen', 'A. The forms',
  tbl(['Person', 'Akkusativ', 'Dativ', 'Beispiel'], [
   ['ich', 'mich', 'mir', 'Ich freue <b>mich</b>. · Ich wasche <b>mir</b> die Hände.'], ['du', 'dich', 'dir', 'Du beeilst <b>dich</b>. · Du kaufst <b>dir</b> ein Buch.'],
   ['er / sie / es', '<b>sich</b>', '<b>sich</b>', 'Er interessiert <b>sich</b> für Technik.'], ['wir', 'uns', 'uns', 'Wir treffen <b>uns</b> um acht.'], ['ihr', 'euch', 'euch', 'Ihr müsst <b>euch</b> anmelden.'], ['sie / Sie', '<b>sich</b>', '<b>sich</b>', 'Sie bewerben <b>sich</b> um die Stelle.']])
  + '<p>Nur in der <b>1. und 2. Person Singular</b> unterscheidet man Akkusativ und Dativ (mich/mir, dich/dir). In allen anderen Formen ist die Form gleich.</p>'
  '<p>Das Reflexivpronomen steht für dieselbe Person wie das Subjekt: <i>Ich wasche mich.</i> (ich = mich) · <i>Ich wasche ihn.</i> (zwei Personen: kein Reflexivpronomen)</p>',
  '<p>A reflexive pronoun refers back to the subject. Only for ich and du do accusative and dative differ (mich/mir, dich/dir); for er/sie/es and sie/Sie the form is always sich.</p>'],
 ['B. Wichtige reflexive Verben', 'B. Important reflexive verbs',
  tbl(['Verb', 'Beispiel'], [
   ['sich freuen (auf + Akk. / über + Akk.)', 'Ich freue mich <b>auf</b> den Urlaub. · Ich freue mich <b>über</b> dein Geschenk.'], ['sich interessieren für + Akk.', 'Er interessiert sich <b>für</b> Musik.'],
   ['sich ärgern über + Akk.', 'Ich ärgere mich <b>über</b> den Lärm.'], ['sich beschweren über + Akk. / bei + Dat.', 'Ich beschwere mich <b>über</b> den Lärm <b>bei</b> der Hausverwaltung.'],
   ['sich bewerben um / bei', 'Ich bewerbe mich <b>um</b> die Stelle <b>bei</b> Ihrer Firma.'], ['sich kümmern um + Akk.', 'Er kümmert sich <b>um</b> die Kinder.'],
   ['sich vorbereiten auf + Akk.', 'Wir bereiten uns <b>auf</b> die Prüfung vor.'], ['sich entscheiden für + Akk.', 'Ich habe mich <b>für</b> den Kurs entschieden.'],
   ['sich erinnern an + Akk.', 'Ich erinnere mich <b>an</b> den Tag.'], ['sich gewöhnen an + Akk.', 'Ich gewöhne mich <b>an</b> das Wetter.'],
   ['sich beschäftigen mit + Dat.', 'Sie beschäftigt sich <b>mit</b> Fotografie.'], ['sich verabreden / treffen / sehen mit', 'Ich treffe mich <b>mit</b> meiner Freundin.'],
   ['sich anmelden / abmelden (für / bei)', 'Ich melde mich <b>für</b> den Kurs an.'], ['sich beeilen, sich entschuldigen, sich setzen, sich fühlen', 'Beeil dich! · Ich fühle mich gut. · Bitte setzen Sie sich.']])
  + '<p>Viele dieser Verben haben eine feste <b>Präposition</b>. Lerne Verb + Präposition + Kasus zusammen (siehe auch N13).</p>',
  '<p>Many reflexive verbs have a fixed preposition. Learn verb + preposition + case together (see N13).</p>'],
 ['C. Reflexivpronomen im Dativ', 'C. Reflexive pronouns in the dative',
  '<p>Wenn schon ein <b>Akkusativobjekt</b> im Satz steht, ist das Reflexivpronomen <b>Dativ</b> (mir, dir): <i>Ich wasche mir die Hände. · Ich putze mir die Zähne. · Ich kaufe mir ein Handy. · Stell dir vor! · Ich merke mir den Namen. · Ich nehme mir Zeit.</i></p>'
  '<p>Vergleich: <i>Ich wasche <b>mich</b>.</i> (kein Objekt) · <i>Ich wasche <b>mir</b> die Haare.</i> (Haare = Akkusativobjekt)</p>',
  '<p>If there is already an accusative object, the reflexive pronoun is dative: Ich wasche mir die Hände. Without another object it is accusative: Ich wasche mich.</p>'],
 ['D. Wo steht das Reflexivpronomen?', 'D. Where does the reflexive pronoun go?',
  tbl(['Satz', 'Beispiel'], [
   ['Hauptsatz', 'Ich freue <b>mich</b> auf das Wochenende.'], ['Inversion', 'Morgen treffe ich <b>mich</b> mit meinem Chef.'],
   ['Frage', 'Interessierst du <b>dich</b> für Fußball?'], ['Nebensatz', 'Ich komme später, weil ich <b>mich</b> verspätet habe.'],
   ['Perfekt', 'Ich habe <b>mich</b> sehr gefreut. · Wir haben <b>uns</b> gut erholt.'], ['Imperativ', 'Beeil <b>dich</b>! · Setzen Sie <b>sich</b> bitte!'],
   ['trennbar', 'Ich melde <b>mich</b> für den Kurs <b>an</b>.'], ['Infinitiv mit zu', 'Ich habe vergessen, <b>mich</b> anzumelden.']])
  + '<p><b>Perfekt:</b> reflexive Verben bilden das Perfekt immer mit <b>haben</b>.</p>'
  '<p><b>Gegenseitig:</b> <i>Wir sehen uns morgen. · Sie lieben sich. · Wir schreiben uns oft.</i> (= einander)</p>',
  '<p>The reflexive pronoun usually comes right after the verb (or after the subject in questions and subordinate clauses). The perfect is formed with haben. uns/sich can also mean each other.</p>'],
 ['E. Prüfungstipp', 'E. Exam tip',
  '<div class="tip"><b>In der E-Mail:</b> Mit reflexiven Verben schreibst du natürliche Sätze: <i>Ich freue mich auf Ihre Antwort. · Ich möchte mich für den Kurs anmelden. · Ich beschwere mich über … · Ich interessiere mich für …</i> Diese vier Muster kannst du in fast jeder E-Mail benutzen.</div>'
  '<ul class="tight"><li>✗ <i>Ich freue mich über den Urlaub</i> (der Urlaub kommt noch) → ✓ <i>auf den Urlaub</i>.</li><li>✗ <i>Er interessiert sich über Musik.</i> → ✓ <i>für Musik</i>.</li><li>✗ <i>Ich habe mich ein Handy gekauft.</i> → ✓ <i>mir ein Handy</i>.</li></ul>',
  '<p>Four reflexive patterns work in nearly every email: Ich freue mich auf …, Ich möchte mich anmelden, Ich beschwere mich über …, Ich interessiere mich für … sich freuen auf = looking forward (future), über = being happy about something (present/past).</p>'],
 ],
 ex=[
 ['Ich freue ___ auf das Wochenende.', ['mich', 'mir', 'sich'], 0, 'sich freuen: ich → mich.', 'ich → mich.'],
 ['Er interessiert ___ für Technik.', ['sich', 'ihn', 'er'], 0, 'er → sich.', 'er → sich.'],
 ['Wir treffen ___ um acht Uhr.', ['uns', 'wir', 'sich'], 0, 'wir → uns.', 'wir → uns.'],
 ['Du musst ___ beeilen.', ['dir', 'dich', 'sich'], 1, 'sich beeilen: du → dich.', 'du → dich.'],
 ['Ich wasche ___ die Hände.', ['mich', 'mir', 'meine'], 1, 'Akkusativobjekt (die Hände) ist da: Dativ mir.', 'accusative object present: dative mir.'],
 ['Ich kaufe ___ ein neues Handy.', ['mich', 'mir', 'sich'], 1, 'Akkusativobjekt (Handy): mir.', 'dative mir.'],
 ['Ich habe ___ sehr gefreut.', ['mich', 'mir', 'sich'], 0, 'sich freuen im Perfekt: Ich habe mich gefreut.', 'perfect: Ich habe mich gefreut.'],
 ['Ich freue mich ___ deinen Besuch. (er kommt nächste Woche)', ['auf', 'über', 'für'], 0, 'Zukunft: sich freuen auf + Akkusativ.', 'future: sich freuen auf + accusative.'],
 ['Ich ärgere mich ___ den Lärm.', ['auf', 'über', 'an'], 1, 'sich ärgern über + Akkusativ.', 'sich ärgern über + accusative.'],
 ['Sie bewirbt sich ___ eine Stelle.', ['für', 'um', 'auf'], 1, 'sich bewerben um + Akkusativ.', 'sich bewerben um + accusative.'],
 ['Wir bereiten ___ auf die Prüfung vor.', ['uns', 'wir', 'unser'], 0, 'wir → uns; sich vorbereiten auf + Akkusativ.', 'wir → uns.'],
 ['Wähle die richtige Perfektform.', ['Ich bin mich angemeldet.', 'Ich habe mich angemeldet.', 'Ich habe angemeldet mich.'], 1, 'Reflexive Verben bilden das Perfekt mit haben; mich nach dem Hilfsverb.', 'reflexive verbs form the perfect with haben.'],
 ['___ Sie bitte!', ['Setzen Sie sich', 'Setzen sich Sie', 'Sie setzen sich'], 0, 'Imperativ Sie: Verb, Sie, sich.', 'imperative: verb, Sie, sich.'],
 ['Ich erinnere ___ ___ den Tag.', ['mich an', 'mir an', 'mich für'], 0, 'sich erinnern an + Akkusativ.', 'sich erinnern an + accusative.'],
 ['Wir sehen ___ morgen. (gegenseitig)', ['uns', 'wir', 'euch'], 0, 'wir sehen uns = we see each other.', 'wir sehen uns.'],
 ]))

# ---------------------------------------------------------------- N13
L2.append(dict(
 id='N13', t='Verben mit Präpositionen und Pronominaladverbien (darauf, worauf)', te='Verbs with prepositions and pronominal adverbs',
 where='Sprachbausteine Teil 1 und 2 · Lesen · Schreiben', wen='Language elements parts 1 and 2 · Reading · Writing',
 goal='Du kennst die wichtigsten Verben mit fester Präposition und bildest damit Fragen und Antworten: Worauf wartest du? Ich warte darauf.',
 goalen='You know the most important verbs with a fixed preposition and use them in questions and answers: Worauf wartest du? Ich warte darauf.',
 sec=[
 ['A. Verben mit fester Präposition', 'A. Verbs with a fixed preposition',
  '<p>Viele Verben verlangen eine bestimmte Präposition mit einem bestimmten Kasus. Die Präposition hat hier <b>keine wörtliche Bedeutung</b>: du musst sie mit dem Verb lernen.</p>'
  + tbl(['Verb + Präposition', 'Kasus', 'Beispiel'], [
   ['warten auf', 'Akk.', 'Ich warte auf den Bus.'], ['sich freuen auf / über', 'Akk.', 'Ich freue mich auf den Urlaub.'], ['denken an', 'Akk.', 'Ich denke oft an meine Familie.'],
   ['sich erinnern an', 'Akk.', 'Erinnerst du dich an den Termin?'], ['sich ärgern über', 'Akk.', 'Er ärgert sich über den Fehler.'], ['sprechen über', 'Akk.', 'Wir sprechen über das Wetter.'],
   ['sich interessieren für', 'Akk.', 'Sie interessiert sich für Kunst.'], ['sich bewerben um', 'Akk.', 'Ich bewerbe mich um die Stelle.'], ['sich kümmern um', 'Akk.', 'Wer kümmert sich um die Kinder?'],
   ['bitten um', 'Akk.', 'Ich bitte Sie um Hilfe.'], ['teilnehmen an', 'Dat.', 'Ich nehme an dem Kurs teil.'], ['arbeiten an', 'Dat.', 'Er arbeitet an einem Projekt.'],
   ['sich beschäftigen mit', 'Dat.', 'Sie beschäftigt sich mit Fotografie.'], ['sprechen mit / telefonieren mit', 'Dat.', 'Ich spreche mit meinem Chef.'], ['anfangen / beginnen mit', 'Dat.', 'Wir fangen mit dem Test an.'],
   ['träumen von', 'Dat.', 'Er träumt von einem Haus.'], ['erzählen von', 'Dat.', 'Sie erzählt von ihrer Reise.'], ['abhängen von', 'Dat.', 'Das hängt vom Wetter ab.'],
   ['leiden unter', 'Dat.', 'Wir leiden unter dem Lärm.'], ['gehören zu', 'Dat.', 'Das gehört zu meinem Job.'], ['sich verlassen auf', 'Akk.', 'Ich verlasse mich auf dich.'],
   ['Angst haben vor', 'Dat.', 'Er hat Angst vor der Prüfung.'], ['achten auf', 'Akk.', 'Achte auf die Zeit!'], ['sich vorbereiten auf', 'Akk.', 'Ich bereite mich auf den Test vor.']])
  , '<p>Many verbs take a fixed preposition with a fixed case. The preposition has no literal meaning, so learn it together with the verb. Accusative: warten auf, denken an, sich ärgern über, sprechen über, sich interessieren für. Dative: teilnehmen an, sich beschäftigen mit, träumen von, Angst haben vor.</p>'],
 ['B. Pronominaladverbien: da(r) + Präposition', 'B. Pronominal adverbs: da(r) + preposition',
  '<p>Statt <i>Präposition + Pronomen</i> sagst du für <b>Dinge und Sachverhalte</b> ein Pronominaladverb: <b>da(r)- + Präposition</b>. Vor einem Vokal kommt ein <b>r</b>: <i>darauf, daran, darüber, darum, davon, damit, dafür, dazu, davor, dabei</i>.</p>'
  + tbl(['Mit Personen', 'Mit Dingen'], [
   ['Ich warte <b>auf ihn</b>. (auf meinen Freund)', 'Ich warte <b>darauf</b>. (auf den Bus)'], ['Ich spreche <b>mit ihr</b>.', 'Ich spreche <b>damit</b> nicht gern. (mit diesem Thema)'],
   ['Ich denke <b>an dich</b>.', 'Ich denke <b>daran</b>.'], ['Er träumt <b>von ihr</b>.', 'Er träumt <b>davon</b>.']])
  + '<p><b>Fragen:</b> Personen: <i>Auf wen wartest du? Mit wem sprichst du?</i> Dinge: <i>Worauf wartest du? Womit beschäftigst du dich? Woran denkst du? Worüber ärgerst du dich?</i> (wo(r) + Präposition)</p>',
  '<p>For things and facts use da(r) + preposition (darauf, daran, damit, davon …). For people use preposition + pronoun (auf ihn). Questions: Auf wen? (person) / Worauf? (thing). Before a vowel an r is added: darauf, worauf.</p>'],
 ['C. Pronominaladverb + dass-Satz oder Infinitiv', 'C. Pronominal adverb + dass clause or infinitive',
  '<p>Das Pronominaladverb kann auf einen <b>Nebensatz</b> hinweisen: <i>Ich warte <b>darauf</b>, <b>dass</b> du anrufst. · Ich freue mich <b>darauf</b>, dich zu sehen. · Ich bitte Sie <b>darum</b>, mir zu antworten. · Es hängt <b>davon</b> ab, ob es regnet.</i></p>'
  '<p><b>Regel:</b> Gleiches Subjekt in beiden Teilen → Infinitiv mit <i>zu</i> (Ich freue mich darauf, <b>zu kommen</b>). Verschiedene Subjekte → dass-Satz (Ich freue mich darauf, <b>dass du kommst</b>).</p>',
  '<p>The pronominal adverb can point to a clause: Ich warte darauf, dass du anrufst. Same subject → infinitive with zu; different subjects → dass clause.</p>'],
 ['D. In der E-Mail benutzen', 'D. Using them in the email',
  '<ul class="tight"><li>Ich <b>freue mich auf</b> Ihre Antwort. · Ich <b>warte auf</b> Ihre Bestätigung.</li><li>Ich <b>bitte Sie um</b> eine schnelle Antwort. · Ich <b>bedanke mich für</b> Ihre Hilfe.</li>'
  '<li>Ich <b>interessiere mich für</b> den Kurs. · Ich <b>möchte mich über</b> den Lärm <b>beschweren</b>.</li><li>Ich <b>nehme</b> gern <b>an</b> dem Ausflug <b>teil</b>.</li><li><b>Es geht um</b> die Heizung. · <b>Dabei</b> handelt es sich um ein Problem.</li></ul>'
  '<div class="tip"><b>Tipp:</b> Schreibe dir die 25 Verben aus Abschnitt A auf Karten (vorn Verb, hinten Präposition + Kasus). Sprachbausteine Teil 1 prüft sie sehr oft.</div>',
  '<p>Handy phrases for emails: Ich freue mich auf …, Ich warte auf …, Ich bitte Sie um …, Ich bedanke mich für …, Ich interessiere mich für …, Es geht um … Tip: make flash cards for the 25 verbs.</p>'],
 ],
 ex=[
 ['Ich warte ___ den Bus.', ['auf', 'an', 'für'], 0, 'warten auf + Akkusativ.', 'warten auf + accusative.'],
 ['Er interessiert sich ___ Musik.', ['an', 'für', 'über'], 1, 'sich interessieren für.', 'sich interessieren für.'],
 ['Wir sprechen ___ das Wetter.', ['über', 'von', 'mit'], 0, 'sprechen über + Akkusativ (Thema).', 'sprechen über + accusative.'],
 ['Ich nehme ___ dem Kurs teil.', ['an', 'auf', 'für'], 0, 'teilnehmen an + Dativ.', 'teilnehmen an + dative.'],
 ['Er träumt ___ einem Haus am Meer.', ['an', 'von', 'über'], 1, 'träumen von + Dativ.', 'träumen von + dative.'],
 ['Ich warte auf den Bus. Ersetze „auf den Bus“: Ich warte ___.', ['darauf', 'dafür', 'darüber'], 0, 'warten auf → darauf.', 'warten auf → darauf.'],
 ['___ ärgerst du dich? (Über den Lärm.)', ['Worüber', 'Worauf', 'Womit'], 0, 'sich ärgern über → worüber.', 'sich ärgern über → worüber.'],
 ['___ sprichst du? (Mit meiner Chefin.)', ['Womit', 'Mit wem', 'Worüber'], 1, 'Person: mit wem.', 'person: mit wem.'],
 ['Er hat Angst ___ der Prüfung.', ['vor', 'für', 'auf'], 0, 'Angst haben vor + Dativ.', 'Angst haben vor + dative.'],
 ['Ich freue mich ___, dich zu sehen.', ['darauf', 'darüber', 'dafür'], 0, 'sich freuen auf → darauf (Zukunft).', 'sich freuen auf → darauf.'],
 ['Ich warte ___, dass du anrufst.', ['darauf', 'damit', 'darüber'], 0, 'warten auf: darauf, dass …', 'warten auf: darauf, dass …'],
 ['Sie bewirbt sich ___ die Stelle.', ['um', 'für', 'auf'], 0, 'sich bewerben um.', 'sich bewerben um.'],
 ['Das hängt ___ Wetter ab.', ['vom', 'am', 'beim'], 0, 'abhängen von + Dativ: vom (von dem).', 'abhängen von: vom.'],
 ['Ich denke oft ___ meine Eltern.', ['an', 'auf', 'über'], 0, 'denken an + Akkusativ.', 'denken an + accusative.'],
 ['Wir beginnen ___ dem Unterricht.', ['mit', 'an', 'von'], 0, 'beginnen mit + Dativ.', 'beginnen mit + dative.'],
 ]))

# ---------------------------------------------------------------- N14
L2.append(dict(
 id='N14', t='Partizip I und II als Adjektiv', te='Present and past participles as adjectives',
 where='Lesen Teil 1–3 (längere Texte) · Sprachbausteine · Hören', wen='Reading parts 1–3 (longer texts) · Language elements · Listening',
 goal='Du erkennst und bildest Partizipien als Adjektive: die steigenden Preise, das geplante Fest, ein gut bezahlter Job.',
 goalen='You recognise and form participles as adjectives: die steigenden Preise, das geplante Fest, ein gut bezahlter Job.',
 sec=[
 ['A. So bildest du sie', 'A. How to form them',
  tbl(['Form', 'Bildung', 'Beispiele'], [
   ['<b>Partizip I</b>', 'Infinitiv + <b>d</b> (aktiv, gleichzeitig)', 'spielen → spielend · steigen → steigend · lachen → lachend · fließen → fließend'],
   ['<b>Partizip II</b>', 'wie im Perfekt (passiv oder abgeschlossen)', 'planen → geplant · öffnen → geöffnet · schreiben → geschrieben · buchen → gebucht']])
  + '<p>Als Adjektiv bekommen sie <b>Endungen wie jedes Adjektiv</b>: <i>die steigenden Preise · ein geplantes Fest · der gebuchte Flug · mit der spielenden Gruppe</i>.</p>'
  '<p>Auch einige <b>unregelmäßige</b> Partizipien: <i>gewonnen (der gewonnene Preis), geschlossen (die geschlossene Tür), gebrochen, verloren (der verlorene Schlüssel), gelesen, getroffen</i>.</p>',
  '<p>Participle I = infinitive + d (active, simultaneous). Participle II = as in the perfect (passive or completed). They take normal adjective endings: die steigenden Preise, ein geplantes Fest.</p>'],
 ['B. Bedeutung', 'B. Meaning',
  tbl(['Partizip', 'Bedeutung', 'Beispiel'], [
   ['Partizip I', 'etwas <b>tut</b> gerade etwas (aktiv)', 'die steigenden Preise = die Preise, die steigen<br>das schlafende Kind = das Kind, das schläft'],
   ['Partizip II', 'etwas <b>wurde</b> gemacht (passiv) oder ist schon fertig', 'das geplante Fest = das Fest, das geplant wurde<br>die geöffnete Tür = die Tür, die geöffnet wurde / ist']])
  + '<p>Du kannst fast jedes <b>Relativsatz</b> mit Partizip kürzen und umgekehrt:</p><ul class="tight"><li>Die Preise, <b>die steigen</b> → die <b>steigenden</b> Preise</li><li>Das Haus, <b>das gebaut wurde</b> → das <b>gebaute</b> Haus</li><li>Der Kurs, <b>der geplant ist</b> → der <b>geplante</b> Kurs</li></ul>',
  '<p>Participle I: something is doing something (active). Participle II: something was done (passive) or is finished. You can turn a relative clause into a participle and back.</p>'],
 ['C. Typische Beispiele aus Prüfungstexten', 'C. Typical examples from exam texts',
  tbl(['Partizip', 'Beispiel'], [
   ['die <b>steigenden</b> Mieten', 'Die steigenden Mieten sind ein Problem für Studenten.'], ['die <b>wachsende</b> Zahl', 'Die wachsende Zahl von Autos belastet die Umwelt.'],
   ['das <b>folgende</b> Beispiel', 'Beachten Sie das folgende Beispiel.'], ['die <b>angegebene</b> Adresse', 'Bitte schicken Sie das Paket an die angegebene Adresse.'],
   ['der <b>gebuchte</b> Flug', 'Der gebuchte Flug ist leider ausgefallen.'], ['die <b>geplante</b> Reise', 'Wir müssen die geplante Reise verschieben.'],
   ['ein gut <b>bezahlter</b> Job', 'Sie hat einen gut bezahlten Job gefunden.'], ['die <b>beschädigte</b> Ware', 'Die beschädigte Ware schicke ich zurück.'],
   ['die <b>geöffneten</b> Fenster', 'Bei geöffneten Fenstern wird es kalt.'], ['der <b>überfüllte</b> Bus', 'Im überfüllten Bus gab es keinen Platz.']])
  + '<p>In Reklamationen und Beschwerden findest du viele Partizipien: <i>die defekte Heizung, die beschädigte Lieferung, das falsch gelieferte Produkt, die laufende Reparatur</i>.</p>',
  '<p>You meet many participles in complaints: die defekte Heizung, die beschädigte Lieferung, das falsch gelieferte Produkt.</p>'],
 ['D. Endungen kurz wiederholt', 'D. Adjective endings in short',
  tbl(['Artikel', 'Nominativ', 'Akkusativ', 'Dativ'], [
   ['der-Wort', 'der geplante Kurs', 'den geplanten Kurs', 'dem geplanten Kurs'], ['die-Wort', 'die geplante Reise', 'die geplante Reise', 'der geplanten Reise'],
   ['das-Wort', 'das geplante Fest', 'das geplante Fest', 'dem geplanten Fest'], ['Plural', 'die geplanten Feste', 'die geplanten Feste', 'den geplanten Festen'],
   ['ohne Artikel (m.)', 'geplanter Urlaub', 'geplanten Urlaub', 'mit geplantem Urlaub']])
  + '<p>Nach <b>der/die/das</b> steht fast immer <b>-e</b> oder <b>-en</b>. Nach <b>ein/kein/mein</b>: <i>ein geplanter Kurs (m. Nom.), ein geplantes Fest (n.)</i>.</p>',
  '<p>After der/die/das almost always -e or -en. After ein/kein/mein the masculine nominative gets -er and the neuter nominative/accusative -es.</p>'],
 ['E. Prüfungstipp', 'E. Exam tip',
  '<div class="tip"><b>Lesen Teil 1 und 2:</b> Lange Sätze mit Partizip (<i>die in diesem Jahr stark gestiegenen Preise</i>) sehen schwer aus. Lies von rechts nach links: Nomen suchen, dann das Partizip als Beschreibung davor. Frage: „Wer macht etwas?“ (Partizip I) oder „Was wurde gemacht?“ (Partizip II).</div>',
  '<p>Reading tip: in long phrases find the noun first, then read the participle as a description of it.</p>'],
 ],
 ex=[
 ['Die Preise, die steigen = die ___ Preise.', ['steigenden', 'gestiegenen', 'steigende'], 0, 'Partizip I: steigen + d + Endung -en (Plural nach „die“).', 'participle I: steigenden.'],
 ['Das Fest, das geplant wurde = das ___ Fest.', ['planende', 'geplante', 'plant'], 1, 'Passiv/abgeschlossen: Partizip II: geplante.', 'participle II: geplante.'],
 ['Das Kind, das schläft = das ___ Kind.', ['schlafende', 'geschlafene', 'schläft'], 0, 'aktiv, gleichzeitig: Partizip I: schlafende.', 'participle I: schlafende.'],
 ['Ich schicke die ___ Ware zurück. (beschädigen)', ['beschädigende', 'beschädigte', 'beschädigt'], 1, 'Partizip II: beschädigte Ware (die Ware wurde beschädigt).', 'participle II: beschädigte.'],
 ['Wir wohnen in einem ___ Haus. (bauen, schon fertig)', ['bauenden', 'gebauten', 'gebautem'], 1, 'Dativ n. nach „einem“: -en: einem gebauten Haus.', 'dative neuter after einem: -en.'],
 ['Die ___ Tür ist offen. (öffnen)', ['öffnende', 'geöffnete', 'geöffnet'], 1, 'Partizip II: geöffnete Tür.', 'participle II: geöffnete.'],
 ['Der Bus war ___ . (überfüllen)', ['überfüllt', 'überfüllende', 'überfüllend'], 0, 'Prädikativ (nach „sein“) ohne Endung: überfüllt.', 'after sein no ending: überfüllt.'],
 ['Wie lautet der Relativsatz? „die wachsende Zahl“', ['die Zahl, die wächst', 'die Zahl, die gewachsen wurde', 'die Zahl, wird gewachsen'], 0, 'Partizip I = aktiv: die Zahl, die wächst.', 'participle I = active.'],
 ['Wie lautet der Relativsatz? „der gebuchte Flug“', ['der Flug, der bucht', 'der Flug, der gebucht wurde', 'der Flug, den bucht'], 1, 'Partizip II = Passiv: der Flug, der gebucht wurde.', 'participle II = passive.'],
 ['Sie hat einen gut ___ Job. (bezahlen)', ['bezahlten', 'bezahlend', 'bezahlter'], 0, 'Akkusativ maskulin nach „einen“: -en: gut bezahlten.', 'accusative masc.: -en.'],
 ['Bitte beachten Sie das ___ Beispiel. (folgen)', ['folgende', 'folgendes', 'gefolgte'], 0, 'Nach „das“ steht im Nominativ und Akkusativ -e: das folgende Beispiel.', 'after das: -e (nominative and accusative).'],
 ['Die ___ Heizung muss repariert werden. (defekt)', ['defekte', 'defektem', 'defektes'], 0, 'feminin Nominativ nach „die“: -e.', 'feminine nominative: -e.'],
 ['Im ___ Bus gab es keinen Platz. (überfüllen)', ['überfüllten', 'überfüllte', 'überfüllende'], 0, 'Dativ maskulin nach „im“ (in dem): -en.', 'dative masc.: -en.'],
 ['Welches Partizip ist aktiv?', ['das gelöste Problem', 'die lachenden Kinder', 'die gebuchte Reise'], 1, 'lachend ist Partizip I = aktiv.', 'lachend = participle I = active.'],
 ['Die Zahl der ___ Menschen wird größer. (arbeiten, jetzt)', ['arbeitenden', 'gearbeiteten', 'arbeitende'], 0, 'Genitiv Plural: -en, Partizip I: arbeitenden.', 'genitive plural: arbeitenden.'],
 ]))

# ---------------------------------------------------------------- N15
L2.append(dict(
 id='N15', t='Genitiv: Attribut und Präpositionen', te='The genitive: attributes and prepositions',
 where='Lesen · Sprachbausteine · Schreiben (formelle E-Mail)', wen='Reading · Language elements · Writing (formal email)',
 goal='Du erkennst und benutzt den Genitiv: das Auto meines Vaters, wegen des Wetters, während der Reise.',
 goalen='You recognise and use the genitive: das Auto meines Vaters, wegen des Wetters, während der Reise.',
 sec=[
 ['A. Die Formen', 'A. The forms',
  tbl(['', 'maskulin', 'feminin', 'neutrum', 'Plural'], [
   ['Nominativ', 'der Mann', 'die Frau', 'das Kind', 'die Kinder'], ['Genitiv', 'des Mann<b>es</b>', '<b>der</b> Frau', 'des Kind<b>es</b>', '<b>der</b> Kinder'],
   ['mit ein-', 'eines Mann<b>es</b>', 'einer Frau', 'eines Kind<b>es</b>', 'meiner Kinder (mein-)']])
  + '<p>Maskuline und neutrale Nomen bekommen im Genitiv <b>-s</b> oder <b>-es</b>: <i>des Hauses, des Tages, des Mannes, des Autos, des Studenten</i> (n-Nomen: -en). Feminine und Plural-Nomen bleiben gleich.</p>'
  '<p><b>Eigennamen</b> bekommen -s ohne Artikel: <i>Peters Auto, Annas Freund, Manojs Wohnung</i>. Namen auf -s, -z, -x: Apostroph: <i>Hans\' Auto</i>.</p>',
  '<p>Masculine and neuter nouns get -s or -es in the genitive; feminine and plural stay the same. Names get -s: Peters Auto.</p>'],
 ['B. Das Genitivattribut', 'B. The genitive attribute',
  '<p>Das Genitiv-Nomen steht <b>hinter</b> dem Nomen, zu dem es gehört (Besitz oder Zugehörigkeit): <i>das Auto <b>meines Vaters</b> · die Meinung <b>der Lehrerin</b> · die Preise <b>der Wohnungen</b> · der Beginn <b>des Kurses</b> · die Qualität <b>des Produkts</b></i>.</p>'
  + tbl(['Schriftlich (Genitiv)', 'Gesprochen (von + Dativ)'], [
   ['das Auto meines Vaters', 'das Auto von meinem Vater'], ['die Preise der Wohnungen', 'die Preise von den Wohnungen'], ['der Beginn des Kurses', 'der Beginn vom Kurs']])
  + '<p>In der gesprochenen Sprache hörst du oft <b>von + Dativ</b>. In der <b>Prüfung</b> (Lesen, Sprachbausteine, formelle E-Mail) erwartet man den Genitiv.</p>',
  '<p>The genitive noun follows the noun it belongs to. In speech you often hear von + dative; in the exam (reading, language elements, formal email) the genitive is expected.</p>'],
 ['C. Präpositionen mit Genitiv', 'C. Prepositions with the genitive',
  tbl(['Präposition', 'Bedeutung', 'Beispiel'], [
   ['<b>wegen</b>', 'because of', 'Wegen des Regens bleiben wir zu Hause.'], ['<b>trotz</b>', 'despite', 'Trotz der Kälte gehen wir spazieren.'],
   ['<b>während</b>', 'during', 'Während der Ferien arbeite ich nicht.'], ['<b>statt / anstatt</b>', 'instead of', 'Statt des Busses nehme ich das Fahrrad.'],
   ['<b>innerhalb</b>', 'within', 'Innerhalb einer Woche bekommen Sie eine Antwort.'], ['<b>außerhalb</b>', 'outside of', 'Außerhalb der Öffnungszeiten ist das Büro geschlossen.'],
   ['<b>aufgrund</b>', 'because of (formal)', 'Aufgrund eines Fehlers müssen wir den Termin verschieben.'], ['<b>trotz</b> / <b>wegen</b> + Dativ (gesprochen)', 'colloquial', 'Wegen dem Regen … (nur gesprochen, nicht in der Prüfung)']])
  + '<p><b>Merke:</b> Nach <b>wegen, trotz, während, statt</b> steht in der Schriftsprache der <b>Genitiv</b>. Danach kein Nebensatz: <i>wegen des Regens</i> (Nomen) = <i>weil es regnet</i> (Nebensatz).</p>',
  '<p>wegen, trotz, während, statt, innerhalb, außerhalb, aufgrund take the genitive in written German. A preposition is followed by a noun, a subordinate clause by weil/obwohl/während.</p>'],
 ['D. Weitere Genitiv-Wendungen', 'D. More genitive expressions',
  '<ul class="tight"><li>Zeitangaben: <i>eines Tages, eines Morgens, des Nachts</i></li><li>Verben und Adjektive mit Genitiv sind selten und für B1 nicht nötig.</li><li>Nomen im Genitiv nach <b>Mengen</b>: <i>die Hälfte der Studenten, einige der Teilnehmer</i></li></ul>'
  '<div class="tip"><b>Tipp:</b> Für B1 zählen vor allem: Genitivattribut (<i>die Meinung der Lehrerin</i>), <i>wegen / trotz / während / statt</i> und <i>des/der</i> im Lesetext. Wenn du <i>des</i> oder <i>eines</i> siehst, ist es fast immer Genitiv maskulin/neutrum.</div>',
  '<p>For B1 you mainly need: genitive attribute, wegen/trotz/während/statt, and recognising des/der/eines in reading texts.</p>'],
 ['E. Prüfungstipp', 'E. Exam tip',
  '<ul class="tight"><li>✗ <i>wegen dem Wetter</i> (gesprochen) → ✓ <i>wegen des Wetters</i> (schriftlich)</li><li>✗ <i>das Auto von meinem Vater</i> (in der formellen E-Mail unelegant) → ✓ <i>das Auto meines Vaters</i></li><li>✗ <i>die Preise des Wohnungen</i> → ✓ <i>der Wohnungen</i> (Plural: der)</li><li>✗ <i>des Kind</i> → ✓ <i>des Kindes</i> (-es)</li></ul>'
  '<p>In der <b>Beschwerde-E-Mail</b> klingt es gut: <i>Aufgrund des Lärms … · Wegen der defekten Heizung … · Trotz mehrerer Anrufe …</i></p>',
  '<p>In a complaint email these sound good: Aufgrund des Lärms …, Wegen der defekten Heizung …, Trotz mehrerer Anrufe …</p>'],
 ],
 ex=[
 ['Das ist das Auto ___ Vaters. (mein)', ['meines', 'meinem', 'mein'], 0, 'Genitiv maskulin: meines Vaters.', 'genitive masc.: meines.'],
 ['Die Meinung ___ Lehrerin ist wichtig.', ['der', 'des', 'die'], 0, 'feminin Genitiv: der Lehrerin.', 'feminine genitive: der.'],
 ['Wegen ___ Regens bleiben wir zu Hause.', ['dem', 'des', 'der'], 1, 'wegen + Genitiv, Regen ist maskulin: des Regens.', 'wegen + genitive.'],
 ['Trotz ___ Kälte gehen wir spazieren.', ['der', 'des', 'die'], 0, 'trotz + Genitiv, Kälte ist feminin: der Kälte.', 'trotz + genitive.'],
 ['Während ___ Ferien arbeite ich nicht.', ['der', 'des', 'den'], 0, 'während + Genitiv Plural: der Ferien.', 'während + genitive plural.'],
 ['Der Beginn ___ Kurses ist am Montag.', ['des', 'dem', 'der'], 0, 'Genitiv maskulin: des Kurses.', 'genitive: des Kurses.'],
 ['Das Genitiv von „das Kind“ lautet:', ['des Kind', 'des Kindes', 'dem Kind'], 1, 'neutrum Genitiv: des Kindes.', 'des Kindes.'],
 ['Die Preise ___ Wohnungen steigen.', ['der', 'des', 'die'], 0, 'Plural Genitiv: der Wohnungen.', 'plural genitive: der.'],
 ['___ eines Fehlers müssen wir den Termin verschieben. (formell)', ['Aufgrund', 'Wegen dem', 'Weil'], 0, 'Aufgrund + Genitiv ist formell; weil leitet einen Nebensatz ein.', 'Aufgrund + genitive.'],
 ['Statt ___ Busses nehme ich das Fahrrad.', ['des', 'dem', 'den'], 0, 'statt + Genitiv: des Busses.', 'statt + genitive.'],
 ['Innerhalb ___ Woche bekommen Sie Antwort.', ['einer', 'einem', 'eine'], 0, 'innerhalb + Genitiv feminin: einer Woche.', 'innerhalb + genitive.'],
 ['Wie sagst du „Peters Wohnung“ mit von?', ['die Wohnung von Peter', 'die Wohnung des Peter', 'die Wohnung Peters Peter'], 0, 'von + Dativ: die Wohnung von Peter.', 'von + dative.'],
 ['Welcher Satz ist richtig (schriftlich)?', ['Wegen dem Lärm ziehe ich um.', 'Wegen des Lärms ziehe ich um.', 'Wegen der Lärm ziehe ich um.'], 1, 'Schriftlich: wegen + Genitiv, des Lärms.', 'written German: wegen + genitive.'],
 ['Welcher Ersatz ist richtig? „Weil es regnet“ = ___', ['wegen des Regens', 'wegen Regen', 'wegen dem Regen'], 0, 'weil + Satz = wegen + Genitiv-Nomen.', 'weil clause = wegen + genitive noun.'],
 ['Außerhalb ___ Öffnungszeiten ist das Büro zu.', ['der', 'des', 'den'], 0, 'außerhalb + Genitiv Plural: der Öffnungszeiten.', 'außerhalb + genitive plural.'],
 ]))

# ---------------------------------------------------------------- N16
L2.append(dict(
 id='N16', t='Relativsätze: mit Präposition, wo, was, wer', te='Relative clauses: with preposition, wo, was, wer',
 where='Lesen · Sprachbausteine · Schreiben · Sprechen (Erklären)', wen='Reading · Language elements · Writing · Speaking (explaining)',
 goal='Du bildest Relativsätze mit Präposition (der Zug, auf den wir warten) und mit wo, was, wer, und erklärst damit Dinge.',
 goalen='You form relative clauses with a preposition (der Zug, auf den wir warten) and with wo, was, wer, and use them to explain things.',
 sec=[
 ['A. Wiederholung: das Relativpronomen', 'A. Revision: the relative pronoun',
  tbl(['Kasus', 'maskulin', 'feminin', 'neutrum', 'Plural'], [
   ['Nominativ', 'der', 'die', 'das', 'die'], ['Akkusativ', '<b>den</b>', 'die', 'das', 'die'], ['Dativ', '<b>dem</b>', '<b>der</b>', '<b>dem</b>', '<b>denen</b>'], ['Genitiv', '<b>dessen</b>', '<b>deren</b>', '<b>dessen</b>', '<b>deren</b>']])
  + '<p>Das Relativpronomen richtet sich nach <b>Genus und Zahl des Bezugsworts</b> und nach dem <b>Kasus im Relativsatz</b>.</p><ul class="tight"><li>Der Mann, <b>der</b> dort steht, ist mein Chef. (Nominativ: Er steht dort.)</li><li>Der Film, <b>den</b> ich gesehen habe, war gut. (Akkusativ: Ich habe ihn gesehen.)</li><li>Die Frau, <b>der</b> ich geholfen habe, hat sich bedankt. (Dativ: Ich habe ihr geholfen.)</li></ul>'
  '<p>Das Verb steht im Relativsatz <b>am Ende</b>, vor dem Relativsatz steht ein <b>Komma</b>.</p>',
  '<p>The relative pronoun agrees in gender and number with the noun it refers to and takes the case required in the relative clause. The verb is at the end, with commas.</p>'],
 ['B. Relativsätze mit Präposition', 'B. Relative clauses with a preposition',
  '<p>Wenn das Verb oder ein Adverb eine <b>Präposition</b> braucht, steht sie <b>vor dem Relativpronomen</b>. Die Präposition bestimmt den Kasus (Akkusativ oder Dativ).</p>'
  + tbl(['Frage im Relativsatz', 'Beispiel'], [
   ['mit + Dativ', 'Das ist die Frau, <b>mit der</b> ich arbeite.'], ['auf + Akkusativ (warten auf)', 'Der Zug, <b>auf den</b> wir warten, hat Verspätung.'],
   ['an + Akkusativ (denken an)', 'Das Land, <b>an das</b> ich oft denke, ist Indien.'], ['in + Dativ (wo?)', 'Die Stadt, <b>in der</b> ich wohne, ist klein.'],
   ['für + Akkusativ', 'Das ist ein Kurs, <b>für den</b> man sich anmelden muss.'], ['von + Dativ', 'Das ist der Freund, <b>von dem</b> ich dir erzählt habe.'],
   ['bei + Dativ', 'Die Firma, <b>bei der</b> ich arbeite, hat 500 Mitarbeiter.'], ['über + Akkusativ', 'Das Thema, <b>über das</b> wir sprechen, ist wichtig.']])
  + '<p>Vorsicht bei <b>Perfekt</b>: <i>Der Film, <b>über den</b> wir gesprochen <b>haben</b>, war lang.</i> (Hilfsverb ganz am Ende)</p>',
  '<p>If the verb needs a preposition, it comes before the relative pronoun and decides the case. In the perfect the auxiliary is last.</p>'],
 ['C. wo, was, wer', 'C. wo, was, wer',
  '<p><b>wo</b> für Orte statt in + Relativpronomen: <i>Das ist die Stadt, <b>wo</b> ich wohne.</i> (in der Schriftsprache besser: <i>in der ich wohne</i>)</p>'
  '<p><b>was</b> nach <b>alles, nichts, etwas, vieles, das Beste, das Einzige, das Schönste</b> und nach einem ganzen Satz:</p><ul class="tight"><li>Alles, <b>was</b> ich weiß, habe ich gesagt.</li><li>Das ist das Beste, <b>was</b> ich kenne.</li><li>Er hat gewonnen, <b>was</b> alle gefreut hat. (was bezieht sich auf den ganzen Satz)</li><li>Nichts, <b>was</b> er sagt, stimmt.</li></ul>'
  '<p><b>wer</b> ohne Bezugswort (für Personen allgemein): <i><b>Wer</b> nicht kommt, verpasst den Spaß. · <b>Wer</b> viel liest, lernt viel.</i> (Der Satz mit wer steht oft zuerst.)</p>',
  '<p>wo for places; was after alles, nichts, etwas, das Beste and after a whole sentence; wer without an antecedent (Wer nicht kommt, verpasst den Spaß).</p>'],
 ['D. Zusammenfassende Regel', 'D. Summary rule',
  tbl(['Bezugswort', 'Relativpronomen'], [
   ['ein Nomen (Mann, Frau, Kind, Leute)', 'der / die / das / die'], ['Ort mit Präposition', 'in der / in dem / wo'], ['alles, nichts, etwas, das Beste, ganzer Satz', 'was'], ['kein Bezugswort (Person allgemein)', 'wer']])
  + '<div class="tip"><b>Schreiben und Sprechen:</b> Relativsätze machen deinen Stil besser. Statt „Ich habe einen Freund. Er wohnt in Köln.“ → „Ich habe einen Freund, der in Köln wohnt.“ In Sprechen Teil 2 kannst du damit Meinungen erklären: <i>Ich finde Läden gut, in denen man beraten wird.</i></div>',
  '<p>Relative clauses improve your style in writing and speaking. Join two sentences: Ich habe einen Freund, der in Köln wohnt.</p>'],
 ],
 ex=[
 ['Der Mann, ___ dort steht, ist mein Chef.', ['der', 'den', 'dem'], 0, 'Nominativ maskulin: der.', 'nominative masc.: der.'],
 ['Der Film, ___ ich gesehen habe, war gut.', ['den', 'der', 'dem'], 0, 'Akkusativ maskulin: den.', 'accusative masc.: den.'],
 ['Die Frau, ___ ich geholfen habe, hat sich bedankt.', ['die', 'der', 'den'], 1, 'helfen + Dativ, feminin: der.', 'dative fem.: der.'],
 ['Das ist die Frau, mit ___ ich arbeite.', ['der', 'die', 'den'], 0, 'mit + Dativ, feminin: der.', 'mit + dative fem.: der.'],
 ['Der Zug, auf ___ wir warten, hat Verspätung.', ['den', 'dem', 'der'], 0, 'warten auf + Akkusativ, Zug maskulin: den.', 'warten auf + accusative masc.: den.'],
 ['Die Stadt, in ___ ich wohne, ist klein.', ['der', 'die', 'den'], 0, 'wo? → Dativ, Stadt feminin: in der.', 'dative fem.: in der.'],
 ['Das ist der Freund, von ___ ich erzählt habe.', ['dem', 'den', 'der'], 0, 'von + Dativ maskulin: dem.', 'von + dative: dem.'],
 ['Alles, ___ ich weiß, habe ich gesagt.', ['was', 'das', 'wo'], 0, 'nach alles: was.', 'after alles: was.'],
 ['Das ist das Beste, ___ ich kenne.', ['was', 'das', 'wer'], 0, 'nach dem Superlativ (das Beste): was.', 'after superlative: was.'],
 ['___ viel liest, lernt viel.', ['Wer', 'Was', 'Der'], 0, 'Ohne Bezugswort für Personen: Wer.', 'no antecedent: wer.'],
 ['Die Firma, bei ___ ich arbeite, ist groß.', ['der', 'die', 'dem'], 0, 'bei + Dativ feminin: der.', 'bei + dative fem.: der.'],
 ['Wähle den richtigen Satz.', ['Der Film, über den wir gesprochen haben, war lang.', 'Der Film, über den haben wir gesprochen, war lang.', 'Der Film, über dem wir gesprochen haben, war lang.'], 0, 'Relativsatz: Verb am Ende, über + Akkusativ (den).', 'verb at the end; über + accusative.'],
 ['Das Thema, ___ wir sprechen, ist wichtig. (sprechen über)', ['über das', 'über dem', 'über der'], 0, 'über + Akkusativ neutrum: über das.', 'über + accusative neuter.'],
 ['Er hat gewonnen, ___ alle gefreut hat.', ['was', 'das', 'wer'], 0, 'Bezug auf den ganzen Satz: was.', 'refers to the whole sentence: was.'],
 ['Die Kinder, ___ ich helfe, sind nett.', ['denen', 'die', 'den'], 0, 'Dativ Plural: denen.', 'dative plural: denen.'],
 ]))

# ---------------------------------------------------------------- N17
L2.append(dict(
 id='N17', t='Nomen-Verb-Verbindungen und feste Wendungen', te='Noun-verb phrases and fixed expressions',
 where='Sprachbausteine Teil 2 · Schreiben (formelle E-Mail) · Lesen', wen='Language elements part 2 · Writing (formal email) · Reading',
 goal='Du kennst 60 feste Verbindungen (eine Entscheidung treffen, in Anspruch nehmen …) und benutzt sie in der E-Mail und in Sprachbausteine Teil 2.',
 goalen='You know 60 fixed phrases (eine Entscheidung treffen, in Anspruch nehmen …) and use them in the email and in language elements part 2.',
 sec=[
 ['A. Was sind Nomen-Verb-Verbindungen?', 'A. What are noun-verb phrases?',
  '<p>Das sind feste Kombinationen aus <b>Nomen + Verb</b> (oft mit Präposition). Das Verb hat dabei eine schwache Bedeutung, die Hauptbedeutung steckt im Nomen: <i>eine Entscheidung <b>treffen</b> = entscheiden · einen Antrag <b>stellen</b> = beantragen · Kontakt <b>aufnehmen</b> = sich melden</i>.</p>'
  '<p>In <b>Sprachbausteine Teil 2</b> (Wortliste) fehlen oft das Verb oder das Nomen. Du musst die Verbindung kennen: man sagt <i>eine Frage <b>stellen</b></i>, nicht <i>machen</i>.</p>',
  '<p>Fixed combinations of noun + verb; the meaning is in the noun, the verb is weak. In language elements part 2 you have to know which verb goes with which noun.</p>'],
 ['B. Die wichtigsten Verbindungen (nach Verb)', 'B. The most important phrases (by verb)',
  tbl(['Verb', 'Verbindungen'], [
   ['<b>stellen</b>', 'eine Frage stellen · einen Antrag stellen · eine Bedingung stellen · ein Problem stellen · die Frage stellen, ob …'],
   ['<b>machen</b>', 'einen Vorschlag machen · eine Pause machen · einen Ausflug machen · Urlaub machen · einen Fehler machen · Spaß machen · Sport machen · eine Reservierung machen'],
   ['<b>treffen</b>', 'eine Entscheidung treffen · eine Vereinbarung treffen · Vorbereitungen treffen · eine Auswahl treffen · einen Termin treffen (mit jemandem)'],
   ['<b>nehmen</b>', 'Rücksicht nehmen (auf) · Urlaub nehmen · in Anspruch nehmen · zur Kenntnis nehmen · an einem Kurs teilnehmen · Platz nehmen · Abschied nehmen · einen Bus nehmen'],
   ['<b>haben</b>', 'Zeit haben · Hunger haben · Angst haben (vor) · recht haben · Schwierigkeiten haben · Interesse haben (an) · Lust haben (auf) · Erfahrung haben (mit)'],
   ['<b>geben</b>', 'Bescheid geben · eine Antwort geben · einen Rat geben · Auskunft geben · Unterricht geben · eine Erlaubnis geben'],
   ['<b>bringen</b>', 'in Ordnung bringen · zum Ausdruck bringen · in Gefahr bringen · zur Sprache bringen'],
   ['<b>kommen</b>', 'zum Einsatz kommen · in Frage kommen · zur Sprache kommen · in Kontakt kommen · zu spät kommen'],
   ['<b>setzen / legen / bleiben / stehen</b>', 'sich in Verbindung setzen (mit) · Wert legen auf · in Kontakt bleiben · zur Verfügung stehen · unter Druck stehen'],
   ['<b>aufnehmen / ablegen / halten</b>', 'Kontakt aufnehmen · eine Prüfung ablegen · einen Vortrag halten · ein Versprechen halten · Kontakt halten']])
  , '<p>Memorise the verb with the noun: stellen (Frage, Antrag), machen (Vorschlag, Pause, Fehler), treffen (Entscheidung, Vereinbarung), nehmen (Rücksicht, Urlaub, in Anspruch nehmen), haben (Zeit, Angst, Interesse), geben (Bescheid, Rat, Auskunft).</p>'],
 ['C. Bedeutung und einfache Verben', 'C. Meaning and simple verbs',
  tbl(['Nomen-Verb-Verbindung', 'einfaches Verb', 'Beispiel'], [
   ['eine Entscheidung treffen', 'entscheiden', 'Wir müssen heute eine Entscheidung treffen.'], ['einen Antrag stellen', 'beantragen', 'Ich möchte einen Antrag auf Wohngeld stellen.'],
   ['Kontakt aufnehmen', 'sich melden bei', 'Bitte nehmen Sie mit uns Kontakt auf.'], ['in Anspruch nehmen', 'nutzen', 'Viele Leute nehmen die Beratung in Anspruch.'],
   ['zur Verfügung stehen', 'da sein', 'Das Auto steht Ihnen jederzeit zur Verfügung.'], ['zur Kenntnis nehmen', 'erfahren / lesen', 'Bitte nehmen Sie das zur Kenntnis.'],
   ['Rücksicht nehmen auf', 'beachten', 'Nehmen Sie bitte Rücksicht auf Ihre Nachbarn.'], ['Bescheid geben', 'informieren', 'Geben Sie mir bitte Bescheid, wenn Sie kommen.'],
   ['in Frage kommen', 'möglich sein', 'Dieser Termin kommt für mich nicht in Frage.'], ['Wert legen auf', 'wichtig finden', 'Ich lege Wert auf pünktliche Lieferung.'],
   ['zur Sprache kommen', 'besprochen werden', 'Das Thema kam im Meeting zur Sprache.'], ['Schwierigkeiten haben', 'nicht gut klarkommen', 'Ich habe Schwierigkeiten mit dem Internet.']])
  , '<p>Nomen-Verb-Verbindungen sound more formal than the simple verb. Use them in formal emails: Ich möchte einen Antrag stellen; Bitte geben Sie mir Bescheid.</p>'],
 ['D. Nützliche Sätze für die formelle E-Mail', 'D. Useful sentences for the formal email',
  '<ul class="tight"><li>Ich möchte <b>einen Termin vereinbaren</b>. · Ich <b>bitte Sie um Rückruf</b>.</li><li>Bitte <b>geben Sie mir Bescheid</b>, ob der Termin möglich ist.</li><li>Ich <b>habe Interesse an</b> einem Kurs und <b>möchte Kontakt aufnehmen</b>.</li><li>Ich <b>habe</b> große <b>Schwierigkeiten mit</b> der Heizung. · Der Lärm <b>stellt ein Problem dar</b>.</li><li>Ich <b>lege Wert auf</b> eine schnelle Lösung. · Ich <b>nehme</b> gern Ihre Hilfe <b>in Anspruch</b>.</li><li>Ich <b>mache</b> Ihnen folgenden <b>Vorschlag</b>: …</li></ul>'
  '<div class="tip"><b>Tipp für Sprachbausteine Teil 2:</b> Lies den Satz mit jeder Wortliste-Option im Kopf. Meist passt nur eine Verbindung zum Nomen. Merke dir die Paare (Frage – stellen, Entscheidung – treffen, Pause – machen, Rücksicht – nehmen).</div>',
  '<p>Useful phrases for formal emails: Ich möchte einen Termin vereinbaren, Bitte geben Sie mir Bescheid, Ich lege Wert auf …, Ich nehme Ihre Hilfe in Anspruch. Tip: for language elements part 2, learn the pairs.</p>'],
 ],
 ex=[
 ['Ich möchte Ihnen eine Frage ___.', ['machen', 'stellen', 'geben'], 1, 'eine Frage stellen.', 'eine Frage stellen.'],
 ['Wir müssen eine Entscheidung ___.', ['machen', 'treffen', 'nehmen'], 1, 'eine Entscheidung treffen.', 'eine Entscheidung treffen.'],
 ['Er macht Urlaub = Er ___ Urlaub.', ['nimmt', 'macht', 'hat'], 0, 'Urlaub nehmen (oder Urlaub machen).', 'Urlaub nehmen.'],
 ['Bitte ___ Sie Rücksicht auf Ihre Nachbarn.', ['machen', 'nehmen', 'geben'], 1, 'Rücksicht nehmen auf.', 'Rücksicht nehmen auf.'],
 ['Ich möchte einen Antrag ___.', ['stellen', 'machen', 'treffen'], 0, 'einen Antrag stellen.', 'einen Antrag stellen.'],
 ['Bitte ___ Sie mir Bescheid.', ['geben', 'machen', 'bringen'], 0, 'Bescheid geben.', 'Bescheid geben.'],
 ['Ich ___ Wert auf pünktliche Lieferung.', ['mache', 'lege', 'nehme'], 1, 'Wert legen auf.', 'Wert legen auf.'],
 ['Bitte ___ Sie mit uns Kontakt auf.', ['nehmen', 'machen', 'stellen'], 0, 'Kontakt aufnehmen (nehmen Sie … auf).', 'Kontakt aufnehmen.'],
 ['Dieser Termin ___ für mich nicht in Frage.', ['kommt', 'geht', 'macht'], 0, 'in Frage kommen.', 'in Frage kommen.'],
 ['Das Thema kam im Gespräch zur ___.', ['Sprache', 'Antwort', 'Frage'], 0, 'zur Sprache kommen.', 'zur Sprache kommen.'],
 ['Ich habe große ___ mit dem Computer.', ['Schwierigkeiten', 'Hilfe', 'Lust'], 0, 'Schwierigkeiten haben mit.', 'Schwierigkeiten haben mit.'],
 ['Wir machen ___.', ['einen Vorschlag', 'eine Entscheidung', 'einen Antrag'], 0, 'einen Vorschlag machen (aber: eine Entscheidung treffen, einen Antrag stellen).', 'einen Vorschlag machen.'],
 ['Das Auto steht Ihnen jederzeit zur ___.', ['Verfügung', 'Hilfe', 'Nutzung'], 0, 'zur Verfügung stehen.', 'zur Verfügung stehen.'],
 ['Viele Leute ___ die Beratung in Anspruch.', ['nehmen', 'machen', 'treffen'], 0, 'in Anspruch nehmen.', 'in Anspruch nehmen.'],
 ['Wir ___ eine Pause.', ['machen', 'stellen', 'treffen'], 0, 'eine Pause machen.', 'eine Pause machen.'],
 ]))

# ---------------------------------------------------------------- N18
L2.append(dict(
 id='N18', t='Zahlen, Datum und Zeitangaben', te='Numbers, dates and time expressions',
 where='Lesen · Hören · Schreiben (Termine) · Sprechen Teil 3 (planen)', wen='Reading · Listening · Writing (appointments) · Speaking part 3 (planning)',
 goal='Du nennst Datum, Uhrzeit, Preise und Zeiträume richtig und wählst die richtige Zeitpräposition (um, am, im, vor, seit, bis, ab, für).',
 goalen='You state dates, times, prices and periods correctly and choose the right time preposition (um, am, im, vor, seit, bis, ab, für).',
 sec=[
 ['A. Ordnungszahlen und das Datum', 'A. Ordinal numbers and the date',
  tbl(['Zahl', 'Ordnungszahl', 'Beispiel'], [
   ['1', 'der <b>erste</b>', 'am 1. Mai = am ersten Mai'], ['2', 'der zweite', 'am 2. Juni'], ['3', 'der <b>dritte</b>', 'am 3. Juli'], ['4–19', 'Zahl + <b>-te</b>', 'der vierte, fünfte, sechste, <b>siebte</b>, <b>achte</b>, zehnte, zwölfte'],
   ['20–31', 'Zahl + <b>-ste</b>', 'der zwanzigste, einundzwanzigste, dreißigste, einunddreißigste']])
  + '<p><b>Datum:</b> <i>Heute ist der 25. Februar.</i> (Nominativ) · <i>Wir treffen uns <b>am</b> 25. Februar.</i> (an + Dativ: am fünfundzwanzigsten Februar) · <i>Die Prüfung ist <b>im</b> Februar.</i> · <i>Ich bin <b>im</b> Jahr 1996 geboren. / 1996 geboren.</i></p>'
  '<p><b>Jahre:</b> <i>1996 = neunzehnhundertsechsundneunzig · 2027 = zweitausendsiebenundzwanzig</i>. In der E-Mail schreibst du: <i>Köln, den 25. Februar 2027</i>.</p>',
  '<p>Ordinals: erste, zweite, dritte, vierte … siebte, achte; from 20: -ste. Dates: am 25. Februar, im Februar, im Jahr 1996. Years up to 1999 are said as hundreds: neunzehnhundertsechsundneunzig; from 2000: zweitausendsiebenundzwanzig.</p>'],
 ['B. Zahlen, Preise und Mengen', 'B. Numbers, prices and quantities',
  tbl(['Thema', 'Beispiel'], [
   ['Zahlen', '13 dreizehn · 16 sechzehn · 17 siebzehn · 21 einundzwanzig · 70 siebzig · 100 hundert · 1000 tausend · 1 000 000 eine Million'],
   ['Preise', '4,50 € = vier Euro fünfzig · 19,99 € = neunzehn Euro neunundneunzig · 0,80 € = achtzig Cent'], ['Prozent', '25 % = fünfundzwanzig Prozent · 100 % = hundert Prozent'],
   ['Brüche', '½ = ein halb(es) · ¼ = ein Viertel · ¾ = drei Viertel'], ['Mengen', 'ein Kilo Äpfel · 500 Gramm Käse · zwei Liter Milch · eine Packung Nudeln · ein Stück Kuchen'],
   ['Telefon', '0241 55 12 87 = null-zwei-vier-eins, fünf-fünf, eins-zwei, acht-sieben']])
  + '<p>Nach Mengen steht das Nomen ohne Artikel und ohne Plural-Endung bei Maßen: <i>zwei Kilo Äpfel, drei Glas Wasser</i>.</p>',
  '<p>Practise saying prices (vier Euro fünfzig), percentages, fractions and quantities. After measure words the noun has no article.</p>'],
 ['C. Uhrzeit', 'C. Telling the time',
  tbl(['Uhrzeit', 'offiziell (Fahrplan, Radio)', 'umgangssprachlich'], [
   ['08:15', 'acht Uhr fünfzehn', 'Viertel nach acht'], ['08:30', 'acht Uhr dreißig', '<b>halb neun</b>'], ['08:45', 'acht Uhr fünfundvierzig', 'Viertel vor neun'], ['14:05', 'vierzehn Uhr fünf', 'fünf nach zwei'],
   ['14:25', 'vierzehn Uhr fünfundzwanzig', 'fünf vor halb drei'], ['18:00', 'achtzehn Uhr', 'sechs Uhr (abends)'], ['00:00', 'null Uhr', 'Mitternacht']])
  + '<p><b>Merke:</b> <i>halb neun</i> = 8:30 (eine halbe Stunde <b>vor</b> neun). Frage: <i>Wie spät ist es? · Wie viel Uhr ist es? · Um wie viel Uhr beginnt der Kurs?</i> Antwort mit <b>um</b>: <i>Um halb neun.</i></p>',
  '<p>Official time uses 24 hours; in speech use 12 hours with Viertel and halb. halb neun = 8:30!</p>'],
 ['D. Zeitpräpositionen', 'D. Time prepositions',
  tbl(['Präposition', 'Bedeutung', 'Beispiel'], [
   ['<b>um</b>', 'genaue Uhrzeit', 'um 8 Uhr · um halb drei'], ['<b>am</b> (an + Dativ)', 'Tag, Datum, Tageszeit', 'am Montag · am 3. Mai · am Abend · am Wochenende'],
   ['<b>im</b> (in + Dativ)', 'Monat, Jahr, Jahreszeit', 'im Mai · im Jahr 2027 · im Winter'], ['<b>in</b> + Dativ', 'in der Zukunft (nach)', 'in zwei Wochen · in einer Stunde'],
   ['<b>vor</b> + Dativ', 'in der Vergangenheit (ago)', 'vor einem Jahr · vor drei Tagen'], ['<b>seit</b> + Dativ', 'seit einem Zeitpunkt / Zeitraum (bis jetzt)', 'seit einem Jahr · seit Montag'],
   ['<b>bis</b> + Akkusativ-Zeitpunkt', 'bis zu diesem Zeitpunkt', 'bis Freitag · bis 18 Uhr · bis zum 30. Juni'], ['<b>ab</b> + Dativ', 'ab diesem Zeitpunkt', 'ab Montag · ab dem 1. Mai'],
   ['<b>von … bis</b>', 'von … bis …', 'von 9 bis 17 Uhr · von Montag bis Freitag'], ['<b>für</b> + Akkusativ', 'für einen Zeitraum', 'für eine Woche · für zwei Tage'],
   ['<b>während</b> + Genitiv', 'in dieser Zeit', 'während der Ferien'], ['<b>nach / vor</b> + Dativ', 'danach / davor', 'nach dem Essen · vor der Arbeit'], ['<b>gegen</b>', 'ungefähr', 'gegen 18 Uhr (ca.)'], ['<b>zwischen</b> … <b>und</b>', 'in diesem Zeitraum', 'zwischen 10 und 12 Uhr']])
  + '<p><b>Achtung:</b> <i>seit zwei Jahren</i> (Dativ + Präsens: Ich wohne seit zwei Jahren hier) ≠ <i>vor zwei Jahren</i> (Perfekt/Präteritum: Ich bin vor zwei Jahren gekommen) ≠ <i>in zwei Jahren</i> (Zukunft).</p>',
  '<p>um (clock time), am (day, date), im (month, year, season), in (future), vor (ago), seit (since), bis (until), ab (from), von … bis, für (for), während, gegen (about).</p>'],
 ['E. Häufigkeit und Zeitadverbien', 'E. Frequency and time adverbs',
  tbl(['Thema', 'Wörter'], [
   ['Häufigkeit', 'immer · oft · meistens · manchmal · selten · nie · jeden Tag · einmal pro Woche · zweimal im Monat · täglich · wöchentlich · monatlich · jährlich'],
   ['Tag', 'vorgestern · gestern · heute · morgen · übermorgen · morgens · mittags · abends · nachts · montags (jeden Montag)'],
   ['Reihenfolge', 'zuerst · dann · danach · später · schließlich · zum Schluss · vorher · nachher · gleichzeitig · inzwischen'], ['Zeitpunkt', 'sofort · bald · gleich · früher · jetzt · damals · neulich · bisher · noch · schon · erst']])
  + '<div class="tip"><b>Tipp:</b> In der E-Mail zum Thema Termin stehen Datum und Uhrzeit oft in den Leitpunkten. Schreibe sie klar: <i>Ich komme am Montag, den 3. März, um 14 Uhr.</i> Wiederhole sie laut: Prüfer achten bei Sprechen Teil 3 auf genaue Zeitangaben („am Samstag um 15 Uhr“).</div>',
  '<p>Frequency, day and sequence words. In emails write dates and times clearly: Ich komme am Montag, den 3. März, um 14 Uhr.</p>'],
 ],
 ex=[
 ['Wir treffen uns ___ Montag.', ['am', 'im', 'um'], 0, 'Tag: am Montag.', 'am Montag.'],
 ['Der Kurs beginnt ___ 8 Uhr.', ['am', 'um', 'im'], 1, 'Uhrzeit: um 8 Uhr.', 'um 8 Uhr.'],
 ['Ich bin ___ Februar geboren.', ['im', 'am', 'um'], 0, 'Monat: im Februar.', 'im Februar.'],
 ['Ich wohne ___ zwei Jahren in Aachen. (noch heute)', ['vor', 'seit', 'in'], 1, 'seit + Dativ: Zeitraum bis jetzt.', 'seit = since/for until now.'],
 ['Ich bin ___ zwei Jahren umgezogen. (es ist vorbei)', ['vor', 'seit', 'in'], 0, 'vor + Dativ: ago.', 'vor = ago.'],
 ['Der Kurs beginnt ___ zwei Wochen. (Zukunft)', ['vor', 'seit', 'in'], 2, 'in + Dativ: future.', 'in = in (future).'],
 ['Das Büro ist ___ Montag ___ Freitag geöffnet.', ['von … bis', 'ab … um', 'seit … bis'], 0, 'von … bis.', 'von … bis.'],
 ['Wir fahren ___ eine Woche nach Indien.', ['für', 'seit', 'vor'], 0, 'für + Akkusativ: Zeitraum.', 'für = for a period.'],
 ['08:30 Uhr sagt man umgangssprachlich:', ['halb acht', 'halb neun', 'Viertel nach acht'], 1, 'halb neun = 8:30.', 'halb neun = 8:30.'],
 ['Der ___ Mai ist ein Feiertag. (1.)', ['erste', 'einte', 'eins'], 0, 'der erste Mai.', 'erste.'],
 ['Ich habe am ___ Juli Geburtstag. (7.)', ['siebten', 'sieben', 'siebenten Jahr'], 0, 'am siebten Juli (Dativ: -en).', 'am siebten.'],
 ['1996 sagt man:', ['neunzehnhundertsechsundneunzig', 'tausendneunhundert sechsundneunzig', 'neunzehn sechsundneunzig tausend'], 0, 'bis 1999: neunzehnhundert …', 'nineteen hundred …'],
 ['4,50 € sagt man:', ['vier Euro fünfzig', 'vierzig fünf Euro', 'vier fünfzig Cent'], 0, 'vier Euro fünfzig.', 'four euro fifty.'],
 ['Das Angebot gilt ___ 30. Juni.', ['bis zum', 'seit dem', 'vor dem'], 0, 'bis zum 30. Juni.', 'until 30 June.'],
 ['Ich schicke Ihnen die Unterlagen ___ Freitag. (spätestens)', ['bis', 'seit', 'vor einem'], 0, 'bis Freitag = by Friday.', 'bis Freitag = by Friday.'],
 ]))
