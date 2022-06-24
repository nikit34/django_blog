from django.shortcuts import render, redirect
from django.contrib import messages

from .templatetags import extras
from .models import Post, BlogComment


def blog_home(request):
    all_posts = Post.objects.all()
    context = {'posts': all_posts}
    return render(request, 'main/blog_home.html', context=context)

def blog_post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context = {
        'post': post,
        'comments': comments,
        'user': request.user,
        'replyDict': replyDict
    }
    return render(request, 'main/blog_post.html', context=context)

def post_comment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        user = request.user
        post_sno = request.POST['post_sno']
        post = Post.objects.get(sno=post_sno)
        parent_sno = request.POST["parent_sno"]
        if parent_sno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent = BlogComment.objects.get(sno=parent_sno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        return redirect(f'/{post.slug}')
    return render(request, 'errors/404.html')