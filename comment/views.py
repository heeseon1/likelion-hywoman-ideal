from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

def board_detail(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    comments = board.comment_set.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.board = board
            comment.save()
            return redirect('board_detail', board_id=board_id)
    else:
        form = CommentForm()
    return render(request, 'board_detail.html', {'board': board, 'comments': comments, 'form': form})

