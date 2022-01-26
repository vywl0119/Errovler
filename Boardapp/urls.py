from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Boardapp'

urlpatterns = [
    path('qna_board/', views.qna_board, name='qna_board'),
    path('sol_board/', views.sol_board, name='sol_board'),
    path('scrap/', views.scrap, name='scrap'),
   
]