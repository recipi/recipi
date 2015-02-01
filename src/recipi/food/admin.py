# -*- coding: utf-8 -*-
from django.contrib import admin

from recipi.food.models import (
    FoodGroup, Food, Language, LanguageDescription, Nutrient,
    Weight, Footnote)


class FoodGroupAdmin(admin.ModelAdmin):
    pass


class FoodAdmin(admin.ModelAdmin):
    pass


class LanguageAdmin(admin.ModelAdmin):
    pass


class LanguageDescriptionAdmin(admin.ModelAdmin):
    pass


class NutrientAdmin(admin.ModelAdmin):
    pass


class WeightAdmin(admin.ModelAdmin):
    pass


class FootnoteAdmin(admin.ModelAdmin):
    pass


admin.site.register(FoodGroup, FoodGroupAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(LanguageDescription, LanguageDescriptionAdmin)
admin.site.register(Nutrient, NutrientAdmin)
admin.site.register(Weight, WeightAdmin)
admin.site.register(Footnote, FootnoteAdmin)
