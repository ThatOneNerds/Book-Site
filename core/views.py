from django.shortcuts import render
from .models import *

# Create your views here.

def homepage(request):
    return render(request, 'core/index.html')


def browse(request):
    browse = book.objects.all()
    return render(request, 'core/browse.html', {'browse': browse})

def discussion(request):
    reviews = review.objects.all()
    return render(request, 'core/discuss.html', {'discuss':reviews})




