from django.shortcuts import render , get_object_or_404 , redirect
from .models import *
from taggit.models import Tag
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *

# Create your views here.

@login_required
def home (request):
    all_blogs = Blog.objects.all().order_by('-id')
    return render(request, 'index.html',{'all_blogs':all_blogs})


def detail (request,pk):
    blog = Blog.objects.get(id = pk)
    comments = Comment.objects.filter(blog=blog , active = True)
    return render(request, 'detail.html' , {'blog' : blog , 'comments' : comments})

def tags (request,tag_slug):
    all_blogs = Blog.objects.all().order_by('-id')

    if tag_slug:
        tag = get_object_or_404(Tag , slug = tag_slug)
        blogs = all_blogs.filter(tags__in = [tag])
    
    context = {
        'all_blogs' : blogs,
        'tag'  : tag
    }

    return render (request , 'tags.html' , context)


def comment (request):
    if request.POST:
        pk = request.POST.get('id')
        message = request.POST.get('message')
        blog = Blog.objects.get(id = pk)
        user = request.user 

        new_comment = Comment.objects.create(comment = message , active = True , blog = blog , user = user)
        new_comment.save()

        return redirect ('detail_blog' ,pk)
    
def delete_comment (request):
    if request.POST:
        pk = request.POST.get('delete')
        blog_id = request.POST.get('id')
        comment = Comment.objects.get(id = pk)
        comment.delete()
        return redirect('detail_blog',blog_id)
    

def edit_blog (request , pk):
    blog = Blog.objects.get(id = pk)
    if request.POST:
        form = Edit_blog(request.POST , request.FILES , instance = blog)

        if form.errors:
            messages.warning(request , f'{form.errors}')

        if form.is_valid():
            form.save()
            messages.success(request,'Updated Successfully...')
            return redirect('detail_blog' , pk)
        
    else:
        form = Edit_blog(instance = blog)
        
    return render(request , 'edit_post.html' , {'form':form , 'blog':blog})


def delete_blog (request , pk):
    blog = Blog.objects.get(id = pk).delete()
    messages.success(request , 'Deleted Successfully...')
    return redirect('home')
