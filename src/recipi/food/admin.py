# -*- coding: utf-8 -*-
from django.contrib import admin

from recipi.food.models import (
    FoodGroup, Food, Language, LanguageDescription, Nutrient,
    Weight, Footnote)


admin.site.register(FoodGroup)
admin.site.register(Food)
admin.site.register(Language)
admin.site.register(LanguageDescription)
admin.site.register(Nutrient)
admin.site.register(Weight)
admin.site.register(Footnote)
