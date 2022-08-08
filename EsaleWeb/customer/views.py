from django.shortcuts import render,redirect
from .froms import UserRegistertionForm,UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin,logout as auth_logout
from django.contrib import messages
# Create your views here.


def signup(requst):
    if requst.method == 'POST':
        form = UserRegistertionForm(requst.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password']!=cd["confirmPassword"]:
                messages.success(requst,'confirm password is wrong','danger')
                return render(requst,'signUp.html',{'form':form})

            user = User.objects.create_user(cd['username'],cd['email'],cd['password'])
            user.first_name = cd['firstName']
            user.last_name = cd['lastName']
            user.save() 
            print('sss')
            messages.success(requst,'user added successfuly','success')
            return redirect('home')


    else:
        form = UserRegistertionForm()
    return render(requst,'signUp.html',{'form':form})



def login(requst):
    if requst.method == 'POST':
        form = UserLoginForm(requst.POST)
        if form.is_valid():
            cd = form.cleaned_data
            userlogind = authenticate(request= requst,username=cd['username'],password= cd['password'])
            print(userlogind)
            if userlogind is not None:
                authlogin(requst,userlogind)
                messages.success(requst,'you logined successfuly','success')
                return redirect('home')
            else:
                messages.error(requst,'username or password is wrong','danger')
                
    else:
        form = UserLoginForm()
    return render(requst,'login.html',{'form':form})    


def logout(request):
    auth_logout(request)
    messages.success(request,'user logouted succefully','success')
    return redirect('home')