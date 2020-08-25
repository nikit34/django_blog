from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Post, BlogComment


def blog_home(request):
    all_posts = Post.objects.all()
    context = {'posts': all_posts}
    return render(request, 'main/blog_home.html', context=context)

def blog_post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'user': request.user,
    }
    return render(request, 'main/blog_post.html', context=context)

def post_comment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        user = request.user
        post_sno = request.POST['post_sno']
        post = Post.objects.get(sno=post_sno)
        comment = BlogComment(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfullly")
        return redirect(f'/blog/{post.slug}')
    return render(request, 'errors/404.html')