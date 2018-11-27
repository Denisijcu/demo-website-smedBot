from django.urls import include, path
from about import views


urlpatterns = [
    path('about', views.about, name='about')
]
