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
    
    context = {'board_detail': board_detail,
                'comment_list': comment_list,
                'comment_cnt': comment_cnt,
                
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



def writing(request):
    return render(request, 'MakeBoard/writing.html')



def qna_board_write(request):
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
            total_board = Total_Board(
                title=write_form.title,
                contents=write_form.contents,
                writer =writer,
                category=write_form.category,
                type=write_form.type
            )
            total_board.save()
            return redirect('/Board/qna_board')
        else:
            context['forms'] = write_form
            if write_form.errors:
                for value in write_form.errors.values():
                    context['error'] = value
            return render(request, 'MakeBoard/writing_error.html', context)

def sol_board_write(request):
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
            total_board = Total_Board(
                title=write_form.title,
                contents=write_form.contents,
                writer =writer,
                category=write_form.category,
                type=write_form.type
            )
            total_board.save()
            return redirect('/Board/sol_board')
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
                username = request.user.first_name
                comment = Total_Comment.objects.create(tb_no_id=tb_no, contents=contents, writer = username)
                comment.save()
               
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
    writer=request.user.first_name
    scrap=Total_Scrap.objects.create(tb_no_id=tb_no, writer=writer, category=category)
    print('이유이상')
    scrap.save()
    return redirect('MakeBoardapp:detail_board',tb_no)


def scrap(request, tb_no, category):
    print('scrap', tb_no, category)
    writer=request.user.first_name
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
    writer=request.user.first_name
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




    
def qna_like(request, qna_no):
    print('qna_like')
    qna_board = QnA_Board.objects.get(qna_no=qna_no)
    writer=request.user.first_name
    check_like_board = Like_Board.objects.filter(qna_no=qna_no)

    if check_like_board.exists():
        check_like_board.delete()
        qna_board.like -= 1
        qna_board.save()

    else:
        like=Like_Board.objects.create(qna_no_id=qna_no, writer=writer)
        like.save()
        qna_board.like += 1
        qna_board.save()

    return redirect('MakeBoardapp:qna_detail_board',qna_no)


def sole_like(request, b_no):
    print('sol_like')
    board = Board.objects.get(b_no=b_no)
    writer=request.user.first_name
    check_like_board = Like_Board.objects.filter(b_no=b_no)

    if check_like_board.exists():
        check_like_board.delete()
        board.like -= 1
        board.save()

    else:
        like=Like_Board.objects.create(b_no_id=b_no, writer=writer)
        like.save()
        board.like += 1
        board.save()

    return redirect('MakeBoardapp:sol_detail_board',b_no)



