from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile (models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0 , blank=True)
    img = models.ImageField(upload_to='profile_img/' , height_field ='300' , width_field='300' , blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.user.username