from django.db import models

# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(default='no_photo.png')
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    colors = models.ManyToManyField('ProductColor')

    def __str__(self):
        return self.name


class ProductColor(models.Model):
    color = models.CharField(max_length=200)

    def __str__(self):
        return self.color
