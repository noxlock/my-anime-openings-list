import json

from django.shortcuts import render

from home.models import Song


def index(request):
    qs = Song.objects.values('video_link', 'anime__cover', 'pk').order_by('anime__english_name')[:20]

    qs_json = json.dumps(list(qs))

    return render(request, 'home/index.html', {'songs': qs_json})
