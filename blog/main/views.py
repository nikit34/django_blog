from django.shortcuts import render

def blogHome(request):
    return render(request, 'home.html')

def blogPost(request, slug):
    return render(request, 'blog.html')