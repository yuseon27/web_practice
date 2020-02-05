from django.shortcuts import render

# Create your views here.

def home(request) : #{
    return render(request, 'home.html')
#}


def about(request) : #{
    return render(request, 'about.html')
#}


def result(request) : #{
    full_text  = request.GET['full_text']
    count = len(full_text.split())
    p_dict = {'full_text' : full_text, 'count' : count}
    return render(request, 'result.html', p_dict)
#}