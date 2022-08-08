from django.contrib import admin
from .models import Product,ProductDetail,Category
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(Category)