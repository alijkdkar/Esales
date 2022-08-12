from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from product import models
# Create your views here.

def index(requst):
    if requst.method == 'POST':
        pass
    else:    
        viewData = models.Product.objects.all()
        print(viewData[0])
        return render(requst,'index.html',{"list":viewData})