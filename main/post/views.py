from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import PostForm, CommentForm
from .models import Post, Comment

def list(request):
    posts = Post.objects.all().order_by('-created_at')
    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'list.html', {'posts': posts,
                                         'comments': comments})

def createPost(request):
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

def detail(request, id):
    template_name = 'detail.html'
    post = get_object_or_404(Post, pk=id)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            if request.user.is_anonymous:
                new_comment.author = "Anonymous"
                new_comment.is_anonymous = request.user.is_anonymous
            else:
                new_comment.author = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def app_test(request):
    return HttpResponse("Hello, World!")