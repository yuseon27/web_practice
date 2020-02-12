from django.shortcuts import render
from .models import Blog

# Create your views here.

def home(request) : #{
    blogs = Blog.objects     # Query Set // Method : deal with functions of query set

    return render(request, 'home.html', {'blogs':blogs})   
#}