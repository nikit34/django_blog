from django.urls import path
from .views import blog_home, blog_post, post_comment

urlpatterns = [
    path('post_comment', post_comment, name='post_comment'),
    path('', blog_home,  name='blog_home'),
    path('<str:slug>', blog_post,  name='blog_post'),
]