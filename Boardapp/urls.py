from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Boardapp'

urlpatterns = [
    path('board/', views.board, name='board'),
    path('scrap/', views.scrap, name='scrap'),
   
]