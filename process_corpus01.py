import nltk
from nltk.corpus import reuters

#nltk.download()


files = reuters.fileids()
print(files)

print("*********************")

words16097 = reuters.words(['test/16097'])
print(words16097)


print("*********************")

words20 = reuters.words(['test/16097'])[:20]
print(words20)

print("***********List of Topics**********")

reutersGeneres = reuters.categories()
print(reutersGeneres)

print("******Categories***********")
for w in reuters.words(categories=['bop','cocos']):
    print(w + '  ', end=' ')
    if w is '.':
        print()