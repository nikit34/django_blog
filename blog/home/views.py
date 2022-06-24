from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from .models import Contact
from main.models import Post


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
    posts = Post.objects.filter(title__icontains=query)
    context = {'posts': posts, 'query': query}
    return render(request, 'home/search.html', context=context)

def handle_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, "Password do not match")
            return redirect('home')
        new_user = User.objects.create_user(username, email, pass1)
        new_user.first_name = fname
        new_user.last_name = lname
        new_user.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('home')
    return render(request, 'errors/404.html')

def handle_login(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)

    if user is not None:
        login(request, user)
        messages.success(request, "Successfully Logged In")
        return redirect('home')
    else:
        messages.error(request, "Invalid Credentials, please try again")
        return redirect('home')
    return render(request, 'errors/404.html')

def handle_logout(request):
    logout(request)
    messages.success(request, "Successfully Loggout Out")
    return redirect('home')