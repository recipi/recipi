from django.db import models
from djorm_pgarray.fields import TextArrayField
from timedelta import fields as timedelta_fields

from recipi.utils.db.uuid import UUIDField


class Ingredient(models.Model):
    name = models.CharField(max_length=256)
    food = models.ForeignKey('food.Food', null=True, blank=True)
    nutrients = models.ManyToManyField('food.Nutrient', null=True, blank=True)

    # TODO: There is tooooons more: http://ndb.nal.usda.gov/ndb/foods/show/3044
    # I tried to find the most important values for now (cg)
    # All fields allow values up to 9999.99 - I think this should suffice (cg)

    # TODO: Those are calculatable from what we already have via our nutrition database

    # calories = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    # carbohydrate = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    # protein = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    # fat = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    # saturated_fat = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    # polyunsaturated_fat = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    # monounsaturated_fat = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    # trans_fat = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    # cholesterol = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    # sodium = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    # potassium = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    # fiber = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    # sugar = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    # # TODO: depending on the source we need to make sure to use those values
    # # identically. E.g fatsecret.com gives these values only as a
    # # "percentage of daily Calcium/Iron" etc based on a 2000 calorie diet.
    # vitamin_a = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    # vitamin_b = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    # vitamin_c = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    # vitamin_d = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    # calcium = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    # iron = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)


class RecipeIngredient(models.Model):
    # TODO: Figure out if this makes sense.
    # Currently this model would be used for simple ingredients such as
    # "one slice of brown bread" and more specific ingredients such as
    # "350g of white flour". Imho this works as not every
    # recipe will be so detailed (e.g imagine a jelly-bread recipe)
    # (cg)
    recipe = models.ForeignKey('Recipe')
    ingredient = models.ForeignKey(Ingredient)

    # TODO: Normalize units in `recipes.constants`
    metric_unit = models.CharField(max_length=3, choices=())
    volume = models.PositiveIntegerField()


class Cuisine(models.Model):
    pass


class Picture(models.Model):
    pass


class Recipe(models.Model):
    id = UUIDField(auto=True, primary_key=True)
    url = models.URLField(max_length=2048, blank=True)

    title = models.CharField(max_length=80)

    # TODO: I think we're going to need some kind of shadow-user
    # account for automatic imports.
    author = models.ForeignKey('accounts.User')

    description = models.TextField(blank=True)

    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipes',
        through='RecipeIngredient',
        blank=True
    )

    cuisines = models.ManyToManyField(
        Cuisine,
        related_name='recipes',
        blank=True
    )

    pictures = models.ManyToManyField(
        Picture,
        related_name='recipes',
        blank=True
    )

    # We're always talking about a one serving per 'Person' here.
    servings = models.PositiveIntegerField()

    # TODO: Are there any more units we need to measure?
    preparation_time = timedelta_fields.TimedeltaField()
    cook_time = timedelta_fields.TimedeltaField()
