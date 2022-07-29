from django.shortcuts import render
from django.http import HttpResponseNotFound

from home.models import Anime, Song
from .serializers import song_serializer


def index(request):
    qs = Song.get_top_songs(20).values('video_link', 'anime__cover', 'pk')

    qs_json = song_serializer(qs)

    return render(request, 'home/index.html', {'songs': qs_json})


def anime_listing(request):
    qs = Anime.objects.values('english_name', 'cover', 'pk')[:100]

    qs_json = song_serializer(qs)
    return render(request, 'home/anime_listing.html', {'animes': qs_json})


def anime(request, id):
    if id:
        try:
            anime = Anime.objects.filter(pk=id).values(
                'english_name',
                'cover',
                'pk'
            )

        except Anime.DoesNotExist:
            return HttpResponseNotFound('<h1>Anime not found</h1>')
        else:
            songs = Song.objects.filter(anime=id).values(
                'song_type', 'number', 'name', 'video_link', 'pk'
            )
            songs = song_serializer(songs)
            anime = song_serializer(anime)

            return render(
                request,
                'home/anime.html',
                {'anime': anime, 'songs': songs}
            )


def song(request, slug):
    if slug:
        try:
            slug = slug.split('-')
            print(slug)
            song = Song.objects.filter(
                anime__slug_name=slug[0],
                song_type=slug[1],
                number=slug[2]
            ).values(
                'name',
                'video_link',
                'anime__english_name',
                'song_type',
                'number',
                'pk'
            )

        except Song.DoesNotExist:
            return HttpResponseNotFound('<h1>Song not found</h1>')
        else:
            song = song_serializer(song)

            return render(
                request,
                'home/song.html',
                {'song': song}
            )
