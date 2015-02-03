# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from djorm_pgarray.fields import TextArrayField

from recipi.utils.db import sane_repr, sane_str
from recipi.utils.db.uuid import UUIDField


class FoodGroup(models.Model):
    code = models.CharField(
        _('Code'),
        max_length=4, primary_key=True,
        help_text=_(
            '4-digit code identifying a food group. Only'
            ' the first 2 digits are currently assigned.'
        )
    )

    name = models.CharField(_('Name'), max_length=60)

    __repr__ = sane_repr('code', 'name')
    __str__ = sane_str('name')


class Food(models.Model):
    """Descriptions and group designators for all food items.

    Also contains common names, manufacturer name, scientific name,
    percentage and description of refuse and factors used for calculating
    protein and kilocalories, if applicable.
    """
    ndb_number = models.CharField(
        _('NDB Number'),
        max_length=5, primary_key=True,
        help_text=_(
            '5-digit nutrient databank number that uniquely identifies a food item.'
        )
    )

    food_group = models.ForeignKey(FoodGroup, verbose_name=_('Food Group'))

    name = models.TextField(
        _('Name'),
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

    common_names = TextArrayField(
        verbose_name=_('Common Names'),
        blank=True,
        help_text=_(
            'Other names commonly used to describe this item.'
            ' For example "soda" or "pop" for "carbonated beverages".'
        )
    )

    manufacturer_name = models.TextField(_('Manufacturer Name'), blank=True)

    survey = models.NullBooleanField(
        _('Has Survey?'),
        default=None, blank=True,
        help_text=_(
            'Indicates if the food item is used in the USDA Food and Nutrient Database'
            ' for Dietary Studies (FNDDS) and thus has a complete nutrient profile'
            ' for the 65 FNDDS nutrients.'
        )
    )

    refuse_description = models.TextField(
        _('Refuse Description'),
        blank=True,
        help_text=_(
            'Description of inedible parts of a food item (refuse), such as seeds or bone.'
        )
    )

    refuse_percentage = models.PositiveIntegerField(
        _('Percentage of refuse'),
        default=None, null=True, blank=True
    )

    nitrogen_factor = models.DecimalField(
        _('Nitrogen Factor'),
        max_digits=4, decimal_places=2, default=0.0,
        help_text=_('Factor for converting nitrogen to protein')
    )

    protein_factor = models.DecimalField(
        _('Protein Factor'),
        max_digits=4, decimal_places=2, default=0.0,
        help_text=_('Factor for calculating calories from protein')
    )

    fat_factor = models.DecimalField(
        _('Fat Factor'),
        max_digits=4, decimal_places=2, default=0.0,
        help_text=_('Factor for calculating calories from fat')
    )

    carbohydrate_factor = models.DecimalField(
        _('Carbohydrate Factor'),
        max_digits=4, decimal_places=2, default=0.0,
        help_text=_('Factor for calculating calories from carbohydrate')
    )

    __repr__ = sane_repr('ndb_number', 'food_group', 'name')
    __str__ = sane_str('name')


class Language(models.Model):
    id = UUIDField(auto=True, primary_key=True)

    food = models.ForeignKey(Food)

    factor_code = models.CharField(
        _('Factor Code'),
        max_length=5,
        help_text=_('The LanguaL factor from the Thesaurus')
    )

    __repr__ = sane_repr('food', 'factor_code')
    __str__ = sane_str('factor_code', 'food')

    class Meta:
        unique_together = ('food', 'factor_code')


class LanguageDescription(models.Model):
    factor_code = models.CharField(_('Factor Code'), max_length=5, primary_key=True)
    description = models.TextField('Description')

    __repr__ = sane_repr('factor_code', 'description')
    __str__ = sane_str('factor_code', 'description')


class Nutrient(models.Model):
    id = UUIDField(auto=True, primary_key=True)

    food = models.ForeignKey(Food)

    nutrient_id = models.CharField(_('Nutrient ID'), max_length=3)
    name = models.CharField(_('Name'), max_length=60, blank=True)

    nutrient_value = models.DecimalField(
        _('Nutrient Value'),
        max_digits=10, decimal_places=3,
        help_text=_('Amount in 100 grams, edible portion †.')
    )

    unit = models.CharField(
        _('Unit'),
        max_length=7,
        help_text=_('Units of measure (mg, g, μg, etc)')
    )

    decimal_places = models.PositiveIntegerField(
        _('Decimal Places'),
        help_text=_('Number of decimal places to which a nutrient value is rounded.')
    )

    ordering = models.PositiveIntegerField(
        _('Ordering'),
        help_text=_('Used for correct ordering in nutrition information.')
    )

    min = models.DecimalField(_('Min'), max_digits=10, decimal_places=3)
    max = models.DecimalField(_('Max'), max_digits=10, decimal_places=3)
    degrees_of_freedom = models.PositiveIntegerField(_('Degrees of Freedom'))
    lower_error_bound = models.DecimalField(
        _('Lower Error Bound'),
        max_digits=10, decimal_places=3
    )
    upper_error_bound = models.DecimalField(
        _('Upper Error Bound'),
        max_digits=10, decimal_places=3
    )

    __repr__ = sane_repr('description', 'nutrient_value', 'unit')
    __str__ = sane_str('food', 'description', 'nutrient_value', 'unit')

    class Meta:
        unique_together = ('food', 'nutrient_id')


class Weight(models.Model):
    """Contains the weight in grams of a number of common measures for each food item."""
    id = UUIDField(auto=True, primary_key=True)

    food = models.ForeignKey(Food)

    sequence = models.PositiveIntegerField(_('Sequence'))

    amount = models.DecimalField(
        _('Amount'),
        max_digits=5, decimal_places=2,
        help_text=_('Unit modifier (for example 1 in "1 cup")')
    )

    description = models.TextField(
        _('Description'),
        help_text=_('Description (for example, cup, diced, and 1-inch pieces)')
    )

    weight = models.DecimalField(
        _('Weight'),
        max_digits=7, decimal_places=2,
        help_text=_('Weight in gram')
    )

    deviation = models.DecimalField(
        _('Deviation'),
        max_digits=7, decimal_places=3, default=0.0,
        help_text=_('Standard deviation')
    )

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
