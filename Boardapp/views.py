from django.shortcuts import render

# Create your views here.
def board(request):
    return render(request, 'Board/board.html')

def scrap(request):
    return render(request, 'Board/scrap.html')
