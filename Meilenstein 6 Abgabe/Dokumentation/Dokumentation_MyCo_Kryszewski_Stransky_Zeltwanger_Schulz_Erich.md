## Dokumentation MyCo

|Gruppenmitglieder  |  Matrikelnummer| Kürzel
|--|--|--|
| Georg Erich |39255|ge007|
| Lisa Kryszewski | 38943 | lk157
| Michael Schulz | 39579 | ms560
|Philipp Stransky | 39068 | ps136
| Christoph Zeltwanger |39748 |cz028


**CLOUD COMPUTING TECHNOLOGY WS 19/20**
Prof. Dr.-Ing. Peter Thies
Prof. Dr.-Ing. Christoph Kunz
Datum: 30.01.2020



**

## Inhaltsverzeichnis

**1.0 Aufgabenstellung/Zielsetzung**

	1.1 Rahmenbedingungen

	1.2 Beschreibung des Zielsystems

	1.3 Vorgehensweise

	1.4 Aufgabenverteilung
	
**2.0 Projektphasen**

	2.1 Meilenstein 1

	2.2 Meilenstein 2

	2.3 Meilenstein 3

	2.4 Meilenstein 4

	2.5 Meilenstein 5

	2.6 Meilenstein 6

	2.7 Meilenstein 7

	2.8 Meilenstein 8

**3.0 Theoretische Grundlagen**

	3.1 Neuronales Netz

	3.2 Word Embedding und Word Index

	3.3 Trainingsdaten
	
**4.0 UML-Diagramme**

**5.0 Hinweise für Entwickler**

**6.0 Installationshinweise und Bedienungsanleitung**

	6.1 Benötigte Programme

		6.1.1 GitHub Repository

		6.1.2 Ngrok

		6.1.3 Tensorflow

		6.1.4 Dialogflow

			6.1.4.1 Anlegen von Intents

			6.1.4.2 Anlegen von Entitys

			6.1.4.3 Anlegen von Agents

		6.1.5 PyCharm

		6.1.6 Webhook

		6.1.7 Flask

		6.1.8 Google App Engine

		6.1.9 Google Cloud Plattform

		6.1.10 Google Assistant

	6.2 Bedienungsanleitung und Testing



## 1.0 Aufgabenstellung/Zielsetzung


1.0 Aufgabenstellung/Zielsetzung

  

Ziel des Projektes ist es im Rahmen der Vorlesung CloudComputing des Masterstudiengangs Wirtschaftsinformatik einen selbstlernenden Sprachassistent zu konzipieren, welcher auf Basis des Google Home entwickelt wird. Dieser hat das Ziel einen Gesprächsverlauf durchzuführen und dem Nutzer als Recherchetool zu dienen. Anhand der Spracheingabe sollen Themen ermittelt werden, welche dem Nutzer in einer Liste von relevanten Dokumenten ausgegeben werden. Dabei soll das Zielsystem in drei Teilbereiche untergliedert sein (s. Abb. 1). Die Spracheingabe des Nutzers soll an den Sprachassistenten weitergeleitet werden um einen Gesprächskontext aufzubauen. Dabei soll sich das System zudem vergangene Anfragen merken und somit trainiert werden.

![Abb. 1: Grobstruktur Zielsystem](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilenstein%206%20Abgabe/Bilder_Final_Dokumentation/Abb1.JPG) 
Abb.1: Grobstruktur Zielsystem


**1.1 Rahmenbedingungen**


Die Zusammensetzung der Gruppen wird den Studierenden selbst überlassen, wobei sich die Projektgruppen hierbei auf 4-5 Personen belaufen. Die Gruppen müssen ihre Zusammensetzung spätestens eine Woche nach Bekanntgabe der Aufgabenstellung den Dozenten verbindlich über das Moodle-System mitteilen. Weiterhin müssen alle Teilnehmer spätestens zu diesem Zeitpunkt in dem bekanntgegebenen Moodle-Kurs registriert sein, um die Prüfungsvorleistung in diesem Semester erbringen zu können.

Im Projektverlauf muss jede Gruppe Teilaufgaben zusammen mit den dafür verantwortlichen Gruppenmitgliedern definieren. Zudem muss jede Gruppe ein GitHub Repository (s. Kapitel 6.1.1) erfolgreich einrichten, sodass für die Dozenten als auch für die Studierenden ein dauerhafter Zugriff möglich ist. Darüber hinaus sollten die Aufgaben und die Verantwortlichkeiten innerhalb des Teams verteilt werden und zum Zeitpunkt des ersten Meilensteins angegeben werden. Die für die erfolgreiche Bearbeitung des Projekts nötigen Kenntnisse bauen auf bisher erlernten Inhalten auf und müssen falls erforderlich selbständig erweitert werden. Durch die Arbeit mit GitHub ist für die Dozenten jeder Schritt sichtbar, daher wird es eine individuelle Bewertung jedes Teammitglieds geben.

Ein weiterer Punkt ist es das sich die Teammitglieder gegenseitig, jedoch anonym, bewerten hinsichtlich Aufgaben, Arbeitsweise und Verantwortlichkeit. Nach Abschluss des Projektes wird dieses auf der Medianight der Hochschule der Medien vorgestellt und demonstriert. Die vorherige Anmeldung hierfür dient Maßgeblich dazu um das Projekt zu werten und ist daher eine Voraussetzung. Zum erfolgreichen Bestehen der praktischen Arbeit muss jeder geforderte Meilenstein dieses Projektes (s. Kapitel 2.0) erbracht werden. Zur Unterstützung der Projektteams werden anstelle der organisierten Vorlesungen, Sprechstunden bei den Dozenten abgehalten, die individuell von den Projektteams über Moodle gebucht werden. Ansonsten können die Übungsstunden in eigener Regie für Teambesprechungen, die Dokumentenerstellung und zur Programmierung verwendet werden.

**1.2 Beschreibung des Zielsystems**

![Abb. 2: Grobstruktur Zielsystem](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilenstein%206%20Abgabe/Bilder_Final_Dokumentation/Abb2.JPG) 
Abb. 2: Zielsystem

In Abbildung 2 beschreiben wir unser Zielsystem und dessen Aufbau. Das System soll wie folgt aufgebaut sein. Die Eingabe erfolgt über einen Google Home der mit Dialogflow verbunden ist. Dialogflow soll die Eingabe des Users erkennen. Aus der Eingabe werden dann anhand eines Wortindexes aus den Worten Zahlen, die in einem Array abgebildet werden, umgewandelt. Ngrok baut einen Tunnel zwischen dem lokalen Host und dem Server durch den die Eingabe gesendet wird. Flask nimmt dann die Eingabe, die von Dialogflow gesendet wurde, entgegen und leitet sie weiter an Python Skript. Aus der Eingabe wird dann in Pythonskript anhand eines Wortindexes aus den Worten Zahlen, die in einem Array abgebildet werden, umgewandelt. In dem Python Skript wird ein neuronales Netz erzeugt dessen Input aus dem Array mit den Zahlen die durch den Wortindex erzeugt wurden und den einzelnen Dokumenten, deren Inhalt mit Hilfe des Wortidexes auch in Zahlen umgewandelt wird und als Array in das Netz hineingegeben wird. Als Output des neuronalen Netzes gibt es nur zwei Neuronen, eis für relevant und eins für nicht relevant. Flask leitet dann die als relevant gekennzeichneten Ausgabe von Python Skript über den immer noch bestehenden Tunnel von Ngrok an eine HTML-Seite.Auf dieser HTML Seite wir eine Liste mit allen relevanten Dokumenten an den User ausgegeben.


**1.3 Vorgehensweise**

Wir entschieden im Team, uns immer dienstags und freitags zusammenzusetzen und uns von Treffen zu Treffen Ziele zu stecken, sodass wir diese dann im nächsten Treffen besprechen konnten. Diese Treffen fanden sowohl an der Hochschule statt als auch mehrmals wöchentlich per Skype. In diesen Treffen wurde besprochen, was genau für das nächste Treffen zu tun ist. Es wurde außerdem besprochen, wie und ob die gesteckten Ziele erreicht wurden. Es wurde dann entweder diskutiert warum ein Ziel nicht erreicht wurde und wie man es im Team erreichen könnte oder man hat die erzielten Ergebnisse reflektiert und bewertet, inwieweit die erzielten Ergebnisse zielführend sind. So wollten wir uns Stück für Stück dem Erreichen des jeweiligen Meilensteins und natürlich auch dem Projektziel nähern. Während jeder Projektphase ist auf eine angemessene Dokumentation zu achten.Es ist wichtig, dass man den Entwicklungsprozess während und auch nach Abschluss des Projekts nachvollziehen kann. Daher ist auch eine textuelle Beschreibung inklusive Installations- und Bedienungsanleitung nötig. Zur Erstellung von Code wurde die Entwicklungsumgebung PyCharm verwendet werden. Zur Erstellung und Pflege von UML-Diagrammen ist die Software StarUML zu verwenden. Zur Koordination der Projektteilnehmer untereinander und der verschiedenen Software-Entwicklungsstufen ist GIT als Werkzeug zur verteilten Versionsverwaltung unter Nutzung des webbasierten Git-Hosting-Dienstes GitHub zu verwenden. Die GitHub-Nutzernamen müssen eine Identifizierung der Teilnehmer in Form von vollständigen Klarnamen ermöglichen. Den Dozenten ist dauerhaft ein Zugriff auf sämtliche GitHub-Repositories einzuräumen, die im Zuge dieses

Projekts benutzt werden. Jedes Teammitglied hat sich an der Entwicklungstätigkeit substantiell zu beteiligen. Die individuellen Beiträge der Teammitglieder sind durch Commits auf GitHub zu fixieren. Im Rahmen von Vorlesungen und sonstigen erworbenen Kenntnissen wird darüber hinaus erwartet, dass bei Bedarf selbständig weiterführende Informationen aus der Literatur oder im Internet genutzt werden.

**1.4 Aufgabenverteilung**

Zu Beginn wollten wir die Aufgaben klar abgrenzen und einteilen. Jedoch wurde schnell klar das dies nicht der effektivste Weg bei diesem Projekt war. Wir entschieden uns daher für eine agile Arbeitsweise bei der wir uns wöchentlich mehrmals trafen um den aktuellen Status zu besprechen und zudem auch die wöchentlichen Meetings bei den Professoren wahr nahmen. Wir in unserem Team haben uns dazu entschlossen alle gemeinschaftlich mit dem gleichen Anteil an den Aufgaben zu arbeiten sodass jeder das gleiche Verständnis zu der Fallstudie und der Aufgabe aufbauen kann. Diese Arbeitsweise half uns dabei Probleme schneller zu erkennen und zu lösen, insbesondere dann wenn ein Gruppenmitglied Schwierigkeiten bei einer Aufgabe hatte.

## 2.0 Projektphasen
Die Projektarbeit unterteilt sich in 8 Meilensteine mit mehreren Unteraufgaben (s. Abb. 3). Auf diese wird im folgenden Kapitel näher eingegangen und diese beschrieben.

	2.1 Meilenstein 1

Der erste Meilenstein befasst sich unter anderem mit der ersten Grundvoraussetzung für die Teilnahme an diesem Projekt und damit einem Organisatorischen Gesichtspunkt. Daher beinhaltet dieser Meilenstein zum einen die erfolgreiche Teilnahme an der ersten Auftaktveranstaltung an diesem Projekt, sowie die Registrierung für diesen Kurs via Moodle.

	  2.2 Meilenstein 2

Im zweiten Meilenstein erfolgt die Aufstellung von Teilaufgaben bzw. die Überlegung einer Strategie/Vorgehensweise für das anstehende Projekt. Ebenfalls wurde ein GitHub Repository (s. Kap. 6.1.1) eingerichtet um den Teammitgliedern sowie den Dozenten einen Dauerhaften Zugriff auf hochgeladene und geteilte Inhalte zu gewähren.

	2.3 Meilenstein 3

Der dritte Meilenstein gliedert sich in zwei Teilaufgaben und befasst sich mit dem Start der Realisierung der Fallstudie durch Dialogflow und den damit kooperierenden Programmen, die in Kapitel 4.0 noch weiter erläutert werden.

	2.4 Meilenstein 4

In Meilenstein vier Die Demonstration der bisherigen abgearbeiteten Meilensteinen bzw. des aktuellen Projektstands erfolgte live bei der Projektpräsentation am 03.12.2019.

 
	2.3 Meilenstein 5

In Meilenstein fünf erfolgte das “Peer-Feedback” und dient der gegenseitigen und anonymen Bewertung der Projektmitglieder. Dadurch soll den Dozenten ein besserer Überblick über die Arbeitsweise innerhalb des Teams gegeben werden.

	2.4 Meilenstein 6

Der sechste Meilenstein befasst sich mit der Umsetzung des bisherigen Projekts in Tensor Flow. Für die Realisierung des Neuronalen Netzes wurde das Python Modul Tensor Flow eingesetzt.

	2.5 Meilenstein 7

Nach Abschluss der vorherigen Meilensteine erfolgt im siebten Meilenstein die Demonstration sowie Präsentation des Projektes vor den Dozenten sowie im Anschluss auf der Medianight um dadurch die Funktionalität der Fallstudie zu zeigen.

	2.6 Meilenstein 8

Wie auch in Meilenstein fünf, erfolgt in Meilenstein acht ebenfalls ein erneutes und abschließendes Peer-Feedback um die Teammitglieder abschließend zu bewerten und den Dozenten ein finales Fazit über die Arbeitsweise und Projektarbeit während des Projektes zu geben.
Die Projektarbeit unterteilt sich in 3 Meilensteine mit mehreren Unteraufgaben (s. Abb. 5). Auf diese wird im folgenden Kapitel näher eingegangen und diese beschrieben.

![Abb. 3: Grobstruktur Zielsystem](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilenstein%206%20Abgabe/Bilder_Final_Dokumentation/Abb3.JPG)
Abb.3: Meilensteine

## **3.0 Theoretische Grundlagen**

	  3.1 Neuronales Netz
	  
![Abb. 4: Grobstruktur Zielsystem](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilenstein%206%20Abgabe/Bilder_Final_Dokumentation/Abb4.JPG)
Abb.4: Neuronales Netz

Ein neuronales Netz ist eine Ansammlung von einzelnen Informationsverarbeitung Einheiten, auch Neuronen genannt, die schichtweise in einer Netzarchitektur angeordnet sind. Neuronen eines künstlichen neuronalen Netzes sind schichtweise in sogenannten Layern angeordnet. Das neuronale Netz besteht aus dem Embedding Layer oder Input Layer, in das ein Array aus Zahlen gesteckt wird, das durch das Umwandeln der Anfrage mit Hilfe des Wortindex entsteht. Außerdem wird ein Dokument, ebenfalls mit Hilfe des Wortindexes in ein Zahlenarry umgewandelt, in das neuronale Netz gesteckt. Dieses Embedding Layer besteht im vorliegenden Netz aus 210 Neuronen. Zwischen dem Input Layer und dem Output Layer kann eine vielzahl von Hidden Layern eingesetzt werden. In diesem Fall ist es ein Hidden Layer. Im Hidden Layer der dem Embedding Layer nachfolgt gibt es noch 125 Neuronen, die sich dann im Output Layer auf zwei Neuronen reduzieren. Hier gibt es ein Neuron für “relevant”, also sprich das Dokument aus dem Embedding Layer ist für die Anfrag aus dem Embedding Layer relevant oder “nicht relevant”, also das Dokument ist nicht relevant für die Anfrage. Hierbei gibt das Netz aber nicht relevant oder nicht relevant aus sondern gibt bei jeweils einem Output Neuron eine 1 (trifft zu) und 0 (trifft nicht zu) aus. Gibt das Neuron for relevant eine 1 und das Neuron für nicht relevant eine 0 aus, ist das Dokument für die Anfrage relevant.

	3.2 Word Embedding und Word Index
Damit ein Neuronales Netz Input in form von Wörtern verarbeiten kann muss dieser in Zahlen umgewandelt werden. Neuronale Netze können können nur mit Daten in Zahlenform arbeiten. Um dies umwandeln zu können muss ein Wortindex erstellt werden. Ein Wortindex ist ein dictionary (Wörterbuch) das aus Key Value Paaren besteht. Jedes Wort ist eindeutig einem Index zuzuordnen. Der Wortindex beinhaltet jedes Wort, dass im gesamten Datensatz verwendet wird. Dadurch lässt sich jedes Dokument in eine Form bringen mit der das neuronale Netz arbeiten kann.

	3.4 Trainingsdaten
Um ein neuronales Netz zu Trainieren, benötigt man Trainingsdaten. Die Erstellung der Trainingsdaten wurden aus dem Reuters-Datensatz “rcv1” die ersten vier Ordner ausgewählt. Auf Basis dieser, in den Ordnern erhaltenen, Dokumente wurden die Trainingsdaten erstellt. Trainingsdaten bestehen aus einer “Anfrage”, damit ist der Input zu verstehen nach dem ein Nutzer suchen könnte. Zu jeder Anfrage wurden von hand einige Dokumente aus dem Datensatz herausgesucht die passend zu der gestellten Anfrage sind. Um diese Aufgabe etwas geschickter zu gestalten wurde ein Skript geschrieben in welchen nach bestimmten Keywörtern im gesamten Datensatz gesucht werden konnte (siehe Abb. 5.1 + 5.2).

![Abb. 5: Grobstruktur Zielsystem](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilenstein%206%20Abgabe/Bilder_Final_Dokumentation/Abb51.JPG))
Abb.5.1: Themensuche Trainingsdaten

![Abb. 5: Grobstruktur Zielsystem](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilenstein%206%20Abgabe/Bilder_Final_Dokumentation/Abb52.JPG)
Abb. 5.1: Themensuche Trainingsdaten


4.0 Hinweise für Entwickler

  

Folgender Teil der Dokumentation enthält Informationen für alle an der Weiterentwicklung des Programms interessierten Parteien.

  

**Eingesetzte Entwicklungs-Werkzeuge**

Folgende Werkzeuge wurden zur Realisierung des Systems benutzt:

  

**Zur Kommunikation im Team:**

-   Github (Git Hosting Plattform)
    
-   Google Drive
    
-   WhatsApp Gruppe
    
-   Skype
    
    
**Zur Modellierung der Use-Cases, UML-Klassendiagramme**

-   StarUML
    
**Zur Entwicklung von Hosting und Applikationslogik:**

-   Dialogflow
    
-   Tensor Flow
    
-   Keras
    
-   Entwicklungsumgebung - Pycharm
    
-   Google Assistant
    
-   Google App Engine

## **5.0 UML-Diagramme**

Im folgenden Kapitel werden die erstellten Diagramme dargestellt. Die Diagramme wurden mit Hilfe von “StarUML” erstellt. Das erste Diagramm (s. Abb. 6 ) zeigt den Gesprächskontext.

	  5.1 Gesprächskontext

![Abb. 6: Grobstruktur Zielsystem](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilenstein%206%20Abgabe/Bilder_Final_Dokumentation/Abb6.JPG)
Abb. 6: Gesprächskontext

Die folgende Abbildung (s. Abb.7 ) zeigt den Use Case “Sprachassistent”.

![Abb. 7: Grobstruktur Zielsystem](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilenstein%206%20Abgabe/Bilder_Final_Dokumentation/Abb7.JPG)
Abb. 7: Sprachassistent

---
| Name       | Dokumentenanfrage           | 
| ------------- |:-------------:| 
| Ziel      |  Google Assistant identifiziert das gewünschte Dokument für den Nutzers  | 
| Vorbedingung     | Der Nutzer verfügt über ein Google-Home gerät oder ein Gerät, auf welchem Google Assistent verfügbar ist und der Google Assistant wurde gestartet ; Der Nutzer führt eine Spracheingabe durch, in welcher der Nutzer nach dem gewünschten Dokument anfragt       | 
| Nachbedingung| Der Sprachassistent identifiziert das gewünschte Dokument und zeigt dieses dem Nutzer an  | 
| Nachbedingung im Sonderfall | Google Assistent verfügt nicht über das gewünschte Dokument und kann somit das Dokument nicht ausgeben | 
| Akteuer | Nutzer | 
| Normalablauf | Der Nutzer benutz Google Assistant und fragt nach einen Dokument. Diese Anfrage wird unmittelbar verarbeitet und das System identifiziert das Dokument  und teilt dies dem Nutzer mit |
| Sonderfälle |Das gewünschte Dokument des Nutzers kann nicht identifiziert werden, da es nicht im Datensatz vorhanden ist |
---

---
| Name       | Dokumentenbestätigung           | 
| ------------- |:-------------:| 
| Ziel      |  Google Assistant identifiziert das gewünschte Dokument für den Nutzer und zeigt dies dem Nutzer an  | 
| Vorbedingung     | Der Nutzer verfügt über ein Google-Home gerät oder ein Gerät, auf welchem Google Assistent verfügbar ist und der Google Assistant wurde gestartet ; Der Nutzer führt eine Spracheingabe durch, in welcher der Nutzer nach dem gewünschten Dokument anfragt       | 
| Nachbedingung| Der Sprachassistent identifiziert das gewünschte Dokument und stellt dies für die Konsumierung zur Verfügung  | 
| Nachbedingung im Sonderfall | Google Assistent verfügt nicht über das gewünschte Dokument und kann somit das Dokument nicht ausgeben | 
| Akteuer | Nutzer | 
| Normalablauf | Der Nutzer benutz Google Assistant und fragt nach einen Dokument. Diese Anfrage wird unmittelbar verarbeitet und das System identifiziert das Dokument  zeigt dies dem Nutzer an |
| Sonderfälle |Das gewünschte Dokument des Nutzers kann nicht identifiziert werden, da es nicht im Datensatz vorhanden ist |
---

---
| Name       | Spracheingabe           | 
| ------------- |:-------------:| 
| Ziel      | Die Spracheingabe zu Google Assistant | 
| Vorbedingung     | Der Nutzer verfügt über ein Google-Home gerät oder ein Gerät, auf welchem Google Assistent verfügbar ist und der Google Assistant wurde gestartet      | 
| Nachbedingung| Der Sprachassistent verarbeitet die Gesprächseingabe des Nutzers  | 
| Nachbedingung im Sonderfall |Das System kann die Spracheingabe nicht verarbeiten und meldet den Nutzer einen Fehler | 
| Akteuer | Nutzer | 
| Normalablauf | Der Nutzer benutz Google Assistant, indem dieser eine Spracheingabe tätigt. Diese Spracheingabe wird anschließend vom Google Assistant verarbeitet |
| Sonderfälle |Die Spracheingabe kann nicht verarbeitet werden auf Grund undeutiger Spracheingabe, falsche Eingabesprache oder einen Hardwaredefekt (z.B. Mikrofon) |
---
---
| Name       | Sprachassistent starten           | 
| ------------- |:-------------:| 
| Ziel      | Das starten des Sprachassistenten | 
| Vorbedingung     | Der Nutzer verfügt über ein Google-Home gerät oder ein Gerät, auf welchem Google Assistent verfügbar ist      | 
| Nachbedingung| Der Sprachassistent ist gestartet  | 
| Nachbedingung im Sonderfall | - | 
| Akteuer | Nutzer | 
| Normalablauf | Der Nutzer startet Google Assistent über Google Home oder ein anderes kompatibeles Gerät |
| Sonderfälle | - |
---
						    
---
| Name       | Themenanfrage           | 
| ------------- |:-------------:| 
| Ziel      |  Google Assistant identifiziert das gewünschte Thema des Nutzers  | 
| Vorbedingung     | Der Nutzer verfügt über ein Google-Home gerät oder ein Gerät, auf welchem Google Assistent verfügbar ist und der Google Assistant wurde gestartet ; Der Nutzer führt eine Spracheingabe durch, in welcher der Nutzer nach seinem gewünschten Thema anfragt       | 
| Nachbedingung| Der Sprachassistent identifiziert das gewünschte Thema des Nutzers  | 
| Nachbedingung im Sonderfall | Google Assistent kann das Thema nicht identifizieren | 
| Akteuer | Nutzer | 
| Normalablauf | Der Nutzer benutz Google Assistant und fragt nach einen Thema. Diese Anfrage wird unmittelbar verarbeitet und das System identifiziert das Thema und teilt dies dem Nutzer mit |
| Sonderfälle |Das gewünschte Thema des Nutzers kann nicht identifiziert werden, da es nicht im Datensatz vorhanden ist |
---
## **6.0 Installationshinweise und Bedienungsanleitung**

Für die Realisierung und Vereinfachung des Projektes, sind einige Plugins und Programme notwendig. Diese Programme sind zum einen für die Entwicklung relevant sowie für die Teaminterne Kommunikation.

	6.1 Benötigte Programme

Für die erfolgreiche Entwicklung und Implementierung sind folgende Programme notwendig:

-   GitHub
    
-   nGrok
    
-   Tensor Flow
    
-   Dialogflow
    
-   Pycharm
    
-   Webhook
    
-   Flask
    
-   Google Assistant
    
-   Google App Engine
    



		6.1.1 GitHub Repository

  

Um es allen Mitgliedern möglich zu machen gleichzeitig an diesem Projekt arbeiten zu können, war die Einrichtung eines GitHub Repositories unumgänglich. Durch die Nutzung des GitHub Repository werden veränderte Codes nicht überschrieben. Hierbei hat jedes Gruppenmitglied zwei Branches. Ein Branch beinhaltet den Namen des jeweiligen Gruppenmitglieds und der zweite Branch ist ein lokaler Master Branch. Unter folgendem Link ist das Repository der Gruppe namens “MyCo-Gruppe-3” zu finden: [https://github.com/georgerich/MyCo-Gruppe-3](https://github.com/georgerich/MyCo-Gruppe-3)
		
		6.1.2 ngrok

  

Ngrok ist eine Software die es erlaubt Software zu Testen ohne sie in die Cloud zu laden. Dazu öffnet Ngrok einen Tunnel zwischen einem Localhost Port und einem ngrok-Server der für Cloud-Anwendungen erreichbar ist. Daten werden an den ngrok-Server gesendet und von dort aus an den Localhost weitergeleitet. Ngrok wird dazu genutzt mobile Apps zu testen die über ein Lokales Backend verfügen, oder zum testen von Cloud-Anwendungen ohne zu sie deployen.

  
  
  
  
  

		6.1.3 Tensor Flow

  

Tensor Flow ist ein Framework für die Datenstrom Orientierten Programmierung. Tensorflow wird für Anwendungen des maschinelle Lernens benutzt. Mit Komponenten aus Tensor Flow lassen sich Neuronale Netze relativ einfach aufsetzen und trainieren. Tensor Flow wurde ursprünglich vom Google-Brain-Team für den Google-internen Bedarf entwickelt und später unter der Apache-2.0-Open-Source-Lizenz veröffentlicht. Tensor Flow liefert eine umfangreiche Dokumentation sowie eine vielzahl von Beispielanwendungen direkt auf der Offiziellen Website.

  
  
  

		6.1.4 Dialogflow

  

Im folgenden wird der Umgang mit dem Tool “Dialogflow” näher beschrieben. Dabei wird auf das Anlegen von Intents, Entities und Agents eingegangen und der Umgang mit diesen Funktionen erklärt.

  

			6.1.4.1 Anlegen von Intents

  

In diesem Kapitel wird das Anlegen von Intents beschrieben. Intents werden benötigt, um Eingaben des Users zu erkennen, verarbeiten zu können und eine passende Antwort auf die Eingabe auszugeben.

Im Folgenden wird in einer Klickanleitung beschrieben, wie man einen Intent anlegt.

Als erstes klickt man in der linken Menüleiste auf den Punkt Intent (s. Abb. 8) und oben auf den Button “Create Intent”.

![Abb. 8: Grobstruktur Zielsystem](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilenstein%206%20Abgabe/Bilder_Final_Dokumentation/Abb8.JPG)
Abb. 8: Create Intent 

Im unteren Bereich sieht man die bereits ausgewählten bzw. angelegten Intents. Hier zum Beispiel “Book a flight ticket”, “Default Fallback Intent” und “Default Welcome Intent”. Wenn man auf den Button Create Intent geklickt hat, öffnet sich ein neuer Intent (s. Abb. 9)

![Abb. 9: Grobstruktur Zielsystem](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilenstein%206%20Abgabe/Bilder_Final_Dokumentation/Abb9.JPG)
Abb. 9: Neuer Intent

Als muss man dem Intent in der obersten Zeile einen Namen geben. In dem Abbildungs Beispiel hat der Intent den Namen “Find Subject”.

Unter dem Punkt “Training Phrases” werden mögliche Eingaben des Users vordefiniert. Man sieht hier auch schon farblich markierte Parameter, die als Entities angelegt werden. Wie man ein Entity anlegt wird in Kapitel 6.1.4.2 erklärt.

Man hat außerdem die Möglichkeit Antworten auf Eingaben zu definieren (s. Abb. 10).


![Abb. 10: Grobstruktur Zielsystem](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilenstein%206%20Abgabe/Bilder_Final_Dokumentation/Abb10.JPG)
Abb. 10: Responses

In unserem Beispiel wurden keine Antworten für dieses Intent hinzugefügt, da es sonst Probleme mit der Übergabe der Daten gibt. Wichtig ist für unser Intent außerdem unter dem Punkt Fulfillment den Punkt “Enable webhook call for this intent” aktiv zu setzen.

Dieser von uns angelegte Intent, erkennt finance, politics, technology, science und health als topic. Education, company und government wurden als Subtopics angelegt. Außerdem erkennt das Intent soweit alle Länder, da ein vorgefertigtes Entity für alle Länder verwendet wurde.

			6.1.4.2 Anlegen von Entitys

Entities werden benötigt, um in einem Intent ein Thema zu erkennen. im Folgenden wird beschrieben, wie man ein Intent anlegen kann.

![Abb. 11: Grobstruktur Zielsystem](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilenstein%206%20Abgabe/Bilder_Final_Dokumentation/Abb11.JPG)
Abb. 11: Entity anlegen

Um ein Entity anzulegen klickt man in der linken Menüleiste auf den Punkt Entities (s. Abb. 11). Als erstes wird dem Entity ein Name gegeben, welcher in unserem Fall Topic ist. wir haben hier die Topics financ, politic, tech, scien und health definiert. Für jedes Topic wurden mehrer mögliche Schreibweisen definiert. Im Anschluss kann im Intent auf dieses Entity verwiesen werden und dadurch die Themen erkannt werden, über die gesprochen werden möchte.

			6.1.4.3 Anlegen von Agents

Einen Agent benötigt man um Intents und Entities anlegen zu können. Einen Agent kann man durchaus als Projekt bezeichnen. Das Anlegen wird im Folgenden beschrieben (s. Abb.12).

![Abb. 12: Grobstruktur Zielsystem](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilenstein%206%20Abgabe/Bilder_Final_Dokumentation/Abb12.JPG)
Abb. 12: Anlegen von Agents

Um einen neuen Agent anzulegen, muss man in der linken Menüleiste das Dropdown Menü öffnen und unten auf “Create new Agent” klicken. Daraufhin öffnet sich folgendes Fenster (s. Abb. 13).


![Abb. 13: Grobstruktur Zielsystem](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilenstein%206%20Abgabe/Bilder_Final_Dokumentation/Abb13.JPG)
Abb. 13: Create New Agents

Hier kann man den Agent benennen, die Sprache und die Zeitzone einstellen. Im Anschluss klickt man auch “Create” und der Agent ist erstellt.


			6.1.5 Pycharm

PyCharm ist die Entwicklungsumgebung, mit dessen Hilfe das neuronale Netz aufgebaut wurde. In PyCharm werden zunächst alle nötigen Packages installiert, um den Code importieren zu können. Hier werden außerdem die Anfragen mittels Wortindex umgewandelt um den Input für das neuronale Netz zu erzeugen.

			6.1.6 Webhook

WebHooks ermöglichen es, einer Server-Software mitzuteilen, dass ein bestimmtes Ereignis eingetreten ist und eine Reaktion auf das Ereignis auslösen. Über einen WebHook werden die in Dialogflow erkannte Eingaben an ein, auf Input wartendes Pythonskript schicken. In dem Pythonskript werden die Daten dann verarbeitet und die eigentliche Suche nach passenden Dokumenten durchgeführt. Der Webhook stellt die Verbindung zwischen Dialogflow und Python her.


			6.1.7 Flask

Flask ist ein Mikroframework für Python basierend auf den Bibliotheken „Werkzeug“, einer Bibliothek zum Erstellen von WSGI-Anwendungen und Jinja2, einer Template-Engine. Mit Flask können einfach und unkompliziert Web-Applikationen erstellt werden. Es benötigt nur wenig Quellcode, um eine Web-Applikation aufzusetzen und zum Laufen zu bekommen. Flask wird vorwiegend für Testzwecke verwendet, da es schon durch wenige Zeilen Code lauffähig ist.

 
			6.1.8 Google App Engine

Die Google App Engine ist ein Platform-as-a-Service, der von Google zum Entwickeln und Bereitstellen von Web Anwendungen zu Verfügung gestellt wird. Ein einfaches Hochladen der Anwendung wird hiermit ermöglicht. Für dieses Projekt war ein Upload dieser Art ebenfalls vorgesehen. Durch einige technische Fehler, die leider nicht behoben werden konnten, war ein Upload in dieser Form nicht möglich.

  

			6.1.9 Google Cloud Plattform

Die Google Cloud Platform, die von Google angeboten wird, ist eine Reihe von Cloud-Computing-Diensten, die auf der gleichen Infrastruktur laufen, die auch Google selbst intern für seine Endbenutzer Produkte wie Google Search und YouTube nutzt. Die Google Cloud Platform bietet Infrastructure as a Service, Platform as a Service und serverlose Computer Umgebungen.

  

			6.1.10 Google Assistant

Der Google Assistant wird dafür benötigt um den Google Home Speaker einzurichten.

Dieser dient in diesem Projekt als eine Art Mikrofon an das man seine Anfrage stellen kann, um dadurch eine Ausgabe zu erhalten. Mittels des Google Assistants kann der Google Home auf dem Smartphone eingerichtet werden. Hierfür müssen sich Smartphone und das Google Home Gerät im selben WLAN befinden um eine erfolgreiche Verbindung herzustellen und das Gerät erfolgreich einzurichten.

	6.2 Bedienungsanleitung und Testing

Für eine erfolgreiche Inbetriebnahme des Projektes gilt es die Installationshinweise zu beachten sowie die in diesem Kapitel beschriebenen Programme zu Installieren.

  

**1. Schritt: ngrok**

-   Download von [https://ngrok.com/download](https://ngrok.com/download)
    
-   Datei entpacken
    
-   Exe-Datei ausführen
    
-   "ngrok http 5000" in der Kommandozeile ausführen (s.Abb. 15)

![Abb. 14: Grobstruktur Zielsystem](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilenstein%206%20Abgabe/Bilder_Final_Dokumentation/Abb14.JPG)
Abb. 14: ngrok http 5000

-   Markierte URL kopieren oder aufschreiben
    

  

**2. Schritt: Dialogflow**

-   Agent importieren:
    

	-   Einstellungen
	    
	-   Import and Export
	    
	-   IMPORT FROM ZIP
	    
	-   Datei aus Git-Repository auswählen [Dialogflow Agent/MyCo.zip](Dialogflow%20Agent/MyCo.zip)
	    

  

-   Webhook aktivieren:
    

	-   Fulfillment
	    
	-   Enable Webhook
	    
	-   Zuvor kopierte URL einfügen und "/webhook" ohne Leerzeichen dazwischen anhängen
	    
	-   speichern
    

  
  

**3. Schritt: PyCharm**

-   Kontrollieren ob alle nötigen Packages installiert sind (siehe Rot unterstrichener "Import code". Ansonsten Pakete installieren
    
-   MyCoApp.py ausführen
    

**4. Schritt: Anfragen in Dialogflow stellen**

  

Nach den zuvor befolgten Installationsschritten erfolgt das stellen von Anfragen über Dialogflow.

Diese gestellten Anfragen werden über die Actions Console mittels Google Assistant gestellt, wodurch der erstellte Agent getestet werden kann. Dazu muss die Testumgebung aufgerufen werden (s. Abb.15 Testumgebung). In der Testumgebung kann der erstellte Agent über den Google Home Speaker getestet werden indem man Anfragen stellt. Für ein erfolgreiches Testen müssen der Google Home Speaker und der zu testende Agent über den gleichen Google Account angemeldet sein mit der der Agent erstellt wurde und der Google Home Speaker eingerichtet wurde.

Für das Testing selbst spricht man folgenden Befehl in den Google Home Speaker “Okay Google, talk to my test app” nach dieser Ausführung erfolgt eine Abfrage via dem Google Home Speaker in Form einer Begrüßung. Nun spricht man seine Anfrage aus. Die Anfrage wird nun an das Python Skript weitergeleitet welches im Hintergrund läuft und auf den Webhook wartet. Abschließend führt das Skript die Suche nach dem Begriff durch und gibt die für relevant befundenen Dokumente auf html-Seite localhost:5000 aus.

![Abb. 15: Grobstruktur Zielsystem](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilenstein%206%20Abgabe/Bilder_Final_Dokumentation/Abb15.JPG)
Abb. 15: Testumgebung


## **7.0 Zusammenfassung**

Im Rahmen dieses Projektes haben wir uns mit der Implementierung eines intelligenten Sprachassistenten befasst. Diese Aufgabe hat uns vor einige Herausforderungen gestellt. Hier galt es sich als erstes mit der Implementierung eines neuronalen Netzes auseinanderzusetzen, welches das Herzstück unseres Projektes bilden sollte. Hierzu mussten wir uns erst mit der allgemeinen Funktionsweise eines solchen Netzes befassen und deren Funktionsweise vertraut machen. Eine weitere Herausforderung nach der Implementierung des Netzes war das Trainieren, welches sich als recht knifflig erwies. Das Bereitstellen von Trainingsdaten erwies sich dabei als schwieriger aber auch wichtiger als gedacht. Hier musste sehr sorgfältig gearbeitet werden, denn das sollte die Grundlage unseres Netzes bilden. Alles in allem können wir auf ein sehr spannendes und anspruchsvolles Projekt zurückblicken, welches uns vor viele Herausforderungen gestellt hat, bei dem wir aber an diesen Herausforderungen gewachsen sind und viel dabei mitnehmen konnten.

  
  
  

	7.1 Ausblick

Dadurch das dieses Projekt im 2. Semester WI unter der Lehrveranstaltung “Technology Lab” weiter bearbeitet wird, werden wir daran arbeiten die aktuellen Differenzen zu verbessern. Dabei soll dem Nutzer auch die Möglichkeit geboten werden ausführlichere Dialoge mit dem Sprachassistenten zu führen. Dieser soll außerdem zukünftig in der Lage sein dem User nicht mehr eine Liste von Dokumenten anzuzeigen, sondern durch den Dialog und damit verbundene Nachfragen, die Suche so zu spezifizieren, dass nur noch ein Dokument angezeigt wird, das perfekt auf die Anfrage des Nutzers passt. Zudem soll der Sprachassistent durch verbesserte Nachfragen dem User mehr und mehr das Gefühl vermitteln mit einer realen Person zu sprechen und nicht mit einem System.
