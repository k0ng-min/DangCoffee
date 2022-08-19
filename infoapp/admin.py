from django.contrib import admin

# Register your models here.
from infoapp.models import Product, Category, Menu, Image, Allergy, AllergyProduct, Nutrition, info_list
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Image)
admin.site.register(Allergy)
admin.site.register(AllergyProduct)
admin.site.register(Nutrition)
