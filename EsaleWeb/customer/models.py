from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=500)
    email = models.EmailField(max_length=400)
    profileimage = models.FileField(upload_to='uploads/%Y/%m/%d/')


class Address(models.Model):
    name = models.CharField(max_length=50)
    fullAddress = models.TextField(max_length=500)
    longtiut = models.DecimalField(max_digits=10,decimal_places=8)
    latitut = models.DecimalField(max_digits=10,decimal_places=8)
    createdDate = models.DateTimeField(auto_now_add=True,blank=True)
    customer  = models.ForeignKey(Customer,on_delete=models.CASCADE )