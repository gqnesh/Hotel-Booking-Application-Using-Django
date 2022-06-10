from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Category)
class ModelCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name']


@admin.register(models.Hotels)
class ModelHotelAdmin(admin.ModelAdmin):
    list_display = ['id', 'HotelName', 'HotelAddress', 'HotelImages', 'Price']    