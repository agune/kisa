# -*- coding: utf-8 -*-
## 7000 word word2Vec example

from dataHandler.MysqlHandler import DataHandler
import gensim

import os
dbUser = os.environ["DB_USER"]
dbPw = os.environ["DB_PW"]

dataHandler = DataHandler("localhost", dbUser, dbPw, "kisa")

document = {}
termList = dataHandler.getTokenTitle(7000)

texts = []      # docuemnt text
ids = []	# document ids
for term in termList :
    if term[1] in document :
        document[term[1]].append(term[2])
    else:
        document[term[1]] = []
        document[term[1]].append(term[2])


for key, item in document.items() :
    texts.append(item)
    ids.append(key)



model = gensim.models.Word2Vec(texts, min_count=1)

print(model.most_similar(positive=['부정행위']))



