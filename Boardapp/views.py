from unicodedata import category
from django.shortcuts import render
from nbformat import write
from Mainapp.models import Total_Board, Total_Comment, Total_Scrap
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def qna_board(request):
    qna_boards = Total_Board.objects.filter(type='질문')
    #모든 글들을 대상으로
    qna_board_list=Total_Board.objects.filter(type='질문').order_by('-tb_no')
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
    sol_board_list=Total_Board.objects.filter(type='해결').order_by('-tb_no')
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(sol_board_list,9)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    sol_posts = paginator.get_page(page)
    return render(request, 'Board/sol_board.html', {'sol_boards' : sol_boards, 'sol_posts':sol_posts})

def scrap_page(request):
        path = "../../../media/"
        profile = request.user.last_name
        profile_path = path + profile
        user = request.user.username
        user_scrap = Total_Scrap.objects.filter(writer=user)
        
        tag_list = ['Python', 'Django', 'etc']
        scrap_cnt = []
        
        for tag in tag_list:
            cnt = user_scrap.filter(category=tag).count()
            scrap_cnt.append(cnt)
            
        scrap = Total_Scrap.objects.all()
        #모든 글들을 대상으로
        scrap_list=Total_Scrap.objects.filter(writer=user).order_by('-s_date')
        #블로그 객체 세 개를 한 페이지로 자르기
        paginator = Paginator(scrap_list,9)
        #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
        page = request.GET.get('page')
        #request된 페이지를 얻어온 뒤 return 해 준다
        scrap_posts = paginator.get_page(page)

        print(scrap_posts)
            
        context = { 'scrap_cnt' : scrap_cnt,
                    'scrap' : scrap,
                    'scrap_posts' : scrap_posts,
                    'scrap_list':scrap_list,
                    'currentprofile' : profile_path
                }
        
        return render(request, 'Board/scrap.html', context)


def mypage(request):        
        path = "../../../media/"
        profile = request.user.last_name
        profile_path = path + profile 
        user = request.user.first_name
        user_write = Total_Board.objects.filter(writer=user)
        
        tag_list = ['Python', 'Django', 'etc']
        write_cnt = []
        
        for tag in tag_list:
            cnt = user_write.filter(category=tag).count()
            write_cnt.append(cnt)
            
        write = Total_Board.objects.all()
        #모든 글들을 대상으로
        write_list=Total_Board.objects.filter(writer=user).order_by('-tb_no')
        #블로그 객체 세 개를 한 페이지로 자르기
        paginator = Paginator(write_list,9)
        #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
        page = request.GET.get('page')
        #request된 페이지를 얻어온 뒤 return 해 준다
        write_posts = paginator.get_page(page)

        print(write_posts)
            
        context = { 'write_cnt' : write_cnt,
                    'write' : write,
                    'write_posts' : write_posts,
                    'write_list':write_list,
                    'currentprofile' : profile_path
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

def total_category(request, category):
    total_search_boards = Total_Board.objects.filter(category=category).order_by('-tb_date')
    q = request.POST.get('q', "") 

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


def scrap_category(request, category):
    path = "../../../media/"
    profile = request.user.last_name
    profile_path = path + profile
        
    user = request.user.first_name

    user_scrap = Total_Scrap.objects.filter(writer=user)
        
    tag_list = ['Python', 'Django', 'etc']
    scrap_cnt = []
        
    for tag in tag_list:
        cnt = user_scrap.filter(category=tag).count()
        scrap_cnt.append(cnt)

    print(category)
    scrap_boards = Total_Scrap.objects.filter(writer=user)
    #모든 글들을 대상으로
    scrap_board_list=Total_Scrap.objects.filter(writer=user,category=category).order_by('-s_date')
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(scrap_board_list,9)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    scrap_posts = paginator.get_page(page)
    return render(request, 'Board/scrap.html', {'scrap_list' : scrap_board_list, 'scrap_posts':scrap_posts,'scrap_cnt':scrap_cnt, 'currentprofile' : profile_path})


def write_category(request, category):
    path = "../../../media/"
    profile = request.user.last_name
    profile_path = path + profile
    user = request.user.first_name

    user_write = Total_Board.objects.filter(writer=user)
        
    tag_list = ['Python', 'Django', 'etc']
    write_cnt = []
        
    for tag in tag_list:
        cnt = user_write.filter(category=tag).count()
        write_cnt.append(cnt)

    print(category)
    write_boards = Total_Board.objects.filter(writer=user)
    #모든 글들을 대상으로
    write_board_list=Total_Board.objects.filter(writer=user,category=category).order_by('-tb_date')
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(write_board_list,9)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    write_posts = paginator.get_page(page)
    return render(request, 'Board/mypage.html', {'write_list' : write_board_list, 'write_posts':write_posts,'write_cnt':write_cnt, 'currentprofile' : profile_path})