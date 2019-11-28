# import flask dependencies
from flask import Flask, request, make_response, jsonify
from datetime import datetime

# initialize the flask app
app = Flask(__name__)


# default route
@app.route('/')
def index():
    return 'Hello World!'


# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    action = req.get('queryResult').get('action')
    print(action)
    print(req)
    topic = req.get('queryResult').get('parameters').get('Topic')
    geocountry = req.get('queryResult').get('parameters').get('geo-country')
    subtopic = req.get('queryResult').get('parameters').get('Subtopic')
    topic1 = req.get('queryResult').get('parameters').get('Topic1')
    timestamp = datetime.now()

    print('topic: ' + topic)
    print('geo-location:' + geocountry)
    print('Subtopic: ' + subtopic)
    print('topic 1: ' + topic1)
    print('timestamp: ' + str(timestamp))

    # return a fulfillment response
    return {
        'fulfillmentText': 'you where looking for topic: ' + topic + '\n and topic 1: ' + topic1 + '\n and Subtopic: ' + subtopic + ' in: ' + geocountry}


# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))


# run the app
if __name__ == '__main__':
    app.run(debug=True)
