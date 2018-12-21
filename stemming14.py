from nltk import PorterStemmer, LancasterStemmer, word_tokenize

line = "My name is Venkatram Veerareddy, technical architect.\n I am having 20 years of experience in "\
                          " Software industry working \nfrom applications to products by using \n" \
                          " C, C++, Java, Javascript and databases "\
                          " like Oracle, MS SQL Server, Postgres, MySQL and OrientDB."

tokens = word_tokenize(line)
porter = PorterStemmer()
pStems = [porter.stem(t) for t in tokens]
print(pStems)

print("************************************************")

lancaster = LancasterStemmer()
lStems = [lancaster.stem(t) for t in tokens]
print(lStems)



