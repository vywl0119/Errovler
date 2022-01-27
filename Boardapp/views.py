from unicodedata import category
from django.shortcuts import render
<<<<<<< HEAD
from Mainapp.models import Total_Board, Total_Comment, Total_Scrap
=======
from Mainapp.models import Board, QnA_Board, Scrap
>>>>>>> 6d47c4cf24804b4d3b7f5df9319621b25fab46ab
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def qna_board(request):
    qna_boards = Total_Board.objects.filter(type='질문')
    #모든 글들을 대상으로
    qna_board_list=Total_Board.objects.filter(type='질문').order_by('-tb_date')
    #블로그 객체 9개를 한 페이지로 자르기
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
    sol_boards = Total_Board.objects.filter(type='해결')
    #모든 글들을 대상으로
    sol_board_list=Total_Board.objects.filter(type='해결').order_by('-tb_date')
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(sol_board_list,9)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    sol_posts = paginator.get_page(page)
    return render(request, 'Board/sol_board.html', {'sol_boards' : sol_boards, 'sol_posts':sol_posts})

def mypage(request):
<<<<<<< HEAD
        user = request.user.first_name
        user_scrap = Total_Scrap.objects.filter(writer=user)
        
        tag_list = ['Python', 'Django', 'etc']
        scrap_cnt = []
        
        for tag in tag_list:
            cnt = user_scrap.filter(category=tag).count()
            scrap_cnt.append(cnt)
            
        context = { 'scrap_cnt' : scrap_cnt, 
                }
        
        return render(request, 'Board/mypage.html', context)

def qna_category(request, category):
    qna_boards = Total_Board.objects.filter(type='질문')
    #모든 글들을 대상으로
    qna_board_list=Total_Board.objects.filter(type='질문',category=category).order_by('-tb_date')
    #블로그 객체 9개를 한 페이지로 자르기
    paginator = Paginator(qna_board_list,9)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    qna_posts = paginator.get_page(page)
    return render(request, 'Board/qna_board.html', {'qna_boards' : qna_boards, 'qna_posts':qna_posts})



def sol_category(request, category):
    sol_boards = Total_Board.objects.filter(type='해결')
    #모든 글들을 대상으로
    sol_board_list=Total_Board.objects.filter(type='해결',category=category).order_by('-tb_date')
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(sol_board_list,9)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    sol_posts = paginator.get_page(page)
    return render(request, 'Board/sol_board.html', {'sol_boards' : sol_boards, 'sol_posts':sol_posts})
=======
    user = request.user.first_name
    user_scrap = Scrap.objects.filter(writer=user)
    
    tag_list = ['Python', 'Django', 'etc']
    scrap_cnt = []
    
    for tag in tag_list:
        cnt = user_scrap.filter(category=tag).count()
        scrap_cnt.append(cnt)
        
    context = { 'scrap_cnt' : scrap_cnt, 
               }
    
    return render(request, 'Board/mypage.html', context)
>>>>>>> 6d47c4cf24804b4d3b7f5df9319621b25fab46ab

def total_category(request, category):
    total_search_boards = Total_Board.objects.filter(category=category).order_by('-tb_date')
    q = request.POST.get('q', "") 

<<<<<<< HEAD
    if q:
        print('q 들어옴')
        board_list = total_search_boards = total_search_boards.filter(
            Q(title__icontains = q) | #제목
            Q(contents__icontains = q) | #내용
            Q(writer__icontains = q) #글쓴이
        )
            #블로그 객체 9개를 한 페이지로 자르기
        paginator = Paginator(board_list,9)
        #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
        page = request.GET.get('page')
        #request된 페이지를 얻어온 뒤 return 해 준다
        posts = paginator.get_page(page)
        return render(request, 'Board/total_search_board.html', {'boards' : board_list, 'posts':posts, 'q':q})

    else:
        return render(request, 'Mainapp:home')



def total_search(request):
    total_search_boards = Total_Board.objects.all().order_by('-tb_date')
    q = request.POST.get('q', "") 

    if q:
        board_list = total_search_boards = total_search_boards.filter(
            Q(title__icontains = q) | #제목
            Q(contents__icontains = q) | #내용
            Q(writer__icontains = q) #글쓴이
        )
            #블로그 객체 9개를 한 페이지로 자르기
        paginator = Paginator(board_list,9)
        #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
        page = request.GET.get('page')
        #request된 페이지를 얻어온 뒤 return 해 준다
        posts = paginator.get_page(page)
        return render(request, 'Board/total_search_board.html', {'boards' : board_list, 'posts':posts, 'q':q})

    else:
        return render(request, 'Mainapp:home')
=======
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
>>>>>>> 6d47c4cf24804b4d3b7f5df9319621b25fab46ab
