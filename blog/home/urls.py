from django.contrib import admin
from django.urls import path, include

from .views import home, contact, about, search


urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('search', search, name='search'),
]