"""Helpers for parsing a recipe.

Rules for parsing an ingredient list:

<amount> <unit> [of <ingredient>]

<amount>:
x whole or decimal number, in digits (250, 0.75)
x common fraction (3/4)
- numeral in words (half, one, ten, twenty-five, three quarters)
- determiner instead of a numeral ("an onion")
- subjective (some, a few, several)

- two to three
- 2 to 3
- 2-3
- five to 10

<unit>:

x general-purpose measurements (lb, oz, kg, g; pounds, ounces, etc.)
x cooking units (Tb, tsp)
x informal units (a pinch, a dash)
x container sizes (package, bunch, large can)
x no unit at all, for countable ingredients (as in "three lemons")
- a little
- to taste

"""
import re
from fractions import Fraction

import django
django.setup()

from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer

from recipi.recipes.constants import ALL_UNITS


lemmatizer = WordNetLemmatizer()

units = []
reversed_units = {}

for descr, unit in ALL_UNITS.items():
    units.append(str(unit['name']))
    reversed_units[str(unit['name'])] = descr

    if unit['abbreviation']:
        reversed_units[unit['abbreviation']] = descr
        units.append(unit['abbreviation'])

    for alias in unit['aliases']:
        units.append(alias)
        reversed_units[alias] = descr


_amount_re = '([1-9]+\d*\s)?((\d+)\/(\d+)\s+)?'
_units_re = '|'.join(sorted(units, key=len, reverse=True))


ingredient_line_regex = re.compile(''.join((
    '(?P<amount>{regex})'.format(regex=_amount_re),
    ('(?P<pre_detail>\('
        '(?P<pre_detail_amount>{amount_regex})?'
        '(?P<pre_detail_unit>{unit_regex}\s*)?'
    '\)\s+)?'.format(amount_regex=_amount_re, unit_regex=_units_re)),
    '(?P<unit>(?:{regex})\s+)?'.format(regex=_units_re),
    ('(?P<post_detail>\('
        '(?P<post_detail_amount>{amount_regex})?'
        '(?P<post_detail_unit>{unit_regex}\s*)?'
    '\))?'.format(amount_regex=_amount_re, unit_regex=_units_re)),
    '\s*(?P<ingredients>[a-z \-,]+)'
)))


def is_ingredient(word, ingredients):
    """Return True if the word is an ingredient, False otherwise.

    >>> is_ingredient('milk')
    True
    >>> is_ingredient('blackberries')
    True
    >>> is_ingredient('Canada')
    False
    >>> is_ingredient('breakfast')
    False
    >>> is_ingredient('dish')
    False
    """
    # TODO: Integrate more details, allow for more variation.
    reject_synsets = ['meal.n.01', 'meal.n.02', 'dish.n.02', 'vitamin.n.01']
    reject_synsets = set(wordnet.synset(w) for w in reject_synsets)
    accept_synsets = ['food.n.01', 'food.n.02']
    accept_synsets = set(wordnet.synset(w) for w in accept_synsets)
    for word_synset in wordnet.synsets(word, wordnet.NOUN):
        all_synsets = set(word_synset.closure(lambda s: s.hypernyms()))
        all_synsets.add(word_synset)
        for synset in reject_synsets:
            if synset in all_synsets:
                return False
        for synset in accept_synsets:
            if synset in all_synsets:
                return True

    return word in ingredients


def normalize(string):
    """Normalizes an ingredient name, removing pluralization.

    >>> normalize_ingredient_name('eggs')
    'egg'
    >>> normalize_ingredient_name('bing cherries')
    'bing cherry'
    """
    words = string.lower().strip(' *').split()
    return ' '.join(lemmatizer.lemmatize(w) for w in words)


def parse_line(line):
    normalized = normalize(line)
    match = ingredient_line_regex.match(normalized)

    if match is None:
        return

    return match.groupdict()


def filter_ingredients(ingredients):
    return ' '.join(ingredients.split(' ')).strip()


def parse_ingredients(ingredients):
    def _amount(line):
        match = re.match(_amount_re, line)
        number, fraction = match.group(1), match.group(2)

        if not fraction:
            return Fraction(number.strip())
        elif not number:
            return Fraction(fraction.strip())

        return Fraction(number.strip()) + Fraction(fraction.strip())

    def _unit(parsed, key):
        return (parsed.get(key, None) or 'unknown').strip()

    result = []

    for line in ingredients:
        parsed = parse_line(line)

        data = {
            'ingredients': filter_ingredients(parsed['ingredients']),
            'amount': _amount(parsed['amount']),
            'unit': _unit(parsed, 'unit')
        }

        if parsed['pre_detail_amount'] is not None:
            data['amount_detail'] = {
                'amount': _amount(parsed['pre_detail_amount']),
                'unit': _unit(parsed, 'pre_detail_unit')
            }
        elif parsed['post_detail_amount'] is not None:
            data['amount_detail'] = {
                'amount': _amount(parsed['post_detail_amount']),
                'unit': _unit(parsed, 'post_detail_unit')
            }
        else:
            data['amount_detail'] = None

        result.append(data)

    return result
