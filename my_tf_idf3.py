from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import pandas as pd

corpus = {"doc1": "Betty Botter bought some butter", "doc2": "But the butter’s bitter", "doc3": "The bitter butter makes the batter bitter"}

def process_tf_and_idf():
    cv = CountVectorizer(stop_words='english')
    x_traincv = cv.fit_transform(corpus.values())
    feature_names = cv.get_feature_names()
    corpus_index = [n for n in corpus]
    print("****TF********")
    print(feature_names)
    print(x_traincv.toarray())
    print("****TFIDF********")
    '''tf = pd.DataFrame(x_traincv.toarray(), index=feature_names, columns=corpus_index)
print(tf)'''
    tfidf = TfidfVectorizer(stop_words='english', analyzer='word')
    tfs = tfidf.fit_transform(corpus.values())
    feature_names = tfidf.get_feature_names()
    corpus_index = [n for n in corpus]
    print(feature_names)
    print(tfs.toarray())
    '''rows, cols = tfs.nonzero()
for row, col in zip(rows, cols):
    print((feature_names[col], corpus_index[row]), tfs[row, col])'''
    print("******TFIDF as a dataframe********")
    df = pd.DataFrame(tfs.T.todense(), index=feature_names, columns=corpus_index)
    print(df)

def process_consine_similarity(query):

    doc_tf_idf = TfidfVectorizer(stop_words='english', analyzer='word').fit_transform(corpus.values())
    query_tf_idf = TfidfVectorizer(stop_words='english', analyzer='word').fit(corpus.values())
    query_tf_idf = query_tf_idf.transform([query])

    cosine_similarities = cosine_similarity(query_tf_idf, doc_tf_idf).flatten()
    return cosine_similarities


if __name__ == '__main__':
    process_tf_and_idf()
    print("******cosine similarity********")
    print(process_consine_similarity("bitter butter in the batter"))
    print(process_consine_similarity("bitter batter"))