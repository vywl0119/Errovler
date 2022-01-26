from unicodedata import category
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
import datetime

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from matplotlib.style import context

from .forms import BoardPost
from Mainapp.models import Board, Comment
from django.contrib.auth.models import User
from django.utils import timezone

from Mainapp.models import Board
from Mainapp.models import QnA_Board

def qna_detail_board(request, qna_no):
    board_detail = QnA_Board.objects.get(qna_no = qna_no)
    comment_list = Comment.objects.filter(qna_no = qna_no)
    comment_cnt = len(comment_list)

    context = {'board_detail': board_detail,
                'comment_list': comment_list,
                'comment_cnt': comment_cnt,
                }
    return render(request, 'MakeBoard/qna_reading.html',context)



def sol_detail_board(request, b_no):
    board_detail = Board.objects.get(b_no = b_no)
    comment_list = Comment.objects.filter(b_no = b_no)
    comment_cnt = len(comment_list)
 
    context = {'board_detail': board_detail,
                'comment_list':comment_list,
                'comment_cnt':comment_cnt,
                }
    return render(request, 'MakeBoard/sol_reading.html',context)



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
            board = QnA_Board(
                title=write_form.title,
                contents=write_form.contents,
                writer =writer,
                category=write_form.category
            )
            board.save()
            return redirect('/Board/qna_board')
        else:
            context['forms'] = write_form
            if write_form.errors:
                for value in write_form.errors.values():
                    context['error'] = value
            return render(request, 'MakeBoard/writing_error.html', context)



def solboard_write(request):
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
            board = Board(
                title=write_form.title,
                contents=write_form.contents,
                writer =writer,
                category=write_form.category
            )
            board.save()
            return redirect('/Board/sol_board')
        else:
            context['forms'] = write_form
            if write_form.errors:
                for value in write_form.errors.values():
                    context['error'] = value
            return render(request, 'MakeBoard/writing_error.html', context)




def qna_comment(request):
    print('qna')
    if request.method == 'POST':
        contents = request.POST.get('contents')
        qna_no = request.POST.get('qna_no')
        print(qna_no, contents)
        if contents:
            try:
                print(contents)
                username = request.user.first_name
                comment = Comment.objects.create(qna_no_id=qna_no, contents=contents, writer = username)
                comment.save()
                return redirect('MakeBoardapp:qna_detail_board' , qna_no)

            except:
                return redirect('MakeBoardapp:qna_detail_board' , qna_no)
        else:
            return redirect('MakeBoardapp:qna_detail_board' , qna_no)



def sol_comment(request):
    print('sol')
    if request.method == 'POST':
        contents = request.POST.get('contents')
        b_no = request.POST.get('b_no')
        
        if contents:
            try:
                print(contents)
                username = request.user.first_name
                comment = Comment.objects.create(b_no_id=b_no, contents=contents, writer = username)
                comment.save()
                return redirect('MakeBoardapp:sol_detail_board' , b_no)

            except:
                return redirect('MakeBoardapp:sol_detail_board' , b_no)
        else:
            return redirect('MakeBoardapp:sol_detail_board' , b_no)




# def photoboard(request):
#     portfolios = Portfolio.objects
#     return render(request, 'portfolio/portfolio.html', {'portfolios': portfolios})





def sol_delete(request, b_no):
    try:
        board = Board.objects.get(b_no=b_no)
        board.delete()
        return redirect('Boardapp:sol_board')
    except:
        return redirect('MakeBoardapp:sol_detail_board' , b_no)


def qna_delete(request, qna_no):
    try:
        qna_board = QnA_Board.objects.get(qna_no=qna_no)

        qna_board.delete()
        return redirect('Boardapp:qna_board')
    except:
        return redirect('MakeBoardapp:qna_detail_board' , qna_no)





def sol_comment_delete(request, b_no, c_no):
    try:
      
        comment = Comment.objects.get(c_no=c_no)
        comment.delete()
        return redirect('MakeBoardapp:sol_detail_board' , b_no)
    except:
        return redirect('MakeBoardapp:sol_detail_board' , b_no)


def sol_comment_updateurl(request, b_no, c_no):

    request.session['update_c_no'] = c_no
    
    print(request.session['update_c_no'])

    return redirect('MakeBoardapp:sol_detail_board' , b_no)


def sol_comment_update(request, c_no):
    
    if request.method == 'POST':
        comment = Comment.objects.get(c_no=c_no)

        contents = request.POST.get('contents')
        b_no = request.POST.get('b_no')
        print(contents, b_no)
        c_date = datetime.datetime.now()

        if contents:
            try:

                comment.contents = contents
                comment.c_date = c_date
                comment.save()

                del request.session['update_c_no']
                return redirect('MakeBoardapp:sol_detail_board' , b_no)

            except:
                return redirect('MakeBoardapp:sol_detail_board' , b_no)
        else:
            return redirect('MakeBoardapp:sol_detail_board' , b_no)





def qna_comment_delete(request, qna_no, c_no):
    try:
      
        comment = Comment.objects.get(c_no=c_no)
        comment.delete()
        return redirect('MakeBoardapp:qna_detail_board' , qna_no)
    except:
        return redirect('MakeBoardapp:qna_detail_board' , qna_no)


def qna_comment_updateurl(request, qna_no, c_no):

    request.session['update_c_no'] = c_no
    
    print(request.session['update_c_no'])

    return redirect('MakeBoardapp:qna_detail_board' , qna_no)


def qna_comment_update(request, c_no):
    if request.method == 'POST':
        comment = Comment.objects.get(c_no=c_no)

        contents = request.POST.get('contents')
        qna_no = request.POST.get('qna_no')
        c_date = datetime.datetime.now()

        if contents:
            try:

                comment.contents = contents
                comment.c_date = c_date
                comment.save()

                del request.session['update_c_no']
                return redirect('MakeBoardapp:qna_detail_board' , qna_no)

            except:
                return redirect('MakeBoardapp:qna_detail_board' , qna_no)
        else:
            return redirect('MakeBoardapp:qna_detail_board' , qna_no)
            # return render(request, 'MakeBoard/writing.html')

