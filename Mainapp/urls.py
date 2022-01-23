from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Mainapp'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
]