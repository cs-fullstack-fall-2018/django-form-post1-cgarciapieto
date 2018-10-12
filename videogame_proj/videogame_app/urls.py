from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('videogames/', views.index, name='videogame'),
]