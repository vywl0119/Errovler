from django.shortcuts import render
from Mainapp.models import Board, QnA_Board
from django.core.paginator import Paginator

# Create your views here.
def qna_board(request):
    qna_boards = QnA_Board.objects
    #모든 글들을 대상으로
    qna_board_list=QnA_Board.objects.all().order_by('-qna_date')
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(qna_board_list,9)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    qna_posts = paginator.get_page(page)
    return render(request, 'Board/qna_board.html', {'qna_boards' : qna_boards, 'qna_posts':qna_posts})

def sol_board(request):
    boards = Board.objects
    #모든 글들을 대상으로
    board_list=Board.objects.all().order_by('-b_date')
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(board_list,9)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)
    return render(request, 'Board/sol_board.html', {'boards' : boards, 'posts':posts})

def mypage(request):
    return render(request, 'Board/mypage.html')




def sol_python(request):
    boards = Board.objects
    #모든 글들을 대상으로
    board_list=Board.objects.filter(category='python').order_by('-b_date')
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(board_list,9)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)
    return render(request, 'Board/sol_board.html', {'boards' : boards, 'posts':posts})

def sol_django(request):
    boards = Board.objects
    #모든 글들을 대상으로
    board_list=Board.objects.filter(category='Django').order_by('-b_date')
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(board_list,9)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)
    return render(request, 'Board/sol_board.html', {'boards' : boards, 'posts':posts})

def sol_etc(request):
    boards = Board.objects
    #모든 글들을 대상으로
    board_list=Board.objects.filter(category='etc').order_by('-b_date')
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(board_list,9)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)
    return render(request, 'Board/sol_board.html', {'boards' : boards, 'posts':posts})



def qna_python(request):
    qna_boards = QnA_Board.objects
    #모든 글들을 대상으로
    qna_board_list=QnA_Board.objects.filter(category='python').order_by('-qna_date')
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(qna_board_list,9)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    qna_posts = paginator.get_page(page)
    return render(request, 'Board/qna_board.html', {'qna_boards' : qna_boards, 'qna_posts':qna_posts})

def qna_django(request):
    qna_boards = QnA_Board.objects
    #모든 글들을 대상으로
    qna_board_list=QnA_Board.objects.filter(category='Django').order_by('-qna_date')
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(qna_board_list,9)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    qna_posts = paginator.get_page(page)
    return render(request, 'Board/qna_board.html', {'qna_boards' : qna_boards, 'qna_posts':qna_posts})

def qna_etc(request):
    qna_boards = QnA_Board.objects
    #모든 글들을 대상으로
    qna_board_list=QnA_Board.objects.filter(category='etc').order_by('-qna_date')
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(qna_board_list,9)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    qna_posts = paginator.get_page(page)
    return render(request, 'Board/qna_board.html', {'qna_boards' : qna_boards, 'qna_posts':qna_posts})
