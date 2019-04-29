from math import *
#http://dataaspirant.com/2015/04/11/five-most-popular-similarity-measures-implementation-in-python/

def euclidean_distance(x, y):
    return sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))


print(euclidean_distance([0, 3, 4, 5], [7, 6, 3, -1]))


def manhattan_distance(x, y):
    return sum(abs(a - b) for a, b in zip(x, y))

print(manhattan_distance([0, 3, 4, 5], [7, 6, 3, -1]))
print(manhattan_distance([10, 20, 10], [10, 20, 20]))


def square_rooted(x):
    return round(sqrt(sum([a * a for a in x])), 3)


def cosine_similarity(x, y):
    numerator = sum(a * b for a, b in zip(x, y))
    denominator = square_rooted(x) * square_rooted(y)
    return round(numerator / float(denominator), 3)

print(cosine_similarity([3, 45, 7, 2], [2, 54, 13, 15]))