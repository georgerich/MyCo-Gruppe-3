import glob
import json
import os
import xml.etree.ElementTree as ET
from tempfile import TemporaryFile

import numpy as np
import pandas as pd
from nltk import word_tokenize
from tensorflow import keras
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
dir = os.getcwd()

#Stopwords initiieren
stop_words = set(stopwords.words('english'))
stop_words2 = {'tell', 'something', 'know', 'let', 'show', 'talk', 'lets', 'lets', 'talk', 'information', 'give', 'want', 'learn', 'year', 'place', 'give', 'see', 'some', 'news', 'new'}
stopwords_new=stop_words.union(stop_words2)


#aktuell beim lokalen ablegen
data = pd.read_excel(os.path.join(dir, "Trainingsdaten", "Traingsdaten_komplett.xlsx"), header=None)

# verwenden wenn die lokale Datei im gleichen verzeichnis liegt
#data = pd.read_excel('Trainingsdaten_Christoph_Zeltwanger.xlsx', header=None)
dir = 'G:/chris/Nicht veränderte Daten/rcv1subsetKleinbuchstaben/19960820'
dir2 = 'G:/chris/Nicht veränderte Daten/rcv1subsetKleinbuchstaben/'

#Wordindex sollte ebenfalls in selber directory liegen
word_index = json.load(open("dict.json"))
# bilden eines umgekehrten Wordindex
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
#'''
# Array für Trainingdaten(Inputs) und Trainingslabels(Outputs) erzeugen
train_data = []
train_labels = []
array_tokenized_dokument=[]
array_dokumenten_namen=[]
for file in glob.iglob(os.path.join(dir2, '*/*.xml')):
    file = file[67:]
    array_dokumenten_namen.append(file)

train_data_einzel = []






# for file in glob.iglob(os.path.join(dir2, '*/*.xml')):
#     with open(file) as f:  # hier startet die Arbeit am Artikel
#         tree = ET.parse(file)
#         root = tree.getroot()
#         text = ""
#         for node in tree.iter('text'):
#             for elem in node.iter():
#                 if not elem.tag == node.tag:
#                     # print("{}: {}".format(elem.tag, elem.text))
#                     text = text + elem.text + "  "
#                     text = text.lower()  # nur Kleinbuchstaben
#         text = text.replace(", ", " ")  # Einige Zeichen werden ersetzt
#         text = text.replace("'", "")
#         text = text.replace(". ", " ")
#         text = text.replace("(", "")
#         text = text.replace(")", "")
#         text = text.replace(": ", "")
#         text = text.replace("\" ", "")
#         tokenized_dokument = word_tokenize(text)  # Liste mit den Worten eines Dokuments ['german', 'bundesbank']
#         # in der folgenden WHile Schleife wird ['german', 'bundesbank'] umgeformt, sodass die Zahlen aus dem WordIndex im Array enthalten sind
#         q = 0
#         while q < len(tokenized_dokument):
#             tokenized_dokument[q] = word_index[tokenized_dokument[q]]
#             q += 1
#         tokenized_dokument = tokenized_dokument[:200]
#         # in der folgenden While Schleife wird die länge einer Anfrage vereinheitlicht( Länge = 500). Sollte eine Anfrage kürzer sein, so wird diese mit "0" aufgefüllt
#         while len(tokenized_dokument) < 200:
#             tokenized_dokument = tokenized_dokument + [0]
#         array_tokenized_dokument.append(tokenized_dokument)
#
#
#
#
# array_tokenized_dokument =np.asarray(array_tokenized_dokument)
# np.save('Array_speichern', array_tokenized_dokument)

array_tokenized_dokument = np.load('Array_speichern.npy')
print("Array mit allen DOkumenten")
print(array_tokenized_dokument)
print(np.shape(array_tokenized_dokument))

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

    #mit jedem neuen Dokument werden die Trainingsdaten und Trainingslabels erweitert
    train_data.append(train_data_einzel)
    train_labels.append(data[2][z])

    z += 1 #hochzählen um an neuen Dokument in den Trainingsdaten zu gelangen

###########################################################################################################################################################################################################################################################################################
# print("Gesamte Trainingsdaten: ")
# print(train_data)
#
# print("Gesamte Trainingslabel: ")
# print(train_labels)
x_val = train_data[680:]
x_train = train_data[:680]

y_val = train_labels[680:]
y_train = train_labels[:680]
dir2 = os.getcwd()
data = pd.read_excel(os.path.join(dir2, "Testdaten", "Testdaten.xlsx"), header=None)

# verwenden wenn die lokale Datei im gleichen verzeichnis liegt
#data = pd.read_excel('testdaten_Christoph_Zeltwanger.xlsx', header=None)
dir2 = 'G:/chris/Nicht veränderte Daten/rcv1subsetKleinbuchstaben/19960820'


# Array für testingdaten(Inputs) und testlabels(Outputs) erzeugen
test_data = []
test_labels = []
# oberste Schleife: es wird jede "Zeile" der testdaten durchgegangen
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
    for file in glob.iglob(os.path.join(dir2, doc)):
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
            test_data_einzel=tokenized_anfrage+tokenized_dokument
            encoded_test_data_einzel= keras.preprocessing.sequence.pad_sequences([test_data_einzel],
                                                       maxlen=210)
            #print(encoded_test_data_einzel)


    # mit jedem neuen Dokument werden die testdaten und testlabels erweitert
    test_data.append(encoded_test_data_einzel)
    test_labels.append(data[2][z])
    z += 1 #hochzählen um an neuen Dokument in den testdaten zu gelangen


#########################################################################################################################################################################################################################################
# Arrays in ein Numpy-Array umformen
train_data = np.asarray(train_data)
train_labels = np.asarray(train_labels)
test_data = np.asarray(test_data)
test_labels = np.asarray(test_labels)
# print("Trainingsdaten: ")
# print(train_data)
# print("Trainingslabels: ")
# print(train_labels)
#'''

class_names = ['nicht relevant', 'relevant']



#Model erzeugen
model = keras.Sequential()
model.add(keras.layers.Embedding(88226, 150, input_length=510))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(150, activation="relu"))
model.add(keras.layers.Dense(2, activation="softmax"))

model.summary()
#
# print("train_data: ")
# print(train_data)
# print("shape(train_data):")
# print(np.shape(train_data))
# print("train_labels:")
# print(train_labels)
# print("shape(train_labels):")
# print(np.shape(train_labels))
#
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]) #Model kompilieren
#
#
#
fitModel = model.fit(x_train, y_train, epochs=3, batch_size=1, validation_data=(x_val, y_val), verbose=1) # Model trainieren
#
model.save("model.h5")


model = keras.models.load_model("model.h5")
model.summary()


# Beliebiger Input
user_imput="I want to talk about US Open tennis"
user_imput = user_imput.lower() #der gespeicherte String wird nurnoch aus Kleinbuchstaben bestehen
user_imput = user_imput.replace(", ", " ") #einige Zeichen werden herausgefiltert
user_imput = user_imput.replace("'", "")
user_imput = user_imput.replace(". ", " ")
user_imput = user_imput.replace("(", "")
user_imput = user_imput.replace(")", "")
user_imput = user_imput.replace(": ", "")
user_imput = user_imput.replace("\" ", "")
tokenized_user_input = word_tokenize(user_imput) # Liste mit den Anfrageworten ['german', 'bundesbank']
# in der folgenden WHile Schleife wird ['german', 'bundesbank'] umgeformt, sodass die Zahlen aus dem WordIndex im Array enthalten sind


filtered_sentence = [w for w in tokenized_user_input if not w in stopwords_new]
tokenized_user_input = filtered_sentence

print("Userinput (tokenized): ")
print(tokenized_user_input)


b = 0
while b < len(tokenized_user_input):
    tokenized_user_input[b] = word_index[tokenized_user_input[b]]
    b += 1
        # in der folgenden While Schleife wird die länge einer Anfrage vereinheitlicht( Länge = 10). Sollte eine Anfrage kürzer sein, so wird diese mit "0" aufgefüllt
while len(tokenized_user_input) < 10:
    tokenized_user_input = tokenized_user_input + [0]
print("Userinput (Tokenzied und mit einheitlicher Länge): " ,tokenized_user_input)

dir = 'G:/chris/Nicht veränderte Daten/rcv1subsetKleinbuchstaben/'
for file in glob.iglob(os.path.join(dir, '*/*.xml')):
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
        userinput_mit_dokument=tokenized_user_input+tokenized_dokument
        userinput_mit_dokument = np.asarray(userinput_mit_dokument)
        encode = keras.preprocessing.sequence.pad_sequences([userinput_mit_dokument],
                                                            maxlen=510)



        # #print(encode)
        predict = model.predict(encode)
        #(predict[0])
        #print([np.argmax(predict[0])])

        if [np.argmax(predict)] == [1]:
            print("File Directory: ")
            print(file)
            print("Kategorie: ")
            print([np.argmax(predict)])
            print("Predictionergebnis: ")
            print(predict)



