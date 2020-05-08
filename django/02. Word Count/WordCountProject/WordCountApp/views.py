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
    word_list  = full_text.split()

    word_dict = {}
    for word in word_list : #{
        if word in word_dict : #{
            word_dict[word] += 1
        else : #{
            word_dict[word] = 1
        #}   
    #}

    p_dict = {'full_text' : full_text, 
            'count' : len(word_list), 
            'word_dict' : word_dict.items()}

    return render(request, 'result.html', p_dict)
#}