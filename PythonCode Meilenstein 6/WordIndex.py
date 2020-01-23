import xml.etree.ElementTree as ET
import glob
import os
from nltk.tokenize import word_tokenize
import json
###Directory, in welcher der Datensatz abgelegt ist
dir = os.getcwd()
i = 0
dict = {}
try:
    dict = json.load(open("dict.json"))
except:
    print("Es beginnt")

for file in glob.iglob(os.path.join(dir, '*/*.xml')):
    with open(file) as f:
        tree = ET.parse(file)
        root = tree.getroot()
        text = ""

        for node in tree.iter('text'):
            for elem in node.iter():
                if not elem.tag == node.tag:
                    # print("{}: {}".format(elem.tag, elem.text))
                    text = text + elem.text +"  "
        text = text.replace(", ", " ")
        text = text.replace("'", "")
        text = text.replace(". ", " ")
        text = text.replace("(", "")
        text = text.replace(")", "")
        text = text.replace(": ", "")
        text = text.replace("\" ", "")



        text = text.lower()

        tokenizedtext = word_tokenize(text)

        for n in tokenizedtext:

            if n not in dict:
                dict.update({n: 4+len(dict)})


        i = i + 1
        print('Dokument Nr: ' + str(i) + ' ' + str(i / 10000) + '%')

        # if i > 2:
        #      break
json.dump(dict, open("dict.json", 'w'))
