#!/usr/bin/env python3
"""Replace the Goethe-style "talk in five steps" for Sprechen Teil 2 with the telc format from the official
Übungstest: each partner reports on a different short opinion text, then both discuss (own opinion,
own experience, react, ask). Usage: python3 scripts/fixes/sprechen_teil2_2026-11-24.py  (idempotent)"""
import re, glob, os
D = os.path.join(os.path.dirname(__file__), '..', '..', 'docs')

ROWS_DE = [
 ('1. Über deinen Text berichten', 'In meinem Text geht es um … · Die Person im Text meint, dass …'),
 ('2. Nach dem Text des Partners fragen', 'Und was steht in deinem Text? · Habe ich richtig verstanden, dass …?'),
 ('3. Eigene Meinung mit Grund', 'Meiner Meinung nach …, weil … · Ein Vorteil ist, dass … · Ein Nachteil ist, dass …'),
 ('4. Eigene Erfahrung', 'Bei mir ist das so: … · Ich habe selbst erlebt, dass … · In meinem Heimatland ist das anders: …'),
 ('5. Reagieren und weiterfragen', 'Da hast du recht, aber … · Das sehe ich anders, weil … · Wie siehst du das?')]
ROWS_EN = [
 ('1. Report on your text', 'Who says what, and why', 'In meinem Text geht es um … · Die Person im Text meint, dass …'),
 ('2. Ask about your partner’s text', 'Listen, then ask', 'Und was steht in deinem Text? · Habe ich richtig verstanden, dass …?'),
 ('3. Your opinion with a reason', 'An advantage or a disadvantage helps', 'Meiner Meinung nach …, weil … · Ein Vorteil ist, dass … · Ein Nachteil ist, dass …'),
 ('4. Your own experience', 'Also how it is in your home country', 'Bei mir ist das so: … · Ich habe selbst erlebt, dass … · In meinem Heimatland ist das anders: …'),
 ('5. React and ask', 'A conversation, not a speech', 'Da hast du recht, aber … · Das sehe ich anders, weil … · Wie siehst du das?')]
INTRO_EN = ('<p>In telc B1 Teil 2 you and your partner each get a different short text with an opinion on the same topic. '
            'First each of you reports on your text. Then you talk together: give your opinion, tell about your own experience, '
            'react and ask questions. It is a conversation (about 6 minutes for both of you), not a presentation.</p>')

def table_de(head):
    return '<h3>%s</h3>\n<table><tr><th>Schritt</th><th>Wendungen</th></tr>\n%s</table>' % (
        head, '\n'.join('<tr><td>%s</td><td>%s</td></tr>' % r for r in ROWS_DE))
def table_en(head):
    return '<h3>%s</h3>\n%s\n<table><tr><th>Step</th><th>What you do</th><th>Useful phrases</th></tr>\n%s</table>' % (
        head, INTRO_EN, '\n'.join('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % r for r in ROWS_EN))

D66_DE = ('<h3>C. Sprechen Teil 2: über einen Text berichten und diskutieren (Thema: allein oder in der Gruppe reisen?)</h3>\n'
 '<table><tr><th>Schritt</th><th>Beispiel</th></tr>\n'
 '<tr><td>1. Über den Text berichten</td><td>In meinem Text steht, dass man in der Gruppe Geld spart.</td></tr>\n'
 '<tr><td>2. Nach dem Text des Partners fragen</td><td>Und was steht in deinem Text?</td></tr>\n'
 '<tr><td>3. Meinung mit Grund</td><td>Meiner Meinung nach reist man allein freier, weil man selbst entscheiden kann.</td></tr>\n'
 '<tr><td>4. Eigene Erfahrung</td><td>Ich bin letztes Jahr mit einer Gruppe nach Italien gefahren. Das war sehr bequem.</td></tr>\n'
 '<tr><td>5. Reagieren und fragen</td><td>Da hast du recht, aber … · Wie siehst du das?</td></tr></table>')
D66_EN = ('<h3>C. Sprechen Teil 2: report on a text and discuss (topic: travelling alone or in a group?)</h3>\n'
 '<table><tr><th>Step</th><th>Example</th></tr>\n'
 '<tr><td>1. Report on your text</td><td>In meinem Text steht, dass man in der Gruppe Geld spart.</td></tr>\n'
 '<tr><td>2. Ask about your partner’s text</td><td>Und was steht in deinem Text?</td></tr>\n'
 '<tr><td>3. Opinion with a reason</td><td>Meiner Meinung nach reist man allein freier, weil man selbst entscheiden kann.</td></tr>\n'
 '<tr><td>4. Own experience</td><td>Ich bin letztes Jahr mit einer Gruppe nach Italien gefahren. Das war sehr bequem.</td></tr>\n'
 '<tr><td>5. React and ask</td><td>Da hast du recht, aber … · Wie siehst du das?</td></tr></table>')

BLOCKS = [  # (regex over the whole block, replacement)
 (r'<h3>B\. Sprechen Teil 2: ein kurzer Beitrag in fünf Schritten</h3>\s*<table>.*?</table>', table_de('B. Sprechen Teil 2: über einen Text berichten und diskutieren')),
 (r'<h3>B\. Sprechen Teil 2: a short talk in five steps</h3>\s*<p>.*?</p>\s*<table>.*?</table>', table_en('B. Sprechen Teil 2: report on a text and discuss')),
 (r'<h3>B\. Die fünf Schritte von Teil 2 \(Endform\)</h3>\s*<table>.*?</table>', table_de('B. Sprechen Teil 2: Bericht, Meinung, Gespräch (Endform)')),
 (r'<h3>B\. The five steps of Teil 2 \(final form\)</h3>\s*<table>.*?</table>', table_en('B. Sprechen Teil 2: report, opinion, discussion (final form)')),
 (r'<h3>C\. Sprechen Teil 2 in fünf Schritten \(Thema: allein oder in der Gruppe reisen\?\)</h3>\s*<table>.*?</table>', D66_DE),
 (r'<h3>C\. Sprechen Teil 2 in five steps \(topic: travelling alone or in a group\?\)</h3>\s*<table>.*?</table>', D66_EN),
]
TEL = 'Berichten Sie über Ihren Text, sagen Sie Ihre Meinung und erzählen Sie von eigenen Erfahrungen. Sprechen Sie dann mit Ihrem Partner darüber.'
PHRASES = [
 ('Berichten Sie in fünf Schritten (Einleitung, Situation, Vorteile und Nachteile, eigene Meinung, Abschluss) und reagieren Sie auf eine Frage.', TEL),
 ('Berichten Sie in fünf Schritten (Einleitung, eigene Erfahrung, Heimatland, Vor- und Nachteile, Abschluss und Dank) und reagieren Sie auf eine Frage.', TEL),
 ('Berichten Sie in fünf Schritten und reagieren Sie auf eine Frage.', TEL),
 ('hältst einen Beitrag in fünf Schritten in Sprechen Teil 2', 'berichtest in Sprechen Teil 2 über einen Text und diskutierst darüber'),
 ('einen Beitrag in fünf Schritten (Teil 2)', 'Sprechen Teil 2 (über einen Text berichten und diskutieren)'),
 ('einen Vortrag in fünf Schritten (Teil 2) trainieren', 'Sprechen Teil 2 (über einen Text berichten und diskutieren) trainieren'),
 ('Teil 2 Beitrag in fünf Schritten', 'Teil 2 über einen Text berichten und diskutieren'),
 ('Teil 2 Vortrag in fünf Schritten', 'Teil 2 über einen Text berichten und diskutieren'),
 ('der Vortrag in fünf Schritten und die Planungswendungen', 'die Wendungen für Teil 2 (Bericht, Meinung, Reaktion) und die Planungswendungen'),
 ('Teil 2 – Beitrag in fünf Schritten:', 'Teil 2 – Über ein Thema sprechen:'),
 ('<ul class="tight"><li>Thema</li><li>Erfahrung</li><li>Heimatland</li><li>Vor- und Nachteile</li><li>Meinung</li></ul>',
  '<ul class="tight"><li>Bericht über Ihren Text</li><li>Meinung mit Grund</li><li>Eigene Erfahrung</li><li>Frage an den Partner und Reaktion</li></ul>'),
 ('<td>Heimatland.</td>', '<td>Eigene Erfahrung (Heimatland).</td>'),
 ('<td class=de>Vielen Dank für Ihre Aufmerksamkeit.</td><td>Abschluss.</td>', '<td class=de>Wie sehen Sie das? Haben Sie das auch schon erlebt?</td><td>Frage an den Partner.</td>'),
 ('<td>Einleitung · Erfahrung · Heimatland · Vor-/Nachteile · Abschluss</td>', '<td>Bericht über den Text · Meinung mit Grund · eigene Erfahrung · reagieren und nachfragen</td>'),
 ('<td>Einleitung · eigene Erfahrung · Heimatland · Vor-/Nachteil · Abschluss + Dank</td>', '<td>Bericht über den Text · Meinung mit Grund · eigene Erfahrung · reagieren und nachfragen</td>'),
 ('<td>Vortrag in fünf Schritten, dann eine Frage des Partners</td>', '<td>Über den eigenen Text berichten, Meinung und Erfahrung sagen, dann mit dem Partner diskutieren</td>'),
 ('<td>Beitrag in fünf Schritten zu einem Thema, dann auf eine Frage reagieren.</td>', '<td>Über den eigenen Meinungstext berichten, Meinung und Erfahrung sagen, dann mit dem Partner diskutieren.</td>'),
 ('<li>Teil 2: Thema in fünf Schritten</li>', '<li>Teil 2: Bericht über den Text, Meinung, Gespräch</li>'),
 ('<td>Beitrag in fünf Schritten. Dann ein oder zwei Fragen beantworten.</td>', '<td>Über den Text berichten, Meinung und Erfahrung sagen, dann mit dem Partner diskutieren.</td>'),
 ('<td>Talk in five steps. Then answer one or two questions from the examiners or your partner.</td>', '<td>Report on your text, give your opinion and experience, then discuss with your partner.</td>'),
 ('Teil 2: alle fünf Schritte;', 'Teil 2: Bericht, Meinung, Erfahrung, Reaktion;'),
 ('Teil 2: all five steps;', 'Teil 2: report, opinion, experience, reaction;'),
 ('<td>Fünf Schritte: Einleitung · persönliche Erfahrung · Heimatland · Vor- und Nachteile · Abschluss.</td>', '<td>Bericht über deinen Text · Meinung mit Grund · eigene Erfahrung · reagieren und nachfragen.</td>'),
 ('<td>Five steps: Einleitung · persönliche Erfahrung · Heimatland · Vor- und Nachteile · Abschluss.</td>', '<td>Report on your text · opinion with a reason · own experience · react and ask questions.</td>'),
 ('<td>Mein Thema ist … · Ein Vorteil ist … · Ein Nachteil ist … · Meiner Meinung nach … · Vielen Dank für Ihre Aufmerksamkeit.</td>', '<td>In meinem Text geht es um … · Die Person meint, dass … · Meiner Meinung nach … · Bei mir ist das so: … · Wie siehst du das?</td>'),
 ('<li>Teil 2: fünf Schritte</li>', '<li>Teil 2: Bericht, Meinung, Gespräch</li>'),
 ('<td>Teil 1 Vorstellung, Teil 2 Vortrag in fünf Schritten, Teil 3 gemeinsam planen.</td>', '<td>Teil 1 Vorstellung, Teil 2 über einen Text berichten und diskutieren, Teil 3 gemeinsam planen.</td>'),
 # English goal and summary texts
 ('Sprechen Teil 2 in five steps.', 'Sprechen Teil 2: report on your text, give your opinion, discuss.'),
 ('Sprechen Teil 2: five steps, then answer a question.', 'Sprechen Teil 2: report on your text, give your opinion and experience, react to your partner.'),
 ('and give a talk in five steps in Sprechen Teil 2', 'and report on a text and discuss it in Sprechen Teil 2'),
 ('and give a five-step talk in Sprechen Teil 2', 'and report on a text and discuss it in Sprechen Teil 2'),
 ('the complete Hören section and a five-step talk (Teil 2)', 'the complete Hören section and Sprechen Teil 2 (report on a text and discuss)'),
 ('the five-step talk and the Teil-3 planning phrases aloud', 'the Teil 2 phrases (report, opinion, reaction) and the Teil-3 planning phrases aloud'),
 ('(Teil 1, a five-step talk, a joint planning task)', '(Teil 1, Teil 2 report and discussion, a joint planning task)'),
 ('(introduction, five-step talk, planning together)', '(introduction, Teil 2 report and discussion, planning together)'),
 ('Teil 2 five-step talk', 'Teil 2 report and discussion'),
]
OPEN = re.compile(r'<td class=de>Ich möchte über (.+?) sprechen\.</td><td>(Teil 2: )?Einleitung\.</td>')

n = 0
for f in sorted(glob.glob(os.path.join(D, 'D*', '*.html'))):
    t0 = t = open(f, encoding='utf-8').read()
    for p, r in BLOCKS:
        t = re.sub(p, lambda m: r, t, flags=re.S)
    for a, b in PHRASES:
        t = t.replace(a, b)
    t = OPEN.sub(lambda m: '<td class=de>In meinem Text geht es um %s.</td><td>%sBericht über den Text.</td>' % (m.group(1), m.group(2) or ''), t)
    if t != t0:
        open(f, 'w', encoding='utf-8').write(t); n += 1
print(n, 'files changed')

# second pass: D104 exercise and task text, goal sentences, note about the older model audio
NOTE = ('<p class="mut">Hinweis: In den Modell-Audios einiger Tage beginnt der Sprecher mit „Ich möchte über … sprechen“ und endet mit '
        '„Vielen Dank für Ihre Aufmerksamkeit“. Das ist nicht falsch, aber in telc Teil 2 hältst du keinen Vortrag. Es reicht: '
        '„In meinem Text geht es um …“, und am Ende fragst du deinen Partner: „Wie siehst du das?“</p>')
MORE = [
 ('<div class="q"><b>1.</b> Closing a Teil-2 talk:</div><div class="opts mc"><label><input type="radio" name="uebungen_1" value="a"> <span>a) Vielen Dank für Ihre Aufmerksamkeit.</span>',
  '<div class="q"><b>1.</b> End of your part in Teil 2 – you ask your partner:</div><div class="opts mc"><label><input type="radio" name="uebungen_1" value="a"> <span>a) Wie siehst du das?</span>'),
 ('"uebungen_1": {"t": "mc", "a": "a", "w": "höflicher, formeller Schluss.", "e": "polite formal closing."}',
  '"uebungen_1": {"t": "mc", "a": "a", "w": "Frage an den Partner: In Teil 2 sprecht ihr miteinander, es ist kein Vortrag.", "e": "a question to your partner: Teil 2 is a conversation, not a presentation."}'),
 ('fünf Schritte, Schluss mit „Vielen Dank für Ihre Aufmerksamkeit.“',
  'berichte über deinen Text, sag deine Meinung und Erfahrung und frage am Ende deinen Partner: „Wie siehst du das?“'),
 ('Sprechen Teil 2 in fünf Schritten.', 'Sprechen Teil 2 (über einen Text berichten und diskutieren).'),
 ('(Teil 1, Beitrag in fünf Schritten, gemeinsame Planung)', '(Teil 1, Teil 2 Bericht und Gespräch, gemeinsame Planung)'),
 ('(Vorstellung, Vortrag in fünf Schritten, gemeinsames Planen)', '(Vorstellung, Teil 2 Bericht und Gespräch, gemeinsames Planen)'),
 ('Vielen Dank für Ihre Aufmerksamkeit (Schluss eines Beitrags).', 'Vielen Dank für Ihre Aufmerksamkeit (Schluss eines Vortrags; in telc Teil 2 fragst du am Ende lieber deinen Partner).'),
]
m = 0
for f in sorted(glob.glob(os.path.join(D, 'D*', '*.html'))):
    t0 = t = open(f, encoding='utf-8').read()
    for a, b in MORE:
        t = t.replace(a, b)
    for head in ('<h3>B. Sprechen Teil 2: über einen Text berichten und diskutieren</h3>', '<h3>B. Sprechen Teil 2: Bericht, Meinung, Gespräch (Endform)</h3>'):
        i = t.find(head)
        if i >= 0:
            j = t.find('</table>', i) + len('</table>')
            if not t[j:j + 200].lstrip().startswith('<p class="mut">Hinweis: In den Modell-Audios'):
                t = t[:j] + '\n' + NOTE + t[j:]
    if t != t0:
        open(f, 'w', encoding='utf-8').write(t); m += 1
print(m, 'files changed (second pass)')
