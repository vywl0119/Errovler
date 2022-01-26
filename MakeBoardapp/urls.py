from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'MakeBoardapp'

urlpatterns = [
    path('writing/qna_board/', views.qna_board_write, name='writing_qna_board'),
    path('writing/solboard/', views.solboard_write, name='writing_board'),


    path('reading/sol_board/<int:b_no>', views.sol_detail_board, name='sol_detail_board'),
    path('reading/qna_board/<int:qna_no>', views.qna_detail_board, name='qna_detail_board'),
     path('reading/scrap/<int:s_no>', views.scrap_qna, name='scrap_qna'),


    path('board/sol_comment/', views.sol_comment, name='sol_comment'),
    path('board/qna_comment/', views.qna_comment, name='qna_comment'),


    path('board/sol_delete/<int:b_no>/', views.sol_delete,  name='sol_delete'),
    path('board/qna_delete/<int:qna_no>/', views.qna_delete,  name='qna_delete'),


    path('board/sol_comment/delete/<int:b_no>/<int:c_no>', views.sol_comment_delete,  name='sol_comment_delete'),
    path('board/sol_comment/update/<int:b_no>/<int:c_no>', views.sol_comment_updateurl,  name='sol_comment_updateurl'),
    path('board/sol_comment/update/<int:c_no>', views.sol_comment_update,  name='sol_comment_update'),

    path('board/qna_comment/delete/<int:qna_no>/<int:c_no>', views.qna_comment_delete,  name='qna_comment_delete'),
    path('board/qna_comment/update/<int:qna_no>/<int:c_no>', views.qna_comment_updateurl,  name='qna_comment_updateurl'),
    path('board/qna_comment/update/<int:c_no>', views.qna_comment_update,  name='qna_comment_update'),
]