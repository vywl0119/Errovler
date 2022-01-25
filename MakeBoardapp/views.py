from unicodedata import category
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from matplotlib.style import context

from .forms import BoardPost
from Mainapp.models import Board, Comment, Scrap
from django.contrib.auth.models import User
from django.utils import timezone


def reading(request):
    return render(request, 'MakeBoard/reading.html')

def board_detail(request):
    return render(request, 'MakeBoard/reading.html')

def writing(request):
    return render(request, 'MakeBoard/writing.html')


def board_write(request):
    login_session = request.session.get('login_session','')
    context = {'login_session': login_session}

    if request.method == 'GET':
        write_form = BoardPost()
        context['forms'] = write_form
        return render(request, 'MakeBoard/writing.html', context)

    elif request.method == 'POST':
        write_form = BoardPost(request.POST)
        if write_form.is_valid():
            writer = request.user.username
            board = Board(
                title=write_form.title,
                contents=write_form.contents,
                writer =writer,
                category=write_form.category
            )
            board.save()
            return redirect('/Board/board')
        else:
            context['forms'] = write_form
            if write_form.errors:
                for value in write_form.errors.values():
                    context['error'] = value
            return render(request, 'MakeBoard/writing_error.html', context)


def comment(request):
    if request.method == 'POST':
        contents = request.POST.get('contents')
        b_no = request.POST.get('b_no')
        print(contents, b_no)

    try:
        username = request.user.username
        comment = Comment.objects.create(b_no_id=b_no, contents=contents, writer = username)
        comment.save()
        return render(request, 'Main/home.html')

    except:
        return render(request, 'MakeBoard/reading.html')

    return render(request, 'MakeBoard/writing.html')

# def scrap(request):
#      if request.method == 'POST':
#          b_no=request.POST.get('b_no')
#          qna_no=request.POST.get('qna_no')
    
#      try:
#         username=request.user.username
#         scrap=Scrap.objects.create(b_no=b_no, qna_no=qna_no)
#         scrap.save()
#         return render(request,'MakeBoard/reading.html')
#      except:
#          return render(request,'Main/home.html')



#      return render(request,'MakeBoard/reading.html')