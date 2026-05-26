from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Game, LibraryItem


def game_list(request):
    games = Game.objects.all().order_by('-created_at')

    return render(request, 'games/game_list.html', {'games': games})


def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)

    is_in_library = False

    if request.user.is_authenticated:
        is_in_library = LibraryItem.objects.filter(user=request.user, game=game).exists()

    return render(
        request,
        'games/game_detail.html',
        {
            'game': game,
            'is_in_library': is_in_library,
        }
    )


@login_required
def add_to_library(request, pk):
    game = get_object_or_404(Game, pk=pk)

    LibraryItem.objects.get_or_create(user=request.user, game=game)

    messages.success(request, f'{game.title} has been added to your library.')
    return redirect('game_detail', pk=game.pk)


@login_required
def library_view(request):
    library_items = LibraryItem.objects.filter(user=request.user).select_related('game')

    return render(request, 'games/library.html', {'library_items': library_items})


@login_required
def remove_from_library(request, pk):
    game = get_object_or_404(Game, pk=pk)

    LibraryItem.objects.filter(user=request.user, game=game).delete()

    messages.success(request, f'{game.title} has been removed from your library.')
    return redirect('library')