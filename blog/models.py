from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.

class Blog (models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='BlogImg/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.title
