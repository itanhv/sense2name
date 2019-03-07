import gensim
from gensim.models import Word2Vec,KeyedVectors
from gensim.models import word2vec
model = KeyedVectors.load_word2vec_format("model.bin", binary=True)  # C bin format
print(model.most_similar('japan/NOUN', topn = 5))
#model.wv.save_word2vec_format('model.bin' , binary = True )
