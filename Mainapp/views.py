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
            u = form.save(commit=False)
            
            # 이메일
            username = form.cleaned_data.get('username')
            # 비밀번호
            raw_password = form.cleaned_data.get('password1')
            # 닉네임
            first_name = form.cleaned_data.get('first_name')
            # 프로필
            # profile_path = form.cleaned_data.get('last_name')
            # profile_path = request.FILES.get('last_name')
            profile_path = request.FILES.get('last_name')
            name = profile_path.name
            with open('media/%s' % name, 'wb') as file:
                for chunk in profile_path.chunks():
                    file.write(chunk)
            # profile_path = profile_image.value
            # upload_file = request.FILES.get('fileInput')
            # filepath = upload_file.name
            # profile_image = filepath
            # profile_image = upload(request)

            u.last_name = name
            u.save()
            user = authenticate(username=username, password=raw_password, first_name=first_name, last_name=profile_path)
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
    username = request.user.first_name
    profile = request.user.last_name
    
    login_session = request.session.get('login_session','')
    context = {'login_session': login_session}

    if request.method == 'GET':
        context = {'currentname' : username, 
                   'currentprofile' : profile
                   }
        return render(request, 'Main/profile_update.html', context)

    # elif request.method == 'POST':
    #     write_form = BoardPost(request.POST )
    #     if write_form.is_valid():
    #         board.tb_date = tb_date
    #         board.writer = writer
    #         board.title = write_form.title
    #         board.contents=write_form.contents
    #         category=write_form.category,
    #         type=write_form.type


    #         board.save()
           
    #         return redirect('MakeBoardapp:detail_board' , tb_no)

    #     else:
    #         context['forms'] = write_form
    #         if write_form.errors:
    #             for value in write_form.errors.values():
    #                 context['error'] = value
    #         return render(request, 'MakeBoard/writing_error.html', context)
    # return render(request, 'Main/profile_update.html')