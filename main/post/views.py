from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostForm
from .models import Post

def list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'list.html', {'posts': posts})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_anonymous:
                post.author = "Anonymous"
                post.is_anonymous = request.user.is_anonymous
            else:
                post.author = request.user
            post.save()
            return redirect('post:list')
    else:
        form = PostForm()
    return render(request, 'create.html', {'form': form})

def app_test(request):
    return HttpResponse("Hello, World!")