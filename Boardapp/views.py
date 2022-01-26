from unicodedata import category
from django.shortcuts import render
from Mainapp.models import Board, QnA_Board
from django.core.paginator import Paginator
from django.db.models import Q

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

    # category_list = QnA_Board.objects.values('category')
    # seen = []
    # for key, val in category_list.items():
    #     if val not in seen:
    #         seen.append(val)
            
    # for i in seen:
    #     print(i)

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


def search(request):
    qna_search_boards = QnA_Board.objects.all().order_by('-qna_date')
    q = request.POST.get('q', "") 

    if q:
        qna_search_boards = qna_search_boards.filter(title__icontains=q)
        return render(request, 'Board/search_board.html', {'qna_search_boards' : qna_search_boards, 'q' : q})
    
    else:
        return render(request, 'Board/search_board.html')

def qna_category(request, category):
    qna_boards = QnA_Board.objects
    #모든 글들을 대상으로
    qna_board_list=QnA_Board.objects.filter(category=category).order_by('-qna_date')
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(qna_board_list,9)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    qna_posts = paginator.get_page(page)
    return render(request, 'Board/qna_board.html', {'qna_boards' : qna_boards, 'qna_posts':qna_posts})

def sol_category(request, category):
    boards = Board.objects
    #모든 글들을 대상으로
    board_list=Board.objects.filter(category=category).order_by('-b_date')
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(board_list,9)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)
    return render(request, 'Board/sol_board.html', {'boards' : boards, 'posts':posts})