
import gensim
sentences = [['남자', '왕'], ['여자', '여왕']]
model = gensim.models.Word2Vec(sentences, min_count=1)

print(model.most_similar(positive=['여자', '여왕'], negative=['남자']))

