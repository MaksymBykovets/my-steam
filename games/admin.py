from django.contrib import admin
from .models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'developer', 'price', 'release_date')
    search_fields = ('title', 'genre', 'developer')
    list_filter = ('genre', 'release_date')