import re
import difflib
import heapq

import textblob

from recipi.food.models import Food


def match_ingredient(ingredient, n=10, cutoff=0.3):
    ingredients = sorted([
        re.replace(r'[^a-z ]', '', name.lower())
        for name in Food.objects.values_list('name', flat=True)])

    conll = textblob.en.np_extractors.ConllExtractor()

    def _nouns(s):
        return (
            set(textblob.TextBlob(s, np_extractor=conll).noun_phrases)
            | set(textblob.TextBlob(s).noun_phrases))

    def _matches(s, cutoff):
        return (
            s.real_quick_ratio() >= cutoff
            and s.quick_ratio() >= cutoff
            and s.ratio() >= cutoff)

    def _matcher(n, m):
        return difflib.SequenceMatcher(None, n.lower(), m.lower(), autojunk=False)

    result = []

    for name in ingredients:
        s = _matcher(ingredient, name)
        if _matches(s, 0.9):
            result.append((s.ratio(), name))
        else:
            s = _matcher(ingredient, ' '.join(_nouns(name)))
            if _matches(s, cutoff):
                result.append((s.ratio(), name))
    return heapq.nlargest(n, result)


# textblob_nouns = {}

# print('Grouping tags')
# for tag in tags:
#     key = tag[0].lower()
#     if tag[1] == 'NLTK':
#         if key not in nltk_nouns:
#             nltk_nouns[key] = set()
#         nltk_nouns[key].update(tag[2])
#     else:
#         if key not in textblob_nouns:
#             textblob_nouns[key] = set()
#         textblob_nouns[key].update(tag[2])

# print('Adding tags')
# done = 0.0
# for ingredient in nltk_nouns:
#     usda[translation[ingredient]]['name']['split'] = list
# (nltk_nouns[ingredient].union(textblob_nouns[ingredient]))

import django
django.setup()

print(match_ingredient('egg'))
