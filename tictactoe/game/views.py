# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Game

def index(request):
    # Initialize or retrieve the game
    if 'game_id' not in request.session:
        game = Game.objects.create()
        request.session['game_id'] = game.id
    else:
        game = Game.objects.get(id=request.session['game_id'])

    # Handle a move
    if request.method == 'POST':
        position = int(request.POST.get('position'))
        if game.board[position] == ' ' and game.winner is None:
            board_list = list(game.board)
            board_list[position] = game.current_turn
            game.board = ''.join(board_list)
            game.current_turn = 'O' if game.current_turn == 'X' else 'X'
            game.winner = check_winner(game.board)
            game.save()

    context = {
        'game': game,
        'board': game.board,
        'winner': game.winner,
    }
    return render(request, 'game/index.html', context)

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    if ' ' not in board:
        return 'Tie'
    return None

