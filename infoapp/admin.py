from django.contrib import admin

# Register your models here.
from infoapp.models import Product, Category, Menu, Image, Allergy, AllergyProduct, Nutrition, info_list
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

class ProductAdmin(ImportMixin, admin.ModelAdmin):
    pass

class CategoryAdmin(ImportMixin, admin.ModelAdmin):
    pass

class MenuAdmin(ImportMixin, admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Image)
admin.site.register(Allergy)
admin.site.register(AllergyProduct)
admin.site.register(Nutrition)
