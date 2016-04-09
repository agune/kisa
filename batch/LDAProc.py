# -*- coding: utf-8 -*-

## 7000 word related topic 예제 by LDA

from dataHandler.MysqlHandler import DataHandler
from analysis.util.DocumentUtil import DocumentUtil
from gensim import corpora, models
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


# create corpus and dictionary
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# learn lda model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=500, id2word = dictionary, passes=20)

#example
#print(ldamodel.print_topics(num_topics=20, num_words=7))
#lda = ldamodel[dictionary.doc2bow(texts[0])]
#print(lda[0][0])
#print(ldamodel.print_topic(lda[0][0]))
#print(texts[0])


dataHandler2 = DataHandler("localhost", dbUser, dbPw, "kisa")

#check document topic and related document by topic
for i in range(len(texts)):
	lda = ldamodel[dictionary.doc2bow(texts[i])]
	if lda :
		dataHandler2.insertRelatedTopic(ids[i], str(lda[0][0]))
