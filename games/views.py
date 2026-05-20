from django.shortcuts import render


def game_list(request):
    games = [
        {
            'title': 'Cyberpunk 2077',
            'genre': 'RPG',
            'price': '59.99',
            'tag': 'Hot',
        },
        {
            'title': 'Minecraft',
            'genre': 'Sandbox',
            'price': '29.99',
            'tag': 'Popular',
        },
        {
            'title': 'Terraria',
            'genre': 'Adventure',
            'price': '9.99',
            'tag': 'Sale',
        },
        {
            'title': 'Stardew Valley',
            'genre': 'Simulation',
            'price': '14.99',
            'tag': 'New',
        },
    ]

    return render(request, 'games/game_list.html', {'games': games})