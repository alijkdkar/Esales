from itertools import product
from this import d
from django.shortcuts import render,redirect
from product.models import Product as prod,ProductDetail as pd,Color ,size as siz
# Create your views here.

def productDetail(request,pid):
    if request.method =='POST':
        pass
    else:
        print(pid)
        product =  prod.objects.get(id =pid)
        detail = pd.objects.filter(product =product)
        color = Color.objects.filter(product =product)
        size = siz.objects.filter(product=product)
        product.prop = detail
        product.color = color
        product.size = size
        
        return render(request,'productDetail.html',{'form':product})    