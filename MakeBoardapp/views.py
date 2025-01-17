from unicodedata import category
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from datetime import date, datetime, timedelta

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from matplotlib.style import context

from .forms import BoardPost
from Mainapp.models import Total_Comment, Total_Scrap, Total_Board, Total_Like_Board
from django.contrib.auth.models import User
from django.utils import timezone


def detail_board(request, tb_no):
    board_detail = Total_Board.objects.get(tb_no = tb_no)
    comment_list = Total_Comment.objects.filter(tb_no = tb_no)
    comment_cnt = len(comment_list)

    username = request.user.username
    
    like = Total_Like_Board.objects.filter(tb_no=tb_no, writer=username)
    like_yn = ''
    if like:
        like_yn = 'y'
    else:
        like_yn = 'n'
    print(like_yn)    
    
    
    scrap = Total_Scrap.objects.filter(tb_no=tb_no, writer=username)
    scrap_yn = ''
    if scrap:
        scrap_yn = 'y'
    else:
        scrap_yn = 'n'
    print(scrap_yn)   

    context = {'board_detail': board_detail,
                'comment_list': comment_list,
                'comment_cnt': comment_cnt,
                'like_yn':like_yn,
                'scrap_yn':scrap_yn,
                } 
    
   
    
    
    response = render(request, 'MakeBoard/detail_board.html',context)
    
    # 조회수
    expire_date, now = datetime.now(), datetime.now()
    expire_date += timedelta(days=1)
    expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
    expire_date -= now
    max_age = expire_date.total_seconds()
    
    cookie_value = request.COOKIES.get('hitboard', '_')
    
    if f'_{tb_no}_' not in cookie_value:
        cookie_value += f'{tb_no}_'
        response.set_cookie('hitboard', value=cookie_value, max_age=max_age, httponly=True)
        board_detail.view += 1
        board_detail.save()

    return response



def writing_board(request, type):
    login_session = request.session.get('login_session','')
    context = {'login_session': login_session}

    if request.method == 'GET':
        write_form = BoardPost()
        context['forms'] = write_form
        return render(request, 'MakeBoard/writing.html', context)

    elif request.method == 'POST':
        
        write_form = BoardPost(request.POST)
        if write_form.is_valid():
            writer = request.user.first_name
            username = request.user.username
            print(username)
            total_board = Total_Board(
                title=write_form.title,
                contents=write_form.contents,
                writer =writer,
                category=write_form.category,
                type=write_form.type,
                username=username
            )
            total_board.save()
            if type == '해결':
                return redirect('/Board/sol_board')
            else:
                return redirect('/Board/qna_board')
        else:
            context['forms'] = write_form
            if write_form.errors:
                for value in write_form.errors.values():
                    context['error'] = value
            return render(request, 'MakeBoard/writing_error.html', context)

def update_board(request, tb_no):
    login_session = request.session.get('login_session','')
    context = {'login_session': login_session}
    board = Total_Board.objects.get(tb_no=tb_no)
    tb_date = datetime.now()
    writer = request.user.first_name
    print(writer)

    if request.method == 'GET':
        write_form = BoardPost(instance=board)
        context['forms'] = write_form
        return render(request, 'MakeBoard/writing.html', context)

    elif request.method == 'POST':
       
        write_form = BoardPost(request.POST )
        if write_form.is_valid():
            board.tb_date = tb_date
            board.writer = writer
            board.title = write_form.title
            board.contents=write_form.contents
            board.category=write_form.category,
            board.type=write_form.type


            board.save()
           
            return redirect('MakeBoardapp:detail_board' , tb_no)

        else:
            context['forms'] = write_form
            if write_form.errors:
                for value in write_form.errors.values():
                    context['error'] = value
            return render(request, 'MakeBoard/writing_error.html', context)





def total_comment(request):
    if request.method == 'POST':
        contents = request.POST.get('contents')
        tb_no = request.POST.get('tb_no')
        print(tb_no, contents)
        if contents:
            try:
                print(contents)
                nickname = request.user.first_name
                username = request.user.username

                comment = Total_Comment.objects.create(tb_no_id=tb_no, contents=contents, writer = nickname, username=username)
                comment.save()

                board = Total_Board.objects.get(tb_no=tb_no)
                board.comment_cnt = board.comment_cnt+1
                board.save()
               
                return redirect('MakeBoardapp:detail_board' , tb_no)
            except:
                return redirect('MakeBoardapp:detail_board' , tb_no)
        else:
            return redirect('MakeBoardapp:detail_board' , tb_no)
            




def board_delete(request, tb_no):
    try:
        board = Total_Board.objects.get(tb_no=tb_no)
        print('이상')
        if board.type == '질문':
            print('질문')
            board.delete()
            return redirect('Boardapp:qna_board')
        else:
            print('해결')
            board.delete()
            return redirect('Boardapp:sol_board')
    except:
        return redirect('MakeBoardapp:detail_board' , tb_no)



def comment_delete(request, tb_no, c_no):
    try:
      
        comment = Total_Comment.objects.get(c_no=c_no)
        comment.delete()

        board = Total_Board.objects.get(tb_no=tb_no)
        board.comment_cnt = board.comment_cnt-1
        board.save()


        return redirect('MakeBoardapp:detail_board' , tb_no)
    except:
        return redirect('MakeBoardapp:detail_board' , tb_no)


def comment_updateurl(request, tb_no, c_no):

    request.session['update_c_no'] = c_no
    
    print(request.session['update_c_no'])

    return redirect('MakeBoardapp:detail_board' , tb_no)


def comment_update(request, c_no):
    
    if request.method == 'POST':
        comment = Total_Comment.objects.get(c_no=c_no)

        contents = request.POST.get('contents')
        tb_no = request.POST.get('tb_no')
        c_date = datetime.now()

        if contents:
            try:

                comment.contents = contents
                comment.c_date = c_date
                comment.save()

                del request.session['update_c_no']
                return redirect('MakeBoardapp:detail_board' , tb_no)

            except:
                return redirect('MakeBoardapp:detail_board' , tb_no)
        else:
            return redirect('MakeBoardapp:detail_board' , tb_no)





def scrap(request, tb_no, category):
    print('scrap', tb_no, category)
    writer=request.user.username
    check_scrap_board=Total_Scrap.objects.filter(tb_no=tb_no)

    if check_scrap_board.exists():
        check_scrap_board.delete()

    else:
        scrap=Total_Scrap.objects.create(tb_no_id=tb_no, writer=writer, category=category)
        scrap.save()

    return redirect('MakeBoardapp:detail_board',tb_no)



def like(request, tb_no):
    print('like')
    board = Total_Board.objects.get(tb_no=tb_no)
    writer=request.user.username
    check_like_board = Total_Like_Board.objects.filter(tb_no=tb_no)

    if check_like_board.exists():
        check_like_board.delete()
        board.like -= 1
        board.save()

    else:
        like=Total_Like_Board.objects.create(tb_no_id=tb_no, writer=writer)
        like.save()
        board.like += 1
        board.save()

    return redirect('MakeBoardapp:detail_board',tb_no)
