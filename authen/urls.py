from django.urls import include, path
from authen import views


urlpatterns = [
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('postsign', views.postsign, name='postsign'),
    path('create', views.create, name="create"),
    path('postcreate', views.postcreate, name="postcreate")
]
