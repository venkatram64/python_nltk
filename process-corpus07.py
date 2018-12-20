import nltk
from nltk.corpus import wordnet as wn

import matplotlib

type = 'n'
synsets = wn.all_synsets(type)

lemmas = []
for synset in synsets:
    for lemma in synset.lemmas():
        lemmas.append(lemma.name())

lemmas = set(lemmas)
print("Total distinct lemmas: ", len(lemmas))

count = 0
for lemma in lemmas:
    count = count + len(wn.synsets(lemma, type))

print("Total senses: ", count)
print("Average Polysemy of ", type, ': ', count/len(lemmas))





















