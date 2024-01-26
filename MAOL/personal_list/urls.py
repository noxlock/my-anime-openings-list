from django.urls import path

from . import views

urlpatterns = [
    path('<str:id>/', views.profile, name='profile'),
    path('<str:id>/list/', views.list, name='list'),
    path('', views.profile, name='profile_no_id'),
]
