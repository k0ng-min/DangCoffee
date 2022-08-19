from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default=None, null=True)
    cafe = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to="admin/image/", null=True, blank=True)

    def __str__(self):
        return self.name