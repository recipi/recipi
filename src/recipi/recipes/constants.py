from django.utils.translation import ugettext_lazy as _


VOLUME, WEIGHT, INDEFINITE = range(1, 4)


US_UNITS = {
    'cup': {
        'name': _('cup'),
        'plural': _('cups'),
        'abbreviation': 'c',
        'type': VOLUME,
        'aliases': ()
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
        'aliases': ()
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
        'aliases': (),
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
        'aliases': (),
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
        'aliases': ('tbsp', 'tb'),
    },
    'teaspoon': {
        'name': _('teaspoon'),
        'plural': _('teaspoons'),
        'abbreviation': 't',
        'type': VOLUME,
        'aliases': ('tsp',),
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
