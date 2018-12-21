from nltk.tokenize import LineTokenizer, SpaceTokenizer, TweetTokenizer
from nltk import word_tokenize

line = "My name is Venkatram Veerareddy, technical architect.\n I am having 20 years of experience in "\
                          " Software industry working \nfrom applications to products by using \n" \
                          " C, C++, Java, Javascript and databases "\
                          " like Oracle, MS SQL Server, Postgres, MySQL and OrientDB."

lTokenizer = LineTokenizer()
print("Line tokenizer output: ", lTokenizer.tokenize(line))

sTokenizer = SpaceTokenizer()
print("Space Tokenizer output: ", sTokenizer.tokenize(line))

print("Word Tokenizer output: ", word_tokenize(line))

tTokenizer = TweetTokenizer()
print("Tweet Tokenizer output: ", tTokenizer.tokenize("This is a coooool #dummysmiley: :-) :-P <3"))

