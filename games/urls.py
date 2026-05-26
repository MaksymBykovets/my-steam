from django.urls import path
from . import views


urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('library/', views.library_view, name='library'),
    path('<int:pk>/', views.game_detail, name='game_detail'),
    path('<int:pk>/add-to-library/', views.add_to_library, name='add_to_library'),
    path('<int:pk>/remove-from-library/', views.remove_from_library, name='remove_from_library'),
]