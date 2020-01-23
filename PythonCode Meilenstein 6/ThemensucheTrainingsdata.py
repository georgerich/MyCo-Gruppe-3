import xml.etree.ElementTree as ET
import glob
import os

import nltk
from nltk.tokenize import word_tokenize
from lxml import etree
from xml.dom import minidom

# Hier das verzeichnis angeben, indem nurnoch die 4 verschiedenen Ordner drinnen liegen
dir = os.getcwd()
i = 0

for file in glob.iglob(os.path.join(dir, '*/*.xml')):
    with open(file) as f:

        tree = ET.parse(file)
        root = tree.getroot()
        text = ""

        for node in tree.iter('text'):
            for elem in node.iter():
                if not elem.tag == node.tag:
                    text = text + elem.text + " "






        tokenizedtext = word_tokenize(text)
####Beispiel für ein Wort das gesucht werden mussJeweils die nichtverwendete Art mit # an jedem Zeilenanfang auskommentieren"
#        if 'Volkswagen' in tokenizedtext:
#            print('file: ' + file)
#            print(text)
#            print('----------------------------------------')
#            i = i + 1
#        else:
#            i = i + 1


####Beispiel für zwei Worte die gesucht werden sollen. Jeweils die nichtverwendete Art mit # an jedem Zeilenanfang auskommentieren"



        if 'Bundesbank' in tokenizedtext:
            if 'German' in tokenizedtext:
#                if 'Germany' in tokenizedtext:
                print('file: ' + file)
                print(text)
                print('----------------------------------------')

            i = i + 1
        else:
            i = i + 1
        if i> 10000:
            break
