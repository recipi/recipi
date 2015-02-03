

`Weight` table per 100g of food
The following formula is used to calculate the nutrient
content per household measure:
N = (V*W)/100

where:
N = nutrient value per household measure,
V = nutrient value per 100 g (Nutr_Val in the Nutrient Data file), and
W = g weight of portion (Gm_Wgt in the Weight file).



... are provided, which are the first two common measures in the Weight file for each NDB
number. To obtain values per one of the common measures, multiply the value in the
desired nutrient field by the value in the desired common measure field and divide by
100. For example, to calculate the amount of fat in 1 tablespoon of butter (NDB No. 01001):

VH=(N*CM)/100
where:
VH = the nutrient content per the desired common measure,
N = the nutrient content per 100 g,
For NDB No. 01001, fat = 81.11 g/100 g
CM = grams of the common measure.

For NDB No. 01001, 1 tablespoon = 14.2 g

So using this formula for the above example:
VH = (81.11*14.2)/100 = 11.52 g fat in 1 tablespoon of butter


TODO: Write down summary of those paragraphs:

The general factor of 6.25 is used to calculate protein in items that do not
have a specific factor.
Protein values for chocolate, cocoa, coffee, mushrooms, and yeast were adjusted for
non-protein nitrogenous material (Merrill and Watt, 1973). The adjusted protein
conversion factors used to calculate protein for these items are as follows:
chocolate and cocoa 4.74
coffee 5.3
mushrooms 4.38
yeast 5.7

For soybeans, nitrogen values were multiplied by a factor of 5.71 (Jones, 1941) to
calculate protein. The soybean industry, however, uses 6.25 to calculate protein. To
convert these values divide the proteins value by 5.71, and then multiply the resulting
value by 6.25. It will also be necessary to adjust the value for carbohydrate by
difference (Nutr. No. 205).

Food Energy. Food energy is expressed in kilocalories (kcal) and kilojoules (kJ). One
kcal equals 4.184 kJ. The data represent physiologically available energy, which is the
energy value remaining after digestive and urinary losses are deducted from gross

Calorie factors for protein, fat, and carbohydrates are included in the Food Description
file. For foods containing alcohol, a factor of 6.93 is used to calculate kilocalories per
gram of alcohol (Merrill and Watt, 1973). No calorie factors are given for items prepared
using the recipe program of the NDBS. Instead, total kilocalories for these items equal
the sums of the kilocalories contributed by each ingredient after adjustment for changes
in yield, as appropriate. For multi-ingredient processed foods, if the kilocalories
calculated by the manufacturer are reported, no calorie factors are given.

Calorie factors for fructose and sorbitol, not available in the Atwater system,
are derived from the work of Livesay and Marinos (1988). Calorie factors
for coffee and tea are estimated from those for seeds and vegetables, respectively.
