from django.db import models

# Create your models here.

from django.db import models

class Product(models.Model):
    product_id = models.IntegerField(verbose_name= 'app_id', null=True, blank = True)
    category = models.CharField(max_length=50)
    korean_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    thumbnail = models.ImageField()
    allergy = models.CharField(max_length=30)
    kcal = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    sodium_mg = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    saturated_fat_g = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    sugars_g = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    protein_g = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    caffeine_mg = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    size = models.CharField(max_length=30)

    def __str__(self):
        return self.korean_name

    # korean_name로 정렬
    class Meta:
        ordering = ["korean_name"]

class category_list(models.Model):
    category_list = models.CharField(verbose_name='category_list', max_length=100)
    def __str__(self):
        return self.category_list