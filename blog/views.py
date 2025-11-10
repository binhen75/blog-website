from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, "home.html", {"posts":posts})

def single_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "single_post.html", {"post":post})