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
Datum: 03.12.2019



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

**3.0 Hinweise für Entwickler
4.0 Installationshinweise**

	4.1 Benötigte Programme
		4.1.1 GitHub Repository
		4.1.2 Ngrok
		4.1.3 Dialogflow
			4.1.3.1 Anlegen von Intents
			4.1.3.2 Anlegen von Entitys
			4.1.3.3 Anlegen von Agents
	4.2 Installationsanleitung Testing
	4.3 UML-Diagramme

**5.0 Zusammenfassung**
		
		5.1 Ausblick




## 1.0 Aufgabenstellung/Zielsetzung


1.0 Aufgabenstellung/Zielsetzung

  

Ziel des Projektes ist es im Rahmen der Vorlesung CloudComputing des Masterstudiengangs Wirtschaftsinformatik/Digitale Medien einen selbstlernenden Sprachassistent zu konzipieren, welcher auf Basis des Google Home entwickelt wird. Dieser hat das Ziel einen Gesprächsverlauf durchzuführen und dem Nutzer als Recherchetool zu dienen. Anhand der Spracheingabe sollen Themen ermittelt werden, welche dem Nutzer in einer Liste von relevanten Dokumenten ausgegeben werden. Dabei soll das Zielsystem in drei Teilbereiche untergliedert sein (s. Abb. 1). Die Spracheingabe des Nutzers soll an den Sprachassistenten weitergeleitet werden um einen Gesprächskontext aufzubauen. Dabei soll sich das System zudem vergangene Anfragen merken und somit trainiert werden.

![Abb. 1: Grobstruktur Zielsystem](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilensteine/Meilenstein%203/BilderDoku/4.JPG)


**1.1 Rahmenbedingungen**

Die Projektgruppen belaufen sich auf 4-5 Personen die von den Studierenden selbst eingeteilt wurden. Der erste Meilenstein befasste sich daher damit sich zunächst erfolgreich in den Moodle-Kurs “Cloud Computing und Technology Lab” einzuschreiben sowie an der Auftaktveranstaltung teilzunehmen. Der zweite Meilenstein beschäftigte sich damit das GitHub Repository (s. Kapitel 4.1.1) erfolgreich einzurichten, sodass für die Dozenten als auch für die Studierenden ein dauerhafter Zugriff ermöglicht wird. Zudem sollten die Aufgaben und die Verantwortlichkeiten innerhalb des Teams verteilt werden und zum Zeitpunkt des ersten Meilensteins angegeben werden.

Die für die erfolgreiche Bearbeitung des Projekts nötigen Kenntnisse bauen auf bisher erlernten Inhalten auf und müssen falls erforderlich selbständig erweitert werden. Durch die Arbeit mit GitHub ist für die Dozenten jeder Schritt sichtbar, daher wird es eine individuelle Bewertung jedes Teammitglieds geben. Ein weiterer Punkt ist es das sich die Teammitglieder gegenseitig jedoch anonym bewerten hinsichtlich Aufgaben, Arbeitsweise und Verantwortlichkeit. Nach Abschluss des Projektes wird dieses auf der Medianight der Hochschule der Medien vorgestellt und demonstriert. Die vorherige Anmeldung hierfür dient Maßgeblich dazu um das Projekt zu werten und ist daher eine Voraussetzung.

**1.2 Beschreibung des Zielsystems**

![Abb. 2: Zielsystem](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilensteine/Meilenstein%203/BilderDoku/Zielsystem.JPG)

In Abbildung 2 beschreiben wir unser Zielsystem und dessen Aufbau. Das System soll wie folgt aufgebaut sein. Dialogflow soll die Eingabe des Users, sei es eine Sprach- oder Texteingabe, erkennen und einen JSON-String mit dem angesprochenen Thema erzeugen und senden. Ngrok baut einen Tunnel zwischen dem lokalen Host und dem Server durch den der JSON-String gesendet wird. Flask nimmt dann den JSON-String, der von Dialogflow gesendet wurde, entgegen und leitet ihn weiter an Pythonskript. Das Pythonskript erkennt die gesuchten Begriffe aus dem JSON-String und durchsucht mit einer Volltextsuche den Datensatz, also sprich die Dokumente, nach passenden Dokumenten und gibt diese zurück. Flask leitet dann die Ausgabe von Pythonskript über den immer noch bestehenden Tunnel von Ngrok zurück an Dilogflow. Dialogflow erkennt den zurückgegebenen JSON-String und gibt dem User die Dokumente aus.


**1.3 Vorgehensweise**

Wir entschieden im Team, uns immer montags und freitags zusammenzusetzen und uns von Treffen zu Treffen Ziele zu stecken, sodass wir diese dann im nächsten Treffen besprechen konnten. Diese Treffen fanden immer an der Hochschule statt. In diesen Treffen wurde besprochen, was genau für das nächste Treffen zu tun sei. Es wurde außerdem besprochen, wie und ob die gesteckten Ziele erreicht wurden. Es wurde dann entweder diskutiert warum ein Ziel nicht erreicht wurde und wie man es im Team erreichen könnte oder man hat die erzielten Ergebnisse reflektiert und bewertet, inwieweit die erzielten Ergebnisse zielführend sind. So wollten wir uns Stück für Stück dem Erreichen des Meilensteins nähern.


**1.4 Aufgabenverteilung**

Zu beginn wollten wir die Aufgaben klar abgrenzen und einteilen. Jedoch wurde schnell klar das dies nicht der effektivste Weg bei diesem Projekt war. Wir entschieden uns daher für unser Team für eine agile Arbeitsweise bei denen wir wöchentliche Treffen mit den aktuellen Status besprechen und zudem auch die wöchentlichen Meetings bei den Professoren wahrnehmen (s. Abb. 3). Wir in unserem Team haben uns dazu entschlossen alle gemeinschaftlich mit dem gleichen Anteil an den Aufgaben zu arbeiten sodass jeder das gleiche Verständnis zu der Fallstudie und der Aufgabe aufbauen kann (s. Abb. 4). Diese Arbeitsweise half uns dabei Probleme schneller zu erkennen und zu lösen, insbesondere dann wenn ein Gruppenmitglied Schwierigkeiten bei einer Aufgabe hatte.

![Abb.3:Sprechstunden](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilensteine/Meilenstein%203/BilderDoku/1.JPG)



![Abb.4: AUfgabenverteilung](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilensteine/Meilenstein%203/BilderDoku/2.JPG)



## 2.0 Projektphasen

Die Projektarbeit unterteilt sich in 3 Meilensteine mit mehreren Unteraufgaben (s.Abb. 5). Auf diese wird im folgenden Kapitel näher eingegangen und diese beschrieben.

![Abb. 5: Meilensteine](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilensteine/Meilenstein%203/BilderDoku/3.JPG)

**2.1 Meilenstein 1**

Der erste Meilenstein (s.Abb.6) gliedert sich in zwei Teilaufgaben und beschäftigt sich mit einigen Organisatorischen Gesichtspunkten. Daher beinhaltet dieser Meilenstein die erfolgreiche Teilnahme an der ersten Auftaktveranstaltung an diesem Projekt sowie die Registrierung für diesen Kurs via Moodle. Des weiteren erfolgte die Aufstellung von Teilaufgaben bzw. das überlegen einer Strategie/Vorgehensweise für das anstehende Projekt. Ebenfalls wurde ein GitHub Repository (s. Kap. 4.1.1) eingerichtet um für die Teammitglieder sowie einen Dauerhaften zugriff auf hochgeladene und geteilte Dokumente zu gewähren.

![Abb. 6: Meilenstein 1](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilensteine/Meilenstein%203/BilderDoku/Meilenstein%201.JPG)


**2.2 Meilenstein 2**

Der Meilenstein 2 (s. Abb.7)gliedert sich in drei Teilaufgaben und befasst sich mit dem Start der Realisierung der Fallstudie durch Dialogflow und den damit kooperierenden Programmen, die in Kapitel 4.0 erläutert werden. Die Demonstration der bisherigen abgearbeiteten Meilensteinen erfolgt live bei der Projektpräsentation am 03.12.2019. Das “Peer-Feedback” ist ebenfalls Teil von Meilenstein 2 und dient der gegenseitig und anonym Bewertung der Projektmitglieder.

![Abb.7: Meilenstein 2](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilensteine/Meilenstein%203/BilderDoku/Meilenstein%202.JPG)


**2.3 Meilenstein 3**

IIn Meilenstein 3 (s. Abb. 8) der sich ebenfalls in drei Teilaufgaben gliedert, erfolgt die Umsetzung des bisherigen Projekts in Tensorflow. Zudem wird das abgeschlossene Projekt auf der Medianight demonstriert

![Abb.8: Meilenstein 3](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilensteine/Meilenstein%203/BilderDoku/Meilenstein%203.JPG)

## **3.0 Hinweise für Entwickler**


Folgender Teil der Dokumentation enthält Informationen für alle an der Weiterentwicklung des Programms interessierten Parteien.

**Eingesetzte Entwicklungs-Werkzeuge**

Folgende Werkzeuge wurden zur Realisierung des Systems benutzt:

**Zur Kommunikation im Team**

-   Github (Git Hosting Plattform)
    
-   Google Drive
    
-   WhatsApp Gruppe
    

**Zur Modellierung der Use-Cases, UML-Klassendiagramme**

-   StarUML
    
       
**Zur Entwicklung von Hosting und Applikationslogik**

-   Dialogflow
    
-   Tensorflow
    
-   Keras
    
-   Entwicklungsumgebung - Pycharm
    
-   StackEdit



**

## 4.0 Installationshinweise

**
Für die Realisierung und Vereinfachung des Projektes, sind einige Plugins und Programme notwendig. Diese Programme sind zum einen für die Entwicklung relevant sowie für die Teaminterne Kommunikation.

**4.1 Benötigte Programme**


Für die erfolgreiche Entwicklung und Implementierung sind folgende Programme notwendig:

  

-   GitHub
    
-   nGrok
    
-   Tensorflow
    
-   Dialogflow
    
-   Pycharm
    
-   Elasticsearch
    
-   Webhook
    
-   Flask

		4.1.1 GitHub Repository
	
	Um es allen Mitgliedern möglich zu machen gleichzeitig an diesem Projekt arbeiten zu können, war die Einrichtung eines GitHub Repositorys unumgänglich. Durch die Nutzung des GitHub Repository werden veränderte Codes nicht überschrieben. Hierbei hat jedes Gruppenmitglied zwei Branches. Ein Branch beinhaltet den Namen des jeweiligen Gruppenmitglieds und der zweite Branch ist ein lokaler Master Branch. Unter folgendem Link ist das Repository der Gruppe namens “MyCo-Gruppe-3” zu finden: [https://github.com/georgerich/MyCo-Gruppe-3](https://github.com/georgerich/MyCo-Gruppe-3)
	
		4.1.2 Ngrok
	
Ngrok ist eine Software die es erlaubt Software zu Testen ohne sie in die Cloud zu laden. Dazu öffnet Ngrok einen Tunnel zwischen einem Localhost Port und einem ngrok-Server der für Cloud-Anwendungen erreichbar ist. Daten werden an den ngrok-Server gesendet und von dort aus an den Localhost weitergeleitet. Ngrok wir dazu genutzt mobile Apps zu testen die über ein Lokales Backend verfügen, oder zum testen von Cloud-Anwendungen ohne zu sie deployen.
	
	4.1.3 Dialogflow
	
Im folgenden wird der Umgang mit dem Tool “Dialogflow” näher beschrieben. Dabei wird auf das Anlegen von Intents, Entitys und Agents eingegangen und der Umgang mit diesen Funktionen erklärt.

		4.1.3.1 Anlegen von Intents

In diesem Kapitel wird das Anlegen von Intents beschrieben. Intents werden benötigt, um Eingaben des Users zu erkennen, verarbeiten zu können und eine passende Antwort auf die Eingabe auszugeben.

Im Folgenden wird in einer Klickanleitung beschrieben, wie man einen Intent anlegt.

Als erstes klickt man in der linken Menüleiste auf den Punkt Intent (s. Abb. 9) und oben auf den Button “Create Intent”.

![Abb. 9: Create Intent](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilensteine/Meilenstein%203/BilderDoku/Dialog1.jpeg)

Im unteren Bereich sieht man die bereits ausgewählten bzw. angelegten Intents. Hier zum Beispiel “Book a flight ticket”, “Default Fallback Intent” und “Default Welcome Intent”. Wenn man auf den Button Create Intent geklickt hat, öffnet sich ein neuer Intent (s. Abb. 10)

![Abb. 10: Neuer Intent](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilensteine/Meilenstein%203/BilderDoku/Dialog2.jpeg)

Als muss man dem Intent in der obersten Zeile einen Namen geben. In dem Abbildungs Beispiel hat der Intent den Namen “Find Subject”.
Unter dem Punkt “Training Phrases” werden mögliche Eingaben des Users vordefiniert. Man sieht hier auch schon farblich markierte Parameter, die als Entitys angelegt werden. Wie man ein Entity anlegt wird in Kapitel 4.1.3.2 erklärt.
Man hat außerdem die Möglichkeit Antworten auf Eingaben zu definieren (s. Abb. 11).

![Abb. 11: Responses](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilensteine/Meilenstein%203/BilderDoku/Dialog5.jpeg)

In unserem Beispiel wurden keine Antworten für dieses Intent hinzugefügt, da es sonst Probleme mit der Übergabe der Daten gibt. Wichtig ist für unser Intent außerdem unter dem Punkt Fulfillment den Punkt “Enable webhook call for this intent” aktiv zu setzen.

Dieser von uns angelegte Intent, erkennt finance, politics, technology, science und health als topic. Education, company und government wurden als Subtopics angelegt. Außerdem erkennt das Intent soweit alle Länder, da ein vorgefertigtes Entity für alle Länder verwendet wurde.

		4.1.3.2 Anlegen von Entitys
Entitys werden benötigt, um in einem Intent ein Thema zu erkennen. im Folgenden wird beschrieben, wie man ein Intent anlegen kann.

Um ein Entity anzulegen klickt man in der linken Menüleiste auf den Punkt Entites (s. Abb. 12). Als erstes wird dem Entity ein Name gegeben, welcher in unserem Fall Topic ist. wir haben hier die Topics financ, politic, tech, scien und health definiert. Für jedes Topic wurden mehrer mögliche Schreibweisen definiert. Im Anschluss kann im Intent auf dieses Entity verwiesen werden und dadurch die Themen erkannt werden, über die gesprochen werden möchte.

![Abb. 12: Entity anlegen](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilensteine/Meilenstein%203/BilderDoku/Dialog4.jpeg)

		4.1.3.3 Anlegen von Agents
Einen Agent benötigt man um Intents und Entitys anlegen zu können. Einen Agent kann man durchaus als Projekt bezeichnen. Das Anlegen wird im Folgenden beschrieben (s. Abb.13).	

![Abb. 13: Anlegen von Agents](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilensteine/Meilenstein%203/BilderDoku/Dialog6.jpeg) 

Um einen neuen Agent anzulegen, muss man in der linken Menüleiste das Dropdown Menü öffnen und unten auf “Create new Agent” klicken. Daraufhin öffnet sich folgendes Fenster (s. Abb. 14).

![Abb.14: Create new Agent](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilensteine/Meilenstein%203/BilderDoku/Dialog3.jpeg) 

Hier kann man den Agent benennen, die Sprache und die Zeitzone einstellen. Im Anschluss klickt man auch “Create” und der Agent ist erstellt.

	4.1.4 Elasticsearch
Bei diesem Projekt wurde auch mit dem Programm “Elasticsearch” gearbeitet. Dieses Programm ist als Suchmaschine zu verstehen welches Dokumente in einem NoSQL-Format (JSON) speichert. Elasticsearch bietet die Möglichkeit nach Dokumenten zu suchen und diese nach Relevanz sortiert zurück zu geben.

Suchanfragen werden als JSON-Dokumente über eine REST-Schnittstelle an Elasticsearch gesendet. Die Antwort von Elasticsearch mit den gefundenen Dokumenten erfolgt ebenfalls im JSON-Format.




**4.2 Installationsanleitung Testing**

 **1.Schritt: Elasticsearch**

 - Download von
   [https://www.elastic.co/de/downloads/elasticsearch](https://www.elastic.co/de/downloads/elasticsearch)
 - Datei entpacken Cmd starten und zum Ordner „bin“ im Elasticsearch-Ordner navigieren   
 -  "Elasticsearch.bat" ausführen

 **2.Schritt: ngrok**
 - Download von [https://ngrok.com/download](https://ngrok.com/download)
 - Datei entpacken
 - Exe-Datei ausführen
 - "ngrok http 5000" ausführen (s.Abb.15)
 
 ![Abb.15: nGrok http 500](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilensteine/Meilenstein%203/BilderDoku/NGrok.png)
 
 - Markierte URL kopierte oder aufschreiben

 **3.Schritt: Dialogflow**
 
 - Agent importieren:
 - Einstellungen
 - Import and Export
 - IMPORT FROM ZIP
 - Datei aus Git-Repository auswählen [Dialogflow Agent/MyCo.zip](Dialogflow%20Agent/MyCo.zip)
 - Webhook aktivieren:
 -  Fulfillment
 - Enable Webhook
 - Zuvor kopierte URL einfügen und "/webhook" ohne Leerzeichen dazwischen anhängen
 - speichern

 **4.Schritt: PyCharm**
 - Kontrollieren ob alle nötigen Packages installiert sind (siehe Rot unterstrichener "Import code". Ansonsten Pakete installieren
 - Elasticsearch_indexing.py ausführen
 - My_Co.py ausführen

**5. Schritt: Anfragen in Dialogflow stellen**




**4.3 UML-Diagramme**

Im folgenden Kapitel werden die erstellten Diagramme dargestellt. Die Diagramme wurden mit Hilfe von “StarUML” erstellt. Das erste Diagramm (s. Abb. 16 ) zeigt den Gesprächskontext.

![Abb.16:Gesprächskontext](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilensteine/Meilenstein%203/BilderDoku/Klassendiagramm%20Gespr%C3%A4chskontext.jpg)

Die folgende Abbildung (s. Abb.17 ) zeigt den Use Case “Sprachassistent”.

![Abb.17:Sprachassistent](https://github.com/georgerich/MyCo-Gruppe-3/blob/master/Meilensteine/Meilenstein%203/BilderDoku/Use%20Case%20Sprachassistent.jpg)


## 5.0 Zusammenfassung
Wir glauben das im aktuellen Reuters Testdatensatz der über Keras bezogen wird es unserer Ansicht nach keine andere Möglichkeit gibt als dies als Volltextsuche zu implementieren da der Datensatz nicht kategorisiert ist. Daher war dies die bestmöglichste Lösung für uns da wir uns für eine Suche entschieden haben die zum Datensatz passt und funktioniert.

**5.1 Ausblick**

Um das Projekt abzuschließen, fehlt nun noch die Umsetzung von Meilenstein 3. Hierbei liegt der Fokus insbesondere bei der Umsetzung des Projektes in Tensorflow und dafür ist der komplette kategorisierte Reuters Datensatz nötig.
