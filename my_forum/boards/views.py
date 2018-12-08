from django.shortcuts import render
from boards.models import Board


def index(request):
    boards = Board.objects.all()
    return render(request, 'index.html', {'boards': boards})

