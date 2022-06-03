from django.shortcuts import render
from .models import *

# Create your views here.

def homepage(request):
    return render(request, 'core/home.html')


def browse(request):
    browse = Book.objects.all()
    return render(request, 'core/browse.html', {'browse': browse})

def discussion(request):
    reviews = Review.objects.all()
    return render(request, 'core/discuss.html', {'discuss':reviews})




