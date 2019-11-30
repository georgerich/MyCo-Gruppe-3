# import flask dependencies
from flask import Flask, request, make_response, jsonify, render_template
from datetime import datetime
import json

from elasticsearch import Elasticsearch

# initialize the flask app
app = Flask(__name__)


# default route
@app.route('/')
def index():
    return render_template('index.html')


# function for responses
def results():
    es = Elasticsearch()
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    action = req.get('queryResult').get('action')
    print(action)
    print(req)
    topic = req.get('queryResult').get('parameters').get('Topic')
    geocountry = str(req.get('queryResult').get('parameters').get('geo-country'))
    subtopic = req.get('queryResult').get('parameters').get('Subtopic')
    topic1 = req.get('queryResult').get('parameters').get('Topic1')
    timestamp = datetime.now()
    term = "\"" + topic +" "+" "+ geocountry+" "+" "+subtopic+ "\""
    print(term)
    if term is not None:
        resp = es.search(index="test-index", body={
            "size": 10,
            "query": {

                "bool": {
                    "must": {
                        "multi_match": {
                            "type": "best_fields",
                            "query": term,
                            "fields": ["text"]

                        }
                    }
                }

            }

        })


    print(resp)
    print('topic: ' + topic)
    print('geo-location: ' + geocountry)
    print('Subtopic: ' + subtopic)
    print('topic 1: ' + topic1)
    print('timestamp: ' + str(timestamp))

    # Letzen Aufruf der Topics Finden

    lasttime = ""
    with open('data.json', 'r') as file:
        data = json.load(file)
        for person in data['history']:
            # print(person)
            if person['topic'] == topic:
                lasttime = "Zum letzten mal wurde das Thema gesucht am: " + person['timestamp']
                i = (person['id'])

    # Historie anlegen
    with open('data.json', "r") as json_file:
        data = json.load(json_file)

    print(data)
    lenght = len(data['history'])
    data['history'].append(
        {"id": lenght + 1, "topic": topic, "geocountry": geocountry, "subtopic": subtopic, "topic1": topic1,
         "timestamp": str(timestamp)})
    print(data)
    print(len(data['history']))
    with open('data.json', 'w') as file:
        json.dump(data, file)


        # return a fulfillment response
    #return {'fulfillmentText': 'you where looking for topic: ' + topic + '\n and topic 1: ' + topic1 + '\n and Subtopic: ' + subtopic + ' in: ' + geocountry}
    returntext =""
    for doc in resp['hits']['hits']:
        #print('document '+str(doc['_source']["id"])+': '+doc['_source']['text'])
        returntext = returntext + 'document '+str(doc['_source']["id"]) + ': '+str(doc['_source']['text'])
    #print(resp['hits']['hits'])
    text = '{'+returntext +'}'
    print(text)
    return {'fulfillmentText': lasttime+" Dokumente passend zur Anfrage sind: "+ returntext}




# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))


# run the app
if __name__ == '__main__':
    app.run(debug=True)
