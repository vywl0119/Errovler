from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Boardapp'

urlpatterns = [
    path('qna_board/', views.qna_board, name='qna_board'),
    path('sol_board/', views.sol_board, name='sol_board'),

    path('qna_category/<str:category>', views.qna_category, name='qna_category'),
    path('sol_category/<str:category>', views.sol_category, name='sol_category'),
    path('total_category/<str:category>', views.total_category, name='total_category'),
    path('scrap_category/<str:category>', views.scrap_category, name='scrap_category'),

    
    path('scrap_page/', views.scrap_page, name='scrap_page'),
    path('profile/', views.mypage, name='profile'),
    

    path('total_search/', views.total_search, name='total_search'),

]