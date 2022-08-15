from itertools import product
from this import d
from django.shortcuts import render,redirect
from product.models import Product as prod
# Create your views here.

def productDetail(request,pid):
    if request.method =='POST':
        pass
    else:
        print(pid)
        data =  prod.objects.get(id =pid)
        return render(request,'productDetail.html',{'form':data})    