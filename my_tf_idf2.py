import pandas as pd
import math
import nltk
from nltk.corpus import stopwords
import re, math
from collections import Counter

#https://www.youtube.com/watch?v=hXNbFNCgPfY

'''
tf(w) = Number of times the word appears in a document/Total number of words in a document

idf(w) = log(Total Number of documents/Number of documents that contains word w)

The tfidf score of a word, w is  tf(w) * idf(w)
'''
def computeTF(wordDict, doc):
    tfDict = {}
    bow = doc
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict

def computeIDF(docList):
    idfDict = {}
    N = len(docList)

    #counts the number of document tht contain a word w
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    #print("1. compute idf")
    #print(idfDict)
    #print("2")
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1

    #divide N by denominator above, take the log of that
    for word, val in idfDict.items():
        idfDict[word] = math.log(N/float(val))

    return idfDict

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val * idfs[word]
    return tfidf

def convertToDic(wordSet, docA, docB, docC):
    #create dictionaries to keep word count
    wordDictA = dict.fromkeys(wordSet, 0)
    #print(wordDictA)
    wordDictB = dict.fromkeys(wordSet, 0)
    #print(wordDictB)
    wordDictC = dict.fromkeys(wordSet, 0)
    #print(wordDictC)
    #count the words in bags
    bowA = docA
    bowB = docB
    bowC = docC

    for word in bowA:
        wordDictA[word] += 1

    for word in bowB:
        wordDictB[word] += 1

    for word in bowC:
        wordDictC[word] += 1

    df = pd.DataFrame([wordDictA, wordDictB, wordDictC])
    print("***document frequency")
    print(df.to_string())

    return wordDictA, wordDictB, wordDictC


def combine_docs(docs):
    doc_set = set()
    for index, doc in enumerate(docs):
        if index == 0:
            doc_set = set(doc)
        else:
            doc_set = doc_set.union(set(doc))

    return doc_set


def normalize_bow(words):

    ws = []
    words = words.split(" ")
    #word_lemma = [wln.lemmatize(word) for word in words]
    st = [stemmer.stem(word) for word in words]
    for word in st:
        if word.lower() not in stop_words:
            ws.append(word)
    return ws


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

if __name__ == '__main__':
    WORD = re.compile(r'\w+')
    doc1 = "Betty botter bought some butter"
    doc2 = "But the butter bitter"
    doc3 = "The bitter butter makes the batter bitter"
    stop_words = set(stopwords.words('english'))
    wln = nltk.WordNetLemmatizer()
    stemmer = nltk.PorterStemmer()

    docA = normalize_bow(doc1)
    print(docA)
    docB = normalize_bow(doc2)
    print(docB)
    docC = normalize_bow(doc3)
    print(docC)
    wordSet = combine_docs([docA, docB, docC])

    wordDictA, wordDictB, wordDictC = convertToDic(wordSet, docA, docB, docC)

    print("***term frequency for doc1")
    tfBowA = computeTF(wordDictA, docA)
    print(tfBowA)

    print("***term frequency for doc2")
    tfBowB = computeTF(wordDictB, docB)
    print(tfBowB)

    print("***term frequency for doc2")
    tfBowC = computeTF(wordDictC, docC)
    print(tfBowC)

    print("***inverse document frequency")
    idfs = computeIDF([wordDictA, wordDictB, wordDictC])
    print(idfs)

    print("******tfidf*******")
    tfidfBowA = computeTFIDF(tfBowA, idfs)
    print(tfidfBowA)
    tfidfBowB = computeTFIDF(tfBowB, idfs)
    print(tfidfBowB)
    tfidfBowC = computeTFIDF(tfBowC, idfs)
    print(tfidfBowC)

    '''Above tfidfBowA, tfidfBowB will be printed in pandas dataframe'''
    print("******tfidf in different way of representation*******")
    df = pd.DataFrame([tfidfBowA, tfidfBowB, tfidfBowC])

    print(df.to_string())