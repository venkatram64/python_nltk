from nltk.metrics.distance import edit_distance




"""
How to handle a typical text analytics problem

http://www.english-for-students.com/
"""


story1 = """This site provides a large collection of English as a Second Language (ESL) tools & resources for students, 
teachers, learners and academics. Browse all the pages and find useful links and plenty of information.
Did you realize that over a two billion people in the world now speak this language? This figure is ever growing. 
It is the language of globalization. It's the language of international business and politics. 
It is the primary language used for most computers and for the inner workings of the Internet.
It is the dominant international language in communications, science, aviation, entertainment, 
radio and diplomacy. It is an important tool for operating on the world stage. The ability to speak and understand this 
language is mandatory in certain fields, professions and occupations. In fact, it is so widely spoken. 
It is referred to as the """

story2 = """Here is something which I am sure that any student will readily understand. Good and bad habits, 
once formed, are difficult to undo. It is hoped that the things which you learn in connection with reading, 
speaking and pronouncing English will be correct, because psychologists tell us that if you do a thing a certain 
way three times in succession, a habit will be formed which will be difficult to undo. After all, we may be 
intellectually superior to other animal species, but we are basically animals and you will find that if you are 
training a dog, cat, horse etc, the same principles will apply. Perhaps you may give your pet dog a treat if they 
have done something the way you want them to do it three times, but usually, after that they will continue using 
the habit which they have now acquired without even thinking about it."""

story1 = story1.replace(",", "").replace("\n", "").replace(".", '').replace('"', '').replace("!", "").replace("?", "").casefold()
story2 = story2.replace(",", "").replace("\n", "").replace(".", '').replace('"', '').replace("!", "").replace("?", "").casefold()


story1_words = story1.split(" ")
print("First Story words: ", story1_words)
story2_words = story2.split(" ")
print("Second Story words: ", story2_words)

story1_vocab = set(story1_words)
print("First Story Vocabulary: ", story1_vocab)
story2_vocab = set(story2_words)
print("Second Story Vocabulary: ", story2_vocab)

common_vocab = story1_vocab & story2_vocab
print("Common Vocabulary: ", common_vocab)



