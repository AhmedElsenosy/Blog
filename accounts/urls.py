from django.urls import path
from .views import *

urlpatterns = [
    path('register' , register , name='register'),
    path('login/' , login_page , name='login'),
    path('logout/' , logout_page , name='logout'),
    path('change-pass/' , change_password , name='change-pass'),
]
