from django.shortcuts import render
import pyrebase
from home import urls


config = {
    'apiKey': "AIzaSyA7gaJ36er2Q8PXyiNCiyZ-aktqJqNDTpY",
    'authDomain': "pythonproject-43540.firebaseapp.com",
    'databaseURL': "https://pythonproject-43540.firebaseio.com",
    'projectId': "pythonproject-43540",
    'storageBucket': "pythonproject-43540.appspot.com",
    'messagingSenderId': "390436330738"
}

# initialize app with config
firebase = pyrebase.initialize_app(config)

# authenticate a user
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("dslij@hotmail.com", "Cuba2018")


db = firebase.database()


# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def login(request):
    # return HttpResponse('Hello From Posts')
    context = {
        'email': 'dslij@hotmail.com',
        'pass': 'Cuba2018',
    }
    return render(request, 'authen/login/index.html', context)


def signup(request):
    return render(request, 'authen/signup/index.html')


def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')

    user = auth.sign_in_with_email_and_password(email, passw)

    context = {
        "email": email
    }

    Email = email
    print(Email)

    return render(request, 'welcome.html', context)


def get_users(request):
    users = db.child("users").get()
    return render(request, 'contact/users.html', {'users': users.val()})


def create(request):

    return render(request, 'posts/posts.html')


def postcreate(request):

    work = request.POST.get('work')
    progress = request.POST.get('progress')

    data = {
        "work": work,
        "progress": progress,
        "email": 'dslij@hotmail.com'
    }

    email = 'dslij'

   # db.child('users').child(email).child('reports').set(data)
    addData(email, data)
    return render(request, 'home/index.html')


def addData(email, data):
    db.child('users').child(email).child('reports').set(data)
