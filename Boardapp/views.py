from django.shortcuts import render
from Mainapp.models import Board, QnA_Board
from django.core.paginator import Paginator

# Create your views here.
def board(request):
    qna_boards = QnA_Board.objects
    #모든 글들을 대상으로
    qna_board_list=QnA_Board.objects.all().order_by('-qna_date')
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(qna_board_list,9)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    qna_posts = paginator.get_page(page)
    return render(request, 'Board/board.html', {'qna_boards' : qna_boards, 'qna_posts':qna_posts})

def solboard(request):
    boards = Board.objects
    #모든 글들을 대상으로
    board_list=Board.objects.all().order_by('-b_date')
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(board_list,9)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)
    return render(request, 'Board/solboard.html', {'boards' : boards, 'posts':posts})

def scrap(request):
    return render(request, 'Board/scrap.html')
