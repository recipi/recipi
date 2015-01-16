# -*- coding: utf-8 -*-
import nltk
from stopwords import stoplists


# TODO: Split to specifically localized modules.
measure_units = (
    '(few|handful|pinch|some|dash|g|kg|ml|l|cup|tbsp|tsp|löffel|teelöffel|'
    'tasse|unze|oz|pfund|pound)'
)

stopwords = set()

for language, words in stoplists.items():
    stopwords.update(words)


tokens = [
    (measure_units, 'measure_units'),
    (r'({0})$'.format(r'|'.join(stopwords)), 'stopword'),
    (r'[\s]*', 'join')
]

tagger = nltk.RegexpTagger(tokens)


def join_tags(tags):
    result = []
    buffer = []
    for item in tags:
        if item[1] == 'join':
            buffer.append(item[0])
        else:
            if buffer:
                result.append((u' '.join(buffer), 'detail'))
                buffer = []
            result.append(item)
    if buffer:
        result.append((u' '.join(buffer), 'detail'))

    return result


def parse(string, *args, **kwargs):
    result = join_tags(tagger.tag(string.split()))
    values = []
    ignore = False

    next = lambda: result[idx + 1] if len(result) > idx + 1 else (None, None)
    for idx, item in enumerate(result):
        if ignore:
            ignore = False
            continue
        
        value, type = item

        if type == 'stopword':
            continue
        elif type == 'measure_units':
            values.append({'unit': value})
        else:
            values.append({'word': value})

    return values
