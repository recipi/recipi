# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from djorm_pgarray.fields import TextArrayField

from recipi.utils.db import sane_repr, sane_str
from recipi.utils.db.uuid import UUIDField

# TODO: Figure out what the fucking hell a LanguaL factor is
# and how to use it (Pages 31, 32, TAble 6, 7 in sr27_doc.pdf)

# This is a *HIGHLY* experimental structure that mostly
# follows the structure of the USDA database.
# It's entirely possible to change over time once we actually
# develop code that uses it.

# The original database is not well designed so there are other ways
# of structuring the data. Figure it out! (cg)

# General information
# TODO: Write summary and move somewhere else!
# by the True Retention Method (%TR) (Murphy et al., 1975). This method, as shown
# below, accounts for the loss or gain of moisture and the loss of nutrients due to heat or
# other food preparation methods:
# %TR = (Nc*Gc ) / (Nr*Gr) * 100

# where:
# TR = true retention
# Nc = nutrient content per g of cooked food,
# Gc = g of cooked food,
# Nr = nutrient content per g of raw food, and
# Gr = g of food before cooking.

# `Weight` table per 100g of food
#  The following formula is used to calculate the nutrient
# content per household measure:
# N = (V*W)/100
#
# where:
# N = nutrient value per household measure,
# V = nutrient value per 100 g (Nutr_Val in the Nutrient Data file), and
# W = g weight of portion (Gm_Wgt in the Weight file).


class FoodGroup(models.Model):
    id = UUIDField(auto=True, primary_key=True)

    # 4-digit code identifying a food group. Only
    # the first 2 digits are currently assigned.
    # TODO: decide if this can be a proper primary key.
    code = models.CharField(max_length=4)

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
    id = UUIDField(auto=True, primary_key=True)

    # 5-digit nutrient databank number that uniquely identifies
    # a food item.
    # TODO: decide if this can be a proper primary key.
    ndb_number = models.CharField(max_length=5)

    # NOTE: In database import identified by the 4-digit code in `FoodGroup.code`
    food_group = models.ForeignKey(FoodGroup)

    # Nmae of this food item
    name = models.TextField()

    # abbreviated name of this food item.
    short_name = models.TextField()

    # scientific name of the food item. Given for the
    # least processed for mof food (usually raw), if applicable.
    scientific_name = models.TextField(blank=True)

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
    id = UUIDField(auto=True, primary_key=True)

    factor_code = models.CharField(max_length=5, unique=True)
    description = models.TextField()

    __repr__ = sane_repr('factor_code', 'description')
    __str__ = sane_str('factor_code', 'description')


class Nutrient(models.Model):
    id = UUIDField(auto=True, primary_key=True)

    food = models.ForeignKey(Food)

    nutrient_id = models.CharField(max_length=3)

    # Amount in 100 grams, edible portion †.
    nutrient_value = models.DecimalField(max_digits=10, decimal_places=3)

    min = models.DecimalField(max_digits=10, decimal_places=3)
    max = models.DecimalField(max_digits=10, decimal_places=3)
    degrees_of_freedon = models.PositiveIntegerField()
    lower_error_bound = models.DecimalField(max_digits=10, decimal_places=3)
    upper_error_bound = models.DecimalField(max_digits=10, decimal_places=3)

    __repr__ = sane_repr('nutrient_id', 'nutrient_value')
    __str__ = sane_str('nutrient_id', 'nutrient_value')

    class Meta:
        unique_together = ('food', 'nutrient_id')


class NutrientDefinition(models.Model):
    id = UUIDField(auto=True, primary_key=True)

    nutrient = models.ForeignKey(Nutrient)

    # Units of measure (mg, g, μg, etc)
    units = models.CharField(max_length=7)

    # INFOODS Tagnames.† A unique abbreviation for a
    # nutrient/food component developed by INFOODS to
    # aid in the interchange of data.
    tagname = models.CharField(max_length=20, blank=True)

    # Name of nutrient/food component.
    description = models.CharField(max_length=60, blank=True)

    # Number of decimal places to which a nutrient value is rounded.
    decimal_places = models.PositiveIntegerField()

    # Used for correct ordering
    ordering = models.PositiveIntegerField()

    __repr__ = sane_repr('nutrient_id', 'description', 'units')
    __str__ = sane_str('nutrient_id', 'description', 'units')


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
    __str__ = sane_str('type', 'nutrient', 'text')


# are provided, which are the first two common measures in the Weight file for each NDB
# number. To obtain values per one of the common measures, multiply the value in the
# desired nutrient field by the value in the desired common measure field and divide by
# 100. For example, to calculate the amount of fat in 1 tablespoon of butter (NDB No. 01001):

# VH=(N*CM)/100
# where:
# VH = the nutrient content per the desired common measure,
# N = the nutrient content per 100 g,
# For NDB No. 01001, fat = 81.11 g/100 g
# CM = grams of the common measure.
# For NDB No. 01001, 1 tablespoon = 14.2 g
# So using this formula for the above example:
# VH = (81.11*14.2)/100 = 11.52 g fat in 1 tablespoon of butter
