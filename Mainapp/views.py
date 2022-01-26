from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm
from Mainapp.models import Board, Class_Board, Comment
import datetime 






def home(request):
    board_list = Board.objects.order_by('-view')[:5]
    dt_now = datetime.datetime.now()
    todays = dt_now.date()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
   
    today_class = Class_Board.objects.get(cb_date = todays)
    next_class = Class_Board.objects.get(cb_date = tomorrow)
    


    context = {'board_list': board_list,
                'today_class':today_class,
                'next_class':next_class,
                }

    return render(request, 'Main/home.html',context)



def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        print('d')
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')

            user = authenticate(username=username, password=raw_password, first_name=first_name)
            login(request, user)
            return render(request, 'Main/login.html')
    else:
        form = UserForm()
    return render(request, 'Main/signup.html', {'form': form})