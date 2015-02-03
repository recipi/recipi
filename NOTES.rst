

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
