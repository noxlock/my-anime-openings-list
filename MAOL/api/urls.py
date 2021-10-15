from django.urls import path

from . import views

urlpatterns = [
    path('addtolist/', views.add_to_list, name='add_to_list'),
]
