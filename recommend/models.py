from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    cafe = models.ForeignKey('Cafe', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Cafe(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
