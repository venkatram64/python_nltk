import nltk.classify.util

def word_feets(words):
    return dict([(word, True) for word in words])


p_words = ['good', 'excellent', 'marvelous', 'mindful','magnificient', 'memorable']
n_words = ['bad', 'ugly', 'sucks']
normal_words = ['ok', 'movie', 'the', 'actors', 'not', 'while'],

p_features = [(word_feets(pos), 'pos') for pos in p_words]
n_features = [(word_feets(neg), 'neg') for neg in n_words]
normal_features = [(word_feets(normal), 'normal') for normal in normal_words]

train_set = p_features + n_features + normal_features
model = nltk.NaiveBayesClassifier.train(train_set)

#prediction
neg = 0
pos = 0

sentence = "Excellent movie, I ever saw"
sentence = sentence.lower()
words = sentence.split(' ')

for word in words:
    result = model.classify(word_feets(word))
    if result == 'neg':
        neg += 1
    if result == 'pos':
        pos += 1


print('Positive: ' + str(float(pos)/len(words)))
print('Negative: ' + str(float(neg)/len(words)))