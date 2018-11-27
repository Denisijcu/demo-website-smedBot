from django.shortcuts import render
from home import urls
# Create your views here.

from .models import Posts


def index(request):
    return render(request, 'home/index.html')


def login(request):
    return render(request, 'authen/login/index.html')


def signup(request):
    return render(request, 'authen/signup/index.html')


def contact(request):

    posts = Posts.objects.all()[:10]

    context = {
        'title': 'Lates Posts',
        'posts': posts
    }

    return render(request, 'contact/index.html', context)


def details(request):
    #post = Posts.objects.get(id=id)
    post = Posts.objects.all()[:10]

    context = {
        'post': post
    }
    return render(request, 'contact/details.html', context)


def postsign(request):
    return render(request, 'welcome.html')


def create(request):
    return render(request, 'welcome.html')


def postcreate(request):
    return render(request, 'welcome.html')


def about(request):
    return render(request, 'about/index.html')
