# This code by [ref](https://github.com/josephwilk/semanticpy) modify

from math import *
from analysis.lsa.transform import Transform
import functools

class TFIDF(Transform):

    def __init__(self, matrix):
        Transform.__init__(self, matrix)
        self.document_total = len(self.matrix)

    def transform(self):
        rows,cols = self.matrix.shape
        transformed_matrix = self.matrix.copy()
        for row in range(0, rows):
            word_total = functools.reduce(lambda x, y: x+y, self.matrix[row] )
            word_total = float(word_total)
            for col in range(0, cols):
                transformed_matrix[row,col] = float(transformed_matrix[row,col])
                if transformed_matrix[row][col] != 0:
                    transformed_matrix[row,col] = self._tf_idf(row, col, word_total)

        return transformed_matrix

    def _tf_idf(self, row, col, word_total):
        term_frequency = self.matrix[row][col] / float(word_total)
        inverse_document_frequency = log(abs(self.document_total / float(self._get_term_document_occurences(col))))
        return term_frequency * inverse_document_frequency

    def _get_term_document_occurences(self, col):
        term_document_occurrences = 0
        rows, cols = self.matrix.shape

        for n in range(0,rows):
            if self.matrix[n][col] > 0:
                term_document_occurrences +=1

        return term_document_occurrences


