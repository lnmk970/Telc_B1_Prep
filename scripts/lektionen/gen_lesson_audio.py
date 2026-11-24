#!/usr/bin/env python3
"""Create one MP3 per listen button (▶) of the extra lessons: docs/Lektionen/audio/<word>.mp3 (free German neural voice via edge-tts).
Run on your own computer (needs internet and: pip install edge-tts). Safe to re-run: existing files are skipped, --force rebuilds.
Usage (from the repo folder):  python scripts/lektionen/gen_lesson_audio.py [--force]
Then: git add docs/Lektionen/audio && git commit -m "Lesson audio" && git push origin main
The lesson pages fall back to the browser voice for any word without an MP3."""
import asyncio, glob, os, re, sys
import edge_tts

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'docs', 'Lektionen')
OUT = os.path.join(ROOT, 'audio')
VOICE, RATE = 'de-DE-KatjaNeural', '-15%'
FORCE = '--force' in sys.argv

def slug(t):  # must match slug() in lektion.js
    t = t.lower().replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
    return re.sub(r'^_|_$', '', re.sub(r'[^a-z0-9]+', '_', t))

async def one(text, path):
    for k in range(4):
        try:
            await edge_tts.Communicate(text, VOICE, rate=RATE).save(path)
            if os.path.getsize(path) > 500: return
        except Exception as e:
            err = e
            await asyncio.sleep(1.5 * (k + 1))
    raise RuntimeError('failed: %s (%s)' % (text, err))

async def main():
    words = sorted({w for f in glob.glob(os.path.join(ROOT, 'N*.html')) for w in re.findall(r'data-t="([^"]+)"', open(f, encoding='utf-8').read())})
    os.makedirs(OUT, exist_ok=True)
    made = 0
    for w in words:
        p = os.path.join(OUT, slug(w) + '.mp3')
        if os.path.exists(p) and not FORCE: continue
        print('making', w, flush=True)
        await one(w, p); made += 1
    print('done:', len(words), 'words,', made, 'files created')

asyncio.run(main())
