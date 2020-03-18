from django.shortcuts import render
from .models import Pictures

# Create your views here.

def thumbnail(request) : #{
    pictures = Pictures.objects
    return render(request, 'thumbnail.html', {'pictures':pictures})
#}