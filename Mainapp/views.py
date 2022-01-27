from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, HttpResponse
from .forms import UserForm
from Mainapp.models import Class_Board, Total_Comment, Total_Board
import datetime 

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
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            profile_image = form.cleaned_data.get('fileInput')
            # upload_file = request.FILES.get('fileInput')
            # filepath = upload_file.name
            # profile_image = filepath
            # profile_image = upload(request)

            user = authenticate(username=username, password=raw_password, first_name=first_name, email=profile_image)
            login(request, user)
            return render(request, 'Main/login.html')
    else:
        form = UserForm()
    return render(request, 'Main/signup.html', {'form': form})

def upload(request):
    # if request.method == 'POST':
        upload_file = request.FILES.get('fileInput') # 파일 객체
        name = upload_file.name # 파일 이름
        size = upload_file.size # 파일 크기
        
        return name
        
    #     with open(name, 'wb') as file: # 파일 저장
    #         for chunk in upload_file.chunks():
    #             file.write(chunk)
                
    #     return HttpResponse('%s<br>%s' % (name, size))
    
    # return render(request, 'Main/signup.html')

def profile_update(request):
    return render(request, 'Main/profile_update.html')