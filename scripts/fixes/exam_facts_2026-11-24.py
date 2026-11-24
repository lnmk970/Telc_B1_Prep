#!/usr/bin/env python3
"""Align the site with the official telc Deutsch B1 Übungstest 1 (telc gGmbH, 2020).
- Schreiben: 4 Leitpunkte (D26–D92 had 5: two related points are merged, or a closing-formula point is dropped)
- Schreiben: one recommendation, "etwa 100 Wörter" (the official task names no word count)
- Hören: correct description of Teil 1 (opinions, once) and Teil 3 (announcements, twice) in the guide
Usage: python3 scripts/fixes/exam_facts_2026-11-24.py   (idempotent)
"""
import re, glob, os
D = os.path.join(os.path.dirname(__file__), '..', '..', 'docs')

# (op, a, b, label): merge items a and b into one item with label; ('drop', i) removes a closing-formula item
OPS = {
 26: ('merge', 1, 2, 'Erfahrung im Service und Sprachkenntnisse'),
 27: ('merge', 0, 1, 'Dank und Grund: Warum waren Sie nicht im Kurs? (mit weil)'),
 28: ('merge', 1, 2, 'Rat zum Schlaf und zum Arzt (ja oder nein? warum?)'),
 29: ('merge', 2, 3, 'Kosten der Mitgliedschaft und Probestunde'),
 30: ('drop', 4),
 31: ('merge', 2, 3, 'Preis, Termine und Probestunde'),
 32: ('merge', 1, 2, 'Rat: Arzt und Sport (mit Begründung)'),
 33: ('merge', 0, 1, 'Wo wohnen Sie, und wie ist das Hotel? (Lage mit Wechselpräposition)'),
 34: ('merge', 3, 4, 'Frühstück inklusive? Hund erlaubt?'),
 35: ('merge', 3, 4, 'Etwas Negatives, und wollen Sie wieder hin?'),
 36: ('merge', 2, 3, 'Anreise und Unterkunft'),
 37: ('drop', 4),
 38: ('merge', 3, 4, 'Was erwarten Sie jetzt? (mit Frist)'),
 39: ('merge', 3, 4, 'Was erwarten Sie? (mit Frist für die Antwort)'),
 40: ('merge', 0, 1, 'Ihre Meinung mit zwei Gründen'),
 41: ('merge', 3, 4, 'Was wollen Sie jetzt? (mit Frist)'),
 42: ('merge', 1, 2, 'Zwei Ratschläge: Schlaf oder Sport, Gespräch mit dem Chef'),
 43: ('merge', 1, 2, 'Ihre Meinung mit zwei Gründen'),
 44: ('merge', 2, 3, 'Bitte um einen Handwerker: Wann sind Sie zu Hause?'),
 45: ('merge', 1, 2, 'Essen und Trinken: Was sollen die Gäste mitbringen?'),
 46: ('merge', 3, 4, 'Ihre Forderung mit Frist'),
 47: ('merge', 3, 4, 'Einstufungstest und Bitte um ein Anmeldeformular'),
 48: ('merge', 1, 2, 'Ein Tipp: Wie lernen Sie Vokabeln?'),
 49: ('merge', 1, 2, 'Termin passt nicht (mit Grund) und neuer Vorschlag'),
 50: ('merge', 2, 3, 'Tipp: eine Sprachschule empfehlen'),
 51: ('merge', 2, 3, 'Kosten, und wer berät?'),
 52: ('merge', 2, 3, 'Mitbringen und Ablauf der Treffen'),
 53: ('merge', 3, 4, 'Mitbringen und Dauer des Praktikums'),
 54: ('merge', 2, 3, 'Höfliche Bitte um einen neuen Termin: Wann haben Sie Zeit?'),
 55: ('merge', 0, 1, 'Umzugstermin und Frist zur Ummeldung'),
 56: ('drop', 4),
 57: ('merge', 1, 2, 'Kosten und Kreditkarte'),
 58: ('merge', 2, 3, 'Höfliche Bitte um Entschädigung oder Rückerstattung'),
 59: ('merge', 2, 3, 'Mitbringen oder Bezahlen, und wer hilft?'),
 60: ('merge', 0, 1, 'Problem und Grund für den Ärger'),
 61: ('merge', 2, 3, 'Hund und Anreise mit dem Zug'),
 62: ('drop', 4),
 63: ('merge', 1, 2, 'Erste Erlebnisse und ein besonderes Erlebnis'),
 64: ('merge', 2, 3, 'Anreise, Programm und wer sich um was kümmert'),
 65: ('merge', 2, 3, 'Stornogebühren und Rückerstattung'),
 66: ('merge', 0, 1, 'Dank, Zusage und Grund'),
 67: ('merge', 2, 3, 'Bitte um Entschädigung (mit Summe) und Frage nach der Dauer'),
 68: ('merge', 0, 1, 'Vorstellung und Grund der Suche'),
 69: ('merge', 0, 1, 'Vorstellung und Grund der Bewerbung'),
 70: ('merge', 0, 2, 'Problem und Folgen'),
 71: ('merge', 0, 1, 'Planung, Datum und Grund'),
 72: ('merge', 3, 4, 'Besichtigung: Wann haben Sie Zeit?'),
 73: ('drop', 4),
 74: ('merge', 0, 2, 'Problem und Folgen für die Nachbarin'),
 75: ('merge', 0, 1, 'Was passiert ist und warum Sie sich ärgern'),
 76: ('merge', 0, 1, 'Was passiert ist und warum Sie sich ärgern'),
 77: ('merge', 1, 2, 'Eigene Überlegungen mit Grund und Budget'),
 78: ('merge', 3, 4, 'Frage nach Begleitung und Weg'),
 79: ('merge', 0, 1, 'Vorstellung, Kurs und Grund'),
 80: ('merge', 0, 1, 'Hobby und Grund'),
 81: ('merge', 3, 4, 'Hilfe beim Aufbau und Regenplan'),
 82: ('merge', 0, 1, 'Vorstellung und Grund'),
 83: ('merge', 0, 1, 'Was passiert ist und warum Sie sich ärgern'),
 84: ('merge', 0, 2, 'Was passiert ist und Folgen'),
 85: ('merge', 0, 1, 'Einladung mit Details und Grund'),
 86: ('merge', 0, 1, 'Einladung mit Datum und Grund'),
 87: ('merge', 0, 1, 'Rat mit Begründung: Vorteil und Nachteil'),
 88: ('merge', 1, 3, 'Beginn, Dauer und Unterrichtszeit'),
 89: ('merge', 0, 1, 'Antrag, Datum und Problem'),
 90: ('merge', 3, 4, 'Hilfe anbieten und Frage nach der Abreise'),
 91: ('merge', 0, 1, 'Reaktion und Rat mit Begründung'),
 92: ('merge', 0, 1, 'Rat mit Begründung'),
}
LIST = re.compile(r'(<p><b>Schreiben Sie zu allen Leitpunkten:</b></p><ul class="tight">)(.*?)(</ul>)', re.S)

def fix_list(m, n):
    items = re.findall(r'<li>(.*?)</li>', m.group(2), re.S)
    if len(items) != 5:
        return m.group(0)  # already 4 (re-run) or other format
    op = OPS[n]
    if op[0] == 'drop':
        items.pop(op[1])
    else:
        _, a, b, label = op
        items[a] = label
        items.pop(b)
    return m.group(1) + ''.join('<li>%s</li>' % x for x in items) + m.group(3)

WORDS = [  # (pattern, replacement)
    (r'([Ee])twa (?:80|90) bis (?:100|110) Wörter', r'\1twa 100 Wörter'),
    (r'(?<![Ee]twa )\b(?:80 bis 100|90 bis 110|80–100|90–110|100–120) Wörter', 'etwa 100 Wörter'),
    (r'(?i)about (?:80|90)–(?:100|110) words', 'about 100 words'),
    (r'(?<!about )\b(?:80–100|90–110|100–120) words', 'about 100 words'),
]
FIVE = [
    ('Alle fünf Leitpunkte', 'Alle vier Leitpunkte'), ('alle fünf Leitpunkte', 'alle vier Leitpunkte'),
    ('allen fünf Leitpunkten', 'allen vier Leitpunkten'), ('fünf Leitpunkten', 'vier Leitpunkten'),
    ('fünf Leitpunkte', 'vier Leitpunkte'), ('alle 5 Leitpunkte', 'alle 4 Leitpunkte'),
    ('mit 5 Leitpunkten', 'mit 4 Leitpunkten'), ('5 Leitpunkte', '4 Leitpunkte'),
]
changed = {}
for f in sorted(glob.glob(os.path.join(D, 'D*', '*.html'))):
    n = int(re.match(r'D(\d+)', os.path.basename(os.path.dirname(f))).group(1))
    t0 = t = open(f, encoding='utf-8').read()
    if f.endswith('day.html') and n in OPS:
        t = LIST.sub(lambda m: fix_list(m, n), t)
    if n >= 26:
        for a, b in FIVE:
            t = t.replace(a, b)
    # word counts: from D26 on all of them; before D26 only the general exam notes
    # (the D01–D25 practice tasks build up from 30 words on purpose; D103–D105 have short 50–80 warm-ups)
    if n >= 26:
        for p, r in WORDS:
            t = re.sub(p, r, t)
    else:
        t = t.replace('Etwa 80 bis 100 Wörter, in 30 Minuten', 'Etwa 100 Wörter, in 30 Minuten')
        t = t.replace('in der Prüfung solltest du etwa 80–100 Wörter schreiben', 'in der Prüfung solltest du etwa 100 Wörter schreiben')
    if t != t0:
        open(f, 'w', encoding='utf-8').write(t)
        changed[os.path.relpath(f, D)] = 1

# guide on the start page
g = os.path.join(D, 'index.html')
t0 = t = open(g, encoding='utf-8').read()
t = t.replace('<td>5 kurze Texte: Durchsagen, Nachrichten, Anrufbeantworter</td>',
              '<td>5 kurze Texte zu einem Thema: Fünf Personen sagen ihre Meinung oder erzählen, wie es bei ihnen ist</td>')
t = t.replace('<td>Eine Diskussion oder ein Gespräch zwischen mehreren Personen</td>',
              '<td>5 kurze Alltagstexte: Durchsagen (Bahnhof, Zug), Wetterbericht, Wegbeschreibung, Programm- oder Werbeansagen</td>')
t = t.replace('<li>Teil 1 hörst du nur einmal. Wenn du eine Aufgabe verpasst,',
              '<li>Teil 1: Jede Person sagt ihre Meinung. Achte darauf, was <b>diese</b> Person selbst macht oder denkt. Teil 3: Achte auf Zahlen, Zeiten, Orte und Preise. Teil 1 hörst du nur einmal. Wenn du eine Aufgabe verpasst,')
t = re.sub(r'Schreibe etwa 100–120 Wörter\. Das ist eine übliche Empfehlung, keine offizielle Regel für B1\.',
           'Schreibe etwa 100 Wörter. Die offizielle Aufgabe nennt keine Wortzahl. Mit etwa 100 Wörtern kannst du alle vier Leitpunkte gut behandeln.', t)
if t != t0:
    open(g, 'w', encoding='utf-8').write(t)
    changed['index.html'] = 1
print(len(changed), 'files changed')
