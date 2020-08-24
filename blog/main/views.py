from django.shortcuts import render

def blogHome(request):
    render(request, 'home.html')

def blogPost(request, slug):
    render(request, 'blog.html')