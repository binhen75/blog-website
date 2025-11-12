from django.contrib import admin
from django.urls import path,include
from .views import PostList, SinglePostView, BlogCreateView, UpdatePostView, DeletePostView

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("post/<int:pk>/", SinglePostView.as_view(), name="single_post"),
    path("post_new", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/post_edit", UpdatePostView.as_view(), name="post_edit"),
    path("post/<int:pk>/post_delete", DeletePostView.as_view(), name="post_delete"),
]
