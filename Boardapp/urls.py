from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Boardapp'

urlpatterns = [
    path('qna_board/', views.qna_board, name='qna_board'),
    path('sol_board/', views.sol_board, name='sol_board'),

    path('qna_category/<str:category>', views.qna_category, name='qna_category'),
    path('sol_category/<str:category>', views.sol_category, name='sol_category'),
    
    path('mypage/', views.mypage, name='mypage'),
    
    path('search/', views.search, name='search'),
]