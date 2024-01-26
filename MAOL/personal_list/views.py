from django.core.serializers import serialize
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound

from .models import Profile

from home.serializers import song_serializer

from utils.views import get_list


def profile(request, id=None):
    # If an id is passed in, display the user's profile (if exists)
    if id:
        user = User.objects.filter(username=id)

        if user.exists():

            # This profile has to stay a queryset to be serialized nicely.
            profile = Profile.objects.filter(user=user[0])
            json_profile = serialize('json', profile)

            # Get the top rated, and recently rated songs of the user,
            # Serializing the querysets as well.
            topRated = song_serializer(profile[0].get_top_ratings(20).values(
                'video_link',
                'name',
                'detail_link',
                'song_type',
                'number',
                'anime__english_name',
                'anime__cover',
                'anime__pk',
                'pk'
            ))

            context = {
                'profile': json_profile,
                'topRated': topRated,
                'list': get_list(request),
                'id': id
            }

            return render(request, 'profile.html', context)

        # If no user was found, display an error
        else:
            return HttpResponseNotFound(f"<h1>User {id} not found</h1>")

    # if an id is not given, try displaying the logged in user's profile
    elif not id and request.user.is_authenticated:
        return redirect(f'/profile/{request.user.username}/')

    # if no user is logged in, redirect to login page
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


def list(request, id=None):
    user = User.objects.filter(username=id)

    if user.exists():
        profile = Profile.objects.filter(user=user[0])

        ratings = song_serializer(profile[0].get_rated_songs())
        json_profile = serialize('json', profile)

        # Pass the following to the template:
        # profile (for banner & picture)
        # ratings (for their list)
        # id (for certain display conditions)
        context = {
            'profile': json_profile,
            'ratings': ratings,
            'list': get_list(request),
            'id': id
        }
        return render(request, 'list.html', context)

    else:
        return HttpResponseNotFound(f"<h1>User not found</h1>")
