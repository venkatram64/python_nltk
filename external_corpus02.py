#http://www.cs.cornell.edu/people/pabo/movie%2Dreview%2Ddata/

from nltk.corpus import CategorizedPlaintextCorpusReader
from random import randint

reader = CategorizedPlaintextCorpusReader(r'mix20_rand700_tokens_cleaned/tokens', r'.*\.txt', cat_pattern=r'(\w+)/*')
print(reader.categories())
print(reader.fileids())

posFiles = reader.fileids(categories='pos')
negFiles = reader.fileids(categories='neg')

fileP = posFiles[randint(0, len(posFiles) - 1)]
fileN = negFiles[randint(0, len(negFiles) - 1)]

print(fileN)
print(fileP)

for w in reader.words(fileP):
    print(w + ' ', end='')
    if w is '.':
        print()

for w in reader.words(fileN):
    print(w + ' ', end='')
    if w is '.':
        print()

