from fractions import Fraction

import pytest

from recipi.recipes.parser import parse_ingredients


cases = {
    '6 eggs': {
        'unit': 'unknown',
        'amount': Fraction('6'),
        'amount_detail': None,
        'ingredients': 'egg',
    },
    '2 cups water': {
        'unit': 'cup',
        'amount': Fraction('2'),
        'amount_detail': None,
        'ingredients': 'water',
    },
    '1 teaspoon salt': {
        'unit': 'teaspoon',
        'amount': Fraction('1'),
        'amount_detail': None,
        'ingredients': 'salt',
    },
    '4 large eggs': {
        'unit': 'unknown',
        'amount': Fraction('4'),
        'amount_detail': None,
        'ingredients': 'large egg',
    },
    '12 eggs': {
        'unit': 'unknown',
        'amount': Fraction('12'),
        'amount_detail': None,
        'ingredients': 'egg',
    },
    '1 quart water (more if necessary to cover the eggs completely)': {
        'unit': 'quart',
        'amount': Fraction('1'),
        'amount_detail': None,
        'modifiers': '(more if necessary to cover the eggs completely)',
        'ingredients': 'water',
    },
    '2 pounds ground beef': {
        'unit': 'pound',
        'amount': Fraction('2'),
        'amount_detail': None,
        'ingredients': 'ground beef',
    },
    '3/4 cup fresh bread crumbs': {
        'unit': 'cup',
        'amount': Fraction('0.75'),
        'amount_detail': None,
        'ingredients': 'fresh bread crumb',
    },
    '1/2 cup minced onion': {
        'unit': 'cup',
        'amount': Fraction('0.5'),
        'amount_detail': None,
        'ingredients': 'minced onion',
    },
    # Same as above but with ½ as the amount identifier.
    '½ cup minced onion': {
        'unit': 'cup',
        'amount': Fraction('0.5'),
        'amount_detail': None,
        'ingredients': 'minced onion',
    },
    '2 eggs, beaten': {
        'unit': 'unknown',
        'amount': Fraction('2'),
        'amount_detail': None,
        'modifiers': 'beaten',
        'ingredients': 'eggs',
    },
    '1 1/2 teaspoons salt': {
        'unit': 'teaspoon',
        'amount': Fraction('1.5'),
        'amount_detail': None,
        'ingredients': 'salt',
    },
    '1 1/2 teaspoons ground black pepper': {
        'unit': 'teaspoon',
        'amount': Fraction('1.5'),
        'amount_detail': None,
        'ingredients': 'ground black pepper',
    },
    '3 cups shredded Cheddar cheese': {
        'unit': 'cup',
        'amount': Fraction('3'),
        'amount_detail': None,
        'ingredients': 'shredded cheddar cheese',
    },
    '3/4 cup milk': {
        'unit': 'cup',
        'amount': Fraction('0.75'),
        'amount_detail': None,
        'ingredients': 'milk',
    },
    '2 tablespoons white vinegar': {
        'unit': 'tablespoon',
        'amount': Fraction('2'),
        'amount_detail': None,
        'ingredients': 'white vinegar',
    },
    '1 cup all-purpose flour': {
        'unit': 'cup',
        'amount': Fraction('1'),
        'amount_detail': None,
        'ingredients': 'all-purpose flour',
    },
    '2 tablespoons white sugar': {
        'unit': 'tablespoon',
        'amount': Fraction('2'),
        'amount_detail': None,
        'ingredients': 'white sugar',
    },
    '1 teaspoon baking powder': {
        'unit': 'teaspoon',
        'amount': Fraction('1'),
        'amount_detail': None,
        'ingredients': 'baking powder',
    },
    '1/2 teaspoon baking soda': {
        'unit': 'teaspoon',
        'amount': Fraction('0.5'),
        'amount_detail': None,
        'ingredients': 'baking soda',
    },
    '1/2 teaspoon salt': {
        'unit': 'teaspoon',
        'amount': Fraction('0.5'),
        'amount_detail': None,
        'ingredients': 'salt',
    },
    '1 egg': {
        'unit': 'unknown',
        'amount': Fraction('1'),
        'amount_detail': None,
        'ingredients': 'egg',
    },
    '2 tablespoons butter, melted cooking spray': {
        'unit': 'tablespoon',
        'amount': Fraction('2'),
        # XXX
        'amount_detail': None,
        'ingredients': 'butter, melted cooking spray',
    },
    '1 (16 ounce) package bow tie pasta': {
        'unit': 'package',
        'amount': Fraction('1'),
        'amount_detail': {'unit': 'ounce', 'amount': Fraction('16')},
        'ingredients': 'bow tie pasta',
    },
    '1 teaspoon olive oil': {
        'unit': 'teaspoon',
        'amount': Fraction('1'),
        'amount_detail': None,
        'ingredients': 'olive oil',
    },
    '2 cloves garlic, minced': {
        'unit': 'clove',
        'amount': Fraction('2'),
        'amount_detail': None,
        'ingredients': 'garlic, minced',
    },
    # XXX
    '2 boneless skinless chicken breasts, cut into bite-size pieces crushed red pepper flakes to taste': {  # noqa
        'unit': 'unknown',
        'amount': Fraction('2'),
        'amount_detail': None,
        'ingredients': 'boneless skinless chicken breasts, cut into bite-size piece crushed red pepper flake to taste',  # noqa
    },
    '1/3 cup oil-packed sun-dried tomatoes, drained and cut into strips': {
        'unit': 'cup',
        'amount': Fraction('1/3'),
        'amount_detail': None,
        'ingredients': 'oil-packed sun-dried tomatoes, drained and cut into strip',
    },
    '1/2 cup pesto sauce': {
        'unit': 'cup',
        'amount': Fraction('1/2'),
        'amount_detail': None,
        'ingredients': 'pesto sauce',
    },
    '2 (7 ounce) cans whole green chile peppers, drained': {
        'unit': 'can',
        'amount': Fraction('2'),
        'amount_detail': {'unit': 'ounce', 'amount': Fraction('7')},
        'ingredients': 'whole green chile peppers, drained',
    },
    '8 ounces Monterey Jack cheese, shredded': {
        'unit': 'ounce',
        'amount': Fraction('8'),
        'amount_detail': None,
        'ingredients': 'monterey jack cheese, shredded',
    },
    '8 ounces Longhorn or Cheddar cheese, shredded': {
        'unit': 'ounce',
        'amount': Fraction('8'),
        'amount_detail': None,
        'ingredients': 'longhorn or cheddar cheese, shredded',
    },
    '1 (5 ounce) can evaporated milk': {
        'unit': 'can',
        'amount': Fraction('1'),
        'amount_detail': {'unit': 'ounce', 'amount': Fraction('5')},
        'ingredients': 'evaporated milk',
    },
    '2 tablespoons all-purpose flour': {
        'unit': 'tablespoon',
        'amount': Fraction('2'),
        'amount_detail': None,
        'ingredients': 'all-purpose flour',
    },
    '1/2 cup milk': {
        'unit': 'cup',
        'amount': Fraction('1/2'),
        'amount_detail': None,
        'ingredients': 'milk',
    },
    '1 (8 ounce) can tomato sauce': {
        'unit': 'can',
        'amount': Fraction('1'),
        'amount_detail': {'unit': 'ounce', 'amount': Fraction('8')},
        'ingredients': 'tomato sauce',
    },
    '4 (4 ounce) fillets salmon': {
        'unit': 'unknown',
        'amount': Fraction('4'),
        'amount_detail': {'unit': 'ounce', 'amount': Fraction('4')},
        'ingredients': 'fillet salmon',
    },
    '1/4 cup Italian-style dry bread crumbs': {
        'unit': 'cup',
        'amount': Fraction('1/4'),
        'amount_detail': None,
        'ingredients': 'italian-style dry bread crumb',
    },
    '1/4 cup butter, melted': {
        'unit': 'cup',
        'amount': Fraction('1/4'),
        'amount_detail': None,
        'ingredients': 'butter, melted',
    },
    '6 frozen skinless, boneless chicken breast halves': {
        'unit': 'unknown',
        'amount': Fraction('6'),
        'amount_detail': None,
        'ingredients': 'frozen skinless, boneless chicken breast half',
    },
    '1 (12 ounce) bottle barbeque sauce': {
        'unit': 'unknown',
        'amount': Fraction('1'),
        'amount_detail': {'unit': 'ounce', 'amount': Fraction('12')},
        'ingredients': 'bottle barbeque sauce',
    },
    '1/2 cup Italian salad dressing': {
        'unit': 'cup',
        'amount': Fraction('1/2'),
        'amount_detail': None,
        'ingredients': 'italian salad dressing',
    },
    '1/4 cup brown sugar': {
        'unit': 'cup',
        'amount': Fraction('1/4'),
        'amount_detail': None,
        'ingredients': 'brown sugar',
    },
    '2 tablespoons Worcestershire sauce': {
        'unit': 'tablespoon',
        'amount': Fraction('2'),
        'amount_detail': None,
        'ingredients': 'worcestershire sauce',
    },
}


class TestParser:
    parameters = [(input, expected) for input, expected in cases.items()]

    @pytest.mark.parametrize('input, expected', parameters)
    def test_parse_ingredients(self, input, expected):
        assert parse_ingredients([input]) == [expected]
