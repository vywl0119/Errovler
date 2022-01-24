from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'MakeBoardapp'

urlpatterns = [
    path('reading/', views.reading, name='reading'),
    path('writing/', views.writing, name='writing'),
]