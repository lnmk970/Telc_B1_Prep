# -*- coding: utf-8 -*-
# Templates with blanks [[...]] and reusable phrases {{...}}; banks of lines. All (de, en) pairs.

UNI = {
'formal': dict(t='Universal-Vorlage Formell (Sie)', te='Universal fill-in template, formal',
 note='Works for complaints, inquiries, requests, applications. Replace every yellow blank; keep the underlined connecting phrases.',
 lines=[
 ('Köln, den [[Datum]]', 'City, date'),
 ('Betreff: [[Thema in 2–5 Wörtern]]', 'Subject: topic in 2–5 words'),
 ('Sehr geehrte Damen und Herren, / Sehr geehrter Herr [[Name]], / Sehr geehrte Frau [[Name]],', 'Dear Sir or Madam / Mr / Ms'),
 ('{{ich schreibe Ihnen, weil}} [[Grund, Verb am Ende]]. / {{ich möchte mich über}} [[Thema]] {{informieren / beschweren}}.', 'Introduction: why you write (verb at the end after weil).'),
 ('{{Ich habe am}} [[Datum]] [[etwas bestellt / gebucht / gelesen]]. [[Kurze Beschreibung der Situation]].', 'Situation: what happened, when.'),
 ('{{Das erste Problem ist, dass}} [[Problem 1, Verb am Ende]]. {{Das ist ein Problem für mich, weil}} [[Folge]].', 'First point and why it matters.'),
 ('{{Außerdem}} [[zweite Information]]. {{Darüber hinaus}} [[dritte Information]]. {{Deshalb}} [[Folge, Verb an Position 2]].', 'More points, connected with linking words.'),
 ('{{Ich möchte Sie bitten,}} [[Bitte]] {{zu}} [[Infinitiv]]. / {{Könnten Sie mir bitte mitteilen,}} {{ob / wann / wie}} [[Frage, Verb am Ende]]?', 'Your request or question.'),
 ('{{Bitte geben Sie mir bis zum}} [[Datum]] {{Bescheid.}}', 'Deadline / answer wanted by.'),
 ('{{Vielen Dank im Voraus für Ihre Hilfe.}} {{Ich hoffe auf eine baldige Antwort.}}', 'Thanks and closing sentence.'),
 ('Mit freundlichen Grüßen', 'Yours sincerely'),
 ('[[Vor- und Nachname]]', 'Your full name')]),
'informal': dict(t='Universal-Vorlage Informell (du)', te='Universal fill-in template, informal',
 note='Works for invitations, replies, apologies, thanks, plans. Replace every yellow blank; keep the underlined phrases.',
 lines=[
 ('[[Ort]], den [[Datum]] (optional)', 'City, date (optional)'),
 ('Liebe [[Name]], / Lieber [[Name]], / Hallo [[Name]],', 'Dear … / Hi …'),
 ('{{vielen Dank für deine Nachricht.}} / {{wie geht es dir?}} {{Ich hoffe, es geht dir gut.}}', 'Thanks for your message. / How are you? I hope you are well.'),
 ('{{Ich schreibe dir, weil}} [[Grund, Verb am Ende]]. / {{Ich habe mich sehr gefreut, dass}} [[Neuigkeit, Verb am Ende]].', 'Why you write / reaction to news.'),
 ('[[Information 1: wann, wo, was]]. {{Außerdem}} [[Information 2]].', 'Details, linked.'),
 ('{{Leider kann ich}} [[nicht + Verb]], {{denn}} [[Grund, normale Wortstellung]]. / {{Es tut mir leid, dass}} [[Verb am Ende]].', 'Unfortunately, because … / I am sorry that …'),
 ('{{Wie wäre es, wenn wir}} [[Vorschlag, Verb am Ende]]? / {{Ich schlage vor, dass}} [[Vorschlag, Verb am Ende]]. {{Hast du am}} [[Tag]] {{Zeit?}}', 'Suggestion and question.'),
 ('{{Kannst du}} [[Bitte]]? / {{Schreib mir bitte, ob}} [[Frage, Verb am Ende]].', 'Request.'),
 ('{{Ich freue mich auf deine Antwort!}} / {{Ich freue mich, wenn wir uns bald sehen!}}', 'Closing sentence.'),
 ('Viele Grüße / Liebe Grüße / Herzliche Grüße', 'Best wishes / Love / Warm regards'),
 ('[[Vorname]]', 'Your first name')]),
}

BANKS = {
'formal': [
 ('Anrede und Gruß', 'Greeting and sign-off', [
  ('{{Sehr geehrte Damen und Herren,}}', 'Dear Sir or Madam (name unknown)'), ('{{Sehr geehrter Herr Berger,}} / {{Sehr geehrte Frau Weber,}}', 'Dear Mr / Ms (name known)'),
  ('{{Mit freundlichen Grüßen}}', 'Yours sincerely / faithfully'), ('{{Freundliche Grüße}}', 'Kind regards (a bit shorter)')]),
 ('Einleitung: Warum schreibe ich?', 'Introduction: why do I write?', [
  ('{{Ich schreibe Ihnen, weil}} ich mit … nicht zufrieden bin.', 'I am writing because I am not satisfied with …'),
  ('{{Ich möchte mich über}} … {{informieren.}}', 'I would like to find out about …'),
  ('{{Ich möchte mich über}} … {{beschweren.}}', 'I would like to complain about …'),
  ('{{Hiermit möchte ich}} … {{kündigen / bestellen / anmelden.}}', 'I hereby want to cancel / order / register …'),
  ('{{Leider muss ich Ihnen mitteilen, dass}} …', 'Unfortunately I have to tell you that …'),
  ('{{Ich schreibe Ihnen wegen}} meines Termins am …', 'I am writing about my appointment on …'),
  ('{{Mit großem Interesse habe ich Ihre Anzeige gelesen.}}', 'I read your advert with great interest.')]),
 ('Situation und Problem beschreiben', 'Describing the situation and the problem', [
  ('{{Ich habe am}} 3. März {{bei Ihnen}} … {{bestellt / gebucht.}}', 'On 3 March I ordered / booked … with you.'),
  ('{{Das Problem ist, dass}} …', 'The problem is that …'), ('{{Leider entspricht}} … {{nicht meinen Erwartungen.}}', 'Unfortunately … does not meet my expectations.'),
  ('{{Außerdem funktioniert}} … {{nicht richtig.}}', 'Also … does not work properly.'), ('{{Das ist sehr ärgerlich, weil}} …', 'That is very annoying because …'),
  ('{{Seit}} gestern / drei Tagen / dem 5. Mai {{funktioniert}} … {{nicht mehr.}}', 'Since yesterday / three days / 5 May … has not worked.')]),
 ('Gründe nennen', 'Giving reasons', [
  ('{{Der Grund dafür ist, dass}} …', 'The reason for this is that …'), ('{{Aus diesem Grund}} …', 'For this reason …'), ('{{Deshalb}} / {{Deswegen}} … (Verb an Position 2)', 'That is why … (verb in 2nd position)'),
  ('{{Ich muss leider absagen, weil}} …', 'Unfortunately I have to cancel because …'), ('{{wegen}} + Genitiv: {{wegen des Problems}}', 'because of + genitive')]),
 ('Bitten und Forderungen', 'Requests and demands', [
  ('{{Ich möchte Sie bitten,}} … {{zu}} + Infinitiv.', 'I would like to ask you to …'), ('{{Ich bitte Sie um}} + Akk.: {{Ich bitte Sie um eine schnelle Antwort.}}', 'I ask you for a quick reply.'),
  ('{{Ich erwarte von Ihnen, dass}} …', 'I expect you to …'), ('{{Ich möchte mein Geld zurück / einen Ersatz / eine Entschädigung.}}', 'I want my money back / a replacement / compensation.'),
  ('{{Ich wäre Ihnen dankbar, wenn Sie}} … {{könnten.}}', 'I would be grateful if you could …'), ('{{Bitte bestätigen Sie mir}} … {{schriftlich.}}', 'Please confirm … in writing.')]),
 ('Fragen stellen', 'Asking questions', [
  ('{{Könnten Sie mir bitte mitteilen,}} wann / wie / ob / wo …?', 'Could you please tell me when / how / whether / where …?'), ('{{Ich möchte gerne wissen,}} ob / wie viel / wann …', 'I would like to know whether / how much / when …'),
  ('{{Mich würde interessieren,}} …', 'I would be interested to know …'), ('{{Muss ich}} … {{mitbringen?}}', 'Do I have to bring …?')]),
 ('Frist und Konsequenz', 'Deadline and consequence', [
  ('{{Bitte geben Sie mir bis zum}} 5. Dezember {{Bescheid.}}', 'Please let me know by 5 December.'), ('{{Wenn sich nichts ändert,}} möchte ich …', 'If nothing changes, I would like to …'),
  ('{{Andernfalls}} muss ich … (Verb an Position 2)', 'Otherwise I will have to …')]),
 ('Schluss', 'Closing', [
  ('{{Vielen Dank im Voraus für Ihre Hilfe.}}', 'Thank you in advance for your help.'), ('{{Ich hoffe auf eine baldige Antwort.}}', 'I hope for a quick reply.'),
  ('{{Ich freue mich auf Ihre Rückmeldung.}}', 'I look forward to your response.'), ('{{Für weitere Fragen stehe ich gerne zur Verfügung.}}', 'I am happy to answer any questions.'),
  ('{{Vielen Dank für Ihr Verständnis.}}', 'Thank you for your understanding.')]),
],
'informal': [
 ('Anrede und Gruß', 'Greeting and sign-off', [
  ('{{Liebe Anna,}} / {{Lieber Jonas,}}', 'Dear Anna / Dear Jonas'), ('{{Hallo Anna,}} / {{Hallo ihr Lieben,}}', 'Hi Anna / Hello dear all'),
  ('{{Viele Grüße}} / {{Liebe Grüße}} / {{Herzliche Grüße}}', 'Best wishes / Love / Warm regards'), ('{{Bis bald!}} / {{Bis Samstag!}}', 'See you soon! / See you on Saturday!')]),
 ('Einstieg', 'Opening', [
  ('{{Wie geht es dir?}} {{Ich hoffe, es geht dir gut.}}', 'How are you? I hope you are well.'), ('{{Vielen Dank für deine Nachricht / E-Mail / Einladung!}}', 'Thanks for your message / email / invitation!'),
  ('{{Ich schreibe dir, weil}} …', 'I am writing because …'), ('{{Ich habe mich sehr gefreut, dass}} …', 'I was very happy that …'),
  ('{{Ich habe eine Idee / eine kleine Bitte.}}', 'I have an idea / a small favour to ask.')]),
 ('Auf Neuigkeiten reagieren', 'Reacting to news', [
  ('{{Herzlichen Glückwunsch zu}} + Dativ: {{zur neuen Wohnung!}}', 'Congratulations on the new flat!'), ('{{Das ist ja toll / super / schön!}}', 'That is great / wonderful!'),
  ('{{Das tut mir leid.}} / {{Das ist schade.}}', 'I am sorry to hear that. / That is a pity.'), ('{{Ich bin schon sehr gespannt auf}} …', 'I am very curious about …')]),
 ('Einladen und zusagen', 'Inviting and accepting', [
  ('{{Ich möchte dich herzlich zu}} … {{einladen.}}', 'I would like to invite you warmly to …'), ('{{Die Feier findet am}} … {{um}} … {{Uhr statt.}}', 'The party takes place on … at …'),
  ('{{Es gibt}} … (Essen, Trinken, Musik)', 'There will be … (food, drinks, music)'), ('{{Natürlich komme ich gern.}}', 'Of course I will gladly come.'),
  ('{{Ich hoffe, dass du kommen kannst.}}', 'I hope you can come.')]),
 ('Absagen und verschieben', 'Declining and postponing', [
  ('{{Leider kann ich nicht kommen, denn}} + Hauptsatz.', 'Unfortunately I cannot come, because …'), ('{{Leider muss ich dir absagen.}}', 'Unfortunately I have to cancel.'),
  ('{{Der Grund ist, dass}} ich krank bin / arbeiten muss.', 'The reason is that I am ill / have to work.'), ('{{Wie wäre es, wenn wir}} … {{verschieben?}}', 'How about postponing …?'),
  ('{{Ich schlage vor, dass wir}} am Samstag … (Verb am Ende)', 'I suggest that we … on Saturday.'), ('{{Hast du am}} Sonntag {{Zeit?}}', 'Are you free on Sunday?')]),
 ('Vorschläge machen', 'Making suggestions', [
  ('{{Wir könnten}} …', 'We could …'), ('{{Was hältst du davon, wenn}} …?', 'What do you think about …?'), ('{{Wollen wir}} … {{?}}', 'Shall we …?'),
  ('{{Ich habe Lust auf}} …', 'I feel like …'), ('{{Bitte bring}} … {{mit.}}', 'Please bring …')]),
 ('Bitten', 'Asking for something', [
  ('{{Kannst du}} … {{?}} / {{Könntest du bitte}} …?', 'Can you …? / Could you please …?'), ('{{Ich habe eine kleine Bitte an dich.}}', 'I have a small favour to ask you.'),
  ('{{Schreib mir bitte kurz, ob}} …', 'Please write to me briefly whether …'), ('{{Bitte gib mir bis}} … {{Bescheid.}}', 'Please let me know by …')]),
 ('Entschuldigen', 'Apologising', [
  ('{{Es tut mir sehr leid, dass}} …', 'I am very sorry that …'), ('{{Ich möchte mich für}} … {{entschuldigen.}}', 'I would like to apologise for …'),
  ('{{Ich verspreche dir, dass das nicht wieder passiert.}}', 'I promise you it will not happen again.'), ('{{Kann ich etwas tun, um das wieder gutzumachen?}}', 'Can I do something to make up for it?'),
  ('{{Ich hoffe, dass du mir verzeihen kannst.}}', 'I hope you can forgive me.')]),
 ('Danken', 'Thanking', [
  ('{{Ich möchte mich ganz herzlich bei dir bedanken.}}', 'I would like to thank you very much.'), ('{{Ohne deine Hilfe wäre}} … {{nicht so schnell gegangen.}}', 'Without your help … would not have gone so fast.'),
  ('{{Das war wirklich sehr nett von dir.}}', 'That was really very kind of you.'), ('{{Als kleines Dankeschön möchte ich dich einladen.}}', 'As a small thank-you I would like to invite you.')]),
 ('Schluss', 'Closing', [
  ('{{Ich freue mich auf deine Antwort!}}', 'I look forward to your answer!'), ('{{Ich freue mich, wenn wir uns bald sehen!}}', 'I will be glad if we see each other soon!'),
  ('{{Schreib mir bitte, was du denkst.}}', 'Please write me what you think.'), ('{{Ich melde mich, sobald}} … (Verb am Ende)', 'I will get in touch as soon as …')]),
],
}

SKEL = {
'formal': [
 ('Gerüst A: Beschwerde / Reklamation', 'Skeleton A: complaint', 'Grund → Problem 1 → Problem 2 (+ Folge) → Erwartung → Frist + Konsequenz',
  ['{{Ich schreibe Ihnen, weil}} ich mit [[Produkt/Service]] nicht zufrieden bin.', '{{Das erste Problem ist, dass}} [[Problem 1]].', '{{Außerdem}} [[Problem 2]]. {{Deshalb}} [[Folge]].',
   '{{Ich erwarte von Ihnen, dass}} Sie [[Lösung]].', '{{Bitte geben Sie mir bis zum}} [[Datum]] {{Bescheid.}} {{Wenn sich nichts ändert,}} möchte ich [[Konsequenz]].']),
 ('Gerüst B: Anfrage', 'Skeleton B: inquiry', 'Interesse → Frage 1 → Frage 2 → Frage 3 → Dank',
  ['{{Ich möchte mich über}} [[Thema]] {{informieren.}} {{Ich interessiere mich für}} [[Angebot]], weil [[Grund]].', '{{Könnten Sie mir bitte mitteilen,}} wann / wie lange [[Frage 1]]?',
   '{{Mich würde auch interessieren,}} ob [[Frage 2]].', '{{Außerdem möchte ich gerne wissen,}} wie viel [[Frage 3]].', '{{Vielen Dank im Voraus für Ihre Informationen.}} {{Ich freue mich auf Ihre Antwort.}}']),
 ('Gerüst C: Bewerbung / Kündigung / Antrag', 'Skeleton C: application / cancellation / request', 'Hiermit → Grund → Details → Bitte um Bestätigung',
  ['{{Hiermit bewerbe ich mich um}} / {{Hiermit möchte ich}} [[Vertrag]] {{kündigen}}.', '{{Der Grund dafür ist, dass}} [[Grund]]. {{Ich habe}} [[Erfahrung/Dauer]].', '[[Datum / Details]]. {{Ich kann ab dem}} [[Datum]] {{anfangen.}}',
   '{{Bitte bestätigen Sie mir}} [[…]] {{schriftlich.}} / {{Über eine Einladung zu einem Gespräch würde ich mich freuen.}}', '{{Für weitere Fragen stehe ich gerne zur Verfügung.}}']),
 ('Gerüst D: Termin absagen / Bitte um Verschiebung', 'Skeleton D: cancel / postpone', 'Bezug → Grund → Vorschlag → Bitte um Bescheid',
  ['{{Ich schreibe Ihnen wegen}} meines Termins am [[Datum, Uhrzeit]]. {{Leider muss ich diesen Termin absagen.}}', '{{Der Grund ist, dass}} [[Grund]].',
   '{{Ich schlage vor,}} dass wir uns am [[Datum]] treffen. {{Falls das nicht möglich ist,}} kann ich auch am [[Datum]].', '{{Bitte geben Sie mir bis}} [[Tag]] {{Bescheid.}} {{Ich entschuldige mich für die Umstände.}}', '{{Vielen Dank für Ihr Verständnis.}}']),
],
'informal': [
 ('Gerüst A: Einladung', 'Skeleton A: invitation', 'Anlass → Wann/Wo → Essen/Programm → Bitte um Antwort',
  ['{{Wie geht es dir?}} {{Ich möchte dich herzlich zu}} [[Anlass]] {{einladen.}}', '{{Die Feier findet am}} [[Tag, Datum]] {{um}} [[Uhrzeit]] [[Ort]] {{statt.}} [[Wegbeschreibung]].',
   '{{Es gibt}} [[Essen/Trinken/Programm]]. Du kannst [[etwas]] mitbringen.', '{{Ich hoffe, dass du kommen kannst.}} {{Bitte gib mir bis zum}} [[Datum]] {{Bescheid.}}', '{{Ich freue mich auf deine Antwort!}}']),
 ('Gerüst B: Absage mit Gegenvorschlag', 'Skeleton B: declining with counter-proposal', 'Danke → Absage + Grund → Gegenvorschlag → Alternative',
  ['{{Vielen Dank für deine Einladung.}} Ich habe mich sehr gefreut, aber {{leider muss ich dir absagen.}}', '{{Der Grund ist, dass}} [[Grund]].',
   '{{Wie wäre es, wenn wir}} [[Plan]] {{verschieben?}} {{Ich schlage vor, dass wir}} am [[Tag]] [[Plan]].', 'Wenn dir [[Tag]] nicht passt, können wir auch am [[Tag]].', '{{Es tut mir wirklich leid.}} {{Schreib mir bitte, was du denkst.}}']),
 ('Gerüst C: Antwort auf eine Nachricht', 'Skeleton C: reply to news', 'Danke → Reaktion → Zusage + Uhrzeit → Frage',
  ['{{Vielen Dank für deine Nachricht!}} {{Ich habe mich sehr gefreut, dass}} [[Neuigkeit]].', '{{Herzlichen Glückwunsch!}} / {{Das ist ja toll!}}', '{{Natürlich komme ich gern.}} {{Leider kann ich nicht schon um}} [[Uhrzeit]] {{kommen, denn}} [[Grund]].',
   '{{Was soll ich mitbringen?}} {{Ich habe noch eine Frage:}} [[Frage]]?', '{{Ich freue mich auf deine Antwort!}}']),
 ('Gerüst D: Bitte / Entschuldigung / Dank', 'Skeleton D: request / apology / thanks', 'Anlass → Grund / Details → Wiedergutmachung oder Angebot → Schluss',
  ['{{Ich habe eine kleine Bitte an dich.}} / {{Es tut mir sehr leid, dass}} [[…]] / {{Ich möchte mich ganz herzlich bei dir bedanken.}}', '{{Der Grund ist, dass}} [[…]]. / Du hast [[Was hat die Person getan]].',
   '{{Könntest du vielleicht}} [[Bitte]]? / {{Ich verspreche dir, dass das nicht wieder passiert.}}', '{{Als kleines Dankeschön}} / {{Kann ich etwas tun, um das wieder gutzumachen?}} [[Angebot]]', '{{Schreib mir bitte kurz, ob das geht.}} / {{Ich hoffe, dass du mir verzeihen kannst.}}']),
],
}
