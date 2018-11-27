from django.urls import include, path
from contact import views


urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('details', views.details, name='details'),
]
