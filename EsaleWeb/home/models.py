from django.db import models

# Create your models here.
class widget(models.Model):
    name = models.TextField(max_length=100)
    isAvailble = models.BooleanField(null=True)
