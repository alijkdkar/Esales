from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requst):
    viewData={'name':'shahzaD'}
    return render(requst,'index.html',context=viewData)