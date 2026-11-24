# TODO: telc B1 Prep

Status: 24.11.2026. This list was checked against the official telc **Übungstest 1 „telc Deutsch B1 / Zertifikat Deutsch“ (2020)**.

Details on each point: [REVIEW-und-60-Tage-Plan.md](REVIEW-und-60-Tage-Plan.md).

Goal: someone with A1 German and 60 days until the exam can pass telc B1 with this site.

---

## Open (by priority)

### High: affects exam points directly

- [ ] **Mock tests 1–7: record the new Hören Teil 1 audio (on your own computer).**
  - Done (24.11.): new texts, statements, answer keys, explanations and transcripts in the official format (moderator + five opinions, heard once), for all 7 mock tests. The audio script `audio.json` is updated too.
  - Still to do: the MP3s are the old ones until you rebuild them. Until then Teil 1 plays the old recording and does not match the statements.
  - Run in the repo folder (after `git pull`): `python docs/gen_audio.py docs/Modelltests --only=mock-test --force`, listen to each `hoeren.mp3`, then commit and push the MP3s.
- [ ] **Record the audio for the new day-page texts (on your own computer).** All texts are written and merged (24.11.). After `git pull`, run these two commands in the repo folder, listen to a few files, then commit and push the MP3s:
  ```
  python docs/gen_audio.py docs --only=D66_,D73_,D78_,D80_,D81_,D85_,D87_,D89_,D90_,D91_,D94_,D99_,D101,D102,D104 --files=sprechen_modell.mp3 --force
  python docs/gen_audio.py docs --only=D23_,D25_,D26_,D28_,D30_,D31_,D32_,D39_,D46_,D53_,D60_,D67_,D74_,D76_,D81_,D83_,D88_,D90_,D95_,D97_,D102 --files=hoeren.mp3 --force
  ```
  - First command: speaking model answers in the telc Teil 2 format (15 days).
  - Second command: new Hören Teil 1 (opinions) for 21 days (D23–D32 and D39–D102). It rebuilds the whole `hoeren.mp3` of each day, so Teil 2 and Teil 3 are re-recorded too (same texts).
  - The mock tests are done separately: `python docs/gen_audio.py docs/Modelltests --only=mock-test --force`.
  - Until the MP3s are rebuilt, these days play the old recordings, which no longer match the new texts.
- [x] **Early weeks D11–D32 checked (24.11.).** Ten days (D11, 12, 13, 15, 18, 19, 20, 22, 27, 29) already had opinion-style Teil 1 texts, and D14, D17, D21, D24 are correct Teil 3 practice (announcements, twice). Seven days (D23, 25, 26, 28, 30, 31, 32) mixed announcements into Teil 1: they now have short A2-level opinion texts with a moderator. Their audio is in the second command above.

### Medium: content and learning quality

- [ ] **Read through with a German native speaker.** The automatic checks found hardly any errors. A full human proofread of all 105 days, 78 stories and 7 mock tests is still missing.
- [ ] **Stories S16–S78 still have fewer hand-written grammar notes than S07–S15.** Done (24.11.): notes per story 115 → 170 (rule-based, separable verbs and participles added), vocabulary with tooltips and example sentences 2,387 → 4,458 of 4,478 words. S07–S15 have about 420 notes per story. The automatic rules are at their limit (two more rules were tested and dropped because they were wrong too often); more notes need hand-written explanations.
- [ ] **Record the audio for the extra lessons (on your own computer, optional).** The code is done: each ▶ button plays `docs/Lektionen/audio/<word>.mp3` and falls back to the browser voice if the file is missing (tested). To create the 52 files: `pip install edge-tts`, then `python scripts/lektionen/gen_lesson_audio.py`, then `git add docs/Lektionen/audio`, commit and push.

### Low: tidying up

- [ ] The day-page headers (`Datum Mo 16. Nov 2026 …`) show the dates of the 105-day plan. In the 60-day view the dates are calculated from your exam date; only the headers inside the day pages differ. The exam date itself (25 February 2027) is correct everywhere.

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
- [x] **Vocabulary complete (24.11.):** all 494 example sentences without an English translation are translated, and every distinct word of the 4,478-word list is now in a story (the stories page counts 4,458 because 20 entries share a word with another entry).
- [x] **Cleanup (24.11.):** the 26 leftover log files in `docs/` are deleted; the old story checklist moved to `scripts/CHECKLIST-Geschichten.md`.
- [x] **60-day plan: every one of the 78 stories is linked to a day** (dashed "Geschichte" fields; reading time 30 minutes a day).
- [x] **Mock tests: new Hören Teil 1 texts** (7 topics: commuting, holidays, health, learning, shopping, environment, work). Audio still to be recorded (see above).
- [x] **Speaking model answers rewritten (15 days)** in the telc Teil 2 format: opinion text A/B, model dialogue, table, answers page and audio script. Audio still to record (see above).
- [x] **New Hören Teil 1 on 14 day pages** (D39, D46, D53, D60, D67, D74, D76, D81, D83, D88, D90, D95, D97, D102): moderator + five opinions, with keys, explanations in German and English, and transcripts. Audio still to record.
- [x] `docs/gen_audio.py`: pure pause segments no longer call the speech service (tested with a stub voice).
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
| `scripts/fixes/mock_hoeren1_2026-11-24.py` + `mock_hoeren1_content.py` | New Hören Teil 1 in the 7 mock tests |
| `scripts/fixes/sprechen_models_*.py`, `sprechen_full_*.py` (+ `*_content.py`) | Speaking model answers in telc format |
| `scripts/fixes/hoeren1_days_*.py` (+ content) | New Hören Teil 1 on 14 day pages |
| `scripts/check_geschichten.js` | Checks all stories |

All fix scripts can be run again safely: a second run changes nothing.
