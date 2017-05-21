from gensim.models import word2vec
import pandas as pd

# import modules & set up logging
import gensim, logging

#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#sentences = [['first', 'sentence'], ['second', 'sentence']]
# train word2vec on the two sentences
#model = gensim.models.Word2Vec(sentences, min_count=1)

model = 0

def LoadData():
    df = pd.read_csv("reddit_worldnews_start_to_2016-11-22.csv")
    "".join(df[""])
    return word_freq

def LoadModel():
    #sentences = word2vec.Text8Corpus('text8')
    global model
    model = word2vec.Word2Vec(sentences, size=200)

def getSimilarWords(baseWord, pos):
    if (pos == 'UNK'):
        return list()
    else:
        x = model.most_similar([baseWord])
        return x