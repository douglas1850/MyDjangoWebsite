from django.urls import path, include
from . import views

#if the path is ^$, it's the index page, or home page. Seems to be changed now to just using ''
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]