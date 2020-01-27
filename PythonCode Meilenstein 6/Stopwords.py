from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Spracheingabe
input="say me something about the drug war"

# setzen von Stopwords auf einglisch
stopWords=set (stopwords.words("english"))

# erstelle separate stopwords
stopWords2= "tell" , "something" , "know" , "let" , "show", "let´s" , "lets" , "give" , "see" , "some" , "news" , "new", "talk", "information" , "give" , "want" , "learn" , "year" , "place" , "say"

# Ausgabe des eigentlichen input
print (input)

# Ausgabe der einglischen Stopwords
print (stopWords)

# Ausgabe der eigen erstellten Stopwords
print (stopWords2)

words = word_tokenize(input)

#Filterung
ausgabeGefiltert= []

for x in words:
    if x not in stopWords2 and x not in stopWords:
        ausgabeGefiltert.append(x)

# Ausgabe des gefilterten input
print (ausgabeGefiltert)