import nltk
from nltk.corpus import wordnet as wn

import matplotlib

woman = wn.synset('woman.n.01')
bed = wn.synset('ben.n.01')

print(woman.hypernyms())
woman_paths = woman.hypernym_paths()

for idx, path in enumerate(woman_paths):
    print('\n\nHypernym Path: ', idx + 1)
    for synset in path:
        print(synset.name(), ', ', end=' ')

types_of_beds = bed.hyponyms()
print('\n\n Types of beds(Hyponyms): ', types_of_beds)
print("********************")
print(sorted(set(lemma.name() for synset in types_of_beds for lemma in synset.lemmas())))













