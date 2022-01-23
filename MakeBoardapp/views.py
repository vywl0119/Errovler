from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def reading(request):
    return render(request, 'MakeBoard/reading.html')
