from django.shortcuts import render

from .models import Post


def blogHome(request):
    all_posts = Post.objects.all()
    context = {'posts': all_posts}
    return render(request, 'main/blogHome.html', context=context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request, 'main/blogPost.html', context=context)