from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import BoardPost
from Mainapp.models import Board
from Mainapp.models import Member

def reading(request):
    return render(request, 'MakeBoard/reading.html')

def writing(request):
    return render(request, 'MakeBoard/writing.html')

def board_write(request):
    login_session = request.session.get('login_session','')
    context = {'login_session', login_session}

    if request.method == 'GET':
        write_form = BoardPost()
        context['forms'] = write_form
        return render(request, 'MakeBoardapp/writing.html', context)

    elif request.method == 'POST':
        write_form = BoardPost(request.POST)

        if write_form.is_valid():
            writer = Member.objects.get(user_id=login_session)
            board = Board(
                title=write_form.title,
                contents=write_form.contents,
                id=writer,
                category=write_form.category
            )
            board.save()
            return redirect('/board')
        else:
            context['forms'] = write_form
            if write_form.errors:
                for value in write_form.errors.values():
                    context['error'] = value
            return render(request, 'MakeBoardapp/writing.html', context)