from django.db import models

# Create your models here.

#Just For Test ................
class ProductCategory(models.Model):
    name=models.CharField(max_length=20)


class Product(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField
    description=models.TextField(max_length=500,null=True)
    category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)