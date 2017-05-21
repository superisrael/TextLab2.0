from operator import itemgetter
import pandas as pd
import WordNetInterface as syntactic
import word2vec as w2v

def buildFrequncyTable():
    excelFile = pd.ExcelFile("WordFrequency.xlsx")
    df = excelFile.parse("Sheet1")
    filterDF = df[(df['Part of speech'] == 'n') | (df['Part of speech'] == 'v') | (df['Part of speech'] == 'j')]
    X = filterDF[['Word', 'Dispersion']]
    word_freq = X.set_index(['Word']).T.to_dict()

    column_order = ["Dispersion"]
    for k in word_freq:
        word_freq[k] = [word_freq[k][column_name] for column_name in column_order]
        word_freq[k] = word_freq[k][0]
    return word_freq

def CreateItem(word, wordFreq):
    word_item = (word, 0.5)
    if word in wordFreq:
        word_item = (word, wordFreq[word])
    return  word_item

def POS_Map(tagging_pos):
    if (tagging_pos == 'JJ' or tagging_pos == 'JJS'):
        return 'ADJ'
    elif (tagging_pos == 'VB' or  tagging_pos =='VBP' or tagging_pos == 'VBG' or tagging_pos == 'VBD'):
        return 'VERB'
    elif (tagging_pos == 'NN' or tagging_pos == 'NNS'):
        return 'NOUN'
    else:
        return 'UNK'

def GetWordOptions(sentence):
    model = w2v.LoadModel()
    wordFreq = buildFrequncyTable()
    words = syntactic.word_tokenize(sentence)
    wordPOS = syntactic.tag(sentence)
    print (wordPOS)
    sentenceList = []
    i = 0
    for word in words:
        #wordSynonym = syntactic.getWordSynonyms(word, POS_Map(wordPOS[i][1]))

        wordSynonym = w2v.getSimilarWords(word, POS_Map(wordPOS[i][1]))
        print (wordSynonym)
        #wordSynonym = GetNiegbours(word, POS_Map(wordPOS[i][1]))

        #wordSynonym = GetChildren(word, POS_Map(wordPOS[i][1]))

        word_options = []
        for wordSyn in wordSynonym:
            word_options.append(CreateItem(wordSyn, wordFreq))

        word_options = sorted(word_options, key=itemgetter(1), reverse=True)[:3]

        word_options.append(CreateItem(word, wordFreq))
        sentenceList.append(word_options)
        i = i + 1
    print (sentenceList)
    return sentenceList

GetWordOptions("Wallmart cameras captured these terrifying photos")