from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'Main/home.html')

def signup(request):
    return render(request, 'Main/signup.html')

