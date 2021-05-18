from django.contrib import admin
from django.urls import path
import blogapp.views



urlpatterns = [
    path('blog/<int:blog_id>', blogapp.views.detail, name="detail"),
    path('blog/new/', blogapp.views.new, name="new"), 
    path('blog/create', blogapp.views.create, name="create"),
]