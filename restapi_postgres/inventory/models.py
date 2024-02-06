from django.db import models

# Create your models here.

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productDescription = models.TextField()
    productBrand = models.CharField(max_length=200)
    stockMin = models.IntegerField()
    stockMax = models.IntegerField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    
