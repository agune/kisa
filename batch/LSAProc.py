## 3000 word related document 예제 by LSA

from dataHandler.MysqlHandler import DataHandler
from analysis.lsa.vector_space import VectorSpace

import os
dbUser = os.environ["DB_USER"]
dbPw = os.environ["DB_PW"]

dataHandler = DataHandler("localhost", dbUser, dbPw, "kisa")


termList = dataHandler.getTokenTitle(3000)


## document format : {rss_id : [(id. rss_id, term ).(id. rss_id, term)]}
## ex) {11882: [(1, 11882, '6자수석'), (2, 11882, '평화협정')], 11883: [(3, 11883, '문체부')]}
document = {}

index_to_keyword_mapping = {}

for term in termList :

    if term[1] in document :
        document[term[1]].append(term)
    else:
        document[term[1]] = []
        document[term[1]].append(term)

    keywordIndex = dataHandler.getKeywordIndex(term[2])
    if len(keywordIndex) > 0:
        index_to_keyword_mapping[keywordIndex[0][0]] = term[2];

    else:
        index = dataHandler.insertKeywordIndex(term[2])
        index_to_keyword_mapping[index] = term[2];


vector_space = VectorSpace(document, index_to_keyword_mapping.values())

index = 0

doc_list = list(document.values())
for doc in doc_list:
    sim_list = vector_space.ralated(index)
    doc_index = 0
    for sim in sim_list:
        if sim > 0.4 and index != doc_index:
            dataHandler.insertRelatedDoc(doc[0][1], doc_list[doc_index][0][1])
        doc_index = doc_index + 1

    index = index +1


