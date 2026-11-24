# TODO: telc B1 Prep

Status: 24.11.2026. This list was checked against the official telc **Übungstest 1 „telc Deutsch B1 / Zertifikat Deutsch“ (2020)**.

Details on each point: [REVIEW-und-60-Tage-Plan.md](REVIEW-und-60-Tage-Plan.md).

Goal: someone with A1 German and 60 days until the exam can pass telc B1 with this site.

---

## Open (by priority)

### High: affects exam points directly

- [ ] **Mock tests 1–7: Hören Teil 1 uses the wrong text type.**
  - Now: announcements, voicemail, traffic reports. That is the style of Teil 3.
  - Officially: five people give their opinion on **one** topic, heard once (global understanding).
  - To do for each mock test:
    - write 5 new opinion texts and 5 true/false statements,
    - update `audio.json`, `index.html` and the answer key,
    - then create new MP3s on your own computer: `python docs/gen_audio.py docs/Modelltests --only=mock-test-0X --force` (needs `edge-tts` and `ffmpeg`).
  - Claude can write the texts. The audio cannot be generated in the cloud environment (the speech server is not reachable there).
- [ ] **Day pages: check Hören Teil 1 too.** They probably also use announcements instead of opinions. Check, and plan the same fix as for the mock tests.
- [ ] **Speaking model audio (D66–D104).** Some recordings start with „Ich möchte über … sprechen“ and end with „Vielen Dank für Ihre Aufmerksamkeit“. That is presentation style. Better: „In meinem Text geht es um …“ and, at the end, a question to your partner. This needs new transcripts in `audio.json` and `answers.html`, plus new audio. For now there is a note in D57 and D85.

### Medium: content and learning quality

- [ ] **Read through with a German native speaker.** The automatic checks found hardly any errors. A full human proofread of all 105 days, 78 stories and 7 mock tests is still missing.
- [ ] **Densify stories S16–S78.** They have about 40 % of the grammar notes and marked words of S07–S15 (about 120 instead of 300 notes, about 930 instead of 2,200 words).
- [ ] About **1,169 vocabulary words** (`docs/Wortschatz/data.js`) do not appear in any story yet.
- [ ] **60-day plan: link stories to days.** Phase 1 currently has no list of which story goes with which day.
- [ ] **Audio for the extra lessons N1–N9.** N1 (pronunciation) uses the device's German voice. Real MP3s would be more reliable.

### Low: tidying up

- [ ] Delete the 26 log files `docs/_audio_*.log` (they are published but not needed).
- [ ] Folder names and texts of the day pages use the dates of the 105-day plan (e.g. „wie am 25. Februar“ in D102). In the 60-day plan the dates are calculated correctly; only the page texts still show the old date.
- [ ] Move the old checklist `CHECKLIST-Geschichten.md` into this TODO or archive it.

---

## Done

### Plan and structure

- [x] **Full repo review** with a guide for A1 → B1 in 60 days (`REVIEW-und-60-Tage-Plan.md`).
- [x] **60-day plan** on the start page (switch between 105 and 60 days). It contains all 105 day pages; nothing is dropped.
  - Days 1–30: learn
  - Days 31–45: review and improve
  - Days 46–60: only mock tests (11 mock tests, 2 error days, final days)
- [x] **README** rewritten with "Start here".

### New content

- [x] **9 extra lessons** (`docs/Lektionen`, 110 exercises, saved progress):
  - pronunciation,
  - imperative,
  - Präteritum of regular verbs,
  - Futur I,
  - um … zu / damit,
  - two-part connectors,
  - Konjunktiv II past,
  - passive Präteritum + lassen,
  - n-declension, indefinite pronouns, word formation.

### Exam facts (checked against the official Übungstest)

- [x] **Schreiben:** all tasks have **4 Leitpunkte** (67 tasks had 5).
- [x] **Schreiben:** one word recommendation, **about 100 words** (the official task names no word count).
- [x] **Hören guide:** Teil 1 = opinions, heard once. Teil 3 = announcements, weather, directions, heard twice. (It was the wrong way round before.)
- [x] **Sprechen Teil 2:** the Goethe-style "talk in five steps" was replaced on about 20 day pages by the telc format:
  1. report on your text,
  2. ask about your partner's text,
  3. give your opinion,
  4. tell your own experience,
  5. react.
- [x] **Sprechen points** confirmed: 15 / 30 / 30 (D78 was right).

### Stories (Geschichten)

- [x] **Sprechen Teil 2 rewritten in 17 stories** (S16, S19, S20, S22, S24, S30–S36, S38, S39, S40, S58, S66). Each has:
  - a real discussion question,
  - two contrasting opinion texts,
  - a model answer and a dialogue,
  - 34 new rows in the speaking table.
- [x] All 61 other Teil 2 tasks use the **official task text**.
- [x] **Grammar fixes:**
  - „Mir gefallen … die Thermen“
  - logical weil sentence in S01–S06
  - S32: Perfekt instead of Präteritum when speaking
- [x] **Exam labels:** DTZ and „Schreiben Teil 1“ removed; wrong section headings in S34, S36 and S38 fixed.
- [x] **Wrong automatic grammar notes fixed:**
  - 80 × „zu“,
  - 17 × „Sie“ meaning she/they,
  - 4 separable prefixes,
  - „ab und zu“,
  - 44 surnames with a dictionary tooltip.

  The rules in `scripts/expand/auto_rules.js` are also fixed.
- [x] Earlier work:
  - stories S16–S78 have the same structure as S07–S15,
  - exam phrases are highlighted,
  - three-version speaking table (Peter du / Anna du / examiner Sie),
  - story-specific questions in S01–S06.

### Checks

- [x] `scripts/check_geschichten.js`: all 78 stories pass.
- [x] Browser test: all 78 stories, 105 day pages, 105 answer pages, the start page and 9 lessons load without errors.

---

## Scripts for the changes

| Script | Purpose |
|--------|---------|
| `scripts/lektionen/build.py` | Builds the extra lessons from `content.py` |
| `scripts/fixes/exam_facts_2026-11-24.py` | 4 Leitpunkte, word count, Hören guide |
| `scripts/fixes/sprechen_teil2_2026-11-24.py` | Sprechen Teil 2 in telc format |
| `scripts/fixes/teil2_rewrite.js` + `teil2_content.js` | Teil 2 in the 17 stories, grammar-note fixes |
| `scripts/fixes/geschichten_fix_2026-11-24.js` | Grammar and label fixes in the stories |
| `scripts/check_geschichten.js` | Checks all stories |

All fix scripts can be run again safely: a second run changes nothing.
