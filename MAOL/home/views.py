from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from home.models import Anime, Song

from .serializers import song_serializer

from random import randint


def index(request):
    qs = Song.objects.get_top_songs().values(
        'video_link',
        'name',
        'detail_link',
        'song_type',
        'number',
        'anime__english_name',
        'anime__cover',
        'pk'
    )

    qs_json = song_serializer(qs)

    return render(request, 'home/index.html', {'songs': qs_json})


def anime_listing(request):
    qs = Anime.objects.values('english_name', 'cover', 'pk')

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
                'detail_link', 'song_type', 'number',
                'name', 'video_link', 'pk'
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
            song = Song.objects.filter(
                anime__slug_name=slug[0],
                song_type=slug[1],
                number=slug[2]
            ).values(
                'name',
                'video_link',
                'anime__english_name',
                'anime__pk',
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


def random_song(request):
    first = Song.objects.first().pk
    last = Song.objects.last().pk

    rand = randint(first, last)
    song = Song.objects.get(pk=rand)

    return redirect(
        f'/song/{song.anime.slug_name}-{song.song_type}-{song.number}'
    )


def top_songs(request):
    qs = Song.objects.get_top_songs().values(
        'anime__cover',
        'anime__english_name',
        'anime__pk',
        'detail_link',
        'song_type',
        'number',
        'name',
        'video_link',
        'pk'
    )

    qs_json = song_serializer(qs)
    return render(request, 'home/top_songs.html', {'songs': qs_json})


def search(request):
    query = request.GET.get('q')
    if query:
        anime_res = song_serializer(Anime.objects.search(query).values(
            'english_name',
            'cover',
            'pk'
        ))
        song_res = song_serializer(Song.objects.search(query).values(
            'anime__cover',
            'anime__english_name',
            'anime__pk',
            'detail_link',
            'song_type',
            'number',
            'name',
            'video_link',
            'pk'
        ))

        context = {
            'anime': anime_res,
            'songs': song_res,
            'query': query
        }

        return render(request, 'home/search.html', context)
    else:
        return HttpResponse('<h1> No Search Entered </h1>')
