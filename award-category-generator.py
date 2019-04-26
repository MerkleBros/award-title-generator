import nltk
from nltk.corpus import wordnet as wn

import random

nouns = [synset.lemmas()[0].name() for synset in list(wn.all_synsets(wn.NOUN))]
adjectives = [synset.lemmas()[0].name() for synset in list(wn.all_synsets(wn.ADJ))]


def award_category():
    awardy_namey = random.choice(nouns)
    awardy_descripty = random.choice(adjectives)
    return awardy_descripty+" "+awardy_namey

for i in range(100):
    print(award_category())
