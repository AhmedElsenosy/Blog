from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([Blog , Comment , About , ContactInfo , ContactUs])
