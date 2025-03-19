from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('detail_blog/<int:pk>' , detail , name='detail_blog'),
    path('tags/<slug:tag_slug>' , tags , name='tags'),
    path('comment' , comment , name='comment'),
    path('delete_comment', delete_comment , name='delete_comment'),
    path('edit_blog/<int:pk>', edit_blog , name='edit_blog'),
    path('delete_blog/<int:pk>', delete_blog , name='delete_blog'),
    path('create_post', Create_post , name='create_post'),
]