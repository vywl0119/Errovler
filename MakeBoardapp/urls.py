from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'MakeBoardapp'

urlpatterns = [
    path('writing/qna_board/', views.qna_board_write, name='writing_qna_board'),
    path('writing/solboard/', views.solboard_write, name='writing_board'),
    path('reading/board/<int:b_no>', views.board_detail, name='detail_board'),
    path('reading/qna_board/<int:qna_no>', views.qna_board_detail, name='qna_detail_board'),
    path('#', views.comment, name='comment'),
    path('#', views.qna_comment, name='qna_comment'),
]