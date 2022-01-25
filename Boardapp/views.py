from django.shortcuts import render
from Mainapp.models import Board

# Create your views here.
def board(request):
    boards = Board.objects
    return render(request, 'Board/board.html', {'boards' : boards})

def solboard(request):
    return render(request, 'Board/solboard.html')

def scrap(request):
    return render(request, 'Board/scrap.html')
