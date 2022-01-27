from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, HttpResponse
from .forms import UserForm
from Mainapp.models import Class_Board, Total_Comment, Total_Board
import datetime 
from django import forms
from .forms import CustomUserChangeForm
from django.contrib.auth.models import User


def home(request):
    board_list = Total_Board.objects.order_by('-view')[:3]
    dt_now = datetime.datetime.now()
    todays = dt_now.date()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
   
    today_class = Class_Board.objects.get(cb_date = todays)
    next_class = Class_Board.objects.get(cb_date = tomorrow)

    tb_no_list = [board_list[i].tb_no for i in range(3)]
    comment_cnt_list = []
    
    for tb_no in tb_no_list:
        comment_list = Total_Comment.objects.filter(tb_no = tb_no)
        comment_cnt = len(comment_list)
        comment_cnt_list.append(comment_cnt)
        
    board_list = list(zip(board_list, comment_cnt_list))

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
            u = form.save(commit=False)
            # 이메일
            username = form.cleaned_data.get('username')
            # 비밀번호
            raw_password = form.cleaned_data.get('password1')
            # 닉네임
            first_name = form.cleaned_data.get('first_name')
            # 프로필
            profile_path = request.FILES.get('last_name')
            if profile_path:  
                name = profile_path.name
                with open('media/%s' % name, 'wb') as file:
                    for chunk in profile_path.chunks():
                        file.write(chunk)
                u.last_name = name
                
            u.save()
            user = authenticate(username=username, password=raw_password, first_name=first_name, last_name=profile_path)
            login(request, user)
            # return render(request, 'Main/home.html')
            return redirect('Mainapp:home')
    else:
        form = UserForm()
    return render(request, 'Main/signup.html', {'form': form})


def profile_update(request):
    username = request.user.first_name
    path = "../../../media/"
    profile = request.user.last_name
    
    profile_path = path + profile
    
    if request.method == 'GET':
        context = {'currentname' : username, 
                   'currentprofile' : profile_path
                   }
        return render(request, 'Main/profile_update.html', context)

    elif request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            u = form.save(commit=False)
            current = User.objects.get(id=request.user.id)
           
            user = request.POST.get("first_name")
            if user:
                u.first_name = user
            else:
                u.first_name = current.first_name
                
            profile_path = request.FILES.get('last_name')
            
            if profile_path:  
                name = profile_path.name
                with open('media/%s' % name, 'wb') as file:
                    for chunk in profile_path.chunks():
                        file.write(chunk)
                u.last_name = name
            else:
                u.last_name = current.last_name
                
            u.save()
            
            return redirect('Boardapp:scrap_page')
        
        else:
            form = CustomUserChangeForm(instance=request.user)
        
        context = {
            'form':form,
        }
    
        return render(request, 'Main/profile_update.html')