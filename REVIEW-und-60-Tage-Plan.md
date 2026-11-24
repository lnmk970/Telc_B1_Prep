# Repo-Review: Von A1 zu telc B1 in 60 Tagen

Stand: 24.11.2026. Geprüft wurden:
- die Übersichtsseite mit dem Prüfungsleitfaden (`docs/index.html`),
- alle 105 Tagesseiten mit ihren Lösungsseiten,
- die 7 Modelltests,
- der Wortschatz (4.478 Einträge),
- die 78 Geschichten,
- README und Skripte.

## 1. Kurzfazit

**Was schon gut ist**
- Alle Prüfungsteile werden täglich geübt:
  - Lesen 1–3,
  - Sprachbausteine 1–2,
  - Hören 1–3,
  - Schreiben,
  - Sprechen 1–3.
- Zu jedem Tag gibt es Lösungen und Audio. Dazu kommen 7 Modelltests und 4 Mock-Prüfungen im Tagesplan.
- Der Prüfungsleitfaden bietet:
  - eine Strategie pro Teil,
  - typische Fallen,
  - Schreibvorlagen zum Auswendiglernen,
  - Redemittel fürs Sprechen.
- Die Grammatik-Progression passt zu B1: Präsens → Kasus → Perfekt → Nebensätze → Adjektivendungen → Relativsätze → Konjunktiv II → Passiv → Genitiv.
- Alles ist zweisprachig (Deutsch und Englisch). Das ist für A1-Lernende sehr wichtig.

**Was fehlt oder nicht stimmt**

| # | Problem | Wirkung |
|---|---------|---------|
| 1 | Der Plan hat **105 Tage**. Es gibt keinen 60-Tage-Weg. | Wer 60 Tage hat, weiß nicht, was er weglassen darf. |
| 2 | Einige **Prüfungsfakten widersprechen sich** zwischen den Seiten (siehe Abschnitt 2). | Lernende üben ein falsches Format. Das ist das größte Risiko. |
| 3 | Einige **B1-Grammatikthemen haben keine eigene Lektion** (siehe Abschnitt 3). | Sie kosten Punkte in Sprachbausteinen und Lesen. |
| 4 | **Aussprache** wird nirgends gezielt geübt. | Laut den Bewertungskriterien zählt Aussprache beim Sprechen mit. |
| 5 | Die README ist sehr kurz und hat kein „Hier anfangen“. | Neue Nutzer finden den Einstieg nicht. |

**Ehrliche Einschätzung zum Ziel „A1 → B1 in 60 Tagen“:**
- Der Schritt von A1 zu B1 braucht üblicherweise mehrere hundert Lernstunden. Das ist eine grobe Faustregel und keine offizielle telc-Zahl.
- In 60 Tagen heißt das: etwa **4–5 Stunden pro Tag, jeden Tag**.
- Mit diesem Repo ist das schaffbar, wenn der 60-Tage-Plan unten genau eingehalten wird. Mit 1–2 Stunden pro Tag reicht es nicht.
- Das sollte am Anfang der Seite klar stehen, damit niemand falsche Erwartungen hat.

## 2. Prüfungsfakten: geprüft mit dem offiziellen telc-Übungstest

Am 24.11.2026 abgeglichen mit dem offiziellen **Übungstest 1 „telc Deutsch B1 / Zertifikat Deutsch“ (telc gGmbH, 2020)**.

| Thema | Offiziell (Übungstest 1) | Was im Repo steht | Status |
|-------|--------------------------|-------------------|--------|
| **Hören Teil 1** | 5 kurze Texte, **einmal**: Meinungen von Personen zu einem Thema (Globalverstehen) | Leitfaden (`docs/index.html`): „Durchsagen, Nachrichten, Anrufbeantworter“. In **allen 7 Modelltests** sind die Texte in Teil 1 Durchsagen, Mailbox-Nachrichten und Verkehrsmeldungen (also Teil-3-Stil). | Leitfaden **korrigiert** (24.11.). Modelltests: Texte, Aussagen und Lösungen **neu** (24.11.), die neuen MP3s müssen noch erzeugt werden (siehe unten). |
| **Hören Teil 2** | ein Gespräch oder Interview, **zweimal**, 10 Aufgaben | stimmt | ok |
| **Hören Teil 3** | 5 kurze Texte, **zweimal**: Wegbeschreibung, Kinoprogramm, Wetterbericht, Durchsage im Zug, Werbung | Leitfaden: „eine Diskussion“. Modelltests und Tagesseiten: Ansagen, Durchsagen | Leitfaden **korrigiert**, Modelltests ok |
| **Sprechen Teil 2** | Jede Person bekommt ein anderes Blatt mit **einer kurzen Meinung** (Name, Alter, Beruf). Beide berichten über ihren Text, dann sprechen sie über eigene Meinungen und Erfahrungen. | Etwa 20 Tagesseiten: „Vortrag in 5 Schritten“ (Goethe-Format) | **korrigiert** (24.11.): Tabellen, Aufgaben, Ziele und Übungen zeigen jetzt Bericht → Nachfrage → Meinung → Erfahrung → Reaktion. Die Modell-Audios (Transkripte in answers.html) beginnen noch mit „Ich möchte über … sprechen“ und enden mit „Vielen Dank für Ihre Aufmerksamkeit“. In D57 und D85 steht dazu ein Hinweis. |
| **Sprechen: Punkte** | Teil 1: **15**, Teil 2: **30**, Teil 3: **30** (= 75) | D78: 15 / 30 / 30 | **D78 stimmt.** Meine frühere Vermutung (15 / 30 / 15 + Aussprache) war falsch. |
| **Schreiben: Leitpunkte** | **4 Leitpunkte** (dazu passender Betreff, Anrede, Einleitung, Schluss) | 67 Tage sagten „5 Leitpunkte“ | **korrigiert** (24.11.): Je zwei verwandte Punkte wurden zusammengelegt, oder ein reiner Schlusspunkt („Gruß und Ausblick“) wurde gestrichen. Alle Aufgaben haben jetzt 4 Leitpunkte. |
| **Schreiben: Wortzahl** | Die Aufgabe nennt **keine** Wortzahl. | vorher uneinheitlich | **korrigiert** (24.11.): überall „etwa 100 Wörter“. Ausnahmen: D01–D25 steigern die Länge bewusst (30 → 100), und D103–D105 sind kurze Aufwärmversionen. |
| Zeit | Lesen + Sprachbausteine 90 Min., Hören ca. 30 Min., Schreiben 30 Min. Mündlich ca. 15 Min. zu zweit, 20 Min. Vorbereitung. | stimmt | ok |


**Noch offen (neue MP3s erzeugen):** Die Texte sind neu geschrieben (Moderation + fünf Meinungen zu einem Thema). Vorher war in allen 7 Modelltests Hören Teil 1 im Stil von Teil 3 (Durchsagen, Mailbox, Verkehr). Im offiziellen Test sind es fünf Personen, die ihre Meinung zu **einem** Thema sagen (Globalverstehen). Für die Korrektur braucht man pro Modelltest neue Hörtexte und Aussagen in `audio.json` und `index.html` und danach neue MP3-Dateien. Die MP3s erzeugt `docs/gen_audio.py` mit edge-tts. Das ging in dieser Cloud-Umgebung nicht (Server nicht erreichbar), auf einem eigenen Computer aber schon.

## 3. Grammatik: Was fehlt (neue Themen)

Abgedeckt sind:
- Präsens,
- sein und haben,
- Akkusativ und Dativ,
- Präpositionen (inkl. Wechselpräpositionen),
- Modalverben,
- trennbare Verben,
- Perfekt,
- Präteritum von sein, haben und den Modalverben,
- die Konnektoren aus dem Plan (weil, dass, wenn, obwohl, deshalb, trotzdem, als, während, bevor, bis, nachdem),
- Komparativ und Superlativ,
- reflexive Verben,
- Adjektivendungen,
- Relativsätze,
- zu-Infinitiv mit um … zu,
- Konjunktiv II,
- indirekte Fragen,
- Verben mit Präposition mit da-/wo-Wörtern,
- Passiv Präsens und Passiv mit Modalverben,
- wegen und trotz mit Genitiv.

**Ohne eigene Lektion, sollte aber hinein (nach Priorität):**

| Priorität | Thema | Warum für telc B1 wichtig | Vorschlag |
|-----------|-------|---------------------------|-----------|
| hoch | **Zweiteilige Konnektoren**: entweder … oder, sowohl … als auch, weder … noch, nicht nur … sondern auch, je … desto, zwar … aber | Sie kommen oft in den Sprachbausteinen vor. Im Repo tauchen sie fast nur in Beispielen auf (1–2 Seiten). | eigene Lektion in Woche 8 oder 9 |
| hoch | **Präteritum der normalen Verben** (ging, kam, fuhr, sagte, machte, gab, fand, wurde) | Zeitungsartikel in Lesen Teil 2 und Hören sind im Präteritum. Bisher gibt es nur war, hatte und die Modalverben. | Lektion zum Erkennen, mit einer Liste der 40 häufigsten Formen |
| hoch | **damit gegen um … zu** (Zweck mit gleichem oder anderem Subjekt) | ein typischer Lückentyp | in D49 ausbauen |
| mittel | **Futur I** (werden + Infinitiv) | Briefe und Pläne; werden hat drei Bedeutungen (Futur, Passiv, „Veränderung“) | kurze Lektion vor dem Passiv (W10) |
| mittel | **Imperativ** (du, ihr, Sie) | für Bitten in E-Mails und für Anleitungen beim Lesen | kurze Lektion in W2 |
| mittel | **Konjunktiv II Vergangenheit** (hätte … gemacht, wäre … gekommen) | wird in der Absage-Vorlage benutzt („wäre gern gekommen“), aber nicht erklärt | Abschnitt in D57 |
| mittel | **Plusquamperfekt** außerhalb von nachdem | wird für das Lesen gebraucht | ist in D63; als Wiederholung einbauen |
| mittel | **Passiv Präteritum** (wurde gebaut) | Lesetexte, Nachrichten | in D89 ergänzen |
| niedrig | **n-Deklination** (Herrn, Kollegen, Nachbarn, Kunden) | Anrede „Sehr geehrter Herr …“, Sprachbausteine | Infobox |
| niedrig | **Indefinitpronomen** (man, jemand, niemand, etwas, nichts, einer, keiner, welche) | Sprachbausteine Teil 2 | Infobox |
| niedrig | **Wortbildung** (-ung, -heit, -keit, -ion, un-, -bar, -los) | Wörter in Lesen und Sprachbausteine Teil 2 erraten | eine Seite |
| niedrig | **lassen** (Ich lasse mein Auto reparieren.) | häufig in Dienstleistungs-Texten | Infobox in W8 |

**Aussprache (neu, hoch):**
- Aussprache zählt beim Sprechen mit.
- Bisher wird auf keiner Seite gezielt geübt:
  - Umlaute ü, ö, ä,
  - ch (ich gegen ach),
  - r,
  - Wortakzent,
  - Satzmelodie.
- Vorschlag: täglich 5 Minuten Nachsprechen mit den vorhandenen Audios (`vocab.mp3`, `sprechen_modell.mp3`), dazu eine Aussprache-Seite in der Starter-Phase.

## 4. Deutsch-Fehler

- **Tagesseiten, Modelltests, Leitfaden:** Die automatische Prüfung aller Seiten fand **keine echten Fehler**. Gesucht wurde nach:
  - doppelten Wörtern,
  - haben oder sein im Perfekt,
  - wegen mit Dativ,
  - Verbstellung nach weil,
  - das oder dass,
  - Kasus nach Präpositionen,
  - Anredeformen.
  
  Alle Treffer waren absichtlich falsche Antwortmöglichkeiten (zum Beispiel „mit der Zug“ als Ablenker).
  - Hinweis: Das war eine Stichprobe mit Suchregeln. Eine vollständige Prüfung durch eine Muttersprachlerin wäre der nächste Schritt.
- **Geschichten:** Fehler wurden in früheren Runden korrigiert, zum Beispiel:
  - „ich wertete“,
  - „Um was“,
  - „in einen Regen“,
  - falsche Teil-Nummern.

## 5. Weitere Punkte

1. **Geschichten S16–S78** haben jetzt dieselbe Struktur wie S07–S15. Die Dichte liegt aber nur bei etwa 40 %:
   - etwa 120 statt etwa 300 Grammatik-Notizen,
   - etwa 930 statt etwa 2.200 markierte Wörter.
   
   Das ist für den 60-Tage-Plan unten nicht kritisch, weil dort nur die Geschichten zu den Tagesthemen gelesen werden.
2. Etwa 1.169 Wortschatz-Wörter kommen noch in keiner Geschichte vor.
3. **Datum:** Der Plan ist fest auf den 25.02.2027 datiert (Ordnernamen, Texte wie „wie am 25. Februar“ in D102). Das Prüfungsdatum lässt sich auf der Übersicht ändern, die Tagesreihenfolge aber nicht.
4. **Aufräumen:** 25 Logdateien `docs/_audio_*.log` werden mit veröffentlicht und sind unnötig.
5. **README:** Es fehlt eine Anleitung „So benutzt du das Repo“, mit 60-Tage-Plan, Tagesablauf und Link zum Leitfaden.

## 5b. Review der Geschichten (24.11.2026)

**Geprüft:**
- alle 78 Geschichten mit 15.248 deutschen Sätzen und Fragen,
- `check_geschichten.js` (bestanden),
- Browser-Test aller Seiten (keine Fehler),
- Suchregeln für typische Deutschfehler,
- doppelte Texte,
- Prüfungsangaben.

**Korrigiert:**
- S01–S06: „Mir gefällt die Größe der Stadt, die Thermen und …“ → **gefallen** (mehrere Subjekte).
- S01–S06: „Ich spreche Englisch, Telugu …, weil Telugu meine Muttersprache ist“ war unlogisch. Neu: „Ich spreche Telugu, weil es meine Muttersprache ist. Außerdem spreche ich Englisch und ein bisschen Deutsch.“
- S32: Im Gespräch stand das Präteritum („Und was tatst du?“, „Ich rief …“). Der Tipp empfahl sogar, beim Sprechen das Präteritum zu benutzen. Neu: Perfekt im Gespräch. Der Tipp erklärt jetzt: Das Präteritum erkennt man in Zeitungstexten, beim Sprechen benutzt man nur war, hatte und die Modalverben.
- Prüfungsangaben:
  - „DTZ“ (eine andere Prüfung) entfernt (S16, S19, S22, S23, S40).
  - „telc Teil 1“ beim Schreiben entfernt, weil telc B1 nur eine Schreibaufgabe hat (S21, S26, S27, S31, S35 und Grammatiknotizen).
  - S20: „Termin vereinbaren“ heißt jetzt „gemeinsam einen Termin planen“.

**Noch offen:**

1. ~~Sprechen Teil 2 in 17 Geschichten~~ **erledigt** (24.11.2026, Format des offiziellen Übungstests):
   - S16, S19, S20, S22, S24, S30–S36, S38, S39, S40, S58 und S66 haben jetzt eine echte Diskussionsfrage, zwei gegensätzliche Meinungstexte, eine neue Modellrede und ein Gespräch, in dem auch die andere Meinung vorkommt.
   - Die 34 passenden Zeilen in der Sprechen-Tabelle sind neu.
   - In S34, S36 und S38 war die Überschrift falsch („Teil 1“ / „Teil 3“).
   - S40 übt jetzt „Freizeit draußen oder zu Hause?“ mit Wechselpräpositionen statt einer Bildbeschreibung.
2. **Alle 61 übrigen Teil-2-Aufgaben** haben jetzt den offiziellen Aufgabentext („Sie haben in einer Zeitschrift etwas zum Thema … gelesen …“).
3. **Falsche automatische Grammatik-Notizen korrigiert:**
   - 80 × „zu“ vor einem Infinitiv (zu sparen) oder mit der Bedeutung „too“ (zu viel) war als Dativ-Präposition erklärt.
   - 4 abtrennbare Vorsilben (kommst du mit ins Kino) waren als Präposition erklärt.
   - 17 × „Sie“ mit der Bedeutung „she“ oder „they“ war als höfliches „Sie“ erklärt.
   - „ab und zu“ war falsch erklärt.
   - 44 Nachnamen (Keller, Winter …) hatten eine Vokabel-Erklärung (der Keller = cellar).
   - Die Regeln in `scripts/expand/auto_rules.js` sind korrigiert, damit diese Fehler nicht wieder entstehen.
4. **Wortzahl beim Schreiben** ist in den Geschichten weiter uneinheitlich. Sie wird zusammen mit den Tagesseiten vereinheitlicht (Abschnitt 2).
4. Die Dichte von S16–S78 liegt weiter bei etwa 40 % von S07–S15 (siehe Abschnitt 5).

## 6. Der 60-Tage-Plan (umgesetzt am 24.11.2026)

Auf der Startseite gibt es jetzt einen Schalter **„105-Tage-Plan / 60-Tage-Plan (A1 → B1)“**. Der 60-Tage-Plan enthält **alle 105 Tagesseiten**, nichts fällt weg:

| Tage | Phase | Inhalt |
|------|-------|--------|
| 1–30 | Lernen | Alle Lektionstage (Starter, Mo–Fr der Wochen 1–10, D38) plus die 9 Zusatzlektionen N1–N9, meist 2 Seiten pro Tag |
| 31–45 | Wiederholen und verbessern | Alle Samstags-Wiederholungen, alle Wochentests und der Checkpoint, alle Vollversion- und Reparaturtage (D75–D101) |
| 46–60 | Probeprüfungen | Modelltests 1–7, Probeprüfungen 1–4 (D81, D88, D95, D102), 2 Fehlertage, D103–D105 |

- Die Daten zählen 60 Tage rückwärts vom eingestellten Prüfungsdatum.
- Der Fortschritt gilt für beide Pläne.
- Die genaue Zuordnung steht in `PLAN60` in `docs/index.html`.

## 7. Was als Nächstes zu tun ist (Reihenfolge)

1. **Prüfungsfakten klären** (Abschnitt 2): Mit dem offiziellen telc-Übungstest abgleichen. Danach alle Seiten einheitlich machen (Hören Teil 3, Sprechen Teil 2, Punkte, 4 oder 5 Leitpunkte, Wortzahl).
2. ~~60-Tage-Plan auf die Übersichtsseite~~ erledigt (Umschalter „105 Tage / 60 Tage“, siehe Abschnitt 6).
3. ~~Neue Lektionen~~ erledigt (`docs/Lektionen`, N1–N9). Ursprünglich: hohe Priorität:
   - zweiteilige Konnektoren,
   - Präteritum der normalen Verben,
   - damit gegen um … zu,
   - Aussprache.
4. ~~Neue Lektionen~~ erledigt. Ursprünglich: mittlere Priorität: Futur I, Imperativ, Konjunktiv II Vergangenheit, Passiv Präteritum.
5. ~~README~~ erledigt. Ursprünglich: neu schreiben, mit „Hier anfangen“.
6. Logdateien löschen.
7. Optional: Geschichten S16–S78 weiter verdichten.
