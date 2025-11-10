from django.contrib import admin
from django.urls import path,include
from .views import post_list, single_post_view

urlpatterns = [
    path("", post_list, name="home"),
    path("post/<int:pk>/", single_post_view, name="single_post"),
]