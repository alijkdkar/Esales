from django.urls import path
from . import views

urlpatterns =[ 
    path('cartSummery/<int:productID>/',views.cartSummery,name='cartSummery'),
    ]