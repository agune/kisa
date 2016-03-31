# -*- coding: utf-8 -*-


class DocumentUtil:

    # get document term matrix by vacab index count
    # vacab : vocabulary
    # docuemnts
    def get_document_term_matrix(self, vocab, documents):
        vocab_index = self._make_vocab_index(vocab)
        document_term_matrix = [self._make_term_matrix(vocab_index, document) for document in documents]
        return document_term_matrix

    def _make_term_matrix(self, vocab, document):
        vector = [0] * len(vocab)
        for word in document:
            vector[vocab[word]] += 1

        return vector

    def _make_vocab_index(self, vocab):
        vocab_index = {}
        index = 0
        for word in vocab:
            vocab_index[word] = index
            index += 1
        return vocab_index

    def make_vocab(self, docuemnts):
        word_set = {}

        for docuemnt in docuemnts:
            for word in docuemnt:
                word_set[word] = word

        index = 0

        vocab = [0] * len(word_set)

        for word in word_set.values():
            vocab[index] = word
            index += 1

        return vocab