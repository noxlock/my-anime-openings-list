from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('anime/', views.anime_listing, name='anime_listing'),
    path('anime/<str:id>', views.anime, name='anime detail'),
    path('song/<str:slug>', views.song, name='song detail'),
    path('random/', views.random_song, name='random_song'),
    path('top/', views.top_songs, name='top_songs'),
    path('search/', views.search),
]
