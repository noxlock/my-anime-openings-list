from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'ratings', views.SongRatingViewSet, basename="rating")

urlpatterns = [
    path('', include(router.urls))
    # path('addtolist/', views.add_to_list, name='add_to_list'),
    # path('deletefromlist/', views.delete_from_list, name='delete_from_list'),
    # path('editrating/', views.edit_rating, name='edit_rating'),
]
