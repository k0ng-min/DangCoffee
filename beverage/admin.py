from django.contrib import admin

# Register your models here.
from beverage import models

admin.site.register(models.Product)
admin.site.register(models.category_list)