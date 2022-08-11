from django.contrib import admin

# Register your models here.
from infoapp.models import Product, Category, Menu, Image, Allergy, AllergyProduct, Nutrition, info_list

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Image)
admin.site.register(Allergy)
admin.site.register(AllergyProduct)
admin.site.register(Nutrition)
admin.site.register(info_list)
