from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name='detail'),
    path('new/', views.new_memo, name="new"),
    path('create/', views.create_memo, name="create"),
    path('newblog/', views.blogpost, name="newblog"),
    path('newform/', views.anypost, name="newform"),
]