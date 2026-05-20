from django.shortcuts import render
from .models import Game


def game_list(request):
    games = Game.objects.all().order_by('-created_at')

    return render(request, 'games/game_list.html', {'games': games})