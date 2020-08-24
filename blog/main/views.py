from django.shortcuts import render

def blogHome(request):
    return render(request, 'main/blogHome.html')

def blogPost(request, slug):
    return render(request, 'main/blogPost.html')