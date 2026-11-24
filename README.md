# telc Deutsch B1: Prüfungsvorbereitung

A free website for the **telc Deutsch B1** exam (Zertifikat Deutsch). It covers every exam part every day:
- Lesen,
- Sprachbausteine,
- Hören,
- Schreiben,
- Sprechen.

All explanations are in German and English.

**Open the site:** https://lnmk970.github.io/Telc_B1_Prep/

## Hier anfangen / Start here

1. Open the site.
2. Enter your **exam date** (Prüfungsdatum) at the top.
3. Choose your plan:
   - **60-Tage-Plan (A1 → B1)**: for learners with basic German (A1) and about two months. All 105 day pages are packed into 60 days, and nothing is left out:

     | Days | Phase | What you do |
     |------|-------|-------------|
     | 1–30 | **Lernen** | All new grammar and vocabulary: two day pages per day, plus 9 extra lessons |
     | 31–45 | **Wiederholen und verbessern** | Weekly reviews, weekly tests, every exam part at full length |
     | 46–60 | **Probeprüfungen** | One full mock exam every day (11 mock exams), plus error days and the final review |

     Be honest with yourself: going from A1 to B1 in 60 days needs about **5–6 hours a day**, every day.
   - **105-Tage-Plan**: the same content at a calmer pace (about 2.5 hours a day).
4. Press **„Weiter mit …“** at the top. It always opens your next open task.

## Every day

- Do every part of the day page:
  - Lektion,
  - Wortschatz,
  - Übungen,
  - Lesen,
  - Sprachbausteine,
  - Hören,
  - Schreiben,
  - Sprechen.
- Check your work on the Lösungen page.
- 60 % in a part counts as passed. Aim for 75 %.
- Score your own writing (out of 45) and speaking (out of 75) on the day page. You can use the rating criteria in the guide.
- Also do these every day:
  - **10 minutes of pronunciation**: repeat the model audio sentence by sentence (see lesson N1).
  - **30 minutes of Geschichten**: read a story aloud and learn the words in the tooltips.
- Keep an **error notebook**. You will need it in phases 2 and 3.

## What is on the site

| Section | Contents |
|---------|----------|
| Tagesplan | 105 day pages with answer keys and audio (Hören, vocabulary, speaking model) |
| Zusatzlektionen | 9 extra lessons: pronunciation, imperative, simple past, future, um … zu / damit, two-part connectors, Konjunktiv II past, passive past and lassen, n-declension and word formation |
| Modelltests | 7 full model tests with timer and audio |
| Wortschatz | About 4,500 words with example sentences |
| Geschichten | 78 stories with grammar notes, exam phrases and speaking practice |
| Prüfungsleitfaden | Exam format, strategies, writing templates to learn by heart, speaking phrases |

Your progress is saved in your browser. To move it to another device, use the **Sync-Code** or the backup file on the start page. **„Alles offline speichern“** downloads everything (about 330 MB), so the site works without internet.

## Important

- Always follow the official instructions from telc and your test centre. Download the free official practice test (Übungstest) from telc.net and do it at least once.
- `REVIEW-und-60-Tage-Plan.md` lists known open points. Some exam details still need checking against the official telc practice test.

## For maintainers

- The site lives in [`docs`](docs): one folder per day, plus `Modelltests`, `Wortschatz`, `Geschichten` and `Lektionen`.
- `scripts/lektionen/build.py` rebuilds the extra lessons from `content.py`.
- `scripts/check_geschichten.js` checks the stories.
- `docs/gen_audio.py` creates the MP3 files. It needs `edge-tts` and `ffmpeg`.
