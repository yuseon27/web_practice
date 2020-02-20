from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

# Create your views here.
def home(reqeust) : #{
    blog_all = Blog.objects

    return render(reqeust, 'home.html', {'blog_all':blog_all})
#}

def detail(request, blog_id) : #{
    blog_detail = get_object_or_404(Blog, pk=blog_id)    ## FREMEBER to write pk=

    return render(request, 'detail.html', {'blog_detail':blog_detail})
#}

def new_memo(request) : #{
    return render(request, 'new.html')
#}

def create_memo(request) : #{
    blog = Blog()
    
    blog.title    = request.GET['title']
    blog.body     = request.GET['body']
    blog.pub_date = timezone.datetime.now()

    blog.save()

    return redirect(f'/blog/{blog.id}')
#}