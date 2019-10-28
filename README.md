[Moodle Kurs](https://e-learning.hdm-stuttgart.de/moodle/course/view.php?id=2455) 
--
Cloud Computing | Gruppe 3  | WS 2019-2020|
---
| Gruppenmitglieder        | Matrikelnummer           | KÃ¼rzel  |
| ------------- |:-------------:| -----:|
| Georg Erich      | 39255 | ge007 | 
| Lisa Kryszewski     | 38943      | lk157 |
| Michael Schulz|  39579  | ms560 |
| Philipp Stransky | 39068 | ps136 |
| Christoph Zeltwanger | 39748 | cz028 |

---
						    

## Aufgabenstellung im WS 2019/

# Cloud Computing Technology

## Prof. Dr.-Ing. Christoph Kunz & Prof. Dr.-Ing. Peter Thies

```
Modul 368101 
PrÃ¼fungsleistung: Praktische Arbeit und PrÃ¤sentation (PP)
Workload: 5 ECTS
```
## 1. Einleitung

Ziel dieser Lehrveranstaltung ist eine vertiefende Auseinandersetzung mit technischen Fragestellungen
des Cloud Computing und affinen Technologien. Einerseits sollen sich die Teilnehmer spezifische
Techniken aneignen und damit auseinandersetzen. Andererseits sollen diese Techniken von allen
Studierenden im Kontext eines Projekts angewendet werden. Da Software stets das Ergebnis von
TeamaktivitÃ¤ten ist, sollen die Projektarbeiten im Gruppenkontext durchgefÃ¼hrt werden.
Im Rahmen der Projektarbeit steht insbesondere die Frage im Vordergrund, wie am Markt verfÃ¼gbare
Softwarekomponenten unter technischen und wirtschaftlichen Gesichtspunkten zu einem Gesamtsystem
assembliert werden kÃ¶nnen. Dabei ist ein Customizing jener Komponenten bzw. eine entsprechende
individuelle ImplementationstÃ¤tigkeit unumgÃ¤nglich. Weiterhin ist eine wirtschaftliche Beurteilung der
verwendeten Dienste bzw. Komponenten erforderlich.

## 2. Szenario

Lisa Meier ist Mitarbeiterin im Projekt HighNet, zur Erarbeitung neuer AnsÃ¤tze der Integration von
Informationslogistik fÃ¼r z.B. PKW-Fahrer. Im Rahmen dieses mehrjÃ¤hrigen Vorhabens arbeitet Ihre
Stuttgarter Firma Broken Bits fÃ¼r das weltweit agierende Unternehmen Star Cars in Tokio. Das Projekt ist
eines von vielen, dass Broken Bits sowohl mit Star Cars als auch anderen Auftraggebern der Branche
verbindet.
Lisa Meier ist eine von  3  Probanden zur Erprobung von â€‹ _MyCorrespondent_ â€‹(kurz: MyCo). Bei dieser von
Broken Bits konzipierten und realisierten Cloud-basierten Dienstleistung handelt es sich um einen
intelligenten Sprachassistenten. â€‹ _MyCo_ verbindet die MÃ¶glichkeiten von Assistenten wie Google Assistant
bzw. Google Home mit Verfahren zur Realisierung kÃ¼nstlicher Intelligenz.
Mittels â€‹ _MyCo_ kann Lisa nun im angebundenen Nachrichten-Repository recherchieren. Dabei kann â€‹ _MyCo_
anders als heutige Systeme wie Amazon Alexa oder Google Home einen langfristigen GesprÃ¤chskontext
bzw. ein persÃ¶nliches Interessenprofil erlernen und zur Anwendung bringen, wÃ¤hrend es sich mit Lisa
unterhÃ¤lt oder Antworten gibt.
Im Zuge des Projekts HighNet werden zahlreiche Dokumente bereitgestellt. Insbesondere Dokumente
von Dritten (vgl. Nachrichten) spielen eine Rolle. Dokumente werden vorrangig in einer Markup-Sprache
reprÃ¤sentiert. Es kÃ¶nnen jedoch auch Dokumente der folgenden Typen zur Anwendung kommen:
Office-artige Textdokumente, Tabellen sowie Grafiken, Videos, Software-Quelltext, Links auf Web Pages
u.v.a.m.
Heute ist wieder einer der Tage, an dem Lisa eine Testkonversation mit dem â€‹ _MyCo_ â€‹-Prototypen
durchfÃ¼hrt. Sie initiiert dazu eine Konversation mit â€‹ _MyCo_ â€‹. Dieses System setzt auf einem verbreiteten
Sprachassistenzsystem auf und bietet einen neuen, viel weitergehenden Service.
WÃ¤hrend Sie sich mit â€‹ _MyCo_ Ã¼ber das Projekt unterhÃ¤lt, interpretiert die Software das Gesprochene. Dies
resultiert in einer separaten Anzeige von Projektinhalten, die wahrscheinlich mit dem gerade
Besprochenen in Verbindung stehen. Durch Sprachbefehle kann sie das jeweilige Dokument anzeigen
lassen oder annotieren (z.B. durch neue SchlagwÃ¶rter oder allgemeine Anmerkungen):
Prof. Dr.-Ing. Peter Thies âœŽ thies@hdm-stuttgart.de
Hochschule der Medien â˜� +49 (0) 711 / 89 23 - 31 94
NobelstraÃŸe 10 âŒ‚ [http://www.prof-thies.de](http://www.prof-thies.de)
70569 Stuttgart Seite 1 von 7


_Lisa: Hello MyCo!
MyCo: Hello, Lisa! How are you?
Lisa: Iâ€™m fine. Thank you.
[GesprÃ¤chshistorie von Lisas GesprÃ¤chen mit MyCo]
1
Lisa: Let Ì�s talk about current political activities concerning health care within the USA.
MyCo: Ok, Lisa, what do you want to know?
Lisa: Show me all the documents of the Obama presidency!
MyCo: No problem. Here they are!
[Nachrichtendokumente]
Lisa: Please show me the docs that are still relevant under the actual government!
MyCo: Wait a second - do you expect these?
[Nachrichtendokumente]
Lisa: Yeah, but thereâ€™s one document missing. I need the doc weâ€™ve been talking about
yesterday. It was a comparison of the USâ€™ health system and those of other
industrial
nations.
[-]
MyCo: Yesterday we used those two reports. Which one do want to see?
[Zeigt beide Reports an und nennt zudem deren Namen akustisch.]
Lisa: Good boy! Show me â€œDocument 879â€œ. Thatâ€™s what Iâ€™ve been looking for!
MyCo: Here you are!
[Das entsprechende Dokument wird angezeigt. Lisa liest und ist stumm.]
MyCo: Lisa, what else can I do?
Lisa Oh, thank you! Thatâ€™s all for now. Bye!
MyCo: You are welcome. Have a nice day! Bye!
[MyCo beendet die Konversation.]_
Das GesprÃ¤ch verlÃ¤uft also erfolgreich. Lisa findet, was sie sucht.
Trotz anfÃ¤nglicher Vorbehalte konnte man sich auf den Einsatz des neuen Assistenzsystems einigen, das
vollstÃ¤ndig auf Google-basierter Software aufsetzt. So kommen etwa Google Home/Assistant,
Tensorflow, Google Drive mit den darin bekannten Dokumenttypen sowie Google Container Engine,
Google Compute Engine, Google App Engine sowie die SpeicherlÃ¶sungen von Google, wie etwa Google
Cloud Storage zum Einsatz.

## 3. Rahmenbedingungen

Die Teilnehmer sollen in einer simulierten Umgebung einen technologischen Innovationsprozess erleben
und gestalten. Es wird angenommen, dass es sich bei der Umgebung um ein Unternehmen handelt,
dass im Rahmen einer neuen GeschÃ¤ftsidee den Einstieg in neue Technologien (Sprachassistenten in
Verbindung mit KI^2 ) wagt. Auch wenn die finale Programmierung des Zielsystems wahrscheinlich bei
einem Zulieferer/Auftragnehmer (Inland oder Offshore) stattfinden wird, so muss doch der Aufbau von
geschÃ¤ftskritischem Know How (vgl. Intellectual Property) vor Ort erfolgen, um Spezifikationen fÃ¼r
Auftragnehmer erstellen und diese effektiv steuern zu kÃ¶nnen.
Es wurde ein kleines Projektteam gegrÃ¼ndet, das auf Basis von vorgefertigter Software (z.B. Google
Infrastruktur) mit mÃ¶glichst hoher ProduktivitÃ¤t Machbarkeitsstudien im Bereich zuvor identifizierter
â€žChallengesâ€œ durchfÃ¼hrt. Das Vorgehen sowie die Ergebnisse dieser Studien mÃ¼ssen fÃ¼r nachfolgende
Projektphasen und spÃ¤ter hinzuzuziehende Projektmitarbeiter (in-/extern) hinsichtlich Inhalt und Struktur
geeignet aufbereitet und dokumentiert werden. Darauf aufbauend wÃ¤ren zu einem spÃ¤teren Zeitpunkt
Spezifikationen erforderlich, die an Zulieferer im Rahmen einer Beauftragung weitergegeben werden
kÃ¶nnten.

(^1) Texte in eckigen Klammern beschreiben mÃ¶gliche Dokumente, die automatische zur Auswahl angezeigt werden.
(^2) KI = KÃ¼nstliche Intelligenz


## 4. Aufgaben

Die Zusammensetzung der Gruppen wird wird den Studierenden Ã¼berlassen. Alle Teilnehmer mÃ¼ssen
spÃ¤testens eine Woche nach Bekanntgabe der Aufgabe in den begleitenden Moodle-Kurs eingetragen
sein und die Zusammensetzung ihrer Gruppe gemeldet haben, um die PrÃ¼fungsleistung in diesem
Semester erbringen zu kÃ¶nnen.
Im Projektverlauf muss jede Gruppe Teilaufgaben zusammen mit den dafÃ¼r verantwortlichen
Gruppenmitgliedern definieren. Zum Zeitpunkt des zweiten Meilensteins (s. Tabelle am Ende dieses
Dokuments) mÃ¼ssen die fÃ¼r die einzelnen Teilaufgaben verantwortlichen Gruppenmitglieder benannt
werden.
Die Beurteilung der praktischen Arbeit (vgl. PrÃ¼fungsform PP) erfolgt durch die Dozenten. Jedes
Teammitglied erhÃ¤lt eine individuelle Bewertung. Dennoch steht die gesamte Gruppe wie im beruflichen
Alltag einem kollektiven Erfolgszwang gegenÃ¼ber.
Zum erfolgreichen Bestehen der praktischen Arbeit muss jeder der in der Tabelle am Ende dieser
AusfÃ¼hrungen dargestellten Meilensteine erbracht werden. Die Note der PrÃ¼fungsleistung wird anhand
der individuellen Teilleistungen gemÃ¤ÃŸ Tabelle 1 ermittelt.
Die fÃ¼r die erfolgreiche Bearbeitung des Projekts nÃ¶tigen Kenntnisse bauen auf den
Zugangsvoraussetzungen zum Studiengang auf und mÃ¼ssen selbstÃ¤ndig erweitert werden.
Zur UnterstÃ¼tzung der Projektteams werden Projektmeetings mit den Dozenten abgehalten, die zur
vereinbarten Zeit in Anspruch genommen werden kÃ¶nnen. Ansonsten erfolgt die Teamarbeit (Recherche,
Dokumentenerstellung und Programmentwicklung) in eigener Regie.

## 5. Charakterisierung des Zielsystems

Jede Gruppe hat die Aufgabe, im Rahmen von Fallstudien Komponenten eines Cloud-basierten
Sprachassistenzsystems zu entwickeln, das dem in Abschnitt  2  vorgestellten Szenario entspricht bzw.
hierfÃ¼r eine angemessene LÃ¶sung bietet. Das Szenario bietet einige Herausforderungen, die zu
bewÃ¤ltigen sind. Hierzu sind Recherchen, Machbarkeitsstudien und schlieÃŸlich Bewertungen erforderlich,
wie man als Team diese Challenges meistern will. Folgende Herausforderungen mÃ¼ssen von den
Teilnehmern bewÃ¤ltigt werden:
**Challenge 1: Nutzung herkÃ¶mmlicher Sprachassistenten**
Aus der Konversation mit dem Assistenten mÃ¼ssen GesprÃ¤chsinhalte abgeleitet werden, die eine
Identifikation von GesprÃ¤chsthemen ermÃ¶glichen.
**Challenge 2: ReprÃ¤sentation des GesprÃ¤chskontexts sowie der Dokumentstrukturen**
Die in den Nachrichtendokumenten dargestellte Information muss hinsichtlich ihrer Bedeutung fÃ¼r den
GesprÃ¤chskontext aufbereitet werden. Die Frage, welche Funktion ein Dokument bezÃ¼glich eines
GesprÃ¤chskontexts besitzt, muss geeignet reprÃ¤sentiert werden, um mittelbar die thematische
Zuordnung des jeweiligen Dokuments zu einem GesprÃ¤chskontext zu ermÃ¶glichen.
Die Verbindung zwischen Spracherkennung, Dokumentennutzung und GesprÃ¤chskontext erfordert die
ReprÃ¤sentation von GesprÃ¤chskontexten z.B. auf Basis von Ereignissen.
**Challenge 3: Maschinelles Lernen**
Mit der Zeit sollte sich das System bei der PrÃ¤sentation relevanter Dokumente bezogen auf den
GesprÃ¤chskontext verbessern. Vom Nutzer in einem GesprÃ¤chskontext erwÃ¤hnte, verwendete, d.h.
ausgewÃ¤hlte oder geÃ¶ffnete Dokumente zeichnen diese besonders aus. Diese ZusammenhÃ¤nge kÃ¶nnen
mit der Zeit gelernt und fÃ¼r die Auswahl von zu prÃ¤sentierenden Dokumente genutzt werden.


## 6. Spezifische Anforderungen an das Zielsystem

An das zu realisierende System werden die folgenden Anforderungen gestellt:
A1: Das System soll das AuswÃ¤hlen und Anzeigen von Dokumenten aus einem Repository (z.B.
zahlreiche XML-Dokumenten oder Google Drive/Google Docs, wie Textdokumente, Tabellen,
PrÃ¤sentationen) wÃ¤hrend Konversationen unterstÃ¼tzen.
A2: Eine Konversation wird mittels eines Sprachassistenten auf Basis von Google Home/Assistant
durchgefÃ¼hrt.
A3: WÃ¤hrend einer Konversation wird das GesprÃ¤ch analysiert. Es wird daraus der GesprÃ¤chskontext
(z.B.: Wer spricht aktuell worÃ¼ber? Wann hat man worÃ¼ber gesprochen und welche Dokumente wurden
konsumiert?) abgeleitet und einer weiteren Verarbeitung (Lernen) zugÃ¤nglich gemacht.
A4: Die im Dokumenten-Repository abgelegten Dokumente werden inhaltlich hinsichtlich ihres Typs (z.B.
Nachricht aus der Wirtschaft, Unfallmeldung usw.) analysiert. Es wird eine entsprechende inhaltliche
ReprÃ¤sentation fÃ¼r diese Dokumente softwaretechnisch erstellt und abgespeichert.
A5: Eine Inferenz-Komponente leitet aus den bzgl. A3 & A4 erzeugten Daten wÃ¤hrend einer Konversation
eventuell relevante Dokumente ab und benachrichtigt den Benutzer.
A6: Eine zur Konversation ergÃ¤nzende, parallel ausgefÃ¼hrte Zusatzkomponente zeigt bzgl. A5 alle
relevant eingestuften Dokumente zur Auswahl an (einfache Liste wie in einem File Manager).
A7: Einzusetzende Systeme bzw. Dienste sind zwingend Google Home/Assistant, Google Drive sowie
ergÃ¤nzend ggf. Google Compute Engine, Google Container Engine, Google App Engine und Google
Web Toolkit. Der Einsatz weiterer Systeme oder Dienste ist im Vorfeld mit den Dozenten abzustimmen.
A8: FÃ¼r die Dokumentation von Software-Strukturen ist die Unified Modeling Language (UML) zu
verwenden. Dies gilt insbesondere fÃ¼r den Software-Entwurf.
A9: FÃ¼r die Inferenz im Allgemeinen (siehe A5) ist Tensorflow zu verwenden.
A10: Verwendete Programmiersprachen: Sofern eine Java API oder Python API der verwendeten Dienste
und Komponenten verfÃ¼gbar ist, sind diese zu nutzen. ErgÃ¤nzend kann auch auf Javascript
zurÃ¼ckgegriffen werden. Hierzu muss innerhalb der Gruppe ein Konsens erzielt werden.
A11: Falls erforderlich sind fÃ¼r die Integration (Nutzung und Bereitstellung) von Diensten Web Services
nach dem REST-Ansatz zu nutzen. VerfÃ¼gbare Frameworks, die dies z.B. im Java-Umfeld erlauben, sind
Jersey, RestEasy, Restlet und Google Cloud Endpoints.
A12: Jegliche Dokumente sind in dem Format Markdown zu verfassen.


Abbildung 1: Grobarchitektur des Zielsystems
Es ist ein mehrschichtiges System zu entwickeln, das aus einer Vielzahl von Komponenten und Diensten
3
bestehen wird (vgl. Abbildung).
Die oberste Schicht wird die PrÃ¤sentationsschicht sein. Sie wird dem Sprachassistenten und dessen
Anbindung sowie dem Watchdog bestehen. Mit Hilfe des Watchdog werden Ereignisse einer
Konversation zu einem GesprÃ¤chskontext zusammengefÃ¼gt und so der Ãœbergang zur Applikationslogik
geschaffen.
Die mittlere Schicht nimmt die Applikationslogik (auch Anwendungslogik oder Business-Logik genannt)
auf. Sie enthÃ¤lt sÃ¤mtliche Dienste, die notwendig sind, um die Datenstrukturen (Dokumente, Ereignisse,
etc.) und Funktionen (Auswahl relevanter Dokumente, Feststellen von GesprÃ¤chsgegenstÃ¤nden etc.) des
Systems handhaben und bereitstellen zu kÃ¶nnen. Damit erfolgt eine Trennung von den anderen
Funktionen des Systems, die sich z.B. mit der Ã¤uÃŸeren Darstellung oder der internen Speicherung der
Daten befassen. FÃ¼r eine Applikationslogik lieÃŸen sich somit mehrere PrÃ¤sentationslogiken und mehrere
Speicherlogiken definieren.
Anders als in monolithischen Client-Server-Architekturen muss hier die mittlere Schicht nicht durch einen
einzelnen Applikationsserver dargestellt werden, sondern kann aus eine Vielzahl von Diensten (Web
Services) bestehen, die unabhÃ¤ngig voneinander lauffÃ¤hig sein sollen. Es sind mindestens die in der
Abbildung (s.o.) abgebildeten Dienste anzubieten.
Die oben genannte FunktionalitÃ¤t erfordert, dass sich die Applikationslogik in Kontakt mit dem Repository
(z.B. Google Drive) befindet, um die jeweils nÃ¶tigen Daten/Dokumente auslesen bzw. neue Daten (s.
GesprÃ¤chskontext) ablegen zu kÃ¶nnen. Die Datenbankschicht wird demzufolge mit einem Repository
sowie dessen Anbindung an die Services der Applikationsschicht realisiert. Die Anbindung des
Repository kann durch Google-spezifische Frameworks in Verbindung mit eigenentwickelten Mappern
erfolgen.
Die Gruppen sollen dafÃ¼r sorgen, dass mÃ¶glichst viele Teile des Gesamtsystems in der Cloud laufen. Der
Client ist auf einem beliebigen Rechner, der auf die Cloud zugreifen kann, vorzufÃ¼hren. Die Teilnehmer

(^3) Man spricht in diesem Zusammenhang auch von einer 3-Tier- oder Multi-Tier-Architektur.
_Tier_ â€‹ wird ['tir] ausgesprochen und steht im Englischen fÃ¼r: Reihe, Sitzreihe, Rang.


haben dafÃ¼r Sorge zu tragen, dass die Demonstration vorab in dem ihnen genannten Raum lauffÃ¤hig ist.
Hierzu bietet sich ein Test an. Der Raum wird den Teilnehmern rechtzeitig vorher bekannt gegeben.
Termine fÃ¼r Tests sind rechtzeitig zu vereinbaren.
Die Aufteilung in drei Schichten bietet einige wichtige Vorteile gegenÃ¼ber z.B. zweischichtigen AnsÃ¤tzen.
Zum einen wird durch die Konzentration sÃ¤mtlicher Applikationslogik auf die mittlere Schicht eine
Entkopplung der PrÃ¤sentationsschicht von der Datenbank erreicht. Zum anderen kÃ¶nnen
PrÃ¤sentations-Clients verÃ¤ndert werden, ohne die Applikationslogik modifizieren zu mÃ¼ssen. DarÃ¼ber
4
hinaus ist es so mÃ¶glich, auf derselben Applikationslogik unterschiedliche Clients aufsetzen zu kÃ¶nnen.
Dies kÃ¶nnten einerseits Clients bzgl. unterschiedlicher Medien (Sprachausgabe, Web-basiert oder
dedizierte Applikationen) oder bzgl. unterschiedlicher Benutzerrollen (z.B. fÃ¼r Reporting oder
Systemnutzung) sein. Aus diesem Grund ist unbedingt darauf zu achten, dass Clients keinerlei
Applikationslogik enthalten. Diese ist ausschlieÃŸlich in der Applikationsschicht zu finden!

## 7. Vorgehensweise

Im Rahmen eines professionellen Software-Engineerings wird die Einhaltung eines
Software-Entwicklungsprozesses erwartet. Dies bedeutet, dass die Projektarbeit in festgelegten Schritten
ablÃ¤uft (z.B. Anforderungsanalyse, Systemspezifikation/Entwurf, Implementierung, Test). Hierbei kann ein
wasserfallartiges Vorgehen oder ein agiler Ansatz (z.B. Extreme Programming oder Scrum) gewÃ¤hlt
werden.
WÃ¤hrend jeder Projektphase ist auf eine angemessene Dokumentation zu achten. Hierzu gehÃ¶ren z.B.
die Erstellung von UML-Diagrammen sowie deren ErlÃ¤uterung und die ausfÃ¼hrliche, sinnvolle
Dokumentation des Programmcodes. Im Falle von Java ist Javadoc zu verwenden.
Es ist wichtig, dass man den Entwicklungsprozess wÃ¤hrend und auch nach Abschluss des Projekts
nachvollziehen kann. Daher ist auch eine textuelle Beschreibung inklusive Installations- und
Bedienungsanleitung nÃ¶tig.
FÃ¼r die Erstellung von UML-Diagrammen ist StarUML zu verwenden. Zur Erstellung von Source-Code ist
im Falle von Java die Entwicklungsumgebung Eclipse oder im Falle von Python PyCharm zu verwenden.
Es wird erwartet, dass der Source-Code den Konventionen der jeweils verwendeten Sprache
entsprechend erstellt wird. Im Fall von Java wÃ¤ren dies z.B. die Java Code Conventions, im Fall von
Python PEP 8. SÃ¤mtliche verwendeten Frameworks bzw. APIs mÃ¼ssen geeignet dokumentiert und
hinsichtlich ihrer VerfÃ¼gbarkeit (lizenzrechtlich und wirtschaftlich) analysiert und dies dokumentiert
werden.
Zur Koordination der Projektteilnehmer untereinander und den verschiedenen
Software-Entwicklungsstufen ist â€‹ _Git_ als Werkzeug zur verteilten Versionsverwaltung unter Nutzung des
webbasierten Git-Hosting-Dienstes GitHub zu verwenden. FÃ¼r Eclipse existiert dazu das eGit-Plugin, mit
dessen Hilfe die Git-Funktionen innerhalb der Entwicklungsumgebung genutzt werden kÃ¶nnen. PyCharm
besitzt eine analoge FunktionalitÃ¤t. Die GitHub-Nutzernamen mÃ¼ssen unbedingt eine Identifizierung der
Teilnehmer â€‹ _in Form von Klarnamen_ ermÃ¶glichen. AbkÃ¼rzungen und Pseudonyme werden nicht
akzeptiert. Den Dozenten ist spÃ¤testens ab Meilenstein  2  dauerhaft ein Zugriff auf sÃ¤mtliche
5
GitHub-Repositories einzurÃ¤umen, die im Zuge dieses Projekts benutzt werden. â€‹ _Jedes Teammitglied hat
sich an der EntwicklungstÃ¤tigkeit substantiell und nachvollziehbar zu beteiligen. Die individuellen BeitrÃ¤ge
sind in mindestens einem Commit pro Arbeitstag und Teammitglied in GitHub zu fixieren. Auch sÃ¤mtliche
weiteren Dokumente sind in Github abzulegen. Diese mÃ¼ssen wie oben bereits erwÃ¤hnt in
Markdown-Format vorliegen. Etwaige bildliche Darstellungen sind als separate Bilddateien in Github
abzulegen und geeignet in die Markdown-Dokumente einzubetten. Es werden nur solche individuellen
BeitrÃ¤ge gewertet, deren zugehÃ¶rige Commits eindeutig und offensichtlich einem Git-Benutzerkonto
unter den sogenannten â€œContributionsâ€� in Github zuordenbar sind._
Im Rahmen von vorausgegangenen Studien der Teilnehmer wie z.B. Bachelor-Studium der
Wirtschaftsinformatik wurden die fÃ¼r die erfolgreiche Projektbearbeitung erforderlichen Grundlagen
vermittelt. Es wird erwartet und ist integraler Bestandteil der Lehrveranstaltung, dass selbstÃ¤ndig

(^4) Z.B. wenn eine Client-Software bzgl. ihres Erscheinungsbilds (optisch oder akustisch) Ã¼berarbeitet werden soll
(^5) â€‹GitHub-Id: PeterThies & ChristophKunz


```
weiterfÃ¼hrende Informationen aus der Literatur und im WWW genutzt werden.
```
## 8. Bewertungskriterien

```
Die Bewertung des Arbeitsergebnisses erfolgt aufgrund unterschiedlicher AktivitÃ¤ten: Zum einen werden
nach Abschluss des Meilensteins  3  und des Meilensteins  6  (vgl. Tabelle 1) PrÃ¤sentationen bzw.
Demonstrationen der bis dahin erreichten Arbeitsergebnisse durchgefÃ¼hrt. Bei der Bewertung werden die
Leistungen der Studierenden gemÃ¤ÃŸ dieser Aufgabenstellung bewertet. Hierzu gehÃ¶rt die Beteiligung an
der Erstellung der Projektdokumente und insbesondere die Source-Code-BeitrÃ¤ge in GitHub.
Wichtig: Die Teilnehmer haben die Ergebnisse selbstÃ¤ndig zu erbringen und sich an sÃ¤mtlichen
TÃ¤tigkeiten umfÃ¤nglich und substanziell zu beteiligen. Zu jeglichen Komponenten (sÃ¤mtliche
Programmteile und Dokumentationen) ist deren Urheberschaft zu dokumentieren. Hierzu gehÃ¶rt auch,
dass sÃ¤mtliche Quellen in geeigneter Weise genannt und adÃ¤quat gekennzeichnet werden.
MaÃŸgeblich fÃ¼r die Deadlines zur Erreichung der Meilensteine sind die in der Tabelle  1  dargestellten
Termine. Eine spÃ¤tere Abgabe und eine zu Github â€‹ alternative Abgabe ist ausgeschlossen â€‹.
```
## 9. Weitere Informationen

```
Weitere Informationen finden sich im Moodle-Kurs fÃ¼r diese Lehrveranstaltung. Insbesondere sind die
FAQ des Moodle-Kurses Teil dieser Aufgabenstellung.
Tabelle 1: Meilensteine & Bewertungskriterien
Meilenstein Bewertung Bewertungskriterien Form Termin
```
1. Teilnahme an der
    Auftaktveranstaltung
Registrierung in Moodle
bestanden/
nicht
bestanden
Hat die Person sich in den Moodle-Kurs eingetragen
und an der Aufgabenbesprechung teilgenommen?
pers. Teilnahme,
Login in den
Moodle-Kurs
22.10.
2. Aufstellung von Teilaufgaben
    und Verantwortlichkeiten;
Einrichten von
GitHub-Repositories und
dauerhafter Zugriff fÃ¼r
Dozent und Teammitglieder
bestanden/
nicht
bestanden
Inhalt und Umfang der BeitrÃ¤ge, erkennbare
Eigenleistung.
Dokumente auf
Github
29.10.
3. Realisierung Fallstudie Google
    Assistant, Dialogflow
       40 Punkte Anschaulichkeit, Aussagekraft, Nachvollziehbarkeit
          sowie Relevanz und AdÃ¤quanz der Fallstudie.
Inhalt und Umfang der individuellen BeitrÃ¤ge, erkennbare
Eigenleistung.
Source Code und
weitere
Dokumente auf
Github
03.12.
4. Demonstration / PrÃ¤sentation 5 Punkte Struktur, Anschaulichkeit, Angemessenheit und
    TransferqualitÃ¤t der PrÃ¤sentation/Demonstration.
Nachweis der allgemeinen FunktionalitÃ¤t der Fallstudie.
Demonstration /
PrÃ¤sentation;
pers. Teilnahme;
Dokumente auf
Github
03.12.
5. Peer-Feedback bestanden/
    nicht
    bestanden
       Peer Feedback abgegeben;
       Tiefe der Auseinandersetzung, Strukturierungsgrad
          Datei in Moodle 03.12.
6. Realisierung Fallstudie
    Tensorflow
       70 Punkte Anschaulichkeit, Aussagekraft, Nachvollziehbarkeit
          sowie Relevanz und AdÃ¤quanz der Fallstudie.
       Inhalt und Umfang der individuellen BeitrÃ¤ge, erkennbare
          Eigenleistung.
             Source Code und
                weitere
                Dokumente auf
                Github
                   30.01.
7. Demonstration / PrÃ¤sentation 5 Punkte Struktur, Anschaulichkeit, Angemessenheit und
    TransferqualitÃ¤t der PrÃ¤sentation/Demonstration
       Nachweis der allgemeinen FunktionalitÃ¤t der Fallstudie.
          Demonstration /
             PrÃ¤sentation
          pers. Teilnahme;
          Dokumente auf
             Github
                30.01.
8. Peer-Feedback bestanden/
    nicht
    bestanden
       Peer Feedback abgegeben;
       Tiefe der Auseinandersetzung, Strukturierungsgrad
          Datei in Moodle 30.01.
---
