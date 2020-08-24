from django.contrib import admin
from django.urls import path, include
from .views import blogHome, blogPost

urlpatterns = [
    path('', blogHome,  name='blogHome'),
    path('<str:slug>', blogPost,  name='blogPost'),
]