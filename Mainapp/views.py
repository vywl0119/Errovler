from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm

def home(request):
    return render(request, 'Main/home.html')

def signup(request):
    return render(request, 'Main/signup.html')

def login(request):
    return render(request, 'Main/login.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main:login')
    else:
        form = UserForm()
    return render(request, 'main/signup.html', {'form': form})