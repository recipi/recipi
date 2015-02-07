# -*- coding: utf-8 -*-
from django.contrib import admin

from recipi.food.models import (
    FoodGroup, Food, Language, LanguageDescription, Nutrient,
    Weight, Footnote)


@admin.register(FoodGroup)
class FoodGroupAdmin(admin.ModelAdmin):
    search_fields = ('code', 'name')


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    search_fields = (
        'ndb_number', 'name', 'short_name',
        'common_names', 'manufacturer_name'
    )

    list_filter = ('food_group__name',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    search_fields = ('food__name', 'factor_code')
    list_filter = ('food__food_group__name',)


@admin.register(LanguageDescription)
class LanguageDescriptionAdmin(admin.ModelAdmin):
    search_fields = ('factor_code', 'description')


@admin.register(Nutrient)
class NutrientAdmin(admin.ModelAdmin):
    search_fields = ('food__name', 'nutrient_id', 'description')
    list_filter = ('food__food_group__name', 'unit')


@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):
    search_fields = ('food__name', 'description')
    list_filter = ('food__food_group__name',)


@admin.register(Footnote)
class FootnoteAdmin(admin.ModelAdmin):
    search_fields = ('text', 'type', 'food__name')
    list_filter = ('type', 'food__food_group__name')
