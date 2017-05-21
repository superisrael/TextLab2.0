from nltk.corpus import wordnet as wn
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from operator import itemgetter
import pandas as pd

def string_to_pos(str_pos):
    if (str_pos == 'ADJ'):
        return wn.ADJ
    elif str_pos == 'VERB':
        return wn.VERB
    elif str_pos == 'NOUN':
        return wn.NOUN

def tag(x):
    return pos_tag(word_tokenize(x))

def getWordStem(word):
    """
    """
    return SnowballStemmer("english").stem(word)

def getWordSynonyms(word, pos):
    """
    """
    synonymsSet = set()
    if (pos == 'UNK'):
        return list()
    else:
        for synset in wn.synsets(word, string_to_pos(pos)):
            for synWord in synset.lemma_names():
                if synWord != word:
                    synonymsSet.add(synWord)
        return list(synonymsSet)

def GetNiegbours(word, pos):
    """
    """
    synonymsSet = set()
    if (pos == 'UNK'):
        return list()
    else:
        for synset in wn.synsets(getWordStem(word), string_to_pos(pos)):
            for parent in synset.hypernyms():
                synonymsSet.add(parent)
                for brother in parent.hyponyms():
                    synonymsSet.add(brother.name().split('.')[0])
        return list(synonymsSet)

def GetChildren(word, pos):
    """
    """
    synonymsSet = set()
    if (pos == 'UNK'):
        return list()
    else:
        for synset in wn.synsets(getWordStem(word), string_to_pos(pos)):
            for brother in synset.hyponyms():
                synonymsSet.add(brother.name().split('.')[0])
        return list(synonymsSet)
