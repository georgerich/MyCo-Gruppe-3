from elasticsearch import Elasticsearch
from elasticsearch import helpers
from keras.datasets import reuters

term = ""

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

(x_train, y_train), (x_test, y_test) = reuters.load_data(num_words=None, test_split=0.2)
word_index = reuters.get_word_index()

print(len(x_train))
print(x_train[0])

index_to_word = {}
for key, value in word_index.items():
    index_to_word[value] = key
print(index_to_word)

i = 0
inhalt = [0 for x in range(len(x_train))]
for i in range(len(x_train)):
    try:
        string = ' '.join([index_to_word[x] for x in x_train[i]])
    except KeyError:
        print("Something went wrong")
    inhalt[i] = string
    # print(str(i) +" "+ inhalt[i])

body = []
j = 0
for j in range(len(x_train)):
    try:
        #body.append({'index': {'_index': 'could', '_type': 'doc', '_id': "'" + str(j) + "'"}})
        #body.append(inhalt[j])
        doc = {
            'id': j,
            'text': '\'' + inhalt[j] + '\''
        }
        res = es.index(index="test-index", doc_type='tweet', id=j, body=doc)
    except:
        print("something went wrong again")


