from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'MakeBoardapp'

urlpatterns = [
    path('writing/qna_board/', views.qna_board_write, name='writing_qna_board'),
    path('writing/sol_board/', views.sol_board_write, name='writing_sol_board'),

    path('reading/board/<int:tb_no>', views.detail_board, name='detail_board'),

    path('board/total_comment/', views.total_comment, name='total_comment'),

    path('board/board_delete/<int:tb_no>/', views.board_delete,  name='board_delete'),


    path('board/comment/delete/<int:tb_no>/<int:c_no>', views.comment_delete,  name='comment_delete'),
    path('board/comment/update/<int:tb_no>/<int:c_no>', views.comment_updateurl,  name='comment_updateurl'),
    path('board/comment/update/<int:c_no>', views.comment_update,  name='comment_update'),

    path('reading/scrap/<int:tb_no>/<str:category>', views.scrap, name='scrap'),

    path('reading/like/<int:tb_no>', views.like, name='like'),

    path('reading/sol_like/<int:b_no>', views.sole_like, name='sol_like'),
    path('reading/qna_like/<int:qna_no>', views.qna_like, name='qna_like'),
]