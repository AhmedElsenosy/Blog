from django.shortcuts import render ,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate , login

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
