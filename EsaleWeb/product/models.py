from ast import mod
from pyexpat import model
from unicodedata import name
from django.db import models
from django.contrib import admin

# Create your models here.

class Category(models.Model):
    parent  = models.ForeignKey('self', blank=True, null=True, related_name='children',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    

class Product(models.Model):
    name  = models.CharField(max_length=100)
    codeNo = models.CharField(max_length=20)
    description = models.TextField(max_length=8000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    active = models.BooleanField(default=True)
    orginal = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='products/%Y/%m/%d/')

class ProductDetail(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    detailName = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

class Color(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    colorName = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    
class size(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    sizeName = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
        
