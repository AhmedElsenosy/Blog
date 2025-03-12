from django.shortcuts import render
from .models import *

# Create your views here.


def home (request):
    all_blogs = Blog.objects.all().order_by('-id')
    return render(request, 'index.html',{'all_blogs':all_blogs})