from django.shortcuts import render, get_object_or_404
from boards.models import Board


def index(request):
    boards = Board.objects.all()
    return render(request, 'index.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})

