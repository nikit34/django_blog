from django.contrib import admin
from django.urls import path, include

from .views import (
    home,
    contact,
    about,
    search,
    handle_signup,
    handle_login,
    # handle_logout,
)


urlpatterns = [
    path('', home, name='home'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('search', search, name='search'),
    path('signup', handle_signup, name='handle_signup'),
    path('login', handle_login, name='handle_login'),
    # path('logout', handle_logout, name='handle_logout'),
]