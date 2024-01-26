from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from personal_list.models import SongRating

from .serializers import SongRatingSerializer
from .permissions import IsOwner


class SongRatingViewSet(viewsets.ModelViewSet):
    queryset = SongRating.objects.all()
    serializer_class = SongRatingSerializer
    permission_classes = [IsOwner]

    def create(self, request):
        permission_classes = [IsAuthenticated]
        return super().create(request)