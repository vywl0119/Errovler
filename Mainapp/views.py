from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm

def home(request):
    return render(request, 'Main/home.html')


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