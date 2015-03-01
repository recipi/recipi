from django.utils.translation import ugettext_lazy as _


VOLUME, WEIGHT, INDEFINITE = range(1, 4)


US_UNITS = {
    'cup': {
        'name': _('cup'),
        'plural': _('cups'),
        'abbreviation': 'c',
        'type': VOLUME,
        'aliases': ('c.',),
    },
    'us liquid pint': {
        'name': _('pint'),
        'plural': _('pints'),
        'abbreviation': 'pt',
        'type': VOLUME,
        'aliases': (),
    },
    'us liquid quart': {
        'name': _('quart'),
        'plural': _('quarts'),
        'abbreviation': 'q',
        'type': VOLUME,
        'aliases': ('qt', 'qts')
    },
    'us gallon': {
        'name': _('gallon'),
        'plural': _('gallons'),
        'abbreviation': 'gal',
        'type': VOLUME,
        'aliases': (),
    },
    'pound': {
        'name': _('pound'),
        'plural': _('pounds'),
        'abbreviation': 'lb',
        'type': WEIGHT,
        'aliases': (),
    },
    'ounce': {
        'name': _('ounce'),
        'plural': _('ounces'),
        'abbreviation': 'oz',
        'type': WEIGHT,
        'aliases': ()
    },
    'us fluid ounce': {
        'name': _('fluid ounce'),
        'plural': _('fluid ounces'),
        'abbreviation': 'fl oz',
        'type': VOLUME,
        'aliases': ('fl. oz',),
    }
}


SI_UNITS = {
    'milliliter': {
        'name': _('milliliter'),
        'plural': _('milliliters'),
        'abbreviation': 'ml',
        'type': VOLUME,
        'aliases': (),
    },
    'centiliter': {
        'name': _('centiliter'),
        'plural': _('centiliters'),
        'abbreviation': 'cl',
        'type': VOLUME,
        'aliases': (),
    },
    'liter': {
        'name': _('liter'),
        'plural': _('liters'),
        'abbreviation': 'l',
        'type': VOLUME,
        'aliases': (),
    },
    'deciliter': {
        'name': _('deciliter'),
        'plural': _('deciliters'),
        'abbreviation': 'dl',
        'type': VOLUME,
        'aliases': (),
    },
    'milligram': {
        'name': _('milligram'),
        'plural': _('milligrams'),
        'abbreviation': 'mg',
        'type': WEIGHT,
        'aliases': (),
    },
    'gram': {
        'name': _('gram'),
        'plural': _('grams'),
        'abbreviation': 'g',
        'type': WEIGHT,
        'aliases': ('gr', 'gr.', 'g.'),
    },
    'centigram': {
        'name': _('centigram'),
        'plural': _('centigrams'),
        'abbreviation': 'cg',
        'type': WEIGHT,
        'aliases': (),
    },
    'kilogram': {
        'name': _('kilogram'),
        'plural': _('kilograms'),
        'abbreviation': 'kg',
        'type': WEIGHT,
        'aliases': (),
    },
}

COMMON_UNITS = {
    'tablespoon': {
        'name': _('tablespoon'),
        'plural': _('tablespoons'),
        'abbreviation': 'T',
        'type': VOLUME,
        'aliases': ('tbsp', 'tbsp.', 'T', 'T.', 'tbs', 'tbs.', 'tb'),
    },
    'teaspoon': {
        'name': _('teaspoon'),
        'plural': _('teaspoons'),
        'abbreviation': 't',
        'type': VOLUME,
        'aliases': ('tsp', 'tsp.', 't', 't.',),
    },
    'slice': {
        'name': _('slice'),
        'plural': _('slices'),
        'abbreviation': 'sli',
        'type': INDEFINITE,
        'aliases': (),
    },
    'clove': {
        'name': _('clove'),
        'plural': _('cloves'),
        'abbreviation': 'clv',
        'type': INDEFINITE,
        'aliases': (),
    },
    'load': {
        'name': _('loaf'),
        'plural': _('loaves'),
        'abbreviation': 'lf',
        'type': INDEFINITE,
        'aliases': (),
    },
    'pinch': {
        'name': _('pinch'),
        'plural': _('pinches'),
        'abbreviation': 'pn',
        'type': INDEFINITE,
        'aliases': (),
    },
    'package': {
        'name': _('package'),
        'plural': _('packages'),
        'abbreviation': 'pk',
        'type': INDEFINITE,
        'aliases': ('pack',),
    },
    'can': {
        'name': _('can'),
        'plural': _('cans'),
        'abbreviation': 'cn',
        'type': INDEFINITE,
        'aliases': ('jar',),
    },
    'drop': {
        'name': _('drop'),
        'plural': _('drops'),
        'abbreviation': 'dr',
        'type': INDEFINITE,
        'aliases': (),
    },
    'bunch': {
        'name': _('bunch'),
        'plural': _('bunches'),
        'abbreviation': 'bn',
        'type': INDEFINITE,
        'aliases': (),
    },
    'dash': {
        'name': _('dash'),
        'plural': _('dashes'),
        'abbreviation': 'ds',
        'type': INDEFINITE,
        'aliases': (),
    },
    'carton': {
        'name': _('carton'),
        'plural': _('cartons'),
        'abbreviation': 'ct',
        'type': INDEFINITE,
        'aliases': (),
    },
    'unit': {
        'name': _('unit'),
        'plural': _('units'),
        'abbreviation': None,
        'type': INDEFINITE,
        'aliases': ('each', 'ea', 'whole'),
    },
    'unknown': {
        'name': _('unknown'),
        'plural': _('unknown'),
        'abbreviation': None,
        'type': INDEFINITE,
        'aliases': (),
    },
}


ALL_UNITS = {}
ALL_UNITS.update(COMMON_UNITS)
ALL_UNITS.update(SI_UNITS)
ALL_UNITS.update(US_UNITS)

UNIT_CHOICES = tuple((key, value['name']) for key, value in ALL_UNITS.items())

NUMBERS = {
    'a': 1,
    'an': 1,
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 9,
}


FOOD_ADJECTIVES = frozenset((
    'drained', 'sifted', 'ripe', 'sliced', 'medium', 'large', 'small',
    'frozen', 'roasted', 'coarsely', 'chopped', 'seasoned', 'sliced',
    'softened', 'slightly', 'beaten', 'torn', 'light', 'pure', 'peeled',
    'stale', 'piece', 'fresh', 'shredded', 'thawed', 'lightly', 'mild',
    'thinly', 'crumbled', 'minced', 'size', 'pitted', 'firmly', 'packed',
    'cooked', 'baby', 'ground', 'hot', 'dried', 'cubed', 'grated', 'cold',
    'boiling', 'diced', 'slivered', 'crushed', 'warm', 'finely', 'freshly',
    'hard-cooked', 'water-packed', 'low-fat', 'fat-free', 'reduced-fat',
    'reduced-sodium', 'ready-to-serve', 'quick-cooking', 'day-old',
    'pre-baked', 'melted', 'stewed', 'uncooked', 'blanched', 'fresh-ground',
    'cut-up', 'julienned', 'toasted', 'snipped', 'minced', 'wrapped', 'mashed',
    'additional', 'individually', 'firm', 'miniature', 'refrigerated',
    'thick', 'regular', 'scalded', 'cored', 'unpeeled', 'rubbed', 'canned'
))
