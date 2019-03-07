from gensim.models import Word2Vec,KeyedVectors
from gensim.models import word2vec
from nltk.tokenize import word_tokenize,sent_tokenize
sample = open('pos_tagged_words.txt','r')
s = sample.read()
#tokenize Sentences
temp = sent_tokenize(s)
#tokenize those sentences to words
a = []
for sent in temp:
	a.append(word_tokenize(sent))
#create model
model = word2vec.Word2Vec(a, workers = 4, size = 100, min_count = 1, window = 6,sg = 1)
model.train(temp, total_examples = len(temp), epochs=10)
#vocab size
print(len(model.wv.vocab))
#print vocab
#print(model.wv.vocab.keys())
print(model.wv.most_similar('japan/NOUN',topn = 5))
model_name = 'sense2vec'
model.wv.save_word2vec_format('model.bin' , binary = True )
