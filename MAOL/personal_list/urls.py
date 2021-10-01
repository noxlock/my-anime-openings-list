from django.urls import path

from . import views

urlpatterns = [
    path('<str:id>', views.profile, name='profile'),
    path('', views.profile, name='profile_no_id'),
]