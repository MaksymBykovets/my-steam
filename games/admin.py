from django.contrib import admin
from .models import Game, LibraryItem


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'developer', 'price', 'release_date')
    search_fields = ('title', 'genre', 'developer')
    list_filter = ('genre', 'release_date')


@admin.register(LibraryItem)
class LibraryItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'added_at')
    search_fields = ('user__username', 'game__title')
    list_filter = ('added_at',)