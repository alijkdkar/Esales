from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

def index(requst):
    viewData={'name':'shahzaD'}
    # messages.success(requst,"hi",'success')
    return render(requst,'index.html',context=viewData)