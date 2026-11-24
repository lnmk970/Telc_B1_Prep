#!/usr/bin/env python3
"""Adds a fixed "Start" (home) button on the left edge of every page in docs/ (except the home page itself).
Safe to re-run: pages that already have the marker are skipped, so run it again after regenerating pages."""
import os, re, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'docs')
MARK = '<!--homebtn-->'
CSS = ('<style>#homebtn{position:fixed;left:6px;bottom:64px;z-index:2147483000;display:flex;align-items:center;gap:0;overflow:hidden;'
       'background:#ffd400;color:#14262b;text-decoration:none;font:700 15px/1 "Bahnschrift","Segoe UI",system-ui,sans-serif;'
       'height:40px;min-width:40px;padding:0 11px;border-radius:20px;box-shadow:0 2px 8px rgba(0,0,0,.35)}'
       '#homebtn span{max-width:0;overflow:hidden;white-space:nowrap;transition:max-width .2s,margin .2s}'
       '#homebtn:hover span,#homebtn:focus-visible span{max-width:80px;margin-left:7px}'
       '#homebtn:hover,#homebtn:focus-visible{background:#fff;outline:3px solid #14262b}#homebtn svg{width:18px;height:18px;flex:none}'
       '@media print{#homebtn{display:none}}</style>')
def block(rel):
    return (MARK + CSS + '<a id="homebtn" href="%s" target="_top" title="Zur Startseite" aria-label="Zur Startseite">'
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-8 9 8"/><path d="M5 10v10h5v-6h4v6h5V10"/></svg><span>Start</span></a>'
            '<script>if(window.self!==window.top){var h=document.getElementById("homebtn");if(h)h.remove()}</script>' % rel)
added = skipped = 0
for dp, dn, fn in os.walk(ROOT):
    for f in fn:
        if not f.endswith('.html'): continue
        p = os.path.join(dp, f)
        rel_dir = os.path.relpath(dp, ROOT)
        if rel_dir == '.' and f == 'index.html': continue
        s = open(p, encoding='utf-8').read()
        if MARK in s: skipped += 1; continue
        up = '' if rel_dir == '.' else '../' * (rel_dir.count(os.sep) + 1)
        i = s.rfind('</body>')
        if i < 0: print('no </body>:', p); continue
        open(p, 'w', encoding='utf-8').write(s[:i] + block(up + 'index.html') + s[i:])
        added += 1
print('added', added, 'skipped', skipped)
