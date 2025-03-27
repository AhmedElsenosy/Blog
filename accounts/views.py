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


def login_page(request):
    next = request.GET.get('next')
    if request.user.is_authenticated:
        messages.warning(request, f'You are already logged in, welcome {request.user}')
        return redirect('home')
    
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.info(request, f'Login successfully! Welcome to our website {username}')
                if next:
                    return redirect(next)
                return redirect('home')
            else:
                # Add error message for invalid credentials
                messages.error(request, 'Invalid username or password')
        else:
            # Add error message for form validation errors
            messages.error(request, 'Please correct the errors below')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'next': next})
    



def logout_page (request):
    logout(request)
    messages.warning(request , "You are logged out.")
    return redirect('login')

def change_password (request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.POST:
        form = ChangePassForm(request.user , request.POST)
        if form.is_valid():
            user = form.save()
            login(request ,user)
            messages.success(request , "Password changed successfully.")
            return redirect('home')
    else:
        form = ChangePassForm(request.user)
    return render(request , 'change_password.html' , {'form' : form})

def create_profile(request , pk):
    profile = Profile.objects.get(id = pk)
    if request.POST:
        form = ProfileForm(request.POST , request.FILES , instance = profile)
        if form.errors:
            messages.error(request , f'{form.errors}')
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            new.save()
            messages.success(request , "Profile Updated successfully.")
            return redirect('profile' , profile.id)
    else:
        form = ProfileForm(instance = profile)
    return render(request , 'profile.html' , {'form' : form , 'profile' : profile})
