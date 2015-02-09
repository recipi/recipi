import sys
import re
from collections import Counter

import django
django.setup()

from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer

from recipi.food.models import Food


lemmatizer = WordNetLemmatizer()


def word_check(word_to_test):
    if (not wn.synsets(word_to_test)) or (len(word_to_test) < 3):
        return False
    else:
        return True


def simplify(y, reg):
    y = [x.lower() for x in y]
    y = [re.sub(reg, '', x) for x in y]
    y = [re.sub(r'&| f$', ' ', x) for x in y]
    y = [s.strip() for s in y]
    return y


ingredients = list(set(Food.objects.values_list('name', flat=True)))

clean_re = (
    r'&nbsp;|&#\d+;|\*|\%|\:|,.+|\(.+\)| \- .+|'
    r'\d.+?|\\.+| in .+| and .+| or .+| with .+|'
    r' at .+| into .+| as .+|<a href.+')

ingredients = simplify(ingredients, clean_re)

ingredients = list(set(ingredients))

# single words, main ingredients.
one_words = list(set(
    [lemmatizer.lemmatize(x.split()[0]) for x in ingredients
    if len(x.split()) == 1]
))

one_words = [x for x in one_words if word_check(x)]


simplified = dict(zip(one_words, one_words))

for x in ingredients:
    if not x in simplified:
        for w in x.split()[::-1]: # this starts from the last word, and goes backwards
            if lemmatizer.lemmatize(w) in simplified:
                simplified[x] = simplified[lemmatizer.lemmatize(w)]
                break
        if not x in simplified and len(x.split()) > 1:
            simplified[x] = x
        elif not x in simplified and len(x.split()) == 1:
            simplified[x] = None

import pprint

pprint.pprint(simplified)
