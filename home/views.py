from django.shortcuts import render


# Create your views here.


def index(request):
    # return HttpResponse('Hello From Posts')
      context = {
        'title': 'Home Page'
      }
      return render(request, 'home/index.html', context)


def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'home/index.html', context)
