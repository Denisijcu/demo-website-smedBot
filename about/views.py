from django.shortcuts import render
from home import urls
# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'about/index.html')
