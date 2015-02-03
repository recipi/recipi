# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from djorm_pgarray.fields import TextArrayField

from recipi.utils.db import sane_repr, sane_str
from recipi.utils.db.uuid import UUIDField


class FoodGroup(models.Model):
    # 4-digit code identifying a food group. Only
    # the first 2 digits are currently assigned.
    code = models.CharField(max_length=4, primary_key=True)

    name = models.CharField(max_length=60)

    __repr__ = sane_repr('code', 'name')
    __str__ = sane_str('name')


class Food(models.Model):
    """Descriptions and group designators for all food items.

    Also contains common names, manufacturer name, scientific name,
    percentage and description of refuse and factors used for calculating
    protein and kilocalories, if applicable.

    Links to the Food Group Description file by the FdGrp_Cd field
    Links to the Nutrient Data file by the NDB_No field
    Links to the Weight file by the NDB_No field
    Links to the Footnote file by the NDB_No field
    Links to the LanguaL Factor file by the NDB_No field
    """
    #
    ndb_number = models.CharField(
        _('NDB Number'),
        max_length=5, primary_key=True,
        help_text=_(
            '5-digit nutrient databank number that uniquely identifies a food item.'
        )
    )

    # NOTE: In database import identified by the 4-digit code in `FoodGroup.code`
    food_group = models.ForeignKey(label=_('Food Group'), FoodGroup)

    name = models.TextField(
        label=_('Name'),
        help_text=_('of this food item')
    )

    short_name = models.TextField(
        _('Short Name'),
        help_text=_('abbreviated name of this food item.')
    )

    scientific_name = models.TextField(
        _('Scientific Name'),
        blank=True,
        help_text=_(
            'scientific name of the food item. Given for the '
            'least processed for most food (usually raw), if applicable.'
        )
    )

    # Other names commonly used to describe this item.
    # For example "soda" or "pop" for "carbonated beverages".
    common_names = TextArrayField(blank=True)

    manufacturer_name = models.TextField(blank=True)

    # Indicates if the food item is used in the USDA Food and Nutrient Database
    # for Dietary Studies (FNDDS) and thus has a complete nutrient profile
    # for the 65 FNDDS nutrients.
    # TODO: find out what to do with that information.
    survey = models.NullBooleanField(default=None, blank=True)

    # Description of inedible parts of a food item (refuse), such as seeds or bone.
    refuse_description = models.TextField(blank=True)

    # Percentage of refuse. (2-digit, no floating point.)
    refuse_percentage = models.PositiveIntegerField(default=None, null=True, blank=True)

    # TODO: Write down summary of those paragraphs:

    # The general factor of 6.25 is used to calculate protein in items that do not
    # have a specific factor.
    # Protein values for chocolate, cocoa, coffee, mushrooms, and yeast were adjusted for
    # non-protein nitrogenous material (Merrill and Watt, 1973). The adjusted protein
    # conversion factors used to calculate protein for these items are as follows:
    # chocolate and cocoa 4.74
    # coffee 5.3
    # mushrooms 4.38
    # yeast 5.7

    # For soybeans, nitrogen values were multiplied by a factor of 5.71 (Jones, 1941) to
    # calculate protein. The soybean industry, however, uses 6.25 to calculate protein. To
    # convert these values divide the proteins value by 5.71, and then multiply the resulting
    # value by 6.25. It will also be necessary to adjust the value for carbohydrate by
    # difference (Nutr. No. 205).

    # Food Energy. Food energy is expressed in kilocalories (kcal) and kilojoules (kJ). One
    # kcal equals 4.184 kJ. The data represent physiologically available energy, which is the
    # energy value remaining after digestive and urinary losses are deducted from gross

    # Calorie factors for protein, fat, and carbohydrates are included in the Food Description
    # file. For foods containing alcohol, a factor of 6.93 is used to calculate kilocalories per
    # gram of alcohol (Merrill and Watt, 1973). No calorie factors are given for items prepared
    # using the recipe program of the NDBS. Instead, total kilocalories for these items equal
    # the sums of the kilocalories contributed by each ingredient after adjustment for changes
    # in yield, as appropriate. For multi-ingredient processed foods, if the kilocalories
    # calculated by the manufacturer are reported, no calorie factors are given.

    # Calorie factors for fructose and sorbitol, not available in the Atwater system,
    # are derived from the work of Livesay and Marinos (1988). Calorie factors
    # for coffee and tea are estimated from those for seeds and vegetables, respectively.

    # Factor for converting nitrogen to protein (see above)
    nitrogen_factor = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)

    # Factor for calculating calories from protein (see above)
    protein_factor = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)

    # Factor for calculating calories from fat (see above)
    fat_factor = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)

    # Factor for calculating calories from carbohydrate
    carbohydrate_factor = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)

    __repr__ = sane_repr('ndb_number', 'food_group', 'name')
    __str__ = sane_str('name')


class Language(models.Model):
    id = UUIDField(auto=True, primary_key=True)

    food = models.ForeignKey(Food)

    # The LanguaL factor from the Thesaurus
    factor_code = models.CharField(max_length=5)

    __repr__ = sane_repr('food', 'factor_code')
    __str__ = sane_str('factor_code', 'food')

    class Meta:
        unique_together = ('food', 'factor_code')


class LanguageDescription(models.Model):
    factor_code = models.CharField(max_length=5, primary_key=True)
    description = models.TextField()

    __repr__ = sane_repr('factor_code', 'description')
    __str__ = sane_str('factor_code', 'description')


class Nutrient(models.Model):
    id = UUIDField(auto=True, primary_key=True)

    food = models.ForeignKey(Food)

    nutrient_id = models.CharField(max_length=3)

    # Amount in 100 grams, edible portion †.
    nutrient_value = models.DecimalField(max_digits=10, decimal_places=3)

    # Units of measure (mg, g, μg, etc)
    unit = models.CharField(max_length=7)

    # Name of nutrient/food component.
    description = models.CharField(max_length=60, blank=True)

    # Number of decimal places to which a nutrient value is rounded.
    decimal_places = models.PositiveIntegerField()

    # Used for correct ordering
    ordering = models.PositiveIntegerField()

    min = models.DecimalField(max_digits=10, decimal_places=3)
    max = models.DecimalField(max_digits=10, decimal_places=3)
    degrees_of_freedon = models.PositiveIntegerField()
    lower_error_bound = models.DecimalField(max_digits=10, decimal_places=3)
    upper_error_bound = models.DecimalField(max_digits=10, decimal_places=3)

    __repr__ = sane_repr('description', 'nutrient_value', 'unit')
    __str__ = sane_str('food', 'description', 'nutrient_value', 'unit')

    class Meta:
        unique_together = ('food', 'nutrient_id')


class Weight(models.Model):
    """Contains the weight in grams of a number of common measures for each food item."""
    id = UUIDField(auto=True, primary_key=True)

    food = models.ForeignKey(Food)

    sequence = models.PositiveIntegerField()

    # Unit modifier (for example 1 in "1 cup")
    amount = models.DecimalField(max_digits=5, decimal_places=2)

    # Description (for example, cup, diced, and 1-inch pieces)
    description = models.TextField()

    # Weight in gram
    weight = models.DecimalField(max_digits=7, decimal_places=2)

    # Standard deviation
    deviation = models.DecimalField(max_digits=7, decimal_places=3, default=0.0)

    __repr__ = sane_repr('food', 'description', 'amount', 'weight')
    __str__ = sane_str('food', 'description', 'amount', 'weight')

    class Meta:
        unique_together = ('food', 'sequence')


class Footnote(models.Model):
    """Contains additional information.

    About:

     * food item
     * household weight
     * nutrient value
    """
    # Type of footnotes.
    TYPE_FOOD = 'D'
    TYPE_MEASURE = 'M'
    TYPE_NUTRIENT = 'N'

    id = UUIDField(auto=True, primary_key=True)

    food = models.ForeignKey(Food)

    # Sequence number. If a given footnote applies
    # to more than one nutrient number, the same `number` is used.
    sequence = models.PositiveIntegerField()

    # Type of footnote:
    # If `TYPE_NUTRIENT`, then `nutrient_number` is also set as it applies
    # for this nutrient specifically.
    type = models.CharField(max_length=1, choices=(
        (TYPE_FOOD, _('Food ')),
        (TYPE_MEASURE, _('Measure')),
        (TYPE_NUTRIENT, _('Nutrient'))
    ))

    nutrient_id = models.CharField(max_length=3)

    text = models.TextField()

    __repr__ = sane_repr('type', 'nutrient')
    __str__ = sane_str('text')
