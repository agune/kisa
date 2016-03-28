from gensim import corpora, models
from dataHandler.MysqlHandler import DataHandler

import gensim


import os
dbUser = os.environ["DB_USER"]
dbPw = os.environ["DB_PW"]

dataHandler = DataHandler("localhost", dbUser, dbPw, "kisa")

document = {}
termList = dataHandler.getTokenTitle(3000)
index_to_keyword_mapping = {}

texts = []

for term in termList :
    if term[1] in document :
        document[term[1]].append(term[2])
    else:
        document[term[1]] = []
        document[term[1]].append(term[2])


for item in document.values() :
    texts.append(item)



dictionary = corpora.Dictionary(texts)

corpus = [dictionary.doc2bow(text) for text in texts]



ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word = dictionary, passes=20)


## TODO use ldamodel
print(ldamodel)

