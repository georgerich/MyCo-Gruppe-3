from flask import Flask, request, make_response, jsonify, render_template
import datetime
import xml.etree.ElementTree as ET
from nltk.tokenize import word_tokenize
import json
import glob
import os

word_index = json.load(open("dict.json"))

# initialize the flask app
app = Flask(__name__)


# default route
@app.route('/')
def index():
    return 'Hello World!'


def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    # action = req.get('queryResult').get('action')
    # print(action)
    # print(req)
    # topic = req.get('queryResult').get('parameters').get('Topic')
    # geocountry = str(req.get('queryResult').get('parameters').get('geo-country'))
    # subtopic = req.get('queryResult').get('parameters').get('Subtopic')
    # topic1 = req.get('queryResult').get('parameters').get('Topic1')
    # print(topic1,subtopic,geocountry,topic)


    querytext = req.get('queryResult').get('queryText')
    print(querytext)

    suche(querytext)

    return {'fulfillmentText': "Die Antwort auf die Eingabe wird auf \"http://localhost:5000/\" ausgegeben"}

list =[]

def suche(eingabe):
    for file in glob.iglob(os.path.join(dir, '*/*.xml')):
        if isDocRelevant(file, eingabe)== "yes":
            list.append(file)


def  isDocRelevant(doc, eingabe):

    relevant = 'yes'
    return relevant


# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))


# run the app
if __name__ == '__main__':
    app.run(debug=True)
