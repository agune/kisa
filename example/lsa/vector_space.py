from numpy import dot
from numpy.linalg import norm
from LSA import LSA
from tfidf import TFIDF
import functools

class VectorSpace:
    collection_of_document_term_vectors = []
    vector_index_to_keyword_mapping = []

    parser = None

    def __init__(self, documents = [], transforms = [TFIDF, LSA]):
        self.collection_of_document_term_vectors = []
        #self.parser = Parser()
        if len(documents) > 0:
            self._build(documents, transforms)

    def _build(self, documents, transforms):
        self.vector_index_to_keyword_mapping = self._get_vector_keyword_index(documents)
        matrix = [self._make_vector(document) for document in documents]
        matrix = functools.reduce(lambda matrix, transform: transform(matrix).transform(), transforms, matrix)
        
        self.collection_of_document_term_vectors = matrix

    def _get_vector_keyword_index(self, document_list):
         # skip stop word check
         vocabulary_list = []
         for document in document_list:
             vocabulary_list.extend(document.split(" "))

         unique_vocabulary_list = self._remove_duplicates(vocabulary_list)
         vector_index={}
         offset=0
         for word in unique_vocabulary_list:
             vector_index[word] = offset
             offset += 1
         return vector_index  #(keyword:position)

    def _remove_duplicates(self, list):
        """ remove duplicates from a list """
        return set((item for item in list))

    def _make_vector(self, word_string):
        vector = [0] * len(self.vector_index_to_keyword_mapping)
        word_list = word_string.split(" ")
        ## skip stop word check

        for word in word_list:
            vector[self.vector_index_to_keyword_mapping[word]] += 1;
        
        return vector

    def _cosine(self, vector1, vector2):
        return float(dot(vector1, vector2) / (norm(vector1) * norm(vector2)))

    def _build_query_vector(self, term_list):
        query = self._make_vector(" ".join(term_list))
        return query

    def search(self, searchList):
        queryVector = self._build_query_vector(searchList)

        ratings = [self._cosine(queryVector, document_vector) for document_vector in self.collection_of_document_term_vectors]
        ratings.sort(reverse = True)
        return ratings

    def ralated(self, document_id):
        ratings = [self._cosine(self.collection_of_document_term_vectors[document_id], document_vector) for document_vector in self.collection_of_document_term_vectors]
        ratings.sort(reverse = True)
        return ratings
