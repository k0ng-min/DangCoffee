from django.contrib import admin
from .models import Product
# Register your models here.

from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

from .models import Product

class ProductAdmin(ImportExportMixin, admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
