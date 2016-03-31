# -*- coding: utf-8 -*-

## 7000 word related topic 예제 by LDA

from dataHandler.MysqlHandler import DataHandler
from analysis.util.DocumentUtil import DocumentUtil
import numpy as np
import lda
import os
dbUser = os.environ["DB_USER"]
dbPw = os.environ["DB_PW"]

dataHandler = DataHandler("localhost", dbUser, dbPw, "kisa")

document = {}
termList = dataHandler.getTokenTitle(7000)

texts = []      # docuemnt text
ids = []        # document rss id
for term in termList :
    if term[1] in document :
        document[term[1]].append(term[2])
    else:
        document[term[1]] = []
        document[term[1]].append(term[2])


for key, item in document.items() :
    texts.append(item)
    ids.append(key)

## manual implement document term matrix and vocabulary
## TODO IDF & stop word check
documentUtil = DocumentUtil()
vocab = documentUtil.make_vocab(texts)
docuemnt_term_matrix = documentUtil.get_document_term_matrix(vocab, texts)

## init LDA model
model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)

#train model
model.fit(np.asarray(docuemnt_term_matrix))
topic_word = model.topic_word_
n_top_words = 8

## check init topic model
vocab2 = lda.datasets.load_reuters_vocab()
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))


#check document topic and related document by topic
doc_topic = model.doc_topic_
relate_d = {}
for i in range(len(texts)):
    dataHandler.insertRelatedTopic(ids[i], str(doc_topic[i].argmax()))
    print("{} (top topic: {})".format(texts[i], doc_topic[i].argmax()))