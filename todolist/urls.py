"""Urls"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('update/', views.update_profile, name='update_profile'),
    path('todolist/', views.todolist, name='todolist'),
]
