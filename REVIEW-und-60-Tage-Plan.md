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

## 2. Prüfungsfakten: Widersprüche im Repo (bitte zuerst prüfen)

Ich konnte die offizielle telc-Seite aus dieser Umgebung nicht erreichen. Die folgenden Punkte bitte mit dem **offiziellen Übungstest „telc Deutsch B1 / Zertifikat Deutsch“** (kostenlos auf telc.net) abgleichen. Danach passe ich alle Seiten einheitlich an.

| Thema | Was im Repo steht | Wo | Meine Einschätzung |
|-------|-------------------|----|--------------------|
| **Hören Teil 3** | Leitfaden: „Eine Diskussion zwischen mehreren Personen“. Modelltests und Tagesseiten: „5 kurze Texte (Anrufbeantworter, Durchsagen), zweimal“. | `docs/index.html` gegen `Modelltests/*`, D62 | Eher die Version der Modelltests (kurze Alltagstexte). Den Leitfaden sollte man anpassen. **Bitte prüfen.** |
| **Sprechen Teil 2** | Einige Tage lehren einen **Vortrag in 5 Schritten** mit „Heimatland, Vor-/Nachteil, Dank“. Das ist das Format von **Goethe B1**. Andere Tage lehren „einen Text vorstellen und Meinung sagen“. | D57, D66, D78, D85, D99 gegen D22, D29, D36, D43 | Bei telc ist Teil 2 ein **Gespräch über ein Thema** auf Basis kurzer Texte, keine Präsentation mit Folien. **Bitte prüfen.** Wenn das stimmt, müssen 5 Tage umgeschrieben werden. |
| **Sprechen: Punkte** | D78: Teil 1 = 15, Teil 2 = 30, Teil 3 = 30. | D78, D17 | Nach meinem Wissen: 15 + 30 + 15 und **15 Punkte für Aussprache**. **Bitte prüfen.** |
| **Schreiben: Leitpunkte** | Der Leitfaden und 38 Tage sagen **4 Leitpunkte**. 67 Tage sagen **5 Leitpunkte**. | viele Tage | Wahrscheinlich 4. Alle Aufgaben sollten einheitlich sein. |
| **Schreiben: Wortzahl** | D07 sagt „80–100 Wörter“, der Leitfaden „100–120“. | D07 gegen `index.html` | Telc nennt laut Leitfaden keine feste Zahl. Wir sollten **eine** Empfehlung nennen. |

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

1. **Sprechen Teil 2 in etwa 17 Geschichten:** Als Thema steht dort der Titel der Geschichte. Text A und Text B sind keine gegensätzlichen Meinungen, sondern Erlebnisse oder Fakten. Deshalb wirkt die Modellrede mit „Vorteil/Nachteil“ unlogisch.
   - Betroffen: S16, S19, S20, S22, S24, S30, S31, S32, S33, S34, S35, S36, S38, S39, S40, S58, S66.
   - Vorschlag: eine echte Diskussionsfrage (zum Beispiel S20: „Arzttermin online buchen oder anrufen?“), zwei gegensätzliche Meinungen und eine neue Modellrede.
   - Wird erst gemacht, wenn das telc-Format von Sprechen Teil 2 geklärt ist (Abschnitt 2).
2. **S40 (Bildbeschreibung):** Das ist ein DTZ-Format und kommt in telc B1 nicht vor. Die Geschichte ist jetzt als Training markiert. Sie könnte ganz in ein telc-Thema umgebaut werden.
3. **Wortzahl beim Schreiben** ist in den Geschichten uneinheitlich: 100–120 Wörter (14 Geschichten), 80–100 (12), 60–80 (S39). Sie wird zusammen mit Abschnitt 2 vereinheitlicht.
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
