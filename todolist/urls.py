"""Urls"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('singup/', views.singup, name='singup'),
    path('update/', views.update_profile, name='update_profile'),
    path('todolist/', views.todolist, name='todolist'),
]
