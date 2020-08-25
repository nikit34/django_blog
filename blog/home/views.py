from django.shortcuts import render
from django.contrib import messages

from .models import Contact
from main.models import Post


def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, 'Please fill the form correctly ')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'Your message has been successfully sent')
    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query) > 80:
        posts = Post.objects.none()
    else:
        posts_title = Post.objects.filter(title__icontains=query)
        posts_content = Post.objects.filter(content__icontains=query)
        posts = posts_title.union(posts_content)
    if posts.count() == 0:
        messages.warning(request, "No search result found. Please refine your query")
    posts = Post .objects.filter(title__icontains=query)
    context = {'posts': posts, 'query': query}
    return render(request, 'home/search.html', context=context)