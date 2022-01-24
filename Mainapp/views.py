from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Member

# Create your views here.
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'Main/home.html')


def login(request):
    return render(request, 'Main/login.html')

def signup(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        nickname = request.POST.get('nickname')
        m = Member(
        id=id, pw=pw, nickname=nickname)

        m.save()
        return render(request, 'Main/login.html')
    else:
        return render(request, 'Main/signup.html')