from django.urls import path
from django.views import View
from . import views


urlpatterns = [
    path('signup/',views.signup,name='signUpAddress'),
    path('login/',views.login,name='lognAddress')
]