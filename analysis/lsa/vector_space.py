# This code by [ref](https://github.com/josephwilk/semanticpy) modify

from numpy import dot
from numpy.linalg import norm
from analysis.lsa.LSA import LSA
from analysis.lsa.tfidf import TFIDF
import functools

class VectorSpace:
    collection_of_document_term_vectors = []
    vector_index_to_keyword_mapping = []

    parser = None

    def __init__(self, documents = {}, keyword_index = [], transforms = [TFIDF, LSA]):
        self.collection_of_document_term_vectors = []
        self.vector_index_to_keyword_mapping = self._get_vector_keyword_index(keyword_index)
        if len(documents) > 0:
            self._build(documents, transforms)

    def _build(self, documents, transforms):
        matrix = [self._make_vector(document) for document in documents.values()]
        matrix = functools.reduce(lambda matrix, transform: transform(matrix).transform(), transforms, matrix)
        self.collection_of_document_term_vectors = matrix


    def _remove_duplicates(self, list):
        """ remove duplicates from a list """
        return set((item for item in list))

    def _make_vector(self, document):
        vector = [0] * len(self.vector_index_to_keyword_mapping)
        for word in document:
            vector[self.vector_index_to_keyword_mapping[word[2]]] += 1

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
    #    ratings.sort(reverse = True)
        return ratings



    def _get_vector_keyword_index(self, kewrod_list):
        # skip stop word check
        unique_vocabulary_list = self._remove_duplicates(kewrod_list)
        vector_index={}
        offset=0
        for word in unique_vocabulary_list:
            vector_index[word] = offset
            offset += 1
        return vector_index  #(keyword:position)
