from django.shortcuts import render
from .models import Blog

# Create your views here.

def home(request) : #{
    blogs = Blog.objects    

    return render(request, 'home.html', {'blogs' : blogs})    
#}

# def detail(request, blog_id) : #{
#     blog_detail = get_object_or_404(Blog, pk=#TODO)

#     return render(request, 'detail.html', {'blog_detail':blog_detail})
# #}