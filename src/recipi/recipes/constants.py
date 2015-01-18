VOLUME, WEIGHT, INDEFINITE = range(1, 4)


US_UNITS = {
    'cup': {
        'name': 'cup',
        'plural': 'cups',
        'abbreviation': 'c',
        'type': VOLUME,
        'aliases': ()
    },
    'us liquid pint': {
        'name': 'pint',
        'plural': 'pints',
        'abbreviation': 'pt',
        'type': VOLUME,
        'aliases': (),
    },
    'us liquid quart': {
        'name': 'quart',
        'plural': 'quarts',
        'abbreviation': 'q',
        'type': VOLUME,
        'aliases': ()
    },
    'us gallon': {
        'name': 'gallon',
        'plural': 'gallons',
        'abbreviation': 'gal',
        'type': VOLUME,
        'aliases': (),
    },
    'pound': {
        'name': 'pound',
        'plural': 'pounds',
        'abbreviation': 'lb',
        'type': WEIGHT,
        'aliases': (),
    },
    'ounce': {
        'name': 'ounce',
        'plural': 'ounces',
        'abbreviation': 'oz',
        'type': WEIGHT,
        'aliases': ()
    },
    'us fluid ounce': {
        'name': 'fluid ounce',
        'plural': 'fluid ounces',
        'abbreviation': 'fl oz',
        'type': VOLUME,
        'aliases': (),
    }
}


SI_UNITS = {
    'milliliter': {
        'name': 'milliliter',
        'plural': 'milliliters',
        'abbreviation': 'ml',
        'type': VOLUME,
        'aliases': (),
    },
    'centiliter': {
        'name': 'centiliter',
        'plural': 'centiliters',
        'abbreviation': 'cl',
        'type': VOLUME,
        'aliases': (),
    },
    'liter': {
        'name': 'liter',
        'plural': 'liters',
        'abbreviation': 'l',
        'type': VOLUME,
        'aliases': (),
    },
    'deciliter': {
        'name': 'deciliter',
        'plural': 'deciliters',
        'abbreviation': 'dl',
        'type': VOLUME,
        'aliases': (),
    },
    'milligram': {
        'name': 'milligram',
        'plural': 'milligrams',
        'abbreviation': 'mg',
        'type': WEIGHT,
        'aliases': (),
    },
    'gram': {
        'name': 'gram',
        'plural': 'grams',
        'abbreviation': 'g',
        'type': WEIGHT,
        'aliases': (),
    },
    'centigram': {
        'name': 'centigram',
        'plural': 'centigrams',
        'abbreviation': 'cg',
        'type': WEIGHT,
        'aliases': (),
    },
    'kilogram': {
        'name': 'kilogram',
        'plural': 'kilograms',
        'abbreviation': 'kg',
        'type': WEIGHT,
        'aliases': (),
    },
}

COMMON_UNITS = {
    'tablespoon': {
        'name': 'tablespoon',
        'plural': 'tablespoons',
        'abbreviation': 'T',
        'type': VOLUME,
        'aliases': ('tbsp', 'tb'),
    },
    'teaspoon': {
        'name': 'teaspoon',
        'plural': 'teaspoons',
        'abbreviation': 't',
        'type': VOLUME,
        'aliases': ('tsp',),
    },
    'slice': {
        'name': 'slice',
        'plural': 'slices',
        'abbreviation': 'sli',
        'type': INDEFINITE,
        'aliases': (),
    },
    'clove': {
        'name': 'clove',
        'plural': 'cloves',
        'abbreviation': 'clv',
        'type': INDEFINITE,
        'aliases': (),
    },
    'load': {
        'name': 'loaf',
        'plural': 'loaves',
        'abbreviation': 'lf',
        'type': INDEFINITE,
        'aliases': (),
    },
    'pinch': {
        'name': 'pinch',
        'plural': 'pinches',
        'abbreviation': 'pn',
        'type': INDEFINITE,
        'aliases': (),
    },
    'package': {
        'name': 'package',
        'plural': 'packages',
        'abbreviation': 'pk',
        'type': INDEFINITE,
        'aliases': ('pack',),
    },
    'can': {
        'name': 'can',
        'plural': 'cans',
        'abbreviation': 'cn',
        'type': INDEFINITE,
        'aliases': ('jar',),
    },
    'drop': {
        'name': 'drop',
        'plural': 'drops',
        'abbreviation': 'dr',
        'type': INDEFINITE,
        'aliases': (),
    },
    'bunch': {
        'name': 'bunch',
        'plural': 'bunches',
        'abbreviation': 'bn',
        'type': INDEFINITE,
        'aliases': (),
    },
    'dash': {
        'name': 'dash',
        'plural': 'dashes',
        'abbreviation': 'ds',
        'type': INDEFINITE,
        'aliases': (),
    },
    'carton': {
        'name': 'carton',
        'plural': 'cartons',
        'abbreviation': 'ct',
        'type': INDEFINITE,
        'aliases': (),
    },
    'unit': {
        'name': 'unit',
        'plural': 'units',
        'abbreviation': None,
        'type': INDEFINITE,
        'aliases': ('each', 'ea', 'whole'),
    },
    'unknown': {
        'name': 'unknown',
        'plural': 'unknown',
        'abbreviation': None,
        'type': INDEFINITE,
        'aliases': (),
    },
}
