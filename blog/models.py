from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse


# Create your models here.

class Blog (models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='BlogImg/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()

    def get_related_posts (self):
        return Blog.objects.filter(tags__in = self.tags.all()).distinct()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail_blog", kwargs={"pk": self.pk})
    

class Comment (models.Model):
    comment = models.CharField( max_length=2000)
    user = models.ForeignKey(User, on_delete=models.SET_NULL , null = True)
    active = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE , related_name='comment')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.user.username


class About (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img = models.ImageField(upload_to='about/')
    background = models.TextField()
    team_work = models.TextField()
    our_core_value = models.TextField()

    def __str__(self):
        return self.title
