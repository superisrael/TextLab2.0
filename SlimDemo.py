from nltk.corpus import wordnet as wn
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
import pandas as pd

def getWordStem(word):
    """
    """
    return SnowballStemmer("english").stem(word)

def getWordSynonyms(word, pos):
    """
    """
    synonymsSet = set()

    for synset in wn.synsets(word, pos):
        for synWord in synset.lemma_names():
            if synWord != word:
                synonymsSet.add(synWord)
    return list(synonymsSet)

def buildFrequncyTable():
    excelFile = pd.ExcelFile("WordFrequency.xlsx")
    df = excelFile.parse("Sheet1")
    #df = [df['Dispersion'] < 0.98]
    filterDF = df[(df['Part of speech'] == 'n') | (df['Part of speech'] == 'v') | (df['Part of speech'] == 'j')]
    X = filterDF[['Word', 'Dispersion']]
    word_freq = X.set_index(['Word']).T.to_dict()
    return word_freq

def CreateItem(word, wordFreq):
    word_item = (word, 0.5)
    if word in wordFreq:
        word_item = (word, wordFreq[word])
    return  word_item

def GetWordOptions(sentence):
    wordFreq = buildFrequncyTable()
    words = word_tokenize(sentence)
    sentenceList = []
    for word in words:
        stemWord = getWordStem(word)
        wordSynonym = getWordSynonyms(word, wn.NOUN) + getWordSynonyms(word, wn.ADJ) + getWordSynonyms(word, wn.VERB)
        word_options = []

        word_options.append(CreateItem(word, wordFreq))
        for wordSyn in wordSynonym:
            word_options.append(CreateItem(wordSyn, wordFreq))
        sentenceList.append(word_options)
    print (sentenceList)
    return sentenceList

GetWordOptions("The funny clown of the world is on the screens")