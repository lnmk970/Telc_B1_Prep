# Geschichten S01–S15: Checkliste für Sprechen und Schreiben

Stand: alle Punkte sind in der Seite umgesetzt und im Browser geprüft (alle 15 Geschichten, keine JavaScript-Fehler, kein horizontales Scrollen auf dem Handy).

## Aufgaben

- [x] **1. Teil 1 nur bis S06.** Die Sätze zum Vorstellen (Woher kommst du, Wo wohnst du, Beruf, Familie, Freizeit) erscheinen nur in S01–S06.
- [x] **2. Partner und Prüfer getrennt.** In jeder Geschichte eine Tabelle mit drei Spalten: Partner (er) mit Peter, Partnerin (sie) mit Anna und Prüfer/in (Sie), jeweils mit englischer Übersetzung.
- [x] **3. Teil-3-Redemittel.** Gemeinsame Redemittel für alle Geschichten: Ich schlage vor …, Was hältst du davon?, zustimmen, widersprechen, nachfragen, Zeit gewinnen, Abschluss.
- [x] **4. Schreiben-Checkliste und Selbstcheck.** Jede Schreibaufgabe hat die vier Punkte aus der Aufgabe, Anrede und Gruß (informell oder formell) und drei Fragen zum lauten Beantworten.

## Konsistenz-Regel (nicht vergessen)

Jede Geschichte S01–S15 muss dieselben Teile haben. Vor jedem Commit ausführen:

```
node scripts/check_geschichten.js
```

Das Skript prüft: keine alten Namen (Tom), Teil-2- und Teil-3-Partner heißen Anna und Peter, Prüfer-Zeile im Dialog, drei Fassungen je Zeile (er, sie, Prüfer), Schreiben-Checkliste mit mindestens fünf Punkten, drei Selbstcheck-Fragen und markierte Prüfungsphrasen. Teil 1 gilt nur bis S06.

## Stand pro Geschichte

| Story | Thema | Teil 1 | Partner/Prüfer-Tabelle | Teil-3-Redemittel | Schreiben-Checkliste | Selbstcheck | Doppelte Unterstreichung (Anzahl) | Partner im Dialog | Prüfer im Dialog |
|---|---|---|---|---|---|---|---|---|---|
| S01 | Hallo, ich heiße Manoj | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ 52 | Anna (Teil 2), Peter (Teil 3) | ✅ Prüfer-Gespräch im Dialog |
| S02 | Im Bürgeramt | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ 43 | Anna (Teil 2), Peter (Teil 3) | ✅ Prüfer-Gespräch im Dialog |
| S03 | Frühstück am Sonntag | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ 38 | Anna (Teil 2), Peter (Teil 3) | ✅ Prüfer-Gespräch im Dialog |
| S04 | Einkaufen im Supermarkt | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ 39 | Anna (Teil 2), Peter (Teil 3) | ✅ Prüfer-Gespräch im Dialog |
| S05 | Meine neue Wohnung | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ 32 | Anna (Teil 2), Peter (Teil 3) | ✅ Prüfer-Gespräch im Dialog |
| S06 | Mein Tag | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ 40 | Anna (Teil 2), Peter (Teil 3) | ✅ Prüfer-Gespräch im Dialog |
| S07 | Ich stelle mich vor | — | ✅ | ✅ | ✅ | ✅ | ✅ 32 | Anna (Teil 2), Peter (Teil 3) | ✅ Prüfer-Gespräch im Dialog |
| S08 | Antwort an eine Freundin | — | ✅ | ✅ | ✅ | ✅ | ✅ 36 | Anna (Teil 2), Peter (Teil 3) | ✅ Prüfer-Gespräch im Dialog |
| S09 | Eine Beschwerde schreiben | — | ✅ | ✅ | ✅ | ✅ | ✅ 45 | Anna (Teil 2), Peter (Teil 3) | ✅ Prüfer-Gespräch im Dialog |
| S10 | Mein Thema: Homeoffice | — | ✅ | ✅ | ✅ | ✅ | ✅ 51 | Anna (Teil 2), Peter (Teil 3) | ✅ Prüfer-Gespräch im Dialog |
| S11 | Gemeinsam einen Ausflug planen | — | ✅ | ✅ | ✅ | ✅ | ✅ 46 | Anna (Teil 2 und Szene 1), Peter (Teil 3) | ✅ Prüfer-Gespräch im Dialog |
| S12 | Den Mantel zurückschicken | — | ✅ | ✅ | ✅ | ✅ | ✅ 45 | Anna (Teil 2), Peter (Teil 3) | ✅ Prüfer-Gespräch im Dialog |
| S13 | Online einkaufen ist praktisch | — | ✅ | ✅ | ✅ | ✅ | ✅ 44 | Anna (Teil 2), Peter (Teil 3) | ✅ Prüfer-Gespräch im Dialog |
| S14 | Ich kaufe lieber im Laden | — | ✅ | ✅ | ✅ | ✅ | ✅ 36 | Anna (Teil 2), Peter (Teil 3) | ✅ Prüfer-Gespräch im Dialog |
| S15 | Wohnungsbesichtigung | — | ✅ | ✅ | ✅ | ✅ | ✅ 38 | Anna (Teil 2), Peter (Teil 3); Vermieter bleibt Vermieter | ✅ Prüfer-Gespräch im Dialog |

„—“ bedeutet bewusst nicht vorhanden (Teil 1 nur bis S06).

- [x] **5. Teil 1: voller Name und Aachen (S01–S06).** Satz mit vollem Namen (Naga Manoj Kumar Lakkoju, Nachname Lakkoju, Anrede Manoj), dazu fünf Sätze über Aachen (warum ich die Stadt mag, auf Deutsch mit englischer Übersetzung). Nachname in allen Geschichten auf Lakkoju geändert.

- [x] **6. Teil 1 in Reihenfolge (S01–S06).** Gruß und voller Name, Herkunft, Alter (30) und Geburtsjahr (1996), Wohnort Aachen mit fünf Sätzen, Familie, Beruf, Hobby, Sprachen, fünf Fragen und Antworten (was gefällt / gefällt nicht in Aachen und Deutschland, was man aus Indien vermisst), Abschluss mit Frage an den Partner. Die Geschichte steht danach im Abschnitt „Einstieg · Die Geschichte“.

- [x] **7. Zusatzfragen zur Vorstellung (S01–S06).** Pro Geschichte drei eigene Fragen mit Antwort, passend zum Thema: eine positive, eine negative und eine neutrale Frage (z. B. Bürgeramt: was war einfach / was war schwierig; Supermarkt: was ärgert Sie). Stehen vor dem Abschluss.

## Stand S16–S78 (Sprechen und Schreiben ergänzt)

Diese Geschichten hatten vorher keine Sprechen- oder Schreiben-Abschnitte. Jede bekommt jetzt:
- Sprechen Teil 2 (Manoj-Vortrag, Anna stellt eine Frage, Manoj antwortet)
- Sprechen Teil 3 (Dialog mit Peter), außer S24 und S75–S78, die schon einen Dialog haben
- Prüfer-Gespräch (eine Frage und Antwort)
- Schreiben-Aufgabe mit den vier Punkten
- Partner/Prüfer-Tabelle (er / sie / Sie), Schreiben-Checkliste, drei Selbstcheck-Fragen
- Doppelte Unterstreichung für Prüfungsphrasen

- [x] S16–S25, S26–S35, S36–S45, S46–S55, S56–S65, S66–S78 umgesetzt und im Browser geprüft (alle 78 Seiten ohne Fehler).
- [x] Tom ist überall Peter (Teil 3) bzw. Anna (Teil 2). In den Schreiben-Aufgaben heißt der Freund jetzt Felix.
- [ ] Die Schreiben-Aufgaben und Sprechen-Texte sind von mir geschrieben. Bitte mit einer offiziellen telc-Musteraufgabe und mit Ihrem Lehrer vergleichen.
- [ ] S16–S74 haben keinen Teil 1 (Vorstellung), nur S01–S06.

## Stand: Sprechen-Perspektiven (S01–S78)

- [x] Alle 78 Geschichten: jede Manoj-Zeile in den Sprechen-Teilen hat drei Fassungen (Peter du, Anna du, Prüfer Sie) und eine Frage von Peter, Anna und dem Prüfer.
- [x] Fragen, die Manoj selbst an Anna stellt, brauchen keine Antwortzeile.
- [x] Wortschatz-Sätze für S07–S78 eingefügt (je Geschichte ca. 4–12 Sätze mit „Neue Wörter in Sätzen“ und Einträgen in „Wörter in dieser Geschichte“).
- [ ] Restliche Wortschatz-Wörter ohne Platz in einer Geschichte: rund 1.169 (Stichwort-Prüfung, grob). Diese bleiben in der Wortschatz-Liste und können später in Extra-Sätzen ergänzt werden.
- [ ] Offizielle telc-B1-Prüfung: Struktur und Schreiben-Wortzahl mit einer Musterprüfung abgleichen (telc.net war vom Sitz aus nicht erreichbar).

## Frühere Änderungen (Git-Verlauf)

| Commit | Was |
|---|---|
| `c16e7bf` | Prüfungsphrasen in S01–S15 mit `==…==` markiert; eigene Farbe (doppelte Unterstreichung, bernstein) und Legendeneintrag |
| `08b292d` | Fortschrittsbalken: TOT und COV werden aus den Daten berechnet, nicht fest eingetragen |
| `5a8226e` | Partner/Prüfer-Tabellen, Schreiben-Checkliste und Selbstcheck für S01–S15 |
| (dieser Commit) | Teil-3-Redemittel „Ich schlage vor …“ ergänzt; diese Checkliste |

Hinweis zu den Spalten:
- **Partner im Dialog:** Tom ist in allen Geschichten der Partner für Teil 3. Die zweite Person (Anna, Lena, Julia …) ist in jeder Geschichte anders. In der Tabelle sind dagegen immer Peter und Anna.
- **Prüfer im Dialog:** Die Dialoge in den Geschichten enthalten keine Prüferrolle. Die Prüfersätze stehen nur in der Tabelle.
- **Doppelte Unterstreichung:** Anzahl der markierten Prüfungsphrasen in der Geschichte.

## Noch offen (bitte prüfen)

- [x] Partnernamen in den Dialogen: Teil 2 ist Anna, Teil 3 ist Peter (in allen 15 Geschichten).
- [x] Beispielnamen: „Kollege Peter“ in S03 und S05 ist jetzt „Kollege Markus“. Der Vermieter in S15 heißt im Dialog jetzt Herr Hoffmann, wie im Schreiben.
- [x] Prüfersätze in den Dialogen: jede Geschichte hat ein Prüfer-Gespräch mit zwei Fragen und Antworten (vor dem Schreiben-Abschnitt).
- [x] Gleiche Zeile in drei Fassungen (Partner er, Partnerin sie, Prüfer Sie): zwei Zeilen pro Geschichte (Teil 2 und Teil 3) in der Tabelle.

- [ ] Die Schreiben-Checklisten mit einer offiziellen telc-Musteraufgabe vergleichen (die Wortzahl und die Anzahl der Punkte konnte ich nicht sicher bestätigen).
- [ ] Du oder Sie mit dem Partner: mit dem Lehrer klären, welche Form in der Prüfung üblich ist.
- [ ] S14: Die Beschwerde-Checkliste ist allgemein gehalten; die Aufgabe selbst noch einmal lesen.
