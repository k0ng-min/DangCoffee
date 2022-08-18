from django.db import models

# Create your models here.


from django.db import models

from django.db import models

# Create your models here.

from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.IntegerField(verbose_name= 'app_id', null=True, blank = True)
    korean_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    def __str__(self):
        return self.korean_name


class Image(models.Model):
    image_url = models.URLField(max_length=2000)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

class Allergy(models.Model):
    name = models.CharField(max_length=30)
    products = models.ManyToManyField('Product', through='AllergyProduct')
    def __str__(self):
        return self.name

class AllergyProduct(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)


class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    sodium_mg = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    saturated_fat_g = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    sugars_g = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    protein_g = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    caffeine_mg = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    size = models.CharField(max_length=30)
    product = models.OneToOneField('Product', on_delete=models.CASCADE)

class info_list(models.Model):
    info_list = models.CharField(verbose_name='info_list', max_length=100)
    def __str__(self):
        return self.info_list