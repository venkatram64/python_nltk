import nltk
from nltk.corpus import gutenberg



"""
Elaborate the usage of Frequency Distribution:
Within the context of stopwords
"""

print(gutenberg.fileids())
print("*******************bible*************************")
gb_words = gutenberg.words('bible-kjv.txt')
words_filtered = [e.lower() for e in gb_words if len(e) >= 3]
print(words_filtered)
print("*******************stopwords*************************")
stopwords = nltk.corpus.stopwords.words('english')
words = [w for w in words_filtered if w.lower() not in stopwords]
print(words)
print("*******************frequency 1*************************")
fdist = nltk.FreqDist(words)
fdist2 = nltk.FreqDist(gb_words)
print(fdist.most_common(10))
print("*******************frequency 2*************************")
print(fdist2.most_common(10))

