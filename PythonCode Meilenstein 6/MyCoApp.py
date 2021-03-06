from flask import Flask, request, make_response, jsonify, render_template
import datetime
import xml.etree.ElementTree as ET
import json
import glob
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
from tensorflow import keras

word_index = json.load(open("dict.json"))
ergebnisliste = []
querytext = ''
globaltext = ''
textliste = []
#trainiertes Model laden.
model = keras.models.load_model("model.h5")
model.summary()

# initialize the flask app
app = Flask(__name__)


def results():
    global ergebnisliste
    ergebnisliste = []
    print('Start')
    # build a request object
    req = request.get_json(force=True)
    # Stopwords und Wörter aus der Phrase der Eingabe definieren
    stopWords = set(stopwords.words("english"))

    stopWords2 = "tell", "something", "know", "let", "show", "let´s", "lets", "give", "see", "some", "news", "new", \
                 "talk", "information", "give", "want", "learn", "year", "place", "say"
    eingabeGefiltert = []
    global querytext
    querytext = req.get('queryResult').get('queryText')
    anfrage = querytext
    anfrage = anfrage.lower()  # der gespeicherte String wird nurnoch aus Kleinbuchstaben bestehen
    anfrage = anfrage.replace(", ", " ")  # einige Zeichen werden herausgefiltert
    anfrage = anfrage.replace("'", "")
    anfrage = anfrage.replace(". ", " ")
    anfrage = anfrage.replace("(", "")
    anfrage = anfrage.replace(")", "")
    anfrage = anfrage.replace(": ", "")
    anfrage = anfrage.replace("\" ", "")
    tokenized_anfrage = word_tokenize(anfrage)

    #oben definierte Stopwörter und Phrasen entfernen
    for x in tokenized_anfrage:
        if x not in stopWords2 and x not in stopWords:
            eingabeGefiltert.append(x)
    b = 0
    while b < len(eingabeGefiltert):
        eingabeGefiltert[b] = word_index[eingabeGefiltert[b]]
        b += 1
        # in der folgenden While Schleife wird die länge einer Anfrage vereinheitlicht( Länge = 10). Sollte eine Anfrage kürzer sein, so wird diese mit "0" aufgefüllt
    while len(eingabeGefiltert) < 10:
        eingabeGefiltert = eingabeGefiltert + [0]
    print("Anfrage (Tokenzied): ", eingabeGefiltert)

    dir = 'D:/Downloads/rcv1/rcv/'
    for file in glob.iglob(os.path.join(dir, '*/*.xml')):
        if isDocRelevant(file, eingabeGefiltert) == "yes":
            ergebnisliste.append(file)
            textliste.append(globaltext)
            if len(ergebnisliste) > 10:
                break
            print(ergebnisliste)
            print(len(ergebnisliste))

    # return {'fulfillmentText': "Die Antwort auf die Eingabe wird auf \"http://localhost:5000/\" ausgegeben"}


def isDocRelevant(file, tokenized_anfrage):

    with open(file):  # hier startet die Arbeit am Artikel
        print(file)
        tree = ET.parse(file)
        global globaltext
        globaltext = ''
        text = ""
        # Inhalte des geladenen Dokuments laden
        for node in tree.iter('text'):
            for elem in node.iter():
                if not elem.tag == node.tag:
                    # print("{}: {}".format(elem.tag, elem.text))
                    text = text + elem.text + "  "
                    globaltext = globaltext + elem.text + " "
                    text = text.lower()  # nur Kleinbuchstaben

        text = text.replace(", ", " ")  # Einige Zeichen werden ersetzt
        text = text.replace("'", "")
        text = text.replace(". ", " ")
        text = text.replace("(", "")
        text = text.replace(")", "")
        text = text.replace(": ", "")
        text = text.replace("\" ", "")

        tokenized_dokument = word_tokenize(text)  # Liste mit den Worten eines Dokuments ['german', 'bundesbank']
        # print(tokenized_dokument)
        # in der folgenden WHile Schleife wird ['german', 'bundesbank'] umgeformt,
        # sodass die Zahlen aus dem WordIndex im Array enthalten sind
        q = 0
        while q < len(tokenized_dokument):
            tokenized_dokument[q] = word_index[tokenized_dokument[q]]
            q += 1
        tokenized_dokument = tokenized_dokument[:200]
        # in der folgenden While Schleife wird die länge einer Anfrage vereinheitlicht( Länge = 200).
        # Sollte eine Anfrage kürzer sein, so wird diese mit "0" aufgefüllt

        while len(tokenized_dokument) < 200:
            tokenized_dokument = tokenized_dokument + [0]

        # hier wird die Liste der Anfrage mit der Liste des Dokuments verknüpft
        test_data_einzel = tokenized_anfrage + tokenized_dokument
        test_data_einzel = np.asarray(test_data_einzel)
        encode = keras.preprocessing.sequence.pad_sequences([test_data_einzel],
                                                            maxlen=210)

        # #print(encode)
        predict = model.predict(encode)
    relevant = 'no'
    if [np.argmax(predict)] == [1]:  # Vergleichen ob das relevant flag gesetzt wurde
        relevant = 'yes'
    return relevant


# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    print(datetime.datetime.now(), 'Webhook wurde ausgelöst')
    global ergebnisliste
    ergebnisliste = []
    global textliste
    textliste = []
    results()
    # return response
    return make_response(
        jsonify({'fulfillmentText': "Die Antwort auf die Eingabe wird auf \"http://localhost:5000/\" ausgegeben"}))


# default route
@app.route('/')
def index():
    print(datetime.datetime.now(), 'Seite wurde upgedatet')
    global ergebnisliste
    global textliste
    return render_template('index.html', list=ergebnisliste, text=textliste, begriff=querytext)


# run the app
if __name__ == '__main__':
    app.run(debug=True)
