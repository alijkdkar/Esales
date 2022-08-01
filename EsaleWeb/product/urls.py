from django.urls import path
from . import views


urlpatterns = [
    path('productDetail/',views.productDetail,name='pdetail'),
]
