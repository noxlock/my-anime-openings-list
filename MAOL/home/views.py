from django.shortcuts import render

from home.models import Song
from .serializers import song_serializer


def index(request):
    qs = Song.get_top_songs(20).values('video_link', 'anime__cover', 'pk')

    qs_json = song_serializer(qs)

    return render(request, 'home/index.html', {'songs': qs_json})
