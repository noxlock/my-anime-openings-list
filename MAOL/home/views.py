from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse

from home.models import Song

def index(request):
    qs = Song.objects.all()
    qs_json = serializers.serialize('json', qs)
    return render(request, 'home/index.html', {'songs': qs_json})
