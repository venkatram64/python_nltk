from nltk import PorterStemmer, WordNetLemmatizer, word_tokenize

"""
Lemma(lexicon headword) - the base form of a word
Dictionary-matched base form unlike the stem
Removing the suffixes
"""

line = "My name is Venkatram Veerareddy, technical architect.\n I am having 20 years of experience in "\
                          " Software industry working \nfrom applications to products by using \n" \
                          " C, C++, Java, Javascript and databases "\
                          " like Oracle, MS SQL Server, Postgres, MySQL and OrientDB."

tokens = word_tokenize(line)
porter = PorterStemmer()
pStems = [porter.stem(t) for t in tokens]
print(pStems)

print("************************************************")

lemmatizer = WordNetLemmatizer()
lemma = [lemmatizer.lemmatize(t) for t in tokens]
print(lemma)



