from django.shortcuts import render ,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout

# Create your views here.

def register (request):
    form = RegisterForm()
    if request.user.is_authenticated:
        messages.warning(request , "You are already logged in.")
        return redirect ('home')
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user =form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            new_user = authenticate (request , username = username , password = password)
            login(request , new_user)

            messages.success(request , "Make user successfully..")
            return redirect('home')
            
    return render(request , 'register.html' , {'form' : form})


def login_page (request):
    next = request.GET.get('next')
    if request.user.is_authenticated:
        messages.warning(request , f'You are already logged in, welcome {request.user}')
        return redirect('home')
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request , username = username , password = password)

            if user:
                login(request , user)
                messages.info(request , f'Login successfully! Welcome to our website {username}')
                return redirect ('home')
            
    else:
        form = LoginForm()

    return render (request , 'login.html' , {'form' : form , 'next' : next})
    



def logout_page (request):
    logout(request)
    messages.warning(request , "You are logged out.")
    return redirect('login')
