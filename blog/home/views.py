from django.shortcuts import render


def home(request):
    render(request, 'home.html')

def about(request):
    render(request, 'about.html')

def contact(request):
    render(request, 'contact.html')