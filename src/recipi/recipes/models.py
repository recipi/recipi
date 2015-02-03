from django.db import models
from djorm_pgarray.fields import TextArrayField
from timedelta import fields as timedelta_fields

from recipi.utils.db.uuid import UUIDField


class Ingredient(models.Model):
    name = models.CharField(max_length=256)
    food = models.ForeignKey('food.Food', null=True, blank=True)
    nutrients = models.ManyToManyField('food.Nutrient', null=True, blank=True)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('Recipe')
    ingredient = models.ForeignKey(Ingredient)

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
