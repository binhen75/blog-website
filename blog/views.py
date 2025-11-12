from django.shortcuts import render, get_object_or_404
from .models import Post
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

class PostList(ListView):
    model = Post
    template_name="home.html"

class SinglePostView(DetailView):
    model = Post
    template_name="single_post.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]

class UpdatePostView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields=["title", "body"]
    
class DeletePostView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")

