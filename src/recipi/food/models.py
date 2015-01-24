from django.db import models
from djorm_pgarray.fields import TextArrayField

from recipi.utils.db.uuid import UUIDField

# This is a *HIGHLY* experimental structure that mostly
# follows the structure of the USDA database.
# It's entirely possible to change over time once we actually
# develop code that uses it.

# The original database is not well designed so there are other ways
# of structuring the data. Figure it out! (cg)

### General information
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


class FoodDescription(models.Model):
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
    ndb_no = models.CharField(max_length=5)

    # 4-digit code indicating the food group to which a food item belongs
    food_group = models.CharField(max_length=4)

    # Description of this food item
    long_description = models.TextField()

    # abbreviated description of this food item.
    short_description = models.TextField()

    # Other names commonly used to describe this item.
    # For example "soda" or "pop" for "carbonated beverages".
    common_names = TextArrayField(blank=True)

    # Indicates if the food item is used in the USDA Food and Nutrient Database
    # for Dietary Studies (FNDDS) and thus has a complete nutrient profile
    # for the 65 FNDDS nutrients.
    # TODO: find out what to do with that information.
    survey = models.BooleanField(default=False, blank=True)

    # Description of inedible parts of a food item (refuse), such as seeds or bone.
    refuse_description = models.TextField(blank=True)

    # Percentage of refuse. (2-digit, no floating point.)
    refuse = models.PositiveIntegerField(default=None, null=True, blank=True)

    # scientific name of the food item. Given for the
    # least processed for mof food (usually raw), if applicable.
    scientific_name = models.TextField(blank=True)

    # TODO: Write down summary of those paragraphs:

    # The general factor of 6.25 is used to calculate protein in items that do not have a specific factor.
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

    # Calorie factors for fructose and sorbitol, not available in the Atwater system, are derived
    # from the work of Livesay and Marinos (1988). Calorie factors for coffee and tea are
    # estimated from those for seeds and vegetables, respectively.

    # Factor for converting nitrogen to protein (see above)
    nitrogen_factor = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)

    # Factor for calculating calories from protein (see above)
    protein_factor = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)

    # Factor for calculating calories from fat (see above)
    fat_factor = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)

    # Factor for calculating calories from carbohydrate
    carbohydrate_factor = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
