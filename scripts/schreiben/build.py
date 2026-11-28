# -*- coding: utf-8 -*-
"""Builds docs/Schreiben/index.html. Run: python scripts/schreiben/build.py"""
import os, sys, re, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import STRUCT, GRAM, CSS as CSS0
from data2 import FORMAL_EMAILS, INFORMAL_EMAILS
from data3 import UNI, BANKS, SKEL
from extras import X
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'docs', 'Schreiben')
os.makedirs(OUT, exist_ok=True)
e = html.escape
def mk(s):
    s = e(s, quote=False)
    s = re.sub(r'\{\{(.+?)\}\}', r'<u class="re">\1</u>', s)
    return re.sub(r'\[\[(.+?)\]\]', r'<span class="gap">\1</span>', s)
def plain(s): return re.sub(r'\{\{|\}\}', '', s)
PAIR = {'f-ofen': 'i-ofen', 'i-ofen': 'f-ofen', 'f-termin': 'i-absage', 'i-absage': 'f-termin'}

def email(L):
    body = [list(p) for p in L['body']]
    for i, d, en in X.get(L['id'], []):
        body[i][0] += d; body[i][1] += en
    words = len(plain(' '.join(p[0] for p in body)).split())
    formal = L['id'].startswith('f-')
    paras = ''.join('<p class="de">%s</p><p class="en">%s</p>' % (mk(d), e(n)) for d, n in body)
    pts = ''.join('<li>%s</li>' % e(p) for p in L['pts'])
    pair = ''
    if L['id'] in PAIR:
        pair = '<p class="pair">Same topic in the other register: <a href="#%s">open it</a> and compare Sie / du, greeting and tone.</p>' % PAIR[L['id']]
    return '''<details class="lt" id="%(id)s"><summary><b>%(t)s</b><small>%(te)s</small><span class="wc">%(w)d Wörter</span></summary>
<div class="in"><div class="task"><b>Aufgabe</b> <small>(%(story)s)</small><p>%(task)s</p><p class="tl">Schreiben Sie etwas zu folgenden Punkten:</p><ol>%(pts)s</ol></div>
<div class="mail"><p class="meta de">Köln, den 28.11.2026<br>%(bet)s</p><p class="meta en">Cologne, 28 Nov 2026<br>%(bete)s</p>
<p class="de sal">%(anr)s</p><p class="en">%(anre)s</p>%(paras)s<p class="de sal">%(g)s</p><p class="en">%(ge)s</p><p class="de sal">%(n)s</p></div>%(pair)s</div></details>''' % dict(
        id=L['id'], t=e(L['t']), te=e(L['te']), w=words, story=e(L['story']), task=e(L['task']), pts=pts, bet=e(L['bet']), bete=e(L['bete']),
        anr=e(L['anr']), anre=e(L['anre']), paras=paras, g=e(L['gruss']), ge=e(L['gruse']), n=e(L['name']), pair=pair)

def uni(reg):
    U = UNI[reg]
    rows = ''.join('<div class="tl2"><p class="de">%s</p><p class="en">%s</p></div>' % (mk(d), e(n)) for d, n in U['lines'])
    return '<div class="uni"><h3>%s <small>%s</small></h3><p class="en">%s</p>%s</div>' % (e(U['t']), e(U['te']), e(U['note']), rows)

def banks(reg):
    out = ''
    for t, te, items in BANKS[reg]:
        li = ''.join('<li><span class="de">%s</span><span class="en">%s</span></li>' % (mk(d), e(n)) for d, n in items)
        out += '<details class="bk"><summary><b>%s</b><small>%s</small></summary><ul class="bl">%s</ul></details>' % (e(t), e(te), li)
    return out

def skels(reg):
    out = ''
    for t, te, flow, lines in SKEL[reg]:
        li = ''.join('<li class="de">%s</li>' % mk(x) for x in lines)
        out += '<div class="card"><h3>%s</h3><p class="en">%s</p><p class="flow">%s</p><ol>%s</ol></div>' % (e(t), e(te), e(flow), li)
    return '<div class="grid">%s</div>' % out

def group(reg, emails, ident, title, sub, note):
    return '''<section id="%s" class="grp %s"><h2>%s <small>%s</small></h2><p class="en note">%s</p>
<h3 class="sh">1 · Universal-Vorlage mit Lücken</h3>%s
<h3 class="sh">2 · Bausteine zum Wiederverwenden</h3><p class="en">Tap a group to open lines you can copy into any email.</p>%s
<h3 class="sh">3 · Gerüste für verschiedene Themen</h3>%s
<h3 class="sh">4 · Beispiel-E-Mails (ca. 160–180 Wörter)</h3><p class="en">Each email is built from the lines above. Underlined parts are reusable phrases.</p>%s</section>''' % (
        ident, reg, title, sub, note, uni(reg), banks(reg), skels(reg), ''.join(email(x) for x in emails))


# ---------------------------------------------------------------- side-by-side comparison (Sie | du)
def col(items): return items
def sbs_row(label, a, b):
    return '<div class="sb-r"><div class="sb-l">%s</div><div class="sb-c f">%s</div><div class="sb-c i">%s</div></div>' % (label, a, b)
def lines_html(lines):
    return ''.join('<p class="de">%s</p><p class="en">%s</p>' % (mk(d), e(n)) for d, n in lines) if lines else '<p class="mut">—</p>'

BASICS = [
 ('Pronomen','Pronouns',[('Sie · Ihnen · Ihr(e) – always capital','you (formal): always capitalised')],[('du · dir · dich · dein(e) – lowercase','you (informal): lowercase')]),
 ('Ton','Tone',[('Sachlich, höflich, vollständige Sätze','Factual, polite, full sentences')],[('Warm, persönlich, aber alle Punkte nennen','Warm, personal, but still cover every point')]),
 ('1 Betreff','Subject line',[('Betreff: Beschwerde über die Heizung','Complaint about the heating'),('Betreff: Anfrage zu Ihrem Angebot','Inquiry about your offer'),('Betreff: Bewerbung als Verkäufer','Application as sales assistant'),('Betreff: Terminverschiebung am 12. März','Rescheduling on 12 March')],[('Einladung zu meiner Geburtstagsfeier','Invitation to my birthday party'),('Absage für Samstag','Cancelling Saturday'),('Danke für das Geschenk!','Thanks for the gift!'),('Entschuldigung wegen gestern','Sorry about yesterday')]),
 ('2 Anrede','Greeting',[('Sehr geehrte Damen und Herren,','Dear Sir or Madam (name unknown)'),('Sehr geehrter Herr Berger,','Dear Mr Berger'),('Sehr geehrte Frau Schmidt,','Dear Ms Schmidt')],[('Liebe Anna,','Dear Anna (female friend)'),('Lieber Jonas,','Dear Jonas (male friend)'),('Hallo Anna,','Hi Anna'),('Liebe Anna, lieber Jonas,','Dear Anna and Jonas')]),
 ('3 Einleitung','Opening',[('Ich schreibe Ihnen, weil …','I am writing to you because …'),('Bezug nehmend auf Ihre Anzeige möchte ich …','With reference to your ad, I would like to …'),('Hiermit möchte ich mich über … beschweren.','I hereby want to complain about …'),('Ich wende mich an Sie wegen …','I am contacting you regarding …')],[('Danke für deine Nachricht!','Thanks for your message!'),('Ich hoffe, es geht dir gut.','I hope you are well.'),('Wie geht es dir? Ich habe tolle Neuigkeiten!','How are you? I have great news!'),('Ich schreibe dir, weil …','I am writing to you because …')]),
 ('4 Problem','Problem / topic',[('Leider funktioniert … nicht mehr.','Unfortunately … no longer works.'),('Seit drei Tagen ist … defekt.','… has been broken for three days.'),('Leider muss ich Ihnen mitteilen, dass …','Unfortunately I must tell you that …'),('Ich bin mit … nicht zufrieden.','I am not satisfied with …')],[('Leider ist … kaputt.','Unfortunately … is broken.'),('Stell dir vor, …','Imagine, …'),('Leider kann ich am Samstag nicht kommen.','I cannot come on Saturday.'),('Es tut mir leid, dass …','I am sorry that …')]),
 ('5 Grund','Reason',[('Der Grund dafür ist, dass …','The reason is that …'),('Aus diesem Grund …','For this reason …'),('Da … , bitte ich Sie …','Since …, I ask you …'),('Dadurch kann ich … nicht','Because of this I cannot …')],[('Das liegt daran, dass …','That is because …'),('Deshalb …','That is why …'),('Weil … , kann ich leider nicht …','Because …, I unfortunately cannot …'),('Ich bin nämlich krank / habe Arbeit.','You see, I am ill / have work.')]),
 ('6 Frage','Question',[('Ich möchte gerne wissen, ob …','I would like to know whether …'),('Mich würde interessieren, wann …','I would be interested to know when …'),('Könnten Sie mir mitteilen, wie …?','Could you tell me how …?')],[('Weißt du, ob …?','Do you know whether …?'),('Hast du Lust, … ?','Do you feel like …?'),('Kannst du mir sagen, wann …?','Can you tell me when …?')]),
 ('7 Bitte','Request',[('Könnten Sie bitte … ?','Could you please …?'),('Ich möchte Sie bitten, … zu …','I would like to ask you to …'),('Ich bitte Sie, bis … zu …','I ask you to … by …'),('Wäre es möglich, dass Sie …?','Would it be possible for you to …?')],[('Kannst du bitte … ?','Can you please …?'),('Könntest du … ? Das wäre toll.','Could you …? That would be great.'),('Ich wollte dich bitten, … zu …','I wanted to ask you to …'),('Hilfst du mir bitte?','Will you help me?')]),
 ('8 Imperativ','Imperative / call to act',[('Bitte geben Sie mir Bescheid.','Please let me know.'),('Bitte bestätigen Sie den Termin.','Please confirm the appointment.'),('Bitte rufen Sie mich zurück.','Please call me back.')],[('Gib mir bitte Bescheid.','Let me know please.'),('Schreib mir kurz zurück.','Write back briefly.'),('Ruf mich an!','Call me!')]),
 ('9 Dank','Thanks',[('Vielen Dank im Voraus für Ihre Hilfe.','Many thanks in advance for your help.'),('Ich danke Ihnen für Ihre Mühe.','Thank you for your effort.'),('Besten Dank für Ihr Verständnis.','Thanks for your understanding.')],[('Vielen Dank für deine Hilfe!','Thanks a lot for your help!'),('Danke dir!','Thank you!'),('Das ist wirklich lieb von dir.','That is really kind of you.')]),
 ('10 Schluss','Closing sentence',[('Ich hoffe auf eine baldige Antwort.','I hope for a quick reply.'),('Ich freue mich auf Ihre Rückmeldung.','I look forward to your reply.'),('Für Rückfragen stehe ich Ihnen gern zur Verfügung.','I am happy to answer questions.'),('Falls nötig, erreichen Sie mich unter …','If needed, you can reach me at …')],[('Ich freue mich auf deine Antwort!','Looking forward to your reply!'),('Ich freue mich schon sehr auf dich!','I am really looking forward to seeing you!'),('Melde dich einfach, wenn du Fragen hast.','Just get in touch if you have questions.'),('Bis bald!','See you soon!')]),
 ('11 Gruß','Sign-off',[('Mit freundlichen Grüßen','Kind regards'),('Mit besten Grüßen','Best regards'),('Hochachtungsvoll (very formal)','Yours faithfully')],[('Viele Grüße','Many greetings'),('Liebe Grüße','Love / kind greetings'),('Herzliche Grüße','Warm regards'),('Bis bald, dein Manoj','See you soon, yours Manoj')]),
 ('12 Name','Name',[('Max Mustermann (full name)','')],[('Manoj (first name only)','')]),
]
def basics():
    return ''.join(sbs_row('<b>%s</b><span class="en">%s</span>' % (e(l), e(en)), lines_html(f), lines_html(i)) for l, en, f, i in BASICS)

# template pairing by function: (label, [formal line idx], [informal line idx])
TP = [('Datum', [0], [0]), ('Betreff / Anrede', [1, 2], [1]), ('Einleitung / Einstieg', [3], [2, 3]), ('Situation / Details', [4, 5], [4]),
      ('Weitere Punkte', [6], [5]), ('Bitte / Vorschlag', [7], [6, 7]), ('Frist', [8], []), ('Schluss', [9], [8]), ('Gruß', [10], [9]), ('Name', [11], [10])]
ALT = {
 'Datum': ([('Aachen, [[Datum]]','City, date'),('[[Datum]] (right-aligned, top)','Date only, top right'),('[[Ort]], den [[Datum]]','Place, date')],
           [('(Datum weglassen oder: [[Datum]])','Date can be left out'),('Samstag, [[Datum]]','Saturday, date'),('[[Ort]], [[Datum]]','Place, date')]),
 'Betreff / Anrede': ([('Betreff: {{Anfrage zu}} [[Thema]]','Subject: inquiry about …'),('Betreff: {{Beschwerde über}} [[Thema]]','Subject: complaint about …'),('Betreff: {{Ihre Anzeige vom}} [[Datum]]','Subject: your ad of …'),('Sehr geehrte Frau Dr. [[Name]],','Dear Dr … (with title)')],
           [('Hallo [[Name]],','Hi …'),('Liebe [[Name]], lieber [[Name]],','Dear … and …'),('Hallo ihr Lieben,','Hi you two / all'),('Hi [[Name]],','Hi (very casual)')]),
 'Einleitung / Einstieg': ([('{{Bezug nehmend auf}} [[Anzeige / Gespräch]], {{möchte ich}} [[Wunsch]].','Referring to …, I would like to …'),('{{Ich wende mich an Sie, weil}} [[Grund, Verb am Ende]].','I am contacting you because …'),('{{Hiermit möchte ich mich über}} [[Thema]] {{beschweren.}}','I hereby want to complain about …'),('{{Ich interessiere mich für}} [[Angebot]].','I am interested in …')],
           [('{{Danke für deine Mail!}} {{Ich habe mich sehr darüber gefreut.}}','Thanks for your mail, it made me happy'),('{{Ich hoffe, dir geht es gut!}} {{Bei mir ist viel los.}}','Hope you are fine, I am busy'),('{{Ich muss dir etwas erzählen:}} [[Neuigkeit]].','I have to tell you something'),('{{Ich schreibe dir, weil ich}} [[Wunsch]] {{möchte.}}','I write because I want …')]),
 'Situation / Details': ([('{{Seit}} [[Datum]] {{funktioniert}} [[Gerät]] {{nicht mehr.}}','Since …, … no longer works'),('{{Leider muss ich Ihnen mitteilen, dass}} [[Problem, Verb am Ende]].','Unfortunately I must tell you that …'),('{{Ich habe am}} [[Datum]] [[etwas]] {{gekauft, aber}} [[Problem]].','I bought … on …, but …'),('{{Der Grund dafür ist, dass}} [[Grund, Verb am Ende]].','The reason is that …')],
           [('{{Es findet am}} [[Datum]] {{um}} [[Uhrzeit]] {{in}} [[Ort]] {{statt.}}','It takes place on … at … in …'),('{{Ich war letzte Woche}} [[Ort]]. {{Es war}} [[Adjektiv]].','Last week I was … It was …'),('{{Stell dir vor:}} [[Neuigkeit]]!','Imagine: …'),('{{Das liegt daran, dass}} [[Grund, Verb am Ende]].','That is because …')]),
 'Weitere Punkte': ([('{{Außerdem möchte ich erwähnen, dass}} [[Punkt]].','Also I want to mention that …'),('{{Darüber hinaus}} [[Punkt]]. {{Aus diesem Grund}} [[Folge]].','Moreover … For this reason …'),('{{Ein weiteres Problem ist}} [[Problem]].','Another problem is …'),('{{Zusätzlich möchte ich wissen, ob}} [[Frage, Verb am Ende]].','In addition I want to know whether …')],
           [('{{Außerdem}} [[Punkt]]. {{Übrigens,}} [[Info]].','Also … By the way …'),('{{Leider kann ich nicht kommen, weil}} [[Grund, Verb am Ende]].','I cannot come, because …'),('{{Es tut mir wirklich leid, dass}} [[Verb am Ende]].','I am really sorry that …'),('{{Ich war so überrascht, dass}} [[Verb am Ende]].','I was so surprised that …')]),
 'Bitte / Vorschlag': ([('{{Könnten Sie bitte}} [[Bitte, Infinitiv am Ende]]?','Could you please …?'),('{{Ich bitte Sie, mir}} [[etwas]] {{zu schicken.}}','I ask you to send me …'),('{{Wäre es möglich, dass Sie}} [[Verb am Ende]]?','Would it be possible that you …'),('{{Ich erwarte, dass}} [[Forderung, Verb am Ende]].','I expect that …')],
           [('{{Hast du Lust, am}} [[Tag]] [[etwas]] {{zu machen?}}','Do you feel like … on …?'),('{{Wollen wir}} [[Vorschlag]]?','Shall we …?'),('{{Könntest du mir bitte helfen? Das wäre sehr nett.}}','Could you help me? Would be nice'),('{{Ich wollte dich fragen, ob du}} [[Verb am Ende]].','I wanted to ask whether you …')]),
 'Frist': ([('{{Bitte antworten Sie mir bis spätestens}} [[Datum]].','Reply by … at the latest'),('{{Ich bitte um eine Rückmeldung innerhalb von}} [[Zahl]] {{Tagen.}}','Reply within … days'),('{{Andernfalls werde ich}} [[Konsequenz]].','Otherwise I will …'),('{{Bitte bestätigen Sie den Termin schriftlich.}}','Please confirm in writing')],
           [('{{Sag mir bitte bis}} [[Tag]] {{Bescheid.}}','Let me know by …'),('{{Schreib mir kurz zurück, ob das klappt.}}','Write back if that works')]),
 'Schluss': ([('{{Ich freue mich auf Ihre Rückmeldung.}}','I look forward to your reply'),('{{Für Rückfragen stehe ich Ihnen gern zur Verfügung.}}','Happy to answer questions'),('{{Vielen Dank für Ihr Verständnis.}}','Thanks for understanding'),('{{Ich danke Ihnen für Ihre Mühe.}}','Thanks for your effort')],
           [('{{Ich freue mich schon sehr auf dich!}}','Looking forward to you!'),('{{Melde dich einfach, wenn du Fragen hast.}}','Contact me if questions'),('{{Danke für alles!}} {{Bis bald!}}','Thanks for everything, see you soon'),('{{Ich hoffe, wir sehen uns bald!}}','Hope we see each other soon')]),
 'Gruß': ([('Mit besten Grüßen','Best regards'),('Freundliche Grüße','Friendly regards'),('Hochachtungsvoll','Yours faithfully (very formal)')],
          [('Liebe Grüße','Love'),('Herzliche Grüße','Warm regards'),('Bis bald!','See you soon'),('Alles Gute!','All the best')]),
 'Name': ([('[[Vorname]] [[Nachname]]','Full name'),('[[Vorname Nachname]], [[Adresse]]','Name and address (for complaints)')],
          [('Dein [[Vorname]] / Deine [[Vorname]]','Yours (m / f)'),('[[Vorname]]','First name')]),
}
def tpl_side():
    F, I = UNI['formal']['lines'], UNI['informal']['lines']
    out = ''
    for lab, fi, ii in TP:
        af, ai = ALT.get(lab, ([], []))
        def col(base, alt):
            h = lines_html(base)
            if alt: h += '<p class="alt">Weitere Varianten</p>' + lines_html(alt)
            return h
        out += sbs_row('<b>%s</b>' % e(lab), col([F[i] for i in fi], af), col([I[i] for i in ii], ai))
    return out

# banks paired by function: (label, formal bank title or None, informal bank title or None)
BP = [('Anrede und Gruß', 'Anrede und Gruß', 'Anrede und Gruß'), ('Einleitung / Einstieg', 'Einleitung: Warum schreibe ich?', 'Einstieg'),
      ('Problem / Neuigkeit', 'Situation und Problem beschreiben', 'Auf Neuigkeiten reagieren'), ('Gründe / Absagen', 'Gründe nennen', 'Absagen und verschieben'),
      ('Bitten', 'Bitten und Forderungen', 'Bitten'), ('Fragen / Vorschläge', 'Fragen stellen', 'Vorschläge machen'), ('Frist / Einladen', 'Frist und Konsequenz', 'Einladen und zusagen'),
      ('Entschuldigen', None, 'Entschuldigen'), ('Danken', None, 'Danken'), ('Schluss', 'Schluss', 'Schluss')]
def bank_by_title(reg, title):
    if not title: return None
    for t, te, items in BANKS[reg]:
        if t == title: return items
def banks_side():
    out = ''
    for lab, ft, it in BP:
        a, b = bank_by_title('formal', ft), bank_by_title('informal', it)
        out += '<details class="bk"><summary><b>%s</b></summary><div class="sb-r"><div class="sb-c f">%s</div><div class="sb-c i">%s</div></div></details>' % (e(lab), lines_html(a), lines_html(b))
    return out

SKP = [(0, 1), (1, 2), (2, 3), (3, 0)]
def skel_side():
    out = ''
    # pair complaint/inquiry/application/appointment with invitation-decline/reply/request-apology-thanks by function
    pairs = [(0, 3, 'Problem / Bitte'), (1, 2, 'Anfrage / Antwort'), (2, 0, 'Antrag / Einladung'), (3, 1, 'Termin / Absage')]
    for fi, ii, lab in pairs:
        ft, fte, ffl, fl = SKEL['formal'][fi]; it, ite, ifl, il = SKEL['informal'][ii]
        a = '<p class="flow">%s</p><p class="en">%s</p><ol>%s</ol>' % (e(ft), e(ffl), ''.join('<li class="de">%s</li>' % mk(x) for x in fl))
        b = '<p class="flow">%s</p><p class="en">%s</p><ol>%s</ol>' % (e(it), e(ifl), ''.join('<li class="de">%s</li>' % mk(x) for x in il))
        out += sbs_row('<b>%s</b>' % e(lab), a, b)
    return out

EP = [('f-ofen', 'i-ofen', 'Der Ofen funktioniert nicht'), ('f-termin', 'i-absage', 'Absage / Termin verschieben'), ('f-anfrage', 'i-antwort', 'Anfrage / Antwort'),
      ('f-mantel', 'i-ausflug', 'Bitte / Vorschlag'), ('f-bewerbung', 'i-einladung', 'Bewerbung / Einladung'), ('f-kuendigung', 'i-dank', 'Kündigung / Dank'), ('f-beschwerde', 'i-entschuldigung', 'Beschwerde / Entschuldigung')]
ALLE = {x['id']: x for x in FORMAL_EMAILS + INFORMAL_EMAILS}
def mail_html(L):
    body = [list(p) for p in L['body']]
    for i, d, en in X.get(L['id'], []): body[i][0] += d; body[i][1] += en
    words = len(plain(' '.join(p[0] for p in body)).split())
    paras = ''.join('<p class="de">%s</p><p class="en">%s</p>' % (mk(d), e(n)) for d, n in body)
    return '<p class="flow">%s <small>(%d Wörter)</small></p><div class="mail"><p class="meta de">%s</p><p class="de sal">%s</p>%s<p class="de sal">%s<br>%s</p></div>' % (e(L['t']), words, e(L['bet']), e(L['anr']), paras, e(L['gruss']), e(L['name']))
def mails_side():
    out = ''
    for f, i, lab in EP:
        out += '<details class="lt sbm"><summary><b>%s</b><small>%s | %s</small></summary><div class="sb-r"><div class="sb-c f">%s</div><div class="sb-c i">%s</div></div></details>' % (e(lab), 'Sie', 'du', mail_html(ALLE[f]), mail_html(ALLE[i]))
    return out

SIDE = '''<section id="vergleich"><h2>Vergleich: Sie und du nebeneinander <small>Formal and informal side by side</small></h2>
<p class="en note">Everything from the two groups above, written again in two columns: left = formal (Sie), right = informal (du). Same function in each row, so you can see exactly what changes.</p>
<div class="sb-h"><div></div><div class="f">Formell (Sie)</div><div class="i">Informell (du)</div></div>
<h3 class="sh">1 · Die wichtigsten Unterschiede</h3>%s
<h3 class="sh">2 · Universal-Vorlage</h3>%s
<h3 class="sh">3 · Bausteine <small class="en">tap to open</small></h3>%s
<h3 class="sh">4 · Gerüste</h3>%s
<h3 class="sh">5 · Beispiel-E-Mails <small class="en">same or similar situations</small></h3>%s</section>''' % (basics(), tpl_side(), banks_side(), skel_side(), mails_side())
CSS_SB = '''
.alt{font:700 .72rem system-ui;color:#6b6b6b;margin:.7em 0 .1em;border-top:1px dashed #ccc;padding-top:.4em}
.sb-h{display:grid;grid-template-columns:76px minmax(0,1fr) minmax(0,1fr);gap:6px;position:sticky;top:46px;z-index:4;margin:8px 0 0}.sb-h div{font:800 .85rem system-ui;padding:6px 8px;border-radius:8px;text-align:center}
.sb-h .f{background:#d9e8f5;color:#12364f}.sb-h .i{background:#ffe6c7;color:#6b3a00}
.sb-r{display:grid;grid-template-columns:76px minmax(0,1fr) minmax(0,1fr);gap:6px;margin:6px 0}.sb-l{font-size:.78rem;word-break:break-word}.sb-l .en{display:block}
.sb-c{background:#fff;border:1px solid var(--line);border-radius:8px;padding:6px 8px;font-size:.9rem;overflow-wrap:anywhere}.sb-c.f{border-top:3px solid #1d4f7a}.sb-c.i{border-top:3px solid #c96a00}.sb-c p{margin:.25em 0}.sb-c ol{padding-left:1.1em;margin:.2em 0}
details.bk>.sb-r{grid-template-columns:minmax(0,1fr) minmax(0,1fr);padding:0 8px 8px}details.sbm>.sb-r{grid-template-columns:minmax(0,1fr) minmax(0,1fr);padding:8px}
.sb-c .mail{border:0;padding:0;background:none;margin:0}.sb-c .mail p{margin:.4em 0}.sb-c .de{font-size:.92rem}.mut{color:var(--mut)}
'''

LEG = '<div class="legend"><b>Legende</b> <u class="re">unterstrichen = wiederverwendbare Wendung</u> <span class="gap">gelb = Lücke zum Ausfüllen</span> <span class="en">grün = English</span></div>'
INTRO = '''<p class="en intro"><b>Which topics?</b> A mix of both. Two common situations are written in both registers (broken oven: Sie to the landlord and du to a friend; cancelling or postponing: Sie to an office and du to a friend), so you see exactly what changes: Sie/Ihnen vs du/dir, Sehr geehrte… vs Liebe…, Könnten Sie… vs Kannst du…. The rest are topics that really appear in the telc exam for each register: formal = complaint, inquiry, application, cancellation, return; informal = invitation, reply, apology, thanks, planning. They match the stories in Geschichten.</p>'''
CSS = CSS0 + CSS_SB + '''
.legend{background:#fff;border:1px solid var(--line);border-radius:10px;padding:8px 12px;margin:10px 0;font-size:.92rem;display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center}
u.re{text-decoration:underline;text-decoration-color:#1fa971;text-decoration-thickness:2px;text-underline-offset:3px;background:#1fa97118;border-radius:2px}
.gap{background:#ffe066;border:1px dashed #b38600;border-radius:4px;padding:0 4px;font-weight:600;color:#5c4500}
.grp{margin-top:34px;padding-top:6px}.grp.formal h2{border-color:#1d4f7a}.grp.informal h2{border-color:#c96a00}.sh{margin:20px 0 6px;font-size:1.08rem}
.uni{background:#fff;border:2px solid var(--ink);border-radius:12px;padding:12px 14px}.uni h3{margin:0}.uni h3 small{font-weight:600;color:var(--mut);font-size:.8rem}
.tl2{padding:5px 0;border-top:1px solid #eee}.tl2 p{margin:.1em 0}.tl2 .de{font-size:1.04rem}
details.bk{background:#fff;border:1px solid var(--line);border-radius:10px;margin:6px 0}details.bk>summary{cursor:pointer;padding:9px 12px;list-style:none;display:flex;flex-wrap:wrap;gap:8px;align-items:baseline}
details.bk>summary::-webkit-details-marker{display:none}details.bk>summary small{color:var(--mut)}ul.bl{list-style:none;margin:0;padding:2px 12px 10px}ul.bl li{padding:5px 0;border-top:1px solid #eee}ul.bl .de{display:block;font-size:1.02rem}
.flow{font-weight:700;color:var(--blue);font-size:.9rem;margin:.2em 0}.card ol{padding-left:1.2em;margin:.3em 0}.card ol li{margin:.35em 0}
.note,.intro{background:#fff;border-left:4px solid #1fa971;padding:8px 12px;border-radius:8px}.pair{font-size:.9rem;margin:10px 0 0}
details.lt summary .wc{margin-left:auto;color:var(--mut);font-size:.82rem}.mail .de{font-size:1.05rem}
.bar a.f{background:#d9e8f5}.bar a.i{background:#ffe6c7}
'''
page = '''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Schreiben-Vorlagen · telc B1</title><link rel="icon" type="image/png" href="../icon-192.png"><style>%(css)s</style></head><body>
<header><div class="wrap"><a href="../index.html">← Startseite</a><h1>Schreiben-Vorlagen</h1><p class="sub">telc B1 · Vorlagen, Bausteine und Beispiel-E-Mails, formell und informell, mit englischer Hilfe</p></div></header>
<div class="bar"><div class="wrap"><a href="#grundlagen">Grundlagen</a><a class="f" href="#formell">Formell (Sie)</a><a class="i" href="#informell">Informell (du)</a><a href="#grammatik">Grammatik</a><a href="#fehler">Fehler</a><a href="#vergleich">Sie | du</a><span class="sp"></span><button id="en" type="button">Englisch: an</button><button id="op" type="button">Alle öffnen</button></div></div>
<main>%(leg)s%(intro)s
<div id="grundlagen">%(struct)s</div>
%(formal)s
%(informal)s
%(gram)s
%(side)s
</main>
<script>
(function(){var b=document.body,en=document.getElementById('en'),op=document.getElementById('op');
try{if(localStorage.getItem('telc_schr_noen')==='1'){b.classList.add('noen');en.textContent='Englisch: aus'}}catch(e){}
en.onclick=function(){var off=b.classList.toggle('noen');en.textContent='Englisch: '+(off?'aus':'an');try{localStorage.setItem('telc_schr_noen',off?'1':'0')}catch(e){}};
var all=false;op.onclick=function(){all=!all;document.querySelectorAll('details.lt,details.bk').forEach(function(d){d.open=all});op.textContent=all?'Alle schließen':'Alle öffnen'};
function openHash(){var h=location.hash.slice(1);var d=h&&document.getElementById(h);if(d&&d.tagName==='DETAILS'){d.open=true;d.scrollIntoView()}}
addEventListener('hashchange',openHash);openHash()})();
</script></body></html>
''' % dict(css=CSS, leg=LEG, intro=INTRO, struct=STRUCT,
           formal=group('formal', FORMAL_EMAILS, 'formell', 'Formelle E-Mails und Briefe', 'Formal (Sie)', 'Use for authorities, companies, landlords, schools, employers. Always: Sie, Betreff, Sehr geehrte…, Mit freundlichen Grüßen.'),
           informal=group('informal', INFORMAL_EMAILS, 'informell', 'Informelle E-Mails', 'Informal (du)', 'Use for friends and family. Always: du, Liebe/Lieber…, Viele Grüße. Warm and personal, but still complete sentences and all four content points.'),
           gram=GRAM, side=SIDE)
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(page)
print('built', len(FORMAL_EMAILS), 'formal +', len(INFORMAL_EMAILS), 'informal emails,', len(page), 'bytes')
