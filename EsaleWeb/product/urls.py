from django.urls import path
from . import views


urlpatterns = [
    path('productDetail/<int:pid>/',views.productDetail,name='pdetail'),
]
