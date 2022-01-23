from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Mainapp'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('join/', views.join, name='join'),
    path('login/', views.login, name='login'),
]