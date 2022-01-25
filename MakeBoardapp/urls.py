from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'MakeBoardapp'

urlpatterns = [
    path('writing/board/', views.board_write, name='writing_board'),
    path('reading/board/<int:pk>', views.board_detail, name='detail_board'),
    path('reading/', views.reading, name='reading'),
    path('#', views.comment, name='comment'),
]