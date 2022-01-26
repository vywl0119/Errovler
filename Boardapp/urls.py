from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Boardapp'

urlpatterns = [
    path('qna_board/', views.qna_board, name='qna_board'),
    path('sol_board/', views.sol_board, name='sol_board'),
 

    path('sol_python/', views.sol_python, name='sol_python'),
    path('sol_django/', views.sol_django, name='sol_django'),
    path('sol_etc/', views.sol_etc, name='sol_etc'),
   
    path('qna_python/', views.qna_python, name='qna_python'),
    path('qna_django/', views.qna_django, name='qna_django'),
    path('qna_etc/', views.qna_etc, name='qna_etc'),
    
    path('mypage/', views.mypage, name='mypage'),
    
    path('search/', views.search, name='search'),
]