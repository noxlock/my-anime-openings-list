from django.urls import path

from . import views

urlpatterns = [
    path('addtolist/', views.add_to_list, name='add_to_list'),
    path('deletefromlist/', views.delete_from_list, name='delete_from_list'),
    path('editrating/', views.edit_rating, name='edit_rating'),
]
