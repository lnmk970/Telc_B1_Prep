# -*- coding: utf-8 -*-
# {{...}} reusable phrase, [[...]] blank. Pairs are (de, en).

OVERVIEW = [
 ('Teil 1: Kontaktaufnahme', 'Part 1: getting to know each other', 'ca. 3 Min.', 'You introduce yourself and ask your partner questions (name, home, family, job, hobbies, German). Decide at the start: du or Sie, and keep it.'),
 ('Teil 2: Gespräch über ein Thema', 'Part 2: talking about a topic', 'ca. 6 Min.', 'You get a graphic or a short text. Summarise it in your own words, say your own experience and opinion, then ask your partner.'),
 ('Teil 3: Gemeinsam planen', 'Part 3: planning together', 'ca. 6 Min.', 'You plan an event with your partner (trip, party, gift). Discuss every point on the note, suggest, agree, doubt, and reach a decision together.'),
]

# ---------------------------------------------------------------- TEIL 1
T1_TEMPLATE = dict(t='Vorlage: Ich stelle mich vor', te='Template: introducing yourself', lines=[
 ('{{Hallo, ich heiße}} [[Vorname Nachname]]. {{Wollen wir du sagen?}}', 'Hello, my name is … Shall we use du?'),
 ('{{Ich komme aus}} [[Land / Stadt]], {{aber ich wohne seit}} [[Zeit]] {{in}} [[Stadt]].', 'I come from …, but I have lived in … for …'),
 ('{{Ich bin}} [[Beruf]] {{von Beruf und arbeite bei}} [[Firma]]. / {{Ich studiere}} [[Fach]].', 'I am a … by profession and work at … / I study …'),
 ('{{Ich bin}} [[verheiratet / ledig]] {{und habe}} [[Kinder / Geschwister]]. {{Meine Familie wohnt in}} [[Ort]].', 'I am married / single and have … My family lives in …'),
 ('{{In meiner Freizeit}} [[Verb, z. B. lese / koche / spiele]] {{ich gern, und}} [[Hobby 2]] {{macht mir auch Spaß.}}', 'In my free time I like … and … is fun too.'),
 ('{{Ich lerne Deutsch, weil}} [[Grund, Verb am Ende]]. {{Deshalb}} [[Folge, Verb an Position 2]].', 'I learn German because … Therefore …'),
 ('{{Und du? / Und Sie?}} {{Woher kommst du?}} {{Was machst du beruflich?}} {{Was machst du in deiner Freizeit?}}', 'And you? Where are you from? What do you do for a living? What do you do in your free time?')])

T1_BANK = [
 ('Fragen an den Partner', 'Questions for your partner', [
  ('{{Wie heißt du?}} / {{Wie heißen Sie?}}', 'What is your name?'), ('{{Woher kommst du?}} / {{Woher kommen Sie?}}', 'Where are you from?'),
  ('{{Wo wohnst du?}} {{Wohnst du schon lange dort?}}', 'Where do you live? Have you lived there long?'), ('{{Was machst du beruflich?}} / {{Was sind Sie von Beruf?}}', 'What is your job?'),
  ('{{Hast du Geschwister / Kinder?}}', 'Do you have siblings / children?'), ('{{Was machst du gern in deiner Freizeit?}}', 'What do you like to do in your free time?'),
  ('{{Warum lernst du Deutsch?}}', 'Why are you learning German?'), ('{{Wie lange lernst du schon Deutsch?}}', 'How long have you been learning German?'),
  ('{{Was gefällt dir an Deutschland?}}', 'What do you like about Germany?'), ('{{Wohin fährst du gern in den Urlaub?}}', 'Where do you like to go on holiday?')]),
 ('Auf Antworten reagieren', 'Reacting to answers', [
  ('{{Ach, wirklich? Das ist interessant!}}', 'Really? That is interesting!'), ('{{Das klingt gut / spannend.}}', 'That sounds good / exciting.'),
  ('{{Das kenne ich auch.}} / {{Bei mir ist das ähnlich / anders.}}', 'I know that too. / It is similar / different for me.'), ('{{Und wie lange machst du das schon?}}', 'And how long have you been doing that?'),
  ('{{Dann haben wir etwas gemeinsam.}}', 'Then we have something in common.')]),
 ('Länger antworten (Erweiterung)', 'Answering with more than one sentence', [
  ('{{Ich mache die Prüfung, weil ich sie für}} … {{brauche.}} {{Außerdem}} …', 'I take the exam because I need it for … Also …'),
  ('{{Ich wohne in}} … {{, weil}} … {{Das gefällt mir, denn}} …', 'I live in … because … I like it because …'),
  ('{{Mein Hobby ist}} … {{Ich mache das}} … {{mal pro Woche und}} … {{macht mir viel Spaß.}}', 'My hobby is … I do it … times a week and it is a lot of fun.'),
  ('{{Früher}} … {{, aber jetzt}} …', 'Earlier … but now …'), ('{{In Zukunft möchte ich}} …', 'In future I would like to …')]),
]
T1_DIALOG = dict(t='Beispielgespräch Teil 1', te='Sample conversation, part 1', lines=[
 ('A', 'Hallo, ich bin {{Manoj}}. Wollen wir du sagen?', 'Hello, I am Manoj. Shall we say du?'),
 ('B', 'Ja, gern. Ich heiße Lena. Woher kommst du, Manoj?', 'Yes, gladly. My name is Lena. Where do you come from, Manoj?'),
 ('A', '{{Ich komme aus}} Indien, aber ich wohne seit drei Jahren in Aachen. Ich arbeite als Softwareentwickler. Und du?', 'I come from India but I have lived in Aachen for three years. I work as a software developer. And you?'),
 ('B', 'Ich komme aus Köln und arbeite im Krankenhaus. Warum lernst du Deutsch?', 'I come from Cologne and work in a hospital. Why are you learning German?'),
 ('A', '{{Ich lerne Deutsch, weil}} ich hier lebe und im Alltag besser sprechen möchte. {{Außerdem}} brauche ich die Prüfung für meinen Beruf. Was machst du in deiner Freizeit?', 'I learn German because I live here and want to speak better in everyday life. I also need the exam for my job. What do you do in your free time?'),
 ('B', 'Ich laufe gern und gehe oft ins Kino. Und du?', 'I like running and often go to the cinema. And you?'),
 ('A', '{{Ach, das ist interessant!}} Ich koche gern und fahre am Wochenende Fahrrad. {{Bei mir ist das ähnlich}}, denn ich bin auch gern draußen.', 'Oh, that is interesting! I like cooking and cycling at the weekend. It is similar for me, because I am also outdoors a lot.')])
T1_TIPS = ['Say du/Sie once at the beginning (Wollen wir du sagen?) and never mix.', 'Answer AND ask back. Never answer with one word.', 'If the examiner asks “Warum machen Sie die Prüfung?” answer with weil + a second sentence with außerdem / deshalb.']

# ---------------------------------------------------------------- TEIL 2
T2_TEMPLATE = dict(t='Vorlage: Gespräch über ein Thema', te='Template: talking about a topic', lines=[
 ('{{Ich habe}} [[eine Grafik / einen Text]] {{zum Thema}} [[Thema]] {{bekommen.}}', 'I got a graphic / a text on the topic …'),
 ('{{In dem Text geht es um}} [[Thema]]. / {{Die Grafik zeigt}} [[was]].', 'The text is about … / The graphic shows …'),
 ('[[Person]] {{sagt, dass}} [[Aussage 1, Verb am Ende]]. {{Außerdem findet sie / er, dass}} [[Aussage 2]].', 'X says that … Also she/he thinks that …'),
 ('{{Aus der Grafik geht hervor, dass}} [[Zahl 1]] {{Prozent}} [[…]]. {{Interessant ist, dass}} [[Zahl 2]].', 'The graphic shows that …% … Interesting is that …'),
 ('{{Ich persönlich}} [[eigene Erfahrung]]. {{Bei uns in}} [[Land]] {{ist das ähnlich / anders, weil}} [[Grund]].', 'Personally I … In our country it is similar / different because …'),
 ('{{Ich finde es interessant / wichtig, dass}} [[Meinung, Verb am Ende]]. {{Meiner Meinung nach}} [[Meinung, Verb an Position 2]].', 'I find it interesting / important that … In my opinion …'),
 ('{{Wie ist das bei Ihnen / bei dir?}} {{Was meinen Sie / meinst du dazu?}}', 'How is that for you? What do you think about it?')])

T2_BANK = [
 ('Grafik beschreiben', 'Describing a graphic', [
  ('{{Die Grafik zeigt}} …', 'The graphic shows …'), ('{{Aus der Grafik geht hervor, dass}} …', 'The graphic shows that …'), ('{{Die Grafik gibt Informationen über}} …', 'The graphic gives information about …'),
  ('{{In dieser Grafik sehen wir}} …', 'In this graphic we see …'), ('{{Die meisten / Die wenigsten Menschen}} …', 'Most / the fewest people …'),
  ('{{Mehr als die Hälfte}} / {{Etwa ein Drittel}} / {{Nur ein Viertel}}', 'More than half / about a third / only a quarter'), ('{{Es sind … Prozent.}} / {{… Prozent der Befragten}} …', 'It is …% / …% of the people asked …')]),
 ('Text wiedergeben (indirekte Rede)', 'Summarising a text', [
  ('{{Ich habe einen Text zum Thema}} … {{bekommen.}}', 'I got a text on the topic …'), ('{{In dem Text geht es um}} …', 'The text is about …'),
  ('{{Sie / Er sagt / findet, dass}} … (Verb am Ende)', 'She/he says / thinks that …'), ('{{Sie / Er ist der Meinung, dass}} …', 'She/he is of the opinion that …'),
  ('{{Nach ihrer / seiner Meinung muss / sollte man}} …', 'In her/his opinion one must / should …'), ('{{Sie / Er fragt sich, ob / wann / wie / warum}} …', 'She/he wonders whether / when / how / why …'),
  ('{{Sie / Er weiß nicht, ob}} …', 'She/he does not know whether …'), ('{{Ihn / Sie interessiert, ob}} …', 'He/she is interested to know whether …')]),
 ('Eigene Erfahrung und Meinung', 'Own experience and opinion', [
  ('{{Ich persönlich}} … {{jeden Tag / oft / manchmal.}}', 'Personally I … every day / often / sometimes.'), ('{{Ich finde es interessant, dass}} …', 'I find it interesting that …'),
  ('{{Mich überrascht, dass}} …', 'I am surprised that …'), ('{{Ich denke aber, dass}} …', 'But I think that …'), ('{{Meiner Meinung nach}} …', 'In my opinion …'),
  ('{{Ich finde es (nicht) sehr wichtig, dass}} …', 'I find it (not) very important that …'), ('{{Bei uns ist es ähnlich / anders.}}', 'With us it is similar / different.'),
  ('{{Ein Vorteil ist, dass}} … {{Ein Nachteil ist, dass}} …', 'An advantage is that … A disadvantage is that …')]),
 ('Den Partner einbeziehen', 'Involving your partner', [
  ('{{Wie ist das bei Ihnen / bei dir?}}', 'How is it for you?'), ('{{Was meinen Sie / meinst du dazu?}}', 'What do you think about it?'), ('{{Haben Sie / Hast du auch schon}} … {{erlebt?}}', 'Have you also experienced …?'),
  ('{{Das sehe ich auch so.}} / {{Da bin ich anderer Meinung.}}', 'I see it that way too. / I disagree.'), ('{{Das stimmt. Aber}} …', 'That is true. But …'), ('{{Und was ist mit}} …{{?}}', 'And what about …?')]),
]

T2_SAMPLES = [
 dict(t='Deutschland surft: Internetnutzung', te='Germany surfs: internet use', kind='Grafik', note='Data from your reference sheet.',
  data='61 % der Internetnutzer sind fast jeden Tag online · 26 % mindestens einmal pro Woche · 13 % seltener · 10–24 Jahre: 64 % täglich · ab 55 Jahre: 53 % täglich',
  de='{{Die Grafik zeigt}} die Internetnutzung in Deutschland. {{Aus der Grafik geht hervor, dass}} 61 Prozent der Nutzer fast jeden Tag online sind. Bei den jungen Menschen zwischen 10 und 24 Jahren sind es sogar 64 Prozent. {{Interessant ist, dass}} auch bei den Menschen über 55 mehr als die Hälfte regelmäßig das Internet nutzt. {{Ich persönlich}} benutze das Internet jeden Tag, hauptsächlich für E-Mails und soziale Medien. {{Ich finde es wichtig, dass}} auch ältere Menschen Hilfe beim Lernen bekommen. {{Wie ist das bei Ihnen?}}',
  en='The graphic shows internet use in Germany. It shows that 61 percent of users are online almost every day. Among young people between 10 and 24 it is even 64 percent. Interesting is that more than half of the people over 55 also use the internet regularly. Personally I use the internet every day, mainly for email and social media. I find it important that older people also get help learning. How is it for you?'),
 dict(t='Fernsehen', te='Television', kind='Text', note='Text by Claudia Volke from your reference sheet.',
  data='„Ich mag Fernsehen. Am liebsten schaue ich mir Nachrichtensendungen und Dokumentationen an. … Was mich nicht interessiert, sind die vielen Shows, Gewinnspiele und die Werbung. … Das Fernsehen bietet heute eine große Programmauswahl.“',
  de='{{Ich habe einen Text von}} Claudia Volke {{zum Thema}} Fernsehen {{bekommen.}} {{Sie sagt, dass}} sie gern fernsieht. Am liebsten schaut sie Nachrichten und Dokumentationen. Filme mag sie auch, aber es gibt selten gute. Shows und Werbung interessieren sie nicht. {{Sie findet, dass}} das Fernsehen heute eine große Auswahl bietet. {{Ich persönlich}} schaue auch gern Dokumentationen, weil man dabei etwas lernt. {{Meiner Meinung nach}} sieht man heute weniger fern, denn viele Menschen schauen Filme im Internet. {{Wie ist das bei Ihnen?}}',
  en='I got a text by Claudia Volke on the topic of television. She says she likes watching TV. She likes watching news and documentaries best. She likes films too, but good ones are rare. Shows and ads do not interest her. She thinks TV offers a large selection today. Personally I also like watching documentaries because you learn something. In my opinion people watch less TV today because many watch films on the internet. How is it for you?'),
 dict(t='Einkäufe per Mausklick: Online-Shopping', te='Shopping at a mouse click', kind='Grafik', note='Practice data (invented) for this exercise.',
  data='Beispieldaten: 72 % kaufen mindestens einmal im Monat online · 18 % einmal im Jahr · 10 % nie · beliebt: Kleidung (64 %), Bücher (51 %), Elektronik (45 %)',
  de='{{Die Grafik gibt Informationen über}} das Online-Shopping. {{Aus der Grafik geht hervor, dass}} 72 Prozent der Befragten mindestens einmal im Monat im Internet einkaufen. Nur 10 Prozent kaufen nie online. Am beliebtesten sind Kleidung, Bücher und Elektronik. {{Mich überrascht, dass}} so viele Menschen Kleidung online bestellen, denn man kann sie nicht anprobieren. {{Ich persönlich}} bestelle Bücher und Technik im Internet, weil es bequem und oft günstiger ist. {{Ein Nachteil ist, dass}} man viel zurückschicken muss. {{Was meinen Sie dazu?}}',
  en='The graphic gives information about online shopping. It shows that 72 percent of people asked shop online at least once a month. Only 10 percent never buy online. Most popular are clothes, books and electronics. I am surprised that so many people order clothes online because you cannot try them on. Personally I order books and technology online because it is convenient and often cheaper. A disadvantage is that you have to send a lot back. What do you think about it?'),
 dict(t='Freizeitaktivitäten', te='Leisure activities', kind='Text', note='Practice text (invented).',
  data='Tim schreibt: „In meiner Freizeit treibe ich gern Sport, besonders Fußball. Aber am Wochenende bin ich oft müde und bleibe lieber zu Hause. Ich finde, man hat zu wenig Zeit für Hobbys.“',
  de='{{Ich habe einen Text von}} Tim {{zum Thema}} Freizeit {{bekommen.}} {{In dem Text geht es um}} seine Hobbys. {{Er sagt, dass}} er gern Sport treibt, besonders Fußball. Am Wochenende ist er aber oft müde und bleibt lieber zu Hause. {{Er findet, dass}} man zu wenig Zeit für Hobbys hat. {{Ich persönlich}} bin auch oft müde nach der Arbeit, aber ich gehe zweimal pro Woche laufen. {{Ich finde es wichtig, dass}} man sich bewegt, weil das gesund ist. {{Bei uns ist es ähnlich}}: Viele Leute arbeiten viel und haben wenig Freizeit. {{Und was machen Sie gern in Ihrer Freizeit?}}',
  en='I got a text by Tim on the topic of leisure. The text is about his hobbies. He says he likes doing sport, especially football. At weekends he is often tired and prefers to stay at home. He thinks people have too little time for hobbies. Personally I am often tired after work too, but I go running twice a week. I find it important to exercise because it is healthy. With us it is similar: many people work a lot and have little free time. And what do you like to do in your free time?'),
 dict(t='Gesundheit und Fitness', te='Health and fitness', kind='Text', note='Practice text (invented).',
  data='Dr. Weiß: „Viele Menschen sitzen den ganzen Tag. Man sollte jeden Tag mindestens 30 Minuten spazieren gehen und mehr Gemüse essen. Das ist nicht teuer und hilft sehr.“',
  de='{{In dem Text geht es um}} Gesundheit. {{Dr. Weiß ist der Meinung, dass}} viele Menschen den ganzen Tag sitzen. {{Nach ihrer Meinung sollte man}} jeden Tag mindestens 30 Minuten spazieren gehen und mehr Gemüse essen. Das ist nicht teuer und hilft sehr. {{Ich finde es interessant, dass}} schon so wenig Bewegung viel hilft. {{Ich persönlich}} sitze bei der Arbeit viel, deshalb gehe ich in der Mittagspause draußen spazieren. {{Ein Vorteil ist, dass}} ich danach besser arbeiten kann. {{Machen Sie auch etwas für Ihre Gesundheit?}}',
  en='The text is about health. Dr Weiß is of the opinion that many people sit all day. In her opinion one should walk at least 30 minutes every day and eat more vegetables. That is not expensive and helps a lot. I find it interesting that so little exercise already helps so much. Personally I sit a lot at work, so I walk outside at lunchtime. An advantage is that I can work better afterwards. Do you also do something for your health?'),
 dict(t='Umwelt: Müll und Recycling', te='Environment: waste and recycling', kind='Grafik', note='Practice data (invented).',
  data='Beispieldaten: 68 % trennen den Müll immer · 25 % manchmal · 7 % nie · 54 % nehmen eine eigene Tasche zum Einkaufen mit',
  de='{{Die Grafik zeigt}} das Umweltverhalten der Menschen. {{Aus der Grafik geht hervor, dass}} 68 Prozent immer ihren Müll trennen. 25 Prozent tun das manchmal, und nur 7 Prozent nie. Mehr als die Hälfte nimmt eine eigene Tasche zum Einkaufen mit. {{Mich überrascht, dass}} nicht noch mehr Menschen den Müll trennen, denn das ist einfach. {{Ich persönlich}} trenne den Müll jeden Tag und kaufe möglichst wenig Plastik. {{Meiner Meinung nach}} sollte man schon Kindern in der Schule zeigen, wie wichtig das ist. {{Wie ist das bei Ihnen?}}',
  en='The graphic shows people’s environmental behaviour. It shows that 68 percent always separate their waste. 25 percent do it sometimes and only 7 percent never. More than half take their own bag when shopping. I am surprised that not even more people separate waste because it is easy. Personally I separate waste every day and buy as little plastic as possible. In my opinion children should be shown at school how important that is. How is it for you?'),
]
T2_TIPS = ['Do not read the text aloud. Use your own words and indirect speech (Sie sagt, dass …; Sie findet, dass …).', 'Order: topic → 2–3 facts → your own experience → opinion → question to your partner.', 'Then keep talking: react to what your partner says and ask follow-up questions.']

# ---------------------------------------------------------------- TEIL 3
T3_TEMPLATE = dict(t='Vorlage: Gemeinsam planen', te='Template: planning together', lines=[
 ('{{Wir wollen also}} [[Aktivität]] {{planen. Womit fangen wir an?}}', 'So we want to plan … Where do we start?'),
 ('{{Ich schlage vor, dass wir}} [[Vorschlag 1, Verb am Ende]]. {{Was hältst du davon?}}', 'I suggest that we … What do you think?'),
 ('{{Das ist eine gute Idee!}} {{Wir könnten auch}} [[Ergänzung, Infinitiv am Ende]].', 'That is a good idea! We could also …'),
 ('{{Ich weiß nicht. Vielleicht sollten wir eher}} [[Alternative]]? {{Das ist zwar ein guter Vorschlag, aber}} [[Problem]].', 'I do not know. Maybe we should rather … That is a good suggestion, but …'),
 ('{{Wann / Wo / Wer / Was / Wie viel}} [[Punkt von der Notiz]]? {{Ich denke,}} [[Vorschlag]].', 'When / where / who / what / how much …? I think …'),
 ('{{Als Kompromiss schlage ich vor, dass}} [[Lösung]]. {{Einverstanden?}}', 'As a compromise I suggest that … Agreed?'),
 ('{{Wer kümmert sich um}} [[Aufgabe]]? {{Ich kann}} [[Aufgabe]] {{übernehmen. Kannst du}} [[Aufgabe]]{{?}}', 'Who takes care of …? I can take over … Can you …?'),
 ('{{Dann haben wir alles besprochen.}} {{Also machen wir es so:}} [[Zusammenfassung]].', 'So we have discussed everything. So we do it like this: …')])

T3_BANK = [
 ('Etwas vorschlagen', 'Making a suggestion', [
  ('{{Ich habe eine Idee / einen Vorschlag.}}', 'I have an idea / a suggestion.'), ('{{Ich schlage vor, dass wir}} …', 'I suggest that we …'), ('{{Mein Vorschlag wäre}} …', 'My suggestion would be …'),
  ('{{Wollen wir}} …{{?}}', 'Shall we …?'), ('{{Wir könnten auch}} …', 'We could also …'), ('{{Was hältst du / halten Sie davon?}}', 'What do you think about it?'),
  ('{{Wie findest du / finden Sie}} …{{?}}', 'How do you find …?'), ('{{Vielleicht wäre es besser, wenn}} …', 'Maybe it would be better if …')]),
 ('Zustimmen', 'Agreeing', [
  ('{{Ja, das ist eine gute Idee!}}', 'Yes, that is a good idea!'), ('{{Das gefällt mir. Wir dürfen aber nicht vergessen,}} …', 'I like that. But we must not forget …'),
  ('{{Das finde ich gut / super / prima.}}', 'I think that is good / great.'), ('{{Ich bin deiner / Ihrer Meinung.}}', 'I agree with you.'), ('{{Damit bin ich einverstanden.}}', 'I agree with that.'),
  ('{{Du hast / Sie haben recht.}}', 'You are right.'), ('{{Dazu könnten wir noch}} …', 'In addition we could …')]),
 ('Zweifel ausdrücken', 'Expressing doubt', [
  ('{{Ich weiß nicht. Vielleicht sollten wir eher}} …{{?}}', 'I do not know. Maybe we should rather …?'), ('{{Vielleicht können wir das so machen, aber}} …', 'Maybe we can do it like that, but …'),
  ('{{Das ist zwar ein guter Vorschlag, aber}} …', 'That is a good suggestion, but …'), ('{{Ich finde es besser, wenn}} …', 'I think it is better if …')]),
 ('Ablehnen und Kompromiss', 'Refusing and compromise', [
  ('{{Es tut mir leid, aber ich kann nicht zustimmen.}}', 'I am sorry but I cannot agree.'), ('{{Besser wäre es, wenn}} …', 'It would be better if …'),
  ('{{Das finde ich nicht gut. Ich habe eine andere Idee.}}', 'I do not think that is good. I have another idea.'), ('{{Ich bin anderer Meinung. Wir sollten}} …', 'I disagree. We should …'),
  ('{{Das kommt nicht in Frage.}}', 'That is out of the question.'), ('{{Als Kompromiss schlage ich vor, dass}} …', 'As a compromise I suggest that …')]),
 ('Aufgaben verteilen und abschließen', 'Sharing tasks and finishing', [
  ('{{Wer kümmert sich um}} …{{?}}', 'Who takes care of …?'), ('{{Ich kann}} … {{übernehmen. Kannst du}} …{{?}}', 'I can take over … Can you …?'),
  ('{{Wann treffen wir uns?}} {{Wo treffen wir uns?}}', 'When do we meet? Where do we meet?'), ('{{Also, wir haben}} … {{besprochen. Machen wir es so?}}', 'So we have discussed … Shall we do it like this?'),
  ('{{Gut, dann ist alles klar.}}', 'Good, then everything is clear.')]),
]

T3_DIALOGS = [
 dict(t='Fahrradausflug', te='Bicycle trip', pts='Wohin? · Kilometer pro Tag? · Übernachtung? · Was mitnehmen? · Wer macht was?', lines=[
  ('A', 'Wir wollen also einen Fahrradausflug machen. {{Wohin sollen wir fahren?}}', 'So we want to go on a bicycle trip. Where should we go?'),
  ('B', '{{Ich würde den Bodensee vorschlagen.}} Dort gibt es einen schönen Radweg.', 'I would suggest Lake Constance. There is a nice cycle path.'),
  ('A', '{{Gute Idee!}} Was ist dort besonders interessant?', 'Good idea! What is especially interesting there?'),
  ('B', 'Man kann schöne Städte wie Konstanz und Lindau besuchen, und die Landschaft ist wunderschön.', 'You can visit beautiful towns like Konstanz and Lindau and the landscape is lovely.'),
  ('A', '{{Wie viele Kilometer sollten wir pro Tag fahren?}}', 'How many kilometres should we ride per day?'),
  ('B', 'Ich denke, 40 bis 50 Kilometer sind gut. {{Dann ist es nicht zu anstrengend.}}', 'I think 40 to 50 km is good. Then it is not too tiring.'),
  ('A', '{{Einverstanden.}} Und wo übernachten wir?', 'Agreed. And where do we stay?'),
  ('B', '{{Wir könnten}} in Jugendherbergen oder kleinen Pensionen übernachten. Das ist nicht so teuer.', 'We could stay in youth hostels or small guesthouses. That is not so expensive.'),
  ('A', '{{Das gefällt mir.}} Was müssen wir mitnehmen?', 'I like that. What do we have to take?'),
  ('B', 'Auf jeden Fall einen Helm, eine Regenjacke, Sonnencreme und genug Wasser.', 'Definitely a helmet, a rain jacket, sun cream and enough water.'),
  ('A', '{{Wer kümmert sich um was?}}', 'Who takes care of what?'),
  ('B', '{{Ich kann}} die Unterkünfte {{buchen. Kannst du}} die Route planen?', 'I can book the accommodation. Can you plan the route?'),
  ('A', 'Ja, gern. {{Dann ist alles klar.}}', 'Yes, gladly. Then everything is clear.')]),
 dict(t='Kindergeburtstag', te='Child’s birthday party', pts='Wann? · Wen einladen? · Geschenk? · Essen? · Bei schlechtem Wetter?', lines=[
  ('A', 'Wir wollen also den Geburtstag von Leon feiern. {{Wann sollen wir die Party machen?}}', 'So we want to celebrate Leon’s birthday. When should we hold the party?'),
  ('B', '{{Ich schlage vor, dass wir}} am Samstagnachmittag feiern. Da haben alle Kinder Zeit.', 'I suggest that we celebrate on Saturday afternoon. All the children are free then.'),
  ('A', '{{Das finde ich gut.}} Und wen laden wir ein?', 'I think that is good. And whom do we invite?'),
  ('B', 'Ich denke, zehn Kinder aus seiner Klasse sind genug. {{Mehr wären zu laut.}}', 'I think ten children from his class are enough. More would be too loud.'),
  ('A', '{{Das ist zwar ein guter Vorschlag, aber}} unsere Wohnung ist klein. {{Vielleicht sollten wir eher}} acht Kinder einladen?', 'That is a good suggestion, but our flat is small. Maybe we should rather invite eight children?'),
  ('B', '{{Als Kompromiss schlage ich vor, dass}} wir acht Kinder einladen. {{Einverstanden?}}', 'As a compromise I suggest we invite eight children. Agreed?'),
  ('A', '{{Damit bin ich einverstanden.}} Was schenken wir Leon?', 'I agree with that. What do we give Leon?'),
  ('B', 'Er liebt Fußball. {{Wir könnten}} ihm einen Fußball und ein Trikot schenken.', 'He loves football. We could give him a football and a shirt.'),
  ('A', '{{Gute Idee!}} Und was gibt es zu essen? Vielleicht Pizza und Kuchen?', 'Good idea! And what is there to eat? Maybe pizza and cake?'),
  ('B', 'Ja. Und was machen wir, wenn es regnet? {{Wir könnten}} im Wohnzimmer Spiele spielen.', 'Yes. And what do we do if it rains? We could play games in the living room.'),
  ('A', '{{Ich kann}} den Kuchen backen. {{Kannst du}} die Einladungen schreiben?', 'I can bake the cake. Can you write the invitations?'),
  ('B', 'Gern, das mache ich heute Abend.', 'Gladly, I will do that tonight.')]),
 dict(t='Abschiedsfeier für eine Kollegin', te='Farewell party for a colleague', pts='Wann? · Wo? · Geschenk? · Musik? · Wer wird eingeladen?', lines=[
  ('A', 'Unsere Kollegin Frau Keller geht in Rente. {{Wir wollen also eine Abschiedsfeier planen. Wann machen wir sie?}}', 'Our colleague Ms Keller is retiring. So we want to plan a farewell party. When do we hold it?'),
  ('B', '{{Mein Vorschlag wäre}} ihr letzter Arbeitstag, am Freitag, um 16 Uhr.', 'My suggestion would be her last working day, on Friday at 4 pm.'),
  ('A', '{{Ja, das ist eine gute Idee!}} Und wo feiern wir?', 'Yes, that is a good idea! And where do we celebrate?'),
  ('B', 'Im Büro, im großen Besprechungsraum. {{Dann sparen wir Geld.}}', 'In the office, in the big meeting room. Then we save money.'),
  ('A', '{{Ich weiß nicht. Vielleicht sollten wir eher}} in ein Restaurant gehen? Im Büro ist es nicht so gemütlich.', 'I do not know. Maybe we should rather go to a restaurant? The office is not so cosy.'),
  ('B', '{{Besser wäre es, wenn}} wir zuerst im Büro anstoßen und danach zusammen essen gehen.', 'It would be better if we first toast in the office and then go for a meal together.'),
  ('A', '{{Das gefällt mir.}} Was schenken wir ihr?', 'I like that. What do we give her?'),
  ('B', 'Alle Kollegen geben etwas Geld, und wir kaufen einen Gutschein für eine Reise.', 'All colleagues give some money and we buy a voucher for a trip.'),
  ('A', '{{Dazu könnten wir noch}} eine Karte mit Unterschriften machen. Und Musik?', 'In addition we could make a card with signatures. And music?'),
  ('B', 'Ein Kollege spielt Gitarre. {{Wer kümmert sich um}} die Einladungen?', 'A colleague plays guitar. Who takes care of the invitations?'),
  ('A', '{{Ich kann}} sie übernehmen. {{Dann ist alles klar.}}', 'I can take them over. Then everything is clear.')]),
 dict(t='Feier nach der bestandenen Prüfung', te='Party after passing the exam', pts='Was machen? · Wann? · Wo? · Wer bezahlt? · Weitere Treffen?', lines=[
  ('A', 'Wir wollen nach der Prüfung zusammen feiern. {{Was machen wir?}}', 'We want to celebrate together after the exam. What do we do?'),
  ('B', '{{Wie wäre es, wenn wir}} ein Picknick im Park machen? Das ist günstig.', 'How about having a picnic in the park? That is cheap.'),
  ('A', '{{Das ist zwar ein guter Vorschlag, aber}} im Februar ist es zu kalt. {{Ich schlage vor, dass wir}} in einem Café feiern.', 'That is a good suggestion, but in February it is too cold. I suggest that we celebrate in a café.'),
  ('B', '{{Da bin ich deiner Meinung.}} Und wann? Direkt nach der Prüfung?', 'I agree with you. And when? Right after the exam?'),
  ('A', 'Nein, am Samstag. {{Dann sind wir nicht mehr müde.}} Um 15 Uhr?', 'No, on Saturday. Then we are no longer tired. At 3 pm?'),
  ('B', '{{Einverstanden.}} Wer bezahlt das Essen?', 'Agreed. Who pays for the food?'),
  ('A', '{{Als Kompromiss schlage ich vor, dass}} jeder sein Essen selbst bezahlt, und die Lehrerin bekommt von uns einen Kuchen.', 'As a compromise I suggest everyone pays for their own food, and we give the teacher a cake.'),
  ('B', '{{Das finde ich super.}} {{Wollen wir}} uns auch später noch treffen?', 'I think that is great. Shall we also meet later?'),
  ('A', 'Ja, {{wir könnten}} einmal im Monat zusammen kochen. Dann üben wir weiter Deutsch.', 'Yes, we could cook together once a month. Then we keep practising German.'),
  ('B', '{{Gute Idee!}} Ich schreibe eine Gruppe in WhatsApp.', 'Good idea! I will create a WhatsApp group.')]),
]
T3_PRACTICE = dict(t='Übung: im Kreis vorschlagen', te='Exercise: suggesting in a circle', de=[
 ('A', 'Ich schlage vor, dass wir alle in ein Café gehen.', 'I suggest that we all go to a café.'),
 ('B', 'Das ist zwar eine gute Idee, aber wir sind zu viele. Wäre es nicht besser, wenn wir im Park spazieren gehen?', 'That is a good idea, but there are too many of us. Would it not be better if we walked in the park?'),
 ('C', 'Nein, das finde ich nicht gut. Draußen ist es doch zu kalt. Was haltet ihr davon, wenn wir in die Bibliothek gehen?', 'No, I do not think that is good. It is too cold outside. What do you think about going to the library?')],
 topics=['Abschiedsgeschenk für die Kursleiterin / den Kursleiter', 'Tagesausflug in die nähere Umgebung', 'Ort für ein Fest nach der bestandenen Prüfung', 'Was unternehmen wir heute nach dem Kurs?'],
 how='Sit in a circle. One person makes a suggestion, everyone else reacts (agree, doubt, refuse) and adds a new suggestion. Practise out loud, 6 minutes.')
T3_TIPS = ['Discuss every point on the note and give each point at least one suggestion.', 'Do not only agree: add your own idea, then agree on a final solution (Kompromiss).', 'Use du or Sie consistently, same as in Teil 1.', 'Say who does what at the end: Wer kümmert sich um …?']
