from django.shortcuts import render

# Create your views here.
def board(request):
    return render(request, 'Board/board.html')

def solboard(request):
    return render(request, 'Board/solboard.html')

def scrap(request):
    return render(request, 'Board/scrap.html')
