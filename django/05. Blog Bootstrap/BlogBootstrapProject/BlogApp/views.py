from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .blog_form import BlogPost
from .form import AnyPost

# Create your views here.
def home(request) : #{
    blog_all = Blog.objects

    # For all Blog ojbects
    blog_list = Blog.objects.all()
    # Split the objects into page that has 3 objects
    paginator = Paginator(blog_list, 3)
    # Find what is the requested page
    page_num = request.GET.get('page')
    # Return requested page
    posts = paginator.get_page(page_num)

    return render(request, 'home.html', {'blog_all':blog_all, 'posts':posts})
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

def blogpost(request) : #{
    # 1. Process input   -> POST
    if request.method == "POST" : #{
        form = BlogPost(request.POST)
        if form.is_valid() : #{
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()

            return redirect('home')
        #}

    #}
    
    # 2. Show empty page => GET
    else : #{
        form = BlogPost()
        return render(request, 'new.html', {'form':form})
    #}
      
#}

def anypost(request) : #{
    # 1. Process input   -> POST
    if request.method == "POST" : #{
        form = AnyPost(request.POST)
        if form.is_valid() : #{
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()

            return redirect('home')
        #}

    #}
    
    # 2. Show empty page => GET
    else : #{
        form = AnyPost()
        return render(request, 'new.html', {'form':form})
    #}
      
#}