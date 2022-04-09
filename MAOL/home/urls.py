from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('anime/', views.anime_listing, name='anime_listing'),
    path('anime/<str:id>', views.anime, name='anime'),
]
