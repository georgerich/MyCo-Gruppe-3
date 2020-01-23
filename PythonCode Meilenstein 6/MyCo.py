import glob
import json
import os
import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
from nltk import word_tokenize
from tensorflow import keras
dir = os.getcwd()
print(dir)
#aktuell beim lokalen ablegen
data = pd.read_excel(os.path.join(dir, "Trainingsdaten", "Traingsdaten_komplett.xlsx"), header=None)

# verwenden wenn die lokale Datei im gleichen verzeichnis liegt
#data = pd.read_excel('Trainingsdaten_Christoph_Zeltwanger.xlsx', header=None)
dir = 'G:/chris/Nicht veränderte Daten/rcv1subsetKleinbuchstaben/19960820'
#Wordindex sollte ebenfalls in selber directory liegen
word_index = json.load(open("dict.json"))
# bilden eines umgekehrten Wordindex
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

# Array für Trainingdaten(Inputs) und Trainingslabels(Outputs) erzeugen
train_data = []
train_labels = []
# oberste Schleife: es wird jede "Zeile" der Trainingsdaten durchgegangen
z=1
while z < len(data):
    anfrage=data[0][z] # Der Inhalt der ersten Spalte (die Anfrage) wird durchgegangen
    anfrage = anfrage.lower() #der gespeicherte String wird nurnoch aus Kleinbuchstaben bestehen
    anfrage = anfrage.replace(", ", " ") #einige Zeichen werden herausgefiltert
    anfrage = anfrage.replace("'", "")
    anfrage = anfrage.replace(". ", " ")
    anfrage = anfrage.replace("(", "")
    anfrage = anfrage.replace(")", "")
    anfrage = anfrage.replace(": ", "")
    anfrage = anfrage.replace("\" ", "")
    tokenized_anfrage = word_tokenize(anfrage) # Liste mit den Anfrageworten ['german', 'bundesbank']
    # in der folgenden WHile Schleife wird ['german', 'bundesbank'] umgeformt, sodass die Zahlen aus dem WordIndex im Array enthalten sind
    r = 0
    while r < len(tokenized_anfrage):
        tokenized_anfrage[r] = word_index[tokenized_anfrage[r]]
        r += 1
    # in der folgenden While Schleife wird die länge einer Anfrage vereinheitlicht( Länge = 10). Sollte eine Anfrage kürzer sein, so wird diese mit "0" aufgefüllt
    while len(tokenized_anfrage) < 10:
        tokenized_anfrage = tokenized_anfrage + [0]
    #print("Anfrage: " ,tokenized_anfrage)

    doc= data[1][z] # Dokumentennummer der entsprechenden Zeile wird herausgesucht, um daraufhin den Text des Dokument einzulesen [6485.xml]
    for file in glob.iglob(os.path.join(dir, doc)):
        with open(file) as f: #hier startet die Arbeit am Artikel
            tree = ET.parse(file)
            root = tree.getroot()
            text = ""
            for node in tree.iter('text'):
                for elem in node.iter():
                    if not elem.tag == node.tag:
                        # print("{}: {}".format(elem.tag, elem.text))
                        text = text + elem.text + "  "
                        text = text.lower() # nur Kleinbuchstaben
            text = text.replace(", ", " ") #Einige Zeichen werden ersetzt
            text = text.replace("'", "")
            text = text.replace(". ", " ")
            text = text.replace("(", "")
            text = text.replace(")", "")
            text = text.replace(": ", "")
            text = text.replace("\" ", "")
            tokenized_dokument=word_tokenize(text) # Liste mit den Worten eines Dokuments ['german', 'bundesbank']
            # in der folgenden WHile Schleife wird ['german', 'bundesbank'] umgeformt, sodass die Zahlen aus dem WordIndex im Array enthalten sind
            q = 0
            while q < len(tokenized_dokument):
                tokenized_dokument[q] = word_index[tokenized_dokument[q]]
                q += 1
            tokenized_dokument = tokenized_dokument[:500]
            # in der folgenden While Schleife wird die länge einer Anfrage vereinheitlicht( Länge = 500). Sollte eine Anfrage kürzer sein, so wird diese mit "0" aufgefüllt
            while len(tokenized_dokument) < 500:
                tokenized_dokument = tokenized_dokument + [0]

            #hier wird die Liste der Anfrage mit der Liste des Dokuments verknüpft
            train_data_einzel=tokenized_anfrage+tokenized_dokument

    # mit jedem neuen Dokument werden die Trainingsdaten und Trainingslabels erweitert
    train_data.append(train_data_einzel)
    train_labels.append(data[2][z])
    z += 1 #hochzählen um an neuen Dokument in den Trainingsdaten zu gelangen

# Arrays in ein Numpy-Array umformen
train_data = np.asarray(train_data)
train_labels = np.asarray(train_labels)
print("Trainingsdaten: ")
print(train_data)
print("Trainingslabels: ")
print(train_labels)




#t=0
# while t < len(train_data):
#     # print(len(train_data))
#     # print(len(train_labels))
#     # print(train_data)
#     # print(train_labels)
#
#     print(data[0][t + 1])
#     print(data[1][t+1])
#     print(train_data[t])
#     print(train_labels[t])
#     t +=1

# Model erzeugen
model = keras.Sequential()
model.add(keras.layers.Embedding(88350, 240))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(240, activation="relu"))
model.add(keras.layers.Dense(1, activation="sigmoid"))

model.summary()


model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"]) #Model kompilieren



fitModel = model.fit(train_data, train_labels, batch_size=10000, epochs=50) # Model trainieren



